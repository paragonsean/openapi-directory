# NetworkManagementClient.ProbePropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**intervalInSeconds** | **Number** | Gets or sets the interval, in seconds, for how frequently to probe the endpoint for health status. Typically, the interval is slightly less than half the allocated timeout period (in seconds) which allows two full probes before taking the instance out of rotation. The default value is 15, the minimum value is 5 | [optional] 
**loadBalancingRules** | [**[SubResource]**](SubResource.md) | Gets Load balancer rules that use this probe | [optional] 
**numberOfProbes** | **Number** | Gets or sets the number of probes where if no response, will result in stopping further traffic from being delivered to the endpoint. This values allows endpoints to be taken out of rotation faster or slower than the typical times used in Azure.  | [optional] 
**port** | **Number** | Gets or sets Port for communicating the probe. Possible values range from 1 to 65535, inclusive. | 
**protocol** | **String** | Gets or sets the protocol of the end point. Possible values are http pr Tcp. If Tcp is specified, a received ACK is required for the probe to be successful. If http is specified,a 200 OK response from the specifies URI is required for the probe to be successful | 
**provisioningState** | **String** | Gets or sets Provisioning state of the PublicIP resource Updating/Deleting/Failed | [optional] 
**requestPath** | **String** | Gets or sets the URI used for requesting health status from the VM. Path is required if a protocol is set to http. Otherwise, it is not allowed. There is no default value | [optional] 



## Enum: ProtocolEnum


* `Http` (value: `"Http"`)

* `Tcp` (value: `"Tcp"`)




