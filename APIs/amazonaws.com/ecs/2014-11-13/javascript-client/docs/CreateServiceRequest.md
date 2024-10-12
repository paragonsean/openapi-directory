# AmazonEc2ContainerService.CreateServiceRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster** | **String** |  | [optional] 
**serviceName** | **String** |  | 
**taskDefinition** | **String** |  | [optional] 
**loadBalancers** | **Array** |  | [optional] 
**serviceRegistries** | **Array** |  | [optional] 
**desiredCount** | **Number** |  | [optional] 
**clientToken** | **String** |  | [optional] 
**launchType** | [**LaunchType**](LaunchType.md) |  | [optional] 
**capacityProviderStrategy** | **Array** |  | [optional] 
**platformVersion** | **String** |  | [optional] 
**role** | **String** |  | [optional] 
**deploymentConfiguration** | [**CreateServiceRequestDeploymentConfiguration**](CreateServiceRequestDeploymentConfiguration.md) |  | [optional] 
**placementConstraints** | **Array** |  | [optional] 
**placementStrategy** | **Array** |  | [optional] 
**networkConfiguration** | [**CreateServiceRequestNetworkConfiguration**](CreateServiceRequestNetworkConfiguration.md) |  | [optional] 
**healthCheckGracePeriodSeconds** | **Number** |  | [optional] 
**schedulingStrategy** | [**SchedulingStrategy**](SchedulingStrategy.md) |  | [optional] 
**deploymentController** | [**CreateServiceRequestDeploymentController**](CreateServiceRequestDeploymentController.md) |  | [optional] 
**tags** | **Array** |  | [optional] 
**enableECSManagedTags** | **Boolean** |  | [optional] 
**propagateTags** | [**PropagateTags**](PropagateTags.md) |  | [optional] 
**enableExecuteCommand** | **Boolean** |  | [optional] 
**serviceConnectConfiguration** | [**CreateServiceRequestServiceConnectConfiguration**](CreateServiceRequestServiceConnectConfiguration.md) |  | [optional] 


