# DockerHubApi.AccessTokensApi

All URIs are relative to *https://hub.docker.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2AccessTokensGet**](AccessTokensApi.md#v2AccessTokensGet) | **GET** /v2/access-tokens | Get a list of personal access tokens
[**v2AccessTokensPost**](AccessTokensApi.md#v2AccessTokensPost) | **POST** /v2/access-tokens | Create a personal access token
[**v2AccessTokensUuidDelete**](AccessTokensApi.md#v2AccessTokensUuidDelete) | **DELETE** /v2/access-tokens/{uuid} | Delete a personal access token
[**v2AccessTokensUuidGet**](AccessTokensApi.md#v2AccessTokensUuidGet) | **GET** /v2/access-tokens/{uuid} | Get a personal access token
[**v2AccessTokensUuidPatch**](AccessTokensApi.md#v2AccessTokensUuidPatch) | **PATCH** /v2/access-tokens/{uuid} | Update a personal access token



## v2AccessTokensGet

> GetAccessTokensResponse v2AccessTokensGet(opts)

Get a list of personal access tokens

Returns a paginated list of personal access tokens.

### Example

```javascript
import DockerHubApi from 'docker_hub_api';

let apiInstance = new DockerHubApi.AccessTokensApi();
let opts = {
  'page': 1, // Number | 
  'pageSize': 10 // Number | 
};
apiInstance.v2AccessTokensGet(opts, (error, data, response) => {
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
 **page** | **Number**|  | [optional] [default to 1]
 **pageSize** | **Number**|  | [optional] [default to 10]

### Return type

[**GetAccessTokensResponse**](GetAccessTokensResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## v2AccessTokensPost

> AccessToken v2AccessTokensPost(createAccessTokenRequest)

Create a personal access token

Creates and returns a personal access token.

### Example

```javascript
import DockerHubApi from 'docker_hub_api';

let apiInstance = new DockerHubApi.AccessTokensApi();
let createAccessTokenRequest = new DockerHubApi.CreateAccessTokenRequest(); // CreateAccessTokenRequest | 
apiInstance.v2AccessTokensPost(createAccessTokenRequest, (error, data, response) => {
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
 **createAccessTokenRequest** | [**CreateAccessTokenRequest**](CreateAccessTokenRequest.md)|  | 

### Return type

[**AccessToken**](AccessToken.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## v2AccessTokensUuidDelete

> v2AccessTokensUuidDelete(uuid)

Delete a personal access token

Deletes a personal access token permanently. This cannot be undone. 

### Example

```javascript
import DockerHubApi from 'docker_hub_api';

let apiInstance = new DockerHubApi.AccessTokensApi();
let uuid = "uuid_example"; // String | 
apiInstance.v2AccessTokensUuidDelete(uuid, (error, data, response) => {
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
 **uuid** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## v2AccessTokensUuidGet

> V2AccessTokensUuidGet200Response v2AccessTokensUuidGet(uuid)

Get a personal access token

Returns a personal access token by UUID.

### Example

```javascript
import DockerHubApi from 'docker_hub_api';

let apiInstance = new DockerHubApi.AccessTokensApi();
let uuid = "uuid_example"; // String | 
apiInstance.v2AccessTokensUuidGet(uuid, (error, data, response) => {
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
 **uuid** | **String**|  | 

### Return type

[**V2AccessTokensUuidGet200Response**](V2AccessTokensUuidGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## v2AccessTokensUuidPatch

> AccessToken v2AccessTokensUuidPatch(uuid, patchAccessTokenRequest)

Update a personal access token

Updates a personal access token partially. You can either update the token&#39;s label or enable/disable it. 

### Example

```javascript
import DockerHubApi from 'docker_hub_api';

let apiInstance = new DockerHubApi.AccessTokensApi();
let uuid = "uuid_example"; // String | 
let patchAccessTokenRequest = new DockerHubApi.PatchAccessTokenRequest(); // PatchAccessTokenRequest | 
apiInstance.v2AccessTokensUuidPatch(uuid, patchAccessTokenRequest, (error, data, response) => {
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
 **uuid** | **String**|  | 
 **patchAccessTokenRequest** | [**PatchAccessTokenRequest**](PatchAccessTokenRequest.md)|  | 

### Return type

[**AccessToken**](AccessToken.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

