

# ApplicationGatewayHttpListenerPropertiesFormat

Properties of Http listener of application gateway

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**frontendIPConfiguration** | [**SubResource**](SubResource.md) |  |  [optional] |
|**frontendPort** | [**SubResource**](SubResource.md) |  |  [optional] |
|**hostName** | **String** | Host name of http listener  |  [optional] |
|**protocol** | [**ProtocolEnum**](#ProtocolEnum) | Protocol |  [optional] |
|**provisioningState** | **String** | Provisioning state of the http listener resource Updating/Deleting/Failed |  [optional] |
|**requireServerNameIndication** | **Boolean** | RequireServerNameIndication of http listener  |  [optional] |
|**sslCertificate** | [**SubResource**](SubResource.md) |  |  [optional] |



## Enum: ProtocolEnum

| Name | Value |
|---- | -----|
| HTTP | &quot;Http&quot; |
| HTTPS | &quot;Https&quot; |



