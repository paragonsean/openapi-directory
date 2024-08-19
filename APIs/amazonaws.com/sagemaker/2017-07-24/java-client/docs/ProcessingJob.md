

# ProcessingJob

An Amazon SageMaker processing job that is used to analyze data and evaluate models. For more information, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/processing-job.html\">Process Data and Evaluate Models</a>.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**processingInputs** | [**List**](List.md) |  |  [optional] |
|**processingOutputConfig** | [**ProcessingOutputConfig**](ProcessingOutputConfig.md) |  |  [optional] |
|**processingJobName** | [**String**](String.md) |  |  [optional] |
|**processingResources** | [**ProcessingResources**](ProcessingResources.md) |  |  [optional] |
|**stoppingCondition** | [**ProcessingStoppingCondition**](ProcessingStoppingCondition.md) |  |  [optional] |
|**appSpecification** | [**AppSpecification**](AppSpecification.md) |  |  [optional] |
|**environment** | [**Map**](Map.md) |  |  [optional] |
|**networkConfig** | [**NetworkConfig**](NetworkConfig.md) |  |  [optional] |
|**roleArn** | [**String**](String.md) |  |  [optional] |
|**experimentConfig** | [**ExperimentConfig**](ExperimentConfig.md) |  |  [optional] |
|**processingJobArn** | [**String**](String.md) |  |  [optional] |
|**processingJobStatus** | [**ProcessingJobStatus**](ProcessingJobStatus.md) |  |  [optional] |
|**exitMessage** | [**String**](String.md) |  |  [optional] |
|**failureReason** | [**String**](String.md) |  |  [optional] |
|**processingEndTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**processingStartTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**lastModifiedTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**creationTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**monitoringScheduleArn** | [**String**](String.md) |  |  [optional] |
|**autoMLJobArn** | [**String**](String.md) |  |  [optional] |
|**trainingJobArn** | [**String**](String.md) |  |  [optional] |
|**tags** | [**List**](List.md) |  |  [optional] |



