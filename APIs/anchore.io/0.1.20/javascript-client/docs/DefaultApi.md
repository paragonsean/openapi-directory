# AnchoreEngineApiServer.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getOauthToken**](DefaultApi.md#getOauthToken) | **POST** /oauth/token | 
[**healthCheck**](DefaultApi.md#healthCheck) | **GET** /health | 
[**listFileContentSearchResults**](DefaultApi.md#listFileContentSearchResults) | **GET** /images/{imageDigest}/artifacts/file_content_search | Return a list of analyzer artifacts of the specified type
[**listRetrievedFiles**](DefaultApi.md#listRetrievedFiles) | **GET** /images/{imageDigest}/artifacts/retrieved_files | Return a list of analyzer artifacts of the specified type
[**listSecretSearchResults**](DefaultApi.md#listSecretSearchResults) | **GET** /images/{imageDigest}/artifacts/secret_search | Return a list of analyzer artifacts of the specified type
[**ping**](DefaultApi.md#ping) | **GET** / | 
[**versionCheck**](DefaultApi.md#versionCheck) | **GET** /version | 



## getOauthToken

> TokenResponse getOauthToken(opts)



Request a jwt token for subsequent operations, this request is authenticated with normal HTTP auth

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.DefaultApi();
let opts = {
  'clientId': "'anonymous'", // String | The type of client used for the OAuth token
  'grantType': "'password'", // String | OAuth Grant type for token
  'password': "password_example", // String | Password for corresponding user
  'username': "username_example" // String | User to assign OAuth token to
};
apiInstance.getOauthToken(opts, (error, data, response) => {
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
 **clientId** | **String**| The type of client used for the OAuth token | [optional] [default to &#39;anonymous&#39;]
 **grantType** | **String**| OAuth Grant type for token | [optional] [default to &#39;password&#39;]
 **password** | **String**| Password for corresponding user | [optional] 
 **username** | **String**| User to assign OAuth token to | [optional] 

### Return type

[**TokenResponse**](TokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## healthCheck

> healthCheck()



Health check, returns 200 and no body if service is running

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.DefaultApi();
apiInstance.healthCheck((error, data, response) => {
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## listFileContentSearchResults

> [FileContentSearchResult] listFileContentSearchResults(imageDigest)

Return a list of analyzer artifacts of the specified type

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.DefaultApi();
let imageDigest = "imageDigest_example"; // String | 
apiInstance.listFileContentSearchResults(imageDigest, (error, data, response) => {
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
 **imageDigest** | **String**|  | 

### Return type

[**[FileContentSearchResult]**](FileContentSearchResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listRetrievedFiles

> [RetrievedFile] listRetrievedFiles(imageDigest)

Return a list of analyzer artifacts of the specified type

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.DefaultApi();
let imageDigest = "imageDigest_example"; // String | 
apiInstance.listRetrievedFiles(imageDigest, (error, data, response) => {
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
 **imageDigest** | **String**|  | 

### Return type

[**[RetrievedFile]**](RetrievedFile.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSecretSearchResults

> [SecretSearchResult] listSecretSearchResults(imageDigest)

Return a list of analyzer artifacts of the specified type

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.DefaultApi();
let imageDigest = "imageDigest_example"; // String | 
apiInstance.listSecretSearchResults(imageDigest, (error, data, response) => {
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
 **imageDigest** | **String**|  | 

### Return type

[**[SecretSearchResult]**](SecretSearchResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ping

> String ping()



Simple status check

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.DefaultApi();
apiInstance.ping((error, data, response) => {
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

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## versionCheck

> ServiceVersion versionCheck()



Returns the version object for the service, including db schema version info

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.DefaultApi();
apiInstance.versionCheck((error, data, response) => {
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

[**ServiceVersion**](ServiceVersion.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

