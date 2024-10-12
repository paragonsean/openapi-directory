# NetBoxApi.VRF

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comments** | **String** |  | [optional] 
**created** | **Date** |  | [optional] [readonly] 
**customFields** | **Object** |  | [optional] 
**description** | **String** |  | [optional] 
**display** | **String** |  | [optional] [readonly] 
**enforceUnique** | **Boolean** | Prevent duplicate prefixes/IP addresses within this VRF | [optional] 
**exportTargets** | [**[NestedRouteTarget]**](NestedRouteTarget.md) |  | [optional] 
**id** | **Number** |  | [optional] [readonly] 
**importTargets** | [**[NestedRouteTarget]**](NestedRouteTarget.md) |  | [optional] 
**ipaddressCount** | **Number** |  | [optional] [readonly] 
**lastUpdated** | **Date** |  | [optional] [readonly] 
**name** | **String** |  | 
**prefixCount** | **Number** |  | [optional] [readonly] 
**rd** | **String** | Unique route distinguisher (as defined in RFC 4364) | [optional] 
**tags** | [**[NestedTag]**](NestedTag.md) |  | [optional] 
**tenant** | [**NestedTenant**](NestedTenant.md) |  | [optional] 
**url** | **String** |  | [optional] [readonly] 


