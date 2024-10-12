# MerakiDashboardApi.UpdateNetworkWirelessSsidVpnRequestSplitTunnelRulesInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **String** | Description for this split tunnel rule (optional). | [optional] 
**destCidr** | **String** | Destination for this split tunnel rule. IP address, fully-qualified domain names (FQDN) or &#39;any&#39;. | 
**destPort** | **String** | Destination port for this split tunnel rule, (integer in the range 1-65535), or &#39;any&#39;. | [optional] 
**policy** | **String** | Traffic policy specified for this split tunnel rule, &#39;allow&#39; or &#39;deny&#39;. | 
**protocol** | **String** | Protocol for this split tunnel rule. | [optional] 



## Enum: ProtocolEnum


* `Any` (value: `"Any"`)

* `TCP` (value: `"TCP"`)

* `UDP` (value: `"UDP"`)




