# NetworkManagementClient.InboundNatPoolPropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backendPort** | **Number** | Gets or sets a port used for internal connections on the endpoint. The localPort attribute maps the eternal port of the endpoint to an internal port on a role. This is useful in scenarios where a role must communicate to an internal component on a port that is different from the one that is exposed externally. If not specified, the value of localPort is the same as the port attribute. Set the value of localPort to &#39;*&#39; to automatically assign an unallocated port that is discoverable using the runtime API | 
**frontendIPConfiguration** | [**SubResource**](SubResource.md) |  | [optional] 
**frontendPortRangeEnd** | **Number** | Gets or sets the ending port range for the NAT pool. You can specify any port number you choose, but the port numbers specified for each role in the service must be unique. Possible values range between 1 and 65535, inclusive | 
**frontendPortRangeStart** | **Number** | Gets or sets the starting port range for the NAT pool. You can specify any port number you choose, but the port numbers specified for each role in the service must be unique. Possible values range between 1 and 65535, inclusive | 
**protocol** | **String** | Gets or sets the transport protocol for the external endpoint. Possible values are Udp or Tcp | 
**provisioningState** | **String** | Gets or sets Provisioning state of the PublicIP resource Updating/Deleting/Failed | [optional] 



## Enum: ProtocolEnum


* `Udp` (value: `"Udp"`)

* `Tcp` (value: `"Tcp"`)




