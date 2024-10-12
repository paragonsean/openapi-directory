

# Peer

This message defines attributes for a node that handles a network request. The node can be either a service or an application that sends, forwards, or receives the request. Service peers should fill in `principal` and `labels` as appropriate.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ip** | **String** | The IP address of the peer. |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | The labels associated with the peer. |  [optional] |
|**port** | **String** | The network port of the peer. |  [optional] |
|**principal** | **String** | The identity of this peer. Similar to &#x60;Request.auth.principal&#x60;, but relative to the peer instead of the request. For example, the identity associated with a load balancer that forwarded the request. |  [optional] |
|**regionCode** | **String** | The CLDR country/region code associated with the above IP address. If the IP address is private, the &#x60;region_code&#x60; should reflect the physical location where this peer is running. |  [optional] |



