

# ApplicationGatewayPropertiesFormat

Properties of the application gateway.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authenticationCertificates** | [**List&lt;Object&gt;**](Object.md) | Authentication certificates of the application gateway resource. |  [optional] |
|**backendAddressPools** | [**List&lt;Object&gt;**](Object.md) | Backend address pool of the application gateway resource. |  [optional] |
|**backendHttpSettingsCollection** | [**List&lt;Object&gt;**](Object.md) | Backend http settings of the application gateway resource. |  [optional] |
|**frontendIPConfigurations** | [**List&lt;Object&gt;**](Object.md) | Frontend IP addresses of the application gateway resource. |  [optional] |
|**frontendPorts** | [**List&lt;Object&gt;**](Object.md) | Frontend ports of the application gateway resource. |  [optional] |
|**gatewayIPConfigurations** | [**List&lt;Object&gt;**](Object.md) | Subnets of application the gateway resource. |  [optional] |
|**httpListeners** | [**List&lt;Object&gt;**](Object.md) | Http listeners of the application gateway resource. |  [optional] |
|**operationalState** | [**OperationalStateEnum**](#OperationalStateEnum) | Operational state of the application gateway resource. Possible values are: &#39;Stopped&#39;, &#39;Started&#39;, &#39;Running&#39;, and &#39;Stopping&#39;. |  [optional] [readonly] |
|**probes** | [**List&lt;Object&gt;**](Object.md) | Probes of the application gateway resource. |  [optional] |
|**provisioningState** | **String** | Provisioning state of the application gateway resource. Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. |  [optional] |
|**requestRoutingRules** | [**List&lt;Object&gt;**](Object.md) | Request routing rules of the application gateway resource. |  [optional] |
|**resourceGuid** | **String** | Resource GUID property of the application gateway resource. |  [optional] |
|**sku** | [**ApplicationGatewaySku**](ApplicationGatewaySku.md) |  |  [optional] |
|**sslCertificates** | [**List&lt;Object&gt;**](Object.md) | SSL certificates of the application gateway resource. |  [optional] |
|**sslPolicy** | [**ApplicationGatewaySslPolicy**](ApplicationGatewaySslPolicy.md) |  |  [optional] |
|**urlPathMaps** | [**List&lt;Object&gt;**](Object.md) | URL path map of the application gateway resource. |  [optional] |
|**webApplicationFirewallConfiguration** | [**ApplicationGatewayWebApplicationFirewallConfiguration**](ApplicationGatewayWebApplicationFirewallConfiguration.md) |  |  [optional] |



## Enum: OperationalStateEnum

| Name | Value |
|---- | -----|
| STOPPED | &quot;Stopped&quot; |
| STARTING | &quot;Starting&quot; |
| RUNNING | &quot;Running&quot; |
| STOPPING | &quot;Stopping&quot; |



