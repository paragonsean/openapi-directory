# RudderApi.TechniquesApi

All URIs are relative to *https://rudder.example.local/rudder/api/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createTechnique**](TechniquesApi.md#createTechnique) | **PUT** /techniques | Create technique
[**deleteTechnique**](TechniquesApi.md#deleteTechnique) | **DELETE** /techniques/{techniqueId}/{techniqueVersion} | Delete technique
[**getTechniqueAllVersion**](TechniquesApi.md#getTechniqueAllVersion) | **GET** /techniques/{techniqueId} | Technique metadata by ID
[**getTechniqueAllVersionId**](TechniquesApi.md#getTechniqueAllVersionId) | **GET** /techniques/{techniqueId}/{techniqueVersion} | Technique metadata by version and ID
[**getTechniquesResources**](TechniquesApi.md#getTechniquesResources) | **GET** /techniques/{techniqueId}/{techniqueVersion}/resources | Technique&#39;s resources
[**listTechniqueVersionDirectives**](TechniquesApi.md#listTechniqueVersionDirectives) | **GET** /techniques/{techniqueId}/{techniqueVersion}/directives | List all directives based on a version of a technique
[**listTechniques**](TechniquesApi.md#listTechniques) | **GET** /techniques | List all techniques
[**listTechniquesDirectives**](TechniquesApi.md#listTechniquesDirectives) | **GET** /techniques/{techniqueId}/directives | List all directives based on a technique
[**listTechniquesVersions**](TechniquesApi.md#listTechniquesVersions) | **GET** /techniques/versions | List versions
[**methods**](TechniquesApi.md#methods) | **GET** /methods | List methods
[**reloadMethods**](TechniquesApi.md#reloadMethods) | **POST** /methods/reload | Reload methods
[**techniqueCategories**](TechniquesApi.md#techniqueCategories) | **GET** /techniques/categories | List categories
[**techniqueRevisions**](TechniquesApi.md#techniqueRevisions) | **GET** /techniques/{techniqueId}/{techniqueVersion}/revisions | Technique&#39;s revisions
[**techniques**](TechniquesApi.md#techniques) | **POST** /techniques/reload | Reload techniques
[**updateTechnique**](TechniquesApi.md#updateTechnique) | **POST** /techniques/{techniqueId}/{techniqueVersion} | Update technique



## createTechnique

> CreateTechnique200Response createTechnique(editorTechnique)

Create technique

Create a new technique in Rudder from a technique in the technique editor

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.TechniquesApi();
let editorTechnique = [new RudderApi.EditorTechnique()]; // [EditorTechnique] | 
apiInstance.createTechnique(editorTechnique, (error, data, response) => {
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
 **editorTechnique** | [**[EditorTechnique]**](EditorTechnique.md)|  | 

### Return type

[**CreateTechnique200Response**](CreateTechnique200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteTechnique

> DeleteTechnique200Response deleteTechnique(techniqueId, techniqueVersion)

Delete technique

Delete a technique from technique editor

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.TechniquesApi();
let techniqueId = "userManagement"; // String | Technique ID
let techniqueVersion = "6.0"; // String | Technique version
apiInstance.deleteTechnique(techniqueId, techniqueVersion, (error, data, response) => {
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
 **techniqueId** | **String**| Technique ID | 
 **techniqueVersion** | **String**| Technique version | 

### Return type

[**DeleteTechnique200Response**](DeleteTechnique200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTechniqueAllVersion

> GetTechniqueAllVersion200Response getTechniqueAllVersion(techniqueId)

Technique metadata by ID

Get each Technique&#39;s versions with their metadata by ID

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.TechniquesApi();
let techniqueId = "userManagement"; // String | Technique ID
apiInstance.getTechniqueAllVersion(techniqueId, (error, data, response) => {
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
 **techniqueId** | **String**| Technique ID | 

### Return type

[**GetTechniqueAllVersion200Response**](GetTechniqueAllVersion200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTechniqueAllVersionId

> GetTechniqueAllVersion200Response getTechniqueAllVersionId(techniqueId, techniqueVersion)

Technique metadata by version and ID

Get Technique metadata

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.TechniquesApi();
let techniqueId = "userManagement"; // String | Technique ID
let techniqueVersion = "6.0"; // String | Technique version
apiInstance.getTechniqueAllVersionId(techniqueId, techniqueVersion, (error, data, response) => {
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
 **techniqueId** | **String**| Technique ID | 
 **techniqueVersion** | **String**| Technique version | 

### Return type

[**GetTechniqueAllVersion200Response**](GetTechniqueAllVersion200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTechniquesResources

> GetTechniquesResources200Response getTechniquesResources(techniqueId, techniqueVersion)

Technique&#39;s resources

Get currently deployed resources of a technique

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.TechniquesApi();
let techniqueId = "userManagement"; // String | Technique ID
let techniqueVersion = "6.0"; // String | Technique version
apiInstance.getTechniquesResources(techniqueId, techniqueVersion, (error, data, response) => {
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
 **techniqueId** | **String**| Technique ID | 
 **techniqueVersion** | **String**| Technique version | 

### Return type

[**GetTechniquesResources200Response**](GetTechniquesResources200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTechniqueVersionDirectives

> ListTechniqueVersionDirectives200Response listTechniqueVersionDirectives(techniqueId, techniqueVersion)

List all directives based on a version of a technique

List all directives based on a version of a technique

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.TechniquesApi();
let techniqueId = "userManagement"; // String | Technique ID
let techniqueVersion = "6.0"; // String | Technique version
apiInstance.listTechniqueVersionDirectives(techniqueId, techniqueVersion, (error, data, response) => {
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
 **techniqueId** | **String**| Technique ID | 
 **techniqueVersion** | **String**| Technique version | 

### Return type

[**ListTechniqueVersionDirectives200Response**](ListTechniqueVersionDirectives200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTechniques

> ListTechniques200Response listTechniques()

List all techniques

List all technique with their versions

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.TechniquesApi();
apiInstance.listTechniques((error, data, response) => {
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

[**ListTechniques200Response**](ListTechniques200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTechniquesDirectives

> ListTechniquesDirectives200Response listTechniquesDirectives(techniqueId)

List all directives based on a technique

List all directives based on all version of a technique

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.TechniquesApi();
let techniqueId = "userManagement"; // String | Technique ID
apiInstance.listTechniquesDirectives(techniqueId, (error, data, response) => {
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
 **techniqueId** | **String**| Technique ID | 

### Return type

[**ListTechniquesDirectives200Response**](ListTechniquesDirectives200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTechniquesVersions

> ListTechniquesVersions200Response listTechniquesVersions()

List versions

List all techniques version

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.TechniquesApi();
apiInstance.listTechniquesVersions((error, data, response) => {
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

[**ListTechniquesVersions200Response**](ListTechniquesVersions200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## methods

> Methods200Response methods()

List methods

Get all generic methods metadata

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.TechniquesApi();
apiInstance.methods((error, data, response) => {
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

[**Methods200Response**](Methods200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reloadMethods

> Methods200Response reloadMethods()

Reload methods

Reload methods metadata from file system

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.TechniquesApi();
apiInstance.reloadMethods((error, data, response) => {
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

[**Methods200Response**](Methods200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## techniqueCategories

> TechniqueCategories200Response techniqueCategories()

List categories

Get all technique categories

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.TechniquesApi();
apiInstance.techniqueCategories((error, data, response) => {
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

[**TechniqueCategories200Response**](TechniqueCategories200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## techniqueRevisions

> TechniqueRevisions200Response techniqueRevisions(techniqueId, techniqueVersion)

Technique&#39;s revisions

Get revisions for given technique

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.TechniquesApi();
let techniqueId = "userManagement"; // String | Technique ID
let techniqueVersion = "6.0"; // String | Technique version
apiInstance.techniqueRevisions(techniqueId, techniqueVersion, (error, data, response) => {
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
 **techniqueId** | **String**| Technique ID | 
 **techniqueVersion** | **String**| Technique version | 

### Return type

[**TechniqueRevisions200Response**](TechniqueRevisions200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## techniques

> ListTechniques200Response techniques()

Reload techniques

Reload all techniques metadata from file system

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.TechniquesApi();
apiInstance.techniques((error, data, response) => {
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

[**ListTechniques200Response**](ListTechniques200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateTechnique

> CreateTechnique200Response updateTechnique(techniqueId, techniqueVersion, editorTechnique)

Update technique

Update technique created with technique editor

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.TechniquesApi();
let techniqueId = "userManagement"; // String | Technique ID
let techniqueVersion = "6.0"; // String | Technique version
let editorTechnique = [new RudderApi.EditorTechnique()]; // [EditorTechnique] | 
apiInstance.updateTechnique(techniqueId, techniqueVersion, editorTechnique, (error, data, response) => {
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
 **techniqueId** | **String**| Technique ID | 
 **techniqueVersion** | **String**| Technique version | 
 **editorTechnique** | [**[EditorTechnique]**](EditorTechnique.md)|  | 

### Return type

[**CreateTechnique200Response**](CreateTechnique200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

