# NetworkManagementClient.BastionHostsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bastionHostsCreateOrUpdate**](BastionHostsApi.md#bastionHostsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/bastionHosts/{bastionHostName} | 
[**bastionHostsDelete**](BastionHostsApi.md#bastionHostsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/bastionHosts/{bastionHostName} | 
[**bastionHostsGet**](BastionHostsApi.md#bastionHostsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/bastionHosts/{bastionHostName} | 
[**bastionHostsList**](BastionHostsApi.md#bastionHostsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Network/bastionHosts | 
[**bastionHostsListByResourceGroup**](BastionHostsApi.md#bastionHostsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/bastionHosts | 
[**bastionHostsUpdateTags**](BastionHostsApi.md#bastionHostsUpdateTags) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/bastionHosts/{bastionHostName} | 



## bastionHostsCreateOrUpdate

> BastionHost bastionHostsCreateOrUpdate(resourceGroupName, bastionHostName, apiVersion, subscriptionId, parameters)



Creates or updates the specified Bastion Host.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.BastionHostsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let bastionHostName = "bastionHostName_example"; // String | The name of the Bastion Host.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new NetworkManagementClient.BastionHost(); // BastionHost | Parameters supplied to the create or update Bastion Host operation.
apiInstance.bastionHostsCreateOrUpdate(resourceGroupName, bastionHostName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **bastionHostName** | **String**| The name of the Bastion Host. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**BastionHost**](BastionHost.md)| Parameters supplied to the create or update Bastion Host operation. | 

### Return type

[**BastionHost**](BastionHost.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## bastionHostsDelete

> bastionHostsDelete(resourceGroupName, bastionHostName, apiVersion, subscriptionId)



Deletes the specified Bastion Host.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.BastionHostsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let bastionHostName = "bastionHostName_example"; // String | The name of the Bastion Host.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.bastionHostsDelete(resourceGroupName, bastionHostName, apiVersion, subscriptionId, (error, data, response) => {
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
 **bastionHostName** | **String**| The name of the Bastion Host. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## bastionHostsGet

> BastionHost bastionHostsGet(resourceGroupName, bastionHostName, apiVersion, subscriptionId)



Gets the specified Bastion Host.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.BastionHostsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let bastionHostName = "bastionHostName_example"; // String | The name of the Bastion Host.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.bastionHostsGet(resourceGroupName, bastionHostName, apiVersion, subscriptionId, (error, data, response) => {
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
 **bastionHostName** | **String**| The name of the Bastion Host. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**BastionHost**](BastionHost.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## bastionHostsList

> BastionHostListResult bastionHostsList(apiVersion, subscriptionId)



Lists all Bastion Hosts in a subscription.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.BastionHostsApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.bastionHostsList(apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**BastionHostListResult**](BastionHostListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## bastionHostsListByResourceGroup

> BastionHostListResult bastionHostsListByResourceGroup(resourceGroupName, apiVersion, subscriptionId)



Lists all Bastion Hosts in a resource group.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.BastionHostsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.bastionHostsListByResourceGroup(resourceGroupName, apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**BastionHostListResult**](BastionHostListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## bastionHostsUpdateTags

> BastionHost bastionHostsUpdateTags(subscriptionId, resourceGroupName, bastionHostName, apiVersion, bastionHostParameters)



Updates bastion host tags.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.BastionHostsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name of the BastionHost.
let bastionHostName = "bastionHostName_example"; // String | The name of the bastionHost.
let apiVersion = "apiVersion_example"; // String | Client API version.
let bastionHostParameters = new NetworkManagementClient.BastionHostsUpdateTagsRequest(); // BastionHostsUpdateTagsRequest | Parameters supplied to update a bastion host tags.
apiInstance.bastionHostsUpdateTags(subscriptionId, resourceGroupName, bastionHostName, apiVersion, bastionHostParameters, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The resource group name of the BastionHost. | 
 **bastionHostName** | **String**| The name of the bastionHost. | 
 **apiVersion** | **String**| Client API version. | 
 **bastionHostParameters** | [**BastionHostsUpdateTagsRequest**](BastionHostsUpdateTagsRequest.md)| Parameters supplied to update a bastion host tags. | 

### Return type

[**BastionHost**](BastionHost.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

