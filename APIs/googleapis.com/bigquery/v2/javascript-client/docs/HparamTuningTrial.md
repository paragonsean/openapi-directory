# BigQueryApi.HparamTuningTrial

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endTimeMs** | **String** | Ending time of the trial. | [optional] 
**errorMessage** | **String** | Error message for FAILED and INFEASIBLE trial. | [optional] 
**evalLoss** | **Number** | Loss computed on the eval data at the end of trial. | [optional] 
**evaluationMetrics** | [**EvaluationMetrics**](EvaluationMetrics.md) |  | [optional] 
**hparamTuningEvaluationMetrics** | [**EvaluationMetrics**](EvaluationMetrics.md) |  | [optional] 
**hparams** | [**TrainingOptions**](TrainingOptions.md) |  | [optional] 
**startTimeMs** | **String** | Starting time of the trial. | [optional] 
**status** | **String** | The status of the trial. | [optional] 
**trainingLoss** | **Number** | Loss computed on the training data at the end of trial. | [optional] 
**trialId** | **String** | 1-based index of the trial. | [optional] 



## Enum: StatusEnum


* `TRIAL_STATUS_UNSPECIFIED` (value: `"TRIAL_STATUS_UNSPECIFIED"`)

* `NOT_STARTED` (value: `"NOT_STARTED"`)

* `RUNNING` (value: `"RUNNING"`)

* `SUCCEEDED` (value: `"SUCCEEDED"`)

* `FAILED` (value: `"FAILED"`)

* `INFEASIBLE` (value: `"INFEASIBLE"`)

* `STOPPED_EARLY` (value: `"STOPPED_EARLY"`)




