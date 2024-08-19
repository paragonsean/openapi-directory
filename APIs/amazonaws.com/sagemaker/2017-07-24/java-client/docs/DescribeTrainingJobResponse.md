

# DescribeTrainingJobResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**trainingJobName** | [**String**](String.md) |  |  |
|**trainingJobArn** | [**String**](String.md) |  |  |
|**tuningJobArn** | [**String**](String.md) |  |  [optional] |
|**labelingJobArn** | [**String**](String.md) |  |  [optional] |
|**autoMLJobArn** | [**String**](String.md) |  |  [optional] |
|**modelArtifacts** | [**DescribeTrainingJobResponseModelArtifacts**](DescribeTrainingJobResponseModelArtifacts.md) |  |  |
|**trainingJobStatus** | [**TrainingJobStatus**](TrainingJobStatus.md) |  |  |
|**secondaryStatus** | [**SecondaryStatus**](SecondaryStatus.md) |  |  |
|**failureReason** | [**String**](String.md) |  |  [optional] |
|**hyperParameters** | [**Map**](Map.md) |  |  [optional] |
|**algorithmSpecification** | [**DescribeTrainingJobResponseAlgorithmSpecification**](DescribeTrainingJobResponseAlgorithmSpecification.md) |  |  |
|**roleArn** | [**String**](String.md) |  |  [optional] |
|**inputDataConfig** | [**List**](List.md) |  |  [optional] |
|**outputDataConfig** | [**DescribeTrainingJobResponseOutputDataConfig**](DescribeTrainingJobResponseOutputDataConfig.md) |  |  [optional] |
|**resourceConfig** | [**DescribeTrainingJobResponseResourceConfig**](DescribeTrainingJobResponseResourceConfig.md) |  |  |
|**vpcConfig** | [**DescribeTrainingJobResponseVpcConfig**](DescribeTrainingJobResponseVpcConfig.md) |  |  [optional] |
|**stoppingCondition** | [**CreateTrainingJobRequestStoppingCondition**](CreateTrainingJobRequestStoppingCondition.md) |  |  |
|**creationTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  |
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
|**profilerRuleConfigurations** | [**List**](List.md) |  |  [optional] |
|**profilerRuleEvaluationStatuses** | [**List**](List.md) |  |  [optional] |
|**profilingStatus** | [**ProfilingStatus**](ProfilingStatus.md) |  |  [optional] |
|**retryStrategy** | [**CreateTrainingJobRequestRetryStrategy**](CreateTrainingJobRequestRetryStrategy.md) |  |  [optional] |
|**environment** | [**Map**](Map.md) |  |  [optional] |
|**warmPoolStatus** | [**DescribeTrainingJobResponseWarmPoolStatus**](DescribeTrainingJobResponseWarmPoolStatus.md) |  |  [optional] |



