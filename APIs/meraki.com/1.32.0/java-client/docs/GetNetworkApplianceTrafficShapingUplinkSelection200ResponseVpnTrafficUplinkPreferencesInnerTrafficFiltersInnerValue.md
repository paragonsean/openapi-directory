

# GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerTrafficFiltersInnerValue

Value of traffic filter

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**destination** | [**GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerTrafficFiltersInnerValueDestination**](GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerTrafficFiltersInnerValueDestination.md) |  |  [optional] |
|**id** | **String** | ID of &#39;applicationCategory&#39; or &#39;application&#39; type traffic filter |  [optional] |
|**protocol** | [**ProtocolEnum**](#ProtocolEnum) | Protocol of &#39;custom&#39; type traffic filter. Must be one of: &#39;tcp&#39;, &#39;udp&#39;, &#39;icmp&#39;, &#39;icmp6&#39; or &#39;any&#39; |  [optional] |
|**source** | [**GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerTrafficFiltersInnerValueSource**](GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerTrafficFiltersInnerValueSource.md) |  |  [optional] |



## Enum: ProtocolEnum

| Name | Value |
|---- | -----|
| ANY | &quot;any&quot; |
| ICMP | &quot;icmp&quot; |
| ICMP6 | &quot;icmp6&quot; |
| TCP | &quot;tcp&quot; |
| UDP | &quot;udp&quot; |



