

# GoogleCloudDocumentaiV1beta3ReviewDocumentRequest

Request message for the ReviewDocument method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**document** | [**GoogleCloudDocumentaiV1beta3Document**](GoogleCloudDocumentaiV1beta3Document.md) |  |  [optional] |
|**documentSchema** | [**GoogleCloudDocumentaiV1beta3DocumentSchema**](GoogleCloudDocumentaiV1beta3DocumentSchema.md) |  |  [optional] |
|**enableSchemaValidation** | **Boolean** | Whether the validation should be performed on the ad-hoc review request. |  [optional] |
|**inlineDocument** | [**GoogleCloudDocumentaiV1beta3Document**](GoogleCloudDocumentaiV1beta3Document.md) |  |  [optional] |
|**priority** | [**PriorityEnum**](#PriorityEnum) | The priority of the human review task. |  [optional] |



## Enum: PriorityEnum

| Name | Value |
|---- | -----|
| DEFAULT | &quot;DEFAULT&quot; |
| URGENT | &quot;URGENT&quot; |



