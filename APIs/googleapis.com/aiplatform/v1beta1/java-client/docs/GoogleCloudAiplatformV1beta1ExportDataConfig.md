

# GoogleCloudAiplatformV1beta1ExportDataConfig

Describes what part of the Dataset is to be exported, the destination of the export and how to export.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**annotationsFilter** | **String** | An expression for filtering what part of the Dataset is to be exported. Only Annotations that match this filter will be exported. The filter syntax is the same as in ListAnnotations. |  [optional] |
|**fractionSplit** | [**GoogleCloudAiplatformV1beta1ExportFractionSplit**](GoogleCloudAiplatformV1beta1ExportFractionSplit.md) |  |  [optional] |
|**gcsDestination** | [**GoogleCloudAiplatformV1beta1GcsDestination**](GoogleCloudAiplatformV1beta1GcsDestination.md) |  |  [optional] |



