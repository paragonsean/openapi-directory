

# GoogleCloudDatacatalogV1TagTemplateField

The template for an individual field within a tag template.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | The description for this field. Defaults to an empty string. |  [optional] |
|**displayName** | **String** | The display name for this field. Defaults to an empty string. The name must contain only Unicode letters, numbers (0-9), underscores (_), dashes (-), spaces ( ), and can&#39;t start or end with spaces. The maximum length is 200 characters. |  [optional] |
|**isRequired** | **Boolean** | If true, this field is required. Defaults to false. |  [optional] |
|**name** | **String** | Output only. The resource name of the tag template field in URL format. Example: &#x60;projects/{PROJECT_ID}/locations/{LOCATION}/tagTemplates/{TAG_TEMPLATE}/fields/{FIELD}&#x60; Note: The tag template field itself might not be stored in the location specified in its name. The name must contain only letters (a-z, A-Z), numbers (0-9), or underscores (_), and must start with a letter or underscore. The maximum length is 64 characters. |  [optional] [readonly] |
|**order** | **Integer** | The order of this field with respect to other fields in this tag template. For example, a higher value can indicate a more important field. The value can be negative. Multiple fields can have the same order and field orders within a tag don&#39;t have to be sequential. |  [optional] |
|**type** | [**GoogleCloudDatacatalogV1FieldType**](GoogleCloudDatacatalogV1FieldType.md) |  |  [optional] |



