

# GoogleCloudDialogflowCxV3Experiment

Represents an experiment in an environment.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Creation time of this experiment. |  [optional] |
|**definition** | [**GoogleCloudDialogflowCxV3ExperimentDefinition**](GoogleCloudDialogflowCxV3ExperimentDefinition.md) |  |  [optional] |
|**description** | **String** | The human-readable description of the experiment. |  [optional] |
|**displayName** | **String** | Required. The human-readable name of the experiment (unique in an environment). Limit of 64 characters. |  [optional] |
|**endTime** | **String** | End time of this experiment. |  [optional] |
|**experimentLength** | **String** | Maximum number of days to run the experiment/rollout. If auto-rollout is not enabled, default value and maximum will be 30 days. If auto-rollout is enabled, default value and maximum will be 6 days. |  [optional] |
|**lastUpdateTime** | **String** | Last update time of this experiment. |  [optional] |
|**name** | **String** | The name of the experiment. Format: projects//locations//agents//environments//experiments/.. |  [optional] |
|**result** | [**GoogleCloudDialogflowCxV3ExperimentResult**](GoogleCloudDialogflowCxV3ExperimentResult.md) |  |  [optional] |
|**rolloutConfig** | [**GoogleCloudDialogflowCxV3RolloutConfig**](GoogleCloudDialogflowCxV3RolloutConfig.md) |  |  [optional] |
|**rolloutFailureReason** | **String** | The reason why rollout has failed. Should only be set when state is ROLLOUT_FAILED. |  [optional] |
|**rolloutState** | [**GoogleCloudDialogflowCxV3RolloutState**](GoogleCloudDialogflowCxV3RolloutState.md) |  |  [optional] |
|**startTime** | **String** | Start time of this experiment. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The current state of the experiment. Transition triggered by Experiments.StartExperiment: DRAFT-&gt;RUNNING. Transition triggered by Experiments.CancelExperiment: DRAFT-&gt;DONE or RUNNING-&gt;DONE. |  [optional] |
|**variantsHistory** | [**List&lt;GoogleCloudDialogflowCxV3VariantsHistory&gt;**](GoogleCloudDialogflowCxV3VariantsHistory.md) | The history of updates to the experiment variants. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| DRAFT | &quot;DRAFT&quot; |
| RUNNING | &quot;RUNNING&quot; |
| DONE | &quot;DONE&quot; |
| ROLLOUT_FAILED | &quot;ROLLOUT_FAILED&quot; |



