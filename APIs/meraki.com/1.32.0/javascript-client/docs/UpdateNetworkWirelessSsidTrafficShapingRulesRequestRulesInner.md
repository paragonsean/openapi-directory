# MerakiDashboardApi.UpdateNetworkWirelessSsidTrafficShapingRulesRequestRulesInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**definitions** | [**[UpdateNetworkApplianceTrafficShapingRulesRequestRulesInnerDefinitionsInner]**](UpdateNetworkApplianceTrafficShapingRulesRequestRulesInnerDefinitionsInner.md) |     A list of objects describing the definitions of your traffic shaping rule. At least one definition is required.  | 
**dscpTagValue** | **Number** |     The DSCP tag applied by your rule. null means &#39;Do not change DSCP tag&#39;.     For a list of possible tag values, use the trafficShaping/dscpTaggingOptions endpoint.  | [optional] 
**pcpTagValue** | **Number** |     The PCP tag applied by your rule. Can be 0 (lowest priority) through 7 (highest priority).     null means &#39;Do not set PCP tag&#39;.  | [optional] 
**perClientBandwidthLimits** | [**UpdateNetworkApplianceTrafficShapingRulesRequestRulesInnerPerClientBandwidthLimits**](UpdateNetworkApplianceTrafficShapingRulesRequestRulesInnerPerClientBandwidthLimits.md) |  | [optional] 


