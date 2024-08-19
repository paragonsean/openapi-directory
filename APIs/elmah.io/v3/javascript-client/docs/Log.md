# ElmahIoApi.Log

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **String** | Color of the log. The color will always be one of the following (green being the default):  green, lightgreen, lime, yellow, orange, deeporange, red, pink, purple, deeppurple, blue, lightblue | [optional] 
**disabled** | **Boolean** | Returns true if the log is currently disabled. A log can be disabled either through the API  or in the elmah.io UI. | [optional] 
**environmentName** | **String** | Environment name this log is in or \&quot;Other\&quot; if not in an environment.  \&quot;Other\&quot; is chosen over null to mimic the experience in the elmah.io UI. | [optional] 
**id** | **String** | ID of the log. | [optional] 
**name** | **String** | Name of the log. | [optional] 


