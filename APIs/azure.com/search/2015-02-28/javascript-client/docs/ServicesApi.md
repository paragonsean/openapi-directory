# SearchManagementClient.ServicesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**servicesCreateOrUpdate**](ServicesApi.md#servicesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Search/searchServices/{serviceName} | 
[**servicesDelete**](ServicesApi.md#servicesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Search/searchServices/{serviceName} | 
[**servicesList**](ServicesApi.md#servicesList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Search/searchServices | 



## servicesCreateOrUpdate

> SearchServiceResource servicesCreateOrUpdate(resourceGroupName, serviceName, apiVersion, subscriptionId, parameters)



Creates or updates a Search service in the given resource group. If the Search service already exists, all properties will be updated with the given values.

### Example

```javascript
import SearchManagementClient from 'search_management_client';
let defaultClient = SearchManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SearchManagementClient.ServicesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the current subscription.
let serviceName = "serviceName_example"; // String | The name of the Search service to create or update.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new SearchManagementClient.SearchServiceCreateOrUpdateParameters(); // SearchServiceCreateOrUpdateParameters | The properties to set or update on the Search service.
apiInstance.servicesCreateOrUpdate(resourceGroupName, serviceName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group within the current subscription. | 
 **serviceName** | **String**| The name of the Search service to create or update. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**SearchServiceCreateOrUpdateParameters**](SearchServiceCreateOrUpdateParameters.md)| The properties to set or update on the Search service. | 

### Return type

[**SearchServiceResource**](SearchServiceResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## servicesDelete

> servicesDelete(resourceGroupName, serviceName, apiVersion, subscriptionId)



Deletes a Search service in the given resource group, along with its associated resources.

### Example

```javascript
import SearchManagementClient from 'search_management_client';
let defaultClient = SearchManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SearchManagementClient.ServicesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the current subscription.
let serviceName = "serviceName_example"; // String | The name of the Search service to delete.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.servicesDelete(resourceGroupName, serviceName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group within the current subscription. | 
 **serviceName** | **String**| The name of the Search service to delete. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## servicesList

> SearchServiceListResult servicesList(resourceGroupName, apiVersion, subscriptionId)



Returns a list of all Search services in the given resource group.

### Example

```javascript
import SearchManagementClient from 'search_management_client';
let defaultClient = SearchManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SearchManagementClient.ServicesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the current subscription.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.servicesList(resourceGroupName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group within the current subscription. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**SearchServiceListResult**](SearchServiceListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

