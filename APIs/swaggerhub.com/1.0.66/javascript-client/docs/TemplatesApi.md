# SwaggerHubRegistryApi.TemplatesApi

All URIs are relative to *https://api.swaggerhub.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteTemplate**](TemplatesApi.md#deleteTemplate) | **DELETE** /templates/{owner}/{templateId} | Delete a template
[**deleteTemplateVersion**](TemplatesApi.md#deleteTemplateVersion) | **DELETE** /templates/{owner}/{templateId}/{version} | Delete a particular version of a template
[**forkTemplate**](TemplatesApi.md#forkTemplate) | **POST** /templates/{owner}/{templateId}/{version}/fork | Create a fork for a template
[**getTemplateComments**](TemplatesApi.md#getTemplateComments) | **GET** /templates/{owner}/{templateId}/{version}/comments | Return the list of comments for a template
[**getTemplateDefinition**](TemplatesApi.md#getTemplateDefinition) | **GET** /templates/{owner}/{templateId}/{version} | Retrieve a template definition
[**getTemplateLifecycleSettings**](TemplatesApi.md#getTemplateLifecycleSettings) | **GET** /templates/{owner}/{templateId}/{version}/settings/lifecycle | Retrieve lifecycle settings for a template
[**getTemplatePrivateSettings**](TemplatesApi.md#getTemplatePrivateSettings) | **GET** /templates/{owner}/{templateId}/{version}/settings/private | Retrieve visibility settings for a template
[**getTemplateVersions**](TemplatesApi.md#getTemplateVersions) | **GET** /templates/{owner}/{templateId} | Retrieve an APIs.json listing for all template versions for an owner and template
[**getTemplates**](TemplatesApi.md#getTemplates) | **GET** /templates | Retrieve a list of templates for an owner
[**renameTemplate**](TemplatesApi.md#renameTemplate) | **POST** /templates/{owner}/{templateId}/rename | Rename a template
[**saveTemplateDefinition**](TemplatesApi.md#saveTemplateDefinition) | **POST** /templates/{owner}/{templateId} | Create or update a template
[**searchApisAndDomains_1**](TemplatesApi.md#searchApisAndDomains_1) | **GET** /specs | Retrieve a list of currently defined APIs, domains, and templates in APIs.json format
[**setTemplateLifecycleSettings**](TemplatesApi.md#setTemplateLifecycleSettings) | **PUT** /templates/{owner}/{templateId}/{version}/settings/lifecycle | Update lifecycle settings for a template
[**setTemplatePrivateSettings**](TemplatesApi.md#setTemplatePrivateSettings) | **PUT** /templates/{owner}/{templateId}/{version}/settings/private | Update visibility settings for a template
[**updateTemplateComments**](TemplatesApi.md#updateTemplateComments) | **POST** /templates/{owner}/{templateId}/{version}/comments/batch | Update the list of comments for a template



## deleteTemplate

> deleteTemplate(owner, templateId)

Delete a template

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.TemplatesApi();
let owner = "owner_example"; // String | API, domain, or template owner identifier (case-sensitive)
let templateId = "templateId_example"; // String | Template identifier
apiInstance.deleteTemplate(owner, templateId, (error, data, response) => {
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
 **owner** | **String**| API, domain, or template owner identifier (case-sensitive) | 
 **templateId** | **String**| Template identifier | 

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteTemplateVersion

> deleteTemplateVersion(owner, templateId, version)

Delete a particular version of a template

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.TemplatesApi();
let owner = "owner_example"; // String | API, domain, or template owner identifier (case-sensitive)
let templateId = "templateId_example"; // String | Template identifier
let version = "version_example"; // String | Version identifier
apiInstance.deleteTemplateVersion(owner, templateId, version, (error, data, response) => {
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
 **owner** | **String**| API, domain, or template owner identifier (case-sensitive) | 
 **templateId** | **String**| Template identifier | 
 **version** | **String**| Version identifier | 

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## forkTemplate

> forkTemplate(owner, templateId, version, body)

Create a fork for a template

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.TemplatesApi();
let owner = "owner_example"; // String | API, domain, or template owner identifier (case-sensitive)
let templateId = "templateId_example"; // String | Template identifier
let version = "version_example"; // String | Version identifier
let body = new SwaggerHubRegistryApi.ForkVersion(); // ForkVersion | Fork version information
apiInstance.forkTemplate(owner, templateId, version, body, (error, data, response) => {
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
 **owner** | **String**| API, domain, or template owner identifier (case-sensitive) | 
 **templateId** | **String**| Template identifier | 
 **version** | **String**| Version identifier | 
 **body** | [**ForkVersion**](ForkVersion.md)| Fork version information | 

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getTemplateComments

> [ClosableComment] getTemplateComments(owner, templateId, version)

Return the list of comments for a template

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.TemplatesApi();
let owner = "owner_example"; // String | API, domain, or template owner identifier (case-sensitive)
let templateId = "templateId_example"; // String | Template identifier
let version = "version_example"; // String | Version identifier
apiInstance.getTemplateComments(owner, templateId, version, (error, data, response) => {
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
 **owner** | **String**| API, domain, or template owner identifier (case-sensitive) | 
 **templateId** | **String**| Template identifier | 
 **version** | **String**| Version identifier | 

### Return type

[**[ClosableComment]**](ClosableComment.md)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTemplateDefinition

> Object getTemplateDefinition(owner, templateId, version, opts)

Retrieve a template definition

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.TemplatesApi();
let owner = "owner_example"; // String | API, domain, or template owner identifier (case-sensitive)
let templateId = "templateId_example"; // String | Template identifier
let version = "version_example"; // String | Version identifier
let opts = {
  'flatten': false // Boolean | If set to `true`, it creates models from inline schemas in OpenAPI definition. AsyncAPI definitions cannot be flattened.
};
apiInstance.getTemplateDefinition(owner, templateId, version, opts, (error, data, response) => {
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
 **owner** | **String**| API, domain, or template owner identifier (case-sensitive) | 
 **templateId** | **String**| Template identifier | 
 **version** | **String**| Version identifier | 
 **flatten** | **Boolean**| If set to &#x60;true&#x60;, it creates models from inline schemas in OpenAPI definition. AsyncAPI definitions cannot be flattened. | [optional] [default to false]

### Return type

**Object**

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTemplateLifecycleSettings

> LifecycleSettings getTemplateLifecycleSettings(owner, templateId, version)

Retrieve lifecycle settings for a template

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.TemplatesApi();
let owner = "owner_example"; // String | API, domain, or template owner identifier (case-sensitive)
let templateId = "templateId_example"; // String | Template identifier
let version = "version_example"; // String | Version identifier
apiInstance.getTemplateLifecycleSettings(owner, templateId, version, (error, data, response) => {
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
 **owner** | **String**| API, domain, or template owner identifier (case-sensitive) | 
 **templateId** | **String**| Template identifier | 
 **version** | **String**| Version identifier | 

### Return type

[**LifecycleSettings**](LifecycleSettings.md)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTemplatePrivateSettings

> VisibilitySettings getTemplatePrivateSettings(owner, templateId, version)

Retrieve visibility settings for a template

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.TemplatesApi();
let owner = "owner_example"; // String | API, domain, or template owner identifier (case-sensitive)
let templateId = "templateId_example"; // String | Template identifier
let version = "version_example"; // String | Version identifier
apiInstance.getTemplatePrivateSettings(owner, templateId, version, (error, data, response) => {
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
 **owner** | **String**| API, domain, or template owner identifier (case-sensitive) | 
 **templateId** | **String**| Template identifier | 
 **version** | **String**| Version identifier | 

### Return type

[**VisibilitySettings**](VisibilitySettings.md)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTemplateVersions

> ApisJson getTemplateVersions(owner, templateId)

Retrieve an APIs.json listing for all template versions for an owner and template

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.TemplatesApi();
let owner = "owner_example"; // String | API, domain, or template owner identifier (case-sensitive)
let templateId = "templateId_example"; // String | Template identifier
apiInstance.getTemplateVersions(owner, templateId, (error, data, response) => {
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
 **owner** | **String**| API, domain, or template owner identifier (case-sensitive) | 
 **templateId** | **String**| Template identifier | 

### Return type

[**ApisJson**](ApisJson.md)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTemplates

> TemplateWrapper getTemplates(opts)

Retrieve a list of templates for an owner

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.TemplatesApi();
let opts = {
  'owner': "owner_example" // String | Owner name
};
apiInstance.getTemplates(opts, (error, data, response) => {
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
 **owner** | **String**| Owner name | [optional] 

### Return type

[**TemplateWrapper**](TemplateWrapper.md)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## renameTemplate

> renameTemplate(owner, templateId, newName)

Rename a template

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.TemplatesApi();
let owner = "owner_example"; // String | API, domain, or template owner identifier (case-sensitive)
let templateId = "templateId_example"; // String | Template identifier
let newName = "newName_example"; // String | New name
apiInstance.renameTemplate(owner, templateId, newName, (error, data, response) => {
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
 **owner** | **String**| API, domain, or template owner identifier (case-sensitive) | 
 **templateId** | **String**| Template identifier | 
 **newName** | **String**| New name | 

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## saveTemplateDefinition

> saveTemplateDefinition(owner, templateId, body, opts)

Create or update a template

Saves the provided template definition; the owner must match the token owner. The version will be extracted from the template definitions itself.

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.TemplatesApi();
let owner = "owner_example"; // String | API, domain, or template owner identifier (case-sensitive)
let templateId = "templateId_example"; // String | Template identifier
let body = "body_example"; // String | The template definition
let opts = {
  'isPrivate': false, // Boolean | Defines whether the API or template has to be private
  'version': "version_example", // String | Template version to create or update. If omitted, the version will be taken from the `info.version` field in the definition.
  'force': true, // Boolean | Force update
  'projectName': "projectName_example" // String | The project to add the API, domain, or template to
};
apiInstance.saveTemplateDefinition(owner, templateId, body, opts, (error, data, response) => {
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
 **owner** | **String**| API, domain, or template owner identifier (case-sensitive) | 
 **templateId** | **String**| Template identifier | 
 **body** | **String**| The template definition | 
 **isPrivate** | **Boolean**| Defines whether the API or template has to be private | [optional] [default to false]
 **version** | **String**| Template version to create or update. If omitted, the version will be taken from the &#x60;info.version&#x60; field in the definition. | [optional] 
 **force** | **Boolean**| Force update | [optional] 
 **projectName** | **String**| The project to add the API, domain, or template to | [optional] 

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: application/json, application/yaml
- **Accept**: Not defined


## searchApisAndDomains_1

> ApisJson searchApisAndDomains_1(opts)

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

let apiInstance = new SwaggerHubRegistryApi.TemplatesApi();
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
apiInstance.searchApisAndDomains_1(opts, (error, data, response) => {
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


## setTemplateLifecycleSettings

> setTemplateLifecycleSettings(owner, templateId, version, body, opts)

Update lifecycle settings for a template

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.TemplatesApi();
let owner = "owner_example"; // String | API, domain, or template owner identifier (case-sensitive)
let templateId = "templateId_example"; // String | Template identifier
let version = "version_example"; // String | Version identifier
let body = new SwaggerHubRegistryApi.LifecycleSettings(); // LifecycleSettings | Fork version information
let opts = {
  'force': true // Boolean | Force update
};
apiInstance.setTemplateLifecycleSettings(owner, templateId, version, body, opts, (error, data, response) => {
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
 **owner** | **String**| API, domain, or template owner identifier (case-sensitive) | 
 **templateId** | **String**| Template identifier | 
 **version** | **String**| Version identifier | 
 **body** | [**LifecycleSettings**](LifecycleSettings.md)| Fork version information | 
 **force** | **Boolean**| Force update | [optional] 

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## setTemplatePrivateSettings

> setTemplatePrivateSettings(owner, templateId, version, body)

Update visibility settings for a template

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';

let apiInstance = new SwaggerHubRegistryApi.TemplatesApi();
let owner = "owner_example"; // String | API, domain, or template owner identifier (case-sensitive)
let templateId = "templateId_example"; // String | Template identifier
let version = "version_example"; // String | Version identifier
let body = new SwaggerHubRegistryApi.VisibilitySettings(); // VisibilitySettings | Private settings
apiInstance.setTemplatePrivateSettings(owner, templateId, version, body, (error, data, response) => {
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
 **owner** | **String**| API, domain, or template owner identifier (case-sensitive) | 
 **templateId** | **String**| Template identifier | 
 **version** | **String**| Version identifier | 
 **body** | [**VisibilitySettings**](VisibilitySettings.md)| Private settings | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## updateTemplateComments

> updateTemplateComments(owner, templateId, version, body)

Update the list of comments for a template

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.TemplatesApi();
let owner = "owner_example"; // String | API, domain, or template owner identifier (case-sensitive)
let templateId = "templateId_example"; // String | Template identifier
let version = "version_example"; // String | Version identifier
let body = new SwaggerHubRegistryApi.CommentsBatch(); // CommentsBatch | 
apiInstance.updateTemplateComments(owner, templateId, version, body, (error, data, response) => {
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
 **owner** | **String**| API, domain, or template owner identifier (case-sensitive) | 
 **templateId** | **String**| Template identifier | 
 **version** | **String**| Version identifier | 
 **body** | [**CommentsBatch**](CommentsBatch.md)|  | 

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

