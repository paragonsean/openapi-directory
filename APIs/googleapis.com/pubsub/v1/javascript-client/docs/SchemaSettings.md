# CloudPubSubApi.SchemaSettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encoding** | **String** | Optional. The encoding of messages validated against &#x60;schema&#x60;. | [optional] 
**firstRevisionId** | **String** | Optional. The minimum (inclusive) revision allowed for validating messages. If empty or not present, allow any revision to be validated against last_revision or any revision created before. | [optional] 
**lastRevisionId** | **String** | Optional. The maximum (inclusive) revision allowed for validating messages. If empty or not present, allow any revision to be validated against first_revision or any revision created after. | [optional] 
**schema** | **String** | Required. The name of the schema that messages published should be validated against. Format is &#x60;projects/{project}/schemas/{schema}&#x60;. The value of this field will be &#x60;_deleted-schema_&#x60; if the schema has been deleted. | [optional] 



## Enum: EncodingEnum


* `ENCODING_UNSPECIFIED` (value: `"ENCODING_UNSPECIFIED"`)

* `JSON` (value: `"JSON"`)

* `BINARY` (value: `"BINARY"`)




