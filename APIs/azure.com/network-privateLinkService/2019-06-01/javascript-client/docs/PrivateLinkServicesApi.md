# NetworkManagementClient.PrivateLinkServicesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**privateLinkServicesCheckPrivateLinkServiceVisibility**](PrivateLinkServicesApi.md#privateLinkServicesCheckPrivateLinkServiceVisibility) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Network/locations/{location}/checkPrivateLinkServiceVisibility | 
[**privateLinkServicesCheckPrivateLinkServiceVisibilityByResourceGroup**](PrivateLinkServicesApi.md#privateLinkServicesCheckPrivateLinkServiceVisibilityByResourceGroup) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/locations/{location}/checkPrivateLinkServiceVisibility | 
[**privateLinkServicesDelete**](PrivateLinkServicesApi.md#privateLinkServicesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateLinkServices/{serviceName} | 
[**privateLinkServicesDeletePrivateEndpointConnection**](PrivateLinkServicesApi.md#privateLinkServicesDeletePrivateEndpointConnection) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateLinkServices/{serviceName}/privateEndpointConnections/{peConnectionName} | 
[**privateLinkServicesGet**](PrivateLinkServicesApi.md#privateLinkServicesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateLinkServices/{serviceName} | 
[**privateLinkServicesList**](PrivateLinkServicesApi.md#privateLinkServicesList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateLinkServices | 
[**privateLinkServicesListAutoApprovedPrivateLinkServices**](PrivateLinkServicesApi.md#privateLinkServicesListAutoApprovedPrivateLinkServices) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Network/locations/{location}/autoApprovedPrivateLinkServices | 
[**privateLinkServicesListAutoApprovedPrivateLinkServicesByResourceGroup**](PrivateLinkServicesApi.md#privateLinkServicesListAutoApprovedPrivateLinkServicesByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/locations/{location}/autoApprovedPrivateLinkServices | 
[**privateLinkServicesListBySubscription**](PrivateLinkServicesApi.md#privateLinkServicesListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Network/privateLinkServices | 
[**privateLinkServicesUpdatePrivateEndpointConnection**](PrivateLinkServicesApi.md#privateLinkServicesUpdatePrivateEndpointConnection) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateLinkServices/{serviceName}/privateEndpointConnections/{peConnectionName} | 



## privateLinkServicesCheckPrivateLinkServiceVisibility

> PrivateLinkServiceVisibility privateLinkServicesCheckPrivateLinkServiceVisibility(location, apiVersion, subscriptionId, parameters)



Checks the subscription is visible to private link service

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.PrivateLinkServicesApi();
let location = "location_example"; // String | The location of the domain name.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new NetworkManagementClient.CheckPrivateLinkServiceVisibilityRequest(); // CheckPrivateLinkServiceVisibilityRequest | The request body of CheckPrivateLinkService API call.
apiInstance.privateLinkServicesCheckPrivateLinkServiceVisibility(location, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **location** | **String**| The location of the domain name. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**CheckPrivateLinkServiceVisibilityRequest**](CheckPrivateLinkServiceVisibilityRequest.md)| The request body of CheckPrivateLinkService API call. | 

### Return type

[**PrivateLinkServiceVisibility**](PrivateLinkServiceVisibility.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## privateLinkServicesCheckPrivateLinkServiceVisibilityByResourceGroup

> PrivateLinkServiceVisibility privateLinkServicesCheckPrivateLinkServiceVisibilityByResourceGroup(location, resourceGroupName, apiVersion, subscriptionId, parameters)



Checks the subscription is visible to private link service

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.PrivateLinkServicesApi();
let location = "location_example"; // String | The location of the domain name.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new NetworkManagementClient.CheckPrivateLinkServiceVisibilityRequest(); // CheckPrivateLinkServiceVisibilityRequest | The request body of CheckPrivateLinkService API call.
apiInstance.privateLinkServicesCheckPrivateLinkServiceVisibilityByResourceGroup(location, resourceGroupName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **location** | **String**| The location of the domain name. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**CheckPrivateLinkServiceVisibilityRequest**](CheckPrivateLinkServiceVisibilityRequest.md)| The request body of CheckPrivateLinkService API call. | 

### Return type

[**PrivateLinkServiceVisibility**](PrivateLinkServiceVisibility.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## privateLinkServicesDelete

> privateLinkServicesDelete(resourceGroupName, serviceName, apiVersion, subscriptionId)



Deletes the specified private link service.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.PrivateLinkServicesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let serviceName = "serviceName_example"; // String | The name of the private link service.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.privateLinkServicesDelete(resourceGroupName, serviceName, apiVersion, subscriptionId, (error, data, response) => {
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
 **serviceName** | **String**| The name of the private link service. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateLinkServicesDeletePrivateEndpointConnection

> privateLinkServicesDeletePrivateEndpointConnection(resourceGroupName, serviceName, peConnectionName, apiVersion, subscriptionId)



Delete private end point connection for a private link service in a subscription.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.PrivateLinkServicesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let serviceName = "serviceName_example"; // String | The name of the private link service.
let peConnectionName = "peConnectionName_example"; // String | The name of the private end point connection.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.privateLinkServicesDeletePrivateEndpointConnection(resourceGroupName, serviceName, peConnectionName, apiVersion, subscriptionId, (error, data, response) => {
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
 **serviceName** | **String**| The name of the private link service. | 
 **peConnectionName** | **String**| The name of the private end point connection. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateLinkServicesGet

> PrivateLinkService privateLinkServicesGet(resourceGroupName, serviceName, apiVersion, subscriptionId, opts)



Gets the specified private link service by resource group.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.PrivateLinkServicesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let serviceName = "serviceName_example"; // String | The name of the private link service.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let opts = {
  'expand': "expand_example" // String | Expands referenced resources.
};
apiInstance.privateLinkServicesGet(resourceGroupName, serviceName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **serviceName** | **String**| The name of the private link service. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **expand** | **String**| Expands referenced resources. | [optional] 

### Return type

[**PrivateLinkService**](PrivateLinkService.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateLinkServicesList

> PrivateLinkServiceListResult privateLinkServicesList(resourceGroupName, apiVersion, subscriptionId)



Gets all private link services in a resource group.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.PrivateLinkServicesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.privateLinkServicesList(resourceGroupName, apiVersion, subscriptionId, (error, data, response) => {
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

[**PrivateLinkServiceListResult**](PrivateLinkServiceListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateLinkServicesListAutoApprovedPrivateLinkServices

> AutoApprovedPrivateLinkServicesResult privateLinkServicesListAutoApprovedPrivateLinkServices(location, apiVersion, subscriptionId)



Returns all of the private link service ids that can be linked to a Private Endpoint with auto approved in this subscription in this region.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.PrivateLinkServicesApi();
let location = "location_example"; // String | The location of the domain name.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.privateLinkServicesListAutoApprovedPrivateLinkServices(location, apiVersion, subscriptionId, (error, data, response) => {
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
 **location** | **String**| The location of the domain name. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**AutoApprovedPrivateLinkServicesResult**](AutoApprovedPrivateLinkServicesResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateLinkServicesListAutoApprovedPrivateLinkServicesByResourceGroup

> AutoApprovedPrivateLinkServicesResult privateLinkServicesListAutoApprovedPrivateLinkServicesByResourceGroup(location, resourceGroupName, apiVersion, subscriptionId)



Returns all of the private link service ids that can be linked to a Private Endpoint with auto approved in this subscription in this region.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.PrivateLinkServicesApi();
let location = "location_example"; // String | The location of the domain name.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.privateLinkServicesListAutoApprovedPrivateLinkServicesByResourceGroup(location, resourceGroupName, apiVersion, subscriptionId, (error, data, response) => {
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
 **location** | **String**| The location of the domain name. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**AutoApprovedPrivateLinkServicesResult**](AutoApprovedPrivateLinkServicesResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateLinkServicesListBySubscription

> PrivateLinkServiceListResult privateLinkServicesListBySubscription(apiVersion, subscriptionId)



Gets all private link service in a subscription.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.PrivateLinkServicesApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.privateLinkServicesListBySubscription(apiVersion, subscriptionId, (error, data, response) => {
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

[**PrivateLinkServiceListResult**](PrivateLinkServiceListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateLinkServicesUpdatePrivateEndpointConnection

> PrivateEndpointConnection privateLinkServicesUpdatePrivateEndpointConnection(resourceGroupName, serviceName, peConnectionName, apiVersion, subscriptionId, parameters)



Approve or reject private end point connection for a private link service in a subscription.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.PrivateLinkServicesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let serviceName = "serviceName_example"; // String | The name of the private link service.
let peConnectionName = "peConnectionName_example"; // String | The name of the private end point connection.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new NetworkManagementClient.PrivateEndpointConnection(); // PrivateEndpointConnection | Parameters supplied to approve or reject the private end point connection.
apiInstance.privateLinkServicesUpdatePrivateEndpointConnection(resourceGroupName, serviceName, peConnectionName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **serviceName** | **String**| The name of the private link service. | 
 **peConnectionName** | **String**| The name of the private end point connection. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**PrivateEndpointConnection**](PrivateEndpointConnection.md)| Parameters supplied to approve or reject the private end point connection. | 

### Return type

[**PrivateEndpointConnection**](PrivateEndpointConnection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

