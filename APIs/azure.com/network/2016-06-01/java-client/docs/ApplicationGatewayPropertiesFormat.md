

# ApplicationGatewayPropertiesFormat

Properties of Application Gateway

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authenticationCertificates** | [**List&lt;ApplicationGatewayAuthenticationCertificate&gt;**](ApplicationGatewayAuthenticationCertificate.md) | Authentication certificates of application gateway resource |  [optional] |
|**backendAddressPools** | [**List&lt;ApplicationGatewayBackendAddressPool&gt;**](ApplicationGatewayBackendAddressPool.md) | Backend address pool of application gateway resource |  [optional] |
|**backendHttpSettingsCollection** | [**List&lt;ApplicationGatewayBackendHttpSettings&gt;**](ApplicationGatewayBackendHttpSettings.md) | Backend http settings of application gateway resource |  [optional] |
|**frontendIPConfigurations** | [**List&lt;ApplicationGatewayFrontendIPConfiguration&gt;**](ApplicationGatewayFrontendIPConfiguration.md) | Frontend IP addresses of application gateway resource |  [optional] |
|**frontendPorts** | [**List&lt;ApplicationGatewayFrontendPort&gt;**](ApplicationGatewayFrontendPort.md) | Frontend ports of application gateway resource |  [optional] |
|**gatewayIPConfigurations** | [**List&lt;ApplicationGatewayIPConfiguration&gt;**](ApplicationGatewayIPConfiguration.md) | Subnets of application gateway resource |  [optional] |
|**httpListeners** | [**List&lt;ApplicationGatewayHttpListener&gt;**](ApplicationGatewayHttpListener.md) | HTTP listeners of application gateway resource |  [optional] |
|**operationalState** | [**OperationalStateEnum**](#OperationalStateEnum) | Operational state of application gateway resource |  [optional] [readonly] |
|**probes** | [**List&lt;ApplicationGatewayProbe&gt;**](ApplicationGatewayProbe.md) | Probes of application gateway resource |  [optional] |
|**provisioningState** | **String** | Provisioning state of the ApplicationGateway resource Updating/Deleting/Failed |  [optional] |
|**requestRoutingRules** | [**List&lt;ApplicationGatewayRequestRoutingRule&gt;**](ApplicationGatewayRequestRoutingRule.md) | Request routing rules of application gateway resource |  [optional] |
|**resourceGuid** | **String** | Resource guid property of the ApplicationGateway resource |  [optional] |
|**sku** | [**ApplicationGatewaySku**](ApplicationGatewaySku.md) |  |  [optional] |
|**sslCertificates** | [**List&lt;ApplicationGatewaySslCertificate&gt;**](ApplicationGatewaySslCertificate.md) | SSL certificates of application gateway resource |  [optional] |
|**sslPolicy** | [**ApplicationGatewaySslPolicy**](ApplicationGatewaySslPolicy.md) |  |  [optional] |
|**urlPathMaps** | [**List&lt;ApplicationGatewayUrlPathMap&gt;**](ApplicationGatewayUrlPathMap.md) | URL path map of application gateway resource |  [optional] |



## Enum: OperationalStateEnum

| Name | Value |
|---- | -----|
| STOPPED | &quot;Stopped&quot; |
| STARTING | &quot;Starting&quot; |
| RUNNING | &quot;Running&quot; |
| STOPPING | &quot;Stopping&quot; |



