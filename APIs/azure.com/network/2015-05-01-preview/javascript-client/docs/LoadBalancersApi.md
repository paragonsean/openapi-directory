# NetworkResourceProviderClient.LoadBalancersApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**loadBalancersCreateOrUpdate**](LoadBalancersApi.md#loadBalancersCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/loadBalancers/{loadBalancerName} | 
[**loadBalancersDelete**](LoadBalancersApi.md#loadBalancersDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/loadBalancers/{loadBalancerName} | 
[**loadBalancersGet**](LoadBalancersApi.md#loadBalancersGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/loadBalancers/{loadBalancerName} | 
[**loadBalancersList**](LoadBalancersApi.md#loadBalancersList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/loadBalancers | 
[**loadBalancersListAll**](LoadBalancersApi.md#loadBalancersListAll) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Network/loadBalancers | 



## loadBalancersCreateOrUpdate

> LoadBalancer loadBalancersCreateOrUpdate(resourceGroupName, loadBalancerName, apiVersion, subscriptionId, parameters)



The Put LoadBalancer operation creates/updates a LoadBalancer

### Example

```javascript
import NetworkResourceProviderClient from 'network_resource_provider_client';
let defaultClient = NetworkResourceProviderClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkResourceProviderClient.LoadBalancersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let loadBalancerName = "loadBalancerName_example"; // String | The name of the loadBalancer.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new NetworkResourceProviderClient.LoadBalancer(); // LoadBalancer | Parameters supplied to the create/delete LoadBalancer operation
apiInstance.loadBalancersCreateOrUpdate(resourceGroupName, loadBalancerName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **loadBalancerName** | **String**| The name of the loadBalancer. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**LoadBalancer**](LoadBalancer.md)| Parameters supplied to the create/delete LoadBalancer operation | 

### Return type

[**LoadBalancer**](LoadBalancer.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## loadBalancersDelete

> loadBalancersDelete(resourceGroupName, loadBalancerName, apiVersion, subscriptionId)



The delete loadbalancer operation deletes the specified loadbalancer.

### Example

```javascript
import NetworkResourceProviderClient from 'network_resource_provider_client';
let defaultClient = NetworkResourceProviderClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkResourceProviderClient.LoadBalancersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let loadBalancerName = "loadBalancerName_example"; // String | The name of the loadBalancer.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.loadBalancersDelete(resourceGroupName, loadBalancerName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **loadBalancerName** | **String**| The name of the loadBalancer. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## loadBalancersGet

> LoadBalancer loadBalancersGet(resourceGroupName, loadBalancerName, apiVersion, subscriptionId)



The Get network interface operation retrieves information about the specified network interface.

### Example

```javascript
import NetworkResourceProviderClient from 'network_resource_provider_client';
let defaultClient = NetworkResourceProviderClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkResourceProviderClient.LoadBalancersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let loadBalancerName = "loadBalancerName_example"; // String | The name of the loadBalancer.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.loadBalancersGet(resourceGroupName, loadBalancerName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **loadBalancerName** | **String**| The name of the loadBalancer. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**LoadBalancer**](LoadBalancer.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## loadBalancersList

> LoadBalancerListResult loadBalancersList(resourceGroupName, apiVersion, subscriptionId)



The List loadBalancer operation retrieves all the load balancers in a resource group.

### Example

```javascript
import NetworkResourceProviderClient from 'network_resource_provider_client';
let defaultClient = NetworkResourceProviderClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkResourceProviderClient.LoadBalancersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.loadBalancersList(resourceGroupName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**LoadBalancerListResult**](LoadBalancerListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## loadBalancersListAll

> LoadBalancerListResult loadBalancersListAll(apiVersion, subscriptionId)



The List loadBalancer operation retrieves all the load balancers in a subscription.

### Example

```javascript
import NetworkResourceProviderClient from 'network_resource_provider_client';
let defaultClient = NetworkResourceProviderClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkResourceProviderClient.LoadBalancersApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.loadBalancersListAll(apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**LoadBalancerListResult**](LoadBalancerListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

