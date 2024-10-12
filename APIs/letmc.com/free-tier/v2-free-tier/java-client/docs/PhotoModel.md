

# PhotoModel

Stores a photo related to a property structure.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**etag** | **String** | A unique identifier defining the object and change revision. |  [optional] |
|**fileName** | **String** | The file name. |  [optional] |
|**inspectionItem** | **String** | The inspection item the photo is assigned to (if applicable). |  [optional] |
|**interimInspection** | **String** | The inspection the photo is assigned to (if applicable). |  [optional] |
|**inventoryItem** | **String** | The inventory item the photo is assigned to (if applicable). |  [optional] |
|**name** | **String** | The photo name. |  [optional] |
|**OID** | **String** | The unique Object ID (OID). |  [optional] |
|**photoNumber** | **Integer** | The photo ordering number |  [optional] |
|**photoType** | [**PhotoTypeEnum**](#PhotoTypeEnum) | The photo type. |  [optional] |
|**property** | **String** | The property the photo is assigned to. |  [optional] |
|**room** | **String** | The room the photo is assigned to. (If applicable) |  [optional] |



## Enum: PhotoTypeEnum

| Name | Value |
|---- | -----|
| PHOTO | &quot;Photo&quot; |
| MAP | &quot;Map&quot; |
| FLOOR_PLAN | &quot;FloorPlan&quot; |
| SITE_MAP | &quot;SiteMap&quot; |
| AERIAL_PHOTO | &quot;AerialPhoto&quot; |



