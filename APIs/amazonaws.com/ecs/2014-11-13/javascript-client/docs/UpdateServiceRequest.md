# AmazonEc2ContainerService.UpdateServiceRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster** | **String** |  | [optional] 
**service** | **String** |  | 
**desiredCount** | **Number** |  | [optional] 
**taskDefinition** | **String** |  | [optional] 
**capacityProviderStrategy** | **Array** |  | [optional] 
**deploymentConfiguration** | [**CreateServiceRequestDeploymentConfiguration**](CreateServiceRequestDeploymentConfiguration.md) |  | [optional] 
**networkConfiguration** | [**UpdateServiceRequestNetworkConfiguration**](UpdateServiceRequestNetworkConfiguration.md) |  | [optional] 
**placementConstraints** | **Array** |  | [optional] 
**placementStrategy** | **Array** |  | [optional] 
**platformVersion** | **String** |  | [optional] 
**forceNewDeployment** | **Boolean** |  | [optional] 
**healthCheckGracePeriodSeconds** | **Number** |  | [optional] 
**enableExecuteCommand** | **Boolean** |  | [optional] 
**enableECSManagedTags** | **Boolean** |  | [optional] 
**loadBalancers** | **Array** |  | [optional] 
**propagateTags** | [**PropagateTags**](PropagateTags.md) |  | [optional] 
**serviceRegistries** | **Array** |  | [optional] 
**serviceConnectConfiguration** | [**CreateServiceRequestServiceConnectConfiguration**](CreateServiceRequestServiceConnectConfiguration.md) |  | [optional] 


