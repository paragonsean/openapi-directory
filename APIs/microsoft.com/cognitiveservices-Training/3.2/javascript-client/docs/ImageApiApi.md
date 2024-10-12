# CustomVisionTrainingClient.ImageApiApi

All URIs are relative to *https://southcentralus.api.cognitive.microsoft.com/customvision/v3.2/training*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createImageRegions**](ImageApiApi.md#createImageRegions) | **POST** /projects/{projectId}/images/regions | Create a set of image regions.
[**createImageTags**](ImageApiApi.md#createImageTags) | **POST** /projects/{projectId}/images/tags | Associate a set of images with a set of tags.
[**createImagesFromData**](ImageApiApi.md#createImagesFromData) | **POST** /projects/{projectId}/images | Add the provided images to the set of training images.
[**createImagesFromFiles**](ImageApiApi.md#createImagesFromFiles) | **POST** /projects/{projectId}/images/files | Add the provided batch of images to the set of training images.
[**createImagesFromPredictions**](ImageApiApi.md#createImagesFromPredictions) | **POST** /projects/{projectId}/images/predictions | Add the specified predicted images to the set of training images.
[**createImagesFromUrls**](ImageApiApi.md#createImagesFromUrls) | **POST** /projects/{projectId}/images/urls | Add the provided images urls to the set of training images.
[**deleteImageRegions**](ImageApiApi.md#deleteImageRegions) | **DELETE** /projects/{projectId}/images/regions | Delete a set of image regions.
[**deleteImageTags**](ImageApiApi.md#deleteImageTags) | **DELETE** /projects/{projectId}/images/tags | Remove a set of tags from a set of images.
[**deleteImages**](ImageApiApi.md#deleteImages) | **DELETE** /projects/{projectId}/images | Delete images from the set of training images.
[**getImagesByIds**](ImageApiApi.md#getImagesByIds) | **GET** /projects/{projectId}/images/id | Get images by id for a given project iteration.
[**getTaggedImageCount**](ImageApiApi.md#getTaggedImageCount) | **GET** /projects/{projectId}/images/tagged/count | Gets the number of images tagged with the provided {tagIds}.
[**getTaggedImages**](ImageApiApi.md#getTaggedImages) | **GET** /projects/{projectId}/images/tagged | Get tagged images for a given project iteration.
[**getUntaggedImageCount**](ImageApiApi.md#getUntaggedImageCount) | **GET** /projects/{projectId}/images/untagged/count | Gets the number of untagged images.
[**getUntaggedImages**](ImageApiApi.md#getUntaggedImages) | **GET** /projects/{projectId}/images/untagged | Get untagged images for a given project iteration.
[**querySuggestedImageCount**](ImageApiApi.md#querySuggestedImageCount) | **POST** /projects/{projectId}/images/suggested/count | Get count of images whose suggested tags match given tags and their probabilities are greater than or equal to the given threshold. Returns count as 0 if none found.
[**querySuggestedImages**](ImageApiApi.md#querySuggestedImages) | **POST** /projects/{projectId}/images/suggested | Get untagged images whose suggested tags match given tags. Returns empty array if no images are found.



## createImageRegions

> ImageRegionCreateSummary createImageRegions(projectId, imageRegionCreateBatch)

Create a set of image regions.

This API accepts a batch of image regions, and optionally tags, to update existing images with region information.  There is a limit of 64 entries in the batch.

### Example

```javascript
import CustomVisionTrainingClient from 'custom_vision_training_client';
let defaultClient = CustomVisionTrainingClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new CustomVisionTrainingClient.ImageApiApi();
let projectId = "bc3f7dad-5544-468c-8573-3ef04d55463e"; // String | The project id.
let imageRegionCreateBatch = new CustomVisionTrainingClient.ImageRegionCreateBatch(); // ImageRegionCreateBatch | Batch of image regions which include a tag and bounding box. Limited to 64.
apiInstance.createImageRegions(projectId, imageRegionCreateBatch, (error, data, response) => {
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
 **projectId** | **String**| The project id. | 
 **imageRegionCreateBatch** | [**ImageRegionCreateBatch**](ImageRegionCreateBatch.md)| Batch of image regions which include a tag and bounding box. Limited to 64. | 

### Return type

[**ImageRegionCreateSummary**](ImageRegionCreateSummary.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
- **Accept**: application/json, application/xml, text/xml


## createImageTags

> ImageTagCreateSummary createImageTags(projectId, imageTagCreateBatch)

Associate a set of images with a set of tags.

### Example

```javascript
import CustomVisionTrainingClient from 'custom_vision_training_client';
let defaultClient = CustomVisionTrainingClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new CustomVisionTrainingClient.ImageApiApi();
let projectId = "bc3f7dad-5544-468c-8573-3ef04d55463e"; // String | The project id.
let imageTagCreateBatch = new CustomVisionTrainingClient.ImageTagCreateBatch(); // ImageTagCreateBatch | Batch of image tags. Limited to 128 tags per batch.
apiInstance.createImageTags(projectId, imageTagCreateBatch, (error, data, response) => {
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
 **projectId** | **String**| The project id. | 
 **imageTagCreateBatch** | [**ImageTagCreateBatch**](ImageTagCreateBatch.md)| Batch of image tags. Limited to 128 tags per batch. | 

### Return type

[**ImageTagCreateSummary**](ImageTagCreateSummary.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
- **Accept**: application/json, application/xml, text/xml


## createImagesFromData

> ImageCreateSummary createImagesFromData(projectId, imageData, opts)

Add the provided images to the set of training images.

This API accepts body content as multipart/form-data and application/octet-stream. When using multipart  multiple image files can be sent at once, with a maximum of 64 files

### Example

```javascript
import CustomVisionTrainingClient from 'custom_vision_training_client';
let defaultClient = CustomVisionTrainingClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new CustomVisionTrainingClient.ImageApiApi();
let projectId = "64b822c5-8082-4b36-a426-27225f4aa18c"; // String | The project id.
let imageData = "/path/to/file"; // File | Binary image data. Supported formats are JPEG, GIF, PNG, and BMP. Supports images up to 6MB.
let opts = {
  'tagIds': ["null"] // [String] | The tags ids with which to tag each image. Limited to 20.
};
apiInstance.createImagesFromData(projectId, imageData, opts, (error, data, response) => {
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
 **projectId** | **String**| The project id. | 
 **imageData** | **File**| Binary image data. Supported formats are JPEG, GIF, PNG, and BMP. Supports images up to 6MB. | 
 **tagIds** | [**[String]**](String.md)| The tags ids with which to tag each image. Limited to 20. | [optional] 

### Return type

[**ImageCreateSummary**](ImageCreateSummary.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json, application/xml, text/xml


## createImagesFromFiles

> ImageCreateSummary createImagesFromFiles(projectId, imageFileCreateBatch)

Add the provided batch of images to the set of training images.

This API accepts a batch of files, and optionally tags, to create images. There is a limit of 64 images and 20 tags.

### Example

```javascript
import CustomVisionTrainingClient from 'custom_vision_training_client';
let defaultClient = CustomVisionTrainingClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new CustomVisionTrainingClient.ImageApiApi();
let projectId = "64b822c5-8082-4b36-a426-27225f4aa18c"; // String | The project id.
let imageFileCreateBatch = new CustomVisionTrainingClient.ImageFileCreateBatch(); // ImageFileCreateBatch | The batch of image files to add. Limited to 64 images and 20 tags per batch.
apiInstance.createImagesFromFiles(projectId, imageFileCreateBatch, (error, data, response) => {
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
 **projectId** | **String**| The project id. | 
 **imageFileCreateBatch** | [**ImageFileCreateBatch**](ImageFileCreateBatch.md)| The batch of image files to add. Limited to 64 images and 20 tags per batch. | 

### Return type

[**ImageCreateSummary**](ImageCreateSummary.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
- **Accept**: application/json, application/xml, text/xml


## createImagesFromPredictions

> ImageCreateSummary createImagesFromPredictions(projectId, imageIdCreateBatch)

Add the specified predicted images to the set of training images.

This API creates a batch of images from predicted images specified. There is a limit of 64 images and 20 tags.

### Example

```javascript
import CustomVisionTrainingClient from 'custom_vision_training_client';
let defaultClient = CustomVisionTrainingClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new CustomVisionTrainingClient.ImageApiApi();
let projectId = "64b822c5-8082-4b36-a426-27225f4aa18c"; // String | The project id.
let imageIdCreateBatch = new CustomVisionTrainingClient.ImageIdCreateBatch(); // ImageIdCreateBatch | Image and tag ids. Limited to 64 images and 20 tags per batch.
apiInstance.createImagesFromPredictions(projectId, imageIdCreateBatch, (error, data, response) => {
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
 **projectId** | **String**| The project id. | 
 **imageIdCreateBatch** | [**ImageIdCreateBatch**](ImageIdCreateBatch.md)| Image and tag ids. Limited to 64 images and 20 tags per batch. | 

### Return type

[**ImageCreateSummary**](ImageCreateSummary.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
- **Accept**: application/json, application/xml, text/xml


## createImagesFromUrls

> ImageCreateSummary createImagesFromUrls(projectId, imageUrlCreateBatch)

Add the provided images urls to the set of training images.

This API accepts a batch of urls, and optionally tags, to create images. There is a limit of 64 images and 20 tags.

### Example

```javascript
import CustomVisionTrainingClient from 'custom_vision_training_client';
let defaultClient = CustomVisionTrainingClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new CustomVisionTrainingClient.ImageApiApi();
let projectId = "64b822c5-8082-4b36-a426-27225f4aa18c"; // String | The project id.
let imageUrlCreateBatch = new CustomVisionTrainingClient.ImageUrlCreateBatch(); // ImageUrlCreateBatch | Image urls and tag ids. Limited to 64 images and 20 tags per batch.
apiInstance.createImagesFromUrls(projectId, imageUrlCreateBatch, (error, data, response) => {
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
 **projectId** | **String**| The project id. | 
 **imageUrlCreateBatch** | [**ImageUrlCreateBatch**](ImageUrlCreateBatch.md)| Image urls and tag ids. Limited to 64 images and 20 tags per batch. | 

### Return type

[**ImageCreateSummary**](ImageCreateSummary.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
- **Accept**: application/json, application/xml, text/xml


## deleteImageRegions

> deleteImageRegions(projectId, regionIds)

Delete a set of image regions.

### Example

```javascript
import CustomVisionTrainingClient from 'custom_vision_training_client';
let defaultClient = CustomVisionTrainingClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new CustomVisionTrainingClient.ImageApiApi();
let projectId = "bc3f7dad-5544-468c-8573-3ef04d55463e"; // String | The project id.
let regionIds = ["null"]; // [String] | Regions to delete. Limited to 64.
apiInstance.deleteImageRegions(projectId, regionIds, (error, data, response) => {
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
 **projectId** | **String**| The project id. | 
 **regionIds** | [**[String]**](String.md)| Regions to delete. Limited to 64. | 

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## deleteImageTags

> deleteImageTags(projectId, imageIds, tagIds)

Remove a set of tags from a set of images.

### Example

```javascript
import CustomVisionTrainingClient from 'custom_vision_training_client';
let defaultClient = CustomVisionTrainingClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new CustomVisionTrainingClient.ImageApiApi();
let projectId = "64b822c5-8082-4b36-a426-27225f4aa18c"; // String | The project id.
let imageIds = ["null"]; // [String] | Image ids. Limited to 64 images.
let tagIds = ["null"]; // [String] | Tags to be deleted from the specified images. Limited to 20 tags.
apiInstance.deleteImageTags(projectId, imageIds, tagIds, (error, data, response) => {
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
 **projectId** | **String**| The project id. | 
 **imageIds** | [**[String]**](String.md)| Image ids. Limited to 64 images. | 
 **tagIds** | [**[String]**](String.md)| Tags to be deleted from the specified images. Limited to 20 tags. | 

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## deleteImages

> deleteImages(projectId, opts)

Delete images from the set of training images.

### Example

```javascript
import CustomVisionTrainingClient from 'custom_vision_training_client';
let defaultClient = CustomVisionTrainingClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new CustomVisionTrainingClient.ImageApiApi();
let projectId = "64b822c5-8082-4b36-a426-27225f4aa18c"; // String | The project id.
let opts = {
  'imageIds': ["null"], // [String] | Ids of the images to be deleted. Limited to 256 images per batch.
  'allImages': true, // Boolean | Flag to specify delete all images, specify this flag or a list of images. Using this flag will return a 202 response to indicate the images are being deleted.
  'allIterations': true // Boolean | Removes these images from all iterations, not just the current workspace. Using this flag will return a 202 response to indicate the images are being deleted.
};
apiInstance.deleteImages(projectId, opts, (error, data, response) => {
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
 **projectId** | **String**| The project id. | 
 **imageIds** | [**[String]**](String.md)| Ids of the images to be deleted. Limited to 256 images per batch. | [optional] 
 **allImages** | **Boolean**| Flag to specify delete all images, specify this flag or a list of images. Using this flag will return a 202 response to indicate the images are being deleted. | [optional] 
 **allIterations** | **Boolean**| Removes these images from all iterations, not just the current workspace. Using this flag will return a 202 response to indicate the images are being deleted. | [optional] 

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/xml


## getImagesByIds

> [Image] getImagesByIds(projectId, opts)

Get images by id for a given project iteration.

This API will return a set of Images for the specified tags and optionally iteration. If no iteration is specified the  current workspace is used.

### Example

```javascript
import CustomVisionTrainingClient from 'custom_vision_training_client';
let defaultClient = CustomVisionTrainingClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new CustomVisionTrainingClient.ImageApiApi();
let projectId = "bc3f7dad-5544-468c-8573-3ef04d55463e"; // String | The project id.
let opts = {
  'imageIds': ["null"], // [String] | The list of image ids to retrieve. Limited to 256.
  'iterationId': "cf0f83fb-ebaa-4b25-8e34-613a6a0b8a12" // String | The iteration id. Defaults to workspace.
};
apiInstance.getImagesByIds(projectId, opts, (error, data, response) => {
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
 **projectId** | **String**| The project id. | 
 **imageIds** | [**[String]**](String.md)| The list of image ids to retrieve. Limited to 256. | [optional] 
 **iterationId** | **String**| The iteration id. Defaults to workspace. | [optional] 

### Return type

[**[Image]**](Image.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/xml


## getTaggedImageCount

> Number getTaggedImageCount(projectId, opts)

Gets the number of images tagged with the provided {tagIds}.

The filtering is on an and/or relationship. For example, if the provided tag ids are for the \&quot;Dog\&quot; and  \&quot;Cat\&quot; tags, then only images tagged with Dog and/or Cat will be returned

### Example

```javascript
import CustomVisionTrainingClient from 'custom_vision_training_client';
let defaultClient = CustomVisionTrainingClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new CustomVisionTrainingClient.ImageApiApi();
let projectId = "bc3f7dad-5544-468c-8573-3ef04d55463e"; // String | The project id.
let opts = {
  'iterationId': "cf0f83fb-ebaa-4b25-8e34-613a6a0b8a12", // String | The iteration id. Defaults to workspace.
  'tagIds': ["null"] // [String] | A list of tags ids to filter the images to count. Defaults to all tags when null.
};
apiInstance.getTaggedImageCount(projectId, opts, (error, data, response) => {
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
 **projectId** | **String**| The project id. | 
 **iterationId** | **String**| The iteration id. Defaults to workspace. | [optional] 
 **tagIds** | [**[String]**](String.md)| A list of tags ids to filter the images to count. Defaults to all tags when null. | [optional] 

### Return type

**Number**

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/xml


## getTaggedImages

> [Image] getTaggedImages(projectId, opts)

Get tagged images for a given project iteration.

This API supports batching and range selection. By default it will only return first 50 images matching images.  Use the {take} and {skip} parameters to control how many images to return in a given batch.  The filtering is on an and/or relationship. For example, if the provided tag ids are for the \&quot;Dog\&quot; and  \&quot;Cat\&quot; tags, then only images tagged with Dog and/or Cat will be returned

### Example

```javascript
import CustomVisionTrainingClient from 'custom_vision_training_client';
let defaultClient = CustomVisionTrainingClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new CustomVisionTrainingClient.ImageApiApi();
let projectId = "bc3f7dad-5544-468c-8573-3ef04d55463e"; // String | The project id.
let opts = {
  'iterationId': "cf0f83fb-ebaa-4b25-8e34-613a6a0b8a12", // String | The iteration id. Defaults to workspace.
  'tagIds': ["null"], // [String] | A list of tags ids to filter the images. Defaults to all tagged images when null. Limited to 20.
  'orderBy': "orderBy_example", // String | The ordering. Defaults to newest.
  'take': 50, // Number | Maximum number of images to return. Defaults to 50, limited to 256.
  'skip': 0 // Number | Number of images to skip before beginning the image batch. Defaults to 0.
};
apiInstance.getTaggedImages(projectId, opts, (error, data, response) => {
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
 **projectId** | **String**| The project id. | 
 **iterationId** | **String**| The iteration id. Defaults to workspace. | [optional] 
 **tagIds** | [**[String]**](String.md)| A list of tags ids to filter the images. Defaults to all tagged images when null. Limited to 20. | [optional] 
 **orderBy** | **String**| The ordering. Defaults to newest. | [optional] 
 **take** | **Number**| Maximum number of images to return. Defaults to 50, limited to 256. | [optional] [default to 50]
 **skip** | **Number**| Number of images to skip before beginning the image batch. Defaults to 0. | [optional] [default to 0]

### Return type

[**[Image]**](Image.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/xml


## getUntaggedImageCount

> Number getUntaggedImageCount(projectId, opts)

Gets the number of untagged images.

This API returns the images which have no tags for a given project and optionally an iteration. If no iteration is specified the  current workspace is used.

### Example

```javascript
import CustomVisionTrainingClient from 'custom_vision_training_client';
let defaultClient = CustomVisionTrainingClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new CustomVisionTrainingClient.ImageApiApi();
let projectId = "bc3f7dad-5544-468c-8573-3ef04d55463e"; // String | The project id.
let opts = {
  'iterationId': "cf0f83fb-ebaa-4b25-8e34-613a6a0b8a12" // String | The iteration id. Defaults to workspace.
};
apiInstance.getUntaggedImageCount(projectId, opts, (error, data, response) => {
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
 **projectId** | **String**| The project id. | 
 **iterationId** | **String**| The iteration id. Defaults to workspace. | [optional] 

### Return type

**Number**

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/xml


## getUntaggedImages

> [Image] getUntaggedImages(projectId, opts)

Get untagged images for a given project iteration.

This API supports batching and range selection. By default it will only return first 50 images matching images.  Use the {take} and {skip} parameters to control how many images to return in a given batch.

### Example

```javascript
import CustomVisionTrainingClient from 'custom_vision_training_client';
let defaultClient = CustomVisionTrainingClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new CustomVisionTrainingClient.ImageApiApi();
let projectId = "bc3f7dad-5544-468c-8573-3ef04d55463e"; // String | The project id.
let opts = {
  'iterationId': "cf0f83fb-ebaa-4b25-8e34-613a6a0b8a12", // String | The iteration id. Defaults to workspace.
  'orderBy': "orderBy_example", // String | The ordering. Defaults to newest.
  'take': 50, // Number | Maximum number of images to return. Defaults to 50, limited to 256.
  'skip': 0 // Number | Number of images to skip before beginning the image batch. Defaults to 0.
};
apiInstance.getUntaggedImages(projectId, opts, (error, data, response) => {
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
 **projectId** | **String**| The project id. | 
 **iterationId** | **String**| The iteration id. Defaults to workspace. | [optional] 
 **orderBy** | **String**| The ordering. Defaults to newest. | [optional] 
 **take** | **Number**| Maximum number of images to return. Defaults to 50, limited to 256. | [optional] [default to 50]
 **skip** | **Number**| Number of images to skip before beginning the image batch. Defaults to 0. | [optional] [default to 0]

### Return type

[**[Image]**](Image.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/xml


## querySuggestedImageCount

> {String: Number} querySuggestedImageCount(projectId, iterationId, tagFilter)

Get count of images whose suggested tags match given tags and their probabilities are greater than or equal to the given threshold. Returns count as 0 if none found.

This API takes in tagIds to get count of untagged images per suggested tags for a given threshold.

### Example

```javascript
import CustomVisionTrainingClient from 'custom_vision_training_client';
let defaultClient = CustomVisionTrainingClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new CustomVisionTrainingClient.ImageApiApi();
let projectId = "bc3f7dad-5544-468c-8573-3ef04d55463e"; // String | The project id.
let iterationId = "b7b9d99c-a2c6-4658-9900-a98d2ff5bc66"; // String | IterationId to use for the suggested tags and regions.
let tagFilter = new CustomVisionTrainingClient.TagFilter(); // TagFilter | Model that contains tagIds, threshold and projectType to query by.
apiInstance.querySuggestedImageCount(projectId, iterationId, tagFilter, (error, data, response) => {
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
 **projectId** | **String**| The project id. | 
 **iterationId** | **String**| IterationId to use for the suggested tags and regions. | 
 **tagFilter** | [**TagFilter**](TagFilter.md)| Model that contains tagIds, threshold and projectType to query by. | 

### Return type

**{String: Number}**

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
- **Accept**: application/json, application/xml, text/xml


## querySuggestedImages

> SuggestedTagAndRegionQuery querySuggestedImages(projectId, iterationId, suggestedTagAndRegionQueryToken)

Get untagged images whose suggested tags match given tags. Returns empty array if no images are found.

This API will fetch untagged images filtered by suggested tags Ids. It returns an empty array if no images are found.

### Example

```javascript
import CustomVisionTrainingClient from 'custom_vision_training_client';
let defaultClient = CustomVisionTrainingClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new CustomVisionTrainingClient.ImageApiApi();
let projectId = "bc3f7dad-5544-468c-8573-3ef04d55463e"; // String | The project id.
let iterationId = "b7b9d99c-a2c6-4658-9900-a98d2ff5bc66"; // String | IterationId to use for the suggested tags and regions.
let suggestedTagAndRegionQueryToken = new CustomVisionTrainingClient.SuggestedTagAndRegionQueryToken(); // SuggestedTagAndRegionQueryToken | Contains properties we need to query suggested images.
apiInstance.querySuggestedImages(projectId, iterationId, suggestedTagAndRegionQueryToken, (error, data, response) => {
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
 **projectId** | **String**| The project id. | 
 **iterationId** | **String**| IterationId to use for the suggested tags and regions. | 
 **suggestedTagAndRegionQueryToken** | [**SuggestedTagAndRegionQueryToken**](SuggestedTagAndRegionQueryToken.md)| Contains properties we need to query suggested images. | 

### Return type

[**SuggestedTagAndRegionQuery**](SuggestedTagAndRegionQuery.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
- **Accept**: application/json, application/xml, text/xml

