# CloudPubSubApi.ValidateMessageRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encoding** | **String** | The encoding expected for messages | [optional] 
**message** | **Blob** | Message to validate against the provided &#x60;schema_spec&#x60;. | [optional] 
**name** | **String** | Name of the schema against which to validate. Format is &#x60;projects/{project}/schemas/{schema}&#x60;. | [optional] 
**schema** | [**Schema**](Schema.md) |  | [optional] 



## Enum: EncodingEnum


* `ENCODING_UNSPECIFIED` (value: `"ENCODING_UNSPECIFIED"`)

* `JSON` (value: `"JSON"`)

* `BINARY` (value: `"BINARY"`)




