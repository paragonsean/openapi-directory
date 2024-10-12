# StorecoveApi.ReceivedDocumentsApi

All URIs are relative to *https://api.storecove.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getReceivedDocument**](ReceivedDocumentsApi.md#getReceivedDocument) | **GET** /received_documents/{guid}/{format} | Get a new ReceivedDocument
[**receiveDocument**](ReceivedDocumentsApi.md#receiveDocument) | **POST** /legal_entities/{legal_entity_id}/received_documents | Receive a new Document



## getReceivedDocument

> ReceivedDocument getReceivedDocument(guid, syntax, format)

Get a new ReceivedDocument

EXPERIMENTAL: use only for orders. Get a new ReceivedDocument.

### Example

```javascript
import StorecoveApi from 'storecove_api';
let defaultClient = StorecoveApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new StorecoveApi.ReceivedDocumentsApi();
let guid = "guid_example"; // String | The guid of the document that was received. This is the \"document_guid\" property of the \"received_document\" webhook.
let syntax = "'json'"; // String | The syntax in which to receive the received document.
let format = "format_example"; // String | Automatically added
apiInstance.getReceivedDocument(guid, syntax, format, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **String**| The guid of the document that was received. This is the \&quot;document_guid\&quot; property of the \&quot;received_document\&quot; webhook. | 
 **syntax** | **String**| The syntax in which to receive the received document. | [default to &#39;json&#39;]
 **format** | **String**| Automatically added | 

### Return type

[**ReceivedDocument**](ReceivedDocument.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## receiveDocument

> ReceivedDocument receiveDocument(legalEntityId, receivedDocumentCreate)

Receive a new Document

Receive a new Document.

### Example

```javascript
import StorecoveApi from 'storecove_api';
let defaultClient = StorecoveApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new StorecoveApi.ReceivedDocumentsApi();
let legalEntityId = 789; // Number | The id of the LegalEntity for which the document was received.
let receivedDocumentCreate = new StorecoveApi.ReceivedDocumentCreate(); // ReceivedDocumentCreate | Received document to process.
apiInstance.receiveDocument(legalEntityId, receivedDocumentCreate, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **legalEntityId** | **Number**| The id of the LegalEntity for which the document was received. | 
 **receivedDocumentCreate** | [**ReceivedDocumentCreate**](ReceivedDocumentCreate.md)| Received document to process. | 

### Return type

[**ReceivedDocument**](ReceivedDocument.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

