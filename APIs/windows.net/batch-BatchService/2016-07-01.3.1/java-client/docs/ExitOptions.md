

# ExitOptions


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**jobAction** | [**JobActionEnum**](#JobActionEnum) | The default is none for exit code 0 and terminate for all other exit conditions. It is an error to specify this if the job&#39;s onTaskFailed is noAction. The add task request fails with an invalid property value error; if you are calling the REST API directly, the HTTP status code is 400 (Bad Request). |  [optional] |



## Enum: JobActionEnum

| Name | Value |
|---- | -----|
| NONE | &quot;none&quot; |
| DISABLE | &quot;disable&quot; |
| TERMINATE | &quot;terminate&quot; |



