

# GoogleCloudDialogflowCxV3beta1NluSettings

Settings related to NLU.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**classificationThreshold** | **Float** | To filter out false positive results and still get variety in matched natural language inputs for your agent, you can tune the machine learning classification threshold. If the returned score value is less than the threshold value, then a no-match event will be triggered. The score values range from 0.0 (completely uncertain) to 1.0 (completely certain). If set to 0.0, the default of 0.3 is used. |  [optional] |
|**modelTrainingMode** | [**ModelTrainingModeEnum**](#ModelTrainingModeEnum) | Indicates NLU model training mode. |  [optional] |
|**modelType** | [**ModelTypeEnum**](#ModelTypeEnum) | Indicates the type of NLU model. |  [optional] |



## Enum: ModelTrainingModeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;MODEL_TRAINING_MODE_UNSPECIFIED&quot; |
| AUTOMATIC | &quot;MODEL_TRAINING_MODE_AUTOMATIC&quot; |
| MANUAL | &quot;MODEL_TRAINING_MODE_MANUAL&quot; |



## Enum: ModelTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;MODEL_TYPE_UNSPECIFIED&quot; |
| STANDARD | &quot;MODEL_TYPE_STANDARD&quot; |
| ADVANCED | &quot;MODEL_TYPE_ADVANCED&quot; |



