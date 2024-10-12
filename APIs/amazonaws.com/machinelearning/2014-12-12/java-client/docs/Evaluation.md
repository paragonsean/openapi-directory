

# Evaluation

<p> Represents the output of <code>GetEvaluation</code> operation. </p> <p>The content consists of the detailed metadata and data file information and the current status of the <code>Evaluation</code>.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**evaluationId** | [**String**](String.md) |  |  [optional] |
|**mlModelId** | [**String**](String.md) |  |  [optional] |
|**evaluationDataSourceId** | [**String**](String.md) |  |  [optional] |
|**inputDataLocationS3** | [**String**](String.md) |  |  [optional] |
|**createdByIamUser** | [**String**](String.md) |  |  [optional] |
|**createdAt** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**lastUpdatedAt** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**name** | [**String**](String.md) |  |  [optional] |
|**status** | [**EntityStatus**](EntityStatus.md) |  |  [optional] |
|**performanceMetrics** | [**EvaluationPerformanceMetrics**](EvaluationPerformanceMetrics.md) |  |  [optional] |
|**message** | [**String**](String.md) |  |  [optional] |
|**computeTime** | **Integer** | Long integer type that is a 64-bit signed number. |  [optional] |
|**finishedAt** | **OffsetDateTime** | A timestamp represented in epoch time. |  [optional] |
|**startedAt** | **OffsetDateTime** | A timestamp represented in epoch time. |  [optional] |



