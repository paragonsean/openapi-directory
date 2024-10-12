# Semantria.ProcessingDocumentsApi

All URIs are relative to *https://api.semantria.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancelDocument**](ProcessingDocumentsApi.md#cancelDocument) | **DELETE** /document/{document_id}.{content_type} | Cancel document analysis
[**queueBatchOfDocuments**](ProcessingDocumentsApi.md#queueBatchOfDocuments) | **POST** /document/batch.{content_type} | Queue batch of documents for analysis
[**queueDocument**](ProcessingDocumentsApi.md#queueDocument) | **POST** /document.{content_type} | Queue document for analysis
[**receiveDocumentAnalyticData**](ProcessingDocumentsApi.md#receiveDocumentAnalyticData) | **GET** /document/{document_id}.{content_type} | Retrieve document analysis or its status in queue
[**retrieveProcessedDocuments**](ProcessingDocumentsApi.md#retrieveProcessedDocuments) | **GET** /document/processed.{content_type} | Retrieve documents analysis



## cancelDocument

> cancelDocument(documentId, contentType, opts)

Cancel document analysis

This method cancels document analysis by unique ID on Semantria side if it is waiting for analysis in queue.

### Example

```javascript
import Semantria from 'semantria';

let apiInstance = new Semantria.ProcessingDocumentsApi();
let documentId = "documentId_example"; // String | Document ID
let contentType = "contentType_example"; // String | 
let opts = {
  'configId': "configId_example" // String | Identifier of configuration used for analysis.
};
apiInstance.cancelDocument(documentId, contentType, opts, (error, data, response) => {
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
 **documentId** | **String**| Document ID | 
 **contentType** | **String**|  | 
 **configId** | **String**| Identifier of configuration used for analysis. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## queueBatchOfDocuments

> Document queueBatchOfDocuments(contentType, batchOfDocuments, opts)

Queue batch of documents for analysis

This method queues batch of documents for analysis. The rules are the same as for single document mode but here the documents ordered into the batch.

### Example

```javascript
import Semantria from 'semantria';

let apiInstance = new Semantria.ProcessingDocumentsApi();
let contentType = "contentType_example"; // String | 
let batchOfDocuments = {key: null}; // Object | List of parametrized JSON or XML objects.
let opts = {
  'configId': "configId_example" // String | Identifier of configuration used for analysis.
};
apiInstance.queueBatchOfDocuments(contentType, batchOfDocuments, opts, (error, data, response) => {
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
 **contentType** | **String**|  | 
 **batchOfDocuments** | **Object**| List of parametrized JSON or XML objects. | 
 **configId** | **String**| Identifier of configuration used for analysis. | [optional] 

### Return type

[**Document**](Document.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## queueDocument

> Document queueDocument(contentType, document, opts)

Queue document for analysis

This method queues document onto the server for analysis. Queued document analyzes individually and will have its own set of results. If unique configuration ID provided, Semantria uses settings of that configuration during analysis, in opposite the primary configuration uses. Document IDs are unique in scope of configuration. If the same ID appears twice, Semantria overrides existing document with the new Data.

### Example

```javascript
import Semantria from 'semantria';

let apiInstance = new Semantria.ProcessingDocumentsApi();
let contentType = "contentType_example"; // String | 
let document = {key: null}; // Object | Parametrized JSON or XML object.
let opts = {
  'configId': "configId_example" // String | Identifier of configuration used for analysis.
};
apiInstance.queueDocument(contentType, document, opts, (error, data, response) => {
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
 **contentType** | **String**|  | 
 **document** | **Object**| Parametrized JSON or XML object. | 
 **configId** | **String**| Identifier of configuration used for analysis. | [optional] 

### Return type

[**Document**](Document.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## receiveDocumentAnalyticData

> DocumentAnalyticData receiveDocumentAnalyticData(documentId, contentType, opts)

Retrieve document analysis or its status in queue

This method retrieves analysis results for the single document by its unique ID or the document’s status in queue if it did not analyzed yet. Semantria guarantees delivering of all documents back to the client even if they FAILED on Semantria side due to some reason.

### Example

```javascript
import Semantria from 'semantria';

let apiInstance = new Semantria.ProcessingDocumentsApi();
let documentId = "documentId_example"; // String | Document ID
let contentType = "contentType_example"; // String | 
let opts = {
  'configId': "configId_example" // String | Identifier of configuration used for analysis.
};
apiInstance.receiveDocumentAnalyticData(documentId, contentType, opts, (error, data, response) => {
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
 **documentId** | **String**| Document ID | 
 **contentType** | **String**|  | 
 **configId** | **String**| Identifier of configuration used for analysis. | [optional] 

### Return type

[**DocumentAnalyticData**](DocumentAnalyticData.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## retrieveProcessedDocuments

> DocumentAnalyticData retrieveProcessedDocuments(contentType, opts)

Retrieve documents analysis

This method retrieves analysis results for processed documents from Semantria. FAILED documents will have FAILED status in response. Semantria responds with limited amount of results per API call. If configuration ID provided, Semantria responds with the document, which were queued using the same configuration ID, in opposite Primary.

### Example

```javascript
import Semantria from 'semantria';

let apiInstance = new Semantria.ProcessingDocumentsApi();
let contentType = "contentType_example"; // String | 
let opts = {
  'configId': "configId_example" // String | Identifier of configuration used for analysis.
};
apiInstance.retrieveProcessedDocuments(contentType, opts, (error, data, response) => {
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
 **contentType** | **String**|  | 
 **configId** | **String**| Identifier of configuration used for analysis. | [optional] 

### Return type

[**DocumentAnalyticData**](DocumentAnalyticData.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

