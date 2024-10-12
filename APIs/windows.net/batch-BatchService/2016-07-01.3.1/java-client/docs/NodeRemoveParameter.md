

# NodeRemoveParameter


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nodeDeallocationOption** | [**NodeDeallocationOptionEnum**](#NodeDeallocationOptionEnum) | The default value is requeue. |  [optional] |
|**nodeList** | **List&lt;String&gt;** |  |  |
|**resizeTimeout** | **String** | The default value is 15 minutes. The minimum value is 5 minutes. If you specify a value less than 5 minutes, the Batch service returns an error; if you are calling the REST API directly, the HTTP status code is 400 (Bad Request). |  [optional] |



## Enum: NodeDeallocationOptionEnum

| Name | Value |
|---- | -----|
| REQUEUE | &quot;requeue&quot; |
| TERMINATE | &quot;terminate&quot; |
| TASKCOMPLETION | &quot;taskcompletion&quot; |
| RETAINEDDATA | &quot;retaineddata&quot; |



