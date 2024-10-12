

# TransformJobSummary

Provides a summary of a transform job. Multiple <code>TransformJobSummary</code> objects are returned as a list after in response to a <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListTransformJobs.html\">ListTransformJobs</a> call.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**transformJobName** | [**String**](String.md) |  |  |
|**transformJobArn** | [**String**](String.md) |  |  |
|**creationTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  |
|**transformEndTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**lastModifiedTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**transformJobStatus** | [**TransformJobStatus**](TransformJobStatus.md) |  |  |
|**failureReason** | [**String**](String.md) |  |  [optional] |



