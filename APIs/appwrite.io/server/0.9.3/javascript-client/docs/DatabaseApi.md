# Appwrite.DatabaseApi

All URIs are relative to *https://appwrite.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**databaseCreateCollection**](DatabaseApi.md#databaseCreateCollection) | **POST** /database/collections | Create Collection
[**databaseCreateDocument**](DatabaseApi.md#databaseCreateDocument) | **POST** /database/collections/{collectionId}/documents | Create Document
[**databaseDeleteCollection**](DatabaseApi.md#databaseDeleteCollection) | **DELETE** /database/collections/{collectionId} | Delete Collection
[**databaseDeleteDocument**](DatabaseApi.md#databaseDeleteDocument) | **DELETE** /database/collections/{collectionId}/documents/{documentId} | Delete Document
[**databaseGetCollection**](DatabaseApi.md#databaseGetCollection) | **GET** /database/collections/{collectionId} | Get Collection
[**databaseGetDocument**](DatabaseApi.md#databaseGetDocument) | **GET** /database/collections/{collectionId}/documents/{documentId} | Get Document
[**databaseListCollections**](DatabaseApi.md#databaseListCollections) | **GET** /database/collections | List Collections
[**databaseListDocuments**](DatabaseApi.md#databaseListDocuments) | **GET** /database/collections/{collectionId}/documents | List Documents
[**databaseUpdateCollection**](DatabaseApi.md#databaseUpdateCollection) | **PUT** /database/collections/{collectionId} | Update Collection
[**databaseUpdateDocument**](DatabaseApi.md#databaseUpdateDocument) | **PATCH** /database/collections/{collectionId}/documents/{documentId} | Update Document



## databaseCreateCollection

> Collection databaseCreateCollection(opts)

Create Collection

Create a new Collection.

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: Key
let Key = defaultClient.authentications['Key'];
Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Key.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.DatabaseApi();
let opts = {
  'databaseCreateCollectionRequest': new Appwrite.DatabaseCreateCollectionRequest() // DatabaseCreateCollectionRequest | 
};
apiInstance.databaseCreateCollection(opts, (error, data, response) => {
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
 **databaseCreateCollectionRequest** | [**DatabaseCreateCollectionRequest**](DatabaseCreateCollectionRequest.md)|  | [optional] 

### Return type

[**Collection**](Collection.md)

### Authorization

[Project](../README.md#Project), [Key](../README.md#Key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## databaseCreateDocument

> Document databaseCreateDocument(collectionId, opts)

Create Document

Create a new Document. Before using this route, you should create a new collection resource using either a [server integration](/docs/server/database#databaseCreateCollection) API or directly from your database console.

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.apiKeyPrefix = 'Token';
// Configure API key authorization: Key
let Key = defaultClient.authentications['Key'];
Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Key.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.DatabaseApi();
let collectionId = "collectionId_example"; // String | Collection unique ID. You can create a new collection with validation rules using the Database service [server integration](/docs/server/database#createCollection).
let opts = {
  'databaseCreateDocumentRequest': new Appwrite.DatabaseCreateDocumentRequest() // DatabaseCreateDocumentRequest | 
};
apiInstance.databaseCreateDocument(collectionId, opts, (error, data, response) => {
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
 **collectionId** | **String**| Collection unique ID. You can create a new collection with validation rules using the Database service [server integration](/docs/server/database#createCollection). | 
 **databaseCreateDocumentRequest** | [**DatabaseCreateDocumentRequest**](DatabaseCreateDocumentRequest.md)|  | [optional] 

### Return type

[**Document**](Document.md)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT), [Key](../README.md#Key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## databaseDeleteCollection

> databaseDeleteCollection(collectionId)

Delete Collection

Delete a collection by its unique ID. Only users with write permissions have access to delete this resource.

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: Key
let Key = defaultClient.authentications['Key'];
Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Key.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.DatabaseApi();
let collectionId = "collectionId_example"; // String | Collection unique ID.
apiInstance.databaseDeleteCollection(collectionId, (error, data, response) => {
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
 **collectionId** | **String**| Collection unique ID. | 

### Return type

null (empty response body)

### Authorization

[Project](../README.md#Project), [Key](../README.md#Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## databaseDeleteDocument

> databaseDeleteDocument(collectionId, documentId)

Delete Document

Delete a document by its unique ID. This endpoint deletes only the parent documents, its attributes and relations to other documents. Child documents **will not** be deleted.

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.apiKeyPrefix = 'Token';
// Configure API key authorization: Key
let Key = defaultClient.authentications['Key'];
Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Key.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.DatabaseApi();
let collectionId = "collectionId_example"; // String | Collection unique ID. You can create a new collection with validation rules using the Database service [server integration](/docs/server/database#createCollection).
let documentId = "documentId_example"; // String | Document unique ID.
apiInstance.databaseDeleteDocument(collectionId, documentId, (error, data, response) => {
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
 **collectionId** | **String**| Collection unique ID. You can create a new collection with validation rules using the Database service [server integration](/docs/server/database#createCollection). | 
 **documentId** | **String**| Document unique ID. | 

### Return type

null (empty response body)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT), [Key](../README.md#Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## databaseGetCollection

> Collection databaseGetCollection(collectionId)

Get Collection

Get a collection by its unique ID. This endpoint response returns a JSON object with the collection metadata.

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: Key
let Key = defaultClient.authentications['Key'];
Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Key.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.DatabaseApi();
let collectionId = "collectionId_example"; // String | Collection unique ID.
apiInstance.databaseGetCollection(collectionId, (error, data, response) => {
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
 **collectionId** | **String**| Collection unique ID. | 

### Return type

[**Collection**](Collection.md)

### Authorization

[Project](../README.md#Project), [Key](../README.md#Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## databaseGetDocument

> Document databaseGetDocument(collectionId, documentId)

Get Document

Get a document by its unique ID. This endpoint response returns a JSON object with the document data.

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.apiKeyPrefix = 'Token';
// Configure API key authorization: Key
let Key = defaultClient.authentications['Key'];
Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Key.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.DatabaseApi();
let collectionId = "collectionId_example"; // String | Collection unique ID. You can create a new collection with validation rules using the Database service [server integration](/docs/server/database#createCollection).
let documentId = "documentId_example"; // String | Document unique ID.
apiInstance.databaseGetDocument(collectionId, documentId, (error, data, response) => {
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
 **collectionId** | **String**| Collection unique ID. You can create a new collection with validation rules using the Database service [server integration](/docs/server/database#createCollection). | 
 **documentId** | **String**| Document unique ID. | 

### Return type

[**Document**](Document.md)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT), [Key](../README.md#Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## databaseListCollections

> CollectionList databaseListCollections(opts)

List Collections

Get a list of all the user collections. You can use the query params to filter your results. On admin mode, this endpoint will return a list of all of the project&#39;s collections. [Learn more about different API modes](/docs/admin).

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: Key
let Key = defaultClient.authentications['Key'];
Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Key.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.DatabaseApi();
let opts = {
  'search': "''", // String | Search term to filter your list results. Max length: 256 chars.
  'limit': 25, // Number | Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per request.
  'offset': 0, // Number | Results offset. The default value is 0. Use this param to manage pagination.
  'orderType': "'ASC'" // String | Order result by ASC or DESC order.
};
apiInstance.databaseListCollections(opts, (error, data, response) => {
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
 **search** | **String**| Search term to filter your list results. Max length: 256 chars. | [optional] [default to &#39;&#39;]
 **limit** | **Number**| Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per request. | [optional] [default to 25]
 **offset** | **Number**| Results offset. The default value is 0. Use this param to manage pagination. | [optional] [default to 0]
 **orderType** | **String**| Order result by ASC or DESC order. | [optional] [default to &#39;ASC&#39;]

### Return type

[**CollectionList**](CollectionList.md)

### Authorization

[Project](../README.md#Project), [Key](../README.md#Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## databaseListDocuments

> DocumentList databaseListDocuments(collectionId, opts)

List Documents

Get a list of all the user documents. You can use the query params to filter your results. On admin mode, this endpoint will return a list of all of the project&#39;s documents. [Learn more about different API modes](/docs/admin).

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.apiKeyPrefix = 'Token';
// Configure API key authorization: Key
let Key = defaultClient.authentications['Key'];
Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Key.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.DatabaseApi();
let collectionId = "collectionId_example"; // String | Collection unique ID. You can create a new collection with validation rules using the Database service [server integration](/docs/server/database#createCollection).
let opts = {
  'filters': ["null"], // [String] | Array of filter strings. Each filter is constructed from a key name, comparison operator (=, !=, >, <, <=, >=) and a value. You can also use a dot (.) separator in attribute names to filter by child document attributes. Examples: 'name=John Doe' or 'category.$id>=5bed2d152c362'.
  'limit': 25, // Number | Maximum number of documents to return in response.  Use this value to manage pagination. By default will return maximum 25 results. Maximum of 100 results allowed per request.
  'offset': 0, // Number | Offset value. The default value is 0. Use this param to manage pagination.
  'orderField': "''", // String | Document field that results will be sorted by.
  'orderType': "'ASC'", // String | Order direction. Possible values are DESC for descending order, or ASC for ascending order.
  'orderCast': "'string'", // String | Order field type casting. Possible values are int, string, date, time or datetime. The database will attempt to cast the order field to the value you pass here. The default value is a string.
  'search': "''" // String | Search query. Enter any free text search. The database will try to find a match against all document attributes and children. Max length: 256 chars.
};
apiInstance.databaseListDocuments(collectionId, opts, (error, data, response) => {
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
 **collectionId** | **String**| Collection unique ID. You can create a new collection with validation rules using the Database service [server integration](/docs/server/database#createCollection). | 
 **filters** | [**[String]**](String.md)| Array of filter strings. Each filter is constructed from a key name, comparison operator (&#x3D;, !&#x3D;, &gt;, &lt;, &lt;&#x3D;, &gt;&#x3D;) and a value. You can also use a dot (.) separator in attribute names to filter by child document attributes. Examples: &#39;name&#x3D;John Doe&#39; or &#39;category.$id&gt;&#x3D;5bed2d152c362&#39;. | [optional] 
 **limit** | **Number**| Maximum number of documents to return in response.  Use this value to manage pagination. By default will return maximum 25 results. Maximum of 100 results allowed per request. | [optional] [default to 25]
 **offset** | **Number**| Offset value. The default value is 0. Use this param to manage pagination. | [optional] [default to 0]
 **orderField** | **String**| Document field that results will be sorted by. | [optional] [default to &#39;&#39;]
 **orderType** | **String**| Order direction. Possible values are DESC for descending order, or ASC for ascending order. | [optional] [default to &#39;ASC&#39;]
 **orderCast** | **String**| Order field type casting. Possible values are int, string, date, time or datetime. The database will attempt to cast the order field to the value you pass here. The default value is a string. | [optional] [default to &#39;string&#39;]
 **search** | **String**| Search query. Enter any free text search. The database will try to find a match against all document attributes and children. Max length: 256 chars. | [optional] [default to &#39;&#39;]

### Return type

[**DocumentList**](DocumentList.md)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT), [Key](../README.md#Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## databaseUpdateCollection

> Collection databaseUpdateCollection(collectionId, opts)

Update Collection

Update a collection by its unique ID.

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: Key
let Key = defaultClient.authentications['Key'];
Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Key.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.DatabaseApi();
let collectionId = "collectionId_example"; // String | Collection unique ID.
let opts = {
  'databaseUpdateCollectionRequest': new Appwrite.DatabaseUpdateCollectionRequest() // DatabaseUpdateCollectionRequest | 
};
apiInstance.databaseUpdateCollection(collectionId, opts, (error, data, response) => {
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
 **collectionId** | **String**| Collection unique ID. | 
 **databaseUpdateCollectionRequest** | [**DatabaseUpdateCollectionRequest**](DatabaseUpdateCollectionRequest.md)|  | [optional] 

### Return type

[**Collection**](Collection.md)

### Authorization

[Project](../README.md#Project), [Key](../README.md#Key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## databaseUpdateDocument

> Document databaseUpdateDocument(collectionId, documentId, opts)

Update Document

Update a document by its unique ID. Using the patch method you can pass only specific fields that will get updated.

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.apiKeyPrefix = 'Token';
// Configure API key authorization: Key
let Key = defaultClient.authentications['Key'];
Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Key.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.DatabaseApi();
let collectionId = "collectionId_example"; // String | Collection unique ID. You can create a new collection with validation rules using the Database service [server integration](/docs/server/database#createCollection).
let documentId = "documentId_example"; // String | Document unique ID.
let opts = {
  'databaseUpdateDocumentRequest': new Appwrite.DatabaseUpdateDocumentRequest() // DatabaseUpdateDocumentRequest | 
};
apiInstance.databaseUpdateDocument(collectionId, documentId, opts, (error, data, response) => {
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
 **collectionId** | **String**| Collection unique ID. You can create a new collection with validation rules using the Database service [server integration](/docs/server/database#createCollection). | 
 **documentId** | **String**| Document unique ID. | 
 **databaseUpdateDocumentRequest** | [**DatabaseUpdateDocumentRequest**](DatabaseUpdateDocumentRequest.md)|  | [optional] 

### Return type

[**Document**](Document.md)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT), [Key](../README.md#Key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

