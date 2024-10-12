# NetBoxApi.Prefix

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**depth** | **Number** |  | [optional] [readonly] 
**children** | **Number** |  | [optional] [readonly] 
**comments** | **String** |  | [optional] 
**created** | **Date** |  | [optional] [readonly] 
**customFields** | **Object** |  | [optional] 
**description** | **String** |  | [optional] 
**display** | **String** |  | [optional] [readonly] 
**family** | [**Family**](Family.md) |  | [optional] 
**id** | **Number** |  | [optional] [readonly] 
**isPool** | **Boolean** | All IP addresses within this prefix are considered usable | [optional] 
**lastUpdated** | **Date** |  | [optional] [readonly] 
**markUtilized** | **Boolean** | Treat as 100% utilized | [optional] 
**prefix** | **String** | IPv4 or IPv6 network with mask | 
**role** | [**NestedRole**](NestedRole.md) |  | [optional] 
**site** | [**NestedSite**](NestedSite.md) |  | [optional] 
**status** | [**Status10**](Status10.md) |  | [optional] 
**tags** | [**[NestedTag]**](NestedTag.md) |  | [optional] 
**tenant** | [**NestedTenant**](NestedTenant.md) |  | [optional] 
**url** | **String** |  | [optional] [readonly] 
**vlan** | [**NestedVLAN**](NestedVLAN.md) |  | [optional] 
**vrf** | [**NestedVRF**](NestedVRF.md) |  | [optional] 


