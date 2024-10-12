# MerakiDashboardApi.UpdateNetworkApplianceVpnSiteToSiteVpnRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hubs** | [**[UpdateNetworkApplianceVpnSiteToSiteVpnRequestHubsInner]**](UpdateNetworkApplianceVpnSiteToSiteVpnRequestHubsInner.md) | The list of VPN hubs, in order of preference. In spoke mode, at least 1 hub is required. | [optional] 
**mode** | **String** | The site-to-site VPN mode. Can be one of &#39;none&#39;, &#39;spoke&#39; or &#39;hub&#39; | 
**subnets** | [**[UpdateNetworkApplianceVpnSiteToSiteVpnRequestSubnetsInner]**](UpdateNetworkApplianceVpnSiteToSiteVpnRequestSubnetsInner.md) | The list of subnets and their VPN presence. | [optional] 



## Enum: ModeEnum


* `hub` (value: `"hub"`)

* `none` (value: `"none"`)

* `spoke` (value: `"spoke"`)




