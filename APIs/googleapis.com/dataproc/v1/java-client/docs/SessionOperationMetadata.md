

# SessionOperationMetadata

Metadata describing the Session operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | The time when the operation was created. |  [optional] |
|**description** | **String** | Short description of the operation. |  [optional] |
|**doneTime** | **String** | The time when the operation was finished. |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Labels associated with the operation. |  [optional] |
|**operationType** | [**OperationTypeEnum**](#OperationTypeEnum) | The operation type. |  [optional] |
|**session** | **String** | Name of the session for the operation. |  [optional] |
|**sessionUuid** | **String** | Session UUID for the operation. |  [optional] |
|**warnings** | **List&lt;String&gt;** | Warnings encountered during operation execution. |  [optional] |



## Enum: OperationTypeEnum

| Name | Value |
|---- | -----|
| SESSION_OPERATION_TYPE_UNSPECIFIED | &quot;SESSION_OPERATION_TYPE_UNSPECIFIED&quot; |
| CREATE | &quot;CREATE&quot; |
| TERMINATE | &quot;TERMINATE&quot; |
| DELETE | &quot;DELETE&quot; |



