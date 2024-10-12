

# BatchOperationMetadata

Metadata describing the Batch operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**batch** | **String** | Name of the batch for the operation. |  [optional] |
|**batchUuid** | **String** | Batch UUID for the operation. |  [optional] |
|**createTime** | **String** | The time when the operation was created. |  [optional] |
|**description** | **String** | Short description of the operation. |  [optional] |
|**doneTime** | **String** | The time when the operation finished. |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Labels associated with the operation. |  [optional] |
|**operationType** | [**OperationTypeEnum**](#OperationTypeEnum) | The operation type. |  [optional] |
|**warnings** | **List&lt;String&gt;** | Warnings encountered during operation execution. |  [optional] |



## Enum: OperationTypeEnum

| Name | Value |
|---- | -----|
| BATCH_OPERATION_TYPE_UNSPECIFIED | &quot;BATCH_OPERATION_TYPE_UNSPECIFIED&quot; |
| BATCH | &quot;BATCH&quot; |



