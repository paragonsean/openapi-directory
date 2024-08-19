# ElmahIoApi.CreateLog

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **String** | Color of the log. The color must be one of the following (green on unknown value or missing):  green, lightgreen, lime, yellow, orange, deeporange, red, pink, purple, deeppurple, blue, lightblue | [optional] 
**disabled** | **Boolean** | Set to true to disable the log on creation. Defaults to false. A log can be enabled/disabled  afterwards by calling the _disable and _enable endpoints. | [optional] 
**environmentName** | **String** | Environment name of the new log. Must match an environment name (case insensitive).  If a matching environment name was not found or the property is not set, the log  will appear under \&quot;Other\&quot; in the UI. | [optional] 
**name** | **String** | Name of the new log. | 


