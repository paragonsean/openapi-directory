# Dlx.LanguageApi

All URIs are relative to *https://api.digitallinguistics.io/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addLanguage**](LanguageApi.md#addLanguage) | **POST** /languages | Add a new Language
[**addLexemeByLanguage**](LanguageApi.md#addLexemeByLanguage) | **POST** /languages/{languageID}/lexemes | Add a new Lexeme to a Language
[**deleteLanguage**](LanguageApi.md#deleteLanguage) | **DELETE** /languages/{languageID} | Delete a Language by ID
[**deleteLexemeByLanguage**](LanguageApi.md#deleteLexemeByLanguage) | **DELETE** /languages/{languageID}/lexemes/{lexemeID} | Delete a Lexeme by ID
[**getLanguage**](LanguageApi.md#getLanguage) | **GET** /languages/{languageID} | Retrieve a Language by ID
[**getLanguages**](LanguageApi.md#getLanguages) | **GET** /languages | Get all Languages
[**getLexemeByLanguage**](LanguageApi.md#getLexemeByLanguage) | **GET** /languages/{languageID}/lexemes/{lexemeID} | Get a Lexeme by ID
[**getLexemesByLanguage**](LanguageApi.md#getLexemesByLanguage) | **GET** /languages/{languageID}/lexemes | Get all Lexemes for a Language
[**updateLanguage**](LanguageApi.md#updateLanguage) | **PATCH** /languages/{languageID} | Perform a partial update on a Language
[**upsertLanguage**](LanguageApi.md#upsertLanguage) | **PUT** /languages | Upsert (create or replace) a Language
[**upsertLexemeByLanguage**](LanguageApi.md#upsertLexemeByLanguage) | **PUT** /languages/{languageID}/lexemes | Upsert (add or replace) a Lexeme



## addLanguage

> addLanguage(body)

Add a new Language

### Example

```javascript
import Dlx from 'dlx';
let defaultClient = Dlx.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Dlx.LanguageApi();
let body = {key: null}; // Object | A database resource to upsert
apiInstance.addLanguage(body, (error, data, response) => {
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
 **body** | **Object**| A database resource to upsert | 

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## addLexemeByLanguage

> addLexemeByLanguage(languageID)

Add a new Lexeme to a Language

### Example

```javascript
import Dlx from 'dlx';
let defaultClient = Dlx.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Dlx.LanguageApi();
let languageID = "languageID_example"; // String | The ID of the Language to perform the operation on
apiInstance.addLexemeByLanguage(languageID, (error, data, response) => {
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
 **languageID** | **String**| The ID of the Language to perform the operation on | 

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteLanguage

> deleteLanguage(languageID, opts)

Delete a Language by ID

### Example

```javascript
import Dlx from 'dlx';
let defaultClient = Dlx.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Dlx.LanguageApi();
let languageID = "languageID_example"; // String | The ID of the Language to perform the operation on
let opts = {
  'ifMatch': "ifMatch_example" // String | The `If-Match` header is used with PUT and DELETE requests to check whether you have the most up-to-date version of the resource before updating or deleting it. The value of the `If-Match` header is the ETag (`_etag`) property of the resource. It is recommended that your application use this header whenever possible to avoid data conflicts.
};
apiInstance.deleteLanguage(languageID, opts, (error, data, response) => {
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
 **languageID** | **String**| The ID of the Language to perform the operation on | 
 **ifMatch** | **String**| The &#x60;If-Match&#x60; header is used with PUT and DELETE requests to check whether you have the most up-to-date version of the resource before updating or deleting it. The value of the &#x60;If-Match&#x60; header is the ETag (&#x60;_etag&#x60;) property of the resource. It is recommended that your application use this header whenever possible to avoid data conflicts. | [optional] 

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteLexemeByLanguage

> deleteLexemeByLanguage(languageID, lexemeID, opts)

Delete a Lexeme by ID

### Example

```javascript
import Dlx from 'dlx';
let defaultClient = Dlx.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Dlx.LanguageApi();
let languageID = "languageID_example"; // String | The ID of the Language to perform the operation on
let lexemeID = "lexemeID_example"; // String | The ID of the Lexeme to perform the operation on
let opts = {
  'ifMatch': "ifMatch_example" // String | The `If-Match` header is used with PUT and DELETE requests to check whether you have the most up-to-date version of the resource before updating or deleting it. The value of the `If-Match` header is the ETag (`_etag`) property of the resource. It is recommended that your application use this header whenever possible to avoid data conflicts.
};
apiInstance.deleteLexemeByLanguage(languageID, lexemeID, opts, (error, data, response) => {
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
 **languageID** | **String**| The ID of the Language to perform the operation on | 
 **lexemeID** | **String**| The ID of the Lexeme to perform the operation on | 
 **ifMatch** | **String**| The &#x60;If-Match&#x60; header is used with PUT and DELETE requests to check whether you have the most up-to-date version of the resource before updating or deleting it. The value of the &#x60;If-Match&#x60; header is the ETag (&#x60;_etag&#x60;) property of the resource. It is recommended that your application use this header whenever possible to avoid data conflicts. | [optional] 

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getLanguage

> getLanguage(languageID, opts)

Retrieve a Language by ID

### Example

```javascript
import Dlx from 'dlx';
let defaultClient = Dlx.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Dlx.LanguageApi();
let languageID = "languageID_example"; // String | The ID of the Language to perform the operation on
let opts = {
  'deleted': false, // Boolean | Setting the `deleted` option to `true` will return results that have been marked for deletion, but not yet deleted from the database. Otherwise requests for a resource marked for deletion will return a 410 error.
  'ifNoneMatch': "ifNoneMatch_example" // String | If `If-None-Match` header is used with GET requests to check whether you already have the most up-to-date version of the resource, and therefore do not need the resource sent again. The value of the `If-None-Match` header is the ETag (`_etag`) property of the resource. It is recommended that your application use this header whenever possible to reduce bandwidth.
};
apiInstance.getLanguage(languageID, opts, (error, data, response) => {
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
 **languageID** | **String**| The ID of the Language to perform the operation on | 
 **deleted** | **Boolean**| Setting the &#x60;deleted&#x60; option to &#x60;true&#x60; will return results that have been marked for deletion, but not yet deleted from the database. Otherwise requests for a resource marked for deletion will return a 410 error. | [optional] [default to false]
 **ifNoneMatch** | **String**| If &#x60;If-None-Match&#x60; header is used with GET requests to check whether you already have the most up-to-date version of the resource, and therefore do not need the resource sent again. The value of the &#x60;If-None-Match&#x60; header is the ETag (&#x60;_etag&#x60;) property of the resource. It is recommended that your application use this header whenever possible to reduce bandwidth. | [optional] 

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getLanguages

> getLanguages(opts)

Get all Languages

Retrieves all the Languages that the authenticated user or client has permission to access.

### Example

```javascript
import Dlx from 'dlx';
let defaultClient = Dlx.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Dlx.LanguageApi();
let opts = {
  'continuation': "continuation_example", // String | The `dlx-continuation` header is used to send a continuation token with the request, when retrieving the next page of results.
  'deleted': false, // Boolean | Setting the `deleted` option to `true` will return results that have been marked for deletion, but not yet deleted from the database. Otherwise requests for a resource marked for deletion will return a 410 error.
  'ifModifiedSince': "ifModifiedSince_example", // String | The `If-Modified-Since` header is used to retrieve only results modified since a given time. The value of this header must be a valid date string.
  'maxItemCount': "maxItemCount_example", // String | The `dlx-max-item-count` header is used to limit the number of results to a certain amount at a time (by default all results will be returned). If there are more results to be returned, a continuation token will also be sent in the `dlx-continuation` header.
  '_public': "'false'" // String | Set this parameter to `true` to include all publicly-accessible resources, not just those that the user is listed as an Owner, Contributor, or Viewer for.
};
apiInstance.getLanguages(opts, (error, data, response) => {
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
 **continuation** | **String**| The &#x60;dlx-continuation&#x60; header is used to send a continuation token with the request, when retrieving the next page of results. | [optional] 
 **deleted** | **Boolean**| Setting the &#x60;deleted&#x60; option to &#x60;true&#x60; will return results that have been marked for deletion, but not yet deleted from the database. Otherwise requests for a resource marked for deletion will return a 410 error. | [optional] [default to false]
 **ifModifiedSince** | **String**| The &#x60;If-Modified-Since&#x60; header is used to retrieve only results modified since a given time. The value of this header must be a valid date string. | [optional] 
 **maxItemCount** | **String**| The &#x60;dlx-max-item-count&#x60; header is used to limit the number of results to a certain amount at a time (by default all results will be returned). If there are more results to be returned, a continuation token will also be sent in the &#x60;dlx-continuation&#x60; header. | [optional] 
 **_public** | **String**| Set this parameter to &#x60;true&#x60; to include all publicly-accessible resources, not just those that the user is listed as an Owner, Contributor, or Viewer for. | [optional] [default to &#39;false&#39;]

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getLexemeByLanguage

> getLexemeByLanguage(languageID, lexemeID, opts)

Get a Lexeme by ID

### Example

```javascript
import Dlx from 'dlx';
let defaultClient = Dlx.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Dlx.LanguageApi();
let languageID = "languageID_example"; // String | The ID of the Language to perform the operation on
let lexemeID = "lexemeID_example"; // String | The ID of the Lexeme to perform the operation on
let opts = {
  'deleted': false, // Boolean | Setting the `deleted` option to `true` will return results that have been marked for deletion, but not yet deleted from the database. Otherwise requests for a resource marked for deletion will return a 410 error.
  'ifNoneMatch': "ifNoneMatch_example" // String | If `If-None-Match` header is used with GET requests to check whether you already have the most up-to-date version of the resource, and therefore do not need the resource sent again. The value of the `If-None-Match` header is the ETag (`_etag`) property of the resource. It is recommended that your application use this header whenever possible to reduce bandwidth.
};
apiInstance.getLexemeByLanguage(languageID, lexemeID, opts, (error, data, response) => {
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
 **languageID** | **String**| The ID of the Language to perform the operation on | 
 **lexemeID** | **String**| The ID of the Lexeme to perform the operation on | 
 **deleted** | **Boolean**| Setting the &#x60;deleted&#x60; option to &#x60;true&#x60; will return results that have been marked for deletion, but not yet deleted from the database. Otherwise requests for a resource marked for deletion will return a 410 error. | [optional] [default to false]
 **ifNoneMatch** | **String**| If &#x60;If-None-Match&#x60; header is used with GET requests to check whether you already have the most up-to-date version of the resource, and therefore do not need the resource sent again. The value of the &#x60;If-None-Match&#x60; header is the ETag (&#x60;_etag&#x60;) property of the resource. It is recommended that your application use this header whenever possible to reduce bandwidth. | [optional] 

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getLexemesByLanguage

> getLexemesByLanguage(languageID, opts)

Get all Lexemes for a Language

### Example

```javascript
import Dlx from 'dlx';
let defaultClient = Dlx.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Dlx.LanguageApi();
let languageID = "languageID_example"; // String | The ID of the Language to perform the operation on
let opts = {
  'continuation': "continuation_example", // String | The `dlx-continuation` header is used to send a continuation token with the request, when retrieving the next page of results.
  'deleted': false, // Boolean | Setting the `deleted` option to `true` will return results that have been marked for deletion, but not yet deleted from the database. Otherwise requests for a resource marked for deletion will return a 410 error.
  'ifModifiedSince': "ifModifiedSince_example", // String | The `If-Modified-Since` header is used to retrieve only results modified since a given time. The value of this header must be a valid date string.
  'maxItemCount': "maxItemCount_example", // String | The `dlx-max-item-count` header is used to limit the number of results to a certain amount at a time (by default all results will be returned). If there are more results to be returned, a continuation token will also be sent in the `dlx-continuation` header.
  '_public': "'false'" // String | Set this parameter to `true` to include all publicly-accessible resources, not just those that the user is listed as an Owner, Contributor, or Viewer for.
};
apiInstance.getLexemesByLanguage(languageID, opts, (error, data, response) => {
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
 **languageID** | **String**| The ID of the Language to perform the operation on | 
 **continuation** | **String**| The &#x60;dlx-continuation&#x60; header is used to send a continuation token with the request, when retrieving the next page of results. | [optional] 
 **deleted** | **Boolean**| Setting the &#x60;deleted&#x60; option to &#x60;true&#x60; will return results that have been marked for deletion, but not yet deleted from the database. Otherwise requests for a resource marked for deletion will return a 410 error. | [optional] [default to false]
 **ifModifiedSince** | **String**| The &#x60;If-Modified-Since&#x60; header is used to retrieve only results modified since a given time. The value of this header must be a valid date string. | [optional] 
 **maxItemCount** | **String**| The &#x60;dlx-max-item-count&#x60; header is used to limit the number of results to a certain amount at a time (by default all results will be returned). If there are more results to be returned, a continuation token will also be sent in the &#x60;dlx-continuation&#x60; header. | [optional] 
 **_public** | **String**| Set this parameter to &#x60;true&#x60; to include all publicly-accessible resources, not just those that the user is listed as an Owner, Contributor, or Viewer for. | [optional] [default to &#39;false&#39;]

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## updateLanguage

> updateLanguage(languageID, body, opts)

Perform a partial update on a Language

Performs a partial update the Language whose ID is specified in the URL. If the Language object has an &#x60;id&#x60; property, is ignored in favor of the ID in the URL.

### Example

```javascript
import Dlx from 'dlx';
let defaultClient = Dlx.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Dlx.LanguageApi();
let languageID = "languageID_example"; // String | The ID of the Language to perform the operation on
let body = {key: null}; // Object | A database resource to upsert
let opts = {
  'ifMatch': "ifMatch_example" // String | The `If-Match` header is used with PUT and DELETE requests to check whether you have the most up-to-date version of the resource before updating or deleting it. The value of the `If-Match` header is the ETag (`_etag`) property of the resource. It is recommended that your application use this header whenever possible to avoid data conflicts.
};
apiInstance.updateLanguage(languageID, body, opts, (error, data, response) => {
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
 **languageID** | **String**| The ID of the Language to perform the operation on | 
 **body** | **Object**| A database resource to upsert | 
 **ifMatch** | **String**| The &#x60;If-Match&#x60; header is used with PUT and DELETE requests to check whether you have the most up-to-date version of the resource before updating or deleting it. The value of the &#x60;If-Match&#x60; header is the ETag (&#x60;_etag&#x60;) property of the resource. It is recommended that your application use this header whenever possible to avoid data conflicts. | [optional] 

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## upsertLanguage

> upsertLanguage(body, opts)

Upsert (create or replace) a Language

Creates a Language if it does not yet exist (i.e. if the resource does not have an &#x60;id&#x60; property yet), or replaces the existing Language resource if it does. Note that this replaces the *entire* Language. It is not a partial update.

### Example

```javascript
import Dlx from 'dlx';
let defaultClient = Dlx.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Dlx.LanguageApi();
let body = {key: null}; // Object | A database resource to upsert
let opts = {
  'ifMatch': "ifMatch_example" // String | The `If-Match` header is used with PUT and DELETE requests to check whether you have the most up-to-date version of the resource before updating or deleting it. The value of the `If-Match` header is the ETag (`_etag`) property of the resource. It is recommended that your application use this header whenever possible to avoid data conflicts.
};
apiInstance.upsertLanguage(body, opts, (error, data, response) => {
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
 **body** | **Object**| A database resource to upsert | 
 **ifMatch** | **String**| The &#x60;If-Match&#x60; header is used with PUT and DELETE requests to check whether you have the most up-to-date version of the resource before updating or deleting it. The value of the &#x60;If-Match&#x60; header is the ETag (&#x60;_etag&#x60;) property of the resource. It is recommended that your application use this header whenever possible to avoid data conflicts. | [optional] 

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## upsertLexemeByLanguage

> upsertLexemeByLanguage(languageID, opts)

Upsert (add or replace) a Lexeme

### Example

```javascript
import Dlx from 'dlx';
let defaultClient = Dlx.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Dlx.LanguageApi();
let languageID = "languageID_example"; // String | The ID of the Language to perform the operation on
let opts = {
  'ifMatch': "ifMatch_example" // String | The `If-Match` header is used with PUT and DELETE requests to check whether you have the most up-to-date version of the resource before updating or deleting it. The value of the `If-Match` header is the ETag (`_etag`) property of the resource. It is recommended that your application use this header whenever possible to avoid data conflicts.
};
apiInstance.upsertLexemeByLanguage(languageID, opts, (error, data, response) => {
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
 **languageID** | **String**| The ID of the Language to perform the operation on | 
 **ifMatch** | **String**| The &#x60;If-Match&#x60; header is used with PUT and DELETE requests to check whether you have the most up-to-date version of the resource before updating or deleting it. The value of the &#x60;If-Match&#x60; header is the ETag (&#x60;_etag&#x60;) property of the resource. It is recommended that your application use this header whenever possible to avoid data conflicts. | [optional] 

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

