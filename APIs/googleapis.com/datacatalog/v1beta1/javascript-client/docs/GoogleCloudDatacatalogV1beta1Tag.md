# GoogleCloudDataCatalogApi.GoogleCloudDatacatalogV1beta1Tag

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column** | **String** | Resources like Entry can have schemas associated with them. This scope allows users to attach tags to an individual column based on that schema. For attaching a tag to a nested column, use &#x60;.&#x60; to separate the column names. Example: * &#x60;outer_column.inner_column&#x60; | [optional] 
**fields** | [**{String: GoogleCloudDatacatalogV1beta1TagField}**](GoogleCloudDatacatalogV1beta1TagField.md) | Required. This maps the ID of a tag field to the value of and additional information about that field. Valid field IDs are defined by the tag&#39;s template. A tag must have at least 1 field and at most 500 fields. | [optional] 
**name** | **String** | The resource name of the tag in URL format. Example: * projects/{project_id}/locations/{location}/entrygroups/{entry_group_id}/entries/{entry_id}/tags/{tag_id} where &#x60;tag_id&#x60; is a system-generated identifier. Note that this Tag may not actually be stored in the location in this name. | [optional] 
**template** | **String** | Required. The resource name of the tag template that this tag uses. Example: * projects/{project_id}/locations/{location}/tagTemplates/{tag_template_id} This field cannot be modified after creation. | [optional] 
**templateDisplayName** | **String** | Output only. The display name of the tag template. | [optional] [readonly] 


