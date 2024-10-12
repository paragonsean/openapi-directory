# SharedImageGalleryServiceClient.GalleriesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**galleriesCreateOrUpdate**](GalleriesApi.md#galleriesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName} | 
[**galleriesDelete**](GalleriesApi.md#galleriesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName} | 
[**galleriesGet**](GalleriesApi.md#galleriesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName} | 
[**galleriesList**](GalleriesApi.md#galleriesList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Compute/galleries | 
[**galleriesListByResourceGroup**](GalleriesApi.md#galleriesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries | 



## galleriesCreateOrUpdate

> Gallery galleriesCreateOrUpdate(subscriptionId, resourceGroupName, galleryName, apiVersion, gallery)



Create or update a Shared Image Gallery.

### Example

```javascript
import SharedImageGalleryServiceClient from 'shared_image_gallery_service_client';
let defaultClient = SharedImageGalleryServiceClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SharedImageGalleryServiceClient.GalleriesApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let galleryName = "galleryName_example"; // String | The name of the Shared Image Gallery. The allowed characters are alphabets and numbers with dots and periods allowed in the middle. The maximum length is 80 characters.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let gallery = new SharedImageGalleryServiceClient.Gallery(); // Gallery | Parameters supplied to the create or update Shared Image Gallery operation.
apiInstance.galleriesCreateOrUpdate(subscriptionId, resourceGroupName, galleryName, apiVersion, gallery, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **galleryName** | **String**| The name of the Shared Image Gallery. The allowed characters are alphabets and numbers with dots and periods allowed in the middle. The maximum length is 80 characters. | 
 **apiVersion** | **String**| Client Api Version. | 
 **gallery** | [**Gallery**](Gallery.md)| Parameters supplied to the create or update Shared Image Gallery operation. | 

### Return type

[**Gallery**](Gallery.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## galleriesDelete

> galleriesDelete(subscriptionId, resourceGroupName, galleryName, apiVersion)



Delete a Shared Image Gallery.

### Example

```javascript
import SharedImageGalleryServiceClient from 'shared_image_gallery_service_client';
let defaultClient = SharedImageGalleryServiceClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SharedImageGalleryServiceClient.GalleriesApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let galleryName = "galleryName_example"; // String | The name of the Shared Image Gallery to be deleted.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.galleriesDelete(subscriptionId, resourceGroupName, galleryName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **galleryName** | **String**| The name of the Shared Image Gallery to be deleted. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## galleriesGet

> Gallery galleriesGet(subscriptionId, resourceGroupName, galleryName, apiVersion)



Retrieves information about a Shared Image Gallery.

### Example

```javascript
import SharedImageGalleryServiceClient from 'shared_image_gallery_service_client';
let defaultClient = SharedImageGalleryServiceClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SharedImageGalleryServiceClient.GalleriesApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let galleryName = "galleryName_example"; // String | The name of the Shared Image Gallery.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.galleriesGet(subscriptionId, resourceGroupName, galleryName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **galleryName** | **String**| The name of the Shared Image Gallery. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**Gallery**](Gallery.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## galleriesList

> GalleryList galleriesList(subscriptionId, apiVersion)



List galleries under a subscription.

### Example

```javascript
import SharedImageGalleryServiceClient from 'shared_image_gallery_service_client';
let defaultClient = SharedImageGalleryServiceClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SharedImageGalleryServiceClient.GalleriesApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.galleriesList(subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**GalleryList**](GalleryList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## galleriesListByResourceGroup

> GalleryList galleriesListByResourceGroup(subscriptionId, resourceGroupName, apiVersion)



List galleries under a resource group.

### Example

```javascript
import SharedImageGalleryServiceClient from 'shared_image_gallery_service_client';
let defaultClient = SharedImageGalleryServiceClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SharedImageGalleryServiceClient.GalleriesApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.galleriesListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**GalleryList**](GalleryList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

