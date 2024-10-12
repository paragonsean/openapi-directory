# AiPlatformTrainingPredictionApi.GoogleCloudMlV1StudyConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | **String** | The search algorithm specified for the study. | [optional] 
**automatedStoppingConfig** | [**GoogleCloudMlV1AutomatedStoppingConfig**](GoogleCloudMlV1AutomatedStoppingConfig.md) |  | [optional] 
**metrics** | [**[GoogleCloudMlV1StudyConfigMetricSpec]**](GoogleCloudMlV1StudyConfigMetricSpec.md) | Metric specs for the study. | [optional] 
**parameters** | [**[GoogleCloudMlV1StudyConfigParameterSpec]**](GoogleCloudMlV1StudyConfigParameterSpec.md) | Required. The set of parameters to tune. | [optional] 



## Enum: AlgorithmEnum


* `ALGORITHM_UNSPECIFIED` (value: `"ALGORITHM_UNSPECIFIED"`)

* `GAUSSIAN_PROCESS_BANDIT` (value: `"GAUSSIAN_PROCESS_BANDIT"`)

* `GRID_SEARCH` (value: `"GRID_SEARCH"`)

* `RANDOM_SEARCH` (value: `"RANDOM_SEARCH"`)




