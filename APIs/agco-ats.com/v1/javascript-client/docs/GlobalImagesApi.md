# AgcoApi.GlobalImagesApi

All URIs are relative to *https://secure.agco-ats.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**globalImagesDeleteFile**](GlobalImagesApi.md#globalImagesDeleteFile) | **DELETE** /api/v2/GlobalImages/{ID} | Mark a file as &#39;Removed&#39;. Disables download of the image and hides metadata from GET all method
[**globalImagesGetGlobalImage**](GlobalImagesApi.md#globalImagesGetGlobalImage) | **GET** /api/v2/GlobalImages/{ID} | Gets a GlobalImage&#39;s metadata.
[**globalImagesGetGlobalImageContents**](GlobalImagesApi.md#globalImagesGetGlobalImageContents) | **GET** /api/v2/GlobalImages/{ID}/ImageContents | Download the contents of a GlobalImage. The current State of the GlobalImage should be &#39;Available&#39;.
[**globalImagesGetGlobalImages**](GlobalImagesApi.md#globalImagesGetGlobalImages) | **GET** /api/v2/GlobalImages | Get a paged response of GlobalImage.
[**globalImagesPostGlobalImage**](GlobalImagesApi.md#globalImagesPostGlobalImage) | **POST** /api/v2/GlobalImages | Create the metadata for a GlobalImage before uploading. The State should be &#39;Created&#39;.
[**globalImagesPutGlobalImage**](GlobalImagesApi.md#globalImagesPutGlobalImage) | **PUT** /api/v2/GlobalImages/{ID} | Update the metadata for an image.
[**globalImagesPutGlobalImageContents**](GlobalImagesApi.md#globalImagesPutGlobalImageContents) | **PUT** /api/v2/GlobalImages/{ID}/ImageContents | Upload the contents of a GlobalImage. The current State of the File for the GlobalImage should be &#39;Created&#39;.



## globalImagesDeleteFile

> globalImagesDeleteFile(ID)

Mark a file as &#39;Removed&#39;. Disables download of the image and hides metadata from GET all method

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.GlobalImagesApi();
let ID = "ID_example"; // String | The GlobalImage's id.
apiInstance.globalImagesDeleteFile(ID, (error, data, response) => {
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
 **ID** | **String**| The GlobalImage&#39;s id. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## globalImagesGetGlobalImage

> GlobalResourcesSharedModelsGlobalImage globalImagesGetGlobalImage(ID)

Gets a GlobalImage&#39;s metadata.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.GlobalImagesApi();
let ID = "ID_example"; // String | The GlobalImage's id.
apiInstance.globalImagesGetGlobalImage(ID, (error, data, response) => {
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
 **ID** | **String**| The GlobalImage&#39;s id. | 

### Return type

[**GlobalResourcesSharedModelsGlobalImage**](GlobalResourcesSharedModelsGlobalImage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## globalImagesGetGlobalImageContents

> Object globalImagesGetGlobalImageContents(ID, opts)

Download the contents of a GlobalImage. The current State of the GlobalImage should be &#39;Available&#39;.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.GlobalImagesApi();
let ID = "ID_example"; // String | The global image metadata id.
let opts = {
  'isFullImage': true // Boolean | Indicated whether to download the full image or the thumbnail. Defaults to 'true'.
};
apiInstance.globalImagesGetGlobalImageContents(ID, opts, (error, data, response) => {
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
 **ID** | **String**| The global image metadata id. | 
 **isFullImage** | **Boolean**| Indicated whether to download the full image or the thumbnail. Defaults to &#39;true&#39;. | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## globalImagesGetGlobalImages

> APIIPagedResponseGlobalResourcesSharedModelsGlobalImage globalImagesGetGlobalImages(opts)

Get a paged response of GlobalImage.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.GlobalImagesApi();
let opts = {
  'search': "search_example", // String | Optional. Searches for matching global images with the matching Category Name, Publisher or Description
  'categoryId': "categoryId_example", // String | 
  'publisher': "publisher_example", // String | 
  'includeDeleted': true, // Boolean | Indicates whether to include GlobalImages marked as removed.
  'limit': 56, // Number | Optional. The page limit. The default page limit is 10.
  'offset': 56 // Number | Optional. The page offset. The default page offset is 0.
};
apiInstance.globalImagesGetGlobalImages(opts, (error, data, response) => {
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
 **search** | **String**| Optional. Searches for matching global images with the matching Category Name, Publisher or Description | [optional] 
 **categoryId** | **String**|  | [optional] 
 **publisher** | **String**|  | [optional] 
 **includeDeleted** | **Boolean**| Indicates whether to include GlobalImages marked as removed. | [optional] 
 **limit** | **Number**| Optional. The page limit. The default page limit is 10. | [optional] 
 **offset** | **Number**| Optional. The page offset. The default page offset is 0. | [optional] 

### Return type

[**APIIPagedResponseGlobalResourcesSharedModelsGlobalImage**](APIIPagedResponseGlobalResourcesSharedModelsGlobalImage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## globalImagesPostGlobalImage

> String globalImagesPostGlobalImage(globalResourcesSharedModelsGlobalImage, opts)

Create the metadata for a GlobalImage before uploading. The State should be &#39;Created&#39;.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.GlobalImagesApi();
let globalResourcesSharedModelsGlobalImage = new AgcoApi.GlobalResourcesSharedModelsGlobalImage(); // GlobalResourcesSharedModelsGlobalImage | The file's metadata.
let opts = {
  'overridePublisherOrDate': true // Boolean | Whether to set the publisher and date to the provided values.
};
apiInstance.globalImagesPostGlobalImage(globalResourcesSharedModelsGlobalImage, opts, (error, data, response) => {
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
 **globalResourcesSharedModelsGlobalImage** | [**GlobalResourcesSharedModelsGlobalImage**](GlobalResourcesSharedModelsGlobalImage.md)| The file&#39;s metadata. | 
 **overridePublisherOrDate** | **Boolean**| Whether to set the publisher and date to the provided values. | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## globalImagesPutGlobalImage

> globalImagesPutGlobalImage(ID, globalResourcesSharedModelsGlobalImage, opts)

Update the metadata for an image.

Update the metadata for an image. Size may not be modified by the client.                   Set status to &#39;Available&#39; to publish an image. Both the image and thumbnail must be uploaded.                  Set status to &#39;Created&#39; to reset an image&#39;s contents and re-upload.                   A file may only be &#39;Removed&#39; by the DELETE method.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.GlobalImagesApi();
let ID = "ID_example"; // String | The GlobalImage's id.
let globalResourcesSharedModelsGlobalImage = new AgcoApi.GlobalResourcesSharedModelsGlobalImage(); // GlobalResourcesSharedModelsGlobalImage | The GlobalImage's metadata
let opts = {
  'overridePublisherOrDate': true // Boolean | Whether to set the publisher and date to the provided values.
};
apiInstance.globalImagesPutGlobalImage(ID, globalResourcesSharedModelsGlobalImage, opts, (error, data, response) => {
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
 **ID** | **String**| The GlobalImage&#39;s id. | 
 **globalResourcesSharedModelsGlobalImage** | [**GlobalResourcesSharedModelsGlobalImage**](GlobalResourcesSharedModelsGlobalImage.md)| The GlobalImage&#39;s metadata | 
 **overridePublisherOrDate** | **Boolean**| Whether to set the publisher and date to the provided values. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: */*


## globalImagesPutGlobalImageContents

> Object globalImagesPutGlobalImageContents(ID, opts)

Upload the contents of a GlobalImage. The current State of the File for the GlobalImage should be &#39;Created&#39;.

Both the image and thumbnail must be uploaded.                  Set isFullImage &#x3D; &#39;True&#39; for Full Image, isFullImage &#x3D; &#39;False&#39; for Thumbnail

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.GlobalImagesApi();
let ID = "ID_example"; // String | The global image metadata id.
let opts = {
  'isFullImage': true // Boolean | Indicated whether this is the full image or the thumbnail. Defaults to 'true'.
};
apiInstance.globalImagesPutGlobalImageContents(ID, opts, (error, data, response) => {
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
 **ID** | **String**| The global image metadata id. | 
 **isFullImage** | **Boolean**| Indicated whether this is the full image or the thumbnail. Defaults to &#39;true&#39;. | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml

