# GoogleCloudDataCatalogApi.GoogleCloudDatacatalogV1beta1TagTemplateField

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | The description for this field. Defaults to an empty string. | [optional] 
**displayName** | **String** | The display name for this field. Defaults to an empty string. | [optional] 
**isRequired** | **Boolean** | Whether this is a required field. Defaults to false. | [optional] 
**name** | **String** | Output only. The resource name of the tag template field in URL format. Example: * projects/{project_id}/locations/{location}/tagTemplates/{tag_template}/fields/{field} Note that this TagTemplateField may not actually be stored in the location in this name. | [optional] [readonly] 
**order** | **Number** | The order of this field with respect to other fields in this tag template. A higher value indicates a more important field. The value can be negative. Multiple fields can have the same order, and field orders within a tag do not have to be sequential. | [optional] 
**type** | [**GoogleCloudDatacatalogV1beta1FieldType**](GoogleCloudDatacatalogV1beta1FieldType.md) |  | [optional] 


