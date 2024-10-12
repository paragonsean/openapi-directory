# YodleeCoreApis.DocumentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteDocument**](DocumentsApi.md#deleteDocument) | **DELETE** /documents/{documentId} | Delete Document
[**downloadDocument**](DocumentsApi.md#downloadDocument) | **GET** /documents/{documentId} | Download a Document
[**getDocuments**](DocumentsApi.md#getDocuments) | **GET** /documents | Get Documents



## deleteDocument

> deleteDocument(documentId)

Delete Document

The delete document service allows the consumer to delete a document. The deleted document will not be returned in the get documents API. The HTTP response code is 204 (success without content).&lt;br&gt;Documents can be deleted only if the document related dataset attributes are subscribed.&lt;br&gt;

### Example

```javascript
import YodleeCoreApis from 'yodlee_core_apis';

let apiInstance = new YodleeCoreApis.DocumentsApi();
let documentId = "documentId_example"; // String | documentId
apiInstance.deleteDocument(documentId, (error, data, response) => {
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
 **documentId** | **String**| documentId | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## downloadDocument

> DocumentDownloadResponse downloadDocument(documentId)

Download a Document

The get document details service allows consumers to download a document. The document is provided in base64.&lt;br&gt;This API is a premium service which requires subscription in advance to use.  Please contact Yodlee Client Services for more information. &lt;br&gt;

### Example

```javascript
import YodleeCoreApis from 'yodlee_core_apis';

let apiInstance = new YodleeCoreApis.DocumentsApi();
let documentId = "documentId_example"; // String | documentId
apiInstance.downloadDocument(documentId, (error, data, response) => {
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
 **documentId** | **String**| documentId | 

### Return type

[**DocumentDownloadResponse**](DocumentDownloadResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## getDocuments

> DocumentResponse getDocuments(opts)

Get Documents

The get documents service allows customers to search or retrieve metadata related to documents. &lt;br&gt;The API returns the document as per the input parameters passed. If no date range is provided then all downloaded documents will be retrieved. Details of deleted documents or documents associated to closed providerAccount will not be returned. &lt;br&gt;This API is a premium service which requires subscription in advance to use.  Please contact Yodlee Client Services for more information. &lt;br&gt;

### Example

```javascript
import YodleeCoreApis from 'yodlee_core_apis';

let apiInstance = new YodleeCoreApis.DocumentsApi();
let opts = {
  'keyword': "keyword_example", // String | The string used to search a document by its name.
  'accountId': "accountId_example", // String | The unique identifier of an account. Retrieve documents for a given accountId.
  'docType': "docType_example", // String | Accepts only one of the following valid document types: STMT, TAX, and EBILL.
  'fromDate': "fromDate_example", // String | The date from which documents have to be retrieved.
  'toDate': "toDate_example" // String | The date to which documents have to be retrieved.
};
apiInstance.getDocuments(opts, (error, data, response) => {
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
 **keyword** | **String**| The string used to search a document by its name. | [optional] 
 **accountId** | **String**| The unique identifier of an account. Retrieve documents for a given accountId. | [optional] 
 **docType** | **String**| Accepts only one of the following valid document types: STMT, TAX, and EBILL. | [optional] 
 **fromDate** | **String**| The date from which documents have to be retrieved. | [optional] 
 **toDate** | **String**| The date to which documents have to be retrieved. | [optional] 

### Return type

[**DocumentResponse**](DocumentResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8

