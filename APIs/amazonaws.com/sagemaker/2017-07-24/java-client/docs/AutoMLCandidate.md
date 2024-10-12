

# AutoMLCandidate

Information about a candidate produced by an AutoML training job, including its status, steps, and other properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**candidateName** | [**String**](String.md) |  |  |
|**finalAutoMLJobObjectiveMetric** | [**FinalAutoMLJobObjectiveMetric**](FinalAutoMLJobObjectiveMetric.md) |  |  [optional] |
|**objectiveStatus** | [**ObjectiveStatus**](ObjectiveStatus.md) |  |  |
|**candidateSteps** | [**List**](List.md) |  |  |
|**candidateStatus** | [**CandidateStatus**](CandidateStatus.md) |  |  |
|**inferenceContainers** | [**List**](List.md) |  |  [optional] |
|**creationTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  |
|**endTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**lastModifiedTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  |
|**failureReason** | [**String**](String.md) |  |  [optional] |
|**candidateProperties** | [**AutoMLCandidateCandidateProperties**](AutoMLCandidateCandidateProperties.md) |  |  [optional] |
|**inferenceContainerDefinitions** | [**Map**](Map.md) |  |  [optional] |



