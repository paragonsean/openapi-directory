# DvpDataApi.DiscoveryApi

All URIs are relative to *https://hub.docker.com/api/publisher/analytics/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getNamespace**](DiscoveryApi.md#getNamespace) | **GET** /namespaces/{namespace} | Get namespace
[**getNamespaces**](DiscoveryApi.md#getNamespaces) | **GET** / | Get namespaces and repos



## getNamespace

> NamespaceMetadata getNamespace(namespace)

Get namespace

Gets metadata associated with specified namespace, including extra repos associated with the namespace

### Example

```javascript
import DvpDataApi from 'dvp_data_api';
let defaultClient = DvpDataApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: HubAuth
let HubAuth = defaultClient.authentications['HubAuth'];
HubAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new DvpDataApi.DiscoveryApi();
let namespace = "namespace_example"; // String | Namespace to fetch data for
apiInstance.getNamespace(namespace, (error, data, response) => {
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
 **namespace** | **String**| Namespace to fetch data for | 

### Return type

[**NamespaceMetadata**](NamespaceMetadata.md)

### Authorization

[HubAuth](../README.md#HubAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNamespaces

> NamespaceData getNamespaces()

Get namespaces and repos

Gets a list of your namespaces and repos which have data available

### Example

```javascript
import DvpDataApi from 'dvp_data_api';
let defaultClient = DvpDataApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: HubAuth
let HubAuth = defaultClient.authentications['HubAuth'];
HubAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new DvpDataApi.DiscoveryApi();
apiInstance.getNamespaces((error, data, response) => {
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

[**NamespaceData**](NamespaceData.md)

### Authorization

[HubAuth](../README.md#HubAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

