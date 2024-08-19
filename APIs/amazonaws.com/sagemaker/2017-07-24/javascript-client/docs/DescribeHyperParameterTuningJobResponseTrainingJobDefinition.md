# AmazonSageMakerService.DescribeHyperParameterTuningJobResponseTrainingJobDefinition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**definitionName** | **String** |  | [optional] 
**tuningObjective** | [**HyperParameterTuningJobObjective**](HyperParameterTuningJobObjective.md) |  | [optional] 
**hyperParameterRanges** | [**ParameterRanges**](ParameterRanges.md) |  | [optional] 
**staticHyperParameters** | **Object** |  | [optional] 
**algorithmSpecification** | [**HyperParameterTrainingJobDefinitionAlgorithmSpecification**](HyperParameterTrainingJobDefinitionAlgorithmSpecification.md) |  | 
**roleArn** | **String** |  | 
**inputDataConfig** | **Array** |  | [optional] 
**vpcConfig** | [**HyperParameterTrainingJobDefinitionVpcConfig**](HyperParameterTrainingJobDefinitionVpcConfig.md) |  | [optional] 
**outputDataConfig** | [**HyperParameterTrainingJobDefinitionOutputDataConfig**](HyperParameterTrainingJobDefinitionOutputDataConfig.md) |  | 
**resourceConfig** | [**HyperParameterTrainingJobDefinitionResourceConfig**](HyperParameterTrainingJobDefinitionResourceConfig.md) |  | [optional] 
**stoppingCondition** | [**HyperParameterTrainingJobDefinitionStoppingCondition**](HyperParameterTrainingJobDefinitionStoppingCondition.md) |  | 
**enableNetworkIsolation** | **Boolean** |  | [optional] 
**enableInterContainerTrafficEncryption** | **Boolean** |  | [optional] 
**enableManagedSpotTraining** | **Boolean** |  | [optional] 
**checkpointConfig** | [**CheckpointConfig**](CheckpointConfig.md) |  | [optional] 
**retryStrategy** | [**CreateTrainingJobRequestRetryStrategy**](CreateTrainingJobRequestRetryStrategy.md) |  | [optional] 
**hyperParameterTuningResourceConfig** | [**HyperParameterTrainingJobDefinitionHyperParameterTuningResourceConfig**](HyperParameterTrainingJobDefinitionHyperParameterTuningResourceConfig.md) |  | [optional] 
**environment** | **Object** |  | [optional] 


