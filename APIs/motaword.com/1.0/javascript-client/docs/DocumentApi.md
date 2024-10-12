# MotaWordApi.DocumentApi

All URIs are relative to *https://api.motaword.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAllDocumentSubjects**](DocumentApi.md#getAllDocumentSubjects) | **GET** /documents/subjects | Get a list of subjects of projects
[**getDocument**](DocumentApi.md#getDocument) | **GET** /documents/{documentId} | View a single document
[**getDocumentProgress**](DocumentApi.md#getDocumentProgress) | **GET** /documents/{documentId}/progress | View a document translation progress
[**getDocuments**](DocumentApi.md#getDocuments) | **GET** /documents | View your documents
[**getSimilarDocuments**](DocumentApi.md#getSimilarDocuments) | **GET** /documents/{documentId}/similars | Find documents similar to this document.
[**getUserDocuments**](DocumentApi.md#getUserDocuments) | **GET** /{userId}/documents | Get a list of your documents
[**regeneratePreview**](DocumentApi.md#regeneratePreview) | **POST** /documents/{documentId}/regenerate_preview | Regenerate preview and return preview URL for given file
[**useAsDraft**](DocumentApi.md#useAsDraft) | **POST** /documents/{documentId}/use_as_draft | Use the translation of given source manual document as manual draft source for the given target document.
[**useAsRegular**](DocumentApi.md#useAsRegular) | **POST** /documents/{documentId}/use_as_regular | Use the translation of the given manual document as a regular file.



## getAllDocumentSubjects

> [DocumentSubjects] getAllDocumentSubjects()

Get a list of subjects of projects

Get a list of subjects of projects

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.DocumentApi();
apiInstance.getAllDocumentSubjects((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[DocumentSubjects]**](DocumentSubjects.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDocument

> ContinuousProjectDocument getDocument(documentId)

View a single document

View a single document from your MotaWord account with its translation info.

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.DocumentApi();
let documentId = "179469"; // String | Document ID or filename
apiInstance.getDocument(documentId, (error, data, response) => {
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
 **documentId** | **String**| Document ID or filename | 

### Return type

[**ContinuousProjectDocument**](ContinuousProjectDocument.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDocumentProgress

> Progress getDocumentProgress(documentId)

View a document translation progress

View the translation or proofreading progress of a document in your account. You can also track the progress of a document under the project that it was ordered with.

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.DocumentApi();
let documentId = 179469; // Number | Document ID
apiInstance.getDocumentProgress(documentId, (error, data, response) => {
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
 **documentId** | **Number**| Document ID | 

### Return type

[**Progress**](Progress.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDocuments

> DocumentList getDocuments(opts)

View your documents

View a list of files and documents that you have translations for. This endpoint lets you view your MotaWord account as a multilingual translated file repository, without needing to go through your projects to interact with files in them.

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.DocumentApi();
let opts = {
  'recent': true, // Boolean | When true, this will return the most 4 recent active documents.
  'search': "search_example", // String | 
  'typeFilter': "'ALL'", // String | 
  'languageCode': "languageCode_example", // String | searches in source language of documents, in source and target languages of document's quote
  'page': 1, // Number | 
  'perPage': 10, // Number | 
  'orderBy': "'updated_at'", // String | 
  'orderType': new MotaWordApi.ListOrderType(), // ListOrderType | 
  '_with': ["null"] // [String] | Attach further information. Possible values 'preview' to fetch temporary preview URLs. This is NOT recommended to be used with list calls. Only use with[]=preview for single document/style guide calls.
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
 **recent** | **Boolean**| When true, this will return the most 4 recent active documents. | [optional] 
 **search** | **String**|  | [optional] 
 **typeFilter** | **String**|  | [optional] [default to &#39;ALL&#39;]
 **languageCode** | **String**| searches in source language of documents, in source and target languages of document&#39;s quote | [optional] 
 **page** | **Number**|  | [optional] [default to 1]
 **perPage** | **Number**|  | [optional] [default to 10]
 **orderBy** | **String**|  | [optional] [default to &#39;updated_at&#39;]
 **orderType** | [**ListOrderType**](.md)|  | [optional] 
 **_with** | [**[String]**](String.md)| Attach further information. Possible values &#39;preview&#39; to fetch temporary preview URLs. This is NOT recommended to be used with list calls. Only use with[]&#x3D;preview for single document/style guide calls. | [optional] 

### Return type

[**DocumentList**](DocumentList.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSimilarDocuments

> DocumentList getSimilarDocuments(documentId, opts)

Find documents similar to this document.

Find documents similar to this document. Optionally, include translation information.

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.DocumentApi();
let documentId = 179469; // Number | Document ID
let opts = {
  'perPage': 1, // Number | Determines the number of similar documents to return.
  '_with': ["null"] // [String] | Attach further information. Possible values 'preview' to fetch temporary preview URLs. This is NOT recommended to be used with list calls. Only use with[]=preview for single document/style guide calls.
};
apiInstance.getSimilarDocuments(documentId, opts, (error, data, response) => {
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
 **documentId** | **Number**| Document ID | 
 **perPage** | **Number**| Determines the number of similar documents to return. | [optional] [default to 1]
 **_with** | [**[String]**](String.md)| Attach further information. Possible values &#39;preview&#39; to fetch temporary preview URLs. This is NOT recommended to be used with list calls. Only use with[]&#x3D;preview for single document/style guide calls. | [optional] 

### Return type

[**DocumentList**](DocumentList.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUserDocuments

> DocumentList getUserDocuments(userId, opts)

Get a list of your documents

Get a list of your documents

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.DocumentApi();
let userId = 1; // Number | User ID
let opts = {
  'recent': true, // Boolean | When true, this will return the most 4 recent active documents.
  'search': "search_example", // String | 
  'typeFilter': "'ALL'", // String | 
  'languageCode': "languageCode_example", // String | searches in source language of documents, in source and target languages of document's quote
  'page': 1, // Number | 
  'perPage': 10, // Number | 
  'orderBy': "'updated_at'", // String | 
  'orderType': new MotaWordApi.ListOrderType() // ListOrderType | 
};
apiInstance.getUserDocuments(userId, opts, (error, data, response) => {
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
 **userId** | **Number**| User ID | 
 **recent** | **Boolean**| When true, this will return the most 4 recent active documents. | [optional] 
 **search** | **String**|  | [optional] 
 **typeFilter** | **String**|  | [optional] [default to &#39;ALL&#39;]
 **languageCode** | **String**| searches in source language of documents, in source and target languages of document&#39;s quote | [optional] 
 **page** | **Number**|  | [optional] [default to 1]
 **perPage** | **Number**|  | [optional] [default to 10]
 **orderBy** | **String**|  | [optional] [default to &#39;updated_at&#39;]
 **orderType** | [**ListOrderType**](.md)|  | [optional] 

### Return type

[**DocumentList**](DocumentList.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## regeneratePreview

> RegeneratePreviewResponse regeneratePreview(documentId)

Regenerate preview and return preview URL for given file

Regenerate preview and return preview URL for given file

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.DocumentApi();
let documentId = 179469; // Number | Document ID
apiInstance.regeneratePreview(documentId, (error, data, response) => {
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
 **documentId** | **Number**| Document ID | 

### Return type

[**RegeneratePreviewResponse**](RegeneratePreviewResponse.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## useAsDraft

> OperationStatus useAsDraft(documentId, opts)

Use the translation of given source manual document as manual draft source for the given target document.

Use the translation of given source manual document as manual draft source for the given target document.

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.DocumentApi();
let documentId = 179469; // Number | Document ID
let opts = {
  'useAsDraftPayload': new MotaWordApi.UseAsDraftPayload() // UseAsDraftPayload | 
};
apiInstance.useAsDraft(documentId, opts, (error, data, response) => {
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
 **documentId** | **Number**| Document ID | 
 **useAsDraftPayload** | [**UseAsDraftPayload**](UseAsDraftPayload.md)|  | [optional] 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## useAsRegular

> OperationStatus useAsRegular(documentId, opts)

Use the translation of the given manual document as a regular file.

Use the translation of the given manual document as a regular file.

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.DocumentApi();
let documentId = 179469; // Number | Document ID
let opts = {
  'useAsRegularPayload': new MotaWordApi.UseAsRegularPayload() // UseAsRegularPayload | 
};
apiInstance.useAsRegular(documentId, opts, (error, data, response) => {
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
 **documentId** | **Number**| Document ID | 
 **useAsRegularPayload** | [**UseAsRegularPayload**](UseAsRegularPayload.md)|  | [optional] 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

