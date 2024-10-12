# AmplifyBackend.DefaultApi

All URIs are relative to *http://amplifybackend.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cloneBackend**](DefaultApi.md#cloneBackend) | **POST** /backend/{appId}/environments/{backendEnvironmentName}/clone | 
[**createBackend**](DefaultApi.md#createBackend) | **POST** /backend | 
[**createBackendAPI**](DefaultApi.md#createBackendAPI) | **POST** /backend/{appId}/api | 
[**createBackendAuth**](DefaultApi.md#createBackendAuth) | **POST** /backend/{appId}/auth | 
[**createBackendConfig**](DefaultApi.md#createBackendConfig) | **POST** /backend/{appId}/config | 
[**createBackendStorage**](DefaultApi.md#createBackendStorage) | **POST** /backend/{appId}/storage | 
[**createToken**](DefaultApi.md#createToken) | **POST** /backend/{appId}/challenge | 
[**deleteBackend**](DefaultApi.md#deleteBackend) | **POST** /backend/{appId}/environments/{backendEnvironmentName}/remove | 
[**deleteBackendAPI**](DefaultApi.md#deleteBackendAPI) | **POST** /backend/{appId}/api/{backendEnvironmentName}/remove | 
[**deleteBackendAuth**](DefaultApi.md#deleteBackendAuth) | **POST** /backend/{appId}/auth/{backendEnvironmentName}/remove | 
[**deleteBackendStorage**](DefaultApi.md#deleteBackendStorage) | **POST** /backend/{appId}/storage/{backendEnvironmentName}/remove | 
[**deleteToken**](DefaultApi.md#deleteToken) | **POST** /backend/{appId}/challenge/{sessionId}/remove | 
[**generateBackendAPIModels**](DefaultApi.md#generateBackendAPIModels) | **POST** /backend/{appId}/api/{backendEnvironmentName}/generateModels | 
[**getBackend**](DefaultApi.md#getBackend) | **POST** /backend/{appId}/details | 
[**getBackendAPI**](DefaultApi.md#getBackendAPI) | **POST** /backend/{appId}/api/{backendEnvironmentName}/details | 
[**getBackendAPIModels**](DefaultApi.md#getBackendAPIModels) | **POST** /backend/{appId}/api/{backendEnvironmentName}/getModels | 
[**getBackendAuth**](DefaultApi.md#getBackendAuth) | **POST** /backend/{appId}/auth/{backendEnvironmentName}/details | 
[**getBackendJob**](DefaultApi.md#getBackendJob) | **GET** /backend/{appId}/job/{backendEnvironmentName}/{jobId} | 
[**getBackendStorage**](DefaultApi.md#getBackendStorage) | **POST** /backend/{appId}/storage/{backendEnvironmentName}/details | 
[**getToken**](DefaultApi.md#getToken) | **GET** /backend/{appId}/challenge/{sessionId} | 
[**importBackendAuth**](DefaultApi.md#importBackendAuth) | **POST** /backend/{appId}/auth/{backendEnvironmentName}/import | 
[**importBackendStorage**](DefaultApi.md#importBackendStorage) | **POST** /backend/{appId}/storage/{backendEnvironmentName}/import | 
[**listBackendJobs**](DefaultApi.md#listBackendJobs) | **POST** /backend/{appId}/job/{backendEnvironmentName} | 
[**listS3Buckets**](DefaultApi.md#listS3Buckets) | **POST** /s3Buckets | 
[**removeAllBackends**](DefaultApi.md#removeAllBackends) | **POST** /backend/{appId}/remove | 
[**removeBackendConfig**](DefaultApi.md#removeBackendConfig) | **POST** /backend/{appId}/config/remove | 
[**updateBackendAPI**](DefaultApi.md#updateBackendAPI) | **POST** /backend/{appId}/api/{backendEnvironmentName} | 
[**updateBackendAuth**](DefaultApi.md#updateBackendAuth) | **POST** /backend/{appId}/auth/{backendEnvironmentName} | 
[**updateBackendConfig**](DefaultApi.md#updateBackendConfig) | **POST** /backend/{appId}/config/update | 
[**updateBackendJob**](DefaultApi.md#updateBackendJob) | **POST** /backend/{appId}/job/{backendEnvironmentName}/{jobId} | 
[**updateBackendStorage**](DefaultApi.md#updateBackendStorage) | **POST** /backend/{appId}/storage/{backendEnvironmentName} | 



## cloneBackend

> CloneBackendResponse cloneBackend(appId, backendEnvironmentName, cloneBackendRequest, opts)



This operation clones an existing backend.

### Example

```javascript
import AmplifyBackend from 'amplify_backend';
let defaultClient = AmplifyBackend.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmplifyBackend.DefaultApi();
let appId = "appId_example"; // String | The app ID.
let backendEnvironmentName = "backendEnvironmentName_example"; // String | The name of the backend environment.
let cloneBackendRequest = new AmplifyBackend.CloneBackendRequest(); // CloneBackendRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.cloneBackend(appId, backendEnvironmentName, cloneBackendRequest, opts, (error, data, response) => {
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
 **appId** | **String**| The app ID. | 
 **backendEnvironmentName** | **String**| The name of the backend environment. | 
 **cloneBackendRequest** | [**CloneBackendRequest**](CloneBackendRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CloneBackendResponse**](CloneBackendResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createBackend

> CreateBackendResponse createBackend(createBackendRequest, opts)



This operation creates a backend for an Amplify app. Backends are automatically created at the time of app creation.

### Example

```javascript
import AmplifyBackend from 'amplify_backend';
let defaultClient = AmplifyBackend.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmplifyBackend.DefaultApi();
let createBackendRequest = new AmplifyBackend.CreateBackendRequest(); // CreateBackendRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createBackend(createBackendRequest, opts, (error, data, response) => {
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
 **createBackendRequest** | [**CreateBackendRequest**](CreateBackendRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateBackendResponse**](CreateBackendResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createBackendAPI

> CreateBackendAPIResponse createBackendAPI(appId, createBackendAPIRequest, opts)



Creates a new backend API resource.

### Example

```javascript
import AmplifyBackend from 'amplify_backend';
let defaultClient = AmplifyBackend.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmplifyBackend.DefaultApi();
let appId = "appId_example"; // String | The app ID.
let createBackendAPIRequest = new AmplifyBackend.CreateBackendAPIRequest(); // CreateBackendAPIRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createBackendAPI(appId, createBackendAPIRequest, opts, (error, data, response) => {
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
 **appId** | **String**| The app ID. | 
 **createBackendAPIRequest** | [**CreateBackendAPIRequest**](CreateBackendAPIRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateBackendAPIResponse**](CreateBackendAPIResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createBackendAuth

> CreateBackendAuthResponse createBackendAuth(appId, createBackendAuthRequest, opts)



Creates a new backend authentication resource.

### Example

```javascript
import AmplifyBackend from 'amplify_backend';
let defaultClient = AmplifyBackend.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmplifyBackend.DefaultApi();
let appId = "appId_example"; // String | The app ID.
let createBackendAuthRequest = new AmplifyBackend.CreateBackendAuthRequest(); // CreateBackendAuthRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createBackendAuth(appId, createBackendAuthRequest, opts, (error, data, response) => {
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
 **appId** | **String**| The app ID. | 
 **createBackendAuthRequest** | [**CreateBackendAuthRequest**](CreateBackendAuthRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateBackendAuthResponse**](CreateBackendAuthResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createBackendConfig

> CreateBackendConfigResponse createBackendConfig(appId, createBackendConfigRequest, opts)



Creates a config object for a backend.

### Example

```javascript
import AmplifyBackend from 'amplify_backend';
let defaultClient = AmplifyBackend.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmplifyBackend.DefaultApi();
let appId = "appId_example"; // String | The app ID.
let createBackendConfigRequest = new AmplifyBackend.CreateBackendConfigRequest(); // CreateBackendConfigRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createBackendConfig(appId, createBackendConfigRequest, opts, (error, data, response) => {
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
 **appId** | **String**| The app ID. | 
 **createBackendConfigRequest** | [**CreateBackendConfigRequest**](CreateBackendConfigRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateBackendConfigResponse**](CreateBackendConfigResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createBackendStorage

> CreateBackendStorageResponse createBackendStorage(appId, createBackendStorageRequest, opts)



Creates a backend storage resource.

### Example

```javascript
import AmplifyBackend from 'amplify_backend';
let defaultClient = AmplifyBackend.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmplifyBackend.DefaultApi();
let appId = "appId_example"; // String | The app ID.
let createBackendStorageRequest = new AmplifyBackend.CreateBackendStorageRequest(); // CreateBackendStorageRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createBackendStorage(appId, createBackendStorageRequest, opts, (error, data, response) => {
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
 **appId** | **String**| The app ID. | 
 **createBackendStorageRequest** | [**CreateBackendStorageRequest**](CreateBackendStorageRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateBackendStorageResponse**](CreateBackendStorageResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createToken

> CreateTokenResponse createToken(appId, opts)



Generates a one-time challenge code to authenticate a user into your Amplify Admin UI.

### Example

```javascript
import AmplifyBackend from 'amplify_backend';
let defaultClient = AmplifyBackend.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmplifyBackend.DefaultApi();
let appId = "appId_example"; // String | The app ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createToken(appId, opts, (error, data, response) => {
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
 **appId** | **String**| The app ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateTokenResponse**](CreateTokenResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteBackend

> DeleteBackendResponse deleteBackend(appId, backendEnvironmentName, opts)



Removes an existing environment from your Amplify project.

### Example

```javascript
import AmplifyBackend from 'amplify_backend';
let defaultClient = AmplifyBackend.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmplifyBackend.DefaultApi();
let appId = "appId_example"; // String | The app ID.
let backendEnvironmentName = "backendEnvironmentName_example"; // String | The name of the backend environment.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteBackend(appId, backendEnvironmentName, opts, (error, data, response) => {
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
 **appId** | **String**| The app ID. | 
 **backendEnvironmentName** | **String**| The name of the backend environment. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteBackendResponse**](DeleteBackendResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteBackendAPI

> DeleteBackendAPIResponse deleteBackendAPI(appId, backendEnvironmentName, deleteBackendAPIRequest, opts)



Deletes an existing backend API resource.

### Example

```javascript
import AmplifyBackend from 'amplify_backend';
let defaultClient = AmplifyBackend.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmplifyBackend.DefaultApi();
let appId = "appId_example"; // String | The app ID.
let backendEnvironmentName = "backendEnvironmentName_example"; // String | The name of the backend environment.
let deleteBackendAPIRequest = new AmplifyBackend.DeleteBackendAPIRequest(); // DeleteBackendAPIRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteBackendAPI(appId, backendEnvironmentName, deleteBackendAPIRequest, opts, (error, data, response) => {
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
 **appId** | **String**| The app ID. | 
 **backendEnvironmentName** | **String**| The name of the backend environment. | 
 **deleteBackendAPIRequest** | [**DeleteBackendAPIRequest**](DeleteBackendAPIRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteBackendAPIResponse**](DeleteBackendAPIResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteBackendAuth

> DeleteBackendAuthResponse deleteBackendAuth(appId, backendEnvironmentName, deleteBackendAuthRequest, opts)



Deletes an existing backend authentication resource.

### Example

```javascript
import AmplifyBackend from 'amplify_backend';
let defaultClient = AmplifyBackend.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmplifyBackend.DefaultApi();
let appId = "appId_example"; // String | The app ID.
let backendEnvironmentName = "backendEnvironmentName_example"; // String | The name of the backend environment.
let deleteBackendAuthRequest = new AmplifyBackend.DeleteBackendAuthRequest(); // DeleteBackendAuthRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteBackendAuth(appId, backendEnvironmentName, deleteBackendAuthRequest, opts, (error, data, response) => {
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
 **appId** | **String**| The app ID. | 
 **backendEnvironmentName** | **String**| The name of the backend environment. | 
 **deleteBackendAuthRequest** | [**DeleteBackendAuthRequest**](DeleteBackendAuthRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteBackendAuthResponse**](DeleteBackendAuthResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteBackendStorage

> DeleteBackendStorageResponse deleteBackendStorage(appId, backendEnvironmentName, deleteBackendStorageRequest, opts)



Removes the specified backend storage resource.

### Example

```javascript
import AmplifyBackend from 'amplify_backend';
let defaultClient = AmplifyBackend.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmplifyBackend.DefaultApi();
let appId = "appId_example"; // String | The app ID.
let backendEnvironmentName = "backendEnvironmentName_example"; // String | The name of the backend environment.
let deleteBackendStorageRequest = new AmplifyBackend.DeleteBackendStorageRequest(); // DeleteBackendStorageRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteBackendStorage(appId, backendEnvironmentName, deleteBackendStorageRequest, opts, (error, data, response) => {
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
 **appId** | **String**| The app ID. | 
 **backendEnvironmentName** | **String**| The name of the backend environment. | 
 **deleteBackendStorageRequest** | [**DeleteBackendStorageRequest**](DeleteBackendStorageRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteBackendStorageResponse**](DeleteBackendStorageResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteToken

> DeleteTokenResponse deleteToken(appId, sessionId, opts)



Deletes the challenge token based on the given appId and sessionId.

### Example

```javascript
import AmplifyBackend from 'amplify_backend';
let defaultClient = AmplifyBackend.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmplifyBackend.DefaultApi();
let appId = "appId_example"; // String | The app ID.
let sessionId = "sessionId_example"; // String | The session ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteToken(appId, sessionId, opts, (error, data, response) => {
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
 **appId** | **String**| The app ID. | 
 **sessionId** | **String**| The session ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteTokenResponse**](DeleteTokenResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## generateBackendAPIModels

> GenerateBackendAPIModelsResponse generateBackendAPIModels(appId, backendEnvironmentName, deleteBackendAuthRequest, opts)



Generates a model schema for an existing backend API resource.

### Example

```javascript
import AmplifyBackend from 'amplify_backend';
let defaultClient = AmplifyBackend.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmplifyBackend.DefaultApi();
let appId = "appId_example"; // String | The app ID.
let backendEnvironmentName = "backendEnvironmentName_example"; // String | The name of the backend environment.
let deleteBackendAuthRequest = new AmplifyBackend.DeleteBackendAuthRequest(); // DeleteBackendAuthRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.generateBackendAPIModels(appId, backendEnvironmentName, deleteBackendAuthRequest, opts, (error, data, response) => {
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
 **appId** | **String**| The app ID. | 
 **backendEnvironmentName** | **String**| The name of the backend environment. | 
 **deleteBackendAuthRequest** | [**DeleteBackendAuthRequest**](DeleteBackendAuthRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GenerateBackendAPIModelsResponse**](GenerateBackendAPIModelsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getBackend

> GetBackendResponse getBackend(appId, getBackendRequest, opts)



Provides project-level details for your Amplify UI project.

### Example

```javascript
import AmplifyBackend from 'amplify_backend';
let defaultClient = AmplifyBackend.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmplifyBackend.DefaultApi();
let appId = "appId_example"; // String | The app ID.
let getBackendRequest = new AmplifyBackend.GetBackendRequest(); // GetBackendRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getBackend(appId, getBackendRequest, opts, (error, data, response) => {
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
 **appId** | **String**| The app ID. | 
 **getBackendRequest** | [**GetBackendRequest**](GetBackendRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetBackendResponse**](GetBackendResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getBackendAPI

> GetBackendAPIResponse getBackendAPI(appId, backendEnvironmentName, deleteBackendAPIRequest, opts)



Gets the details for a backend API.

### Example

```javascript
import AmplifyBackend from 'amplify_backend';
let defaultClient = AmplifyBackend.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmplifyBackend.DefaultApi();
let appId = "appId_example"; // String | The app ID.
let backendEnvironmentName = "backendEnvironmentName_example"; // String | The name of the backend environment.
let deleteBackendAPIRequest = new AmplifyBackend.DeleteBackendAPIRequest(); // DeleteBackendAPIRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getBackendAPI(appId, backendEnvironmentName, deleteBackendAPIRequest, opts, (error, data, response) => {
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
 **appId** | **String**| The app ID. | 
 **backendEnvironmentName** | **String**| The name of the backend environment. | 
 **deleteBackendAPIRequest** | [**DeleteBackendAPIRequest**](DeleteBackendAPIRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetBackendAPIResponse**](GetBackendAPIResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getBackendAPIModels

> GetBackendAPIModelsResponse getBackendAPIModels(appId, backendEnvironmentName, deleteBackendAuthRequest, opts)



Gets a model introspection schema for an existing backend API resource.

### Example

```javascript
import AmplifyBackend from 'amplify_backend';
let defaultClient = AmplifyBackend.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmplifyBackend.DefaultApi();
let appId = "appId_example"; // String | The app ID.
let backendEnvironmentName = "backendEnvironmentName_example"; // String | The name of the backend environment.
let deleteBackendAuthRequest = new AmplifyBackend.DeleteBackendAuthRequest(); // DeleteBackendAuthRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getBackendAPIModels(appId, backendEnvironmentName, deleteBackendAuthRequest, opts, (error, data, response) => {
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
 **appId** | **String**| The app ID. | 
 **backendEnvironmentName** | **String**| The name of the backend environment. | 
 **deleteBackendAuthRequest** | [**DeleteBackendAuthRequest**](DeleteBackendAuthRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetBackendAPIModelsResponse**](GetBackendAPIModelsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getBackendAuth

> GetBackendAuthResponse getBackendAuth(appId, backendEnvironmentName, deleteBackendAuthRequest, opts)



Gets a backend auth details.

### Example

```javascript
import AmplifyBackend from 'amplify_backend';
let defaultClient = AmplifyBackend.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmplifyBackend.DefaultApi();
let appId = "appId_example"; // String | The app ID.
let backendEnvironmentName = "backendEnvironmentName_example"; // String | The name of the backend environment.
let deleteBackendAuthRequest = new AmplifyBackend.DeleteBackendAuthRequest(); // DeleteBackendAuthRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getBackendAuth(appId, backendEnvironmentName, deleteBackendAuthRequest, opts, (error, data, response) => {
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
 **appId** | **String**| The app ID. | 
 **backendEnvironmentName** | **String**| The name of the backend environment. | 
 **deleteBackendAuthRequest** | [**DeleteBackendAuthRequest**](DeleteBackendAuthRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetBackendAuthResponse**](GetBackendAuthResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getBackendJob

> GetBackendJobResponse getBackendJob(appId, backendEnvironmentName, jobId, opts)



Returns information about a specific job.

### Example

```javascript
import AmplifyBackend from 'amplify_backend';
let defaultClient = AmplifyBackend.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmplifyBackend.DefaultApi();
let appId = "appId_example"; // String | The app ID.
let backendEnvironmentName = "backendEnvironmentName_example"; // String | The name of the backend environment.
let jobId = "jobId_example"; // String | The ID for the job.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getBackendJob(appId, backendEnvironmentName, jobId, opts, (error, data, response) => {
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
 **appId** | **String**| The app ID. | 
 **backendEnvironmentName** | **String**| The name of the backend environment. | 
 **jobId** | **String**| The ID for the job. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetBackendJobResponse**](GetBackendJobResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBackendStorage

> GetBackendStorageResponse getBackendStorage(appId, backendEnvironmentName, getBackendStorageRequest, opts)



Gets details for a backend storage resource.

### Example

```javascript
import AmplifyBackend from 'amplify_backend';
let defaultClient = AmplifyBackend.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmplifyBackend.DefaultApi();
let appId = "appId_example"; // String | The app ID.
let backendEnvironmentName = "backendEnvironmentName_example"; // String | The name of the backend environment.
let getBackendStorageRequest = new AmplifyBackend.GetBackendStorageRequest(); // GetBackendStorageRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getBackendStorage(appId, backendEnvironmentName, getBackendStorageRequest, opts, (error, data, response) => {
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
 **appId** | **String**| The app ID. | 
 **backendEnvironmentName** | **String**| The name of the backend environment. | 
 **getBackendStorageRequest** | [**GetBackendStorageRequest**](GetBackendStorageRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetBackendStorageResponse**](GetBackendStorageResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getToken

> GetTokenResponse getToken(appId, sessionId, opts)



Gets the challenge token based on the given appId and sessionId.

### Example

```javascript
import AmplifyBackend from 'amplify_backend';
let defaultClient = AmplifyBackend.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmplifyBackend.DefaultApi();
let appId = "appId_example"; // String | The app ID.
let sessionId = "sessionId_example"; // String | The session ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getToken(appId, sessionId, opts, (error, data, response) => {
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
 **appId** | **String**| The app ID. | 
 **sessionId** | **String**| The session ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetTokenResponse**](GetTokenResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## importBackendAuth

> ImportBackendAuthResponse importBackendAuth(appId, backendEnvironmentName, importBackendAuthRequest, opts)



Imports an existing backend authentication resource.

### Example

```javascript
import AmplifyBackend from 'amplify_backend';
let defaultClient = AmplifyBackend.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmplifyBackend.DefaultApi();
let appId = "appId_example"; // String | The app ID.
let backendEnvironmentName = "backendEnvironmentName_example"; // String | The name of the backend environment.
let importBackendAuthRequest = new AmplifyBackend.ImportBackendAuthRequest(); // ImportBackendAuthRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.importBackendAuth(appId, backendEnvironmentName, importBackendAuthRequest, opts, (error, data, response) => {
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
 **appId** | **String**| The app ID. | 
 **backendEnvironmentName** | **String**| The name of the backend environment. | 
 **importBackendAuthRequest** | [**ImportBackendAuthRequest**](ImportBackendAuthRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ImportBackendAuthResponse**](ImportBackendAuthResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## importBackendStorage

> ImportBackendStorageResponse importBackendStorage(appId, backendEnvironmentName, importBackendStorageRequest, opts)



Imports an existing backend storage resource.

### Example

```javascript
import AmplifyBackend from 'amplify_backend';
let defaultClient = AmplifyBackend.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmplifyBackend.DefaultApi();
let appId = "appId_example"; // String | The app ID.
let backendEnvironmentName = "backendEnvironmentName_example"; // String | The name of the backend environment.
let importBackendStorageRequest = new AmplifyBackend.ImportBackendStorageRequest(); // ImportBackendStorageRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.importBackendStorage(appId, backendEnvironmentName, importBackendStorageRequest, opts, (error, data, response) => {
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
 **appId** | **String**| The app ID. | 
 **backendEnvironmentName** | **String**| The name of the backend environment. | 
 **importBackendStorageRequest** | [**ImportBackendStorageRequest**](ImportBackendStorageRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ImportBackendStorageResponse**](ImportBackendStorageResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listBackendJobs

> ListBackendJobsResponse listBackendJobs(appId, backendEnvironmentName, listBackendJobsRequest, opts)



Lists the jobs for the backend of an Amplify app.

### Example

```javascript
import AmplifyBackend from 'amplify_backend';
let defaultClient = AmplifyBackend.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmplifyBackend.DefaultApi();
let appId = "appId_example"; // String | The app ID.
let backendEnvironmentName = "backendEnvironmentName_example"; // String | The name of the backend environment.
let listBackendJobsRequest = new AmplifyBackend.ListBackendJobsRequest(); // ListBackendJobsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.listBackendJobs(appId, backendEnvironmentName, listBackendJobsRequest, opts, (error, data, response) => {
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
 **appId** | **String**| The app ID. | 
 **backendEnvironmentName** | **String**| The name of the backend environment. | 
 **listBackendJobsRequest** | [**ListBackendJobsRequest**](ListBackendJobsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**ListBackendJobsResponse**](ListBackendJobsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listS3Buckets

> ListS3BucketsResponse listS3Buckets(listS3BucketsRequest, opts)



The list of S3 buckets in your account.

### Example

```javascript
import AmplifyBackend from 'amplify_backend';
let defaultClient = AmplifyBackend.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmplifyBackend.DefaultApi();
let listS3BucketsRequest = new AmplifyBackend.ListS3BucketsRequest(); // ListS3BucketsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.listS3Buckets(listS3BucketsRequest, opts, (error, data, response) => {
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
 **listS3BucketsRequest** | [**ListS3BucketsRequest**](ListS3BucketsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ListS3BucketsResponse**](ListS3BucketsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## removeAllBackends

> RemoveAllBackendsResponse removeAllBackends(appId, removeAllBackendsRequest, opts)



Removes all backend environments from your Amplify project.

### Example

```javascript
import AmplifyBackend from 'amplify_backend';
let defaultClient = AmplifyBackend.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmplifyBackend.DefaultApi();
let appId = "appId_example"; // String | The app ID.
let removeAllBackendsRequest = new AmplifyBackend.RemoveAllBackendsRequest(); // RemoveAllBackendsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.removeAllBackends(appId, removeAllBackendsRequest, opts, (error, data, response) => {
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
 **appId** | **String**| The app ID. | 
 **removeAllBackendsRequest** | [**RemoveAllBackendsRequest**](RemoveAllBackendsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**RemoveAllBackendsResponse**](RemoveAllBackendsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## removeBackendConfig

> RemoveBackendConfigResponse removeBackendConfig(appId, opts)



Removes the AWS resources required to access the Amplify Admin UI.

### Example

```javascript
import AmplifyBackend from 'amplify_backend';
let defaultClient = AmplifyBackend.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmplifyBackend.DefaultApi();
let appId = "appId_example"; // String | The app ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.removeBackendConfig(appId, opts, (error, data, response) => {
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
 **appId** | **String**| The app ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**RemoveBackendConfigResponse**](RemoveBackendConfigResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateBackendAPI

> UpdateBackendAPIResponse updateBackendAPI(appId, backendEnvironmentName, deleteBackendAPIRequest, opts)



Updates an existing backend API resource.

### Example

```javascript
import AmplifyBackend from 'amplify_backend';
let defaultClient = AmplifyBackend.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmplifyBackend.DefaultApi();
let appId = "appId_example"; // String | The app ID.
let backendEnvironmentName = "backendEnvironmentName_example"; // String | The name of the backend environment.
let deleteBackendAPIRequest = new AmplifyBackend.DeleteBackendAPIRequest(); // DeleteBackendAPIRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateBackendAPI(appId, backendEnvironmentName, deleteBackendAPIRequest, opts, (error, data, response) => {
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
 **appId** | **String**| The app ID. | 
 **backendEnvironmentName** | **String**| The name of the backend environment. | 
 **deleteBackendAPIRequest** | [**DeleteBackendAPIRequest**](DeleteBackendAPIRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateBackendAPIResponse**](UpdateBackendAPIResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateBackendAuth

> UpdateBackendAuthResponse updateBackendAuth(appId, backendEnvironmentName, updateBackendAuthRequest, opts)



Updates an existing backend authentication resource.

### Example

```javascript
import AmplifyBackend from 'amplify_backend';
let defaultClient = AmplifyBackend.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmplifyBackend.DefaultApi();
let appId = "appId_example"; // String | The app ID.
let backendEnvironmentName = "backendEnvironmentName_example"; // String | The name of the backend environment.
let updateBackendAuthRequest = new AmplifyBackend.UpdateBackendAuthRequest(); // UpdateBackendAuthRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateBackendAuth(appId, backendEnvironmentName, updateBackendAuthRequest, opts, (error, data, response) => {
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
 **appId** | **String**| The app ID. | 
 **backendEnvironmentName** | **String**| The name of the backend environment. | 
 **updateBackendAuthRequest** | [**UpdateBackendAuthRequest**](UpdateBackendAuthRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateBackendAuthResponse**](UpdateBackendAuthResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateBackendConfig

> UpdateBackendConfigResponse updateBackendConfig(appId, updateBackendConfigRequest, opts)



Updates the AWS resources required to access the Amplify Admin UI.

### Example

```javascript
import AmplifyBackend from 'amplify_backend';
let defaultClient = AmplifyBackend.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmplifyBackend.DefaultApi();
let appId = "appId_example"; // String | The app ID.
let updateBackendConfigRequest = new AmplifyBackend.UpdateBackendConfigRequest(); // UpdateBackendConfigRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateBackendConfig(appId, updateBackendConfigRequest, opts, (error, data, response) => {
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
 **appId** | **String**| The app ID. | 
 **updateBackendConfigRequest** | [**UpdateBackendConfigRequest**](UpdateBackendConfigRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateBackendConfigResponse**](UpdateBackendConfigResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateBackendJob

> UpdateBackendJobResponse updateBackendJob(appId, backendEnvironmentName, jobId, updateBackendJobRequest, opts)



Updates a specific job.

### Example

```javascript
import AmplifyBackend from 'amplify_backend';
let defaultClient = AmplifyBackend.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmplifyBackend.DefaultApi();
let appId = "appId_example"; // String | The app ID.
let backendEnvironmentName = "backendEnvironmentName_example"; // String | The name of the backend environment.
let jobId = "jobId_example"; // String | The ID for the job.
let updateBackendJobRequest = new AmplifyBackend.UpdateBackendJobRequest(); // UpdateBackendJobRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateBackendJob(appId, backendEnvironmentName, jobId, updateBackendJobRequest, opts, (error, data, response) => {
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
 **appId** | **String**| The app ID. | 
 **backendEnvironmentName** | **String**| The name of the backend environment. | 
 **jobId** | **String**| The ID for the job. | 
 **updateBackendJobRequest** | [**UpdateBackendJobRequest**](UpdateBackendJobRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateBackendJobResponse**](UpdateBackendJobResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateBackendStorage

> UpdateBackendStorageResponse updateBackendStorage(appId, backendEnvironmentName, updateBackendStorageRequest, opts)



Updates an existing backend storage resource.

### Example

```javascript
import AmplifyBackend from 'amplify_backend';
let defaultClient = AmplifyBackend.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmplifyBackend.DefaultApi();
let appId = "appId_example"; // String | The app ID.
let backendEnvironmentName = "backendEnvironmentName_example"; // String | The name of the backend environment.
let updateBackendStorageRequest = new AmplifyBackend.UpdateBackendStorageRequest(); // UpdateBackendStorageRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateBackendStorage(appId, backendEnvironmentName, updateBackendStorageRequest, opts, (error, data, response) => {
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
 **appId** | **String**| The app ID. | 
 **backendEnvironmentName** | **String**| The name of the backend environment. | 
 **updateBackendStorageRequest** | [**UpdateBackendStorageRequest**](UpdateBackendStorageRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateBackendStorageResponse**](UpdateBackendStorageResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

