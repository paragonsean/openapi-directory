

# DocumentEnvelopeMetaData

Meta data associated to payload inside document envelope, helping to read/understand the DocumentEnvelope payload.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**documentType** | **String** | Type of the document in the payload defined by the \&quot;grammarOwner\&quot; |  [optional] |
|**encoding** | [**EncodingEnum**](#EncodingEnum) | Example: BASE_64 |  [optional] |
|**name** | **String** | Document name: name of the document in the payload (namespace, see domain) |  [optional] |



## Enum: EncodingEnum

| Name | Value |
|---- | -----|
| _64 | &quot;BASE_64&quot; |
| _64_URL | &quot;BASE_64_URL&quot; |



