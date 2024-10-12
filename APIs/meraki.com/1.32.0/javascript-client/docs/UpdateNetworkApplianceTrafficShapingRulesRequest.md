# MerakiDashboardApi.UpdateNetworkApplianceTrafficShapingRulesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**defaultRulesEnabled** | **Boolean** | Whether default traffic shaping rules are enabled (true) or disabled (false). There are 4 default rules, which can be seen on your network&#39;s traffic shaping page. Note that default rules count against the rule limit of 8. | [optional] 
**rules** | [**[UpdateNetworkApplianceTrafficShapingRulesRequestRulesInner]**](UpdateNetworkApplianceTrafficShapingRulesRequestRulesInner.md) |     An array of traffic shaping rules. Rules are applied in the order that     they are specified in. An empty list (or null) means no rules. Note that     you are allowed a maximum of 8 rules.  | [optional] 


