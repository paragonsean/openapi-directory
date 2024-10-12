

# ApplicationGatewayBackendHealthServerIpConfigurationPropertiesLoadBalancerInboundNatRulesInnerProperties

Properties of the inbound NAT rule.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backendIPConfiguration** | **DestinationNetworkInterfaceIPConfiguration** |  |  [optional] |
|**backendPort** | **Integer** | The port used for the internal endpoint. Acceptable values range from 1 to 65535. |  [optional] |
|**enableFloatingIP** | **Boolean** | Configures a virtual machine&#39;s endpoint for the floating IP capability required to configure a SQL AlwaysOn Availability Group. This setting is required when using the SQL AlwaysOn Availability Groups in SQL server. This setting can&#39;t be changed after you create the endpoint. |  [optional] |
|**enableTcpReset** | **Boolean** | Receive bidirectional TCP Reset on TCP flow idle timeout or unexpected connection termination. This element is only used when the protocol is set to TCP. |  [optional] |
|**frontendIPConfiguration** | **Model0** |  |  [optional] |
|**frontendPort** | **Integer** | The port for the external endpoint. Port numbers for each rule must be unique within the Load Balancer. Acceptable values range from 1 to 65534. |  [optional] |
|**idleTimeoutInMinutes** | **Integer** | The timeout for the TCP idle connection. The value can be set between 4 and 30 minutes. The default value is 4 minutes. This element is only used when the protocol is set to TCP. |  [optional] |
|**protocol** | [**ProtocolEnum**](#ProtocolEnum) | The transport protocol for the endpoint. |  [optional] |
|**provisioningState** | **ProvisioningState** |  |  [optional] |



## Enum: ProtocolEnum

| Name | Value |
|---- | -----|
| UDP | &quot;Udp&quot; |
| TCP | &quot;Tcp&quot; |
| ALL | &quot;All&quot; |



