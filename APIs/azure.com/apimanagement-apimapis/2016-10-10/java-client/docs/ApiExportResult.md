

# ApiExportResult

The response model for the export API output operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**content** | **byte[]** | Response content bytes. |  [optional] |
|**requestId** | **String** |  |  [optional] |
|**statusCode** | [**StatusCodeEnum**](#StatusCodeEnum) |  |  [optional] |



## Enum: StatusCodeEnum

| Name | Value |
|---- | -----|
| CONTINUE | &quot;Continue&quot; |
| OK | &quot;OK&quot; |
| CREATED | &quot;Created&quot; |
| ACCEPTED | &quot;Accepted&quot; |
| NOT_FOUND | &quot;NotFound&quot; |
| CONFLICT | &quot;Conflict&quot; |



