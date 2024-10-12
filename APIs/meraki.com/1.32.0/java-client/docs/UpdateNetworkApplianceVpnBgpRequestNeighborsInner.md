

# UpdateNetworkApplianceVpnBgpRequestNeighborsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowTransit** | **Boolean** | When this feature is on, the Meraki device will advertise routes learned from other Autonomous Systems, thereby allowing traffic between Autonomous Systems to transit this AS. When absent, it defaults to false. |  [optional] |
|**ebgpHoldTimer** | **Integer** | The EBGP hold timer in seconds for each neighbor. The EBGP hold timer must be an integer between 12 and 240. |  |
|**ebgpMultihop** | **Integer** | Configure this if the neighbor is not adjacent. The EBGP multi-hop must be an integer between 1 and 255. |  |
|**ip** | **String** | The IPv4 address of the neighbor |  [optional] |
|**ipv6** | [**UpdateNetworkApplianceVpnBgpRequestNeighborsInnerIpv6**](UpdateNetworkApplianceVpnBgpRequestNeighborsInnerIpv6.md) |  |  [optional] |
|**receiveLimit** | **Integer** | The receive limit is the maximum number of routes that can be received from any BGP peer. The receive limit must be an integer between 0 and 4294967295. When absent, it defaults to 0. |  [optional] |
|**remoteAsNumber** | **Integer** | Remote ASN of the neighbor. The remote ASN must be an integer between 1 and 4294967295. |  |



