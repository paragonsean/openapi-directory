

# InboundNatRule

A rule for NAT - exposing a VM's port (backendPort) on the public IP address using a load balancer.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backendPort** | **Integer** | The port to which the external traffic will be redirected. |  [optional] |
|**frontendPort** | **Integer** | The external endpoint port of the inbound connection. Possible values range between 1 and 65535, inclusive. If unspecified, a value will be allocated automatically. |  [optional] |
|**transportProtocol** | [**TransportProtocolEnum**](#TransportProtocolEnum) | The transport protocol for the endpoint. |  [optional] |



## Enum: TransportProtocolEnum

| Name | Value |
|---- | -----|
| TCP | &quot;Tcp&quot; |
| UDP | &quot;Udp&quot; |



