# NetworkManagementClient.ApplicationGatewayHttpListenerPropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**frontendIPConfiguration** | [**Model0**](Model0.md) |  | [optional] 
**frontendPort** | [**Model0**](Model0.md) |  | [optional] 
**hostName** | **String** | Host name of HTTP listener. | [optional] 
**protocol** | **String** | Protocol of the HTTP listener. Possible values are &#39;Http&#39; and &#39;Https&#39;. | [optional] 
**provisioningState** | **String** | Provisioning state of the HTTP listener resource. Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. | [optional] 
**requireServerNameIndication** | **Boolean** | Applicable only if protocol is https. Enables SNI for multi-hosting. | [optional] 
**sslCertificate** | [**Model0**](Model0.md) |  | [optional] 



## Enum: ProtocolEnum


* `Http` (value: `"Http"`)

* `Https` (value: `"Https"`)




