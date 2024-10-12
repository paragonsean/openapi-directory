# BillsApi.DocumentsApi

All URIs are relative to *https://bills-api.parliament.uk*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV1PublicationsPublicationIdDocumentsDocumentIdDownloadGet**](DocumentsApi.md#apiV1PublicationsPublicationIdDocumentsDocumentIdDownloadGet) | **GET** /api/v1/Publications/{publicationId}/Documents/{documentId}/Download | Return a document.
[**apiV1PublicationsPublicationIdDocumentsDocumentIdGet**](DocumentsApi.md#apiV1PublicationsPublicationIdDocumentsDocumentIdGet) | **GET** /api/v1/Publications/{publicationId}/Documents/{documentId} | Return information on a document.



## apiV1PublicationsPublicationIdDocumentsDocumentIdDownloadGet

> apiV1PublicationsPublicationIdDocumentsDocumentIdDownloadGet(publicationId, documentId)

Return a document.

### Example

```javascript
import BillsApi from 'bills_api';

let apiInstance = new BillsApi.DocumentsApi();
let publicationId = 56; // Number | Document with publication Id specified
let documentId = 56; // Number | Document with Id specified
apiInstance.apiV1PublicationsPublicationIdDocumentsDocumentIdDownloadGet(publicationId, documentId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **publicationId** | **Number**| Document with publication Id specified | 
 **documentId** | **Number**| Document with Id specified | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiV1PublicationsPublicationIdDocumentsDocumentIdGet

> PublicationDocument apiV1PublicationsPublicationIdDocumentsDocumentIdGet(publicationId, documentId)

Return information on a document.

### Example

```javascript
import BillsApi from 'bills_api';

let apiInstance = new BillsApi.DocumentsApi();
let publicationId = 56; // Number | Document with publication Id specified
let documentId = 56; // Number | Document with Id specified
apiInstance.apiV1PublicationsPublicationIdDocumentsDocumentIdGet(publicationId, documentId, (error, data, response) => {
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
 **publicationId** | **Number**| Document with publication Id specified | 
 **documentId** | **Number**| Document with Id specified | 

### Return type

[**PublicationDocument**](PublicationDocument.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

