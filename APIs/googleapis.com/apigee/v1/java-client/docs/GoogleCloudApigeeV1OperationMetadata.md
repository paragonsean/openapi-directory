

# GoogleCloudApigeeV1OperationMetadata

Metadata describing an Operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**operationType** | [**OperationTypeEnum**](#OperationTypeEnum) |  |  [optional] |
|**progress** | [**GoogleCloudApigeeV1OperationMetadataProgress**](GoogleCloudApigeeV1OperationMetadataProgress.md) |  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) |  |  [optional] |
|**targetResourceName** | **String** | Name of the resource for which the operation is operating on. |  [optional] |
|**warnings** | **List&lt;String&gt;** | Warnings encountered while executing the operation. |  [optional] |



## Enum: OperationTypeEnum

| Name | Value |
|---- | -----|
| OPERATION_TYPE_UNSPECIFIED | &quot;OPERATION_TYPE_UNSPECIFIED&quot; |
| INSERT | &quot;INSERT&quot; |
| DELETE | &quot;DELETE&quot; |
| UPDATE | &quot;UPDATE&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| NOT_STARTED | &quot;NOT_STARTED&quot; |
| IN_PROGRESS | &quot;IN_PROGRESS&quot; |
| FINISHED | &quot;FINISHED&quot; |



