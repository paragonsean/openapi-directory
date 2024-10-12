# MerakiDashboardApi.UpdateNetworkSwitchDhcpServerPolicyRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alerts** | [**UpdateNetworkSwitchDhcpServerPolicyRequestAlerts**](UpdateNetworkSwitchDhcpServerPolicyRequestAlerts.md) |  | [optional] 
**allowedServers** | **[String]** | List the MAC addresses of DHCP servers to permit on the network when defaultPolicy is set to block. An empty array will clear the entries. | [optional] 
**arpInspection** | [**UpdateNetworkSwitchDhcpServerPolicyRequestArpInspection**](UpdateNetworkSwitchDhcpServerPolicyRequestArpInspection.md) |  | [optional] 
**blockedServers** | **[String]** | List the MAC addresses of DHCP servers to block on the network when defaultPolicy is set to allow. An empty array will clear the entries. | [optional] 
**defaultPolicy** | **String** | &#39;allow&#39; or &#39;block&#39; new DHCP servers. Default value is &#39;allow&#39;. | [optional] 



## Enum: DefaultPolicyEnum


* `allow` (value: `"allow"`)

* `block` (value: `"block"`)




