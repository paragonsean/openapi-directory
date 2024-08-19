

# CreateServiceResponseService


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**serviceArn** | [**String**](String.md) |  |  [optional] |
|**serviceName** | [**String**](String.md) |  |  [optional] |
|**clusterArn** | [**String**](String.md) |  |  [optional] |
|**loadBalancers** | [**List**](List.md) |  |  [optional] |
|**serviceRegistries** | [**List**](List.md) |  |  [optional] |
|**status** | [**String**](String.md) |  |  [optional] |
|**desiredCount** | [**Integer**](Integer.md) |  |  [optional] |
|**runningCount** | [**Integer**](Integer.md) |  |  [optional] |
|**pendingCount** | [**Integer**](Integer.md) |  |  [optional] |
|**launchType** | [**LaunchType**](LaunchType.md) |  |  [optional] |
|**capacityProviderStrategy** | [**List**](List.md) |  |  [optional] |
|**platformVersion** | [**String**](String.md) |  |  [optional] |
|**platformFamily** | [**String**](String.md) |  |  [optional] |
|**taskDefinition** | [**String**](String.md) |  |  [optional] |
|**deploymentConfiguration** | [**CreateServiceRequestDeploymentConfiguration**](CreateServiceRequestDeploymentConfiguration.md) |  |  [optional] |
|**taskSets** | [**List**](List.md) |  |  [optional] |
|**deployments** | [**List**](List.md) |  |  [optional] |
|**roleArn** | [**String**](String.md) |  |  [optional] |
|**events** | [**List**](List.md) |  |  [optional] |
|**createdAt** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**placementConstraints** | [**List**](List.md) |  |  [optional] |
|**placementStrategy** | [**List**](List.md) |  |  [optional] |
|**networkConfiguration** | [**StartTaskRequestNetworkConfiguration**](StartTaskRequestNetworkConfiguration.md) |  |  [optional] |
|**healthCheckGracePeriodSeconds** | [**Integer**](Integer.md) |  |  [optional] |
|**schedulingStrategy** | [**SchedulingStrategy**](SchedulingStrategy.md) |  |  [optional] |
|**deploymentController** | [**ServiceDeploymentController**](ServiceDeploymentController.md) |  |  [optional] |
|**tags** | [**List**](List.md) |  |  [optional] |
|**createdBy** | [**String**](String.md) |  |  [optional] |
|**enableECSManagedTags** | [**Boolean**](Boolean.md) |  |  [optional] |
|**propagateTags** | [**PropagateTags**](PropagateTags.md) |  |  [optional] |
|**enableExecuteCommand** | [**Boolean**](Boolean.md) |  |  [optional] |



