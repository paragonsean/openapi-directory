# SwaggerHubRegistryApi.APIsApi

All URIs are relative to *https://api.swaggerhub.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addApiCommentReplyV2**](APIsApi.md#addApiCommentReplyV2) | **POST** /apis/{owner}/{api}/{version}/comments/{comment}/replies | Reply to a comment
[**addApiCommentV2**](APIsApi.md#addApiCommentV2) | **POST** /apis/{owner}/{api}/{version}/comments | Add a new comment
[**cloneApi**](APIsApi.md#cloneApi) | **POST** /apis/{owner}/{api}/{version}/clone | Create a new API version
[**deleteApi**](APIsApi.md#deleteApi) | **DELETE** /apis/{owner}/{api} | Delete an API
[**deleteApiCommentReplyV2**](APIsApi.md#deleteApiCommentReplyV2) | **DELETE** /apis/{owner}/{api}/{version}/comments/{comment}/replies/{reply} | Delete a comment reply
[**deleteApiCommentV2**](APIsApi.md#deleteApiCommentV2) | **DELETE** /apis/{owner}/{api}/{version}/comments/{comment} | Delete a comment
[**deleteApiVersion**](APIsApi.md#deleteApiVersion) | **DELETE** /apis/{owner}/{api}/{version} | Delete an API version
[**forkApi**](APIsApi.md#forkApi) | **POST** /apis/{owner}/{api}/{version}/fork | Fork an API
[**getApiCommentsV2**](APIsApi.md#getApiCommentsV2) | **GET** /apis/{owner}/{api}/{version}/comments | Get comments for the specified API version
[**getApiDefaultVersion**](APIsApi.md#getApiDefaultVersion) | **GET** /apis/{owner}/{api}/settings/default | Get the default version of an API
[**getApiVersions**](APIsApi.md#getApiVersions) | **GET** /apis/{owner}/{api} | Get a list of API versions
[**getDefinition**](APIsApi.md#getDefinition) | **GET** /apis/{owner}/{api}/{version} | Get the OpenAPI definition of the specified API version
[**getJsonDefinition**](APIsApi.md#getJsonDefinition) | **GET** /apis/{owner}/{api}/{version}/swagger.json | Get the OpenAPI definition for the specified API version in JSON format
[**getLifecycleSettings**](APIsApi.md#getLifecycleSettings) | **GET** /apis/{owner}/{api}/{version}/settings/lifecycle | Get the published status for the specified API and version
[**getOwnerApis**](APIsApi.md#getOwnerApis) | **GET** /apis/{owner} | Get a list of APIs of the specified owner
[**getPrivateSettings**](APIsApi.md#getPrivateSettings) | **GET** /apis/{owner}/{api}/{version}/settings/private | Get the visibility (public or private) of API version
[**getStandardizationErrors**](APIsApi.md#getStandardizationErrors) | **GET** /apis/{owner}/{api}/{version}/standardization | Retrieve the standardization errors for a given API definition
[**getValidation**](APIsApi.md#getValidation) | **GET** /apis/{owner}/{api}/{version}/validation | Deprecated Get API Standardization errors and warnings
[**getYamlDefinition**](APIsApi.md#getYamlDefinition) | **GET** /apis/{owner}/{api}/{version}/swagger.yaml | Get the OpenAPI definition for the specified API version in YAML format
[**renameApi**](APIsApi.md#renameApi) | **POST** /apis/{owner}/{api}/rename | Rename an API
[**saveDefinition**](APIsApi.md#saveDefinition) | **POST** /apis/{owner}/{api} | Create or update an API
[**searchApis**](APIsApi.md#searchApis) | **GET** /apis | Search APIs
[**searchApisAndDomains**](APIsApi.md#searchApisAndDomains) | **GET** /specs | Retrieve a list of currently defined APIs, domains, and templates in APIs.json format
[**setApiCommentStatusV2**](APIsApi.md#setApiCommentStatusV2) | **PUT** /apis/{owner}/{api}/{version}/comments/{comment}/status/{status} | Resolve or reopen a comment
[**setApiDefaultVersion**](APIsApi.md#setApiDefaultVersion) | **PUT** /apis/{owner}/{api}/settings/default | Set the default API version
[**setLifecycleSettings**](APIsApi.md#setLifecycleSettings) | **PUT** /apis/{owner}/{api}/{version}/settings/lifecycle | Publish or unpublish an API version
[**setPrivateSettings**](APIsApi.md#setPrivateSettings) | **PUT** /apis/{owner}/{api}/{version}/settings/private | Set the visibility (public or private) of an API version
[**updateApiCommentReplyV2**](APIsApi.md#updateApiCommentReplyV2) | **PATCH** /apis/{owner}/{api}/{version}/comments/{comment}/replies/{reply} | Update a comment reply
[**updateApiCommentV2**](APIsApi.md#updateApiCommentV2) | **PATCH** /apis/{owner}/{api}/{version}/comments/{comment} | Update a comment
[**updateApiCommentsV2**](APIsApi.md#updateApiCommentsV2) | **POST** /apis/{owner}/{api}/{version}/comments/batch | Bulk update comments



## addApiCommentReplyV2

> [Comment] addApiCommentReplyV2(owner, api, version, comment, body)

Reply to a comment

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.APIsApi();
let owner = "owner_example"; // String | API owner (organization or user, case-sensitive)
let api = "api_example"; // String | API name (case-sensitive)
let version = "version_example"; // String | Version identifier
let comment = "comment_example"; // String | Comment identifier
let body = new SwaggerHubRegistryApi.NewReply(); // NewReply | 
apiInstance.addApiCommentReplyV2(owner, api, version, comment, body, (error, data, response) => {
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
 **owner** | **String**| API owner (organization or user, case-sensitive) | 
 **api** | **String**| API name (case-sensitive) | 
 **version** | **String**| Version identifier | 
 **comment** | **String**| Comment identifier | 
 **body** | [**NewReply**](NewReply.md)|  | 

### Return type

[**[Comment]**](Comment.md)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## addApiCommentV2

> ClosableComment addApiCommentV2(owner, api, version, body)

Add a new comment

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.APIsApi();
let owner = "owner_example"; // String | API owner (organization or user, case-sensitive)
let api = "api_example"; // String | API name (case-sensitive)
let version = "version_example"; // String | Version identifier
let body = new SwaggerHubRegistryApi.NewComment(); // NewComment | 
apiInstance.addApiCommentV2(owner, api, version, body, (error, data, response) => {
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
 **owner** | **String**| API owner (organization or user, case-sensitive) | 
 **api** | **String**| API name (case-sensitive) | 
 **version** | **String**| Version identifier | 
 **body** | [**NewComment**](NewComment.md)|  | 

### Return type

[**ClosableComment**](ClosableComment.md)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cloneApi

> cloneApi(owner, api, version, newVersion)

Create a new API version

Use this operation to clone an existing API version as a new version. The new version will have the same YAML content but with updated &#x60;info.version&#x60;.  **Note:** Comments, integrations, and codegen options are not copied to the new version. The default version also remains unchanged.

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.APIsApi();
let owner = "owner_example"; // String | API owner (organization or user, case-sensitive)
let api = "api_example"; // String | API name (case-sensitive)
let version = "version_example"; // String | The version to clone (case-sensitive)
let newVersion = new SwaggerHubRegistryApi.NewVersion(); // NewVersion | An object that contains the new version number and other parameters. The version number must be in the format described in the [documentation](https://support.smartbear.com/swaggerhub/docs/apis/versioning.html#format).
apiInstance.cloneApi(owner, api, version, newVersion, (error, data, response) => {
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
 **owner** | **String**| API owner (organization or user, case-sensitive) | 
 **api** | **String**| API name (case-sensitive) | 
 **version** | **String**| The version to clone (case-sensitive) | 
 **newVersion** | [**NewVersion**](NewVersion.md)| An object that contains the new version number and other parameters. The version number must be in the format described in the [documentation](https://support.smartbear.com/swaggerhub/docs/apis/versioning.html#format). | 

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteApi

> deleteApi(owner, api)

Delete an API

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.APIsApi();
let owner = "owner_example"; // String | API owner (organization or user, case-sensitive)
let api = "api_example"; // String | API name (case-sensitive)
apiInstance.deleteApi(owner, api, (error, data, response) => {
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
 **owner** | **String**| API owner (organization or user, case-sensitive) | 
 **api** | **String**| API name (case-sensitive) | 

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteApiCommentReplyV2

> deleteApiCommentReplyV2(owner, api, version, comment, reply)

Delete a comment reply

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.APIsApi();
let owner = "owner_example"; // String | API owner (organization or user, case-sensitive)
let api = "api_example"; // String | API name (case-sensitive)
let version = "version_example"; // String | Version identifier
let comment = "comment_example"; // String | Comment identifier
let reply = "reply_example"; // String | Reply identifier
apiInstance.deleteApiCommentReplyV2(owner, api, version, comment, reply, (error, data, response) => {
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
 **owner** | **String**| API owner (organization or user, case-sensitive) | 
 **api** | **String**| API name (case-sensitive) | 
 **version** | **String**| Version identifier | 
 **comment** | **String**| Comment identifier | 
 **reply** | **String**| Reply identifier | 

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteApiCommentV2

> deleteApiCommentV2(owner, api, version, comment)

Delete a comment

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.APIsApi();
let owner = "owner_example"; // String | API owner (organization or user, case-sensitive)
let api = "api_example"; // String | API name (case-sensitive)
let version = "version_example"; // String | Version identifier
let comment = "comment_example"; // String | Comment identifier
apiInstance.deleteApiCommentV2(owner, api, version, comment, (error, data, response) => {
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
 **owner** | **String**| API owner (organization or user, case-sensitive) | 
 **api** | **String**| API name (case-sensitive) | 
 **version** | **String**| Version identifier | 
 **comment** | **String**| Comment identifier | 

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteApiVersion

> deleteApiVersion(owner, api, version)

Delete an API version

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.APIsApi();
let owner = "owner_example"; // String | API owner (organization or user, case-sensitive)
let api = "api_example"; // String | API name (case-sensitive)
let version = "version_example"; // String | Version identifier
apiInstance.deleteApiVersion(owner, api, version, (error, data, response) => {
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
 **owner** | **String**| API owner (organization or user, case-sensitive) | 
 **api** | **String**| API name (case-sensitive) | 
 **version** | **String**| Version identifier | 

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## forkApi

> forkApi(owner, api, version, forkVersion)

Fork an API

Creates a [fork](https://support.smartbear.com/swaggerhub/docs/apis/forking-api.html) of the specified API definition and version. The fork can be created as a new API, or as a new version in another existing API.

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.APIsApi();
let owner = "owner_example"; // String | API owner (organization or user, case-sensitive)
let api = "api_example"; // String | API name (case-sensitive)
let version = "version_example"; // String | Version identifier
let forkVersion = new SwaggerHubRegistryApi.ForkVersion(); // ForkVersion | Fork parameters
apiInstance.forkApi(owner, api, version, forkVersion, (error, data, response) => {
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
 **owner** | **String**| API owner (organization or user, case-sensitive) | 
 **api** | **String**| API name (case-sensitive) | 
 **version** | **String**| Version identifier | 
 **forkVersion** | [**ForkVersion**](ForkVersion.md)| Fork parameters | 

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getApiCommentsV2

> [ClosableComment] getApiCommentsV2(owner, api, version)

Get comments for the specified API version

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.APIsApi();
let owner = "owner_example"; // String | API owner (organization or user, case-sensitive)
let api = "api_example"; // String | API name (case-sensitive)
let version = "version_example"; // String | Version identifier
apiInstance.getApiCommentsV2(owner, api, version, (error, data, response) => {
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
 **owner** | **String**| API owner (organization or user, case-sensitive) | 
 **api** | **String**| API name (case-sensitive) | 
 **version** | **String**| Version identifier | 

### Return type

[**[ClosableComment]**](ClosableComment.md)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getApiDefaultVersion

> DefaultVersion getApiDefaultVersion(owner, api)

Get the default version of an API

This operation returns the version identifier, such as &#x60;1.0.0&#x60;. To get the definition itself, use &#x60;GET /apis/{owner}/{api}/{version}&#x60;.

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.APIsApi();
let owner = "owner_example"; // String | API owner (organization or user, case-sensitive)
let api = "api_example"; // String | API name (case-sensitive)
apiInstance.getApiDefaultVersion(owner, api, (error, data, response) => {
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
 **owner** | **String**| API owner (organization or user, case-sensitive) | 
 **api** | **String**| API name (case-sensitive) | 

### Return type

[**DefaultVersion**](DefaultVersion.md)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getApiVersions

> ApisJson getApiVersions(owner, api)

Get a list of API versions

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.APIsApi();
let owner = "owner_example"; // String | API owner (organization or user, case-sensitive)
let api = "api_example"; // String | API name (case-sensitive)
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
 **owner** | **String**| API owner (organization or user, case-sensitive) | 
 **api** | **String**| API name (case-sensitive) | 

### Return type

[**ApisJson**](ApisJson.md)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDefinition

> Object getDefinition(owner, api, version, opts)

Get the OpenAPI definition of the specified API version

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.APIsApi();
let owner = "owner_example"; // String | API owner (organization or user, case-sensitive)
let api = "api_example"; // String | API name (case-sensitive)
let version = "version_example"; // String | Version identifier
let opts = {
  'resolved': false, // Boolean | Set to true to get the resolved version of the API definition. The content of all external $refs will be included in the resulting file.
  'flatten': false // Boolean | If set to `true`, it creates models from inline schemas in OpenAPI definition. AsyncAPI definitions cannot be flattened.
};
apiInstance.getDefinition(owner, api, version, opts, (error, data, response) => {
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
 **owner** | **String**| API owner (organization or user, case-sensitive) | 
 **api** | **String**| API name (case-sensitive) | 
 **version** | **String**| Version identifier | 
 **resolved** | **Boolean**| Set to true to get the resolved version of the API definition. The content of all external $refs will be included in the resulting file. | [optional] [default to false]
 **flatten** | **Boolean**| If set to &#x60;true&#x60;, it creates models from inline schemas in OpenAPI definition. AsyncAPI definitions cannot be flattened. | [optional] [default to false]

### Return type

**Object**

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/yaml


## getJsonDefinition

> Object getJsonDefinition(owner, api, version, opts)

Get the OpenAPI definition for the specified API version in JSON format

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.APIsApi();
let owner = "owner_example"; // String | API owner (organization or user, case-sensitive)
let api = "api_example"; // String | API name (case-sensitive)
let version = "version_example"; // String | Version identifier
let opts = {
  'resolved': false, // Boolean | Set to true to get the resolved version of the API definition. The content of all external $refs will be included in the resulting file.
  'flatten': false // Boolean | If set to `true`, it creates models from inline schemas in OpenAPI definition. AsyncAPI definitions cannot be flattened.
};
apiInstance.getJsonDefinition(owner, api, version, opts, (error, data, response) => {
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
 **owner** | **String**| API owner (organization or user, case-sensitive) | 
 **api** | **String**| API name (case-sensitive) | 
 **version** | **String**| Version identifier | 
 **resolved** | **Boolean**| Set to true to get the resolved version of the API definition. The content of all external $refs will be included in the resulting file. | [optional] [default to false]
 **flatten** | **Boolean**| If set to &#x60;true&#x60;, it creates models from inline schemas in OpenAPI definition. AsyncAPI definitions cannot be flattened. | [optional] [default to false]

### Return type

**Object**

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLifecycleSettings

> LifecycleSettings getLifecycleSettings(owner, api, version)

Get the published status for the specified API and version

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.APIsApi();
let owner = "owner_example"; // String | API owner (organization or user, case-sensitive)
let api = "api_example"; // String | API name (case-sensitive)
let version = "version_example"; // String | Version identifier
apiInstance.getLifecycleSettings(owner, api, version, (error, data, response) => {
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
 **owner** | **String**| API owner (organization or user, case-sensitive) | 
 **api** | **String**| API name (case-sensitive) | 
 **version** | **String**| Version identifier | 

### Return type

[**LifecycleSettings**](LifecycleSettings.md)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOwnerApis

> ApisJson getOwnerApis(owner, opts)

Get a list of APIs of the specified owner

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.APIsApi();
let owner = "owner_example"; // String | API owner (organization or user, case-sensitive)
let opts = {
  'page': 0, // Number | Page to return
  'limit': 10, // Number | Number of results per page (1 .. 100)
  'sort': "'NAME'", // String | Sort criteria of result set: * NAME * UPDATED * CREATED * OWNER * BEST_MATCH - by relevance * TITLE - by `info.title` 
  'order': "'ASC'" // String | Sort order
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
 **owner** | **String**| API owner (organization or user, case-sensitive) | 
 **page** | **Number**| Page to return | [optional] [default to 0]
 **limit** | **Number**| Number of results per page (1 .. 100) | [optional] [default to 10]
 **sort** | **String**| Sort criteria of result set: * NAME * UPDATED * CREATED * OWNER * BEST_MATCH - by relevance * TITLE - by &#x60;info.title&#x60;  | [optional] [default to &#39;NAME&#39;]
 **order** | **String**| Sort order | [optional] [default to &#39;ASC&#39;]

### Return type

[**ApisJson**](ApisJson.md)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPrivateSettings

> VisibilitySettings getPrivateSettings(owner, api, version)

Get the visibility (public or private) of API version

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.APIsApi();
let owner = "owner_example"; // String | API owner (organization or user, case-sensitive)
let api = "api_example"; // String | API name (case-sensitive)
let version = "version_example"; // String | Version identifier
apiInstance.getPrivateSettings(owner, api, version, (error, data, response) => {
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
 **owner** | **String**| API owner (organization or user, case-sensitive) | 
 **api** | **String**| API name (case-sensitive) | 
 **version** | **String**| Version identifier | 

### Return type

[**VisibilitySettings**](VisibilitySettings.md)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getStandardizationErrors

> StandardizationResult getStandardizationErrors(owner, api, version)

Retrieve the standardization errors for a given API definition

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.APIsApi();
let owner = "owner_example"; // String | API owner (organization or user, case-sensitive)
let api = "api_example"; // String | 
let version = "version_example"; // String | Version identifier
apiInstance.getStandardizationErrors(owner, api, version, (error, data, response) => {
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
 **owner** | **String**| API owner (organization or user, case-sensitive) | 
 **api** | **String**|  | 
 **version** | **String**| Version identifier | 

### Return type

[**StandardizationResult**](StandardizationResult.md)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getValidation

> ValidationResult getValidation(owner, api, version)

Deprecated Get API Standardization errors and warnings

**Note:** This endpoint is deprecated. Use the following new endpoint instead: GET /apis/{owner}/{api}/{version}/standardization   If your organization has [API standardization](https://support.smartbear.com/swaggerhub/docs/organizations/api-standardization.html) configured, you can use this operation to validate a specific API version and get a list of errors or warnings with line numbers.  This operation checks for standardization errors only and does not return OpenAPI syntax errors (such as misspelled keywords) or YAML syntax errors.

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.APIsApi();
let owner = "owner_example"; // String | Organization name (case-sensitive)
let api = "api_example"; // String | API name (case-sensitive)
let version = "version_example"; // String | Version identifier
apiInstance.getValidation(owner, api, version, (error, data, response) => {
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
 **owner** | **String**| Organization name (case-sensitive) | 
 **api** | **String**| API name (case-sensitive) | 
 **version** | **String**| Version identifier | 

### Return type

[**ValidationResult**](ValidationResult.md)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getYamlDefinition

> Object getYamlDefinition(owner, api, version, opts)

Get the OpenAPI definition for the specified API version in YAML format

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.APIsApi();
let owner = "owner_example"; // String | API owner (organization or user, case-sensitive)
let api = "api_example"; // String | API name (case-sensitive)
let version = "version_example"; // String | Version identifier
let opts = {
  'resolved': false, // Boolean | Set to true to get the resolved version of the API definition. The content of all external $refs will be included in the resulting file.
  'flatten': false // Boolean | If set to `true`, it creates models from inline schemas in OpenAPI definition. AsyncAPI definitions cannot be flattened.
};
apiInstance.getYamlDefinition(owner, api, version, opts, (error, data, response) => {
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
 **owner** | **String**| API owner (organization or user, case-sensitive) | 
 **api** | **String**| API name (case-sensitive) | 
 **version** | **String**| Version identifier | 
 **resolved** | **Boolean**| Set to true to get the resolved version of the API definition. The content of all external $refs will be included in the resulting file. | [optional] [default to false]
 **flatten** | **Boolean**| If set to &#x60;true&#x60;, it creates models from inline schemas in OpenAPI definition. AsyncAPI definitions cannot be flattened. | [optional] [default to false]

### Return type

**Object**

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/yaml, application/json


## renameApi

> renameApi(owner, api, newName)

Rename an API

The new name must follow the [naming rules](https://support.smartbear.com/swaggerhub/docs/apis/creating-api.html).

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.APIsApi();
let owner = "owner_example"; // String | API owner (organization or user, case-sensitive)
let api = "api_example"; // String | API name (case-sensitive)
let newName = "newName_example"; // String | New name
apiInstance.renameApi(owner, api, newName, (error, data, response) => {
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
 **owner** | **String**| API owner (organization or user, case-sensitive) | 
 **api** | **String**| API name (case-sensitive) | 
 **newName** | **String**| New name | 

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## saveDefinition

> saveDefinition(owner, api, definition, opts)

Create or update an API

Use this operation to create a new API or update an existing API by uploading its OpenAPI definition in YAML or JSON format. The authenticating user must have permissions to create or update APIs in the specified &#x60;owner&#x60; account.  The API name and version must follow SwaggerHub naming rules, otherwise the request will be rejected. Refer to:    * [API name format](https://support.smartbear.com/swaggerhub/docs/apis/creating-api.html)  * [Version format](https://support.smartbear.com/swaggerhub/docs/apis/versioning.html#format)   When a new version of an existing API is created, it does not automatically become the default version. You can use &#x60;PUT /apis/{owner}/{api}/settings/default&#x60; to set the default version.  ### cURL example Line breaks are added for readability.      curl -X POST \&quot;https://api.swaggerhub.com/apis/OWNER/API_TO_CREATE_OR_UPDATE\&quot;          -H \&quot;Authorization: SWAGGERHUB_API_KEY\&quot;          -H \&quot;Content-Type: application/yaml\&quot;          --data-binary @C:\\work\\swagger.yaml  **Note:** Use &#x60;--data-binary&#x60; (not &#x60;-d&#x60;) when uploading YAML files using cURL, and remember to specify the correct &#x60;Content-Type&#x60; header.

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.APIsApi();
let owner = "owner_example"; // String | API owner name (organization or user name, case-sensitive)
let api = "api_example"; // String | API name (case-sensitive)
let definition = "definition_example"; // String | OpenAPI definition in the YAML or JSON format. The content must be syntactically valid YAML or JSON.
let opts = {
  'isPrivate': false, // Boolean | Whether to make the API private (`true`) or public (`false`)
  'version': "version_example", // String | API version to create or update. If omitted, the version is extracted from the `info.version` field of the provided OpenAPI definition.  Either the `version` parameter or the `info.version` value must be specified, otherwise the request will be rejected. If both are specified, the `version` parameter overrides the `info.version` value.  If this API version already exists, it will be updated with the new definition (unless that version has been published - in this case the update will be rejected).
  'force': true // Boolean | Force update
};
apiInstance.saveDefinition(owner, api, definition, opts, (error, data, response) => {
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
 **owner** | **String**| API owner name (organization or user name, case-sensitive) | 
 **api** | **String**| API name (case-sensitive) | 
 **definition** | **String**| OpenAPI definition in the YAML or JSON format. The content must be syntactically valid YAML or JSON. | 
 **isPrivate** | **Boolean**| Whether to make the API private (&#x60;true&#x60;) or public (&#x60;false&#x60;) | [optional] [default to false]
 **version** | **String**| API version to create or update. If omitted, the version is extracted from the &#x60;info.version&#x60; field of the provided OpenAPI definition.  Either the &#x60;version&#x60; parameter or the &#x60;info.version&#x60; value must be specified, otherwise the request will be rejected. If both are specified, the &#x60;version&#x60; parameter overrides the &#x60;info.version&#x60; value.  If this API version already exists, it will be updated with the new definition (unless that version has been published - in this case the update will be rejected). | [optional] 
 **force** | **Boolean**| Force update | [optional] 

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: application/json, application/yaml
- **Accept**: Not defined


## searchApis

> searchApis(opts)

Search APIs

This is a convenience alias for &#x60;GET /specs?specType&#x3D;API&#x60;.

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.APIsApi();
let opts = {
  'query': "query_example", // String | Free text query to match
  'state': "'ALL'", // String | Matches against published state of the spec: * UNPUBLISHED - spec is a draft, a work in progress * PUBLISHED - spec is a stable version ready for consuming from client applications * ANY - either PUBLISHED or UNPUBLISHED 
  'page': 0, // Number | Page to return
  'limit': 10, // Number | Number of results per page (1 .. 100)
  'sort': "'NAME'", // String | Sort criteria of result set: * NAME * UPDATED * CREATED * OWNER * BEST_MATCH - by relevance * TITLE - by `info.title` 
  'order': "'ASC'" // String | Sort order
};
apiInstance.searchApis(opts, (error, data, response) => {
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
 **query** | **String**| Free text query to match | [optional] 
 **state** | **String**| Matches against published state of the spec: * UNPUBLISHED - spec is a draft, a work in progress * PUBLISHED - spec is a stable version ready for consuming from client applications * ANY - either PUBLISHED or UNPUBLISHED  | [optional] [default to &#39;ALL&#39;]
 **page** | **Number**| Page to return | [optional] [default to 0]
 **limit** | **Number**| Number of results per page (1 .. 100) | [optional] [default to 10]
 **sort** | **String**| Sort criteria of result set: * NAME * UPDATED * CREATED * OWNER * BEST_MATCH - by relevance * TITLE - by &#x60;info.title&#x60;  | [optional] [default to &#39;NAME&#39;]
 **order** | **String**| Sort order | [optional] [default to &#39;ASC&#39;]

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## searchApisAndDomains

> ApisJson searchApisAndDomains(opts)

Retrieve a list of currently defined APIs, domains, and templates in APIs.json format

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.APIsApi();
let opts = {
  'specType': "'ANY'", // String | Type of definitions to search: * API - APIs only * DOMAIN - domains only * TEMPLATE - templates only * ANY - APIs, domains, and templates 
  'visibility': "'ANY'", // String | The visibility of a definition in SwaggerHub: * PUBLIC - can be viewed by anyone * PRIVATE - can only be viewed by you or your organization and those that you are collaborating with or have shared it with * ANY - either PUBLIC or PRIVATE 
  'state': "'ALL'", // String | Matches against published state of the spec: * UNPUBLISHED - spec is a draft, a work in progress * PUBLISHED - spec is a stable version ready for consuming from client applications * ANY - either PUBLISHED or UNPUBLISHED 
  'owner': "owner_example", // String | API or domain owner. Can be username or organization name. Case-sensitive.
  'query': "query_example", // String | Free text query to match
  'page': 0, // Number | Page to return
  'limit': 10, // Number | Number of results per page (1 .. 100)
  'sort': "'NAME'", // String | Sort criteria of result set: * NAME * UPDATED * CREATED * OWNER * BEST_MATCH - by relevance * TITLE - by `info.title` 
  'order': "'ASC'" // String | Sort order
};
apiInstance.searchApisAndDomains(opts, (error, data, response) => {
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
 **specType** | **String**| Type of definitions to search: * API - APIs only * DOMAIN - domains only * TEMPLATE - templates only * ANY - APIs, domains, and templates  | [optional] [default to &#39;ANY&#39;]
 **visibility** | **String**| The visibility of a definition in SwaggerHub: * PUBLIC - can be viewed by anyone * PRIVATE - can only be viewed by you or your organization and those that you are collaborating with or have shared it with * ANY - either PUBLIC or PRIVATE  | [optional] [default to &#39;ANY&#39;]
 **state** | **String**| Matches against published state of the spec: * UNPUBLISHED - spec is a draft, a work in progress * PUBLISHED - spec is a stable version ready for consuming from client applications * ANY - either PUBLISHED or UNPUBLISHED  | [optional] [default to &#39;ALL&#39;]
 **owner** | **String**| API or domain owner. Can be username or organization name. Case-sensitive. | [optional] 
 **query** | **String**| Free text query to match | [optional] 
 **page** | **Number**| Page to return | [optional] [default to 0]
 **limit** | **Number**| Number of results per page (1 .. 100) | [optional] [default to 10]
 **sort** | **String**| Sort criteria of result set: * NAME * UPDATED * CREATED * OWNER * BEST_MATCH - by relevance * TITLE - by &#x60;info.title&#x60;  | [optional] [default to &#39;NAME&#39;]
 **order** | **String**| Sort order | [optional] [default to &#39;ASC&#39;]

### Return type

[**ApisJson**](ApisJson.md)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setApiCommentStatusV2

> setApiCommentStatusV2(owner, api, version, comment, status)

Resolve or reopen a comment

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.APIsApi();
let owner = "owner_example"; // String | API owner (organization or user, case-sensitive)
let api = "api_example"; // String | API name (case-sensitive)
let version = "version_example"; // String | Version identifier
let comment = "comment_example"; // String | Comment identifier
let status = "status_example"; // String | Comment status
apiInstance.setApiCommentStatusV2(owner, api, version, comment, status, (error, data, response) => {
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
 **owner** | **String**| API owner (organization or user, case-sensitive) | 
 **api** | **String**| API name (case-sensitive) | 
 **version** | **String**| Version identifier | 
 **comment** | **String**| Comment identifier | 
 **status** | **String**| Comment status | 

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## setApiDefaultVersion

> setApiDefaultVersion(owner, api, defaultVersion)

Set the default API version

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.APIsApi();
let owner = "owner_example"; // String | API owner (organization or user, case-sensitive)
let api = "api_example"; // String | API name (case-sensitive)
let defaultVersion = new SwaggerHubRegistryApi.DefaultVersion(); // DefaultVersion | An object that specifies the default version for this API
apiInstance.setApiDefaultVersion(owner, api, defaultVersion, (error, data, response) => {
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
 **owner** | **String**| API owner (organization or user, case-sensitive) | 
 **api** | **String**| API name (case-sensitive) | 
 **defaultVersion** | [**DefaultVersion**](DefaultVersion.md)| An object that specifies the default version for this API | 

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## setLifecycleSettings

> setLifecycleSettings(owner, api, version, settings, opts)

Publish or unpublish an API version

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.APIsApi();
let owner = "owner_example"; // String | API owner (organization or user, case-sensitive)
let api = "api_example"; // String | API name (case-sensitive)
let version = "version_example"; // String | Version identifier
let settings = new SwaggerHubRegistryApi.LifecycleSettings(); // LifecycleSettings | An object that specifies the new `published` state: `true` means published, `false` - unpublished
let opts = {
  'force': false // Boolean | To publish an API that references _unpublished_ domains, this parameter must be `true`. Otherwise, the request will be rejected with status code 424.
};
apiInstance.setLifecycleSettings(owner, api, version, settings, opts, (error, data, response) => {
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
 **owner** | **String**| API owner (organization or user, case-sensitive) | 
 **api** | **String**| API name (case-sensitive) | 
 **version** | **String**| Version identifier | 
 **settings** | [**LifecycleSettings**](LifecycleSettings.md)| An object that specifies the new &#x60;published&#x60; state: &#x60;true&#x60; means published, &#x60;false&#x60; - unpublished | 
 **force** | **Boolean**| To publish an API that references _unpublished_ domains, this parameter must be &#x60;true&#x60;. Otherwise, the request will be rejected with status code 424. | [optional] [default to false]

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## setPrivateSettings

> setPrivateSettings(owner, api, version, settings)

Set the visibility (public or private) of an API version

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.APIsApi();
let owner = "owner_example"; // String | API owner (organization or user, case-sensitive)
let api = "api_example"; // String | API name (case-sensitive)
let version = "version_example"; // String | Version identifier
let settings = new SwaggerHubRegistryApi.VisibilitySettings(); // VisibilitySettings | An object that specifies the new visibility level: `true` means private, `false` - public
apiInstance.setPrivateSettings(owner, api, version, settings, (error, data, response) => {
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
 **owner** | **String**| API owner (organization or user, case-sensitive) | 
 **api** | **String**| API name (case-sensitive) | 
 **version** | **String**| Version identifier | 
 **settings** | [**VisibilitySettings**](VisibilitySettings.md)| An object that specifies the new visibility level: &#x60;true&#x60; means private, &#x60;false&#x60; - public | 

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateApiCommentReplyV2

> Comment updateApiCommentReplyV2(owner, api, version, comment, reply, opts)

Update a comment reply

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.APIsApi();
let owner = "owner_example"; // String | API owner (organization or user, case-sensitive)
let api = "api_example"; // String | API name (case-sensitive)
let version = "version_example"; // String | Version identifier
let comment = "comment_example"; // String | Comment identifier
let reply = "reply_example"; // String | Reply identifier
let opts = {
  'body': new SwaggerHubRegistryApi.CommentPatch() // CommentPatch | 
};
apiInstance.updateApiCommentReplyV2(owner, api, version, comment, reply, opts, (error, data, response) => {
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
 **owner** | **String**| API owner (organization or user, case-sensitive) | 
 **api** | **String**| API name (case-sensitive) | 
 **version** | **String**| Version identifier | 
 **comment** | **String**| Comment identifier | 
 **reply** | **String**| Reply identifier | 
 **body** | [**CommentPatch**](CommentPatch.md)|  | [optional] 

### Return type

[**Comment**](Comment.md)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateApiCommentV2

> ClosableComment updateApiCommentV2(owner, api, version, comment, opts)

Update a comment

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.APIsApi();
let owner = "owner_example"; // String | API owner (organization or user, case-sensitive)
let api = "api_example"; // String | API name (case-sensitive)
let version = "version_example"; // String | Version identifier
let comment = "comment_example"; // String | Comment identifier
let opts = {
  'body': new SwaggerHubRegistryApi.ClosableCommentPatch() // ClosableCommentPatch | 
};
apiInstance.updateApiCommentV2(owner, api, version, comment, opts, (error, data, response) => {
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
 **owner** | **String**| API owner (organization or user, case-sensitive) | 
 **api** | **String**| API name (case-sensitive) | 
 **version** | **String**| Version identifier | 
 **comment** | **String**| Comment identifier | 
 **body** | [**ClosableCommentPatch**](ClosableCommentPatch.md)|  | [optional] 

### Return type

[**ClosableComment**](ClosableComment.md)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateApiCommentsV2

> updateApiCommentsV2(owner, api, version, body)

Bulk update comments

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.APIsApi();
let owner = "owner_example"; // String | API owner (organization or user, case-sensitive)
let api = "api_example"; // String | API name (case-sensitive)
let version = "version_example"; // String | Version identifier
let body = new SwaggerHubRegistryApi.CommentsBatch(); // CommentsBatch | 
apiInstance.updateApiCommentsV2(owner, api, version, body, (error, data, response) => {
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
 **owner** | **String**| API owner (organization or user, case-sensitive) | 
 **api** | **String**| API name (case-sensitive) | 
 **version** | **String**| Version identifier | 
 **body** | [**CommentsBatch**](CommentsBatch.md)|  | 

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

