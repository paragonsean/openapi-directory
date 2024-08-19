# AmazonSageMakerService.DescribeTrainingJobResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trainingJobName** | **String** |  | 
**trainingJobArn** | **String** |  | 
**tuningJobArn** | **String** |  | [optional] 
**labelingJobArn** | **String** |  | [optional] 
**autoMLJobArn** | **String** |  | [optional] 
**modelArtifacts** | [**DescribeTrainingJobResponseModelArtifacts**](DescribeTrainingJobResponseModelArtifacts.md) |  | 
**trainingJobStatus** | [**TrainingJobStatus**](TrainingJobStatus.md) |  | 
**secondaryStatus** | [**SecondaryStatus**](SecondaryStatus.md) |  | 
**failureReason** | **String** |  | [optional] 
**hyperParameters** | **Object** |  | [optional] 
**algorithmSpecification** | [**DescribeTrainingJobResponseAlgorithmSpecification**](DescribeTrainingJobResponseAlgorithmSpecification.md) |  | 
**roleArn** | **String** |  | [optional] 
**inputDataConfig** | **Array** |  | [optional] 
**outputDataConfig** | [**DescribeTrainingJobResponseOutputDataConfig**](DescribeTrainingJobResponseOutputDataConfig.md) |  | [optional] 
**resourceConfig** | [**DescribeTrainingJobResponseResourceConfig**](DescribeTrainingJobResponseResourceConfig.md) |  | 
**vpcConfig** | [**DescribeTrainingJobResponseVpcConfig**](DescribeTrainingJobResponseVpcConfig.md) |  | [optional] 
**stoppingCondition** | [**CreateTrainingJobRequestStoppingCondition**](CreateTrainingJobRequestStoppingCondition.md) |  | 
**creationTime** | **Date** |  | 
**trainingStartTime** | **Date** |  | [optional] 
**trainingEndTime** | **Date** |  | [optional] 
**lastModifiedTime** | **Date** |  | [optional] 
**secondaryStatusTransitions** | **Array** |  | [optional] 
**finalMetricDataList** | **Array** |  | [optional] 
**enableNetworkIsolation** | **Boolean** |  | [optional] 
**enableInterContainerTrafficEncryption** | **Boolean** |  | [optional] 
**enableManagedSpotTraining** | **Boolean** |  | [optional] 
**checkpointConfig** | [**CheckpointConfig**](CheckpointConfig.md) |  | [optional] 
**trainingTimeInSeconds** | **Number** |  | [optional] 
**billableTimeInSeconds** | **Number** |  | [optional] 
**debugHookConfig** | [**DebugHookConfig**](DebugHookConfig.md) |  | [optional] 
**experimentConfig** | [**ExperimentConfig**](ExperimentConfig.md) |  | [optional] 
**debugRuleConfigurations** | **Array** |  | [optional] 
**tensorBoardOutputConfig** | [**TensorBoardOutputConfig**](TensorBoardOutputConfig.md) |  | [optional] 
**debugRuleEvaluationStatuses** | **Array** |  | [optional] 
**profilerConfig** | [**ProfilerConfig**](ProfilerConfig.md) |  | [optional] 
**profilerRuleConfigurations** | **Array** |  | [optional] 
**profilerRuleEvaluationStatuses** | **Array** |  | [optional] 
**profilingStatus** | [**ProfilingStatus**](ProfilingStatus.md) |  | [optional] 
**retryStrategy** | [**CreateTrainingJobRequestRetryStrategy**](CreateTrainingJobRequestRetryStrategy.md) |  | [optional] 
**environment** | **Object** |  | [optional] 
**warmPoolStatus** | [**DescribeTrainingJobResponseWarmPoolStatus**](DescribeTrainingJobResponseWarmPoolStatus.md) |  | [optional] 


