

# TaskAddResult


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**eTag** | **String** | You can use this to detect whether the task has changed between requests. In particular, you can be pass the ETag with an Update Task request to specify that your changes should take effect only if nobody else has modified the job in the meantime. |  [optional] |
|**error** | [**BatchError**](BatchError.md) |  |  [optional] |
|**lastModified** | **OffsetDateTime** |  |  [optional] |
|**location** | **String** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  |
|**taskId** | **String** |  |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| SUCCESS | &quot;success&quot; |
| CLIENTERROR | &quot;clienterror&quot; |
| SERVERERROR | &quot;servererror&quot; |



