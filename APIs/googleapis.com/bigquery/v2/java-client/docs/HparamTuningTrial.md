

# HparamTuningTrial

Training info of a trial in [hyperparameter tuning](/bigquery-ml/docs/reference/standard-sql/bigqueryml-syntax-hp-tuning-overview) models.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endTimeMs** | **String** | Ending time of the trial. |  [optional] |
|**errorMessage** | **String** | Error message for FAILED and INFEASIBLE trial. |  [optional] |
|**evalLoss** | **Double** | Loss computed on the eval data at the end of trial. |  [optional] |
|**evaluationMetrics** | [**EvaluationMetrics**](EvaluationMetrics.md) |  |  [optional] |
|**hparamTuningEvaluationMetrics** | [**EvaluationMetrics**](EvaluationMetrics.md) |  |  [optional] |
|**hparams** | [**TrainingOptions**](TrainingOptions.md) |  |  [optional] |
|**startTimeMs** | **String** | Starting time of the trial. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the trial. |  [optional] |
|**trainingLoss** | **Double** | Loss computed on the training data at the end of trial. |  [optional] |
|**trialId** | **String** | 1-based index of the trial. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| TRIAL_STATUS_UNSPECIFIED | &quot;TRIAL_STATUS_UNSPECIFIED&quot; |
| NOT_STARTED | &quot;NOT_STARTED&quot; |
| RUNNING | &quot;RUNNING&quot; |
| SUCCEEDED | &quot;SUCCEEDED&quot; |
| FAILED | &quot;FAILED&quot; |
| INFEASIBLE | &quot;INFEASIBLE&quot; |
| STOPPED_EARLY | &quot;STOPPED_EARLY&quot; |



