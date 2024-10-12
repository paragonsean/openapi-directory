# Id4iApi.StorageApi

All URIs are relative to *http://backend.id4i.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createDocument**](StorageApi.md#createDocument) | **POST** /api/v1/documents/{id4n}/{organizationId} | Create an document for an id4n
[**deleteDocument**](StorageApi.md#deleteDocument) | **DELETE** /api/v1/documents/{id4n}/{organizationId}/{fileName} | Delete a document
[**getDocument**](StorageApi.md#getDocument) | **GET** /api/v1/documents/{id4n}/{organizationId}/{fileName}/metadata | Retrieve a document (meta-data only, no content)
[**getPublicDocument_0**](StorageApi.md#getPublicDocument_0) | **GET** /api/v1/public/documents/{id4n}/{organizationId}/{fileName}/metadata | Retrieve a public document (meta-data only, no content)
[**listAllDocuments**](StorageApi.md#listAllDocuments) | **GET** /api/v1/documents/{id4n} | List documents
[**listAllPublicDocuments_0**](StorageApi.md#listAllPublicDocuments_0) | **GET** /api/v1/public/documents/{id4n} | List public documents
[**listDocuments**](StorageApi.md#listDocuments) | **GET** /api/v1/documents/{id4n}/{organizationId} | List organization specific documents
[**putDocument**](StorageApi.md#putDocument) | **PUT** /api/v1/documents/{id4n}/{organizationId} | Put an document for an id4n
[**readDocument**](StorageApi.md#readDocument) | **GET** /api/v1/documents/{id4n}/{organizationId}/{fileName} | Read document contents
[**readFromMicrostorage**](StorageApi.md#readFromMicrostorage) | **GET** /api/v1/microstorage/{id4n}/{organization} | Read data from microstorage
[**readPublicDocument_0**](StorageApi.md#readPublicDocument_0) | **GET** /api/v1/public/documents/{id4n}/{organizationId}/{fileName} | Read public document contents
[**updateDocumentMetadata**](StorageApi.md#updateDocumentMetadata) | **PATCH** /api/v1/documents/{id4n}/{organizationId}/{fileName}/metadata | Update a document
[**writeToMicrostorage**](StorageApi.md#writeToMicrostorage) | **PUT** /api/v1/microstorage/{id4n}/{organization} | Write data to microstorage



## createDocument

> Document createDocument(organizationId, id4n, content)

Create an document for an id4n

The documents&#39; mime type is suggested on octet-stream data. Otherwise the specified content mime type is used.

### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.StorageApi();
let organizationId = "organizationId_example"; // String | organizationId
let id4n = "id4n_example"; // String | id4n
let content = "/path/to/file"; // File | content
apiInstance.createDocument(organizationId, id4n, content, (error, data, response) => {
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
 **organizationId** | **String**| organizationId | 
 **id4n** | **String**| id4n | 
 **content** | **File**| content | 

### Return type

[**Document**](Document.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json, application/xml


## deleteDocument

> deleteDocument(organizationId, id4n, fileName)

Delete a document

### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.StorageApi();
let organizationId = "organizationId_example"; // String | organizationId
let id4n = "id4n_example"; // String | id4n
let fileName = "fileName_example"; // String | fileName
apiInstance.deleteDocument(organizationId, id4n, fileName, (error, data, response) => {
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
 **organizationId** | **String**| organizationId | 
 **id4n** | **String**| id4n | 
 **fileName** | **String**| fileName | 

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getDocument

> Document getDocument(organizationId, id4n, fileName)

Retrieve a document (meta-data only, no content)

### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.StorageApi();
let organizationId = "organizationId_example"; // String | organizationId
let id4n = "id4n_example"; // String | id4n
let fileName = "fileName_example"; // String | fileName
apiInstance.getDocument(organizationId, id4n, fileName, (error, data, response) => {
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
 **organizationId** | **String**| organizationId | 
 **id4n** | **String**| id4n | 
 **fileName** | **String**| fileName | 

### Return type

[**Document**](Document.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getPublicDocument_0

> Document getPublicDocument_0(organizationId, id4n, fileName)

Retrieve a public document (meta-data only, no content)

### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.StorageApi();
let organizationId = "organizationId_example"; // String | organizationId
let id4n = "id4n_example"; // String | id4n
let fileName = "fileName_example"; // String | fileName
apiInstance.getPublicDocument_0(organizationId, id4n, fileName, (error, data, response) => {
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
 **organizationId** | **String**| organizationId | 
 **id4n** | **String**| id4n | 
 **fileName** | **String**| fileName | 

### Return type

[**Document**](Document.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## listAllDocuments

> PaginatedResponseOfDocument listAllDocuments(id4n, opts)

List documents

Listing all documents of an id4n

### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.StorageApi();
let id4n = "id4n_example"; // String | id4n
let opts = {
  'owner': "owner_example", // String | Filter by owner organization
  'offset': 56, // Number | Start with the n-th element
  'limit': 56 // Number | The maximum count of returned elements
};
apiInstance.listAllDocuments(id4n, opts, (error, data, response) => {
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
 **id4n** | **String**| id4n | 
 **owner** | **String**| Filter by owner organization | [optional] 
 **offset** | **Number**| Start with the n-th element | [optional] 
 **limit** | **Number**| The maximum count of returned elements | [optional] 

### Return type

[**PaginatedResponseOfDocument**](PaginatedResponseOfDocument.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## listAllPublicDocuments_0

> PaginatedResponseOfDocument listAllPublicDocuments_0(id4n, opts)

List public documents

Listing all public documents of an id4n

### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.StorageApi();
let id4n = "id4n_example"; // String | id4n
let opts = {
  'organizationId': "organizationId_example", // String | organizationId
  'owner': "owner_example", // String | Filter by owner organization
  'offset': 56, // Number | Start with the n-th element
  'limit': 56 // Number | The maximum count of returned elements
};
apiInstance.listAllPublicDocuments_0(id4n, opts, (error, data, response) => {
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
 **id4n** | **String**| id4n | 
 **organizationId** | **String**| organizationId | [optional] 
 **owner** | **String**| Filter by owner organization | [optional] 
 **offset** | **Number**| Start with the n-th element | [optional] 
 **limit** | **Number**| The maximum count of returned elements | [optional] 

### Return type

[**PaginatedResponseOfDocument**](PaginatedResponseOfDocument.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## listDocuments

> PaginatedResponseOfDocument listDocuments(organizationId, id4n, opts)

List organization specific documents

Listing documents of an id4n seen by a specified organization

### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.StorageApi();
let organizationId = "organizationId_example"; // String | organizationId
let id4n = "id4n_example"; // String | id4n
let opts = {
  'owner': "owner_example", // String | Filter by owner organization
  'offset': 56, // Number | Start with the n-th element
  'limit': 56 // Number | The maximum count of returned elements
};
apiInstance.listDocuments(organizationId, id4n, opts, (error, data, response) => {
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
 **organizationId** | **String**| organizationId | 
 **id4n** | **String**| id4n | 
 **owner** | **String**| Filter by owner organization | [optional] 
 **offset** | **Number**| Start with the n-th element | [optional] 
 **limit** | **Number**| The maximum count of returned elements | [optional] 

### Return type

[**PaginatedResponseOfDocument**](PaginatedResponseOfDocument.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## putDocument

> Document putDocument(organizationId, id4n, content)

Put an document for an id4n

Creating or overwriting an existing document 

### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.StorageApi();
let organizationId = "organizationId_example"; // String | organizationId
let id4n = "id4n_example"; // String | id4n
let content = "/path/to/file"; // File | content
apiInstance.putDocument(organizationId, id4n, content, (error, data, response) => {
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
 **organizationId** | **String**| organizationId | 
 **id4n** | **String**| id4n | 
 **content** | **File**| content | 

### Return type

[**Document**](Document.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json, application/xml


## readDocument

> Blob readDocument(organizationId, id4n, fileName)

Read document contents

### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.StorageApi();
let organizationId = "organizationId_example"; // String | organizationId
let id4n = "id4n_example"; // String | id4n
let fileName = "fileName_example"; // String | fileName
apiInstance.readDocument(organizationId, id4n, fileName, (error, data, response) => {
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
 **organizationId** | **String**| organizationId | 
 **id4n** | **String**| id4n | 
 **fileName** | **String**| fileName | 

### Return type

**Blob**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## readFromMicrostorage

> Blob readFromMicrostorage(organization, id4n)

Read data from microstorage

### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.StorageApi();
let organization = "organization_example"; // String | organization
let id4n = "id4n_example"; // String | id4n
apiInstance.readFromMicrostorage(organization, id4n, (error, data, response) => {
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
 **organization** | **String**| organization | 
 **id4n** | **String**| id4n | 

### Return type

**Blob**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## readPublicDocument_0

> Blob readPublicDocument_0(organizationId, id4n, fileName)

Read public document contents

### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.StorageApi();
let organizationId = "organizationId_example"; // String | organizationId
let id4n = "id4n_example"; // String | id4n
let fileName = "fileName_example"; // String | fileName
apiInstance.readPublicDocument_0(organizationId, id4n, fileName, (error, data, response) => {
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
 **organizationId** | **String**| organizationId | 
 **id4n** | **String**| id4n | 
 **fileName** | **String**| fileName | 

### Return type

**Blob**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## updateDocumentMetadata

> Document updateDocumentMetadata(organizationId, id4n, fileName, documentUpdate)

Update a document

### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.StorageApi();
let organizationId = "organizationId_example"; // String | organizationId
let id4n = "id4n_example"; // String | id4n
let fileName = "fileName_example"; // String | fileName
let documentUpdate = new Id4iApi.DocumentUpdate(); // DocumentUpdate | document
apiInstance.updateDocumentMetadata(organizationId, id4n, fileName, documentUpdate, (error, data, response) => {
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
 **organizationId** | **String**| organizationId | 
 **id4n** | **String**| id4n | 
 **fileName** | **String**| fileName | 
 **documentUpdate** | [**DocumentUpdate**](DocumentUpdate.md)| document | 

### Return type

[**Document**](Document.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## writeToMicrostorage

> Object writeToMicrostorage(organization, id4n, opts)

Write data to microstorage

### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.StorageApi();
let organization = "organization_example"; // String | organization
let id4n = "id4n_example"; // String | id4n
let opts = {
  'contentType': "contentType_example", // String | Content-Type
  'contentLength': 789, // Number | Content-Length
  'body': null // Blob | body
};
apiInstance.writeToMicrostorage(organization, id4n, opts, (error, data, response) => {
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
 **organization** | **String**| organization | 
 **id4n** | **String**| id4n | 
 **contentType** | **String**| Content-Type | [optional] 
 **contentLength** | **Number**| Content-Length | [optional] 
 **body** | **Blob**| body | [optional] 

### Return type

**Object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

