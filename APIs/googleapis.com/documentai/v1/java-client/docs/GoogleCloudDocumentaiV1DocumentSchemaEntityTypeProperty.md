

# GoogleCloudDocumentaiV1DocumentSchemaEntityTypeProperty

Defines properties that can be part of the entity type.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayName** | **String** | User defined name for the property. |  [optional] |
|**name** | **String** | The name of the property. Follows the same guidelines as the EntityType name. |  [optional] |
|**occurrenceType** | [**OccurrenceTypeEnum**](#OccurrenceTypeEnum) | Occurrence type limits the number of instances an entity type appears in the document. |  [optional] |
|**valueType** | **String** | A reference to the value type of the property. This type is subject to the same conventions as the &#x60;Entity.base_types&#x60; field. |  [optional] |



## Enum: OccurrenceTypeEnum

| Name | Value |
|---- | -----|
| OCCURRENCE_TYPE_UNSPECIFIED | &quot;OCCURRENCE_TYPE_UNSPECIFIED&quot; |
| OPTIONAL_ONCE | &quot;OPTIONAL_ONCE&quot; |
| OPTIONAL_MULTIPLE | &quot;OPTIONAL_MULTIPLE&quot; |
| REQUIRED_ONCE | &quot;REQUIRED_ONCE&quot; |
| REQUIRED_MULTIPLE | &quot;REQUIRED_MULTIPLE&quot; |



