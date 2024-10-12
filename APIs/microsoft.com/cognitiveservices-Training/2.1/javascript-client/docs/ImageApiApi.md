# TrainingApi.ImageApiApi

All URIs are relative to *https://southcentralus.api.cognitive.microsoft.com/customvision/v2.1/Training*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createImageRegions**](ImageApiApi.md#createImageRegions) | **POST** /projects/{projectId}/images/regions | Create a set of image regions
[**createImageTags**](ImageApiApi.md#createImageTags) | **POST** /projects/{projectId}/images/tags | Associate a set of images with a set of tags
[**createImagesFromData**](ImageApiApi.md#createImagesFromData) | **POST** /projects/{projectId}/images | Add the provided images to the set of training images
[**createImagesFromFiles**](ImageApiApi.md#createImagesFromFiles) | **POST** /projects/{projectId}/images/files | Add the provided batch of images to the set of training images
[**createImagesFromPredictions**](ImageApiApi.md#createImagesFromPredictions) | **POST** /projects/{projectId}/images/predictions | Add the specified predicted images to the set of training images
[**createImagesFromUrls**](ImageApiApi.md#createImagesFromUrls) | **POST** /projects/{projectId}/images/urls | Add the provided images urls to the set of training images
[**deleteImageRegions**](ImageApiApi.md#deleteImageRegions) | **DELETE** /projects/{projectId}/images/regions | Delete a set of image regions
[**deleteImageTags**](ImageApiApi.md#deleteImageTags) | **DELETE** /projects/{projectId}/images/tags | Remove a set of tags from a set of images
[**deleteImages**](ImageApiApi.md#deleteImages) | **DELETE** /projects/{projectId}/images | Delete images from the set of training images
[**getImagesByIds**](ImageApiApi.md#getImagesByIds) | **GET** /projects/{projectId}/images/id | Get images by id for a given project iteration
[**getTaggedImageCount**](ImageApiApi.md#getTaggedImageCount) | **GET** /projects/{projectId}/images/tagged/count | Gets the number of images tagged with the provided {tagIds}
[**getTaggedImages**](ImageApiApi.md#getTaggedImages) | **GET** /projects/{projectId}/images/tagged | Get tagged images for a given project iteration
[**getUntaggedImageCount**](ImageApiApi.md#getUntaggedImageCount) | **GET** /projects/{projectId}/images/untagged/count | Gets the number of untagged images
[**getUntaggedImages**](ImageApiApi.md#getUntaggedImages) | **GET** /projects/{projectId}/images/untagged | Get untagged images for a given project iteration



## createImageRegions

> ImageRegionCreateSummary createImageRegions(projectId, trainingKey, imageRegionCreateBatch)

Create a set of image regions

This API accepts a batch of image regions, and optionally tags, to update existing images with region information.  There is a limit of 64 entries in the batch.

### Example

```javascript
import TrainingApi from 'training_api';

let apiInstance = new TrainingApi.ImageApiApi();
let projectId = "bc3f7dad-5544-468c-8573-3ef04d55463e"; // String | The project id
let trainingKey = "{API Key}"; // String | 
let imageRegionCreateBatch = new TrainingApi.ImageRegionCreateBatch(); // ImageRegionCreateBatch | Batch of image regions which include a tag and bounding box. Limited to 64
apiInstance.createImageRegions(projectId, trainingKey, imageRegionCreateBatch, (error, data, response) => {
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
 **imageRegionCreateBatch** | [**ImageRegionCreateBatch**](ImageRegionCreateBatch.md)| Batch of image regions which include a tag and bounding box. Limited to 64 | 

### Return type

[**ImageRegionCreateSummary**](ImageRegionCreateSummary.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## createImageTags

> ImageTagCreateSummary createImageTags(projectId, trainingKey, imageTagCreateBatch)

Associate a set of images with a set of tags

### Example

```javascript
import TrainingApi from 'training_api';

let apiInstance = new TrainingApi.ImageApiApi();
let projectId = "bc3f7dad-5544-468c-8573-3ef04d55463e"; // String | The project id
let trainingKey = "{API Key}"; // String | 
let imageTagCreateBatch = new TrainingApi.ImageTagCreateBatch(); // ImageTagCreateBatch | Batch of image tags. Limited to 128 tags per batch
apiInstance.createImageTags(projectId, trainingKey, imageTagCreateBatch, (error, data, response) => {
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

This API accepts a batch of files, and optionally tags, to create images. There is a limit of 64 images and 20 tags.

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

This API creates a batch of images from predicted images specified. There is a limit of 64 images and 20 tags.

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

This API accepts a batch of urls, and optionally tags, to create images. There is a limit of 64 images and 20 tags.

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


## deleteImageRegions

> deleteImageRegions(projectId, regionIds, trainingKey)

Delete a set of image regions

### Example

```javascript
import TrainingApi from 'training_api';

let apiInstance = new TrainingApi.ImageApiApi();
let projectId = "bc3f7dad-5544-468c-8573-3ef04d55463e"; // String | The project id
let regionIds = ["null"]; // [String] | Regions to delete. Limited to 64
let trainingKey = "{API Key}"; // String | 
apiInstance.deleteImageRegions(projectId, regionIds, trainingKey, (error, data, response) => {
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
 **regionIds** | [**[String]**](String.md)| Regions to delete. Limited to 64 | 
 **trainingKey** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


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


## getImagesByIds

> [Image] getImagesByIds(projectId, trainingKey, opts)

Get images by id for a given project iteration

This API will return a set of Images for the specified tags and optionally iteration. If no iteration is specified the  current workspace is used.

### Example

```javascript
import TrainingApi from 'training_api';

let apiInstance = new TrainingApi.ImageApiApi();
let projectId = "bc3f7dad-5544-468c-8573-3ef04d55463e"; // String | The project id
let trainingKey = "{API Key}"; // String | 
let opts = {
  'imageIds': ["null"], // [String] | The list of image ids to retrieve. Limited to 256
  'iterationId': "cf0f83fb-ebaa-4b25-8e34-613a6a0b8a12" // String | The iteration id. Defaults to workspace
};
apiInstance.getImagesByIds(projectId, trainingKey, opts, (error, data, response) => {
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
 **imageIds** | [**[String]**](String.md)| The list of image ids to retrieve. Limited to 256 | [optional] 
 **iterationId** | **String**| The iteration id. Defaults to workspace | [optional] 

### Return type

[**[Image]**](Image.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## getTaggedImageCount

> Number getTaggedImageCount(projectId, trainingKey, opts)

Gets the number of images tagged with the provided {tagIds}

The filtering is on an and/or relationship. For example, if the provided tag ids are for the \&quot;Dog\&quot; and  \&quot;Cat\&quot; tags, then only images tagged with Dog and/or Cat will be returned

### Example

```javascript
import TrainingApi from 'training_api';

let apiInstance = new TrainingApi.ImageApiApi();
let projectId = "bc3f7dad-5544-468c-8573-3ef04d55463e"; // String | The project id
let trainingKey = "{API Key}"; // String | 
let opts = {
  'iterationId': "cf0f83fb-ebaa-4b25-8e34-613a6a0b8a12", // String | The iteration id. Defaults to workspace
  'tagIds': ["null"] // [String] | A list of tags ids to filter the images to count. Defaults to all tags when null.
};
apiInstance.getTaggedImageCount(projectId, trainingKey, opts, (error, data, response) => {
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
 **tagIds** | [**[String]**](String.md)| A list of tags ids to filter the images to count. Defaults to all tags when null. | [optional] 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


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
  'tagIds': ["null"], // [String] | A list of tags ids to filter the images. Defaults to all tagged images when null. Limited to 20
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
 **tagIds** | [**[String]**](String.md)| A list of tags ids to filter the images. Defaults to all tagged images when null. Limited to 20 | [optional] 
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


## getUntaggedImageCount

> Number getUntaggedImageCount(projectId, trainingKey, opts)

Gets the number of untagged images

This API returns the images which have no tags for a given project and optionally an iteration. If no iteration is specified the  current workspace is used.

### Example

```javascript
import TrainingApi from 'training_api';

let apiInstance = new TrainingApi.ImageApiApi();
let projectId = "bc3f7dad-5544-468c-8573-3ef04d55463e"; // String | The project id
let trainingKey = "{API Key}"; // String | 
let opts = {
  'iterationId': "cf0f83fb-ebaa-4b25-8e34-613a6a0b8a12" // String | The iteration id. Defaults to workspace
};
apiInstance.getUntaggedImageCount(projectId, trainingKey, opts, (error, data, response) => {
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

### Return type

**Number**

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

