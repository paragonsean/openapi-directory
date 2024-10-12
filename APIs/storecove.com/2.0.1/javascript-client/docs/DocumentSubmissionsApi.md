# StorecoveApi.DocumentSubmissionsApi

All URIs are relative to *https://api.storecove.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createDocumentSubmission**](DocumentSubmissionsApi.md#createDocumentSubmission) | **POST** /document_submissions | Submit a new document.
[**showDocumentSubmissionEvidence**](DocumentSubmissionsApi.md#showDocumentSubmissionEvidence) | **GET** /document_submissions/{guid}/evidence/{evidence_type} | Get DocumentSubmission Evidence



## createDocumentSubmission

> DocumentSubmissionResult createDocumentSubmission(documentSubmission)

Submit a new document.

Submit a document for delivery. This endpoint will replaces the /invoice_submissions endpoint which will soon be deprecated.

### Example

```javascript
import StorecoveApi from 'storecove_api';
let defaultClient = StorecoveApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new StorecoveApi.DocumentSubmissionsApi();
let documentSubmission = new StorecoveApi.DocumentSubmission(); // DocumentSubmission | Document to submit
apiInstance.createDocumentSubmission(documentSubmission, (error, data, response) => {
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
 **documentSubmission** | [**DocumentSubmission**](DocumentSubmission.md)| Document to submit | 

### Return type

[**DocumentSubmissionResult**](DocumentSubmissionResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## showDocumentSubmissionEvidence

> DocumentSubmissionEvidence showDocumentSubmissionEvidence(guid, evidenceType)

Get DocumentSubmission Evidence

Get evidence for a DocumentSubmission by GUID with corresponding status

### Example

```javascript
import StorecoveApi from 'storecove_api';
let defaultClient = StorecoveApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new StorecoveApi.DocumentSubmissionsApi();
let guid = "guid_example"; // String | DocumentSubmission GUID
let evidenceType = "'sending'"; // String | Type of evidence requested
apiInstance.showDocumentSubmissionEvidence(guid, evidenceType, (error, data, response) => {
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
 **guid** | **String**| DocumentSubmission GUID | 
 **evidenceType** | **String**| Type of evidence requested | [default to &#39;sending&#39;]

### Return type

[**DocumentSubmissionEvidence**](DocumentSubmissionEvidence.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

