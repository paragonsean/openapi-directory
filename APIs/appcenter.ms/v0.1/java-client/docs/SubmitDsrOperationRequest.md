

# SubmitDsrOperationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** |  |  [optional] |
|**appId** | **String** |  |  [optional] |
|**operationId** | **String** | The DSR operation ID provided by the GDPR coordinator. Used for tracking only. |  [optional] |
|**request** | [**RequestEnum**](#RequestEnum) |  |  [optional] |
|**requestId** | **String** | Request ID provided by the GDPR coordinator. Used for tracking. |  [optional] |



## Enum: RequestEnum

| Name | Value |
|---- | -----|
| DELETE | &quot;Delete&quot; |
| PURGE | &quot;Purge&quot; |
| UNDO_DELETE | &quot;UndoDelete&quot; |
| EXPORT | &quot;Export&quot; |



