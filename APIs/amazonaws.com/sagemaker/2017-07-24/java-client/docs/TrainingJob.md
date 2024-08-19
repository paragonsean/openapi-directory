

# TrainingJob

Contains information about a training job.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**trainingJobName** | [**String**](String.md) |  |  [optional] |
|**trainingJobArn** | [**String**](String.md) |  |  [optional] |
|**tuningJobArn** | [**String**](String.md) |  |  [optional] |
|**labelingJobArn** | [**String**](String.md) |  |  [optional] |
|**autoMLJobArn** | [**String**](String.md) |  |  [optional] |
|**modelArtifacts** | [**TrainingJobModelArtifacts**](TrainingJobModelArtifacts.md) |  |  [optional] |
|**trainingJobStatus** | [**TrainingJobStatus**](TrainingJobStatus.md) |  |  [optional] |
|**secondaryStatus** | [**SecondaryStatus**](SecondaryStatus.md) |  |  [optional] |
|**failureReason** | [**String**](String.md) |  |  [optional] |
|**hyperParameters** | [**Map**](Map.md) |  |  [optional] |
|**algorithmSpecification** | [**TrainingJobAlgorithmSpecification**](TrainingJobAlgorithmSpecification.md) |  |  [optional] |
|**roleArn** | [**String**](String.md) |  |  [optional] |
|**inputDataConfig** | [**List**](List.md) |  |  [optional] |
|**outputDataConfig** | [**TrainingJobOutputDataConfig**](TrainingJobOutputDataConfig.md) |  |  [optional] |
|**resourceConfig** | [**TrainingJobResourceConfig**](TrainingJobResourceConfig.md) |  |  [optional] |
|**vpcConfig** | [**DescribeTrainingJobResponseVpcConfig**](DescribeTrainingJobResponseVpcConfig.md) |  |  [optional] |
|**stoppingCondition** | [**CreateTrainingJobRequestStoppingCondition**](CreateTrainingJobRequestStoppingCondition.md) |  |  [optional] |
|**creationTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**trainingStartTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**trainingEndTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**lastModifiedTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**secondaryStatusTransitions** | [**List**](List.md) |  |  [optional] |
|**finalMetricDataList** | [**List**](List.md) |  |  [optional] |
|**enableNetworkIsolation** | [**Boolean**](Boolean.md) |  |  [optional] |
|**enableInterContainerTrafficEncryption** | [**Boolean**](Boolean.md) |  |  [optional] |
|**enableManagedSpotTraining** | [**Boolean**](Boolean.md) |  |  [optional] |
|**checkpointConfig** | [**CheckpointConfig**](CheckpointConfig.md) |  |  [optional] |
|**trainingTimeInSeconds** | [**Integer**](Integer.md) |  |  [optional] |
|**billableTimeInSeconds** | [**Integer**](Integer.md) |  |  [optional] |
|**debugHookConfig** | [**DebugHookConfig**](DebugHookConfig.md) |  |  [optional] |
|**experimentConfig** | [**ExperimentConfig**](ExperimentConfig.md) |  |  [optional] |
|**debugRuleConfigurations** | [**List**](List.md) |  |  [optional] |
|**tensorBoardOutputConfig** | [**TensorBoardOutputConfig**](TensorBoardOutputConfig.md) |  |  [optional] |
|**debugRuleEvaluationStatuses** | [**List**](List.md) |  |  [optional] |
|**profilerConfig** | [**ProfilerConfig**](ProfilerConfig.md) |  |  [optional] |
|**environment** | [**Map**](Map.md) |  |  [optional] |
|**retryStrategy** | [**CreateTrainingJobRequestRetryStrategy**](CreateTrainingJobRequestRetryStrategy.md) |  |  [optional] |
|**tags** | [**List**](List.md) |  |  [optional] |



