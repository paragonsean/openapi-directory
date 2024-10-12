# DeviceServices.DeviceServicesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**servicesCreateOrUpdate**](DeviceServicesApi.md#servicesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.WindowsIoT/deviceServices/{deviceName} | Create or update the metadata of a Windows IoT Device Service.
[**servicesDelete**](DeviceServicesApi.md#servicesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.WindowsIoT/deviceServices/{deviceName} | 
[**servicesGet**](DeviceServicesApi.md#servicesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.WindowsIoT/deviceServices/{deviceName} | 
[**servicesList**](DeviceServicesApi.md#servicesList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.WindowsIoT/deviceServices | 
[**servicesListByResourceGroup**](DeviceServicesApi.md#servicesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.WindowsIoT/deviceServices | 
[**servicesUpdate**](DeviceServicesApi.md#servicesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.WindowsIoT/deviceServices/{deviceName} | Updates the metadata of a Windows IoT Device Service.



## servicesCreateOrUpdate

> DeviceService servicesCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, deviceName, deviceService, opts)

Create or update the metadata of a Windows IoT Device Service.

Create or update the metadata of a Windows IoT Device Service. The usual pattern to modify a property is to retrieve the Windows IoT Device Service metadata and security metadata, and then combine them with the modified values in a new body to update the Windows IoT Device Service.

### Example

```javascript
import DeviceServices from 'device_services';
let defaultClient = DeviceServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DeviceServices.DeviceServicesApi();
let apiVersion = "apiVersion_example"; // String | The version of the API.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Windows IoT Device Service.
let deviceName = "deviceName_example"; // String | The name of the Windows IoT Device Service.
let deviceService = new DeviceServices.DeviceServiceProperties(); // DeviceServiceProperties | The Windows IoT Device Service metadata and security metadata.
let opts = {
  'ifMatch': "ifMatch_example" // String | ETag of the Windows IoT Device Service. Do not specify for creating a new Windows IoT Device Service. Required to update an existing Windows IoT Device Service.
};
apiInstance.servicesCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, deviceName, deviceService, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the Windows IoT Device Service. | 
 **deviceName** | **String**| The name of the Windows IoT Device Service. | 
 **deviceService** | [**DeviceServiceProperties**](DeviceServiceProperties.md)| The Windows IoT Device Service metadata and security metadata. | 
 **ifMatch** | **String**| ETag of the Windows IoT Device Service. Do not specify for creating a new Windows IoT Device Service. Required to update an existing Windows IoT Device Service. | [optional] 

### Return type

[**DeviceService**](DeviceService.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## servicesDelete

> DeviceService servicesDelete(apiVersion, subscriptionId, resourceGroupName, deviceName)



Delete a Windows IoT Device Service.

### Example

```javascript
import DeviceServices from 'device_services';
let defaultClient = DeviceServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DeviceServices.DeviceServicesApi();
let apiVersion = "apiVersion_example"; // String | The version of the API.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Windows IoT Device Service.
let deviceName = "deviceName_example"; // String | The name of the Windows IoT Device Service.
apiInstance.servicesDelete(apiVersion, subscriptionId, resourceGroupName, deviceName, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the Windows IoT Device Service. | 
 **deviceName** | **String**| The name of the Windows IoT Device Service. | 

### Return type

[**DeviceService**](DeviceService.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## servicesGet

> DeviceService servicesGet(apiVersion, subscriptionId, resourceGroupName, deviceName)



Get the non-security related metadata of a Windows IoT Device Service.

### Example

```javascript
import DeviceServices from 'device_services';
let defaultClient = DeviceServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DeviceServices.DeviceServicesApi();
let apiVersion = "apiVersion_example"; // String | The version of the API.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Windows IoT Device Service.
let deviceName = "deviceName_example"; // String | The name of the Windows IoT Device Service.
apiInstance.servicesGet(apiVersion, subscriptionId, resourceGroupName, deviceName, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the Windows IoT Device Service. | 
 **deviceName** | **String**| The name of the Windows IoT Device Service. | 

### Return type

[**DeviceService**](DeviceService.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## servicesList

> DeviceServiceDescriptionListResult servicesList(apiVersion, subscriptionId)



Get all the IoT hubs in a subscription.

### Example

```javascript
import DeviceServices from 'device_services';
let defaultClient = DeviceServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DeviceServices.DeviceServicesApi();
let apiVersion = "apiVersion_example"; // String | The version of the API.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
apiInstance.servicesList(apiVersion, subscriptionId, (error, data, response) => {
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

[**DeviceServiceDescriptionListResult**](DeviceServiceDescriptionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## servicesListByResourceGroup

> DeviceServiceDescriptionListResult servicesListByResourceGroup(apiVersion, subscriptionId, resourceGroupName)



Get all the IoT hubs in a resource group.

### Example

```javascript
import DeviceServices from 'device_services';
let defaultClient = DeviceServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DeviceServices.DeviceServicesApi();
let apiVersion = "apiVersion_example"; // String | The version of the API.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Windows IoT Device Service.
apiInstance.servicesListByResourceGroup(apiVersion, subscriptionId, resourceGroupName, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the Windows IoT Device Service. | 

### Return type

[**DeviceServiceDescriptionListResult**](DeviceServiceDescriptionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## servicesUpdate

> DeviceService servicesUpdate(apiVersion, subscriptionId, resourceGroupName, deviceName, deviceService, opts)

Updates the metadata of a Windows IoT Device Service.

Updates the metadata of a Windows IoT Device Service. The usual pattern to modify a property is to retrieve the Windows IoT Device Service metadata and security metadata, and then combine them with the modified values in a new body to update the Windows IoT Device Service.

### Example

```javascript
import DeviceServices from 'device_services';
let defaultClient = DeviceServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DeviceServices.DeviceServicesApi();
let apiVersion = "apiVersion_example"; // String | The version of the API.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Windows IoT Device Service.
let deviceName = "deviceName_example"; // String | The name of the Windows IoT Device Service.
let deviceService = new DeviceServices.DeviceServiceProperties(); // DeviceServiceProperties | The Windows IoT Device Service metadata and security metadata.
let opts = {
  'ifMatch': "ifMatch_example" // String | ETag of the Windows IoT Device Service. Do not specify for creating a brand new Windows IoT Device Service. Required to update an existing Windows IoT Device Service.
};
apiInstance.servicesUpdate(apiVersion, subscriptionId, resourceGroupName, deviceName, deviceService, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the Windows IoT Device Service. | 
 **deviceName** | **String**| The name of the Windows IoT Device Service. | 
 **deviceService** | [**DeviceServiceProperties**](DeviceServiceProperties.md)| The Windows IoT Device Service metadata and security metadata. | 
 **ifMatch** | **String**| ETag of the Windows IoT Device Service. Do not specify for creating a brand new Windows IoT Device Service. Required to update an existing Windows IoT Device Service. | [optional] 

### Return type

[**DeviceService**](DeviceService.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

