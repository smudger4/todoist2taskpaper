import json
import argparse
import logging
from todoist_api_python.api import TodoistAPI

log = logging.getLogger("todoist2taskpaper")

def load_secrets():
  # load secrets from file
  with open("secrets.json") as json_file:
      imported_secrets = json.load(json_file)

  log.debug("secrets: '%s'" % json.dumps(imported_secrets, indent=4))

  return imported_secrets
  
def get_projects(api):
  projects = api.get_projects()
  log.debug(projects)
  return projects
  
def get_tasks(api, p_id=None):
  tasks = api.get_tasks(project_id=p_id)
  log.debug(tasks)
  return tasks


def main(debug_flag):
  if (debug_flag):
      logging.basicConfig(level=logging.DEBUG)
  else:
      logging.basicConfig(level=logging.INFO)

  # load the api key from the secrets file & use it to create the Todoist API instance
  try:
    secrets_dict = load_secrets()
    api = TodoistAPI(secrets_dict["TODOIST_API_KEY"])
  except Exception as error:
    log.error(error)
    exit(1)
    
  # step through each project in turn and extract associated tasks  
  projects = get_projects(api)
  for project in projects:
    # taskpaper format project 
    print("%s:" % project.name)
    
    tasks = get_tasks(api, project.id)
    for task in tasks:
      # taskpaper format task - incorporate due date if set
      if task.due != None:
        if task.due.is_recurring == True:
          # just set a tag & print out the Todoist recurrance rule rather than trying to convert it
          print("- %s @parallel(true) @autodone(false) @due(%s) @tags(repeat-rule-needs-attention)" % (task.content, task.due.date))
          print("repeat-rule %s" % task.due.string)
        else:
          print("- %s @parallel(true) @autodone(false) @due(%s)" % (task.content, task.due.date))
      else:
        print("- %s @parallel(true) @autodone(false)" % (task.content))
      
      print(task.description)
      print("Migrated from Todoist: %s" % task.url) # link to original task in Todoist
      print("")
        

if __name__ == "__main__":
    # parse command line args
    # Create the command line parser
    my_parser = argparse.ArgumentParser(description='Migrate todoist to onmifocus') 

    # Add the arguments
    # optional
    my_parser.add_argument('-d', '--debug', action='store_true', help='Debug level logging')

    # parse command line
    args = my_parser.parse_args()

    # pass args to main routine & run it
    main(args.debug)
