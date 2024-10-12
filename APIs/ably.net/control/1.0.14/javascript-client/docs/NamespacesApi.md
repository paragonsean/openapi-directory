# ControlApiV1.NamespacesApi

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

List the namespaces for the specified application ID.

### Example

```javascript
import ControlApiV1 from 'control_api_v1';
let defaultClient = ControlApiV1.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ControlApiV1.NamespacesApi();
let appId = "appId_example"; // String | The application ID.
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
 **appId** | **String**| The application ID. | 

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

Deletes the namespace with the specified ID, for the specified application ID.

### Example

```javascript
import ControlApiV1 from 'control_api_v1';
let defaultClient = ControlApiV1.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ControlApiV1.NamespacesApi();
let appId = "appId_example"; // String | The application ID.
let namespaceId = "namespaceId_example"; // String | The namespace ID.
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
 **appId** | **String**| The application ID. | 
 **namespaceId** | **String**| The namespace ID. | 

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

Updates the namespace with the specified ID, for the application with the specified application ID.

### Example

```javascript
import ControlApiV1 from 'control_api_v1';
let defaultClient = ControlApiV1.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ControlApiV1.NamespacesApi();
let appId = "appId_example"; // String | The application ID.
let namespaceId = "namespaceId_example"; // String | The namespace ID.
let opts = {
  'namespacePatch': new ControlApiV1.NamespacePatch() // NamespacePatch | 
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
 **appId** | **String**| The application ID. | 
 **namespaceId** | **String**| The namespace ID. | 
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

Creates a namespace for the specified application ID.

### Example

```javascript
import ControlApiV1 from 'control_api_v1';
let defaultClient = ControlApiV1.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ControlApiV1.NamespacesApi();
let appId = "appId_example"; // String | The application ID.
let opts = {
  'namespacePost': new ControlApiV1.NamespacePost() // NamespacePost | 
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
 **appId** | **String**| The application ID. | 
 **namespacePost** | [**NamespacePost**](NamespacePost.md)|  | [optional] 

### Return type

[**NamespaceResponse**](NamespaceResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

