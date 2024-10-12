# CircleCiRestApi.DefaultApi

All URIs are relative to *https://circleci.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**meGet**](DefaultApi.md#meGet) | **GET** /me | 
[**projectUsernameProjectBuildCacheDelete**](DefaultApi.md#projectUsernameProjectBuildCacheDelete) | **DELETE** /project/{username}/{project}/build-cache | 
[**projectUsernameProjectBuildNumArtifactsGet**](DefaultApi.md#projectUsernameProjectBuildNumArtifactsGet) | **GET** /project/{username}/{project}/{build_num}/artifacts | 
[**projectUsernameProjectBuildNumCancelPost**](DefaultApi.md#projectUsernameProjectBuildNumCancelPost) | **POST** /project/{username}/{project}/{build_num}/cancel | 
[**projectUsernameProjectBuildNumGet**](DefaultApi.md#projectUsernameProjectBuildNumGet) | **GET** /project/{username}/{project}/{build_num} | 
[**projectUsernameProjectBuildNumRetryPost**](DefaultApi.md#projectUsernameProjectBuildNumRetryPost) | **POST** /project/{username}/{project}/{build_num}/retry | 
[**projectUsernameProjectBuildNumTestsGet**](DefaultApi.md#projectUsernameProjectBuildNumTestsGet) | **GET** /project/{username}/{project}/{build_num}/tests | 
[**projectUsernameProjectCheckoutKeyFingerprintDelete**](DefaultApi.md#projectUsernameProjectCheckoutKeyFingerprintDelete) | **DELETE** /project/{username}/{project}/checkout-key/{fingerprint} | 
[**projectUsernameProjectCheckoutKeyFingerprintGet**](DefaultApi.md#projectUsernameProjectCheckoutKeyFingerprintGet) | **GET** /project/{username}/{project}/checkout-key/{fingerprint} | 
[**projectUsernameProjectCheckoutKeyGet**](DefaultApi.md#projectUsernameProjectCheckoutKeyGet) | **GET** /project/{username}/{project}/checkout-key | 
[**projectUsernameProjectCheckoutKeyPost**](DefaultApi.md#projectUsernameProjectCheckoutKeyPost) | **POST** /project/{username}/{project}/checkout-key | 
[**projectUsernameProjectEnvvarGet**](DefaultApi.md#projectUsernameProjectEnvvarGet) | **GET** /project/{username}/{project}/envvar | 
[**projectUsernameProjectEnvvarNameDelete**](DefaultApi.md#projectUsernameProjectEnvvarNameDelete) | **DELETE** /project/{username}/{project}/envvar/{name} | 
[**projectUsernameProjectEnvvarNameGet**](DefaultApi.md#projectUsernameProjectEnvvarNameGet) | **GET** /project/{username}/{project}/envvar/{name} | 
[**projectUsernameProjectEnvvarPost**](DefaultApi.md#projectUsernameProjectEnvvarPost) | **POST** /project/{username}/{project}/envvar | 
[**projectUsernameProjectGet**](DefaultApi.md#projectUsernameProjectGet) | **GET** /project/{username}/{project} | 
[**projectUsernameProjectPost**](DefaultApi.md#projectUsernameProjectPost) | **POST** /project/{username}/{project} | 
[**projectUsernameProjectSshKeyPost**](DefaultApi.md#projectUsernameProjectSshKeyPost) | **POST** /project/{username}/{project}/ssh-key | 
[**projectUsernameProjectTreeBranchPost**](DefaultApi.md#projectUsernameProjectTreeBranchPost) | **POST** /project/{username}/{project}/tree/{branch} | 
[**projectsGet**](DefaultApi.md#projectsGet) | **GET** /projects | 
[**recentBuildsGet**](DefaultApi.md#recentBuildsGet) | **GET** /recent-builds | 
[**userHerokuKeyPost**](DefaultApi.md#userHerokuKeyPost) | **POST** /user/heroku-key | 



## meGet

> User meGet()



Provides information about the signed in user. 

### Example

```javascript
import CircleCiRestApi from 'circle_ci_rest_api';
let defaultClient = CircleCiRestApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new CircleCiRestApi.DefaultApi();
apiInstance.meGet((error, data, response) => {
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

[**User**](User.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectUsernameProjectBuildCacheDelete

> ProjectUsernameProjectBuildCacheDelete200Response projectUsernameProjectBuildCacheDelete(username, project)



Clears the cache for a project. 

### Example

```javascript
import CircleCiRestApi from 'circle_ci_rest_api';
let defaultClient = CircleCiRestApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new CircleCiRestApi.DefaultApi();
let username = "username_example"; // String | XXXXXXXXX 
let project = "project_example"; // String | XXXXXXXXX 
apiInstance.projectUsernameProjectBuildCacheDelete(username, project, (error, data, response) => {
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
 **username** | **String**| XXXXXXXXX  | 
 **project** | **String**| XXXXXXXXX  | 

### Return type

[**ProjectUsernameProjectBuildCacheDelete200Response**](ProjectUsernameProjectBuildCacheDelete200Response.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectUsernameProjectBuildNumArtifactsGet

> [Artifact] projectUsernameProjectBuildNumArtifactsGet(username, project, buildNum)



List the artifacts produced by a given build. 

### Example

```javascript
import CircleCiRestApi from 'circle_ci_rest_api';
let defaultClient = CircleCiRestApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new CircleCiRestApi.DefaultApi();
let username = "username_example"; // String | XXXXXXXXX 
let project = "project_example"; // String | XXXXXXXXX 
let buildNum = 56; // Number | XXXXXXXXXX 
apiInstance.projectUsernameProjectBuildNumArtifactsGet(username, project, buildNum, (error, data, response) => {
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
 **username** | **String**| XXXXXXXXX  | 
 **project** | **String**| XXXXXXXXX  | 
 **buildNum** | **Number**| XXXXXXXXXX  | 

### Return type

[**[Artifact]**](Artifact.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectUsernameProjectBuildNumCancelPost

> Build projectUsernameProjectBuildNumCancelPost(username, project, buildNum)



Cancels the build, returns a summary of the build. 

### Example

```javascript
import CircleCiRestApi from 'circle_ci_rest_api';
let defaultClient = CircleCiRestApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new CircleCiRestApi.DefaultApi();
let username = "username_example"; // String | XXXXXXXXX 
let project = "project_example"; // String | XXXXXXXXX 
let buildNum = 56; // Number | XXXXXXXXXX 
apiInstance.projectUsernameProjectBuildNumCancelPost(username, project, buildNum, (error, data, response) => {
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
 **username** | **String**| XXXXXXXXX  | 
 **project** | **String**| XXXXXXXXX  | 
 **buildNum** | **Number**| XXXXXXXXXX  | 

### Return type

[**Build**](Build.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectUsernameProjectBuildNumGet

> BuildDetail projectUsernameProjectBuildNumGet(username, project, buildNum)



Full details for a single build. The response includes all of the fields from the build summary. This is also the payload for the [notification webhooks](/docs/configuration/#notify), in which case this object is the value to a key named &#39;payload&#39;. 

### Example

```javascript
import CircleCiRestApi from 'circle_ci_rest_api';
let defaultClient = CircleCiRestApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new CircleCiRestApi.DefaultApi();
let username = "username_example"; // String | XXXXXXXXX 
let project = "project_example"; // String | XXXXXXXXX 
let buildNum = 56; // Number | XXXXXXXXXX 
apiInstance.projectUsernameProjectBuildNumGet(username, project, buildNum, (error, data, response) => {
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
 **username** | **String**| XXXXXXXXX  | 
 **project** | **String**| XXXXXXXXX  | 
 **buildNum** | **Number**| XXXXXXXXXX  | 

### Return type

[**BuildDetail**](BuildDetail.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectUsernameProjectBuildNumRetryPost

> Build projectUsernameProjectBuildNumRetryPost(username, project, buildNum)



Retries the build, returns a summary of the new build. 

### Example

```javascript
import CircleCiRestApi from 'circle_ci_rest_api';
let defaultClient = CircleCiRestApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new CircleCiRestApi.DefaultApi();
let username = "username_example"; // String | XXXXXXXXX 
let project = "project_example"; // String | XXXXXXXXX 
let buildNum = 56; // Number | XXXXXXXXXX 
apiInstance.projectUsernameProjectBuildNumRetryPost(username, project, buildNum, (error, data, response) => {
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
 **username** | **String**| XXXXXXXXX  | 
 **project** | **String**| XXXXXXXXX  | 
 **buildNum** | **Number**| XXXXXXXXXX  | 

### Return type

[**Build**](Build.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectUsernameProjectBuildNumTestsGet

> Tests projectUsernameProjectBuildNumTestsGet(username, project, buildNum)



Provides test metadata for a build Note: [Learn how to set up your builds to collect test metadata](https://circleci.com/docs/test-metadata/) 

### Example

```javascript
import CircleCiRestApi from 'circle_ci_rest_api';
let defaultClient = CircleCiRestApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new CircleCiRestApi.DefaultApi();
let username = "username_example"; // String | XXXXXXXXX 
let project = "project_example"; // String | XXXXXXXXX 
let buildNum = 56; // Number | XXXXXXXXXX 
apiInstance.projectUsernameProjectBuildNumTestsGet(username, project, buildNum, (error, data, response) => {
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
 **username** | **String**| XXXXXXXXX  | 
 **project** | **String**| XXXXXXXXX  | 
 **buildNum** | **Number**| XXXXXXXXXX  | 

### Return type

[**Tests**](Tests.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectUsernameProjectCheckoutKeyFingerprintDelete

> ProjectUsernameProjectCheckoutKeyFingerprintDelete200Response projectUsernameProjectCheckoutKeyFingerprintDelete(username, project, fingerprint)



Delete a checkout key. 

### Example

```javascript
import CircleCiRestApi from 'circle_ci_rest_api';
let defaultClient = CircleCiRestApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new CircleCiRestApi.DefaultApi();
let username = "username_example"; // String | XXXXXXXXX 
let project = "project_example"; // String | XXXXXXXXX 
let fingerprint = "fingerprint_example"; // String | XXXXXXXXXX 
apiInstance.projectUsernameProjectCheckoutKeyFingerprintDelete(username, project, fingerprint, (error, data, response) => {
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
 **username** | **String**| XXXXXXXXX  | 
 **project** | **String**| XXXXXXXXX  | 
 **fingerprint** | **String**| XXXXXXXXXX  | 

### Return type

[**ProjectUsernameProjectCheckoutKeyFingerprintDelete200Response**](ProjectUsernameProjectCheckoutKeyFingerprintDelete200Response.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectUsernameProjectCheckoutKeyFingerprintGet

> Key projectUsernameProjectCheckoutKeyFingerprintGet(username, project, fingerprint)



Get a checkout key. 

### Example

```javascript
import CircleCiRestApi from 'circle_ci_rest_api';
let defaultClient = CircleCiRestApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new CircleCiRestApi.DefaultApi();
let username = "username_example"; // String | XXXXXXXXX 
let project = "project_example"; // String | XXXXXXXXX 
let fingerprint = "fingerprint_example"; // String | XXXXXXXXXX 
apiInstance.projectUsernameProjectCheckoutKeyFingerprintGet(username, project, fingerprint, (error, data, response) => {
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
 **username** | **String**| XXXXXXXXX  | 
 **project** | **String**| XXXXXXXXX  | 
 **fingerprint** | **String**| XXXXXXXXXX  | 

### Return type

[**Key**](Key.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectUsernameProjectCheckoutKeyGet

> [Key] projectUsernameProjectCheckoutKeyGet(username, project)



Lists checkout keys. 

### Example

```javascript
import CircleCiRestApi from 'circle_ci_rest_api';
let defaultClient = CircleCiRestApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new CircleCiRestApi.DefaultApi();
let username = "username_example"; // String | XXXXXXXXX 
let project = "project_example"; // String | XXXXXXXXX 
apiInstance.projectUsernameProjectCheckoutKeyGet(username, project, (error, data, response) => {
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
 **username** | **String**| XXXXXXXXX  | 
 **project** | **String**| XXXXXXXXX  | 

### Return type

[**[Key]**](Key.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectUsernameProjectCheckoutKeyPost

> Key projectUsernameProjectCheckoutKeyPost(username, project, opts)



Creates a new checkout key. Only usable with a user API token. 

### Example

```javascript
import CircleCiRestApi from 'circle_ci_rest_api';
let defaultClient = CircleCiRestApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new CircleCiRestApi.DefaultApi();
let username = "username_example"; // String | XXXXXXXXX 
let project = "project_example"; // String | XXXXXXXXX 
let opts = {
  'body': "body_example" // String | The type of key to create. Can be 'deploy-key' or 'github-user-key'. 
};
apiInstance.projectUsernameProjectCheckoutKeyPost(username, project, opts, (error, data, response) => {
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
 **username** | **String**| XXXXXXXXX  | 
 **project** | **String**| XXXXXXXXX  | 
 **body** | **String**| The type of key to create. Can be &#39;deploy-key&#39; or &#39;github-user-key&#39;.  | [optional] 

### Return type

[**Key**](Key.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## projectUsernameProjectEnvvarGet

> [Envvar] projectUsernameProjectEnvvarGet(username, project)



Lists the environment variables for :project 

### Example

```javascript
import CircleCiRestApi from 'circle_ci_rest_api';
let defaultClient = CircleCiRestApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new CircleCiRestApi.DefaultApi();
let username = "username_example"; // String | XXXXXXXXX 
let project = "project_example"; // String | XXXXXXXXX 
apiInstance.projectUsernameProjectEnvvarGet(username, project, (error, data, response) => {
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
 **username** | **String**| XXXXXXXXX  | 
 **project** | **String**| XXXXXXXXX  | 

### Return type

[**[Envvar]**](Envvar.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectUsernameProjectEnvvarNameDelete

> ProjectUsernameProjectCheckoutKeyFingerprintDelete200Response projectUsernameProjectEnvvarNameDelete(username, project, name)



Deletes the environment variable named &#39;:name&#39; 

### Example

```javascript
import CircleCiRestApi from 'circle_ci_rest_api';
let defaultClient = CircleCiRestApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new CircleCiRestApi.DefaultApi();
let username = "username_example"; // String | XXXXXXXXX 
let project = "project_example"; // String | XXXXXXXXX 
let name = "name_example"; // String | XXXXXXXXXX 
apiInstance.projectUsernameProjectEnvvarNameDelete(username, project, name, (error, data, response) => {
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
 **username** | **String**| XXXXXXXXX  | 
 **project** | **String**| XXXXXXXXX  | 
 **name** | **String**| XXXXXXXXXX  | 

### Return type

[**ProjectUsernameProjectCheckoutKeyFingerprintDelete200Response**](ProjectUsernameProjectCheckoutKeyFingerprintDelete200Response.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectUsernameProjectEnvvarNameGet

> Envvar projectUsernameProjectEnvvarNameGet(username, project, name)



Gets the hidden value of environment variable :name 

### Example

```javascript
import CircleCiRestApi from 'circle_ci_rest_api';
let defaultClient = CircleCiRestApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new CircleCiRestApi.DefaultApi();
let username = "username_example"; // String | XXXXXXXXX 
let project = "project_example"; // String | XXXXXXXXX 
let name = "name_example"; // String | XXXXXXXXXX 
apiInstance.projectUsernameProjectEnvvarNameGet(username, project, name, (error, data, response) => {
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
 **username** | **String**| XXXXXXXXX  | 
 **project** | **String**| XXXXXXXXX  | 
 **name** | **String**| XXXXXXXXXX  | 

### Return type

[**Envvar**](Envvar.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectUsernameProjectEnvvarPost

> Envvar projectUsernameProjectEnvvarPost(username, project)



Creates a new environment variable 

### Example

```javascript
import CircleCiRestApi from 'circle_ci_rest_api';
let defaultClient = CircleCiRestApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new CircleCiRestApi.DefaultApi();
let username = "username_example"; // String | XXXXXXXXX 
let project = "project_example"; // String | XXXXXXXXX 
apiInstance.projectUsernameProjectEnvvarPost(username, project, (error, data, response) => {
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
 **username** | **String**| XXXXXXXXX  | 
 **project** | **String**| XXXXXXXXX  | 

### Return type

[**Envvar**](Envvar.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectUsernameProjectGet

> [Build] projectUsernameProjectGet(username, project, opts)



Build summary for each of the last 30 builds for a single git repo. 

### Example

```javascript
import CircleCiRestApi from 'circle_ci_rest_api';
let defaultClient = CircleCiRestApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new CircleCiRestApi.DefaultApi();
let username = "username_example"; // String | XXXXXXXXX 
let project = "project_example"; // String | XXXXXXXXX 
let opts = {
  'limit': 30, // Number | The number of builds to return. Maximum 100, defaults to 30. 
  'offset': 0, // Number | The API returns builds starting from this offset, defaults to 0. 
  'filter': "filter_example" // String | Restricts which builds are returned. Set to \"completed\", \"successful\", \"failed\", \"running\", or defaults to no filter. 
};
apiInstance.projectUsernameProjectGet(username, project, opts, (error, data, response) => {
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
 **username** | **String**| XXXXXXXXX  | 
 **project** | **String**| XXXXXXXXX  | 
 **limit** | **Number**| The number of builds to return. Maximum 100, defaults to 30.  | [optional] [default to 30]
 **offset** | **Number**| The API returns builds starting from this offset, defaults to 0.  | [optional] [default to 0]
 **filter** | **String**| Restricts which builds are returned. Set to \&quot;completed\&quot;, \&quot;successful\&quot;, \&quot;failed\&quot;, \&quot;running\&quot;, or defaults to no filter.  | [optional] 

### Return type

[**[Build]**](Build.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectUsernameProjectPost

> BuildSummary projectUsernameProjectPost(username, project, opts)



Triggers a new build, returns a summary of the build. 

### Example

```javascript
import CircleCiRestApi from 'circle_ci_rest_api';
let defaultClient = CircleCiRestApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new CircleCiRestApi.DefaultApi();
let username = "username_example"; // String | XXXXXXXXX 
let project = "project_example"; // String | XXXXXXXXX 
let opts = {
  'projectUsernameProjectPostRequest': new CircleCiRestApi.ProjectUsernameProjectPostRequest() // ProjectUsernameProjectPostRequest | 
};
apiInstance.projectUsernameProjectPost(username, project, opts, (error, data, response) => {
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
 **username** | **String**| XXXXXXXXX  | 
 **project** | **String**| XXXXXXXXX  | 
 **projectUsernameProjectPostRequest** | [**ProjectUsernameProjectPostRequest**](ProjectUsernameProjectPostRequest.md)|  | [optional] 

### Return type

[**BuildSummary**](BuildSummary.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## projectUsernameProjectSshKeyPost

> ProjectUsernameProjectSshKeyPostDefaultResponse projectUsernameProjectSshKeyPost(username, project, contentType, projectUsernameProjectSshKeyPostRequest)



Create an ssh key used to access external systems that require SSH key-based authentication 

### Example

```javascript
import CircleCiRestApi from 'circle_ci_rest_api';
let defaultClient = CircleCiRestApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new CircleCiRestApi.DefaultApi();
let username = "username_example"; // String | XXXXXXXXX 
let project = "project_example"; // String | XXXXXXXXX 
let contentType = "contentType_example"; // String | 
let projectUsernameProjectSshKeyPostRequest = new CircleCiRestApi.ProjectUsernameProjectSshKeyPostRequest(); // ProjectUsernameProjectSshKeyPostRequest | 
apiInstance.projectUsernameProjectSshKeyPost(username, project, contentType, projectUsernameProjectSshKeyPostRequest, (error, data, response) => {
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
 **username** | **String**| XXXXXXXXX  | 
 **project** | **String**| XXXXXXXXX  | 
 **contentType** | **String**|  | 
 **projectUsernameProjectSshKeyPostRequest** | [**ProjectUsernameProjectSshKeyPostRequest**](ProjectUsernameProjectSshKeyPostRequest.md)|  | 

### Return type

[**ProjectUsernameProjectSshKeyPostDefaultResponse**](ProjectUsernameProjectSshKeyPostDefaultResponse.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## projectUsernameProjectTreeBranchPost

> Build projectUsernameProjectTreeBranchPost(username, project, branch, opts)



Triggers a new build, returns a summary of the build. Optional build parameters can be set using an experimental API.  Note: For more about build parameters, read about [using parameterized builds](https://circleci.com/docs/parameterized-builds/) 

### Example

```javascript
import CircleCiRestApi from 'circle_ci_rest_api';
let defaultClient = CircleCiRestApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new CircleCiRestApi.DefaultApi();
let username = "username_example"; // String | XXXXXXXXX 
let project = "project_example"; // String | XXXXXXXXX 
let branch = "branch_example"; // String | The branch name should be url-encoded. 
let opts = {
  'projectUsernameProjectTreeBranchPostRequest': new CircleCiRestApi.ProjectUsernameProjectTreeBranchPostRequest() // ProjectUsernameProjectTreeBranchPostRequest | 
};
apiInstance.projectUsernameProjectTreeBranchPost(username, project, branch, opts, (error, data, response) => {
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
 **username** | **String**| XXXXXXXXX  | 
 **project** | **String**| XXXXXXXXX  | 
 **branch** | **String**| The branch name should be url-encoded.  | 
 **projectUsernameProjectTreeBranchPostRequest** | [**ProjectUsernameProjectTreeBranchPostRequest**](ProjectUsernameProjectTreeBranchPostRequest.md)|  | [optional] 

### Return type

[**Build**](Build.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## projectsGet

> [Project] projectsGet()



List of all the projects you&#39;re following on CircleCI, with build information organized by branch. 

### Example

```javascript
import CircleCiRestApi from 'circle_ci_rest_api';
let defaultClient = CircleCiRestApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new CircleCiRestApi.DefaultApi();
apiInstance.projectsGet((error, data, response) => {
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

[**[Project]**](Project.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## recentBuildsGet

> [Build] recentBuildsGet(opts)



Build summary for each of the last 30 recent builds, ordered by build_num. 

### Example

```javascript
import CircleCiRestApi from 'circle_ci_rest_api';
let defaultClient = CircleCiRestApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new CircleCiRestApi.DefaultApi();
let opts = {
  'limit': 30, // Number | The number of builds to return. Maximum 100, defaults to 30. 
  'offset': 0 // Number | The API returns builds starting from this offset, defaults to 0. 
};
apiInstance.recentBuildsGet(opts, (error, data, response) => {
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
 **limit** | **Number**| The number of builds to return. Maximum 100, defaults to 30.  | [optional] [default to 30]
 **offset** | **Number**| The API returns builds starting from this offset, defaults to 0.  | [optional] [default to 0]

### Return type

[**[Build]**](Build.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## userHerokuKeyPost

> userHerokuKeyPost()



Adds your Heroku API key to CircleCI, takes apikey as form param name. 

### Example

```javascript
import CircleCiRestApi from 'circle_ci_rest_api';
let defaultClient = CircleCiRestApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new CircleCiRestApi.DefaultApi();
apiInstance.userHerokuKeyPost((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

