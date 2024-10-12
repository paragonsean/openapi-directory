# SharedImageGalleryServiceClient.GalleryApplicationVersionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**galleryApplicationVersionsCreateOrUpdate**](GalleryApplicationVersionsApi.md#galleryApplicationVersionsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/applications/{galleryApplicationName}/versions/{galleryApplicationVersionName} | 
[**galleryApplicationVersionsDelete**](GalleryApplicationVersionsApi.md#galleryApplicationVersionsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/applications/{galleryApplicationName}/versions/{galleryApplicationVersionName} | 
[**galleryApplicationVersionsGet**](GalleryApplicationVersionsApi.md#galleryApplicationVersionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/applications/{galleryApplicationName}/versions/{galleryApplicationVersionName} | 
[**galleryApplicationVersionsListByGalleryApplication**](GalleryApplicationVersionsApi.md#galleryApplicationVersionsListByGalleryApplication) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/applications/{galleryApplicationName}/versions | 
[**galleryApplicationVersionsUpdate**](GalleryApplicationVersionsApi.md#galleryApplicationVersionsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/applications/{galleryApplicationName}/versions/{galleryApplicationVersionName} | 



## galleryApplicationVersionsCreateOrUpdate

> GalleryApplicationVersion galleryApplicationVersionsCreateOrUpdate(subscriptionId, resourceGroupName, galleryName, galleryApplicationName, galleryApplicationVersionName, apiVersion, galleryApplicationVersion)



Create or update a gallery Application Version.

### Example

```javascript
import SharedImageGalleryServiceClient from 'shared_image_gallery_service_client';
let defaultClient = SharedImageGalleryServiceClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SharedImageGalleryServiceClient.GalleryApplicationVersionsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let galleryName = "galleryName_example"; // String | The name of the Shared Application Gallery in which the Application Definition resides.
let galleryApplicationName = "galleryApplicationName_example"; // String | The name of the gallery Application Definition in which the Application Version is to be created.
let galleryApplicationVersionName = "galleryApplicationVersionName_example"; // String | The name of the gallery Application Version to be created. Needs to follow semantic version name pattern: The allowed characters are digit and period. Digits must be within the range of a 32-bit integer. Format: <MajorVersion>.<MinorVersion>.<Patch>
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let galleryApplicationVersion = new SharedImageGalleryServiceClient.GalleryApplicationVersion(); // GalleryApplicationVersion | Parameters supplied to the create or update gallery Application Version operation.
apiInstance.galleryApplicationVersionsCreateOrUpdate(subscriptionId, resourceGroupName, galleryName, galleryApplicationName, galleryApplicationVersionName, apiVersion, galleryApplicationVersion, (error, data, response) => {
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
 **galleryName** | **String**| The name of the Shared Application Gallery in which the Application Definition resides. | 
 **galleryApplicationName** | **String**| The name of the gallery Application Definition in which the Application Version is to be created. | 
 **galleryApplicationVersionName** | **String**| The name of the gallery Application Version to be created. Needs to follow semantic version name pattern: The allowed characters are digit and period. Digits must be within the range of a 32-bit integer. Format: &lt;MajorVersion&gt;.&lt;MinorVersion&gt;.&lt;Patch&gt; | 
 **apiVersion** | **String**| Client Api Version. | 
 **galleryApplicationVersion** | [**GalleryApplicationVersion**](GalleryApplicationVersion.md)| Parameters supplied to the create or update gallery Application Version operation. | 

### Return type

[**GalleryApplicationVersion**](GalleryApplicationVersion.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## galleryApplicationVersionsDelete

> galleryApplicationVersionsDelete(subscriptionId, resourceGroupName, galleryName, galleryApplicationName, galleryApplicationVersionName, apiVersion)



Delete a gallery Application Version.

### Example

```javascript
import SharedImageGalleryServiceClient from 'shared_image_gallery_service_client';
let defaultClient = SharedImageGalleryServiceClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SharedImageGalleryServiceClient.GalleryApplicationVersionsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let galleryName = "galleryName_example"; // String | The name of the Shared Application Gallery in which the Application Definition resides.
let galleryApplicationName = "galleryApplicationName_example"; // String | The name of the gallery Application Definition in which the Application Version resides.
let galleryApplicationVersionName = "galleryApplicationVersionName_example"; // String | The name of the gallery Application Version to be deleted.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.galleryApplicationVersionsDelete(subscriptionId, resourceGroupName, galleryName, galleryApplicationName, galleryApplicationVersionName, apiVersion, (error, data, response) => {
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
 **galleryName** | **String**| The name of the Shared Application Gallery in which the Application Definition resides. | 
 **galleryApplicationName** | **String**| The name of the gallery Application Definition in which the Application Version resides. | 
 **galleryApplicationVersionName** | **String**| The name of the gallery Application Version to be deleted. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## galleryApplicationVersionsGet

> GalleryApplicationVersion galleryApplicationVersionsGet(subscriptionId, resourceGroupName, galleryName, galleryApplicationName, galleryApplicationVersionName, apiVersion, opts)



Retrieves information about a gallery Application Version.

### Example

```javascript
import SharedImageGalleryServiceClient from 'shared_image_gallery_service_client';
let defaultClient = SharedImageGalleryServiceClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SharedImageGalleryServiceClient.GalleryApplicationVersionsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let galleryName = "galleryName_example"; // String | The name of the Shared Application Gallery in which the Application Definition resides.
let galleryApplicationName = "galleryApplicationName_example"; // String | The name of the gallery Application Definition in which the Application Version resides.
let galleryApplicationVersionName = "galleryApplicationVersionName_example"; // String | The name of the gallery Application Version to be retrieved.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'expand': "expand_example" // String | The expand expression to apply on the operation.
};
apiInstance.galleryApplicationVersionsGet(subscriptionId, resourceGroupName, galleryName, galleryApplicationName, galleryApplicationVersionName, apiVersion, opts, (error, data, response) => {
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
 **galleryName** | **String**| The name of the Shared Application Gallery in which the Application Definition resides. | 
 **galleryApplicationName** | **String**| The name of the gallery Application Definition in which the Application Version resides. | 
 **galleryApplicationVersionName** | **String**| The name of the gallery Application Version to be retrieved. | 
 **apiVersion** | **String**| Client Api Version. | 
 **expand** | **String**| The expand expression to apply on the operation. | [optional] 

### Return type

[**GalleryApplicationVersion**](GalleryApplicationVersion.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## galleryApplicationVersionsListByGalleryApplication

> GalleryApplicationVersionList galleryApplicationVersionsListByGalleryApplication(subscriptionId, resourceGroupName, galleryName, galleryApplicationName, apiVersion)



List gallery Application Versions in a gallery Application Definition.

### Example

```javascript
import SharedImageGalleryServiceClient from 'shared_image_gallery_service_client';
let defaultClient = SharedImageGalleryServiceClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SharedImageGalleryServiceClient.GalleryApplicationVersionsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let galleryName = "galleryName_example"; // String | The name of the Shared Application Gallery in which the Application Definition resides.
let galleryApplicationName = "galleryApplicationName_example"; // String | The name of the Shared Application Gallery Application Definition from which the Application Versions are to be listed.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.galleryApplicationVersionsListByGalleryApplication(subscriptionId, resourceGroupName, galleryName, galleryApplicationName, apiVersion, (error, data, response) => {
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
 **galleryName** | **String**| The name of the Shared Application Gallery in which the Application Definition resides. | 
 **galleryApplicationName** | **String**| The name of the Shared Application Gallery Application Definition from which the Application Versions are to be listed. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**GalleryApplicationVersionList**](GalleryApplicationVersionList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## galleryApplicationVersionsUpdate

> GalleryApplicationVersion galleryApplicationVersionsUpdate(subscriptionId, resourceGroupName, galleryName, galleryApplicationName, galleryApplicationVersionName, apiVersion, galleryApplicationVersion)



Update a gallery Application Version.

### Example

```javascript
import SharedImageGalleryServiceClient from 'shared_image_gallery_service_client';
let defaultClient = SharedImageGalleryServiceClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SharedImageGalleryServiceClient.GalleryApplicationVersionsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let galleryName = "galleryName_example"; // String | The name of the Shared Application Gallery in which the Application Definition resides.
let galleryApplicationName = "galleryApplicationName_example"; // String | The name of the gallery Application Definition in which the Application Version is to be updated.
let galleryApplicationVersionName = "galleryApplicationVersionName_example"; // String | The name of the gallery Application Version to be updated. Needs to follow semantic version name pattern: The allowed characters are digit and period. Digits must be within the range of a 32-bit integer. Format: <MajorVersion>.<MinorVersion>.<Patch>
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let galleryApplicationVersion = new SharedImageGalleryServiceClient.GalleryApplicationVersionUpdate(); // GalleryApplicationVersionUpdate | Parameters supplied to the update gallery Application Version operation.
apiInstance.galleryApplicationVersionsUpdate(subscriptionId, resourceGroupName, galleryName, galleryApplicationName, galleryApplicationVersionName, apiVersion, galleryApplicationVersion, (error, data, response) => {
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
 **galleryName** | **String**| The name of the Shared Application Gallery in which the Application Definition resides. | 
 **galleryApplicationName** | **String**| The name of the gallery Application Definition in which the Application Version is to be updated. | 
 **galleryApplicationVersionName** | **String**| The name of the gallery Application Version to be updated. Needs to follow semantic version name pattern: The allowed characters are digit and period. Digits must be within the range of a 32-bit integer. Format: &lt;MajorVersion&gt;.&lt;MinorVersion&gt;.&lt;Patch&gt; | 
 **apiVersion** | **String**| Client Api Version. | 
 **galleryApplicationVersion** | [**GalleryApplicationVersionUpdate**](GalleryApplicationVersionUpdate.md)| Parameters supplied to the update gallery Application Version operation. | 

### Return type

[**GalleryApplicationVersion**](GalleryApplicationVersion.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

