

# ApplicationGatewayPropertiesFormat

Properties of the application gateway.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authenticationCertificates** | [**List&lt;Object&gt;**](Object.md) | Authentication certificates of the application gateway resource. For default limits, see [Application Gateway limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits). |  [optional] |
|**autoscaleConfiguration** | [**ApplicationGatewayAutoscaleConfiguration**](ApplicationGatewayAutoscaleConfiguration.md) |  |  [optional] |
|**backendAddressPools** | [**List&lt;Object&gt;**](Object.md) | Backend address pool of the application gateway resource. For default limits, see [Application Gateway limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits). |  [optional] |
|**backendHttpSettingsCollection** | [**List&lt;Object&gt;**](Object.md) | Backend http settings of the application gateway resource. For default limits, see [Application Gateway limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits). |  [optional] |
|**customErrorConfigurations** | [**List&lt;ApplicationGatewayCustomError&gt;**](ApplicationGatewayCustomError.md) | Custom error configurations of the application gateway resource. |  [optional] |
|**enableFips** | **Boolean** | Whether FIPS is enabled on the application gateway resource. |  [optional] |
|**enableHttp2** | **Boolean** | Whether HTTP2 is enabled on the application gateway resource. |  [optional] |
|**firewallPolicy** | [**ApplicationGatewayPathRulePropertiesFormatRewriteRuleSet**](ApplicationGatewayPathRulePropertiesFormatRewriteRuleSet.md) |  |  [optional] |
|**frontendIPConfigurations** | [**List&lt;Object&gt;**](Object.md) | Frontend IP addresses of the application gateway resource. For default limits, see [Application Gateway limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits). |  [optional] |
|**frontendPorts** | [**List&lt;Object&gt;**](Object.md) | Frontend ports of the application gateway resource. For default limits, see [Application Gateway limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits). |  [optional] |
|**gatewayIPConfigurations** | [**List&lt;Object&gt;**](Object.md) | Subnets of the application gateway resource. For default limits, see [Application Gateway limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits). |  [optional] |
|**httpListeners** | [**List&lt;Object&gt;**](Object.md) | Http listeners of the application gateway resource. For default limits, see [Application Gateway limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits). |  [optional] |
|**operationalState** | [**OperationalStateEnum**](#OperationalStateEnum) | Operational state of the application gateway resource. |  [optional] [readonly] |
|**probes** | [**List&lt;Object&gt;**](Object.md) | Probes of the application gateway resource. |  [optional] |
|**provisioningState** | **String** | Provisioning state of the application gateway resource. Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. |  [optional] |
|**redirectConfigurations** | [**List&lt;Object&gt;**](Object.md) | Redirect configurations of the application gateway resource. For default limits, see [Application Gateway limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits). |  [optional] |
|**requestRoutingRules** | [**List&lt;Object&gt;**](Object.md) | Request routing rules of the application gateway resource. |  [optional] |
|**resourceGuid** | **String** | Resource GUID property of the application gateway resource. |  [optional] |
|**rewriteRuleSets** | [**List&lt;Object&gt;**](Object.md) | Rewrite rules for the application gateway resource. |  [optional] |
|**sku** | [**ApplicationGatewaySku**](ApplicationGatewaySku.md) |  |  [optional] |
|**sslCertificates** | [**List&lt;Object&gt;**](Object.md) | SSL certificates of the application gateway resource. For default limits, see [Application Gateway limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits). |  [optional] |
|**sslPolicy** | [**ApplicationGatewaySslPolicy**](ApplicationGatewaySslPolicy.md) |  |  [optional] |
|**trustedRootCertificates** | [**List&lt;Object&gt;**](Object.md) | Trusted Root certificates of the application gateway resource. For default limits, see [Application Gateway limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits). |  [optional] |
|**urlPathMaps** | [**List&lt;Object&gt;**](Object.md) | URL path map of the application gateway resource. For default limits, see [Application Gateway limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits). |  [optional] |
|**webApplicationFirewallConfiguration** | [**ApplicationGatewayWebApplicationFirewallConfiguration**](ApplicationGatewayWebApplicationFirewallConfiguration.md) |  |  [optional] |



## Enum: OperationalStateEnum

| Name | Value |
|---- | -----|
| STOPPED | &quot;Stopped&quot; |
| STARTING | &quot;Starting&quot; |
| RUNNING | &quot;Running&quot; |
| STOPPING | &quot;Stopping&quot; |



