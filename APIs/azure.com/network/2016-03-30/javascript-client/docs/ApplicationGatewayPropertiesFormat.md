# NetworkManagementClient.ApplicationGatewayPropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backendAddressPools** | [**[ApplicationGatewayBackendAddressPool]**](ApplicationGatewayBackendAddressPool.md) | Gets or sets backend address pool of application gateway resource | [optional] 
**backendHttpSettingsCollection** | [**[ApplicationGatewayBackendHttpSettings]**](ApplicationGatewayBackendHttpSettings.md) | Gets or sets backend http settings of application gateway resource | [optional] 
**frontendIPConfigurations** | [**[ApplicationGatewayFrontendIPConfiguration]**](ApplicationGatewayFrontendIPConfiguration.md) | Gets or sets frontend IP addresses of application gateway resource | [optional] 
**frontendPorts** | [**[ApplicationGatewayFrontendPort]**](ApplicationGatewayFrontendPort.md) | Gets or sets frontend ports of application gateway resource | [optional] 
**gatewayIPConfigurations** | [**[ApplicationGatewayIPConfiguration]**](ApplicationGatewayIPConfiguration.md) | Gets or sets subnets of application gateway resource | [optional] 
**httpListeners** | [**[ApplicationGatewayHttpListener]**](ApplicationGatewayHttpListener.md) | Gets or sets HTTP listeners of application gateway resource | [optional] 
**operationalState** | **String** | Gets operational state of application gateway resource | [optional] [readonly] 
**probes** | [**[ApplicationGatewayProbe]**](ApplicationGatewayProbe.md) | Gets or sets probes of application gateway resource | [optional] 
**provisioningState** | **String** | Gets or sets Provisioning state of the ApplicationGateway resource Updating/Deleting/Failed | [optional] 
**requestRoutingRules** | [**[ApplicationGatewayRequestRoutingRule]**](ApplicationGatewayRequestRoutingRule.md) | Gets or sets request routing rules of application gateway resource | [optional] 
**resourceGuid** | **String** | Gets or sets resource GUID property of the ApplicationGateway resource | [optional] 
**sku** | [**ApplicationGatewaySku**](ApplicationGatewaySku.md) |  | [optional] 
**sslCertificates** | [**[ApplicationGatewaySslCertificate]**](ApplicationGatewaySslCertificate.md) | Gets or sets ssl certificates of application gateway resource | [optional] 
**urlPathMaps** | [**[ApplicationGatewayUrlPathMap]**](ApplicationGatewayUrlPathMap.md) | Gets or sets URL path map of application gateway resource | [optional] 



## Enum: OperationalStateEnum


* `Stopped` (value: `"Stopped"`)

* `Starting` (value: `"Starting"`)

* `Running` (value: `"Running"`)

* `Stopping` (value: `"Stopping"`)




