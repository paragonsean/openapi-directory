# AmazonEc2ContainerService.Service

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**serviceArn** | **String** |  | [optional] 
**serviceName** | **String** |  | [optional] 
**clusterArn** | **String** |  | [optional] 
**loadBalancers** | **Array** |  | [optional] 
**serviceRegistries** | **Array** |  | [optional] 
**status** | **String** |  | [optional] 
**desiredCount** | **Number** |  | [optional] 
**runningCount** | **Number** |  | [optional] 
**pendingCount** | **Number** |  | [optional] 
**launchType** | [**LaunchType**](LaunchType.md) |  | [optional] 
**capacityProviderStrategy** | **Array** |  | [optional] 
**platformVersion** | **String** |  | [optional] 
**platformFamily** | **String** |  | [optional] 
**taskDefinition** | **String** |  | [optional] 
**deploymentConfiguration** | [**CreateServiceRequestDeploymentConfiguration**](CreateServiceRequestDeploymentConfiguration.md) |  | [optional] 
**taskSets** | **Array** |  | [optional] 
**deployments** | **Array** |  | [optional] 
**roleArn** | **String** |  | [optional] 
**events** | **Array** |  | [optional] 
**createdAt** | **Date** |  | [optional] 
**placementConstraints** | **Array** |  | [optional] 
**placementStrategy** | **Array** |  | [optional] 
**networkConfiguration** | [**StartTaskRequestNetworkConfiguration**](StartTaskRequestNetworkConfiguration.md) |  | [optional] 
**healthCheckGracePeriodSeconds** | **Number** |  | [optional] 
**schedulingStrategy** | [**SchedulingStrategy**](SchedulingStrategy.md) |  | [optional] 
**deploymentController** | [**ServiceDeploymentController**](ServiceDeploymentController.md) |  | [optional] 
**tags** | **Array** |  | [optional] 
**createdBy** | **String** |  | [optional] 
**enableECSManagedTags** | **Boolean** |  | [optional] 
**propagateTags** | [**PropagateTags**](PropagateTags.md) |  | [optional] 
**enableExecuteCommand** | **Boolean** |  | [optional] 


