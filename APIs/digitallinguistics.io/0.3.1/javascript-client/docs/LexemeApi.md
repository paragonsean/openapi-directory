# Dlx.LexemeApi

All URIs are relative to *https://api.digitallinguistics.io/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addLexeme**](LexemeApi.md#addLexeme) | **POST** /lexemes | Add a new Lexeme
[**addLexemeByLanguage_0**](LexemeApi.md#addLexemeByLanguage_0) | **POST** /languages/{languageID}/lexemes | Add a new Lexeme to a Language
[**deleteLexeme**](LexemeApi.md#deleteLexeme) | **DELETE** /lexemes/{lexemeID} | Delete a Lexeme by ID
[**deleteLexemeByLanguage_0**](LexemeApi.md#deleteLexemeByLanguage_0) | **DELETE** /languages/{languageID}/lexemes/{lexemeID} | Delete a Lexeme by ID
[**getLexeme**](LexemeApi.md#getLexeme) | **GET** /lexemes/{lexemeID} | Get a Lexeme by ID
[**getLexemeByLanguage_0**](LexemeApi.md#getLexemeByLanguage_0) | **GET** /languages/{languageID}/lexemes/{lexemeID} | Get a Lexeme by ID
[**getLexemes**](LexemeApi.md#getLexemes) | **GET** /lexemes | Get all Lexemes
[**getLexemesByLanguage_0**](LexemeApi.md#getLexemesByLanguage_0) | **GET** /languages/{languageID}/lexemes | Get all Lexemes for a Language
[**updateLexeme**](LexemeApi.md#updateLexeme) | **PATCH** /lexemes/{lexemeID} | Perform a partial update on a Lexeme
[**updateLexemeByLanguage**](LexemeApi.md#updateLexemeByLanguage) | **PATCH** /languages/{languageID}/lexemes/{lexemeID} | Perform a partial update on a Lexeme
[**upsertLexeme**](LexemeApi.md#upsertLexeme) | **PUT** /lexemes | Upsert (add or replace) a Lexeme
[**upsertLexemeByLanguage_0**](LexemeApi.md#upsertLexemeByLanguage_0) | **PUT** /languages/{languageID}/lexemes | Upsert (add or replace) a Lexeme



## addLexeme

> addLexeme(opts)

Add a new Lexeme

Add a new Lexeme. A &#x60;languageID&#x60; must be provided either as a query parameter, or as an attribute on the Lexeme body.

### Example

```javascript
import Dlx from 'dlx';
let defaultClient = Dlx.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Dlx.LexemeApi();
let opts = {
  'languageID': "languageID_example" // String | The ID of the Language to perform the operation on
};
apiInstance.addLexeme(opts, (error, data, response) => {
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
 **languageID** | **String**| The ID of the Language to perform the operation on | [optional] 

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## addLexemeByLanguage_0

> addLexemeByLanguage_0(languageID)

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

let apiInstance = new Dlx.LexemeApi();
let languageID = "languageID_example"; // String | The ID of the Language to perform the operation on
apiInstance.addLexemeByLanguage_0(languageID, (error, data, response) => {
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


## deleteLexeme

> deleteLexeme(lexemeID, opts)

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

let apiInstance = new Dlx.LexemeApi();
let lexemeID = "lexemeID_example"; // String | The ID of the Lexeme to perform the operation on
let opts = {
  'ifMatch': "ifMatch_example" // String | The `If-Match` header is used with PUT and DELETE requests to check whether you have the most up-to-date version of the resource before updating or deleting it. The value of the `If-Match` header is the ETag (`_etag`) property of the resource. It is recommended that your application use this header whenever possible to avoid data conflicts.
};
apiInstance.deleteLexeme(lexemeID, opts, (error, data, response) => {
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
 **lexemeID** | **String**| The ID of the Lexeme to perform the operation on | 
 **ifMatch** | **String**| The &#x60;If-Match&#x60; header is used with PUT and DELETE requests to check whether you have the most up-to-date version of the resource before updating or deleting it. The value of the &#x60;If-Match&#x60; header is the ETag (&#x60;_etag&#x60;) property of the resource. It is recommended that your application use this header whenever possible to avoid data conflicts. | [optional] 

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteLexemeByLanguage_0

> deleteLexemeByLanguage_0(languageID, lexemeID, opts)

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

let apiInstance = new Dlx.LexemeApi();
let languageID = "languageID_example"; // String | The ID of the Language to perform the operation on
let lexemeID = "lexemeID_example"; // String | The ID of the Lexeme to perform the operation on
let opts = {
  'ifMatch': "ifMatch_example" // String | The `If-Match` header is used with PUT and DELETE requests to check whether you have the most up-to-date version of the resource before updating or deleting it. The value of the `If-Match` header is the ETag (`_etag`) property of the resource. It is recommended that your application use this header whenever possible to avoid data conflicts.
};
apiInstance.deleteLexemeByLanguage_0(languageID, lexemeID, opts, (error, data, response) => {
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


## getLexeme

> getLexeme(lexemeID, opts)

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

let apiInstance = new Dlx.LexemeApi();
let lexemeID = "lexemeID_example"; // String | The ID of the Lexeme to perform the operation on
let opts = {
  'deleted': false, // Boolean | Setting the `deleted` option to `true` will return results that have been marked for deletion, but not yet deleted from the database. Otherwise requests for a resource marked for deletion will return a 410 error.
  'ifNoneMatch': "ifNoneMatch_example" // String | If `If-None-Match` header is used with GET requests to check whether you already have the most up-to-date version of the resource, and therefore do not need the resource sent again. The value of the `If-None-Match` header is the ETag (`_etag`) property of the resource. It is recommended that your application use this header whenever possible to reduce bandwidth.
};
apiInstance.getLexeme(lexemeID, opts, (error, data, response) => {
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


## getLexemeByLanguage_0

> getLexemeByLanguage_0(languageID, lexemeID, opts)

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

let apiInstance = new Dlx.LexemeApi();
let languageID = "languageID_example"; // String | The ID of the Language to perform the operation on
let lexemeID = "lexemeID_example"; // String | The ID of the Lexeme to perform the operation on
let opts = {
  'deleted': false, // Boolean | Setting the `deleted` option to `true` will return results that have been marked for deletion, but not yet deleted from the database. Otherwise requests for a resource marked for deletion will return a 410 error.
  'ifNoneMatch': "ifNoneMatch_example" // String | If `If-None-Match` header is used with GET requests to check whether you already have the most up-to-date version of the resource, and therefore do not need the resource sent again. The value of the `If-None-Match` header is the ETag (`_etag`) property of the resource. It is recommended that your application use this header whenever possible to reduce bandwidth.
};
apiInstance.getLexemeByLanguage_0(languageID, lexemeID, opts, (error, data, response) => {
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


## getLexemes

> getLexemes(opts)

Get all Lexemes

Retrieve all Lexemes that the authenticated user has permission to access. Include a &#x60;languageID&#x60; query parameter to limit results to Lexemes from a particular Language.

### Example

```javascript
import Dlx from 'dlx';
let defaultClient = Dlx.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Dlx.LexemeApi();
let opts = {
  'continuation': "continuation_example", // String | The `dlx-continuation` header is used to send a continuation token with the request, when retrieving the next page of results.
  'deleted': false, // Boolean | Setting the `deleted` option to `true` will return results that have been marked for deletion, but not yet deleted from the database. Otherwise requests for a resource marked for deletion will return a 410 error.
  'ifModifiedSince': "ifModifiedSince_example", // String | The `If-Modified-Since` header is used to retrieve only results modified since a given time. The value of this header must be a valid date string.
  'languageID': "languageID_example", // String | The ID of the Language to perform the operation on
  'maxItemCount': "maxItemCount_example", // String | The `dlx-max-item-count` header is used to limit the number of results to a certain amount at a time (by default all results will be returned). If there are more results to be returned, a continuation token will also be sent in the `dlx-continuation` header.
  '_public': "'false'" // String | Set this parameter to `true` to include all publicly-accessible resources, not just those that the user is listed as an Owner, Contributor, or Viewer for.
};
apiInstance.getLexemes(opts, (error, data, response) => {
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
 **languageID** | **String**| The ID of the Language to perform the operation on | [optional] 
 **maxItemCount** | **String**| The &#x60;dlx-max-item-count&#x60; header is used to limit the number of results to a certain amount at a time (by default all results will be returned). If there are more results to be returned, a continuation token will also be sent in the &#x60;dlx-continuation&#x60; header. | [optional] 
 **_public** | **String**| Set this parameter to &#x60;true&#x60; to include all publicly-accessible resources, not just those that the user is listed as an Owner, Contributor, or Viewer for. | [optional] [default to &#39;false&#39;]

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getLexemesByLanguage_0

> getLexemesByLanguage_0(languageID, opts)

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

let apiInstance = new Dlx.LexemeApi();
let languageID = "languageID_example"; // String | The ID of the Language to perform the operation on
let opts = {
  'continuation': "continuation_example", // String | The `dlx-continuation` header is used to send a continuation token with the request, when retrieving the next page of results.
  'deleted': false, // Boolean | Setting the `deleted` option to `true` will return results that have been marked for deletion, but not yet deleted from the database. Otherwise requests for a resource marked for deletion will return a 410 error.
  'ifModifiedSince': "ifModifiedSince_example", // String | The `If-Modified-Since` header is used to retrieve only results modified since a given time. The value of this header must be a valid date string.
  'maxItemCount': "maxItemCount_example", // String | The `dlx-max-item-count` header is used to limit the number of results to a certain amount at a time (by default all results will be returned). If there are more results to be returned, a continuation token will also be sent in the `dlx-continuation` header.
  '_public': "'false'" // String | Set this parameter to `true` to include all publicly-accessible resources, not just those that the user is listed as an Owner, Contributor, or Viewer for.
};
apiInstance.getLexemesByLanguage_0(languageID, opts, (error, data, response) => {
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


## updateLexeme

> updateLexeme(lexemeID, opts)

Perform a partial update on a Lexeme

Perform a partial update on a Lexeme.

### Example

```javascript
import Dlx from 'dlx';
let defaultClient = Dlx.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Dlx.LexemeApi();
let lexemeID = "lexemeID_example"; // String | The ID of the Lexeme to perform the operation on
let opts = {
  'ifMatch': "ifMatch_example" // String | The `If-Match` header is used with PUT and DELETE requests to check whether you have the most up-to-date version of the resource before updating or deleting it. The value of the `If-Match` header is the ETag (`_etag`) property of the resource. It is recommended that your application use this header whenever possible to avoid data conflicts.
};
apiInstance.updateLexeme(lexemeID, opts, (error, data, response) => {
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
 **lexemeID** | **String**| The ID of the Lexeme to perform the operation on | 
 **ifMatch** | **String**| The &#x60;If-Match&#x60; header is used with PUT and DELETE requests to check whether you have the most up-to-date version of the resource before updating or deleting it. The value of the &#x60;If-Match&#x60; header is the ETag (&#x60;_etag&#x60;) property of the resource. It is recommended that your application use this header whenever possible to avoid data conflicts. | [optional] 

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## updateLexemeByLanguage

> updateLexemeByLanguage(languageID, lexemeID, opts)

Perform a partial update on a Lexeme

### Example

```javascript
import Dlx from 'dlx';
let defaultClient = Dlx.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Dlx.LexemeApi();
let languageID = "languageID_example"; // String | The ID of the Language to perform the operation on
let lexemeID = "lexemeID_example"; // String | The ID of the Lexeme to perform the operation on
let opts = {
  'ifMatch': "ifMatch_example" // String | The `If-Match` header is used with PUT and DELETE requests to check whether you have the most up-to-date version of the resource before updating or deleting it. The value of the `If-Match` header is the ETag (`_etag`) property of the resource. It is recommended that your application use this header whenever possible to avoid data conflicts.
};
apiInstance.updateLexemeByLanguage(languageID, lexemeID, opts, (error, data, response) => {
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


## upsertLexeme

> upsertLexeme(opts)

Upsert (add or replace) a Lexeme

Upsert (add or replace) a Lexeme. A &#x60;languageID&#x60; must be provided either as a query parameter, or as an attribute on the Lexeme body.

### Example

```javascript
import Dlx from 'dlx';
let defaultClient = Dlx.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Dlx.LexemeApi();
let opts = {
  'ifMatch': "ifMatch_example", // String | The `If-Match` header is used with PUT and DELETE requests to check whether you have the most up-to-date version of the resource before updating or deleting it. The value of the `If-Match` header is the ETag (`_etag`) property of the resource. It is recommended that your application use this header whenever possible to avoid data conflicts.
  'languageID': "languageID_example" // String | The ID of the Language to perform the operation on
};
apiInstance.upsertLexeme(opts, (error, data, response) => {
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
 **ifMatch** | **String**| The &#x60;If-Match&#x60; header is used with PUT and DELETE requests to check whether you have the most up-to-date version of the resource before updating or deleting it. The value of the &#x60;If-Match&#x60; header is the ETag (&#x60;_etag&#x60;) property of the resource. It is recommended that your application use this header whenever possible to avoid data conflicts. | [optional] 
 **languageID** | **String**| The ID of the Language to perform the operation on | [optional] 

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## upsertLexemeByLanguage_0

> upsertLexemeByLanguage_0(languageID, opts)

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

let apiInstance = new Dlx.LexemeApi();
let languageID = "languageID_example"; // String | The ID of the Language to perform the operation on
let opts = {
  'ifMatch': "ifMatch_example" // String | The `If-Match` header is used with PUT and DELETE requests to check whether you have the most up-to-date version of the resource before updating or deleting it. The value of the `If-Match` header is the ETag (`_etag`) property of the resource. It is recommended that your application use this header whenever possible to avoid data conflicts.
};
apiInstance.upsertLexemeByLanguage_0(languageID, opts, (error, data, response) => {
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

