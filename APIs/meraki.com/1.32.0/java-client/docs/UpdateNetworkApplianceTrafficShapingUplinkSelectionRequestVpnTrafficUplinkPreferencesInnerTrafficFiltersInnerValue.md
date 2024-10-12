

# UpdateNetworkApplianceTrafficShapingUplinkSelectionRequestVpnTrafficUplinkPreferencesInnerTrafficFiltersInnerValue

Value object of this traffic filter

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**destination** | [**UpdateNetworkApplianceTrafficShapingUplinkSelectionRequestVpnTrafficUplinkPreferencesInnerTrafficFiltersInnerValueDestination**](UpdateNetworkApplianceTrafficShapingUplinkSelectionRequestVpnTrafficUplinkPreferencesInnerTrafficFiltersInnerValueDestination.md) |  |  [optional] |
|**id** | **String** | ID of this applicationCategory or application type traffic filter. E.g.: \&quot;meraki:layer7/category/1\&quot;, \&quot;meraki:layer7/application/4\&quot; |  [optional] |
|**protocol** | [**ProtocolEnum**](#ProtocolEnum) | Protocol of this custom type traffic filter. Must be one of: &#39;tcp&#39;, &#39;udp&#39;, &#39;icmp&#39;, &#39;icmp6&#39; or &#39;any&#39; |  [optional] |
|**source** | [**UpdateNetworkApplianceTrafficShapingUplinkSelectionRequestVpnTrafficUplinkPreferencesInnerTrafficFiltersInnerValueSource**](UpdateNetworkApplianceTrafficShapingUplinkSelectionRequestVpnTrafficUplinkPreferencesInnerTrafficFiltersInnerValueSource.md) |  |  [optional] |



## Enum: ProtocolEnum

| Name | Value |
|---- | -----|
| ANY | &quot;any&quot; |
| ICMP | &quot;icmp&quot; |
| ICMP6 | &quot;icmp6&quot; |
| TCP | &quot;tcp&quot; |
| UDP | &quot;udp&quot; |



