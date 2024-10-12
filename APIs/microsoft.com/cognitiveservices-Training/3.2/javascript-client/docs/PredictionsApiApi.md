# CustomVisionTrainingClient.PredictionsApiApi

All URIs are relative to *https://southcentralus.api.cognitive.microsoft.com/customvision/v3.2/training*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deletePrediction**](PredictionsApiApi.md#deletePrediction) | **DELETE** /projects/{projectId}/predictions | Delete a set of predicted images and their associated prediction results.
[**queryPredictions**](PredictionsApiApi.md#queryPredictions) | **POST** /projects/{projectId}/predictions/query | Get images that were sent to your prediction endpoint.
[**quickTestImage**](PredictionsApiApi.md#quickTestImage) | **POST** /projects/{projectId}/quicktest/image | Quick test an image.
[**quickTestImageUrl**](PredictionsApiApi.md#quickTestImageUrl) | **POST** /projects/{projectId}/quicktest/url | Quick test an image url.



## deletePrediction

> deletePrediction(projectId, ids)

Delete a set of predicted images and their associated prediction results.

### Example

```javascript
import CustomVisionTrainingClient from 'custom_vision_training_client';
let defaultClient = CustomVisionTrainingClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new CustomVisionTrainingClient.PredictionsApiApi();
let projectId = "64b822c5-8082-4b36-a426-27225f4aa18c"; // String | The project id.
let ids = ["null"]; // [String] | The prediction ids. Limited to 64.
apiInstance.deletePrediction(projectId, ids, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## queryPredictions

> PredictionQueryResult queryPredictions(projectId, predictionQueryToken)

Get images that were sent to your prediction endpoint.

### Example

```javascript
import CustomVisionTrainingClient from 'custom_vision_training_client';
let defaultClient = CustomVisionTrainingClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new CustomVisionTrainingClient.PredictionsApiApi();
let projectId = "bc3f7dad-5544-468c-8573-3ef04d55463e"; // String | The project id.
let predictionQueryToken = new CustomVisionTrainingClient.PredictionQueryToken(); // PredictionQueryToken | Parameters used to query the predictions. Limited to combining 2 tags.
apiInstance.queryPredictions(projectId, predictionQueryToken, (error, data, response) => {
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
 **predictionQueryToken** | [**PredictionQueryToken**](PredictionQueryToken.md)| Parameters used to query the predictions. Limited to combining 2 tags. | 

### Return type

[**PredictionQueryResult**](PredictionQueryResult.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
- **Accept**: application/json, application/xml, text/xml


## quickTestImage

> ImagePrediction quickTestImage(projectId, imageData, opts)

Quick test an image.

### Example

```javascript
import CustomVisionTrainingClient from 'custom_vision_training_client';
let defaultClient = CustomVisionTrainingClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new CustomVisionTrainingClient.PredictionsApiApi();
let projectId = "64b822c5-8082-4b36-a426-27225f4aa18c"; // String | The project id.
let imageData = "/path/to/file"; // File | Binary image data. Supported formats are JPEG, GIF, PNG, and BMP. Supports images up to 6MB.
let opts = {
  'iterationId': "fe1e83c4-6f50-4899-9544-6bb08cf0e15a", // String | Optional. Specifies the id of a particular iteration to evaluate against.              The default iteration for the project will be used when not specified.
  'store': true // Boolean | Optional. Specifies whether or not to store the result of this prediction. The default is true, to store.
};
apiInstance.quickTestImage(projectId, imageData, opts, (error, data, response) => {
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
 **iterationId** | **String**| Optional. Specifies the id of a particular iteration to evaluate against.              The default iteration for the project will be used when not specified. | [optional] 
 **store** | **Boolean**| Optional. Specifies whether or not to store the result of this prediction. The default is true, to store. | [optional] [default to true]

### Return type

[**ImagePrediction**](ImagePrediction.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json, application/xml, text/xml


## quickTestImageUrl

> ImagePrediction quickTestImageUrl(projectId, imageUrl, opts)

Quick test an image url.

### Example

```javascript
import CustomVisionTrainingClient from 'custom_vision_training_client';
let defaultClient = CustomVisionTrainingClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new CustomVisionTrainingClient.PredictionsApiApi();
let projectId = "64b822c5-8082-4b36-a426-27225f4aa18c"; // String | The project to evaluate against.
let imageUrl = new CustomVisionTrainingClient.ImageUrl(); // ImageUrl | An ImageUrl that contains the url of the image to be evaluated.
let opts = {
  'iterationId': "fe1e83c4-6f50-4899-9544-6bb08cf0e15a", // String | Optional. Specifies the id of a particular iteration to evaluate against.              The default iteration for the project will be used when not specified.
  'store': true // Boolean | Optional. Specifies whether or not to store the result of this prediction. The default is true, to store.
};
apiInstance.quickTestImageUrl(projectId, imageUrl, opts, (error, data, response) => {
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
 **imageUrl** | [**ImageUrl**](ImageUrl.md)| An ImageUrl that contains the url of the image to be evaluated. | 
 **iterationId** | **String**| Optional. Specifies the id of a particular iteration to evaluate against.              The default iteration for the project will be used when not specified. | [optional] 
 **store** | **Boolean**| Optional. Specifies whether or not to store the result of this prediction. The default is true, to store. | [optional] [default to true]

### Return type

[**ImagePrediction**](ImagePrediction.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
- **Accept**: application/json, application/xml, text/xml

