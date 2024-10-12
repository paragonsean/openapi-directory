# AiPlatformTrainingPredictionApi.GoogleCloudMlV1HyperparameterOutput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allMetrics** | [**[GoogleCloudMlV1HyperparameterOutputHyperparameterMetric]**](GoogleCloudMlV1HyperparameterOutputHyperparameterMetric.md) | All recorded object metrics for this trial. This field is not currently populated. | [optional] 
**builtInAlgorithmOutput** | [**GoogleCloudMlV1BuiltInAlgorithmOutput**](GoogleCloudMlV1BuiltInAlgorithmOutput.md) |  | [optional] 
**endTime** | **String** | Output only. End time for the trial. | [optional] 
**finalMetric** | [**GoogleCloudMlV1HyperparameterOutputHyperparameterMetric**](GoogleCloudMlV1HyperparameterOutputHyperparameterMetric.md) |  | [optional] 
**hyperparameters** | **{String: String}** | The hyperparameters given to this trial. | [optional] 
**isTrialStoppedEarly** | **Boolean** | True if the trial is stopped early. | [optional] 
**startTime** | **String** | Output only. Start time for the trial. | [optional] 
**state** | **String** | Output only. The detailed state of the trial. | [optional] 
**trialId** | **String** | The trial id for these results. | [optional] 
**webAccessUris** | **{String: String}** | URIs for accessing [interactive shells](https://cloud.google.com/ai-platform/training/docs/monitor-debug-interactive-shell) (one URI for each training node). Only available if this trial is part of a hyperparameter tuning job and the job&#39;s training_input.enable_web_access is &#x60;true&#x60;. The keys are names of each node in the training job; for example, &#x60;master-replica-0&#x60; for the master node, &#x60;worker-replica-0&#x60; for the first worker, and &#x60;ps-replica-0&#x60; for the first parameter server. The values are the URIs for each node&#39;s interactive shell. | [optional] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `QUEUED` (value: `"QUEUED"`)

* `PREPARING` (value: `"PREPARING"`)

* `RUNNING` (value: `"RUNNING"`)

* `SUCCEEDED` (value: `"SUCCEEDED"`)

* `FAILED` (value: `"FAILED"`)

* `CANCELLING` (value: `"CANCELLING"`)

* `CANCELLED` (value: `"CANCELLED"`)




