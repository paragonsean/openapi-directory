# NetworkManagementClient.ApplicationGatewayBackendHealthServerIpConfigurationPropertiesLoadBalancerInboundNatRulesInnerProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backendIPConfiguration** | [**Items**](Items.md) |  | [optional] 
**backendPort** | **Number** | The port used for the internal endpoint. Acceptable values range from 1 to 65535. | [optional] 
**enableFloatingIP** | **Boolean** | Configures a virtual machine&#39;s endpoint for the floating IP capability required to configure a SQL AlwaysOn Availability Group. This setting is required when using the SQL AlwaysOn Availability Groups in SQL server. This setting can&#39;t be changed after you create the endpoint. | [optional] 
**frontendIPConfiguration** | [**Model0**](Model0.md) |  | [optional] 
**frontendPort** | **Number** | The port for the external endpoint. Port numbers for each rule must be unique within the Load Balancer. Acceptable values range from 1 to 65534. | [optional] 
**idleTimeoutInMinutes** | **Number** | The timeout for the TCP idle connection. The value can be set between 4 and 30 minutes. The default value is 4 minutes. This element is only used when the protocol is set to TCP. | [optional] 
**protocol** | **String** | The transport protocol for the endpoint. Possible values are &#39;Udp&#39; or &#39;Tcp&#39; or &#39;All&#39;. | [optional] 
**provisioningState** | **String** | Gets the provisioning state of the public IP resource. Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. | [optional] 



## Enum: ProtocolEnum


* `Udp` (value: `"Udp"`)

* `Tcp` (value: `"Tcp"`)

* `All` (value: `"All"`)




