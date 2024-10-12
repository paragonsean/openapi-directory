# CloudAutoMlApi.Dataset

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. Timestamp when this dataset was created. | [optional] 
**description** | **String** | User-provided description of the dataset. The description can be up to 25000 characters long. | [optional] 
**displayName** | **String** | Required. The name of the dataset to show in the interface. The name can be up to 32 characters long and can consist only of ASCII Latin letters A-Z and a-z, underscores (_), and ASCII digits 0-9. | [optional] 
**etag** | **String** | Used to perform consistent read-modify-write updates. If not set, a blind \&quot;overwrite\&quot; update happens. | [optional] 
**exampleCount** | **Number** | Output only. The number of examples in the dataset. | [optional] 
**imageClassificationDatasetMetadata** | [**ImageClassificationDatasetMetadata**](ImageClassificationDatasetMetadata.md) |  | [optional] 
**imageObjectDetectionDatasetMetadata** | **Object** | Dataset metadata specific to image object detection. | [optional] 
**name** | **String** | Output only. The resource name of the dataset. Form: &#x60;projects/{project_id}/locations/{location_id}/datasets/{dataset_id}&#x60; | [optional] 
**tablesDatasetMetadata** | [**TablesDatasetMetadata**](TablesDatasetMetadata.md) |  | [optional] 
**textClassificationDatasetMetadata** | [**TextClassificationDatasetMetadata**](TextClassificationDatasetMetadata.md) |  | [optional] 
**textExtractionDatasetMetadata** | **Object** | Dataset metadata that is specific to text extraction | [optional] 
**textSentimentDatasetMetadata** | [**TextSentimentDatasetMetadata**](TextSentimentDatasetMetadata.md) |  | [optional] 
**translationDatasetMetadata** | [**TranslationDatasetMetadata**](TranslationDatasetMetadata.md) |  | [optional] 
**videoClassificationDatasetMetadata** | **Object** | Dataset metadata specific to video classification. All Video Classification datasets are treated as multi label. | [optional] 
**videoObjectTrackingDatasetMetadata** | **Object** | Dataset metadata specific to video object tracking. | [optional] 


