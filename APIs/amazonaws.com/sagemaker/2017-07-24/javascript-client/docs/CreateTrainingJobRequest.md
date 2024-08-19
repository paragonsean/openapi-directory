# AmazonSageMakerService.CreateTrainingJobRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trainingJobName** | **String** |  | 
**hyperParameters** | **Object** |  | [optional] 
**algorithmSpecification** | [**CreateTrainingJobRequestAlgorithmSpecification**](CreateTrainingJobRequestAlgorithmSpecification.md) |  | 
**roleArn** | **String** |  | 
**inputDataConfig** | **Array** |  | [optional] 
**outputDataConfig** | [**CreateTrainingJobRequestOutputDataConfig**](CreateTrainingJobRequestOutputDataConfig.md) |  | 
**resourceConfig** | [**CreateTrainingJobRequestResourceConfig**](CreateTrainingJobRequestResourceConfig.md) |  | 
**vpcConfig** | [**CreateTrainingJobRequestVpcConfig**](CreateTrainingJobRequestVpcConfig.md) |  | [optional] 
**stoppingCondition** | [**CreateTrainingJobRequestStoppingCondition**](CreateTrainingJobRequestStoppingCondition.md) |  | 
**tags** | **Array** |  | [optional] 
**enableNetworkIsolation** | **Boolean** |  | [optional] 
**enableInterContainerTrafficEncryption** | **Boolean** |  | [optional] 
**enableManagedSpotTraining** | **Boolean** |  | [optional] 
**checkpointConfig** | [**CreateTrainingJobRequestCheckpointConfig**](CreateTrainingJobRequestCheckpointConfig.md) |  | [optional] 
**debugHookConfig** | [**DebugHookConfig**](DebugHookConfig.md) |  | [optional] 
**debugRuleConfigurations** | **Array** |  | [optional] 
**tensorBoardOutputConfig** | [**TensorBoardOutputConfig**](TensorBoardOutputConfig.md) |  | [optional] 
**experimentConfig** | [**ExperimentConfig**](ExperimentConfig.md) |  | [optional] 
**profilerConfig** | [**ProfilerConfig**](ProfilerConfig.md) |  | [optional] 
**profilerRuleConfigurations** | **Array** |  | [optional] 
**environment** | **Object** |  | [optional] 
**retryStrategy** | [**CreateTrainingJobRequestRetryStrategy**](CreateTrainingJobRequestRetryStrategy.md) |  | [optional] 


