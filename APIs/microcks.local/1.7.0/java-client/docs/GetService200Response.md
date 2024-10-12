

# GetService200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Unique identifier for this Service or API |  [optional] |
|**metadata** | [**Metadata**](Metadata.md) |  |  [optional] |
|**name** | **String** | Distinct name for this Service or API (maybe shared among many versions) |  |
|**operations** | [**List&lt;Operation&gt;**](Operation.md) | Set of Operations for Service or API |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Service or API Type |  |
|**version** | **String** | Distinct version for a named Service or API |  |
|**xmlNS** | **String** | Associated Xml Namespace in case of Xml based Service |  [optional] |
|**messagesMap** | **Map&lt;String, List&lt;Exchange&gt;&gt;** | Map of messages for this Service. Keys are operation name, values are array of messages for this operation |  |
|**service** | [**Service**](Service.md) |  |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| REST | &quot;REST&quot; |
| SOAP_HTTP | &quot;SOAP_HTTP&quot; |
| GENERIC_REST | &quot;GENERIC_REST&quot; |
| GENERIC_EVENT | &quot;GENERIC_EVENT&quot; |
| EVENT | &quot;EVENT&quot; |
| GRPC | &quot;GRPC&quot; |
| GRAPHQL | &quot;GRAPHQL&quot; |



