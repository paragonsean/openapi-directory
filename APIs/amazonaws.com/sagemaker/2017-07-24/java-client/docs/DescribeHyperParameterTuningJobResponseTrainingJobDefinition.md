

# DescribeHyperParameterTuningJobResponseTrainingJobDefinition


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**definitionName** | [**String**](String.md) |  |  [optional] |
|**tuningObjective** | [**HyperParameterTuningJobObjective**](HyperParameterTuningJobObjective.md) |  |  [optional] |
|**hyperParameterRanges** | [**ParameterRanges**](ParameterRanges.md) |  |  [optional] |
|**staticHyperParameters** | [**Map**](Map.md) |  |  [optional] |
|**algorithmSpecification** | [**HyperParameterTrainingJobDefinitionAlgorithmSpecification**](HyperParameterTrainingJobDefinitionAlgorithmSpecification.md) |  |  |
|**roleArn** | [**String**](String.md) |  |  |
|**inputDataConfig** | [**List**](List.md) |  |  [optional] |
|**vpcConfig** | [**HyperParameterTrainingJobDefinitionVpcConfig**](HyperParameterTrainingJobDefinitionVpcConfig.md) |  |  [optional] |
|**outputDataConfig** | [**HyperParameterTrainingJobDefinitionOutputDataConfig**](HyperParameterTrainingJobDefinitionOutputDataConfig.md) |  |  |
|**resourceConfig** | [**HyperParameterTrainingJobDefinitionResourceConfig**](HyperParameterTrainingJobDefinitionResourceConfig.md) |  |  [optional] |
|**stoppingCondition** | [**HyperParameterTrainingJobDefinitionStoppingCondition**](HyperParameterTrainingJobDefinitionStoppingCondition.md) |  |  |
|**enableNetworkIsolation** | [**Boolean**](Boolean.md) |  |  [optional] |
|**enableInterContainerTrafficEncryption** | [**Boolean**](Boolean.md) |  |  [optional] |
|**enableManagedSpotTraining** | [**Boolean**](Boolean.md) |  |  [optional] |
|**checkpointConfig** | [**CheckpointConfig**](CheckpointConfig.md) |  |  [optional] |
|**retryStrategy** | [**CreateTrainingJobRequestRetryStrategy**](CreateTrainingJobRequestRetryStrategy.md) |  |  [optional] |
|**hyperParameterTuningResourceConfig** | [**HyperParameterTrainingJobDefinitionHyperParameterTuningResourceConfig**](HyperParameterTrainingJobDefinitionHyperParameterTuningResourceConfig.md) |  |  [optional] |
|**environment** | [**Map**](Map.md) |  |  [optional] |



