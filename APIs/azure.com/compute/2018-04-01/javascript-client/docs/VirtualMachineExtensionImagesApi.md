# ComputeManagementClient.VirtualMachineExtensionImagesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**virtualMachineExtensionImagesGet**](VirtualMachineExtensionImagesApi.md#virtualMachineExtensionImagesGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/publishers/{publisherName}/artifacttypes/vmextension/types/{type}/versions/{version} | 
[**virtualMachineExtensionImagesListTypes**](VirtualMachineExtensionImagesApi.md#virtualMachineExtensionImagesListTypes) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/publishers/{publisherName}/artifacttypes/vmextension/types | 
[**virtualMachineExtensionImagesListVersions**](VirtualMachineExtensionImagesApi.md#virtualMachineExtensionImagesListVersions) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/publishers/{publisherName}/artifacttypes/vmextension/types/{type}/versions | 



## virtualMachineExtensionImagesGet

> VirtualMachineExtensionImage virtualMachineExtensionImagesGet(location, publisherName, type, version, apiVersion, subscriptionId)



Gets a virtual machine extension image.

### Example

```javascript
import ComputeManagementClient from 'compute_management_client';
let defaultClient = ComputeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeManagementClient.VirtualMachineExtensionImagesApi();
let location = "location_example"; // String | The name of a supported Azure region.
let publisherName = "publisherName_example"; // String | 
let type = "type_example"; // String | 
let version = "version_example"; // String | 
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.virtualMachineExtensionImagesGet(location, publisherName, type, version, apiVersion, subscriptionId, (error, data, response) => {
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
 **location** | **String**| The name of a supported Azure region. | 
 **publisherName** | **String**|  | 
 **type** | **String**|  | 
 **version** | **String**|  | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**VirtualMachineExtensionImage**](VirtualMachineExtensionImage.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualMachineExtensionImagesListTypes

> [VirtualMachineExtensionImage] virtualMachineExtensionImagesListTypes(location, publisherName, apiVersion, subscriptionId)



Gets a list of virtual machine extension image types.

### Example

```javascript
import ComputeManagementClient from 'compute_management_client';
let defaultClient = ComputeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeManagementClient.VirtualMachineExtensionImagesApi();
let location = "location_example"; // String | The name of a supported Azure region.
let publisherName = "publisherName_example"; // String | 
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.virtualMachineExtensionImagesListTypes(location, publisherName, apiVersion, subscriptionId, (error, data, response) => {
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
 **location** | **String**| The name of a supported Azure region. | 
 **publisherName** | **String**|  | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**[VirtualMachineExtensionImage]**](VirtualMachineExtensionImage.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualMachineExtensionImagesListVersions

> [VirtualMachineExtensionImage] virtualMachineExtensionImagesListVersions(location, publisherName, type, apiVersion, subscriptionId, opts)



Gets a list of virtual machine extension image versions.

### Example

```javascript
import ComputeManagementClient from 'compute_management_client';
let defaultClient = ComputeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeManagementClient.VirtualMachineExtensionImagesApi();
let location = "location_example"; // String | The name of a supported Azure region.
let publisherName = "publisherName_example"; // String | 
let type = "type_example"; // String | 
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let opts = {
  'filter': "filter_example", // String | The filter to apply on the operation.
  'top': 56, // Number | 
  'orderby': "orderby_example" // String | 
};
apiInstance.virtualMachineExtensionImagesListVersions(location, publisherName, type, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **location** | **String**| The name of a supported Azure region. | 
 **publisherName** | **String**|  | 
 **type** | **String**|  | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **filter** | **String**| The filter to apply on the operation. | [optional] 
 **top** | **Number**|  | [optional] 
 **orderby** | **String**|  | [optional] 

### Return type

[**[VirtualMachineExtensionImage]**](VirtualMachineExtensionImage.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

