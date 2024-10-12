# ApiV1.NamespacesApi

All URIs are relative to *https://control.ably.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**appsAppIdNamespacesGet**](NamespacesApi.md#appsAppIdNamespacesGet) | **GET** /apps/{app_id}/namespaces | Lists namespaces
[**appsAppIdNamespacesNamespaceIdDelete**](NamespacesApi.md#appsAppIdNamespacesNamespaceIdDelete) | **DELETE** /apps/{app_id}/namespaces/{namespace_id} | Deletes a namespace
[**appsAppIdNamespacesNamespaceIdPatch**](NamespacesApi.md#appsAppIdNamespacesNamespaceIdPatch) | **PATCH** /apps/{app_id}/namespaces/{namespace_id} | Updates a namespace
[**appsAppIdNamespacesPost**](NamespacesApi.md#appsAppIdNamespacesPost) | **POST** /apps/{app_id}/namespaces | Creates a namespace



## appsAppIdNamespacesGet

> [NamespaceResponse] appsAppIdNamespacesGet(appId)

Lists namespaces

### Example

```javascript
import ApiV1 from 'api_v1';
let defaultClient = ApiV1.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ApiV1.NamespacesApi();
let appId = "appId_example"; // String | 
apiInstance.appsAppIdNamespacesGet(appId, (error, data, response) => {
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
 **appId** | **String**|  | 

### Return type

[**[NamespaceResponse]**](NamespaceResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsAppIdNamespacesNamespaceIdDelete

> appsAppIdNamespacesNamespaceIdDelete(appId, namespaceId)

Deletes a namespace

### Example

```javascript
import ApiV1 from 'api_v1';
let defaultClient = ApiV1.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ApiV1.NamespacesApi();
let appId = "appId_example"; // String | 
let namespaceId = "namespaceId_example"; // String | 
apiInstance.appsAppIdNamespacesNamespaceIdDelete(appId, namespaceId, (error, data, response) => {
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
 **appId** | **String**|  | 
 **namespaceId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsAppIdNamespacesNamespaceIdPatch

> NamespaceResponse appsAppIdNamespacesNamespaceIdPatch(appId, namespaceId, opts)

Updates a namespace

### Example

```javascript
import ApiV1 from 'api_v1';
let defaultClient = ApiV1.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ApiV1.NamespacesApi();
let appId = "appId_example"; // String | 
let namespaceId = "namespaceId_example"; // String | 
let opts = {
  'namespacePatch': new ApiV1.NamespacePatch() // NamespacePatch | 
};
apiInstance.appsAppIdNamespacesNamespaceIdPatch(appId, namespaceId, opts, (error, data, response) => {
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
 **appId** | **String**|  | 
 **namespaceId** | **String**|  | 
 **namespacePatch** | [**NamespacePatch**](NamespacePatch.md)|  | [optional] 

### Return type

[**NamespaceResponse**](NamespaceResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## appsAppIdNamespacesPost

> NamespaceResponse appsAppIdNamespacesPost(appId, opts)

Creates a namespace

### Example

```javascript
import ApiV1 from 'api_v1';
let defaultClient = ApiV1.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ApiV1.NamespacesApi();
let appId = "appId_example"; // String | 
let opts = {
  'namespacePost': new ApiV1.NamespacePost() // NamespacePost | 
};
apiInstance.appsAppIdNamespacesPost(appId, opts, (error, data, response) => {
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
 **appId** | **String**|  | 
 **namespacePost** | [**NamespacePost**](NamespacePost.md)|  | [optional] 

### Return type

[**NamespaceResponse**](NamespaceResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

