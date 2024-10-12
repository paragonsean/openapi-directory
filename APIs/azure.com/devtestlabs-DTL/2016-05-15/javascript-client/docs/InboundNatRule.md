# DevTestLabsClient.InboundNatRule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backendPort** | **Number** | The port to which the external traffic will be redirected. | [optional] 
**frontendPort** | **Number** | The external endpoint port of the inbound connection. Possible values range between 1 and 65535, inclusive. If unspecified, a value will be allocated automatically. | [optional] 
**transportProtocol** | **String** | The transport protocol for the endpoint. | [optional] 



## Enum: TransportProtocolEnum


* `Tcp` (value: `"Tcp"`)

* `Udp` (value: `"Udp"`)




