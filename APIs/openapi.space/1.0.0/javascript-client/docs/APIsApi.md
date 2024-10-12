# OpenApiSpace.APIsApi

All URIs are relative to *https://openapi.space/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteApi**](APIsApi.md#deleteApi) | **DELETE** /apis/{owner}/{api} | Deletes the specified API
[**deleteApiVersion**](APIsApi.md#deleteApiVersion) | **DELETE** /apis/{owner}/{api}/{version} | Deletes a particular version of the specified API
[**getApiVersions**](APIsApi.md#getApiVersions) | **GET** /apis/{owner}/{api} | Retrieves an API meta listing for all API versions for this owner and API
[**getJsonDefinition**](APIsApi.md#getJsonDefinition) | **GET** /apis/{owner}/{api}/{version}/swagger.json | Retrieves the Swagger definition for the specified API and version in JSON format
[**getOwnerApis**](APIsApi.md#getOwnerApis) | **GET** /apis/{owner} | Retrieves an API meta listing of all APIs defined for this owner
[**getYamlDefinition**](APIsApi.md#getYamlDefinition) | **GET** /apis/{owner}/{api}/{version}/swagger.yaml | Retrieves the Swagger definition for the specified API and version in YAML format
[**publishApiVersion**](APIsApi.md#publishApiVersion) | **POST** /apis/{owner}/{api}/{version} | Publish a particular version of the specified API
[**saveDefinition**](APIsApi.md#saveDefinition) | **POST** /apis/{owner}/{api} | Saves the provided Swagger definition
[**searchApis**](APIsApi.md#searchApis) | **GET** /apis | Retrieves a list of currently defined APIs in API meta list format.



## deleteApi

> [APIMeta] deleteApi(owner, api)

Deletes the specified API

### Example

```javascript
import OpenApiSpace from 'open_api_space';
let defaultClient = OpenApiSpace.ApiClient.instance;
// Configure API key authorization: AuthToken
let AuthToken = defaultClient.authentications['AuthToken'];
AuthToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//AuthToken.apiKeyPrefix = 'Token';

let apiInstance = new OpenApiSpace.APIsApi();
let owner = "owner_example"; // String | API owner identifier
let api = "api_example"; // String | API identifier
apiInstance.deleteApi(owner, api, (error, data, response) => {
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
 **owner** | **String**| API owner identifier | 
 **api** | **String**| API identifier | 

### Return type

[**[APIMeta]**](APIMeta.md)

### Authorization

[AuthToken](../README.md#AuthToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteApiVersion

> APIMeta deleteApiVersion(owner, api, version)

Deletes a particular version of the specified API

### Example

```javascript
import OpenApiSpace from 'open_api_space';
let defaultClient = OpenApiSpace.ApiClient.instance;
// Configure API key authorization: AuthToken
let AuthToken = defaultClient.authentications['AuthToken'];
AuthToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//AuthToken.apiKeyPrefix = 'Token';

let apiInstance = new OpenApiSpace.APIsApi();
let owner = "owner_example"; // String | API owner identifier
let api = "api_example"; // String | API identifier
let version = "version_example"; // String | version identifier
apiInstance.deleteApiVersion(owner, api, version, (error, data, response) => {
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
 **owner** | **String**| API owner identifier | 
 **api** | **String**| API identifier | 
 **version** | **String**| version identifier | 

### Return type

[**APIMeta**](APIMeta.md)

### Authorization

[AuthToken](../README.md#AuthToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getApiVersions

> [APIMeta] getApiVersions(owner, api)

Retrieves an API meta listing for all API versions for this owner and API

### Example

```javascript
import OpenApiSpace from 'open_api_space';
let defaultClient = OpenApiSpace.ApiClient.instance;
// Configure API key authorization: AuthToken
let AuthToken = defaultClient.authentications['AuthToken'];
AuthToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//AuthToken.apiKeyPrefix = 'Token';

let apiInstance = new OpenApiSpace.APIsApi();
let owner = "owner_example"; // String | API owner identifier
let api = "api_example"; // String | API identifier
apiInstance.getApiVersions(owner, api, (error, data, response) => {
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
 **owner** | **String**| API owner identifier | 
 **api** | **String**| API identifier | 

### Return type

[**[APIMeta]**](APIMeta.md)

### Authorization

[AuthToken](../README.md#AuthToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getJsonDefinition

> Object getJsonDefinition(owner, api, version)

Retrieves the Swagger definition for the specified API and version in JSON format

### Example

```javascript
import OpenApiSpace from 'open_api_space';
let defaultClient = OpenApiSpace.ApiClient.instance;
// Configure API key authorization: AuthToken
let AuthToken = defaultClient.authentications['AuthToken'];
AuthToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//AuthToken.apiKeyPrefix = 'Token';

let apiInstance = new OpenApiSpace.APIsApi();
let owner = "owner_example"; // String | API owner identifier
let api = "api_example"; // String | API identifier
let version = "version_example"; // String | version identifier
apiInstance.getJsonDefinition(owner, api, version, (error, data, response) => {
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
 **owner** | **String**| API owner identifier | 
 **api** | **String**| API identifier | 
 **version** | **String**| version identifier | 

### Return type

**Object**

### Authorization

[AuthToken](../README.md#AuthToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOwnerApis

> [APIMeta] getOwnerApis(owner, opts)

Retrieves an API meta listing of all APIs defined for this owner

### Example

```javascript
import OpenApiSpace from 'open_api_space';
let defaultClient = OpenApiSpace.ApiClient.instance;
// Configure API key authorization: AuthToken
let AuthToken = defaultClient.authentications['AuthToken'];
AuthToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//AuthToken.apiKeyPrefix = 'Token';

let apiInstance = new OpenApiSpace.APIsApi();
let owner = "owner_example"; // String | API owner identifier
let opts = {
  'sort': "'NAME'", // String | sort criteria or result set * NAME - * UPATED * CREATED * OWNER 
  'order': "'ASC'" // String | sort order
};
apiInstance.getOwnerApis(owner, opts, (error, data, response) => {
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
 **owner** | **String**| API owner identifier | 
 **sort** | **String**| sort criteria or result set * NAME - * UPATED * CREATED * OWNER  | [optional] [default to &#39;NAME&#39;]
 **order** | **String**| sort order | [optional] [default to &#39;ASC&#39;]

### Return type

[**[APIMeta]**](APIMeta.md)

### Authorization

[AuthToken](../README.md#AuthToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getYamlDefinition

> Object getYamlDefinition(owner, api, version)

Retrieves the Swagger definition for the specified API and version in YAML format

### Example

```javascript
import OpenApiSpace from 'open_api_space';
let defaultClient = OpenApiSpace.ApiClient.instance;
// Configure API key authorization: AuthToken
let AuthToken = defaultClient.authentications['AuthToken'];
AuthToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//AuthToken.apiKeyPrefix = 'Token';

let apiInstance = new OpenApiSpace.APIsApi();
let owner = "owner_example"; // String | API owner identifier
let api = "api_example"; // String | API identifier
let version = "version_example"; // String | version identifier
apiInstance.getYamlDefinition(owner, api, version, (error, data, response) => {
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
 **owner** | **String**| API owner identifier | 
 **api** | **String**| API identifier | 
 **version** | **String**| version identifier | 

### Return type

**Object**

### Authorization

[AuthToken](../README.md#AuthToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/vnd.yaml


## publishApiVersion

> publishApiVersion(owner, api, version)

Publish a particular version of the specified API

### Example

```javascript
import OpenApiSpace from 'open_api_space';

let apiInstance = new OpenApiSpace.APIsApi();
let owner = "owner_example"; // String | API owner identifier
let api = "api_example"; // String | API identifier
let version = "version_example"; // String | version identifier
apiInstance.publishApiVersion(owner, api, version, (error, data, response) => {
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
 **owner** | **String**| API owner identifier | 
 **api** | **String**| API identifier | 
 **version** | **String**| version identifier | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## saveDefinition

> APIMeta saveDefinition(owner, api, definition, opts)

Saves the provided Swagger definition

Saves the provided Swagger definition; the owner must match the token owner. The version will be extracted from the Swagger definitions itself.

### Example

```javascript
import OpenApiSpace from 'open_api_space';
let defaultClient = OpenApiSpace.ApiClient.instance;
// Configure API key authorization: AuthToken
let AuthToken = defaultClient.authentications['AuthToken'];
AuthToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//AuthToken.apiKeyPrefix = 'Token';

let apiInstance = new OpenApiSpace.APIsApi();
let owner = "owner_example"; // String | API owner identifier
let api = "api_example"; // String | API identifier
let definition = {key: null}; // Object | the Swagger definition of this API
let opts = {
  '_private': false, // Boolean | Defines whether the API has to be private
  'force': false // Boolean | force update
};
apiInstance.saveDefinition(owner, api, definition, opts, (error, data, response) => {
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
 **owner** | **String**| API owner identifier | 
 **api** | **String**| API identifier | 
 **definition** | **Object**| the Swagger definition of this API | 
 **_private** | **Boolean**| Defines whether the API has to be private | [optional] [default to false]
 **force** | **Boolean**| force update | [optional] [default to false]

### Return type

[**APIMeta**](APIMeta.md)

### Authorization

[AuthToken](../README.md#AuthToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## searchApis

> [APIMeta] searchApis(opts)

Retrieves a list of currently defined APIs in API meta list format.

### Example

```javascript
import OpenApiSpace from 'open_api_space';
let defaultClient = OpenApiSpace.ApiClient.instance;
// Configure API key authorization: AuthToken
let AuthToken = defaultClient.authentications['AuthToken'];
AuthToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//AuthToken.apiKeyPrefix = 'Token';

let apiInstance = new OpenApiSpace.APIsApi();
let opts = {
  'query': "query_example", // String | free text query to match
  'limit': 10, // Number | the maximum number of APIs to return
  'offset': 0, // Number | the offset where to start from when fetching a limited number of APIs
  'sort': "'NAME'", // String | sort criteria or result set * NAME - * UPATED * CREATED * OWNER 
  'order': "'ASC'" // String | sort order
};
apiInstance.searchApis(opts, (error, data, response) => {
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
 **query** | **String**| free text query to match | [optional] 
 **limit** | **Number**| the maximum number of APIs to return | [optional] [default to 10]
 **offset** | **Number**| the offset where to start from when fetching a limited number of APIs | [optional] [default to 0]
 **sort** | **String**| sort criteria or result set * NAME - * UPATED * CREATED * OWNER  | [optional] [default to &#39;NAME&#39;]
 **order** | **String**| sort order | [optional] [default to &#39;ASC&#39;]

### Return type

[**[APIMeta]**](APIMeta.md)

### Authorization

[AuthToken](../README.md#AuthToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

