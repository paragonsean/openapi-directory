

# FrontDoorUpdateParameters

The properties needed to update a Front Door

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backendPools** | [**List&lt;BackendPool&gt;**](BackendPool.md) | Backend pools available to routing rules. |  [optional] |
|**backendPoolsSettings** | [**BackendPoolsSettings**](BackendPoolsSettings.md) |  |  [optional] |
|**enabledState** | [**EnabledStateEnum**](#EnabledStateEnum) | Operational status of the Front Door load balancer. Permitted values are &#39;Enabled&#39; or &#39;Disabled&#39; |  [optional] |
|**friendlyName** | **String** | A friendly name for the frontDoor |  [optional] |
|**frontendEndpoints** | [**List&lt;FrontendEndpoint&gt;**](FrontendEndpoint.md) | Frontend endpoints available to routing rules. |  [optional] |
|**healthProbeSettings** | [**List&lt;HealthProbeSettingsModel&gt;**](HealthProbeSettingsModel.md) | Health probe settings associated with this Front Door instance. |  [optional] |
|**loadBalancingSettings** | [**List&lt;LoadBalancingSettingsModel&gt;**](LoadBalancingSettingsModel.md) | Load balancing settings associated with this Front Door instance. |  [optional] |
|**routingRules** | [**List&lt;RoutingRule&gt;**](RoutingRule.md) | Routing rules associated with this Front Door. |  [optional] |



## Enum: EnabledStateEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |



