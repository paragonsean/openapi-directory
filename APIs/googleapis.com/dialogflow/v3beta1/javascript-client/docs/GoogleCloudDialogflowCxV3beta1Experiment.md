# DialogflowApi.GoogleCloudDialogflowCxV3beta1Experiment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Creation time of this experiment. | [optional] 
**definition** | [**GoogleCloudDialogflowCxV3beta1ExperimentDefinition**](GoogleCloudDialogflowCxV3beta1ExperimentDefinition.md) |  | [optional] 
**description** | **String** | The human-readable description of the experiment. | [optional] 
**displayName** | **String** | Required. The human-readable name of the experiment (unique in an environment). Limit of 64 characters. | [optional] 
**endTime** | **String** | End time of this experiment. | [optional] 
**experimentLength** | **String** | Maximum number of days to run the experiment. If auto-rollout is not enabled, default value and maximum will be 30 days. If auto-rollout is enabled, default value and maximum will be 6 days. | [optional] 
**lastUpdateTime** | **String** | Last update time of this experiment. | [optional] 
**name** | **String** | The name of the experiment. Format: projects//locations//agents//environments//experiments/.. | [optional] 
**result** | [**GoogleCloudDialogflowCxV3beta1ExperimentResult**](GoogleCloudDialogflowCxV3beta1ExperimentResult.md) |  | [optional] 
**rolloutConfig** | [**GoogleCloudDialogflowCxV3beta1RolloutConfig**](GoogleCloudDialogflowCxV3beta1RolloutConfig.md) |  | [optional] 
**rolloutFailureReason** | **String** | The reason why rollout has failed. Should only be set when state is ROLLOUT_FAILED. | [optional] 
**rolloutState** | [**GoogleCloudDialogflowCxV3beta1RolloutState**](GoogleCloudDialogflowCxV3beta1RolloutState.md) |  | [optional] 
**startTime** | **String** | Start time of this experiment. | [optional] 
**state** | **String** | The current state of the experiment. Transition triggered by Experiments.StartExperiment: DRAFT-&gt;RUNNING. Transition triggered by Experiments.CancelExperiment: DRAFT-&gt;DONE or RUNNING-&gt;DONE. | [optional] 
**variantsHistory** | [**[GoogleCloudDialogflowCxV3beta1VariantsHistory]**](GoogleCloudDialogflowCxV3beta1VariantsHistory.md) | The history of updates to the experiment variants. | [optional] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `DRAFT` (value: `"DRAFT"`)

* `RUNNING` (value: `"RUNNING"`)

* `DONE` (value: `"DONE"`)

* `ROLLOUT_FAILED` (value: `"ROLLOUT_FAILED"`)




