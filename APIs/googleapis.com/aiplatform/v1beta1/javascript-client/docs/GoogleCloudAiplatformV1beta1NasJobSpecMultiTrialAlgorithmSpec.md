# VertexAiApi.GoogleCloudAiplatformV1beta1NasJobSpecMultiTrialAlgorithmSpec

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric** | [**GoogleCloudAiplatformV1beta1NasJobSpecMultiTrialAlgorithmSpecMetricSpec**](GoogleCloudAiplatformV1beta1NasJobSpecMultiTrialAlgorithmSpecMetricSpec.md) |  | [optional] 
**multiTrialAlgorithm** | **String** | The multi-trial Neural Architecture Search (NAS) algorithm type. Defaults to &#x60;REINFORCEMENT_LEARNING&#x60;. | [optional] 
**searchTrialSpec** | [**GoogleCloudAiplatformV1beta1NasJobSpecMultiTrialAlgorithmSpecSearchTrialSpec**](GoogleCloudAiplatformV1beta1NasJobSpecMultiTrialAlgorithmSpecSearchTrialSpec.md) |  | [optional] 
**trainTrialSpec** | [**GoogleCloudAiplatformV1beta1NasJobSpecMultiTrialAlgorithmSpecTrainTrialSpec**](GoogleCloudAiplatformV1beta1NasJobSpecMultiTrialAlgorithmSpecTrainTrialSpec.md) |  | [optional] 



## Enum: MultiTrialAlgorithmEnum


* `MULTI_TRIAL_ALGORITHM_UNSPECIFIED` (value: `"MULTI_TRIAL_ALGORITHM_UNSPECIFIED"`)

* `REINFORCEMENT_LEARNING` (value: `"REINFORCEMENT_LEARNING"`)

* `GRID_SEARCH` (value: `"GRID_SEARCH"`)




