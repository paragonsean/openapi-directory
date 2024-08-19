

# GoogleCloudAiplatformV1beta1NasJobSpecMultiTrialAlgorithmSpec

The spec of multi-trial Neural Architecture Search (NAS).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**metric** | [**GoogleCloudAiplatformV1beta1NasJobSpecMultiTrialAlgorithmSpecMetricSpec**](GoogleCloudAiplatformV1beta1NasJobSpecMultiTrialAlgorithmSpecMetricSpec.md) |  |  [optional] |
|**multiTrialAlgorithm** | [**MultiTrialAlgorithmEnum**](#MultiTrialAlgorithmEnum) | The multi-trial Neural Architecture Search (NAS) algorithm type. Defaults to &#x60;REINFORCEMENT_LEARNING&#x60;. |  [optional] |
|**searchTrialSpec** | [**GoogleCloudAiplatformV1beta1NasJobSpecMultiTrialAlgorithmSpecSearchTrialSpec**](GoogleCloudAiplatformV1beta1NasJobSpecMultiTrialAlgorithmSpecSearchTrialSpec.md) |  |  [optional] |
|**trainTrialSpec** | [**GoogleCloudAiplatformV1beta1NasJobSpecMultiTrialAlgorithmSpecTrainTrialSpec**](GoogleCloudAiplatformV1beta1NasJobSpecMultiTrialAlgorithmSpecTrainTrialSpec.md) |  |  [optional] |



## Enum: MultiTrialAlgorithmEnum

| Name | Value |
|---- | -----|
| MULTI_TRIAL_ALGORITHM_UNSPECIFIED | &quot;MULTI_TRIAL_ALGORITHM_UNSPECIFIED&quot; |
| REINFORCEMENT_LEARNING | &quot;REINFORCEMENT_LEARNING&quot; |
| GRID_SEARCH | &quot;GRID_SEARCH&quot; |



