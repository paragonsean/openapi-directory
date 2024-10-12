# MerakiDashboardApi.UpdateNetworkApplianceTrafficShapingUplinkSelectionRequestVpnTrafficUplinkPreferencesInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failOverCriterion** | **String** | Fail over criterion for this uplink preference rule. Must be one of: &#39;poorPerformance&#39; or &#39;uplinkDown&#39; | [optional] 
**performanceClass** | [**UpdateNetworkApplianceTrafficShapingUplinkSelectionRequestVpnTrafficUplinkPreferencesInnerPerformanceClass**](UpdateNetworkApplianceTrafficShapingUplinkSelectionRequestVpnTrafficUplinkPreferencesInnerPerformanceClass.md) |  | [optional] 
**preferredUplink** | **String** | Preferred uplink for this uplink preference rule. Must be one of: &#39;wan1&#39;, &#39;wan2&#39;, &#39;bestForVoIP&#39;, &#39;loadBalancing&#39; or &#39;defaultUplink&#39; | 
**trafficFilters** | [**[UpdateNetworkApplianceTrafficShapingUplinkSelectionRequestVpnTrafficUplinkPreferencesInnerTrafficFiltersInner]**](UpdateNetworkApplianceTrafficShapingUplinkSelectionRequestVpnTrafficUplinkPreferencesInnerTrafficFiltersInner.md) | Array of traffic filters for this uplink preference rule | 



## Enum: FailOverCriterionEnum


* `poorPerformance` (value: `"poorPerformance"`)

* `uplinkDown` (value: `"uplinkDown"`)





## Enum: PreferredUplinkEnum


* `bestForVoIP` (value: `"bestForVoIP"`)

* `defaultUplink` (value: `"defaultUplink"`)

* `loadBalancing` (value: `"loadBalancing"`)

* `wan1` (value: `"wan1"`)

* `wan2` (value: `"wan2"`)




