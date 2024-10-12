# NetworkManagementClient.VerificationIPFlowParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | [**Direction**](Direction.md) |  | 
**localIPAddress** | **String** | The local IP address. Acceptable values are valid IPv4 addresses. | 
**localPort** | **String** | The local port. Acceptable values are a single integer in the range (0-65535). Support for * for the source port, which depends on the direction. | 
**protocol** | **String** | Protocol to be verified on. | 
**remoteIPAddress** | **String** | The remote IP address. Acceptable values are valid IPv4 addresses. | 
**remotePort** | **String** | The remote port. Acceptable values are a single integer in the range (0-65535). Support for * for the source port, which depends on the direction. | 
**targetNicResourceId** | **String** | The NIC ID. (If VM has multiple NICs and IP forwarding is enabled on any of them, then this parameter must be specified. Otherwise optional). | [optional] 
**targetResourceId** | **String** | The ID of the target resource to perform next-hop on. | 



## Enum: ProtocolEnum


* `TCP` (value: `"TCP"`)

* `UDP` (value: `"UDP"`)




