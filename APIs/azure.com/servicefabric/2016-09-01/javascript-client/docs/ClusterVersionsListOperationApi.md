# ServiceFabricManagementClient.ClusterVersionsListOperationApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clusterVersionsListByVersion**](ClusterVersionsListOperationApi.md#clusterVersionsListByVersion) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.ServiceFabric/locations/{location}/clusterVersions/{clusterVersion} | 



## clusterVersionsListByVersion

> ClusterCodeVersionsListResult clusterVersionsListByVersion(location, apiVersion, subscriptionId, clusterVersion)



List cluster code versions by version

### Example

```javascript
import ServiceFabricManagementClient from 'service_fabric_management_client';
let defaultClient = ServiceFabricManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceFabricManagementClient.ClusterVersionsListOperationApi();
let location = "location_example"; // String | The location for the cluster code versions, this is different from cluster location
let apiVersion = "apiVersion_example"; // String | The version of the ServiceFabric resource provider api
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier
let clusterVersion = "clusterVersion_example"; // String | The cluster code version
apiInstance.clusterVersionsListByVersion(location, apiVersion, subscriptionId, clusterVersion, (error, data, response) => {
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
 **clusterVersion** | **String**| The cluster code version | 

### Return type

[**ClusterCodeVersionsListResult**](ClusterCodeVersionsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

