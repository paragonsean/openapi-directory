

# EcsParameters

The templated target type for the Amazon ECS <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_RunTask.html\"> <code>RunTask</code> </a> API operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**capacityProviderStrategy** | [**List**](List.md) |  |  [optional] |
|**enableECSManagedTags** | [**Boolean**](Boolean.md) |  |  [optional] |
|**enableExecuteCommand** | [**Boolean**](Boolean.md) |  |  [optional] |
|**group** | [**String**](String.md) |  |  [optional] |
|**launchType** | [**LaunchType**](LaunchType.md) |  |  [optional] |
|**networkConfiguration** | [**EcsParametersNetworkConfiguration**](EcsParametersNetworkConfiguration.md) |  |  [optional] |
|**placementConstraints** | [**List**](List.md) |  |  [optional] |
|**placementStrategy** | [**List**](List.md) |  |  [optional] |
|**platformVersion** | [**String**](String.md) |  |  [optional] |
|**propagateTags** | [**PropagateTags**](PropagateTags.md) |  |  [optional] |
|**referenceId** | [**String**](String.md) |  |  [optional] |
|**tags** | [**List**](List.md) |  |  [optional] |
|**taskCount** | [**Integer**](Integer.md) |  |  [optional] |
|**taskDefinitionArn** | [**String**](String.md) |  |  |



