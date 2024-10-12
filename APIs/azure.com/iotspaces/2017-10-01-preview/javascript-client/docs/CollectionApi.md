# IoTSpacesClient.CollectionApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ioTSpacesList**](CollectionApi.md#ioTSpacesList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.IoTSpaces/Graph | 
[**ioTSpacesListByResourceGroup**](CollectionApi.md#ioTSpacesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.IoTSpaces/Graph | 



## ioTSpacesList

> IoTSpacesDescriptionListResult ioTSpacesList(apiVersion, subscriptionId)



Get all the IoTSpaces instances in a subscription.

### Example

```javascript
import IoTSpacesClient from 'io_t_spaces_client';
let defaultClient = IoTSpacesClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new IoTSpacesClient.CollectionApi();
let apiVersion = "apiVersion_example"; // String | The version of the API.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
apiInstance.ioTSpacesList(apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. | 
 **subscriptionId** | **String**| The subscription identifier. | 

### Return type

[**IoTSpacesDescriptionListResult**](IoTSpacesDescriptionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ioTSpacesListByResourceGroup

> IoTSpacesDescriptionListResult ioTSpacesListByResourceGroup(apiVersion, subscriptionId, resourceGroupName)



Get all the IoTSpaces instances in a resource group.

### Example

```javascript
import IoTSpacesClient from 'io_t_spaces_client';
let defaultClient = IoTSpacesClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new IoTSpacesClient.CollectionApi();
let apiVersion = "apiVersion_example"; // String | The version of the API.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the IoTSpaces instance.
apiInstance.ioTSpacesListByResourceGroup(apiVersion, subscriptionId, resourceGroupName, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. | 
 **subscriptionId** | **String**| The subscription identifier. | 
 **resourceGroupName** | **String**| The name of the resource group that contains the IoTSpaces instance. | 

### Return type

[**IoTSpacesDescriptionListResult**](IoTSpacesDescriptionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

