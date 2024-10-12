

# HyperParameterTrainingJobSummary

The container for the summary information about a training job.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**trainingJobDefinitionName** | [**String**](String.md) |  |  [optional] |
|**trainingJobName** | [**String**](String.md) |  |  |
|**trainingJobArn** | [**String**](String.md) |  |  |
|**tuningJobName** | [**String**](String.md) |  |  [optional] |
|**creationTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  |
|**trainingStartTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**trainingEndTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**trainingJobStatus** | [**TrainingJobStatus**](TrainingJobStatus.md) |  |  |
|**tunedHyperParameters** | [**Map**](Map.md) |  |  |
|**failureReason** | [**String**](String.md) |  |  [optional] |
|**finalHyperParameterTuningJobObjectiveMetric** | [**HyperParameterTrainingJobSummaryFinalHyperParameterTuningJobObjectiveMetric**](HyperParameterTrainingJobSummaryFinalHyperParameterTuningJobObjectiveMetric.md) |  |  [optional] |
|**objectiveStatus** | [**ObjectiveStatus**](ObjectiveStatus.md) |  |  [optional] |



