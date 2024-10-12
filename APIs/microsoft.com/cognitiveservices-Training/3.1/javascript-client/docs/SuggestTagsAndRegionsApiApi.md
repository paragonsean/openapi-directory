# CustomVisionTrainingClient.SuggestTagsAndRegionsApiApi

All URIs are relative to *https://southcentralus.api.cognitive.microsoft.com/customvision/v3.1/training*

Method | HTTP request | Description
------------- | ------------- | -------------
[**suggestTagsAndRegions**](SuggestTagsAndRegionsApiApi.md#suggestTagsAndRegions) | **POST** /projects/{projectId}/tagsandregions/suggestions | Suggest tags and regions for an array/batch of untagged images. Returns empty array if no tags are found.



## suggestTagsAndRegions

> [SuggestedTagAndRegion] suggestTagsAndRegions(projectId, iterationId, imageIds, trainingKey)

Suggest tags and regions for an array/batch of untagged images. Returns empty array if no tags are found.

This API will get suggested tags and regions for an array/batch of untagged images along with confidences for the tags. It returns an empty array if no tags are found.  There is a limit of 64 images in the batch.

### Example

```javascript
import CustomVisionTrainingClient from 'custom_vision_training_client';

let apiInstance = new CustomVisionTrainingClient.SuggestTagsAndRegionsApiApi();
let projectId = "bc3f7dad-5544-468c-8573-3ef04d55463e"; // String | The project id.
let iterationId = "4d6eb844-42ee-42bc-bd6f-c32455ef07c9"; // String | IterationId to use for tag and region suggestion.
let imageIds = ["null"]; // [String] | Array of image ids tag suggestion are needed for. Use GetUntaggedImages API to get imageIds.
let trainingKey = "{API Key}"; // String | API key.
apiInstance.suggestTagsAndRegions(projectId, iterationId, imageIds, trainingKey, (error, data, response) => {
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
 **iterationId** | **String**| IterationId to use for tag and region suggestion. | 
 **imageIds** | [**[String]**](String.md)| Array of image ids tag suggestion are needed for. Use GetUntaggedImages API to get imageIds. | 
 **trainingKey** | **String**| API key. | 

### Return type

[**[SuggestedTagAndRegion]**](SuggestedTagAndRegion.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/xml

