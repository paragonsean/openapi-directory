# NetworkManagementClient.ApplicationGatewayPropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authenticationCertificates** | [**[ApplicationGatewayAuthenticationCertificate]**](ApplicationGatewayAuthenticationCertificate.md) | Authentication certificates of application gateway resource | [optional] 
**backendAddressPools** | [**[ApplicationGatewayBackendAddressPool]**](ApplicationGatewayBackendAddressPool.md) | Backend address pool of application gateway resource | [optional] 
**backendHttpSettingsCollection** | [**[ApplicationGatewayBackendHttpSettings]**](ApplicationGatewayBackendHttpSettings.md) | Backend http settings of application gateway resource | [optional] 
**frontendIPConfigurations** | [**[ApplicationGatewayFrontendIPConfiguration]**](ApplicationGatewayFrontendIPConfiguration.md) | Frontend IP addresses of application gateway resource | [optional] 
**frontendPorts** | [**[ApplicationGatewayFrontendPort]**](ApplicationGatewayFrontendPort.md) | Frontend ports of application gateway resource | [optional] 
**gatewayIPConfigurations** | [**[ApplicationGatewayIPConfiguration]**](ApplicationGatewayIPConfiguration.md) | Subnets of application gateway resource | [optional] 
**httpListeners** | [**[ApplicationGatewayHttpListener]**](ApplicationGatewayHttpListener.md) | HTTP listeners of application gateway resource | [optional] 
**operationalState** | **String** | Operational state of application gateway resource | [optional] [readonly] 
**probes** | [**[ApplicationGatewayProbe]**](ApplicationGatewayProbe.md) | Probes of application gateway resource | [optional] 
**provisioningState** | **String** | Provisioning state of the ApplicationGateway resource Updating/Deleting/Failed | [optional] 
**requestRoutingRules** | [**[ApplicationGatewayRequestRoutingRule]**](ApplicationGatewayRequestRoutingRule.md) | Request routing rules of application gateway resource | [optional] 
**resourceGuid** | **String** | Resource guid property of the ApplicationGateway resource | [optional] 
**sku** | [**ApplicationGatewaySku**](ApplicationGatewaySku.md) |  | [optional] 
**sslCertificates** | [**[ApplicationGatewaySslCertificate]**](ApplicationGatewaySslCertificate.md) | SSL certificates of application gateway resource | [optional] 
**sslPolicy** | [**ApplicationGatewaySslPolicy**](ApplicationGatewaySslPolicy.md) |  | [optional] 
**urlPathMaps** | [**[ApplicationGatewayUrlPathMap]**](ApplicationGatewayUrlPathMap.md) | URL path map of application gateway resource | [optional] 



## Enum: OperationalStateEnum


* `Stopped` (value: `"Stopped"`)

* `Starting` (value: `"Starting"`)

* `Running` (value: `"Running"`)

* `Stopping` (value: `"Stopping"`)




