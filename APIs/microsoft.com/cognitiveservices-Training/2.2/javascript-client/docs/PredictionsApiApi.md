# CustomVisionTrainingClient.PredictionsApiApi

All URIs are relative to *https://southcentralus.api.cognitive.microsoft.com/customvision/v2.2/Training*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deletePrediction**](PredictionsApiApi.md#deletePrediction) | **DELETE** /projects/{projectId}/predictions | Delete a set of predicted images and their associated prediction results.
[**queryPredictions**](PredictionsApiApi.md#queryPredictions) | **POST** /projects/{projectId}/predictions/query | Get images that were sent to your prediction endpoint.
[**quickTestImage**](PredictionsApiApi.md#quickTestImage) | **POST** /projects/{projectId}/quicktest/image | Quick test an image.
[**quickTestImageUrl**](PredictionsApiApi.md#quickTestImageUrl) | **POST** /projects/{projectId}/quicktest/url | Quick test an image url.



## deletePrediction

> deletePrediction(projectId, ids, trainingKey)

Delete a set of predicted images and their associated prediction results.

### Example

```javascript
import CustomVisionTrainingClient from 'custom_vision_training_client';

let apiInstance = new CustomVisionTrainingClient.PredictionsApiApi();
let projectId = "64b822c5-8082-4b36-a426-27225f4aa18c"; // String | The project id.
let ids = ["null"]; // [String] | The prediction ids. Limited to 64.
let trainingKey = "{API Key}"; // String | 
apiInstance.deletePrediction(projectId, ids, trainingKey, (error, data, response) => {
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
 **ids** | [**[String]**](String.md)| The prediction ids. Limited to 64. | 
 **trainingKey** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## queryPredictions

> PredictionQueryResult queryPredictions(projectId, trainingKey, predictionQueryToken)

Get images that were sent to your prediction endpoint.

### Example

```javascript
import CustomVisionTrainingClient from 'custom_vision_training_client';

let apiInstance = new CustomVisionTrainingClient.PredictionsApiApi();
let projectId = "bc3f7dad-5544-468c-8573-3ef04d55463e"; // String | The project id.
let trainingKey = "{API Key}"; // String | 
let predictionQueryToken = new CustomVisionTrainingClient.PredictionQueryToken(); // PredictionQueryToken | Parameters used to query the predictions. Limited to combining 2 tags.
apiInstance.queryPredictions(projectId, trainingKey, predictionQueryToken, (error, data, response) => {
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
 **trainingKey** | **String**|  | 
 **predictionQueryToken** | [**PredictionQueryToken**](PredictionQueryToken.md)| Parameters used to query the predictions. Limited to combining 2 tags. | 

### Return type

[**PredictionQueryResult**](PredictionQueryResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## quickTestImage

> ImagePrediction quickTestImage(projectId, trainingKey, imageData, opts)

Quick test an image.

### Example

```javascript
import CustomVisionTrainingClient from 'custom_vision_training_client';

let apiInstance = new CustomVisionTrainingClient.PredictionsApiApi();
let projectId = "64b822c5-8082-4b36-a426-27225f4aa18c"; // String | The project id.
let trainingKey = "{API Key}"; // String | 
let imageData = "/path/to/file"; // File | Binary image data.
let opts = {
  'iterationId': "fe1e83c4-6f50-4899-9544-6bb08cf0e15a" // String | Optional. Specifies the id of a particular iteration to evaluate against.              The default iteration for the project will be used when not specified.
};
apiInstance.quickTestImage(projectId, trainingKey, imageData, opts, (error, data, response) => {
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
 **trainingKey** | **String**|  | 
 **imageData** | **File**| Binary image data. | 
 **iterationId** | **String**| Optional. Specifies the id of a particular iteration to evaluate against.              The default iteration for the project will be used when not specified. | [optional] 

### Return type

[**ImagePrediction**](ImagePrediction.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json, application/xml, text/json, text/xml


## quickTestImageUrl

> ImagePrediction quickTestImageUrl(projectId, trainingKey, imageUrl, opts)

Quick test an image url.

### Example

```javascript
import CustomVisionTrainingClient from 'custom_vision_training_client';

let apiInstance = new CustomVisionTrainingClient.PredictionsApiApi();
let projectId = "64b822c5-8082-4b36-a426-27225f4aa18c"; // String | The project to evaluate against.
let trainingKey = "{API Key}"; // String | 
let imageUrl = new CustomVisionTrainingClient.ImageUrl(); // ImageUrl | An {Iris.Web.Api.Models.ImageUrl} that contains the url of the image to be evaluated.
let opts = {
  'iterationId': "fe1e83c4-6f50-4899-9544-6bb08cf0e15a" // String | Optional. Specifies the id of a particular iteration to evaluate against.              The default iteration for the project will be used when not specified.
};
apiInstance.quickTestImageUrl(projectId, trainingKey, imageUrl, opts, (error, data, response) => {
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
 **projectId** | **String**| The project to evaluate against. | 
 **trainingKey** | **String**|  | 
 **imageUrl** | [**ImageUrl**](ImageUrl.md)| An {Iris.Web.Api.Models.ImageUrl} that contains the url of the image to be evaluated. | 
 **iterationId** | **String**| Optional. Specifies the id of a particular iteration to evaluate against.              The default iteration for the project will be used when not specified. | [optional] 

### Return type

[**ImagePrediction**](ImagePrediction.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml

