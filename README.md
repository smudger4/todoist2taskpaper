# todoist2taskpaper
Retrieve projects &amp; tasks from [Todoist](https://todoist.com) in [TaskPaper](https://guide.taskpaper.com/getting-started/) format.
Written to smooth a migration from Todoist to [Omnifocus](https://www.omnigroup.com/omnifocus), which can [use TaskPaper as an intermediate format](https://support.omnigroup.com/omnifocus-taskpaper-reference/).

## Getting started

### Set up secrets

Rename the ```secrets-template.json``` file as ```secrets.json``` and overwrite the placeholder string with your Todoist API key, found in the Todoist [integration settings view](https://todoist.com/prefs/integrations).

### Install dependencies

```pip3 install -r requirements.txt```


### Run it

```python3 app.py > output.txt```


### (optional) Add to Omnifocus

Simply copy & paste the contents of ```output.txt``` into the Projects perspective in Omnifocus. Note that Todoist treats the Inbox as just another project, so you may want to handle the Inbox section of the file separately from the rest, pasting this section directly into the Inbox perspective.

Note that rather than attempt to parse the (quite sophisticated) syntax Todoist uses for date recurrence patterns, I've cheated and just created a tag for when a recurring task is detected, to allow these to be fixed up later in Omnifocus.
