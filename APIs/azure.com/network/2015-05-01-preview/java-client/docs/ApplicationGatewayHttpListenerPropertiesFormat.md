

# ApplicationGatewayHttpListenerPropertiesFormat

Properties of Http listener of application gateway

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**frontendIPConfiguration** | [**SubResource**](SubResource.md) |  |  [optional] |
|**frontendPort** | [**SubResource**](SubResource.md) |  |  [optional] |
|**protocol** | [**ProtocolEnum**](#ProtocolEnum) | Gets or sets the protocol |  [optional] |
|**provisioningState** | **String** | Gets or sets Provisioning state of the http listener resource Updating/Deleting/Failed |  [optional] |
|**sslCertificate** | [**SubResource**](SubResource.md) |  |  [optional] |



## Enum: ProtocolEnum

| Name | Value |
|---- | -----|
| HTTP | &quot;Http&quot; |
| HTTPS | &quot;Https&quot; |



