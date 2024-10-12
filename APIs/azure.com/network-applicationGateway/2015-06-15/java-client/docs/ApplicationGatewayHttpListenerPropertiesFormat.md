

# ApplicationGatewayHttpListenerPropertiesFormat

Properties of HTTP listener of an application gateway.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**frontendIPConfiguration** | **Model0** |  |  [optional] |
|**frontendPort** | **Model0** |  |  [optional] |
|**hostName** | **String** | Host name of HTTP listener. |  [optional] |
|**protocol** | [**ProtocolEnum**](#ProtocolEnum) | Protocol. Possible values are: &#39;Http&#39; and &#39;Https&#39;. |  [optional] |
|**provisioningState** | **String** | Provisioning state of the HTTP listener resource. Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. |  [optional] |
|**requireServerNameIndication** | **Boolean** | Applicable only if protocol is https. Enables SNI for multi-hosting. |  [optional] |
|**sslCertificate** | **Model0** |  |  [optional] |



## Enum: ProtocolEnum

| Name | Value |
|---- | -----|
| HTTP | &quot;Http&quot; |
| HTTPS | &quot;Https&quot; |



