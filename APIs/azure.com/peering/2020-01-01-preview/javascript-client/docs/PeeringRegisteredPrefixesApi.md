# PeeringManagementClient.PeeringRegisteredPrefixesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**registeredPrefixesCreateOrUpdate**](PeeringRegisteredPrefixesApi.md#registeredPrefixesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Peering/peerings/{peeringName}/registeredPrefixes/{registeredPrefixName} | 
[**registeredPrefixesDelete**](PeeringRegisteredPrefixesApi.md#registeredPrefixesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Peering/peerings/{peeringName}/registeredPrefixes/{registeredPrefixName} | 
[**registeredPrefixesGet**](PeeringRegisteredPrefixesApi.md#registeredPrefixesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Peering/peerings/{peeringName}/registeredPrefixes/{registeredPrefixName} | 
[**registeredPrefixesListByPeering**](PeeringRegisteredPrefixesApi.md#registeredPrefixesListByPeering) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Peering/peerings/{peeringName}/registeredPrefixes | 



## registeredPrefixesCreateOrUpdate

> PeeringRegisteredPrefix registeredPrefixesCreateOrUpdate(resourceGroupName, peeringName, registeredPrefixName, subscriptionId, apiVersion, registeredPrefix)



Creates a new registered prefix with the specified name under the given subscription, resource group and peering.

### Example

```javascript
import PeeringManagementClient from 'peering_management_client';
let defaultClient = PeeringManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeeringManagementClient.PeeringRegisteredPrefixesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let peeringName = "peeringName_example"; // String | The name of the peering.
let registeredPrefixName = "registeredPrefixName_example"; // String | The name of the registered prefix.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
let apiVersion = "apiVersion_example"; // String | The client API version.
let registeredPrefix = new PeeringManagementClient.PeeringRegisteredPrefix(); // PeeringRegisteredPrefix | The properties needed to create a registered prefix.
apiInstance.registeredPrefixesCreateOrUpdate(resourceGroupName, peeringName, registeredPrefixName, subscriptionId, apiVersion, registeredPrefix, (error, data, response) => {
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
 **peeringName** | **String**| The name of the peering. | 
 **registeredPrefixName** | **String**| The name of the registered prefix. | 
 **subscriptionId** | **String**| The Azure subscription ID. | 
 **apiVersion** | **String**| The client API version. | 
 **registeredPrefix** | [**PeeringRegisteredPrefix**](PeeringRegisteredPrefix.md)| The properties needed to create a registered prefix. | 

### Return type

[**PeeringRegisteredPrefix**](PeeringRegisteredPrefix.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## registeredPrefixesDelete

> registeredPrefixesDelete(resourceGroupName, peeringName, registeredPrefixName, subscriptionId, apiVersion)



Deletes an existing registered prefix with the specified name under the given subscription, resource group and peering.

### Example

```javascript
import PeeringManagementClient from 'peering_management_client';
let defaultClient = PeeringManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeeringManagementClient.PeeringRegisteredPrefixesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let peeringName = "peeringName_example"; // String | The name of the peering.
let registeredPrefixName = "registeredPrefixName_example"; // String | The name of the registered prefix.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
let apiVersion = "apiVersion_example"; // String | The client API version.
apiInstance.registeredPrefixesDelete(resourceGroupName, peeringName, registeredPrefixName, subscriptionId, apiVersion, (error, data, response) => {
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
 **peeringName** | **String**| The name of the peering. | 
 **registeredPrefixName** | **String**| The name of the registered prefix. | 
 **subscriptionId** | **String**| The Azure subscription ID. | 
 **apiVersion** | **String**| The client API version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## registeredPrefixesGet

> PeeringRegisteredPrefix registeredPrefixesGet(resourceGroupName, peeringName, registeredPrefixName, subscriptionId, apiVersion)



Gets an existing registered prefix with the specified name under the given subscription, resource group and peering.

### Example

```javascript
import PeeringManagementClient from 'peering_management_client';
let defaultClient = PeeringManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeeringManagementClient.PeeringRegisteredPrefixesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let peeringName = "peeringName_example"; // String | The name of the peering.
let registeredPrefixName = "registeredPrefixName_example"; // String | The name of the registered prefix.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
let apiVersion = "apiVersion_example"; // String | The client API version.
apiInstance.registeredPrefixesGet(resourceGroupName, peeringName, registeredPrefixName, subscriptionId, apiVersion, (error, data, response) => {
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
 **peeringName** | **String**| The name of the peering. | 
 **registeredPrefixName** | **String**| The name of the registered prefix. | 
 **subscriptionId** | **String**| The Azure subscription ID. | 
 **apiVersion** | **String**| The client API version. | 

### Return type

[**PeeringRegisteredPrefix**](PeeringRegisteredPrefix.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## registeredPrefixesListByPeering

> PeeringRegisteredPrefixListResult registeredPrefixesListByPeering(resourceGroupName, peeringName, subscriptionId, apiVersion)



Lists all registered prefixes under the given subscription, resource group and peering.

### Example

```javascript
import PeeringManagementClient from 'peering_management_client';
let defaultClient = PeeringManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeeringManagementClient.PeeringRegisteredPrefixesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let peeringName = "peeringName_example"; // String | The name of the peering.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
let apiVersion = "apiVersion_example"; // String | The client API version.
apiInstance.registeredPrefixesListByPeering(resourceGroupName, peeringName, subscriptionId, apiVersion, (error, data, response) => {
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
 **peeringName** | **String**| The name of the peering. | 
 **subscriptionId** | **String**| The Azure subscription ID. | 
 **apiVersion** | **String**| The client API version. | 

### Return type

[**PeeringRegisteredPrefixListResult**](PeeringRegisteredPrefixListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

