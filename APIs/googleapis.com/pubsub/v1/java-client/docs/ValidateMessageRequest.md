

# ValidateMessageRequest

Request for the `ValidateMessage` method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**encoding** | [**EncodingEnum**](#EncodingEnum) | The encoding expected for messages |  [optional] |
|**message** | **byte[]** | Message to validate against the provided &#x60;schema_spec&#x60;. |  [optional] |
|**name** | **String** | Name of the schema against which to validate. Format is &#x60;projects/{project}/schemas/{schema}&#x60;. |  [optional] |
|**schema** | [**Schema**](Schema.md) |  |  [optional] |



## Enum: EncodingEnum

| Name | Value |
|---- | -----|
| ENCODING_UNSPECIFIED | &quot;ENCODING_UNSPECIFIED&quot; |
| JSON | &quot;JSON&quot; |
| BINARY | &quot;BINARY&quot; |



