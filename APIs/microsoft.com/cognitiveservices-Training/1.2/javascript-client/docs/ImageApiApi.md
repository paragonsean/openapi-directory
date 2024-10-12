# TrainingApi.ImageApiApi

All URIs are relative to *https://southcentralus.api.cognitive.microsoft.com/customvision/v1.2/Training*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createImagesFromData**](ImageApiApi.md#createImagesFromData) | **POST** /projects/{projectId}/images | Add the provided images to the set of training images
[**createImagesFromFiles**](ImageApiApi.md#createImagesFromFiles) | **POST** /projects/{projectId}/images/files | Add the provided batch of images to the set of training images
[**createImagesFromPredictions**](ImageApiApi.md#createImagesFromPredictions) | **POST** /projects/{projectId}/images/predictions | Add the specified predicted images to the set of training images
[**createImagesFromUrls**](ImageApiApi.md#createImagesFromUrls) | **POST** /projects/{projectId}/images/urls | Add the provided images urls to the set of training images
[**deleteImageTags**](ImageApiApi.md#deleteImageTags) | **DELETE** /projects/{projectId}/images/tags | Remove a set of tags from a set of images
[**deleteImages**](ImageApiApi.md#deleteImages) | **DELETE** /projects/{projectId}/images | Delete images from the set of training images
[**getTaggedImages**](ImageApiApi.md#getTaggedImages) | **GET** /projects/{projectId}/images/tagged | Get tagged images for a given project iteration
[**getUntaggedImages**](ImageApiApi.md#getUntaggedImages) | **GET** /projects/{projectId}/images/untagged | Get untagged images for a given project iteration
[**postImageTags**](ImageApiApi.md#postImageTags) | **POST** /projects/{projectId}/images/tags | Associate a set of images with a set of tags



## createImagesFromData

> ImageCreateSummary createImagesFromData(projectId, trainingKey, imageData, opts)

Add the provided images to the set of training images

This API accepts body content as multipart/form-data and application/octet-stream. When using multipart  multiple image files can be sent at once, with a maximum of 64 files

### Example

```javascript
import TrainingApi from 'training_api';

let apiInstance = new TrainingApi.ImageApiApi();
let projectId = "64b822c5-8082-4b36-a426-27225f4aa18c"; // String | The project id
let trainingKey = "{API Key}"; // String | 
let imageData = "/path/to/file"; // File | 
let opts = {
  'tagIds': ["null"] // [String] | The tags ids with which to tag each image. Limited to 20
};
apiInstance.createImagesFromData(projectId, trainingKey, imageData, opts, (error, data, response) => {
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
 **projectId** | **String**| The project id | 
 **trainingKey** | **String**|  | 
 **imageData** | **File**|  | 
 **tagIds** | [**[String]**](String.md)| The tags ids with which to tag each image. Limited to 20 | [optional] 

### Return type

[**ImageCreateSummary**](ImageCreateSummary.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json, application/xml, text/json, text/xml


## createImagesFromFiles

> ImageCreateSummary createImagesFromFiles(projectId, trainingKey, imageFileCreateBatch)

Add the provided batch of images to the set of training images

### Example

```javascript
import TrainingApi from 'training_api';

let apiInstance = new TrainingApi.ImageApiApi();
let projectId = "64b822c5-8082-4b36-a426-27225f4aa18c"; // String | The project id
let trainingKey = "{API Key}"; // String | 
let imageFileCreateBatch = new TrainingApi.ImageFileCreateBatch(); // ImageFileCreateBatch | The batch of image files to add. Limited to 64 images and 20 tags per batch
apiInstance.createImagesFromFiles(projectId, trainingKey, imageFileCreateBatch, (error, data, response) => {
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
 **projectId** | **String**| The project id | 
 **trainingKey** | **String**|  | 
 **imageFileCreateBatch** | [**ImageFileCreateBatch**](ImageFileCreateBatch.md)| The batch of image files to add. Limited to 64 images and 20 tags per batch | 

### Return type

[**ImageCreateSummary**](ImageCreateSummary.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## createImagesFromPredictions

> ImageCreateSummary createImagesFromPredictions(projectId, trainingKey, imageIdCreateBatch)

Add the specified predicted images to the set of training images

### Example

```javascript
import TrainingApi from 'training_api';

let apiInstance = new TrainingApi.ImageApiApi();
let projectId = "64b822c5-8082-4b36-a426-27225f4aa18c"; // String | The project id
let trainingKey = "{API Key}"; // String | 
let imageIdCreateBatch = new TrainingApi.ImageIdCreateBatch(); // ImageIdCreateBatch | Image and tag ids. Limited to 64 images and 20 tags per batch
apiInstance.createImagesFromPredictions(projectId, trainingKey, imageIdCreateBatch, (error, data, response) => {
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
 **projectId** | **String**| The project id | 
 **trainingKey** | **String**|  | 
 **imageIdCreateBatch** | [**ImageIdCreateBatch**](ImageIdCreateBatch.md)| Image and tag ids. Limited to 64 images and 20 tags per batch | 

### Return type

[**ImageCreateSummary**](ImageCreateSummary.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## createImagesFromUrls

> ImageCreateSummary createImagesFromUrls(projectId, trainingKey, imageUrlCreateBatch)

Add the provided images urls to the set of training images

### Example

```javascript
import TrainingApi from 'training_api';

let apiInstance = new TrainingApi.ImageApiApi();
let projectId = "64b822c5-8082-4b36-a426-27225f4aa18c"; // String | The project id
let trainingKey = "{API Key}"; // String | 
let imageUrlCreateBatch = new TrainingApi.ImageUrlCreateBatch(); // ImageUrlCreateBatch | Image urls and tag ids. Limited to 64 images and 20 tags per batch
apiInstance.createImagesFromUrls(projectId, trainingKey, imageUrlCreateBatch, (error, data, response) => {
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
 **projectId** | **String**| The project id | 
 **trainingKey** | **String**|  | 
 **imageUrlCreateBatch** | [**ImageUrlCreateBatch**](ImageUrlCreateBatch.md)| Image urls and tag ids. Limited to 64 images and 20 tags per batch | 

### Return type

[**ImageCreateSummary**](ImageCreateSummary.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## deleteImageTags

> deleteImageTags(projectId, imageIds, tagIds, trainingKey)

Remove a set of tags from a set of images

### Example

```javascript
import TrainingApi from 'training_api';

let apiInstance = new TrainingApi.ImageApiApi();
let projectId = "64b822c5-8082-4b36-a426-27225f4aa18c"; // String | The project id
let imageIds = ["null"]; // [String] | Image ids. Limited to 64 images
let tagIds = ["null"]; // [String] | Tags to be deleted from the specified images. Limited to 20 tags
let trainingKey = "{API Key}"; // String | 
apiInstance.deleteImageTags(projectId, imageIds, tagIds, trainingKey, (error, data, response) => {
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
 **projectId** | **String**| The project id | 
 **imageIds** | [**[String]**](String.md)| Image ids. Limited to 64 images | 
 **tagIds** | [**[String]**](String.md)| Tags to be deleted from the specified images. Limited to 20 tags | 
 **trainingKey** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteImages

> deleteImages(projectId, imageIds, trainingKey)

Delete images from the set of training images

### Example

```javascript
import TrainingApi from 'training_api';

let apiInstance = new TrainingApi.ImageApiApi();
let projectId = "64b822c5-8082-4b36-a426-27225f4aa18c"; // String | The project id
let imageIds = ["null"]; // [String] | Ids of the images to be deleted. Limited to 256 images per batch
let trainingKey = "{API Key}"; // String | 
apiInstance.deleteImages(projectId, imageIds, trainingKey, (error, data, response) => {
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
 **projectId** | **String**| The project id | 
 **imageIds** | [**[String]**](String.md)| Ids of the images to be deleted. Limited to 256 images per batch | 
 **trainingKey** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getTaggedImages

> [Image] getTaggedImages(projectId, trainingKey, opts)

Get tagged images for a given project iteration

This API supports batching and range selection. By default it will only return first 50 images matching images.  Use the {take} and {skip} parameters to control how many images to return in a given batch.  The filtering is on an and/or relationship. For example, if the provided tag ids are for the \&quot;Dog\&quot; and  \&quot;Cat\&quot; tags, then only images tagged with Dog and/or Cat will be returned

### Example

```javascript
import TrainingApi from 'training_api';

let apiInstance = new TrainingApi.ImageApiApi();
let projectId = "bc3f7dad-5544-468c-8573-3ef04d55463e"; // String | The project id
let trainingKey = "{API Key}"; // String | 
let opts = {
  'iterationId': "cf0f83fb-ebaa-4b25-8e34-613a6a0b8a12", // String | The iteration id. Defaults to workspace
  'tagIds': ["null"], // [String] | An list of tags ids to filter the images. Defaults to all tagged images when null. Limited to 20
  'orderBy': "orderBy_example", // String | The ordering. Defaults to newest
  'take': 50, // Number | Maximum number of images to return. Defaults to 50, limited to 256
  'skip': 0 // Number | Number of images to skip before beginning the image batch. Defaults to 0
};
apiInstance.getTaggedImages(projectId, trainingKey, opts, (error, data, response) => {
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
 **projectId** | **String**| The project id | 
 **trainingKey** | **String**|  | 
 **iterationId** | **String**| The iteration id. Defaults to workspace | [optional] 
 **tagIds** | [**[String]**](String.md)| An list of tags ids to filter the images. Defaults to all tagged images when null. Limited to 20 | [optional] 
 **orderBy** | **String**| The ordering. Defaults to newest | [optional] 
 **take** | **Number**| Maximum number of images to return. Defaults to 50, limited to 256 | [optional] [default to 50]
 **skip** | **Number**| Number of images to skip before beginning the image batch. Defaults to 0 | [optional] [default to 0]

### Return type

[**[Image]**](Image.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## getUntaggedImages

> [Image] getUntaggedImages(projectId, trainingKey, opts)

Get untagged images for a given project iteration

This API supports batching and range selection. By default it will only return first 50 images matching images.  Use the {take} and {skip} parameters to control how many images to return in a given batch.

### Example

```javascript
import TrainingApi from 'training_api';

let apiInstance = new TrainingApi.ImageApiApi();
let projectId = "bc3f7dad-5544-468c-8573-3ef04d55463e"; // String | The project id
let trainingKey = "{API Key}"; // String | 
let opts = {
  'iterationId': "cf0f83fb-ebaa-4b25-8e34-613a6a0b8a12", // String | The iteration id. Defaults to workspace
  'orderBy': "orderBy_example", // String | The ordering. Defaults to newest
  'take': 50, // Number | Maximum number of images to return. Defaults to 50, limited to 256
  'skip': 0 // Number | Number of images to skip before beginning the image batch. Defaults to 0
};
apiInstance.getUntaggedImages(projectId, trainingKey, opts, (error, data, response) => {
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
 **projectId** | **String**| The project id | 
 **trainingKey** | **String**|  | 
 **iterationId** | **String**| The iteration id. Defaults to workspace | [optional] 
 **orderBy** | **String**| The ordering. Defaults to newest | [optional] 
 **take** | **Number**| Maximum number of images to return. Defaults to 50, limited to 256 | [optional] [default to 50]
 **skip** | **Number**| Number of images to skip before beginning the image batch. Defaults to 0 | [optional] [default to 0]

### Return type

[**[Image]**](Image.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## postImageTags

> ImageTagCreateSummary postImageTags(projectId, trainingKey, imageTagCreateBatch)

Associate a set of images with a set of tags

### Example

```javascript
import TrainingApi from 'training_api';

let apiInstance = new TrainingApi.ImageApiApi();
let projectId = "bc3f7dad-5544-468c-8573-3ef04d55463e"; // String | The project id
let trainingKey = "{API Key}"; // String | 
let imageTagCreateBatch = new TrainingApi.ImageTagCreateBatch(); // ImageTagCreateBatch | Batch of image tags. Limited to 128 tags per batch
apiInstance.postImageTags(projectId, trainingKey, imageTagCreateBatch, (error, data, response) => {
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
 **projectId** | **String**| The project id | 
 **trainingKey** | **String**|  | 
 **imageTagCreateBatch** | [**ImageTagCreateBatch**](ImageTagCreateBatch.md)| Batch of image tags. Limited to 128 tags per batch | 

### Return type

[**ImageTagCreateSummary**](ImageTagCreateSummary.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml

