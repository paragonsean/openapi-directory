

# GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**failOverCriterion** | [**FailOverCriterionEnum**](#FailOverCriterionEnum) | Fail over criterion for uplink preference rule. Must be one of: &#39;poorPerformance&#39; or &#39;uplinkDown&#39; |  [optional] |
|**performanceClass** | [**GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerPerformanceClass**](GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerPerformanceClass.md) |  |  [optional] |
|**preferredUplink** | [**PreferredUplinkEnum**](#PreferredUplinkEnum) | Preferred uplink for uplink preference rule. Must be one of: &#39;wan1&#39;, &#39;wan2&#39;, &#39;bestForVoIP&#39;, &#39;loadBalancing&#39; or &#39;defaultUplink&#39; |  |
|**trafficFilters** | [**List&lt;GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerTrafficFiltersInner&gt;**](GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerTrafficFiltersInner.md) | Traffic filters |  |



## Enum: FailOverCriterionEnum

| Name | Value |
|---- | -----|
| POOR_PERFORMANCE | &quot;poorPerformance&quot; |
| UPLINK_DOWN | &quot;uplinkDown&quot; |



## Enum: PreferredUplinkEnum

| Name | Value |
|---- | -----|
| BEST_FOR_VO_IP | &quot;bestForVoIP&quot; |
| DEFAULT_UPLINK | &quot;defaultUplink&quot; |
| LOAD_BALANCING | &quot;loadBalancing&quot; |
| WAN1 | &quot;wan1&quot; |
| WAN2 | &quot;wan2&quot; |



