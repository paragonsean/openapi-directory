# NetworkManagementClient.TunnelConnectionHealth

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connectionStatus** | **String** | Virtual network Gateway connection status | [optional] [readonly] 
**egressBytesTransferred** | **Number** | The Egress Bytes Transferred in this connection | [optional] [readonly] 
**ingressBytesTransferred** | **Number** | The Ingress Bytes Transferred in this connection | [optional] [readonly] 
**lastConnectionEstablishedUtcTime** | **String** | The time at which connection was established in Utc format. | [optional] [readonly] 
**tunnel** | **String** | Tunnel name. | [optional] [readonly] 



## Enum: ConnectionStatusEnum


* `Unknown` (value: `"Unknown"`)

* `Connecting` (value: `"Connecting"`)

* `Connected` (value: `"Connected"`)

* `NotConnected` (value: `"NotConnected"`)




