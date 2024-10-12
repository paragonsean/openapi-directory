# CloudDocumentAiApi.GoogleCloudDocumentaiV1beta3DocumentSchemaEntityTypeProperty

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**displayName** | **String** | User defined name for the property. | [optional] 
**name** | **String** | The name of the property. Follows the same guidelines as the EntityType name. | [optional] 
**occurrenceType** | **String** | Occurrence type limits the number of instances an entity type appears in the document. | [optional] 
**propertyMetadata** | [**GoogleCloudDocumentaiV1beta3PropertyMetadata**](GoogleCloudDocumentaiV1beta3PropertyMetadata.md) |  | [optional] 
**valueType** | **String** | A reference to the value type of the property. This type is subject to the same conventions as the &#x60;Entity.base_types&#x60; field. | [optional] 



## Enum: OccurrenceTypeEnum


* `OCCURRENCE_TYPE_UNSPECIFIED` (value: `"OCCURRENCE_TYPE_UNSPECIFIED"`)

* `OPTIONAL_ONCE` (value: `"OPTIONAL_ONCE"`)

* `OPTIONAL_MULTIPLE` (value: `"OPTIONAL_MULTIPLE"`)

* `REQUIRED_ONCE` (value: `"REQUIRED_ONCE"`)

* `REQUIRED_MULTIPLE` (value: `"REQUIRED_MULTIPLE"`)




