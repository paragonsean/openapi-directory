

# Location


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | [**Address**](Address.md) |  |  [optional] |
|**businessName** | **String** | The business name of the location |  [optional] |
|**createdAt** | **OffsetDateTime** | The date and time when the object was created. |  [optional] [readonly] |
|**createdBy** | **String** | The user who created the object. |  [optional] [readonly] |
|**currency** | **Currency** |  |  [optional] |
|**customMappings** | **Object** | When custom mappings are configured on the resource, the result is included here. |  [optional] |
|**id** | **String** | A unique identifier for an object. |  [optional] [readonly] |
|**merchantId** | **String** |  |  [optional] |
|**name** | **String** | The name of the location |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Status of this location. |  [optional] |
|**updatedAt** | **OffsetDateTime** | The date and time when the object was last updated. |  [optional] [readonly] |
|**updatedBy** | **String** | The user who last updated the object. |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| INACTIVE | &quot;inactive&quot; |
| OTHER | &quot;other&quot; |



