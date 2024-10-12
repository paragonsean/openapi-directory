

# ModifierGroup


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alternateName** | **String** |  |  [optional] |
|**createdAt** | **OffsetDateTime** | The date and time when the object was created. |  [optional] [readonly] |
|**createdBy** | **String** | The user who created the object. |  [optional] [readonly] |
|**customMappings** | **Object** | When custom mappings are configured on the resource, the result is included here. |  [optional] |
|**deleted** | **Boolean** | Flag to indicate if the object is deleted. |  [optional] |
|**id** | **String** | A unique identifier for an object. |  [optional] [readonly] |
|**maximumAllowed** | **Integer** |  |  [optional] |
|**minimumRequired** | **Integer** |  |  [optional] |
|**modifiers** | [**List&lt;ModifierGroupModifiersInner&gt;**](ModifierGroupModifiersInner.md) |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**presentAtAllLocations** | **Boolean** |  |  [optional] |
|**rowVersion** | **String** | A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object. |  [optional] |
|**selectionType** | [**SelectionTypeEnum**](#SelectionTypeEnum) |  |  [optional] |
|**updatedAt** | **OffsetDateTime** | The date and time when the object was last updated. |  [optional] [readonly] |
|**updatedBy** | **String** | The user who last updated the object. |  [optional] [readonly] |



## Enum: SelectionTypeEnum

| Name | Value |
|---- | -----|
| SINGLE | &quot;single&quot; |
| MULTIPLE | &quot;multiple&quot; |



