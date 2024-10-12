# NetBoxApi.Rack

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assetTag** | **String** | A unique tag used to identify this rack | [optional] 
**comments** | **String** |  | [optional] 
**created** | **Date** |  | [optional] [readonly] 
**customFields** | **Object** |  | [optional] 
**descUnits** | **Boolean** | Units are numbered top-to-bottom | [optional] 
**description** | **String** |  | [optional] 
**deviceCount** | **Number** |  | [optional] [readonly] 
**display** | **String** |  | [optional] [readonly] 
**facilityId** | **String** |  | [optional] 
**id** | **Number** |  | [optional] [readonly] 
**lastUpdated** | **Date** |  | [optional] [readonly] 
**location** | [**NestedLocation**](NestedLocation.md) |  | [optional] 
**maxWeight** | **Number** | Maximum load capacity for the rack | [optional] 
**mountingDepth** | **Number** | Maximum depth of a mounted device, in millimeters. For four-post racks, this is the distance between the front and rear rails. | [optional] 
**name** | **String** |  | 
**outerDepth** | **Number** | Outer dimension of rack (depth) | [optional] 
**outerUnit** | [**OuterUnit**](OuterUnit.md) |  | [optional] 
**outerWidth** | **Number** | Outer dimension of rack (width) | [optional] 
**powerfeedCount** | **Number** |  | [optional] [readonly] 
**role** | [**NestedRackRole**](NestedRackRole.md) |  | [optional] 
**serial** | **String** |  | [optional] 
**site** | [**NestedSite**](NestedSite.md) |  | 
**status** | [**Status11**](Status11.md) |  | [optional] 
**tags** | [**[NestedTag]**](NestedTag.md) |  | [optional] 
**tenant** | [**NestedTenant**](NestedTenant.md) |  | [optional] 
**type** | [**Type8**](Type8.md) |  | [optional] 
**uHeight** | **Number** | Height in rack units | [optional] 
**url** | **String** |  | [optional] [readonly] 
**weight** | **Number** |  | [optional] 
**weightUnit** | [**WeightUnit**](WeightUnit.md) |  | [optional] 
**width** | [**Width**](Width.md) |  | [optional] 


