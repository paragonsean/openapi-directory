

# UpdateNetworkApplianceVpnSiteToSiteVpnRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**hubs** | [**List&lt;UpdateNetworkApplianceVpnSiteToSiteVpnRequestHubsInner&gt;**](UpdateNetworkApplianceVpnSiteToSiteVpnRequestHubsInner.md) | The list of VPN hubs, in order of preference. In spoke mode, at least 1 hub is required. |  [optional] |
|**mode** | [**ModeEnum**](#ModeEnum) | The site-to-site VPN mode. Can be one of &#39;none&#39;, &#39;spoke&#39; or &#39;hub&#39; |  |
|**subnets** | [**List&lt;UpdateNetworkApplianceVpnSiteToSiteVpnRequestSubnetsInner&gt;**](UpdateNetworkApplianceVpnSiteToSiteVpnRequestSubnetsInner.md) | The list of subnets and their VPN presence. |  [optional] |



## Enum: ModeEnum

| Name | Value |
|---- | -----|
| HUB | &quot;hub&quot; |
| NONE | &quot;none&quot; |
| SPOKE | &quot;spoke&quot; |



