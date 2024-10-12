

# GoogleCloudDiscoveryengineV1alphaDocument

Document captures all raw metadata information of items to be recommended or searched.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aclInfo** | [**GoogleCloudDiscoveryengineV1alphaDocumentAclInfo**](GoogleCloudDiscoveryengineV1alphaDocumentAclInfo.md) |  |  [optional] |
|**content** | [**GoogleCloudDiscoveryengineV1alphaDocumentContent**](GoogleCloudDiscoveryengineV1alphaDocumentContent.md) |  |  [optional] |
|**derivedStructData** | **Map&lt;String, Object&gt;** | Output only. This field is OUTPUT_ONLY. It contains derived data that are not in the original input document. |  [optional] [readonly] |
|**id** | **String** | Immutable. The identifier of the document. Id should conform to [RFC-1034](https://tools.ietf.org/html/rfc1034) standard with a length limit of 63 characters. |  [optional] |
|**indexTime** | **String** | Output only. The last time the document was indexed. If this field is set, the document could be returned in search results. This field is OUTPUT_ONLY. If this field is not populated, it means the document has never been indexed. |  [optional] [readonly] |
|**jsonData** | **String** | The JSON string representation of the document. It should conform to the registered Schema or an &#x60;INVALID_ARGUMENT&#x60; error is thrown. |  [optional] |
|**name** | **String** | Immutable. The full resource name of the document. Format: &#x60;projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}/documents/{document_id}&#x60;. This field must be a UTF-8 encoded string with a length limit of 1024 characters. |  [optional] |
|**parentDocumentId** | **String** | The identifier of the parent document. Currently supports at most two level document hierarchy. Id should conform to [RFC-1034](https://tools.ietf.org/html/rfc1034) standard with a length limit of 63 characters. |  [optional] |
|**schemaId** | **String** | The identifier of the schema located in the same data store. |  [optional] |
|**structData** | **Map&lt;String, Object&gt;** | The structured JSON data for the document. It should conform to the registered Schema or an &#x60;INVALID_ARGUMENT&#x60; error is thrown. |  [optional] |



