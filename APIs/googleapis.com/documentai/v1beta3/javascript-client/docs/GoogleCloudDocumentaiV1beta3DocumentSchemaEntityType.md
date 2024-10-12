# CloudDocumentAiApi.GoogleCloudDocumentaiV1beta3DocumentSchemaEntityType

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**baseTypes** | **[String]** | The entity type that this type is derived from. For now, one and only one should be set. | [optional] 
**displayName** | **String** | User defined name for the type. | [optional] 
**entityTypeMetadata** | [**GoogleCloudDocumentaiV1beta3EntityTypeMetadata**](GoogleCloudDocumentaiV1beta3EntityTypeMetadata.md) |  | [optional] 
**enumValues** | [**GoogleCloudDocumentaiV1beta3DocumentSchemaEntityTypeEnumValues**](GoogleCloudDocumentaiV1beta3DocumentSchemaEntityTypeEnumValues.md) |  | [optional] 
**name** | **String** | Name of the type. It must be unique within the schema file and cannot be a \&quot;Common Type\&quot;. The following naming conventions are used: - Use &#x60;snake_casing&#x60;. - Name matching is case-sensitive. - Maximum 64 characters. - Must start with a letter. - Allowed characters: ASCII letters &#x60;[a-z0-9_-]&#x60;. (For backward compatibility internal infrastructure and tooling can handle any ascii character.) - The &#x60;/&#x60; is sometimes used to denote a property of a type. For example &#x60;line_item/amount&#x60;. This convention is deprecated, but will still be honored for backward compatibility. | [optional] 
**properties** | [**[GoogleCloudDocumentaiV1beta3DocumentSchemaEntityTypeProperty]**](GoogleCloudDocumentaiV1beta3DocumentSchemaEntityTypeProperty.md) | Description the nested structure, or composition of an entity. | [optional] 


