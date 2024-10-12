# MicrocksApiV17.GetService200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | Unique identifier for this Service or API | [optional] 
**metadata** | [**Metadata**](Metadata.md) |  | [optional] 
**name** | **String** | Distinct name for this Service or API (maybe shared among many versions) | 
**operations** | [**[Operation]**](Operation.md) | Set of Operations for Service or API | [optional] 
**type** | **String** | Service or API Type | 
**version** | **String** | Distinct version for a named Service or API | 
**xmlNS** | **String** | Associated Xml Namespace in case of Xml based Service | [optional] 
**messagesMap** | **{String: Array}** | Map of messages for this Service. Keys are operation name, values are array of messages for this operation | 
**service** | [**Service**](Service.md) |  | 



## Enum: TypeEnum


* `REST` (value: `"REST"`)

* `SOAP_HTTP` (value: `"SOAP_HTTP"`)

* `GENERIC_REST` (value: `"GENERIC_REST"`)

* `GENERIC_EVENT` (value: `"GENERIC_EVENT"`)

* `EVENT` (value: `"EVENT"`)

* `GRPC` (value: `"GRPC"`)

* `GRAPHQL` (value: `"GRAPHQL"`)




