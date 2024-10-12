

# SchemaSettings

Settings for validating messages published against a schema.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**encoding** | [**EncodingEnum**](#EncodingEnum) | Optional. The encoding of messages validated against &#x60;schema&#x60;. |  [optional] |
|**firstRevisionId** | **String** | Optional. The minimum (inclusive) revision allowed for validating messages. If empty or not present, allow any revision to be validated against last_revision or any revision created before. |  [optional] |
|**lastRevisionId** | **String** | Optional. The maximum (inclusive) revision allowed for validating messages. If empty or not present, allow any revision to be validated against first_revision or any revision created after. |  [optional] |
|**schema** | **String** | Required. The name of the schema that messages published should be validated against. Format is &#x60;projects/{project}/schemas/{schema}&#x60;. The value of this field will be &#x60;_deleted-schema_&#x60; if the schema has been deleted. |  [optional] |



## Enum: EncodingEnum

| Name | Value |
|---- | -----|
| ENCODING_UNSPECIFIED | &quot;ENCODING_UNSPECIFIED&quot; |
| JSON | &quot;JSON&quot; |
| BINARY | &quot;BINARY&quot; |



