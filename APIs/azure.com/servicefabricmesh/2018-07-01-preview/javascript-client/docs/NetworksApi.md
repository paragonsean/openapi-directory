# SeaBreezeManagementClient.NetworksApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**networkCreate**](NetworksApi.md#networkCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabricMesh/networks/{networkName} | Creates or updates a network resource.
[**networkDelete**](NetworksApi.md#networkDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabricMesh/networks/{networkName} | Deletes the network resource.
[**networkGet**](NetworksApi.md#networkGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabricMesh/networks/{networkName} | Gets the network resource.
[**networkListByResourceGroup**](NetworksApi.md#networkListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabricMesh/networks | Gets all the network resources in a given resource group.
[**networkListBySubscription**](NetworksApi.md#networkListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.ServiceFabricMesh/networks | Gets all the network resources in a given subscription.



## networkCreate

> NetworkResourceDescription networkCreate(subscriptionId, apiVersion, resourceGroupName, networkName, networkResourceDescription)

Creates or updates a network resource.

Creates a network resource with the specified name and description. If a network with the same name already exists, then its description is updated to the one indicated in this request.  Use network resources to create private network and configure public connectivity for services within your application.  

### Example

```javascript
import SeaBreezeManagementClient from 'sea_breeze_management_client';
let defaultClient = SeaBreezeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeaBreezeManagementClient.NetworksApi();
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier
let apiVersion = "'2018-07-01-preview'"; // String | The version of the API. This parameter is required and its value must be `2018-07-01-preview`.
let resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
let networkName = "networkName_example"; // String | The identity of the network.
let networkResourceDescription = new SeaBreezeManagementClient.NetworkResourceDescription(); // NetworkResourceDescription | Description for creating a network resource.
apiInstance.networkCreate(subscriptionId, apiVersion, resourceGroupName, networkName, networkResourceDescription, (error, data, response) => {
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
 **subscriptionId** | **String**| The customer subscription identifier | 
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#x60;2018-07-01-preview&#x60;. | [default to &#39;2018-07-01-preview&#39;]
 **resourceGroupName** | **String**| Azure resource group name | 
 **networkName** | **String**| The identity of the network. | 
 **networkResourceDescription** | [**NetworkResourceDescription**](NetworkResourceDescription.md)| Description for creating a network resource. | 

### Return type

[**NetworkResourceDescription**](NetworkResourceDescription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## networkDelete

> networkDelete(subscriptionId, apiVersion, resourceGroupName, networkName)

Deletes the network resource.

Deletes the network resource identified by the name.

### Example

```javascript
import SeaBreezeManagementClient from 'sea_breeze_management_client';
let defaultClient = SeaBreezeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeaBreezeManagementClient.NetworksApi();
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier
let apiVersion = "'2018-07-01-preview'"; // String | The version of the API. This parameter is required and its value must be `2018-07-01-preview`.
let resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
let networkName = "networkName_example"; // String | The identity of the network.
apiInstance.networkDelete(subscriptionId, apiVersion, resourceGroupName, networkName, (error, data, response) => {
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
 **subscriptionId** | **String**| The customer subscription identifier | 
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#x60;2018-07-01-preview&#x60;. | [default to &#39;2018-07-01-preview&#39;]
 **resourceGroupName** | **String**| Azure resource group name | 
 **networkName** | **String**| The identity of the network. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## networkGet

> NetworkResourceDescription networkGet(subscriptionId, apiVersion, resourceGroupName, networkName)

Gets the network resource.

Gets the information about the network resource with a given name. This information includes the network description and other runtime information. 

### Example

```javascript
import SeaBreezeManagementClient from 'sea_breeze_management_client';
let defaultClient = SeaBreezeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeaBreezeManagementClient.NetworksApi();
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier
let apiVersion = "'2018-07-01-preview'"; // String | The version of the API. This parameter is required and its value must be `2018-07-01-preview`.
let resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
let networkName = "networkName_example"; // String | The identity of the network.
apiInstance.networkGet(subscriptionId, apiVersion, resourceGroupName, networkName, (error, data, response) => {
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
 **subscriptionId** | **String**| The customer subscription identifier | 
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#x60;2018-07-01-preview&#x60;. | [default to &#39;2018-07-01-preview&#39;]
 **resourceGroupName** | **String**| Azure resource group name | 
 **networkName** | **String**| The identity of the network. | 

### Return type

[**NetworkResourceDescription**](NetworkResourceDescription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## networkListByResourceGroup

> NetworkResourceDescriptionList networkListByResourceGroup(subscriptionId, apiVersion, resourceGroupName)

Gets all the network resources in a given resource group.

Gets the information about all network resources in a given resource group. The information includes the network description and other runtime properties. 

### Example

```javascript
import SeaBreezeManagementClient from 'sea_breeze_management_client';
let defaultClient = SeaBreezeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeaBreezeManagementClient.NetworksApi();
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier
let apiVersion = "'2018-07-01-preview'"; // String | The version of the API. This parameter is required and its value must be `2018-07-01-preview`.
let resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
apiInstance.networkListByResourceGroup(subscriptionId, apiVersion, resourceGroupName, (error, data, response) => {
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
 **subscriptionId** | **String**| The customer subscription identifier | 
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#x60;2018-07-01-preview&#x60;. | [default to &#39;2018-07-01-preview&#39;]
 **resourceGroupName** | **String**| Azure resource group name | 

### Return type

[**NetworkResourceDescriptionList**](NetworkResourceDescriptionList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## networkListBySubscription

> NetworkResourceDescriptionList networkListBySubscription(subscriptionId, apiVersion)

Gets all the network resources in a given subscription.

Gets the information about all network resources in a given subscription. The information includes the network description and other runtime properties.

### Example

```javascript
import SeaBreezeManagementClient from 'sea_breeze_management_client';
let defaultClient = SeaBreezeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeaBreezeManagementClient.NetworksApi();
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier
let apiVersion = "'2018-07-01-preview'"; // String | The version of the API. This parameter is required and its value must be `2018-07-01-preview`.
apiInstance.networkListBySubscription(subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The customer subscription identifier | 
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#x60;2018-07-01-preview&#x60;. | [default to &#39;2018-07-01-preview&#39;]

### Return type

[**NetworkResourceDescriptionList**](NetworkResourceDescriptionList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

