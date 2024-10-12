# SharedImageGalleryServiceClient.GalleryApplicationsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**galleryApplicationsCreateOrUpdate**](GalleryApplicationsApi.md#galleryApplicationsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/applications/{galleryApplicationName} | 
[**galleryApplicationsDelete**](GalleryApplicationsApi.md#galleryApplicationsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/applications/{galleryApplicationName} | 
[**galleryApplicationsGet**](GalleryApplicationsApi.md#galleryApplicationsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/applications/{galleryApplicationName} | 
[**galleryApplicationsListByGallery**](GalleryApplicationsApi.md#galleryApplicationsListByGallery) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/applications | 
[**galleryApplicationsUpdate**](GalleryApplicationsApi.md#galleryApplicationsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/applications/{galleryApplicationName} | 



## galleryApplicationsCreateOrUpdate

> GalleryApplication galleryApplicationsCreateOrUpdate(subscriptionId, resourceGroupName, galleryName, galleryApplicationName, apiVersion, galleryApplication)



Create or update a gallery Application Definition.

### Example

```javascript
import SharedImageGalleryServiceClient from 'shared_image_gallery_service_client';
let defaultClient = SharedImageGalleryServiceClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SharedImageGalleryServiceClient.GalleryApplicationsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let galleryName = "galleryName_example"; // String | The name of the Shared Application Gallery in which the Application Definition is to be created.
let galleryApplicationName = "galleryApplicationName_example"; // String | The name of the gallery Application Definition to be created or updated. The allowed characters are alphabets and numbers with dots, dashes, and periods allowed in the middle. The maximum length is 80 characters.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let galleryApplication = new SharedImageGalleryServiceClient.GalleryApplication(); // GalleryApplication | Parameters supplied to the create or update gallery Application operation.
apiInstance.galleryApplicationsCreateOrUpdate(subscriptionId, resourceGroupName, galleryName, galleryApplicationName, apiVersion, galleryApplication, (error, data, response) => {
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
 **galleryName** | **String**| The name of the Shared Application Gallery in which the Application Definition is to be created. | 
 **galleryApplicationName** | **String**| The name of the gallery Application Definition to be created or updated. The allowed characters are alphabets and numbers with dots, dashes, and periods allowed in the middle. The maximum length is 80 characters. | 
 **apiVersion** | **String**| Client Api Version. | 
 **galleryApplication** | [**GalleryApplication**](GalleryApplication.md)| Parameters supplied to the create or update gallery Application operation. | 

### Return type

[**GalleryApplication**](GalleryApplication.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## galleryApplicationsDelete

> galleryApplicationsDelete(subscriptionId, resourceGroupName, galleryName, galleryApplicationName, apiVersion)



Delete a gallery Application.

### Example

```javascript
import SharedImageGalleryServiceClient from 'shared_image_gallery_service_client';
let defaultClient = SharedImageGalleryServiceClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SharedImageGalleryServiceClient.GalleryApplicationsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let galleryName = "galleryName_example"; // String | The name of the Shared Application Gallery in which the Application Definition is to be deleted.
let galleryApplicationName = "galleryApplicationName_example"; // String | The name of the gallery Application Definition to be deleted.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.galleryApplicationsDelete(subscriptionId, resourceGroupName, galleryName, galleryApplicationName, apiVersion, (error, data, response) => {
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
 **galleryName** | **String**| The name of the Shared Application Gallery in which the Application Definition is to be deleted. | 
 **galleryApplicationName** | **String**| The name of the gallery Application Definition to be deleted. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## galleryApplicationsGet

> GalleryApplication galleryApplicationsGet(subscriptionId, resourceGroupName, galleryName, galleryApplicationName, apiVersion)



Retrieves information about a gallery Application Definition.

### Example

```javascript
import SharedImageGalleryServiceClient from 'shared_image_gallery_service_client';
let defaultClient = SharedImageGalleryServiceClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SharedImageGalleryServiceClient.GalleryApplicationsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let galleryName = "galleryName_example"; // String | The name of the Shared Application Gallery from which the Application Definitions are to be retrieved.
let galleryApplicationName = "galleryApplicationName_example"; // String | The name of the gallery Application Definition to be retrieved.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.galleryApplicationsGet(subscriptionId, resourceGroupName, galleryName, galleryApplicationName, apiVersion, (error, data, response) => {
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
 **galleryName** | **String**| The name of the Shared Application Gallery from which the Application Definitions are to be retrieved. | 
 **galleryApplicationName** | **String**| The name of the gallery Application Definition to be retrieved. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**GalleryApplication**](GalleryApplication.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## galleryApplicationsListByGallery

> GalleryApplicationList galleryApplicationsListByGallery(subscriptionId, resourceGroupName, galleryName, apiVersion)



List gallery Application Definitions in a gallery.

### Example

```javascript
import SharedImageGalleryServiceClient from 'shared_image_gallery_service_client';
let defaultClient = SharedImageGalleryServiceClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SharedImageGalleryServiceClient.GalleryApplicationsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let galleryName = "galleryName_example"; // String | The name of the Shared Application Gallery from which Application Definitions are to be listed.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.galleryApplicationsListByGallery(subscriptionId, resourceGroupName, galleryName, apiVersion, (error, data, response) => {
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
 **galleryName** | **String**| The name of the Shared Application Gallery from which Application Definitions are to be listed. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**GalleryApplicationList**](GalleryApplicationList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## galleryApplicationsUpdate

> GalleryApplication galleryApplicationsUpdate(subscriptionId, resourceGroupName, galleryName, galleryApplicationName, apiVersion, galleryApplication)



Update a gallery Application Definition.

### Example

```javascript
import SharedImageGalleryServiceClient from 'shared_image_gallery_service_client';
let defaultClient = SharedImageGalleryServiceClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SharedImageGalleryServiceClient.GalleryApplicationsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let galleryName = "galleryName_example"; // String | The name of the Shared Application Gallery in which the Application Definition is to be updated.
let galleryApplicationName = "galleryApplicationName_example"; // String | The name of the gallery Application Definition to be updated. The allowed characters are alphabets and numbers with dots, dashes, and periods allowed in the middle. The maximum length is 80 characters.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let galleryApplication = new SharedImageGalleryServiceClient.GalleryApplicationUpdate(); // GalleryApplicationUpdate | Parameters supplied to the update gallery Application operation.
apiInstance.galleryApplicationsUpdate(subscriptionId, resourceGroupName, galleryName, galleryApplicationName, apiVersion, galleryApplication, (error, data, response) => {
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
 **galleryName** | **String**| The name of the Shared Application Gallery in which the Application Definition is to be updated. | 
 **galleryApplicationName** | **String**| The name of the gallery Application Definition to be updated. The allowed characters are alphabets and numbers with dots, dashes, and periods allowed in the middle. The maximum length is 80 characters. | 
 **apiVersion** | **String**| Client Api Version. | 
 **galleryApplication** | [**GalleryApplicationUpdate**](GalleryApplicationUpdate.md)| Parameters supplied to the update gallery Application operation. | 

### Return type

[**GalleryApplication**](GalleryApplication.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

