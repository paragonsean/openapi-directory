

# GoogleCloudMlV1StudyConfig

Represents configuration of a study.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**algorithm** | [**AlgorithmEnum**](#AlgorithmEnum) | The search algorithm specified for the study. |  [optional] |
|**automatedStoppingConfig** | [**GoogleCloudMlV1AutomatedStoppingConfig**](GoogleCloudMlV1AutomatedStoppingConfig.md) |  |  [optional] |
|**metrics** | [**List&lt;GoogleCloudMlV1StudyConfigMetricSpec&gt;**](GoogleCloudMlV1StudyConfigMetricSpec.md) | Metric specs for the study. |  [optional] |
|**parameters** | [**List&lt;GoogleCloudMlV1StudyConfigParameterSpec&gt;**](GoogleCloudMlV1StudyConfigParameterSpec.md) | Required. The set of parameters to tune. |  [optional] |



## Enum: AlgorithmEnum

| Name | Value |
|---- | -----|
| ALGORITHM_UNSPECIFIED | &quot;ALGORITHM_UNSPECIFIED&quot; |
| GAUSSIAN_PROCESS_BANDIT | &quot;GAUSSIAN_PROCESS_BANDIT&quot; |
| GRID_SEARCH | &quot;GRID_SEARCH&quot; |
| RANDOM_SEARCH | &quot;RANDOM_SEARCH&quot; |



