# GalleryManagementClient.GalleryItemsApi

All URIs are relative to *https://adminmanagement.local.azurestack.external*

Method | HTTP request | Description
------------- | ------------- | -------------
[**galleryItemsCreate**](GalleryItemsApi.md#galleryItemsCreate) | **POST** /subscriptions/{subscriptionId}/providers/microsoft.gallery.admin/galleryItems | Uploads a provider gallery item to the storage.
[**galleryItemsDelete**](GalleryItemsApi.md#galleryItemsDelete) | **DELETE** /subscriptions/{subscriptionId}/providers/microsoft.gallery.admin/galleryItems/{galleryItemName} | Delete a specific gallery item.
[**galleryItemsGet**](GalleryItemsApi.md#galleryItemsGet) | **GET** /subscriptions/{subscriptionId}/providers/microsoft.gallery.admin/galleryItems/{galleryItemName} | Get a specific gallery item.
[**galleryItemsList**](GalleryItemsApi.md#galleryItemsList) | **GET** /subscriptions/{subscriptionId}/providers/microsoft.gallery.admin/galleryItems | Lists gallery items.



## galleryItemsCreate

> GalleryItem galleryItemsCreate(subscriptionId, apiVersion, galleryItemUriPayload)

Uploads a provider gallery item to the storage.

### Example

```javascript
import GalleryManagementClient from 'gallery_management_client';
let defaultClient = GalleryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GalleryManagementClient.GalleryItemsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "'2016-05-01'"; // String | Client API Version.
let galleryItemUriPayload = new GalleryManagementClient.GalleryItemUriPayload(); // GalleryItemUriPayload | The URI to the gallery item JSON file.
apiInstance.galleryItemsCreate(subscriptionId, apiVersion, galleryItemUriPayload, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client API Version. | [default to &#39;2016-05-01&#39;]
 **galleryItemUriPayload** | [**GalleryItemUriPayload**](GalleryItemUriPayload.md)| The URI to the gallery item JSON file. | 

### Return type

[**GalleryItem**](GalleryItem.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## galleryItemsDelete

> galleryItemsDelete(subscriptionId, galleryItemName, apiVersion)

Delete a specific gallery item.

### Example

```javascript
import GalleryManagementClient from 'gallery_management_client';
let defaultClient = GalleryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GalleryManagementClient.GalleryItemsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let galleryItemName = "galleryItemName_example"; // String | Identity of the gallery item. Includes publisher name, item name, and may include version separated by period character.
let apiVersion = "'2016-05-01'"; // String | Client API Version.
apiInstance.galleryItemsDelete(subscriptionId, galleryItemName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **galleryItemName** | **String**| Identity of the gallery item. Includes publisher name, item name, and may include version separated by period character. | 
 **apiVersion** | **String**| Client API Version. | [default to &#39;2016-05-01&#39;]

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## galleryItemsGet

> GalleryItem galleryItemsGet(subscriptionId, galleryItemName, apiVersion)

Get a specific gallery item.

### Example

```javascript
import GalleryManagementClient from 'gallery_management_client';
let defaultClient = GalleryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GalleryManagementClient.GalleryItemsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let galleryItemName = "galleryItemName_example"; // String | Identity of the gallery item. Includes publisher name, item name, and may include version separated by period character.
let apiVersion = "'2016-05-01'"; // String | Client API Version.
apiInstance.galleryItemsGet(subscriptionId, galleryItemName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **galleryItemName** | **String**| Identity of the gallery item. Includes publisher name, item name, and may include version separated by period character. | 
 **apiVersion** | **String**| Client API Version. | [default to &#39;2016-05-01&#39;]

### Return type

[**GalleryItem**](GalleryItem.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## galleryItemsList

> GalleryItemList galleryItemsList(subscriptionId, apiVersion)

Lists gallery items.

### Example

```javascript
import GalleryManagementClient from 'gallery_management_client';
let defaultClient = GalleryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GalleryManagementClient.GalleryItemsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "'2016-05-01'"; // String | Client API Version.
apiInstance.galleryItemsList(subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client API Version. | [default to &#39;2016-05-01&#39;]

### Return type

[**GalleryItemList**](GalleryItemList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

