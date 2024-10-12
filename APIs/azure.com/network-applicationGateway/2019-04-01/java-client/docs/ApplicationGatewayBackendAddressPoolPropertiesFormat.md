

# ApplicationGatewayBackendAddressPoolPropertiesFormat

Properties of Backend Address Pool of an application gateway.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backendAddresses** | [**List&lt;ApplicationGatewayBackendAddress&gt;**](ApplicationGatewayBackendAddress.md) | Backend addresses. |  [optional] |
|**backendIPConfigurations** | [**List&lt;ApplicationGatewayBackendHealthServerIpConfiguration&gt;**](ApplicationGatewayBackendHealthServerIpConfiguration.md) | Collection of references to IPs defined in network interfaces. |  [optional] |
|**provisioningState** | **String** | Provisioning state of the backend address pool resource. Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. |  [optional] |



