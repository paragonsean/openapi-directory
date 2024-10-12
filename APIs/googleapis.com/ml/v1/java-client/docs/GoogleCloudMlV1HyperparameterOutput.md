

# GoogleCloudMlV1HyperparameterOutput

Represents the result of a single hyperparameter tuning trial from a training job. The TrainingOutput object that is returned on successful completion of a training job with hyperparameter tuning includes a list of HyperparameterOutput objects, one for each successful trial.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allMetrics** | [**List&lt;GoogleCloudMlV1HyperparameterOutputHyperparameterMetric&gt;**](GoogleCloudMlV1HyperparameterOutputHyperparameterMetric.md) | All recorded object metrics for this trial. This field is not currently populated. |  [optional] |
|**builtInAlgorithmOutput** | [**GoogleCloudMlV1BuiltInAlgorithmOutput**](GoogleCloudMlV1BuiltInAlgorithmOutput.md) |  |  [optional] |
|**endTime** | **String** | Output only. End time for the trial. |  [optional] |
|**finalMetric** | [**GoogleCloudMlV1HyperparameterOutputHyperparameterMetric**](GoogleCloudMlV1HyperparameterOutputHyperparameterMetric.md) |  |  [optional] |
|**hyperparameters** | **Map&lt;String, String&gt;** | The hyperparameters given to this trial. |  [optional] |
|**isTrialStoppedEarly** | **Boolean** | True if the trial is stopped early. |  [optional] |
|**startTime** | **String** | Output only. Start time for the trial. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The detailed state of the trial. |  [optional] |
|**trialId** | **String** | The trial id for these results. |  [optional] |
|**webAccessUris** | **Map&lt;String, String&gt;** | URIs for accessing [interactive shells](https://cloud.google.com/ai-platform/training/docs/monitor-debug-interactive-shell) (one URI for each training node). Only available if this trial is part of a hyperparameter tuning job and the job&#39;s training_input.enable_web_access is &#x60;true&#x60;. The keys are names of each node in the training job; for example, &#x60;master-replica-0&#x60; for the master node, &#x60;worker-replica-0&#x60; for the first worker, and &#x60;ps-replica-0&#x60; for the first parameter server. The values are the URIs for each node&#39;s interactive shell. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| QUEUED | &quot;QUEUED&quot; |
| PREPARING | &quot;PREPARING&quot; |
| RUNNING | &quot;RUNNING&quot; |
| SUCCEEDED | &quot;SUCCEEDED&quot; |
| FAILED | &quot;FAILED&quot; |
| CANCELLING | &quot;CANCELLING&quot; |
| CANCELLED | &quot;CANCELLED&quot; |



