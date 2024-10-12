

# TaskAddResult


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**eTag** | **String** |  |  [optional] |
|**error** | [**BatchError**](BatchError.md) |  |  [optional] |
|**lastModified** | **OffsetDateTime** |  |  [optional] |
|**location** | **String** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  |
|**taskId** | **String** |  |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| SUCCESS | &quot;success&quot; |
| CLIENT_ERROR | &quot;clientError&quot; |
| SERVER_ERROR | &quot;serverError&quot; |
| UNMAPPED | &quot;unmapped&quot; |



