

# GoogleCloudApigeeV1Schema

Response for Schema call

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dimensions** | [**List&lt;GoogleCloudApigeeV1SchemaSchemaElement&gt;**](GoogleCloudApigeeV1SchemaSchemaElement.md) | List of schema fields grouped as dimensions. |  [optional] |
|**meta** | **List&lt;String&gt;** | Additional metadata associated with schema. This is a legacy field and usually consists of an empty array of strings. |  [optional] |
|**metrics** | [**List&lt;GoogleCloudApigeeV1SchemaSchemaElement&gt;**](GoogleCloudApigeeV1SchemaSchemaElement.md) | List of schema fields grouped as dimensions that can be used with an aggregate function such as &#x60;sum&#x60;, &#x60;avg&#x60;, &#x60;min&#x60;, and &#x60;max&#x60;. |  [optional] |



