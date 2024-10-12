# EinsteinVisionAndEinsteinLanguage.VisionPredictionApi

All URIs are relative to *http://salesforce.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**detectMultipart**](VisionPredictionApi.md#detectMultipart) | **POST** /v2/vision/detect | Detection with Image File
[**ocrMultipart**](VisionPredictionApi.md#ocrMultipart) | **POST** /v2/vision/ocr | Detect Text
[**predictMultipart**](VisionPredictionApi.md#predictMultipart) | **POST** /v2/vision/predict | Make Prediction



## detectMultipart

> ObjectDetectionResponse detectMultipart(opts)

Detection with Image File

Returns labels, probabilities, and bounding box coordinates for items detected in the specified local image file.

### Example

```javascript
import EinsteinVisionAndEinsteinLanguage from 'einstein_vision_and_einstein_language';
let defaultClient = EinsteinVisionAndEinsteinLanguage.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_token
let bearer_token = defaultClient.authentications['bearer_token'];
bearer_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new EinsteinVisionAndEinsteinLanguage.VisionPredictionApi();
let opts = {
  'objectDetectionRequest': new EinsteinVisionAndEinsteinLanguage.ObjectDetectionRequest() // ObjectDetectionRequest | 
};
apiInstance.detectMultipart(opts, (error, data, response) => {
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
 **objectDetectionRequest** | [**ObjectDetectionRequest**](ObjectDetectionRequest.md)|  | [optional] 

### Return type

[**ObjectDetectionResponse**](ObjectDetectionResponse.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/json


## ocrMultipart

> OCRPredictResponse ocrMultipart(opts)

Detect Text

Returns a prediction from an OCR model for the specified image URL or local image file.

### Example

```javascript
import EinsteinVisionAndEinsteinLanguage from 'einstein_vision_and_einstein_language';
let defaultClient = EinsteinVisionAndEinsteinLanguage.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_token
let bearer_token = defaultClient.authentications['bearer_token'];
bearer_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new EinsteinVisionAndEinsteinLanguage.VisionPredictionApi();
let opts = {
  'modelId': "modelId_example", // String | ID of the model that makes the prediction. Valid values are OCRModel and tabulatev2.
  'sampleContent': "/path/to/file", // File | Binary content of image file uploaded as multipart/form-data. Optional.
  'sampleId': "sampleId_example", // String | String that you can pass in to tag the prediction. Optional. Can be any value, and is returned in the response.
  'sampleLocation': "sampleLocation_example", // String | URL of the image file. Use this parameter when sending in a file from a web location. Optional.
  'task': "'text'" // String | Optional. Designates the type of data in the image. Default is text. Valid values: contact, table, and text.
};
apiInstance.ocrMultipart(opts, (error, data, response) => {
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
 **modelId** | **String**| ID of the model that makes the prediction. Valid values are OCRModel and tabulatev2. | [optional] 
 **sampleContent** | **File**| Binary content of image file uploaded as multipart/form-data. Optional. | [optional] 
 **sampleId** | **String**| String that you can pass in to tag the prediction. Optional. Can be any value, and is returned in the response. | [optional] 
 **sampleLocation** | **String**| URL of the image file. Use this parameter when sending in a file from a web location. Optional. | [optional] 
 **task** | **String**| Optional. Designates the type of data in the image. Default is text. Valid values: contact, table, and text. | [optional] [default to &#39;text&#39;]

### Return type

[**OCRPredictResponse**](OCRPredictResponse.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## predictMultipart

> ImageClassificationResponse predictMultipart(opts)

Make Prediction

Returns a prediction from an image or multi-label model for the specified image.

### Example

```javascript
import EinsteinVisionAndEinsteinLanguage from 'einstein_vision_and_einstein_language';
let defaultClient = EinsteinVisionAndEinsteinLanguage.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_token
let bearer_token = defaultClient.authentications['bearer_token'];
bearer_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new EinsteinVisionAndEinsteinLanguage.VisionPredictionApi();
let opts = {
  'imageClassificationRequest': new EinsteinVisionAndEinsteinLanguage.ImageClassificationRequest() // ImageClassificationRequest | 
};
apiInstance.predictMultipart(opts, (error, data, response) => {
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
 **imageClassificationRequest** | [**ImageClassificationRequest**](ImageClassificationRequest.md)|  | [optional] 

### Return type

[**ImageClassificationResponse**](ImageClassificationResponse.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/json

