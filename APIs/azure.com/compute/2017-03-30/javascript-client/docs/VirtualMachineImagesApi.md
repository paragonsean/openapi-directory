# ComputeManagementClient.VirtualMachineImagesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**virtualMachineImagesGet**](VirtualMachineImagesApi.md#virtualMachineImagesGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/publishers/{publisherName}/artifacttypes/vmimage/offers/{offer}/skus/{skus}/versions/{version} | 
[**virtualMachineImagesList**](VirtualMachineImagesApi.md#virtualMachineImagesList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/publishers/{publisherName}/artifacttypes/vmimage/offers/{offer}/skus/{skus}/versions | 
[**virtualMachineImagesListOffers**](VirtualMachineImagesApi.md#virtualMachineImagesListOffers) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/publishers/{publisherName}/artifacttypes/vmimage/offers | 
[**virtualMachineImagesListPublishers**](VirtualMachineImagesApi.md#virtualMachineImagesListPublishers) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/publishers | 
[**virtualMachineImagesListSkus**](VirtualMachineImagesApi.md#virtualMachineImagesListSkus) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/publishers/{publisherName}/artifacttypes/vmimage/offers/{offer}/skus | 



## virtualMachineImagesGet

> VirtualMachineImage virtualMachineImagesGet(location, publisherName, offer, skus, version, apiVersion, subscriptionId)



Gets a virtual machine image.

### Example

```javascript
import ComputeManagementClient from 'compute_management_client';
let defaultClient = ComputeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeManagementClient.VirtualMachineImagesApi();
let location = "location_example"; // String | The name of a supported Azure region.
let publisherName = "publisherName_example"; // String | A valid image publisher.
let offer = "offer_example"; // String | A valid image publisher offer.
let skus = "skus_example"; // String | A valid image SKU.
let version = "version_example"; // String | A valid image SKU version.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.virtualMachineImagesGet(location, publisherName, offer, skus, version, apiVersion, subscriptionId, (error, data, response) => {
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
 **publisherName** | **String**| A valid image publisher. | 
 **offer** | **String**| A valid image publisher offer. | 
 **skus** | **String**| A valid image SKU. | 
 **version** | **String**| A valid image SKU version. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**VirtualMachineImage**](VirtualMachineImage.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualMachineImagesList

> [VirtualMachineImageResource] virtualMachineImagesList(location, publisherName, offer, skus, apiVersion, subscriptionId, opts)



Gets a list of all virtual machine image versions for the specified location, publisher, offer, and SKU.

### Example

```javascript
import ComputeManagementClient from 'compute_management_client';
let defaultClient = ComputeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeManagementClient.VirtualMachineImagesApi();
let location = "location_example"; // String | The name of a supported Azure region.
let publisherName = "publisherName_example"; // String | A valid image publisher.
let offer = "offer_example"; // String | A valid image publisher offer.
let skus = "skus_example"; // String | A valid image SKU.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let opts = {
  'filter': "filter_example", // String | The filter to apply on the operation.
  'top': 56, // Number | 
  'orderby': "orderby_example" // String | 
};
apiInstance.virtualMachineImagesList(location, publisherName, offer, skus, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **publisherName** | **String**| A valid image publisher. | 
 **offer** | **String**| A valid image publisher offer. | 
 **skus** | **String**| A valid image SKU. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **filter** | **String**| The filter to apply on the operation. | [optional] 
 **top** | **Number**|  | [optional] 
 **orderby** | **String**|  | [optional] 

### Return type

[**[VirtualMachineImageResource]**](VirtualMachineImageResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualMachineImagesListOffers

> [VirtualMachineImageResource] virtualMachineImagesListOffers(location, publisherName, apiVersion, subscriptionId)



Gets a list of virtual machine image offers for the specified location and publisher.

### Example

```javascript
import ComputeManagementClient from 'compute_management_client';
let defaultClient = ComputeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeManagementClient.VirtualMachineImagesApi();
let location = "location_example"; // String | The name of a supported Azure region.
let publisherName = "publisherName_example"; // String | A valid image publisher.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.virtualMachineImagesListOffers(location, publisherName, apiVersion, subscriptionId, (error, data, response) => {
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
 **publisherName** | **String**| A valid image publisher. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**[VirtualMachineImageResource]**](VirtualMachineImageResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualMachineImagesListPublishers

> [VirtualMachineImageResource] virtualMachineImagesListPublishers(location, apiVersion, subscriptionId)



Gets a list of virtual machine image publishers for the specified Azure location.

### Example

```javascript
import ComputeManagementClient from 'compute_management_client';
let defaultClient = ComputeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeManagementClient.VirtualMachineImagesApi();
let location = "location_example"; // String | The name of a supported Azure region.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.virtualMachineImagesListPublishers(location, apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**[VirtualMachineImageResource]**](VirtualMachineImageResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualMachineImagesListSkus

> [VirtualMachineImageResource] virtualMachineImagesListSkus(location, publisherName, offer, apiVersion, subscriptionId)



Gets a list of virtual machine image SKUs for the specified location, publisher, and offer.

### Example

```javascript
import ComputeManagementClient from 'compute_management_client';
let defaultClient = ComputeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeManagementClient.VirtualMachineImagesApi();
let location = "location_example"; // String | The name of a supported Azure region.
let publisherName = "publisherName_example"; // String | A valid image publisher.
let offer = "offer_example"; // String | A valid image publisher offer.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.virtualMachineImagesListSkus(location, publisherName, offer, apiVersion, subscriptionId, (error, data, response) => {
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
 **publisherName** | **String**| A valid image publisher. | 
 **offer** | **String**| A valid image publisher offer. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**[VirtualMachineImageResource]**](VirtualMachineImageResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

