# ThePlaidApi.LinkTokenGetResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdAt** | **Date** | The creation timestamp for the &#x60;link_token&#x60;, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format. | 
**expiration** | **Date** | The expiration timestamp for the &#x60;link_token&#x60;, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format. | 
**linkToken** | **String** | A &#x60;link_token&#x60;, which can be supplied to Link in order to initialize it and receive a &#x60;public_token&#x60;, which can be exchanged for an &#x60;access_token&#x60;. | 
**metadata** | [**LinkTokenGetMetadataResponse**](LinkTokenGetMetadataResponse.md) |  | 
**requestId** | **String** | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 


