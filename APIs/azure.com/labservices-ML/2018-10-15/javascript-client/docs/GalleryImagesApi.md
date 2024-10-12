# ManagedLabsClient.GalleryImagesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**galleryImagesCreateOrUpdate**](GalleryImagesApi.md#galleryImagesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/galleryimages/{galleryImageName} | 
[**galleryImagesDelete**](GalleryImagesApi.md#galleryImagesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/galleryimages/{galleryImageName} | 
[**galleryImagesGet**](GalleryImagesApi.md#galleryImagesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/galleryimages/{galleryImageName} | 
[**galleryImagesList**](GalleryImagesApi.md#galleryImagesList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/galleryimages | 
[**galleryImagesUpdate**](GalleryImagesApi.md#galleryImagesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/galleryimages/{galleryImageName} | 



## galleryImagesCreateOrUpdate

> GalleryImage galleryImagesCreateOrUpdate(subscriptionId, resourceGroupName, labAccountName, galleryImageName, apiVersion, galleryImage)



Create or replace an existing Gallery Image.

### Example

```javascript
import ManagedLabsClient from 'managed_labs_client';
let defaultClient = ManagedLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedLabsClient.GalleryImagesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labAccountName = "labAccountName_example"; // String | The name of the lab Account.
let galleryImageName = "galleryImageName_example"; // String | The name of the gallery Image.
let apiVersion = "'2018-10-15'"; // String | Client API version.
let galleryImage = new ManagedLabsClient.GalleryImage(); // GalleryImage | Represents an image from the Azure Marketplace
apiInstance.galleryImagesCreateOrUpdate(subscriptionId, resourceGroupName, labAccountName, galleryImageName, apiVersion, galleryImage, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **labAccountName** | **String**| The name of the lab Account. | 
 **galleryImageName** | **String**| The name of the gallery Image. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-10-15&#39;]
 **galleryImage** | [**GalleryImage**](GalleryImage.md)| Represents an image from the Azure Marketplace | 

### Return type

[**GalleryImage**](GalleryImage.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## galleryImagesDelete

> galleryImagesDelete(subscriptionId, resourceGroupName, labAccountName, galleryImageName, apiVersion)



Delete gallery image.

### Example

```javascript
import ManagedLabsClient from 'managed_labs_client';
let defaultClient = ManagedLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedLabsClient.GalleryImagesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labAccountName = "labAccountName_example"; // String | The name of the lab Account.
let galleryImageName = "galleryImageName_example"; // String | The name of the gallery Image.
let apiVersion = "'2018-10-15'"; // String | Client API version.
apiInstance.galleryImagesDelete(subscriptionId, resourceGroupName, labAccountName, galleryImageName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **labAccountName** | **String**| The name of the lab Account. | 
 **galleryImageName** | **String**| The name of the gallery Image. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-10-15&#39;]

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## galleryImagesGet

> GalleryImage galleryImagesGet(subscriptionId, resourceGroupName, labAccountName, galleryImageName, apiVersion, opts)



Get gallery image

### Example

```javascript
import ManagedLabsClient from 'managed_labs_client';
let defaultClient = ManagedLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedLabsClient.GalleryImagesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labAccountName = "labAccountName_example"; // String | The name of the lab Account.
let galleryImageName = "galleryImageName_example"; // String | The name of the gallery Image.
let apiVersion = "'2018-10-15'"; // String | Client API version.
let opts = {
  'expand': "expand_example" // String | Specify the $expand query. Example: 'properties($select=author)'
};
apiInstance.galleryImagesGet(subscriptionId, resourceGroupName, labAccountName, galleryImageName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **labAccountName** | **String**| The name of the lab Account. | 
 **galleryImageName** | **String**| The name of the gallery Image. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-10-15&#39;]
 **expand** | **String**| Specify the $expand query. Example: &#39;properties($select&#x3D;author)&#39; | [optional] 

### Return type

[**GalleryImage**](GalleryImage.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## galleryImagesList

> ResponseWithContinuationGalleryImage galleryImagesList(subscriptionId, resourceGroupName, labAccountName, apiVersion, opts)



List gallery images in a given lab account.

### Example

```javascript
import ManagedLabsClient from 'managed_labs_client';
let defaultClient = ManagedLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedLabsClient.GalleryImagesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labAccountName = "labAccountName_example"; // String | The name of the lab Account.
let apiVersion = "'2018-10-15'"; // String | Client API version.
let opts = {
  'expand': "expand_example", // String | Specify the $expand query. Example: 'properties($select=author)'
  'filter': "filter_example", // String | The filter to apply to the operation.
  'top': 56, // Number | The maximum number of resources to return from the operation.
  'orderby': "orderby_example" // String | The ordering expression for the results, using OData notation.
};
apiInstance.galleryImagesList(subscriptionId, resourceGroupName, labAccountName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **labAccountName** | **String**| The name of the lab Account. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-10-15&#39;]
 **expand** | **String**| Specify the $expand query. Example: &#39;properties($select&#x3D;author)&#39; | [optional] 
 **filter** | **String**| The filter to apply to the operation. | [optional] 
 **top** | **Number**| The maximum number of resources to return from the operation. | [optional] 
 **orderby** | **String**| The ordering expression for the results, using OData notation. | [optional] 

### Return type

[**ResponseWithContinuationGalleryImage**](ResponseWithContinuationGalleryImage.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## galleryImagesUpdate

> GalleryImage galleryImagesUpdate(subscriptionId, resourceGroupName, labAccountName, galleryImageName, apiVersion, galleryImage)



Modify properties of gallery images.

### Example

```javascript
import ManagedLabsClient from 'managed_labs_client';
let defaultClient = ManagedLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedLabsClient.GalleryImagesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labAccountName = "labAccountName_example"; // String | The name of the lab Account.
let galleryImageName = "galleryImageName_example"; // String | The name of the gallery Image.
let apiVersion = "'2018-10-15'"; // String | Client API version.
let galleryImage = new ManagedLabsClient.GalleryImageFragment(); // GalleryImageFragment | Represents an image from the Azure Marketplace
apiInstance.galleryImagesUpdate(subscriptionId, resourceGroupName, labAccountName, galleryImageName, apiVersion, galleryImage, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **labAccountName** | **String**| The name of the lab Account. | 
 **galleryImageName** | **String**| The name of the gallery Image. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-10-15&#39;]
 **galleryImage** | [**GalleryImageFragment**](GalleryImageFragment.md)| Represents an image from the Azure Marketplace | 

### Return type

[**GalleryImage**](GalleryImage.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

