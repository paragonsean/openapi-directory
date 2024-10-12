# ServiceControlApi.Peer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **String** | The IP address of the peer. | [optional] 
**labels** | **{String: String}** | The labels associated with the peer. | [optional] 
**port** | **String** | The network port of the peer. | [optional] 
**principal** | **String** | The identity of this peer. Similar to &#x60;Request.auth.principal&#x60;, but relative to the peer instead of the request. For example, the identity associated with a load balancer that forwarded the request. | [optional] 
**regionCode** | **String** | The CLDR country/region code associated with the above IP address. If the IP address is private, the &#x60;region_code&#x60; should reflect the physical location where this peer is running. | [optional] 


