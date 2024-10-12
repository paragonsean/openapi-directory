# NetBoxApi.IPAddress

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **String** | IPv4 or IPv6 address (with mask) | 
**assignedObject** | **Object** |  | [optional] [readonly] 
**assignedObjectId** | **Number** |  | [optional] 
**assignedObjectType** | **String** |  | [optional] 
**comments** | **String** |  | [optional] 
**created** | **Date** |  | [optional] [readonly] 
**customFields** | **Object** |  | [optional] 
**description** | **String** |  | [optional] 
**display** | **String** |  | [optional] [readonly] 
**dnsName** | **String** | Hostname or FQDN (not case-sensitive) | [optional] 
**family** | [**Family**](Family.md) |  | [optional] 
**id** | **Number** |  | [optional] [readonly] 
**lastUpdated** | **Date** |  | [optional] [readonly] 
**natInside** | [**NestedIPAddress**](NestedIPAddress.md) |  | [optional] 
**natOutside** | [**[NestedIPAddress]**](NestedIPAddress.md) |  | [optional] [readonly] 
**role** | [**Role1**](Role1.md) |  | [optional] 
**status** | [**Status4**](Status4.md) |  | [optional] 
**tags** | [**[NestedTag]**](NestedTag.md) |  | [optional] 
**tenant** | [**NestedTenant**](NestedTenant.md) |  | [optional] 
**url** | **String** |  | [optional] [readonly] 
**vrf** | [**NestedVRF**](NestedVRF.md) |  | [optional] 


