# CloudAutoMlApi.Model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. Timestamp when the model training finished and can be used for prediction. | [optional] 
**datasetId** | **String** | Required. The resource ID of the dataset used to create the model. The dataset must come from the same ancestor project and location. | [optional] 
**deploymentState** | **String** | Output only. Deployment state of the model. A model can only serve prediction requests after it gets deployed. | [optional] 
**displayName** | **String** | Required. The name of the model to show in the interface. The name can be up to 32 characters long and can consist only of ASCII Latin letters A-Z and a-z, underscores (_), and ASCII digits 0-9. It must start with a letter. | [optional] 
**imageClassificationModelMetadata** | [**ImageClassificationModelMetadata**](ImageClassificationModelMetadata.md) |  | [optional] 
**imageObjectDetectionModelMetadata** | [**ImageObjectDetectionModelMetadata**](ImageObjectDetectionModelMetadata.md) |  | [optional] 
**name** | **String** | Output only. Resource name of the model. Format: &#x60;projects/{project_id}/locations/{location_id}/models/{model_id}&#x60; | [optional] 
**tablesModelMetadata** | [**TablesModelMetadata**](TablesModelMetadata.md) |  | [optional] 
**textClassificationModelMetadata** | [**TextClassificationModelMetadata**](TextClassificationModelMetadata.md) |  | [optional] 
**textExtractionModelMetadata** | [**TextExtractionModelMetadata**](TextExtractionModelMetadata.md) |  | [optional] 
**textSentimentModelMetadata** | **Object** | Model metadata that is specific to text sentiment. | [optional] 
**trainExampleCount** | **Number** | Output only. The number of examples in the training set used for the model creation. | [optional] [readonly] 
**translationModelMetadata** | [**TranslationModelMetadata**](TranslationModelMetadata.md) |  | [optional] 
**updateTime** | **String** | Output only. Timestamp when this model was last updated. | [optional] 
**validateExampleCount** | **Number** | Output only. The number of examples in the validation set used for the model creation. | [optional] [readonly] 
**videoClassificationModelMetadata** | **Object** | Model metadata specific to video classification. | [optional] 
**videoObjectTrackingModelMetadata** | **Object** | Model metadata specific to video object tracking. | [optional] 



## Enum: DeploymentStateEnum


* `DEPLOYMENT_STATE_UNSPECIFIED` (value: `"DEPLOYMENT_STATE_UNSPECIFIED"`)

* `DEPLOYED` (value: `"DEPLOYED"`)

* `UNDEPLOYED` (value: `"UNDEPLOYED"`)




