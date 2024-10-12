# ServiceFabricManagementClient.ClusterVersionApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clusterVersionsGet**](ClusterVersionApi.md#clusterVersionsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.ServiceFabric/locations/{location}/environments/{environment}/clusterVersions/{clusterVersion} | 
[**clusterVersionsList**](ClusterVersionApi.md#clusterVersionsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.ServiceFabric/locations/{location}/clusterVersions | 
[**clusterVersionsListByEnvironment**](ClusterVersionApi.md#clusterVersionsListByEnvironment) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.ServiceFabric/locations/{location}/environments/{environment}/clusterVersions | 



## clusterVersionsGet

> ClusterCodeVersionsResult clusterVersionsGet(location, environment, apiVersion, subscriptionId, clusterVersion)



Get cluster code versions by environment and version

### Example

```javascript
import ServiceFabricManagementClient from 'service_fabric_management_client';
let defaultClient = ServiceFabricManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceFabricManagementClient.ClusterVersionApi();
let location = "location_example"; // String | The location for the cluster code versions, this is different from cluster location
let environment = "environment_example"; // String | Cluster operating system, the default means all
let apiVersion = "apiVersion_example"; // String | The version of the ServiceFabric resource provider api
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier
let clusterVersion = "clusterVersion_example"; // String | The cluster code version
apiInstance.clusterVersionsGet(location, environment, apiVersion, subscriptionId, clusterVersion, (error, data, response) => {
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
 **location** | **String**| The location for the cluster code versions, this is different from cluster location | 
 **environment** | **String**| Cluster operating system, the default means all | 
 **apiVersion** | **String**| The version of the ServiceFabric resource provider api | 
 **subscriptionId** | **String**| The customer subscription identifier | 
 **clusterVersion** | **String**| The cluster code version | 

### Return type

[**ClusterCodeVersionsResult**](ClusterCodeVersionsResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## clusterVersionsList

> ClusterCodeVersionsListResult clusterVersionsList(location, apiVersion, subscriptionId)



List cluster code versions by location

### Example

```javascript
import ServiceFabricManagementClient from 'service_fabric_management_client';
let defaultClient = ServiceFabricManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceFabricManagementClient.ClusterVersionApi();
let location = "location_example"; // String | The location for the cluster code versions, this is different from cluster location
let apiVersion = "apiVersion_example"; // String | The version of the ServiceFabric resource provider api
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier
apiInstance.clusterVersionsList(location, apiVersion, subscriptionId, (error, data, response) => {
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
 **location** | **String**| The location for the cluster code versions, this is different from cluster location | 
 **apiVersion** | **String**| The version of the ServiceFabric resource provider api | 
 **subscriptionId** | **String**| The customer subscription identifier | 

### Return type

[**ClusterCodeVersionsListResult**](ClusterCodeVersionsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## clusterVersionsListByEnvironment

> ClusterCodeVersionsListResult clusterVersionsListByEnvironment(location, environment, apiVersion, subscriptionId)



List cluster code versions by environment

### Example

```javascript
import ServiceFabricManagementClient from 'service_fabric_management_client';
let defaultClient = ServiceFabricManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceFabricManagementClient.ClusterVersionApi();
let location = "location_example"; // String | The location for the cluster code versions, this is different from cluster location
let environment = "environment_example"; // String | Cluster operating system, the default means all
let apiVersion = "apiVersion_example"; // String | The version of the ServiceFabric resource provider api
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier
apiInstance.clusterVersionsListByEnvironment(location, environment, apiVersion, subscriptionId, (error, data, response) => {
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
 **location** | **String**| The location for the cluster code versions, this is different from cluster location | 
 **environment** | **String**| Cluster operating system, the default means all | 
 **apiVersion** | **String**| The version of the ServiceFabric resource provider api | 
 **subscriptionId** | **String**| The customer subscription identifier | 

### Return type

[**ClusterCodeVersionsListResult**](ClusterCodeVersionsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

