

# CreateTrainingJobRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**trainingJobName** | [**String**](String.md) |  |  |
|**hyperParameters** | [**Map**](Map.md) |  |  [optional] |
|**algorithmSpecification** | [**CreateTrainingJobRequestAlgorithmSpecification**](CreateTrainingJobRequestAlgorithmSpecification.md) |  |  |
|**roleArn** | [**String**](String.md) |  |  |
|**inputDataConfig** | [**List**](List.md) |  |  [optional] |
|**outputDataConfig** | [**CreateTrainingJobRequestOutputDataConfig**](CreateTrainingJobRequestOutputDataConfig.md) |  |  |
|**resourceConfig** | [**CreateTrainingJobRequestResourceConfig**](CreateTrainingJobRequestResourceConfig.md) |  |  |
|**vpcConfig** | [**CreateTrainingJobRequestVpcConfig**](CreateTrainingJobRequestVpcConfig.md) |  |  [optional] |
|**stoppingCondition** | [**CreateTrainingJobRequestStoppingCondition**](CreateTrainingJobRequestStoppingCondition.md) |  |  |
|**tags** | [**List**](List.md) |  |  [optional] |
|**enableNetworkIsolation** | [**Boolean**](Boolean.md) |  |  [optional] |
|**enableInterContainerTrafficEncryption** | [**Boolean**](Boolean.md) |  |  [optional] |
|**enableManagedSpotTraining** | [**Boolean**](Boolean.md) |  |  [optional] |
|**checkpointConfig** | [**CreateTrainingJobRequestCheckpointConfig**](CreateTrainingJobRequestCheckpointConfig.md) |  |  [optional] |
|**debugHookConfig** | [**DebugHookConfig**](DebugHookConfig.md) |  |  [optional] |
|**debugRuleConfigurations** | [**List**](List.md) |  |  [optional] |
|**tensorBoardOutputConfig** | [**TensorBoardOutputConfig**](TensorBoardOutputConfig.md) |  |  [optional] |
|**experimentConfig** | [**ExperimentConfig**](ExperimentConfig.md) |  |  [optional] |
|**profilerConfig** | [**ProfilerConfig**](ProfilerConfig.md) |  |  [optional] |
|**profilerRuleConfigurations** | [**List**](List.md) |  |  [optional] |
|**environment** | [**Map**](Map.md) |  |  [optional] |
|**retryStrategy** | [**CreateTrainingJobRequestRetryStrategy**](CreateTrainingJobRequestRetryStrategy.md) |  |  [optional] |



