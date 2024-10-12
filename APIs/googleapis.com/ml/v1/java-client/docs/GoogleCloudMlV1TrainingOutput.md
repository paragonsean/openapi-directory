

# GoogleCloudMlV1TrainingOutput

Represents results of a training job. Output only.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**builtInAlgorithmOutput** | [**GoogleCloudMlV1BuiltInAlgorithmOutput**](GoogleCloudMlV1BuiltInAlgorithmOutput.md) |  |  [optional] |
|**completedTrialCount** | **String** | The number of hyperparameter tuning trials that completed successfully. Only set for hyperparameter tuning jobs. |  [optional] |
|**consumedMLUnits** | **Double** | The amount of ML units consumed by the job. |  [optional] |
|**hyperparameterMetricTag** | **String** | The TensorFlow summary tag name used for optimizing hyperparameter tuning trials. See [&#x60;HyperparameterSpec.hyperparameterMetricTag&#x60;](#HyperparameterSpec.FIELDS.hyperparameter_metric_tag) for more information. Only set for hyperparameter tuning jobs. |  [optional] |
|**isBuiltInAlgorithmJob** | **Boolean** | Whether this job is a built-in Algorithm job. |  [optional] |
|**isHyperparameterTuningJob** | **Boolean** | Whether this job is a hyperparameter tuning job. |  [optional] |
|**trials** | [**List&lt;GoogleCloudMlV1HyperparameterOutput&gt;**](GoogleCloudMlV1HyperparameterOutput.md) | Results for individual Hyperparameter trials. Only set for hyperparameter tuning jobs. |  [optional] |
|**webAccessUris** | **Map&lt;String, String&gt;** | Output only. URIs for accessing [interactive shells](https://cloud.google.com/ai-platform/training/docs/monitor-debug-interactive-shell) (one URI for each training node). Only available if training_input.enable_web_access is &#x60;true&#x60;. The keys are names of each node in the training job; for example, &#x60;master-replica-0&#x60; for the master node, &#x60;worker-replica-0&#x60; for the first worker, and &#x60;ps-replica-0&#x60; for the first parameter server. The values are the URIs for each node&#39;s interactive shell. |  [optional] [readonly] |



