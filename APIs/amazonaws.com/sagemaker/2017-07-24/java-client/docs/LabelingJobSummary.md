

# LabelingJobSummary

Provides summary information about a labeling job.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**labelingJobName** | [**String**](String.md) |  |  |
|**labelingJobArn** | [**String**](String.md) |  |  |
|**creationTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  |
|**lastModifiedTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  |
|**labelingJobStatus** | [**LabelingJobStatus**](LabelingJobStatus.md) |  |  |
|**labelCounters** | [**LabelingJobSummaryLabelCounters**](LabelingJobSummaryLabelCounters.md) |  |  |
|**workteamArn** | [**String**](String.md) |  |  |
|**preHumanTaskLambdaArn** | [**String**](String.md) |  |  |
|**annotationConsolidationLambdaArn** | [**String**](String.md) |  |  [optional] |
|**failureReason** | [**String**](String.md) |  |  [optional] |
|**labelingJobOutput** | [**DescribeLabelingJobResponseLabelingJobOutput**](DescribeLabelingJobResponseLabelingJobOutput.md) |  |  [optional] |
|**inputConfig** | [**LabelingJobSummaryInputConfig**](LabelingJobSummaryInputConfig.md) |  |  [optional] |



