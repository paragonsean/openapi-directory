

# TrafficRuleDescriptor


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**action** | **Action** |  |  |
|**dstInterface** | [**List&lt;InterfaceDescriptor&gt;**](InterfaceDescriptor.md) |  |  [optional] |
|**filterType** | **FilterType** |  |  |
|**priority** | **Integer** | Priority of this traffic rule. If traffic rule conflicts, the one with higher priority take precedence. |  |
|**trafficFilter** | [**List&lt;TrafficFilter&gt;**](TrafficFilter.md) | The filter used to identify specific flow/packets that need to be handled by the MEC host. |  |
|**trafficRuleId** | **String** | Identifies the traffic rule. |  |



