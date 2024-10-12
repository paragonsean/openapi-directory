

# GoogleCloudDocumentaiV1ReviewDocumentRequest

Request message for the ReviewDocument method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**documentSchema** | [**GoogleCloudDocumentaiV1DocumentSchema**](GoogleCloudDocumentaiV1DocumentSchema.md) |  |  [optional] |
|**enableSchemaValidation** | **Boolean** | Whether the validation should be performed on the ad-hoc review request. |  [optional] |
|**inlineDocument** | [**GoogleCloudDocumentaiV1Document**](GoogleCloudDocumentaiV1Document.md) |  |  [optional] |
|**priority** | [**PriorityEnum**](#PriorityEnum) | The priority of the human review task. |  [optional] |



## Enum: PriorityEnum

| Name | Value |
|---- | -----|
| DEFAULT | &quot;DEFAULT&quot; |
| URGENT | &quot;URGENT&quot; |



