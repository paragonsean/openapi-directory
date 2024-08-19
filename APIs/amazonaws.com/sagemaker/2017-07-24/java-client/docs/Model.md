

# Model

The properties of a model as returned by the <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Search.html\">Search</a> API.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**modelName** | [**String**](String.md) |  |  [optional] |
|**primaryContainer** | [**ContainerDefinition**](ContainerDefinition.md) |  |  [optional] |
|**containers** | [**List**](List.md) |  |  [optional] |
|**inferenceExecutionConfig** | [**InferenceExecutionConfig**](InferenceExecutionConfig.md) |  |  [optional] |
|**executionRoleArn** | [**String**](String.md) |  |  [optional] |
|**vpcConfig** | [**VpcConfig**](VpcConfig.md) |  |  [optional] |
|**creationTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**modelArn** | [**String**](String.md) |  |  [optional] |
|**enableNetworkIsolation** | [**Boolean**](Boolean.md) |  |  [optional] |
|**tags** | [**List**](List.md) |  |  [optional] |
|**deploymentRecommendation** | [**DescribeModelOutputDeploymentRecommendation**](DescribeModelOutputDeploymentRecommendation.md) |  |  [optional] |



