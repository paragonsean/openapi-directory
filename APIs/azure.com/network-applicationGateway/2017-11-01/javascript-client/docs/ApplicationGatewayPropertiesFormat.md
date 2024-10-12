# NetworkManagementClient.ApplicationGatewayPropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authenticationCertificates** | **[Object]** | Authentication certificates of the application gateway resource. | [optional] 
**backendAddressPools** | **[Object]** | Backend address pool of the application gateway resource. | [optional] 
**backendHttpSettingsCollection** | **[Object]** | Backend http settings of the application gateway resource. | [optional] 
**enableHttp2** | **Boolean** | Whether HTTP2 is enabled on the application gateway resource. | [optional] 
**frontendIPConfigurations** | **[Object]** | Frontend IP addresses of the application gateway resource. | [optional] 
**frontendPorts** | **[Object]** | Frontend ports of the application gateway resource. | [optional] 
**gatewayIPConfigurations** | **[Object]** | Subnets of application the gateway resource. | [optional] 
**httpListeners** | **[Object]** | Http listeners of the application gateway resource. | [optional] 
**operationalState** | **String** | Operational state of the application gateway resource. | [optional] [readonly] 
**probes** | **[Object]** | Probes of the application gateway resource. | [optional] 
**provisioningState** | **String** | Provisioning state of the application gateway resource. Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. | [optional] 
**redirectConfigurations** | **[Object]** | Redirect configurations of the application gateway resource. | [optional] 
**requestRoutingRules** | **[Object]** | Request routing rules of the application gateway resource. | [optional] 
**resourceGuid** | **String** | Resource GUID property of the application gateway resource. | [optional] 
**sku** | [**ApplicationGatewaySku**](ApplicationGatewaySku.md) |  | [optional] 
**sslCertificates** | **[Object]** | SSL certificates of the application gateway resource. | [optional] 
**sslPolicy** | [**ApplicationGatewaySslPolicy**](ApplicationGatewaySslPolicy.md) |  | [optional] 
**urlPathMaps** | **[Object]** | URL path map of the application gateway resource. | [optional] 
**webApplicationFirewallConfiguration** | [**ApplicationGatewayWebApplicationFirewallConfiguration**](ApplicationGatewayWebApplicationFirewallConfiguration.md) |  | [optional] 



## Enum: OperationalStateEnum


* `Stopped` (value: `"Stopped"`)

* `Starting` (value: `"Starting"`)

* `Running` (value: `"Running"`)

* `Stopping` (value: `"Stopping"`)




