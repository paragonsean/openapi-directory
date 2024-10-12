# IoTSpacesClient.ResourceApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ioTSpacesCreateOrUpdate**](ResourceApi.md#ioTSpacesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.IoTSpaces/Graph/{resourceName} | 
[**ioTSpacesDelete**](ResourceApi.md#ioTSpacesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.IoTSpaces/Graph/{resourceName} | 
[**ioTSpacesGet**](ResourceApi.md#ioTSpacesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.IoTSpaces/Graph/{resourceName} | 
[**ioTSpacesUpdate**](ResourceApi.md#ioTSpacesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.IoTSpaces/Graph/{resourceName} | 



## ioTSpacesCreateOrUpdate

> IoTSpacesDescription ioTSpacesCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, resourceName, iotSpaceDescription)



Create or update the metadata of an IoTSpaces instance. The usual pattern to modify a property is to retrieve the IoTSpaces instance metadata and security metadata, and then combine them with the modified values in a new body to update the IoTSpaces instance.

### Example

```javascript
import IoTSpacesClient from 'io_t_spaces_client';
let defaultClient = IoTSpacesClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new IoTSpacesClient.ResourceApi();
let apiVersion = "apiVersion_example"; // String | The version of the API.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the IoTSpaces instance.
let resourceName = "resourceName_example"; // String | The name of the IoTSpaces instance.
let iotSpaceDescription = new IoTSpacesClient.IoTSpacesDescription(); // IoTSpacesDescription | The IoTSpaces instance metadata and security metadata.
apiInstance.ioTSpacesCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, resourceName, iotSpaceDescription, (error, data, response) => {
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
 **resourceName** | **String**| The name of the IoTSpaces instance. | 
 **iotSpaceDescription** | [**IoTSpacesDescription**](IoTSpacesDescription.md)| The IoTSpaces instance metadata and security metadata. | 

### Return type

[**IoTSpacesDescription**](IoTSpacesDescription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## ioTSpacesDelete

> IoTSpacesDescription ioTSpacesDelete(apiVersion, subscriptionId, resourceGroupName, resourceName)



Delete an IoTSpaces instance.

### Example

```javascript
import IoTSpacesClient from 'io_t_spaces_client';
let defaultClient = IoTSpacesClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new IoTSpacesClient.ResourceApi();
let apiVersion = "apiVersion_example"; // String | The version of the API.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the IoTSpaces instance.
let resourceName = "resourceName_example"; // String | The name of the IoTSpaces instance.
apiInstance.ioTSpacesDelete(apiVersion, subscriptionId, resourceGroupName, resourceName, (error, data, response) => {
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
 **resourceName** | **String**| The name of the IoTSpaces instance. | 

### Return type

[**IoTSpacesDescription**](IoTSpacesDescription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ioTSpacesGet

> IoTSpacesDescription ioTSpacesGet(apiVersion, subscriptionId, resourceGroupName, resourceName)



Get the metadata of a IoTSpaces instance.

### Example

```javascript
import IoTSpacesClient from 'io_t_spaces_client';
let defaultClient = IoTSpacesClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new IoTSpacesClient.ResourceApi();
let apiVersion = "apiVersion_example"; // String | The version of the API.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the IoTSpaces instance.
let resourceName = "resourceName_example"; // String | The name of the IoTSpaces instance.
apiInstance.ioTSpacesGet(apiVersion, subscriptionId, resourceGroupName, resourceName, (error, data, response) => {
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
 **resourceName** | **String**| The name of the IoTSpaces instance. | 

### Return type

[**IoTSpacesDescription**](IoTSpacesDescription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ioTSpacesUpdate

> IoTSpacesDescription ioTSpacesUpdate(apiVersion, subscriptionId, resourceGroupName, resourceName, iotSpacePatchDescription)



Update the metadata of a IoTSpaces instance.

### Example

```javascript
import IoTSpacesClient from 'io_t_spaces_client';
let defaultClient = IoTSpacesClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new IoTSpacesClient.ResourceApi();
let apiVersion = "apiVersion_example"; // String | The version of the API.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the IoTSpaces instance.
let resourceName = "resourceName_example"; // String | The name of the IoTSpaces instance.
let iotSpacePatchDescription = new IoTSpacesClient.IoTSpacesPatchDescription(); // IoTSpacesPatchDescription | The IoTSpaces instance metadata and security metadata.
apiInstance.ioTSpacesUpdate(apiVersion, subscriptionId, resourceGroupName, resourceName, iotSpacePatchDescription, (error, data, response) => {
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
 **resourceName** | **String**| The name of the IoTSpaces instance. | 
 **iotSpacePatchDescription** | [**IoTSpacesPatchDescription**](IoTSpacesPatchDescription.md)| The IoTSpaces instance metadata and security metadata. | 

### Return type

[**IoTSpacesDescription**](IoTSpacesDescription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

