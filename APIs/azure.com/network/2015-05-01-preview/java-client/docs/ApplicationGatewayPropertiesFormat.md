

# ApplicationGatewayPropertiesFormat

Properties of Application Gateway

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backendAddressPools** | [**List&lt;ApplicationGatewayBackendAddressPool&gt;**](ApplicationGatewayBackendAddressPool.md) | Gets or sets backend address pool of application gateway resource |  [optional] |
|**backendHttpSettingsCollection** | [**List&lt;ApplicationGatewayBackendHttpSettings&gt;**](ApplicationGatewayBackendHttpSettings.md) | Gets or sets backend http settings of application gateway resource |  [optional] |
|**frontendIPConfigurations** | [**List&lt;ApplicationGatewayFrontendIPConfiguration&gt;**](ApplicationGatewayFrontendIPConfiguration.md) | Gets or sets frontend IP addresses of application gateway resource |  [optional] |
|**frontendPorts** | [**List&lt;ApplicationGatewayFrontendPort&gt;**](ApplicationGatewayFrontendPort.md) | Gets or sets frontend ports of application gateway resource |  [optional] |
|**gatewayIPConfigurations** | [**List&lt;ApplicationGatewayIPConfiguration&gt;**](ApplicationGatewayIPConfiguration.md) | Gets or sets subnets of application gateway resource |  [optional] |
|**httpListeners** | [**List&lt;ApplicationGatewayHttpListener&gt;**](ApplicationGatewayHttpListener.md) | Gets or sets HTTP listeners of application gateway resource |  [optional] |
|**operationalState** | [**OperationalStateEnum**](#OperationalStateEnum) | Gets operational state of application gateway resource |  [optional] [readonly] |
|**provisioningState** | **String** | Gets or sets Provisioning state of the ApplicationGateway resource Updating/Deleting/Failed |  [optional] |
|**requestRoutingRules** | [**List&lt;ApplicationGatewayRequestRoutingRule&gt;**](ApplicationGatewayRequestRoutingRule.md) | Gets or sets request routing rules of application gateway resource |  [optional] |
|**resourceGuid** | **String** | Gets or sets resource guid property of the ApplicationGateway resource |  [optional] |
|**sku** | [**ApplicationGatewaySku**](ApplicationGatewaySku.md) |  |  [optional] |
|**sslCertificates** | [**List&lt;ApplicationGatewaySslCertificate&gt;**](ApplicationGatewaySslCertificate.md) | Gets or sets ssl certificates of application gateway resource |  [optional] |



## Enum: OperationalStateEnum

| Name | Value |
|---- | -----|
| STOPPED | &quot;Stopped&quot; |
| STARTING | &quot;Starting&quot; |
| RUNNING | &quot;Running&quot; |
| STOPPING | &quot;Stopping&quot; |



