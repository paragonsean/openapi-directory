# EtsiGsMec0102Part2ApplicationLifecycleRulesAndRequirementsManagement.TrafficRuleDescriptor

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**Action**](Action.md) |  | 
**dstInterface** | [**[InterfaceDescriptor]**](InterfaceDescriptor.md) |  | [optional] 
**filterType** | [**FilterType**](FilterType.md) |  | 
**priority** | **Number** | Priority of this traffic rule. If traffic rule conflicts, the one with higher priority take precedence. | 
**trafficFilter** | [**[TrafficFilter]**](TrafficFilter.md) | The filter used to identify specific flow/packets that need to be handled by the MEC host. | 
**trafficRuleId** | **String** | Identifies the traffic rule. | 


