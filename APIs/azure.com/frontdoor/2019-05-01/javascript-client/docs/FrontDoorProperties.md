# FrontDoorManagementClient.FrontDoorProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cname** | **String** | The host that each frontendEndpoint must CNAME to. | [optional] [readonly] 
**provisioningState** | **String** | Provisioning state of the Front Door. | [optional] [readonly] 
**resourceState** | [**ResourceState**](ResourceState.md) |  | [optional] 
**backendPools** | [**[BackendPool]**](BackendPool.md) | Backend pools available to routing rules. | [optional] 
**backendPoolsSettings** | [**BackendPoolsSettings**](BackendPoolsSettings.md) |  | [optional] 
**enabledState** | **String** | Operational status of the Front Door load balancer. Permitted values are &#39;Enabled&#39; or &#39;Disabled&#39; | [optional] 
**friendlyName** | **String** | A friendly name for the frontDoor | [optional] 
**frontendEndpoints** | [**[FrontendEndpoint]**](FrontendEndpoint.md) | Frontend endpoints available to routing rules. | [optional] 
**healthProbeSettings** | [**[HealthProbeSettingsModel]**](HealthProbeSettingsModel.md) | Health probe settings associated with this Front Door instance. | [optional] 
**loadBalancingSettings** | [**[LoadBalancingSettingsModel]**](LoadBalancingSettingsModel.md) | Load balancing settings associated with this Front Door instance. | [optional] 
**routingRules** | [**[RoutingRule]**](RoutingRule.md) | Routing rules associated with this Front Door. | [optional] 



## Enum: EnabledStateEnum


* `Enabled` (value: `"Enabled"`)

* `Disabled` (value: `"Disabled"`)




