# SharedImageGalleryServiceClient.GalleryImageVersionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**galleryImageVersionsCreateOrUpdate**](GalleryImageVersionsApi.md#galleryImageVersionsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/images/{galleryImageName}/versions/{galleryImageVersionName} | 
[**galleryImageVersionsDelete**](GalleryImageVersionsApi.md#galleryImageVersionsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/images/{galleryImageName}/versions/{galleryImageVersionName} | 
[**galleryImageVersionsGet**](GalleryImageVersionsApi.md#galleryImageVersionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/images/{galleryImageName}/versions/{galleryImageVersionName} | 
[**galleryImageVersionsListByGalleryImage**](GalleryImageVersionsApi.md#galleryImageVersionsListByGalleryImage) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/images/{galleryImageName}/versions | 
[**galleryImageVersionsUpdate**](GalleryImageVersionsApi.md#galleryImageVersionsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/images/{galleryImageName}/versions/{galleryImageVersionName} | 



## galleryImageVersionsCreateOrUpdate

> GalleryImageVersion galleryImageVersionsCreateOrUpdate(subscriptionId, resourceGroupName, galleryName, galleryImageName, galleryImageVersionName, apiVersion, galleryImageVersion)



Create or update a gallery Image Version.

### Example

```javascript
import SharedImageGalleryServiceClient from 'shared_image_gallery_service_client';
let defaultClient = SharedImageGalleryServiceClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SharedImageGalleryServiceClient.GalleryImageVersionsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let galleryName = "galleryName_example"; // String | The name of the Shared Image Gallery in which the Image Definition resides.
let galleryImageName = "galleryImageName_example"; // String | The name of the gallery Image Definition in which the Image Version is to be created.
let galleryImageVersionName = "galleryImageVersionName_example"; // String | The name of the gallery Image Version to be created. Needs to follow semantic version name pattern: The allowed characters are digit and period. Digits must be within the range of a 32-bit integer. Format: <MajorVersion>.<MinorVersion>.<Patch>
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let galleryImageVersion = new SharedImageGalleryServiceClient.GalleryImageVersion(); // GalleryImageVersion | Parameters supplied to the create or update gallery Image Version operation.
apiInstance.galleryImageVersionsCreateOrUpdate(subscriptionId, resourceGroupName, galleryName, galleryImageName, galleryImageVersionName, apiVersion, galleryImageVersion, (error, data, response) => {
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
 **galleryName** | **String**| The name of the Shared Image Gallery in which the Image Definition resides. | 
 **galleryImageName** | **String**| The name of the gallery Image Definition in which the Image Version is to be created. | 
 **galleryImageVersionName** | **String**| The name of the gallery Image Version to be created. Needs to follow semantic version name pattern: The allowed characters are digit and period. Digits must be within the range of a 32-bit integer. Format: &lt;MajorVersion&gt;.&lt;MinorVersion&gt;.&lt;Patch&gt; | 
 **apiVersion** | **String**| Client Api Version. | 
 **galleryImageVersion** | [**GalleryImageVersion**](GalleryImageVersion.md)| Parameters supplied to the create or update gallery Image Version operation. | 

### Return type

[**GalleryImageVersion**](GalleryImageVersion.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## galleryImageVersionsDelete

> galleryImageVersionsDelete(subscriptionId, resourceGroupName, galleryName, galleryImageName, galleryImageVersionName, apiVersion)



Delete a gallery Image Version.

### Example

```javascript
import SharedImageGalleryServiceClient from 'shared_image_gallery_service_client';
let defaultClient = SharedImageGalleryServiceClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SharedImageGalleryServiceClient.GalleryImageVersionsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let galleryName = "galleryName_example"; // String | The name of the Shared Image Gallery in which the Image Definition resides.
let galleryImageName = "galleryImageName_example"; // String | The name of the gallery Image Definition in which the Image Version resides.
let galleryImageVersionName = "galleryImageVersionName_example"; // String | The name of the gallery Image Version to be deleted.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.galleryImageVersionsDelete(subscriptionId, resourceGroupName, galleryName, galleryImageName, galleryImageVersionName, apiVersion, (error, data, response) => {
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
 **galleryName** | **String**| The name of the Shared Image Gallery in which the Image Definition resides. | 
 **galleryImageName** | **String**| The name of the gallery Image Definition in which the Image Version resides. | 
 **galleryImageVersionName** | **String**| The name of the gallery Image Version to be deleted. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## galleryImageVersionsGet

> GalleryImageVersion galleryImageVersionsGet(subscriptionId, resourceGroupName, galleryName, galleryImageName, galleryImageVersionName, apiVersion, opts)



Retrieves information about a gallery Image Version.

### Example

```javascript
import SharedImageGalleryServiceClient from 'shared_image_gallery_service_client';
let defaultClient = SharedImageGalleryServiceClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SharedImageGalleryServiceClient.GalleryImageVersionsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let galleryName = "galleryName_example"; // String | The name of the Shared Image Gallery in which the Image Definition resides.
let galleryImageName = "galleryImageName_example"; // String | The name of the gallery Image Definition in which the Image Version resides.
let galleryImageVersionName = "galleryImageVersionName_example"; // String | The name of the gallery Image Version to be retrieved.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'expand': "expand_example" // String | The expand expression to apply on the operation.
};
apiInstance.galleryImageVersionsGet(subscriptionId, resourceGroupName, galleryName, galleryImageName, galleryImageVersionName, apiVersion, opts, (error, data, response) => {
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
 **galleryName** | **String**| The name of the Shared Image Gallery in which the Image Definition resides. | 
 **galleryImageName** | **String**| The name of the gallery Image Definition in which the Image Version resides. | 
 **galleryImageVersionName** | **String**| The name of the gallery Image Version to be retrieved. | 
 **apiVersion** | **String**| Client Api Version. | 
 **expand** | **String**| The expand expression to apply on the operation. | [optional] 

### Return type

[**GalleryImageVersion**](GalleryImageVersion.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## galleryImageVersionsListByGalleryImage

> GalleryImageVersionList galleryImageVersionsListByGalleryImage(subscriptionId, resourceGroupName, galleryName, galleryImageName, apiVersion)



List gallery Image Versions in a gallery Image Definition.

### Example

```javascript
import SharedImageGalleryServiceClient from 'shared_image_gallery_service_client';
let defaultClient = SharedImageGalleryServiceClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SharedImageGalleryServiceClient.GalleryImageVersionsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let galleryName = "galleryName_example"; // String | The name of the Shared Image Gallery in which the Image Definition resides.
let galleryImageName = "galleryImageName_example"; // String | The name of the Shared Image Gallery Image Definition from which the Image Versions are to be listed.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.galleryImageVersionsListByGalleryImage(subscriptionId, resourceGroupName, galleryName, galleryImageName, apiVersion, (error, data, response) => {
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
 **galleryName** | **String**| The name of the Shared Image Gallery in which the Image Definition resides. | 
 **galleryImageName** | **String**| The name of the Shared Image Gallery Image Definition from which the Image Versions are to be listed. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**GalleryImageVersionList**](GalleryImageVersionList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## galleryImageVersionsUpdate

> GalleryImageVersion galleryImageVersionsUpdate(subscriptionId, resourceGroupName, galleryName, galleryImageName, galleryImageVersionName, apiVersion, galleryImageVersion)



Update a gallery Image Version.

### Example

```javascript
import SharedImageGalleryServiceClient from 'shared_image_gallery_service_client';
let defaultClient = SharedImageGalleryServiceClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SharedImageGalleryServiceClient.GalleryImageVersionsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let galleryName = "galleryName_example"; // String | The name of the Shared Image Gallery in which the Image Definition resides.
let galleryImageName = "galleryImageName_example"; // String | The name of the gallery Image Definition in which the Image Version is to be updated.
let galleryImageVersionName = "galleryImageVersionName_example"; // String | The name of the gallery Image Version to be updated. Needs to follow semantic version name pattern: The allowed characters are digit and period. Digits must be within the range of a 32-bit integer. Format: <MajorVersion>.<MinorVersion>.<Patch>
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let galleryImageVersion = new SharedImageGalleryServiceClient.GalleryImageVersionUpdate(); // GalleryImageVersionUpdate | Parameters supplied to the update gallery Image Version operation.
apiInstance.galleryImageVersionsUpdate(subscriptionId, resourceGroupName, galleryName, galleryImageName, galleryImageVersionName, apiVersion, galleryImageVersion, (error, data, response) => {
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
 **galleryName** | **String**| The name of the Shared Image Gallery in which the Image Definition resides. | 
 **galleryImageName** | **String**| The name of the gallery Image Definition in which the Image Version is to be updated. | 
 **galleryImageVersionName** | **String**| The name of the gallery Image Version to be updated. Needs to follow semantic version name pattern: The allowed characters are digit and period. Digits must be within the range of a 32-bit integer. Format: &lt;MajorVersion&gt;.&lt;MinorVersion&gt;.&lt;Patch&gt; | 
 **apiVersion** | **String**| Client Api Version. | 
 **galleryImageVersion** | [**GalleryImageVersionUpdate**](GalleryImageVersionUpdate.md)| Parameters supplied to the update gallery Image Version operation. | 

### Return type

[**GalleryImageVersion**](GalleryImageVersion.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

