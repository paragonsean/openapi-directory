# NetBoxApi.WritableSite

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asns** | **[Number]** |  | [optional] 
**circuitCount** | **Number** |  | [optional] [readonly] 
**comments** | **String** |  | [optional] 
**created** | **Date** |  | [optional] [readonly] 
**customFields** | **Object** |  | [optional] 
**description** | **String** |  | [optional] 
**deviceCount** | **Number** |  | [optional] [readonly] 
**display** | **String** |  | [optional] [readonly] 
**facility** | **String** | Local facility ID or description | [optional] 
**group** | **Number** |  | [optional] 
**id** | **Number** |  | [optional] [readonly] 
**lastUpdated** | **Date** |  | [optional] [readonly] 
**latitude** | **Number** | GPS coordinate (latitude) | [optional] 
**longitude** | **Number** | GPS coordinate (longitude) | [optional] 
**name** | **String** |  | 
**physicalAddress** | **String** |  | [optional] 
**prefixCount** | **Number** |  | [optional] [readonly] 
**rackCount** | **Number** |  | [optional] [readonly] 
**region** | **Number** |  | [optional] 
**shippingAddress** | **String** |  | [optional] 
**slug** | **String** |  | 
**status** | **String** |  | [optional] 
**tags** | [**[NestedTag]**](NestedTag.md) |  | [optional] 
**tenant** | **Number** |  | [optional] 
**timeZone** | **String** |  | [optional] 
**url** | **String** |  | [optional] [readonly] 
**virtualmachineCount** | **Number** |  | [optional] [readonly] 
**vlanCount** | **Number** |  | [optional] [readonly] 



## Enum: StatusEnum


* `planned` (value: `"planned"`)

* `staging` (value: `"staging"`)

* `active` (value: `"active"`)

* `decommissioning` (value: `"decommissioning"`)

* `retired` (value: `"retired"`)




