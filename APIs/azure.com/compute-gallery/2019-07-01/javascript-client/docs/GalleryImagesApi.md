# SharedImageGalleryServiceClient.GalleryImagesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**galleryImagesCreateOrUpdate**](GalleryImagesApi.md#galleryImagesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/images/{galleryImageName} | 
[**galleryImagesDelete**](GalleryImagesApi.md#galleryImagesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/images/{galleryImageName} | 
[**galleryImagesGet**](GalleryImagesApi.md#galleryImagesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/images/{galleryImageName} | 
[**galleryImagesListByGallery**](GalleryImagesApi.md#galleryImagesListByGallery) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/images | 
[**galleryImagesUpdate**](GalleryImagesApi.md#galleryImagesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/images/{galleryImageName} | 



## galleryImagesCreateOrUpdate

> GalleryImage galleryImagesCreateOrUpdate(subscriptionId, resourceGroupName, galleryName, galleryImageName, apiVersion, galleryImage)



Create or update a gallery Image Definition.

### Example

```javascript
import SharedImageGalleryServiceClient from 'shared_image_gallery_service_client';
let defaultClient = SharedImageGalleryServiceClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SharedImageGalleryServiceClient.GalleryImagesApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let galleryName = "galleryName_example"; // String | The name of the Shared Image Gallery in which the Image Definition is to be created.
let galleryImageName = "galleryImageName_example"; // String | The name of the gallery Image Definition to be created or updated. The allowed characters are alphabets and numbers with dots, dashes, and periods allowed in the middle. The maximum length is 80 characters.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let galleryImage = new SharedImageGalleryServiceClient.GalleryImage(); // GalleryImage | Parameters supplied to the create or update gallery image operation.
apiInstance.galleryImagesCreateOrUpdate(subscriptionId, resourceGroupName, galleryName, galleryImageName, apiVersion, galleryImage, (error, data, response) => {
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
 **galleryName** | **String**| The name of the Shared Image Gallery in which the Image Definition is to be created. | 
 **galleryImageName** | **String**| The name of the gallery Image Definition to be created or updated. The allowed characters are alphabets and numbers with dots, dashes, and periods allowed in the middle. The maximum length is 80 characters. | 
 **apiVersion** | **String**| Client Api Version. | 
 **galleryImage** | [**GalleryImage**](GalleryImage.md)| Parameters supplied to the create or update gallery image operation. | 

### Return type

[**GalleryImage**](GalleryImage.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## galleryImagesDelete

> galleryImagesDelete(subscriptionId, resourceGroupName, galleryName, galleryImageName, apiVersion)



Delete a gallery image.

### Example

```javascript
import SharedImageGalleryServiceClient from 'shared_image_gallery_service_client';
let defaultClient = SharedImageGalleryServiceClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SharedImageGalleryServiceClient.GalleryImagesApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let galleryName = "galleryName_example"; // String | The name of the Shared Image Gallery in which the Image Definition is to be deleted.
let galleryImageName = "galleryImageName_example"; // String | The name of the gallery Image Definition to be deleted.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.galleryImagesDelete(subscriptionId, resourceGroupName, galleryName, galleryImageName, apiVersion, (error, data, response) => {
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
 **galleryName** | **String**| The name of the Shared Image Gallery in which the Image Definition is to be deleted. | 
 **galleryImageName** | **String**| The name of the gallery Image Definition to be deleted. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## galleryImagesGet

> GalleryImage galleryImagesGet(subscriptionId, resourceGroupName, galleryName, galleryImageName, apiVersion)



Retrieves information about a gallery Image Definition.

### Example

```javascript
import SharedImageGalleryServiceClient from 'shared_image_gallery_service_client';
let defaultClient = SharedImageGalleryServiceClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SharedImageGalleryServiceClient.GalleryImagesApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let galleryName = "galleryName_example"; // String | The name of the Shared Image Gallery from which the Image Definitions are to be retrieved.
let galleryImageName = "galleryImageName_example"; // String | The name of the gallery Image Definition to be retrieved.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.galleryImagesGet(subscriptionId, resourceGroupName, galleryName, galleryImageName, apiVersion, (error, data, response) => {
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
 **galleryName** | **String**| The name of the Shared Image Gallery from which the Image Definitions are to be retrieved. | 
 **galleryImageName** | **String**| The name of the gallery Image Definition to be retrieved. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**GalleryImage**](GalleryImage.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## galleryImagesListByGallery

> GalleryImageList galleryImagesListByGallery(subscriptionId, resourceGroupName, galleryName, apiVersion)



List gallery Image Definitions in a gallery.

### Example

```javascript
import SharedImageGalleryServiceClient from 'shared_image_gallery_service_client';
let defaultClient = SharedImageGalleryServiceClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SharedImageGalleryServiceClient.GalleryImagesApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let galleryName = "galleryName_example"; // String | The name of the Shared Image Gallery from which Image Definitions are to be listed.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.galleryImagesListByGallery(subscriptionId, resourceGroupName, galleryName, apiVersion, (error, data, response) => {
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
 **galleryName** | **String**| The name of the Shared Image Gallery from which Image Definitions are to be listed. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**GalleryImageList**](GalleryImageList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## galleryImagesUpdate

> GalleryImage galleryImagesUpdate(subscriptionId, resourceGroupName, galleryName, galleryImageName, apiVersion, galleryImage)



Update a gallery Image Definition.

### Example

```javascript
import SharedImageGalleryServiceClient from 'shared_image_gallery_service_client';
let defaultClient = SharedImageGalleryServiceClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SharedImageGalleryServiceClient.GalleryImagesApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let galleryName = "galleryName_example"; // String | The name of the Shared Image Gallery in which the Image Definition is to be updated.
let galleryImageName = "galleryImageName_example"; // String | The name of the gallery Image Definition to be updated. The allowed characters are alphabets and numbers with dots, dashes, and periods allowed in the middle. The maximum length is 80 characters.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let galleryImage = new SharedImageGalleryServiceClient.GalleryImageUpdate(); // GalleryImageUpdate | Parameters supplied to the update gallery image operation.
apiInstance.galleryImagesUpdate(subscriptionId, resourceGroupName, galleryName, galleryImageName, apiVersion, galleryImage, (error, data, response) => {
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
 **galleryName** | **String**| The name of the Shared Image Gallery in which the Image Definition is to be updated. | 
 **galleryImageName** | **String**| The name of the gallery Image Definition to be updated. The allowed characters are alphabets and numbers with dots, dashes, and periods allowed in the middle. The maximum length is 80 characters. | 
 **apiVersion** | **String**| Client Api Version. | 
 **galleryImage** | [**GalleryImageUpdate**](GalleryImageUpdate.md)| Parameters supplied to the update gallery image operation. | 

### Return type

[**GalleryImage**](GalleryImage.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

