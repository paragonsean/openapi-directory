# NetBoxApi.InventoryItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**depth** | **Number** |  | [optional] [readonly] 
**assetTag** | **String** | A unique tag used to identify this item | [optional] 
**component** | **Object** |  | [optional] [readonly] 
**componentId** | **Number** |  | [optional] 
**componentType** | **String** |  | [optional] 
**created** | **Date** |  | [optional] [readonly] 
**customFields** | **Object** |  | [optional] 
**description** | **String** |  | [optional] 
**device** | [**NestedDevice**](NestedDevice.md) |  | 
**discovered** | **Boolean** | This item was automatically discovered | [optional] 
**display** | **String** |  | [optional] [readonly] 
**id** | **Number** |  | [optional] [readonly] 
**label** | **String** | Physical label | [optional] 
**lastUpdated** | **Date** |  | [optional] [readonly] 
**manufacturer** | [**NestedManufacturer**](NestedManufacturer.md) |  | [optional] 
**name** | **String** |  | 
**parent** | **Number** |  | [optional] 
**partId** | **String** | Manufacturer-assigned part identifier | [optional] 
**role** | [**NestedInventoryItemRole**](NestedInventoryItemRole.md) |  | [optional] 
**serial** | **String** |  | [optional] 
**tags** | [**[NestedTag]**](NestedTag.md) |  | [optional] 
**url** | **String** |  | [optional] [readonly] 


