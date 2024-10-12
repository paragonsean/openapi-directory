# EtherpadApi.AuthorApi

All URIs are relative to *http://etherpad.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createAuthorIfNotExistsForUsingGET**](AuthorApi.md#createAuthorIfNotExistsForUsingGET) | **GET** /createAuthorIfNotExistsFor | this functions helps you to map your application author ids to Etherpad author ids
[**createAuthorIfNotExistsForUsingPOST**](AuthorApi.md#createAuthorIfNotExistsForUsingPOST) | **POST** /createAuthorIfNotExistsFor | this functions helps you to map your application author ids to Etherpad author ids
[**createAuthorUsingGET**](AuthorApi.md#createAuthorUsingGET) | **GET** /createAuthor | creates a new author
[**createAuthorUsingPOST**](AuthorApi.md#createAuthorUsingPOST) | **POST** /createAuthor | creates a new author
[**getAuthorNameUsingGET**](AuthorApi.md#getAuthorNameUsingGET) | **GET** /getAuthorName | Returns the Author Name of the author
[**getAuthorNameUsingPOST**](AuthorApi.md#getAuthorNameUsingPOST) | **POST** /getAuthorName | Returns the Author Name of the author
[**listPadsOfAuthorUsingGET**](AuthorApi.md#listPadsOfAuthorUsingGET) | **GET** /listPadsOfAuthor | returns an array of all pads this author contributed to
[**listPadsOfAuthorUsingPOST**](AuthorApi.md#listPadsOfAuthorUsingPOST) | **POST** /listPadsOfAuthor | returns an array of all pads this author contributed to
[**listSessionsOfAuthorUsingGET**](AuthorApi.md#listSessionsOfAuthorUsingGET) | **GET** /listSessionsOfAuthor | returns all sessions of an author
[**listSessionsOfAuthorUsingPOST**](AuthorApi.md#listSessionsOfAuthorUsingPOST) | **POST** /listSessionsOfAuthor | returns all sessions of an author



## createAuthorIfNotExistsForUsingGET

> CreateAuthorUsingGET200Response createAuthorIfNotExistsForUsingGET(opts)

this functions helps you to map your application author ids to Etherpad author ids

### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.AuthorApi();
let opts = {
  'authorMapper': "authorMapper_example", // String | 
  'name': "name_example" // String | 
};
apiInstance.createAuthorIfNotExistsForUsingGET(opts, (error, data, response) => {
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
 **authorMapper** | **String**|  | [optional] 
 **name** | **String**|  | [optional] 

### Return type

[**CreateAuthorUsingGET200Response**](CreateAuthorUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## createAuthorIfNotExistsForUsingPOST

> CreateAuthorUsingGET200Response createAuthorIfNotExistsForUsingPOST(opts)

this functions helps you to map your application author ids to Etherpad author ids

### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.AuthorApi();
let opts = {
  'authorMapper': "authorMapper_example", // String | 
  'name': "name_example" // String | 
};
apiInstance.createAuthorIfNotExistsForUsingPOST(opts, (error, data, response) => {
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
 **authorMapper** | **String**|  | [optional] 
 **name** | **String**|  | [optional] 

### Return type

[**CreateAuthorUsingGET200Response**](CreateAuthorUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## createAuthorUsingGET

> CreateAuthorUsingGET200Response createAuthorUsingGET(opts)

creates a new author

### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.AuthorApi();
let opts = {
  'name': "name_example" // String | 
};
apiInstance.createAuthorUsingGET(opts, (error, data, response) => {
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
 **name** | **String**|  | [optional] 

### Return type

[**CreateAuthorUsingGET200Response**](CreateAuthorUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## createAuthorUsingPOST

> CreateAuthorUsingGET200Response createAuthorUsingPOST(opts)

creates a new author

### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.AuthorApi();
let opts = {
  'name': "name_example" // String | 
};
apiInstance.createAuthorUsingPOST(opts, (error, data, response) => {
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
 **name** | **String**|  | [optional] 

### Return type

[**CreateAuthorUsingGET200Response**](CreateAuthorUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAuthorNameUsingGET

> GetAuthorNameUsingGET200Response getAuthorNameUsingGET(opts)

Returns the Author Name of the author

### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.AuthorApi();
let opts = {
  'authorID': "authorID_example" // String | 
};
apiInstance.getAuthorNameUsingGET(opts, (error, data, response) => {
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
 **authorID** | **String**|  | [optional] 

### Return type

[**GetAuthorNameUsingGET200Response**](GetAuthorNameUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAuthorNameUsingPOST

> GetAuthorNameUsingGET200Response getAuthorNameUsingPOST(opts)

Returns the Author Name of the author

### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.AuthorApi();
let opts = {
  'authorID': "authorID_example" // String | 
};
apiInstance.getAuthorNameUsingPOST(opts, (error, data, response) => {
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
 **authorID** | **String**|  | [optional] 

### Return type

[**GetAuthorNameUsingGET200Response**](GetAuthorNameUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listPadsOfAuthorUsingGET

> ListAllPadsUsingGET200Response listPadsOfAuthorUsingGET(opts)

returns an array of all pads this author contributed to

### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.AuthorApi();
let opts = {
  'authorID': "authorID_example" // String | 
};
apiInstance.listPadsOfAuthorUsingGET(opts, (error, data, response) => {
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
 **authorID** | **String**|  | [optional] 

### Return type

[**ListAllPadsUsingGET200Response**](ListAllPadsUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listPadsOfAuthorUsingPOST

> ListAllPadsUsingGET200Response listPadsOfAuthorUsingPOST(opts)

returns an array of all pads this author contributed to

### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.AuthorApi();
let opts = {
  'authorID': "authorID_example" // String | 
};
apiInstance.listPadsOfAuthorUsingPOST(opts, (error, data, response) => {
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
 **authorID** | **String**|  | [optional] 

### Return type

[**ListAllPadsUsingGET200Response**](ListAllPadsUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSessionsOfAuthorUsingGET

> ListSessionsOfAuthorUsingGET200Response listSessionsOfAuthorUsingGET(opts)

returns all sessions of an author

### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.AuthorApi();
let opts = {
  'authorID': "authorID_example" // String | 
};
apiInstance.listSessionsOfAuthorUsingGET(opts, (error, data, response) => {
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
 **authorID** | **String**|  | [optional] 

### Return type

[**ListSessionsOfAuthorUsingGET200Response**](ListSessionsOfAuthorUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSessionsOfAuthorUsingPOST

> ListSessionsOfAuthorUsingGET200Response listSessionsOfAuthorUsingPOST(opts)

returns all sessions of an author

### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.AuthorApi();
let opts = {
  'authorID': "authorID_example" // String | 
};
apiInstance.listSessionsOfAuthorUsingPOST(opts, (error, data, response) => {
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
 **authorID** | **String**|  | [optional] 

### Return type

[**ListSessionsOfAuthorUsingGET200Response**](ListSessionsOfAuthorUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

