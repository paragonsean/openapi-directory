# AiPlatformTrainingPredictionApi.GoogleCloudMlV1HyperparameterSpec

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | **String** | Optional. The search algorithm specified for the hyperparameter tuning job. Uses the default AI Platform hyperparameter tuning algorithm if unspecified. | [optional] 
**enableTrialEarlyStopping** | **Boolean** | Optional. Indicates if the hyperparameter tuning job enables auto trial early stopping. | [optional] 
**goal** | **String** | Required. The type of goal to use for tuning. Available types are &#x60;MAXIMIZE&#x60; and &#x60;MINIMIZE&#x60;. Defaults to &#x60;MAXIMIZE&#x60;. | [optional] 
**hyperparameterMetricTag** | **String** | Optional. The TensorFlow summary tag name to use for optimizing trials. For current versions of TensorFlow, this tag name should exactly match what is shown in TensorBoard, including all scopes. For versions of TensorFlow prior to 0.12, this should be only the tag passed to tf.Summary. By default, \&quot;training/hptuning/metric\&quot; will be used. | [optional] 
**maxFailedTrials** | **Number** | Optional. The number of failed trials that need to be seen before failing the hyperparameter tuning job. You can specify this field to override the default failing criteria for AI Platform hyperparameter tuning jobs. Defaults to zero, which means the service decides when a hyperparameter job should fail. | [optional] 
**maxParallelTrials** | **Number** | Optional. The number of training trials to run concurrently. You can reduce the time it takes to perform hyperparameter tuning by adding trials in parallel. However, each trail only benefits from the information gained in completed trials. That means that a trial does not get access to the results of trials running at the same time, which could reduce the quality of the overall optimization. Each trial will use the same scale tier and machine types. Defaults to one. | [optional] 
**maxTrials** | **Number** | Optional. How many training trials should be attempted to optimize the specified hyperparameters. Defaults to one. | [optional] 
**params** | [**[GoogleCloudMlV1ParameterSpec]**](GoogleCloudMlV1ParameterSpec.md) | Required. The set of parameters to tune. | [optional] 
**resumePreviousJobId** | **String** | Optional. The prior hyperparameter tuning job id that users hope to continue with. The job id will be used to find the corresponding vizier study guid and resume the study. | [optional] 



## Enum: AlgorithmEnum


* `ALGORITHM_UNSPECIFIED` (value: `"ALGORITHM_UNSPECIFIED"`)

* `GRID_SEARCH` (value: `"GRID_SEARCH"`)

* `RANDOM_SEARCH` (value: `"RANDOM_SEARCH"`)





## Enum: GoalEnum


* `GOAL_TYPE_UNSPECIFIED` (value: `"GOAL_TYPE_UNSPECIFIED"`)

* `MAXIMIZE` (value: `"MAXIMIZE"`)

* `MINIMIZE` (value: `"MINIMIZE"`)




