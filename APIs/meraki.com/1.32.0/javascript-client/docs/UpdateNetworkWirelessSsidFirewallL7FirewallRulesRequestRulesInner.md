# MerakiDashboardApi.UpdateNetworkWirelessSsidFirewallL7FirewallRulesRequestRulesInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy** | **String** | &#39;Deny&#39; traffic specified by this rule | [optional] 
**type** | **String** | Type of the L7 firewall rule. One of: &#39;application&#39;, &#39;applicationCategory&#39;, &#39;host&#39;, &#39;port&#39;, &#39;ipRange&#39; | [optional] 
**value** | **String** | The value of what needs to get blocked. Format of the value varies depending on type of the firewall rule selected. | [optional] 



## Enum: PolicyEnum


* `deny` (value: `"deny"`)





## Enum: TypeEnum


* `application` (value: `"application"`)

* `applicationCategory` (value: `"applicationCategory"`)

* `host` (value: `"host"`)

* `ipRange` (value: `"ipRange"`)

* `port` (value: `"port"`)




