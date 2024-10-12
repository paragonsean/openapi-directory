# NetworkManagementClient.LoadBalancingRulePropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backendAddressPool** | [**SubResource**](SubResource.md) |  | [optional] 
**backendPort** | **Number** | Gets or sets a port used for internal connections on the endpoint. The localPort attribute maps the eternal port of the endpoint to an internal port on a role. This is useful in scenarios where a role must communicate to an internal component on a port that is different from the one that is exposed externally. If not specified, the value of localPort is the same as the port attribute. Set the value of localPort to &#39;*&#39; to automatically assign an unallocated port that is discoverable using the runtime API | [optional] 
**enableFloatingIP** | **Boolean** | Configures a virtual machine&#39;s endpoint for the floating IP capability required to configure a SQL AlwaysOn availability Group. This setting is required when using the SQL Always ON availability Groups in SQL server. This setting can&#39;t be changed after you create the endpoint | [optional] 
**frontendIPConfiguration** | [**SubResource**](SubResource.md) |  | [optional] 
**frontendPort** | **Number** | Gets or sets the port for the external endpoint. You can specify any port number you choose, but the port numbers specified for each role in the service must be unique. Possible values range between 1 and 65535, inclusive | 
**idleTimeoutInMinutes** | **Number** | Gets or sets the timeout for the Tcp idle connection. The value can be set between 4 and 30 minutes. The default value is 4 minutes. This element is only used when the protocol is set to Tcp | [optional] 
**loadDistribution** | **String** | Gets or sets the load distribution policy for this rule | [optional] 
**probe** | [**SubResource**](SubResource.md) |  | [optional] 
**protocol** | **String** | Gets or sets the transport protocol for the external endpoint. Possible values are Udp or Tcp | 
**provisioningState** | **String** | Gets provisioning state of the PublicIP resource Updating/Deleting/Failed | [optional] 



## Enum: LoadDistributionEnum


* `Default` (value: `"Default"`)

* `SourceIP` (value: `"SourceIP"`)

* `SourceIPProtocol` (value: `"SourceIPProtocol"`)





## Enum: ProtocolEnum


* `Udp` (value: `"Udp"`)

* `Tcp` (value: `"Tcp"`)




