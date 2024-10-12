

# UpdateDatasetRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientToken** | **String** | Idempotence Token for API operations |  [optional] |
|**datasetTitle** | **String** | Title for a given Dataset |  |
|**kind** | [**KindEnum**](#KindEnum) | Dataset Kind |  |
|**datasetDescription** | **String** | Description of a dataset |  [optional] |
|**alias** | **String** | The unique resource identifier for a Dataset. |  [optional] |
|**schemaDefinition** | [**CreateDatasetRequestSchemaDefinition**](CreateDatasetRequestSchemaDefinition.md) |  |  [optional] |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| TABULAR | &quot;TABULAR&quot; |
| NON_TABULAR | &quot;NON_TABULAR&quot; |



