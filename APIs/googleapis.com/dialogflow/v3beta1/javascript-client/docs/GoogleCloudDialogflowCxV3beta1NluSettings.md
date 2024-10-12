# DialogflowApi.GoogleCloudDialogflowCxV3beta1NluSettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**classificationThreshold** | **Number** | To filter out false positive results and still get variety in matched natural language inputs for your agent, you can tune the machine learning classification threshold. If the returned score value is less than the threshold value, then a no-match event will be triggered. The score values range from 0.0 (completely uncertain) to 1.0 (completely certain). If set to 0.0, the default of 0.3 is used. | [optional] 
**modelTrainingMode** | **String** | Indicates NLU model training mode. | [optional] 
**modelType** | **String** | Indicates the type of NLU model. | [optional] 



## Enum: ModelTrainingModeEnum


* `UNSPECIFIED` (value: `"MODEL_TRAINING_MODE_UNSPECIFIED"`)

* `AUTOMATIC` (value: `"MODEL_TRAINING_MODE_AUTOMATIC"`)

* `MANUAL` (value: `"MODEL_TRAINING_MODE_MANUAL"`)





## Enum: ModelTypeEnum


* `UNSPECIFIED` (value: `"MODEL_TYPE_UNSPECIFIED"`)

* `STANDARD` (value: `"MODEL_TYPE_STANDARD"`)

* `ADVANCED` (value: `"MODEL_TYPE_ADVANCED"`)




