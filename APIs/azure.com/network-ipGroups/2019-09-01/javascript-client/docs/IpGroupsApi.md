# NetworkManagementClient.IpGroupsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ipGroupsCreateOrUpdate**](IpGroupsApi.md#ipGroupsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/ipGroups/{ipGroupsName} | 
[**ipGroupsDelete**](IpGroupsApi.md#ipGroupsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/ipGroups/{ipGroupsName} | 
[**ipGroupsGet**](IpGroupsApi.md#ipGroupsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/ipGroups/{ipGroupsName} | 
[**ipGroupsList**](IpGroupsApi.md#ipGroupsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Network/ipGroups | 
[**ipGroupsListByResourceGroup**](IpGroupsApi.md#ipGroupsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/ipGroups | 
[**ipGroupsUpdateGroups**](IpGroupsApi.md#ipGroupsUpdateGroups) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/ipGroups/{ipGroupsName} | 



## ipGroupsCreateOrUpdate

> IpGroup ipGroupsCreateOrUpdate(resourceGroupName, ipGroupsName, apiVersion, subscriptionId, parameters)



Creates or updates an ipGroups in a specified resource group.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.IpGroupsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let ipGroupsName = "ipGroupsName_example"; // String | The name of the ipGroups.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new NetworkManagementClient.IpGroup(); // IpGroup | Parameters supplied to the create or update IpGroups operation.
apiInstance.ipGroupsCreateOrUpdate(resourceGroupName, ipGroupsName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **ipGroupsName** | **String**| The name of the ipGroups. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**IpGroup**](IpGroup.md)| Parameters supplied to the create or update IpGroups operation. | 

### Return type

[**IpGroup**](IpGroup.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## ipGroupsDelete

> ipGroupsDelete(resourceGroupName, ipGroupsName, apiVersion, subscriptionId)



Deletes the specified ipGroups.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.IpGroupsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let ipGroupsName = "ipGroupsName_example"; // String | The name of the ipGroups.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.ipGroupsDelete(resourceGroupName, ipGroupsName, apiVersion, subscriptionId, (error, data, response) => {
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
 **ipGroupsName** | **String**| The name of the ipGroups. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ipGroupsGet

> IpGroup ipGroupsGet(resourceGroupName, ipGroupsName, apiVersion, subscriptionId, opts)



Gets the specified ipGroups.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.IpGroupsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let ipGroupsName = "ipGroupsName_example"; // String | The name of the ipGroups.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let opts = {
  'expand': "expand_example" // String | Expands resourceIds (of Firewalls/Network Security Groups etc.) back referenced by the IpGroups resource.
};
apiInstance.ipGroupsGet(resourceGroupName, ipGroupsName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **ipGroupsName** | **String**| The name of the ipGroups. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **expand** | **String**| Expands resourceIds (of Firewalls/Network Security Groups etc.) back referenced by the IpGroups resource. | [optional] 

### Return type

[**IpGroup**](IpGroup.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ipGroupsList

> IpGroupListResult ipGroupsList(apiVersion, subscriptionId)



Gets all IpGroups in a subscription.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.IpGroupsApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.ipGroupsList(apiVersion, subscriptionId, (error, data, response) => {
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

[**IpGroupListResult**](IpGroupListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ipGroupsListByResourceGroup

> IpGroupListResult ipGroupsListByResourceGroup(resourceGroupName, apiVersion, subscriptionId)



Gets all IpGroups in a resource group.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.IpGroupsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.ipGroupsListByResourceGroup(resourceGroupName, apiVersion, subscriptionId, (error, data, response) => {
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

[**IpGroupListResult**](IpGroupListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ipGroupsUpdateGroups

> IpGroup ipGroupsUpdateGroups(resourceGroupName, ipGroupsName, apiVersion, subscriptionId, parameters)



Updates tags of an IpGroups resource.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.IpGroupsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let ipGroupsName = "ipGroupsName_example"; // String | The name of the ipGroups.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new NetworkManagementClient.IpGroupsUpdateGroupsRequest(); // IpGroupsUpdateGroupsRequest | Parameters supplied to the update ipGroups operation.
apiInstance.ipGroupsUpdateGroups(resourceGroupName, ipGroupsName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **ipGroupsName** | **String**| The name of the ipGroups. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**IpGroupsUpdateGroupsRequest**](IpGroupsUpdateGroupsRequest.md)| Parameters supplied to the update ipGroups operation. | 

### Return type

[**IpGroup**](IpGroup.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

