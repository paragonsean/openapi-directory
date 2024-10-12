# CloudDocumentAiApi.GoogleCloudDocumentaiV1beta3DocumentSchemaMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**documentAllowMultipleLabels** | **Boolean** | If true, on a given page, there can be multiple &#x60;document&#x60; annotations covering it. | [optional] 
**documentSplitter** | **Boolean** | If true, a &#x60;document&#x60; entity type can be applied to subdocument (splitting). Otherwise, it can only be applied to the entire document (classification). | [optional] 
**prefixedNamingOnProperties** | **Boolean** | If set, all the nested entities must be prefixed with the parents. | [optional] 
**skipNamingValidation** | **Boolean** | If set, we will skip the naming format validation in the schema. So the string values in &#x60;DocumentSchema.EntityType.name&#x60; and &#x60;DocumentSchema.EntityType.Property.name&#x60; will not be checked. | [optional] 


