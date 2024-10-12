# NetworkManagementClient.BgpPeerStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asn** | **Number** | The autonomous system number of the remote BGP peer | [optional] [readonly] 
**connectedDuration** | **String** | For how long the peering has been up | [optional] [readonly] 
**localAddress** | **String** | The virtual network gateway&#39;s local address | [optional] [readonly] 
**messagesReceived** | **Number** | The number of BGP messages received | [optional] [readonly] 
**messagesSent** | **Number** | The number of BGP messages sent | [optional] [readonly] 
**neighbor** | **String** | The remote BGP peer | [optional] [readonly] 
**routesReceived** | **Number** | The number of routes learned from this peer | [optional] [readonly] 
**state** | **String** | The BGP peer state | [optional] [readonly] 



## Enum: StateEnum


* `Unknown` (value: `"Unknown"`)

* `Stopped` (value: `"Stopped"`)

* `Idle` (value: `"Idle"`)

* `Connecting` (value: `"Connecting"`)

* `Connected` (value: `"Connected"`)




