# ComputerVisionClient.DefaultApi

All URIs are relative to *https://westcentralus.api.cognitive.microsoft.com/vision/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analyzeImage**](DefaultApi.md#analyzeImage) | **POST** /analyze | 
[**analyzeImageByDomain**](DefaultApi.md#analyzeImageByDomain) | **POST** /models/{model}/analyze | 
[**describeImage**](DefaultApi.md#describeImage) | **POST** /describe | 
[**detectObjects**](DefaultApi.md#detectObjects) | **POST** /detect | 
[**generateThumbnail**](DefaultApi.md#generateThumbnail) | **POST** /generateThumbnail | 
[**getAreaOfInterest**](DefaultApi.md#getAreaOfInterest) | **POST** /areaOfInterest | 
[**listModels**](DefaultApi.md#listModels) | **GET** /models | 
[**recognizePrintedText**](DefaultApi.md#recognizePrintedText) | **POST** /ocr | 
[**tagImage**](DefaultApi.md#tagImage) | **POST** /tag | 



## analyzeImage

> ImageAnalysis analyzeImage(imageUrl, opts)



This operation extracts a rich set of visual features based on the image content.  Two input methods are supported -- (1) Uploading an image or (2) specifying an image URL. Within your request, there is an optional parameter to allow you to choose which features to return. By default, image categories are returned in the response.  A successful response will be returned in JSON. If the request failed, the response will contain an error code and a message to help understand what went wrong.

### Example

```javascript
import ComputerVisionClient from 'computer_vision_client';
let defaultClient = ComputerVisionClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ComputerVisionClient.DefaultApi();
let imageUrl = new ComputerVisionClient.ImageUrl(); // ImageUrl | A JSON document with a URL pointing to the image that is to be analyzed.
let opts = {
  'visualFeatures': ["null"], // [String] | A string indicating what visual feature types to return. Multiple values should be comma-separated. Valid visual feature types include: Categories - categorizes image content according to a taxonomy defined in documentation. Tags - tags the image with a detailed list of words related to the image content. Description - describes the image content with a complete English sentence. Faces - detects if faces are present. If present, generate coordinates, gender and age. ImageType - detects if image is clipart or a line drawing. Color - determines the accent color, dominant color, and whether an image is black&white. Adult - detects if the image is pornographic in nature (depicts nudity or a sex act).  Sexually suggestive content is also detected. Objects - detects various objects within an image, including the approximate location. The Objects argument is only available in English. Brands - detects various brands within an image, including the approximate location. The Brands argument is only available in English.
  'details': ["null"], // [String] | A string indicating which domain-specific details to return. Multiple values should be comma-separated. Valid visual feature types include: Celebrities - identifies celebrities if detected in the image, Landmarks - identifies notable landmarks in the image.
  'language': "en" // String | The desired language for output generation. If this parameter is not specified, the default value is &quot;en&quot;.Supported languages:en - English, Default. es - Spanish, ja - Japanese, pt - Portuguese, zh - Simplified Chinese.
};
apiInstance.analyzeImage(imageUrl, opts, (error, data, response) => {
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
 **imageUrl** | [**ImageUrl**](ImageUrl.md)| A JSON document with a URL pointing to the image that is to be analyzed. | 
 **visualFeatures** | [**[String]**](String.md)| A string indicating what visual feature types to return. Multiple values should be comma-separated. Valid visual feature types include: Categories - categorizes image content according to a taxonomy defined in documentation. Tags - tags the image with a detailed list of words related to the image content. Description - describes the image content with a complete English sentence. Faces - detects if faces are present. If present, generate coordinates, gender and age. ImageType - detects if image is clipart or a line drawing. Color - determines the accent color, dominant color, and whether an image is black&amp;white. Adult - detects if the image is pornographic in nature (depicts nudity or a sex act).  Sexually suggestive content is also detected. Objects - detects various objects within an image, including the approximate location. The Objects argument is only available in English. Brands - detects various brands within an image, including the approximate location. The Brands argument is only available in English. | [optional] 
 **details** | [**[String]**](String.md)| A string indicating which domain-specific details to return. Multiple values should be comma-separated. Valid visual feature types include: Celebrities - identifies celebrities if detected in the image, Landmarks - identifies notable landmarks in the image. | [optional] 
 **language** | **String**| The desired language for output generation. If this parameter is not specified, the default value is &amp;quot;en&amp;quot;.Supported languages:en - English, Default. es - Spanish, ja - Japanese, pt - Portuguese, zh - Simplified Chinese. | [optional] [default to &#39;en&#39;]

### Return type

[**ImageAnalysis**](ImageAnalysis.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## analyzeImageByDomain

> DomainModelResults analyzeImageByDomain(model, imageUrl, opts)



This operation recognizes content within an image by applying a domain-specific model. The list of domain-specific models that are supported by the Computer Vision API can be retrieved using the /models GET request. Currently, the API provides following domain-specific models: celebrities, landmarks.  Two input methods are supported -- (1) Uploading an image or (2) specifying an image URL.  A successful response will be returned in JSON.  If the request failed, the response will contain an error code and a message to help understand what went wrong.

### Example

```javascript
import ComputerVisionClient from 'computer_vision_client';
let defaultClient = ComputerVisionClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ComputerVisionClient.DefaultApi();
let model = "Celebrities"; // String | The domain-specific content to recognize.
let imageUrl = new ComputerVisionClient.ImageUrl(); // ImageUrl | A JSON document with a URL pointing to the image that is to be analyzed.
let opts = {
  'language': "en" // String | The desired language for output generation. If this parameter is not specified, the default value is &quot;en&quot;.Supported languages:en - English, Default. es - Spanish, ja - Japanese, pt - Portuguese, zh - Simplified Chinese.
};
apiInstance.analyzeImageByDomain(model, imageUrl, opts, (error, data, response) => {
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
 **model** | **String**| The domain-specific content to recognize. | 
 **imageUrl** | [**ImageUrl**](ImageUrl.md)| A JSON document with a URL pointing to the image that is to be analyzed. | 
 **language** | **String**| The desired language for output generation. If this parameter is not specified, the default value is &amp;quot;en&amp;quot;.Supported languages:en - English, Default. es - Spanish, ja - Japanese, pt - Portuguese, zh - Simplified Chinese. | [optional] [default to &#39;en&#39;]

### Return type

[**DomainModelResults**](DomainModelResults.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeImage

> ImageDescription describeImage(imageUrl, opts)



This operation generates a description of an image in human readable language with complete sentences. The description is based on a collection of content tags, which are also returned by the operation. More than one description can be generated for each image. Descriptions are ordered by their confidence score. All descriptions are in English.  Two input methods are supported -- (1) Uploading an image or (2) specifying an image URL.  A successful response will be returned in JSON. If the request failed, the response will contain an error code and a message to help understand what went wrong.

### Example

```javascript
import ComputerVisionClient from 'computer_vision_client';
let defaultClient = ComputerVisionClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ComputerVisionClient.DefaultApi();
let imageUrl = new ComputerVisionClient.ImageUrl(); // ImageUrl | A JSON document with a URL pointing to the image that is to be analyzed.
let opts = {
  'maxCandidates': 1, // Number | Maximum number of candidate descriptions to be returned.  The default is 1.
  'language': "en" // String | The desired language for output generation. If this parameter is not specified, the default value is &quot;en&quot;.Supported languages:en - English, Default. es - Spanish, ja - Japanese, pt - Portuguese, zh - Simplified Chinese.
};
apiInstance.describeImage(imageUrl, opts, (error, data, response) => {
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
 **imageUrl** | [**ImageUrl**](ImageUrl.md)| A JSON document with a URL pointing to the image that is to be analyzed. | 
 **maxCandidates** | **Number**| Maximum number of candidate descriptions to be returned.  The default is 1. | [optional] [default to 1]
 **language** | **String**| The desired language for output generation. If this parameter is not specified, the default value is &amp;quot;en&amp;quot;.Supported languages:en - English, Default. es - Spanish, ja - Japanese, pt - Portuguese, zh - Simplified Chinese. | [optional] [default to &#39;en&#39;]

### Return type

[**ImageDescription**](ImageDescription.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## detectObjects

> DetectResult detectObjects(imageUrl)



Performs object detection on the specified image.  Two input methods are supported -- (1) Uploading an image or (2) specifying an image URL.  A successful response will be returned in JSON. If the request failed, the response will contain an error code and a message to help understand what went wrong.

### Example

```javascript
import ComputerVisionClient from 'computer_vision_client';
let defaultClient = ComputerVisionClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ComputerVisionClient.DefaultApi();
let imageUrl = new ComputerVisionClient.ImageUrl(); // ImageUrl | A JSON document with a URL pointing to the image that is to be analyzed.
apiInstance.detectObjects(imageUrl, (error, data, response) => {
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
 **imageUrl** | [**ImageUrl**](ImageUrl.md)| A JSON document with a URL pointing to the image that is to be analyzed. | 

### Return type

[**DetectResult**](DetectResult.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## generateThumbnail

> File generateThumbnail(width, height, imageUrl, opts)



This operation generates a thumbnail image with the user-specified width and height. By default, the service analyzes the image, identifies the region of interest (ROI), and generates smart cropping coordinates based on the ROI. Smart cropping helps when you specify an aspect ratio that differs from that of the input image.  A successful response contains the thumbnail image binary. If the request failed, the response contains an error code and a message to help determine what went wrong.  Upon failure, the error code and an error message are returned. The error code could be one of InvalidImageUrl, InvalidImageFormat, InvalidImageSize, InvalidThumbnailSize, NotSupportedImage, FailedToProcess, Timeout, or InternalServerError.

### Example

```javascript
import ComputerVisionClient from 'computer_vision_client';
let defaultClient = ComputerVisionClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ComputerVisionClient.DefaultApi();
let width = 500; // Number | Width of the thumbnail, in pixels. It must be between 1 and 1024. Recommended minimum of 50.
let height = 500; // Number | Height of the thumbnail, in pixels. It must be between 1 and 1024. Recommended minimum of 50.
let imageUrl = new ComputerVisionClient.ImageUrl(); // ImageUrl | A JSON document with a URL pointing to the image that is to be analyzed.
let opts = {
  'smartCropping': true // Boolean | Boolean flag for enabling smart cropping.
};
apiInstance.generateThumbnail(width, height, imageUrl, opts, (error, data, response) => {
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
 **width** | **Number**| Width of the thumbnail, in pixels. It must be between 1 and 1024. Recommended minimum of 50. | 
 **height** | **Number**| Height of the thumbnail, in pixels. It must be between 1 and 1024. Recommended minimum of 50. | 
 **imageUrl** | [**ImageUrl**](ImageUrl.md)| A JSON document with a URL pointing to the image that is to be analyzed. | 
 **smartCropping** | **Boolean**| Boolean flag for enabling smart cropping. | [optional] [default to false]

### Return type

**File**

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/octet-stream


## getAreaOfInterest

> AreaOfInterestResult getAreaOfInterest(imageUrl)



This operation returns a bounding box around the most important area of the image.  A successful response will be returned in JSON. If the request failed, the response contains an error code and a message to help determine what went wrong.  Upon failure, the error code and an error message are returned. The error code could be one of InvalidImageUrl, InvalidImageFormat, InvalidImageSize, NotSupportedImage, FailedToProcess, Timeout, or InternalServerError.

### Example

```javascript
import ComputerVisionClient from 'computer_vision_client';
let defaultClient = ComputerVisionClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ComputerVisionClient.DefaultApi();
let imageUrl = new ComputerVisionClient.ImageUrl(); // ImageUrl | A JSON document with a URL pointing to the image that is to be analyzed.
apiInstance.getAreaOfInterest(imageUrl, (error, data, response) => {
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
 **imageUrl** | [**ImageUrl**](ImageUrl.md)| A JSON document with a URL pointing to the image that is to be analyzed. | 

### Return type

[**AreaOfInterestResult**](AreaOfInterestResult.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listModels

> ListModelsResult listModels()



This operation returns the list of domain-specific models that are supported by the Computer Vision API. Currently, the API supports following domain-specific models: celebrity recognizer, landmark recognizer.  A successful response will be returned in JSON. If the request failed, the response will contain an error code and a message to help understand what went wrong.

### Example

```javascript
import ComputerVisionClient from 'computer_vision_client';
let defaultClient = ComputerVisionClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ComputerVisionClient.DefaultApi();
apiInstance.listModels((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**ListModelsResult**](ListModelsResult.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## recognizePrintedText

> OcrResult recognizePrintedText(detectOrientation, imageUrl, opts)



Optical Character Recognition (OCR) detects text in an image and extracts the recognized characters into a machine-usable character stream.  Upon success, the OCR results will be returned.  Upon failure, the error code together with an error message will be returned. The error code can be one of InvalidImageUrl, InvalidImageFormat, InvalidImageSize, NotSupportedImage, NotSupportedLanguage, or InternalServerError.

### Example

```javascript
import ComputerVisionClient from 'computer_vision_client';
let defaultClient = ComputerVisionClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ComputerVisionClient.DefaultApi();
let detectOrientation = true; // Boolean | Whether detect the text orientation in the image. With detectOrientation=true the OCR service tries to detect the image orientation and correct it before further processing (e.g. if it's upside-down).
let imageUrl = new ComputerVisionClient.ImageUrl(); // ImageUrl | A JSON document with a URL pointing to the image that is to be analyzed.
let opts = {
  'language': "en" // String | The BCP-47 language code of the text to be detected in the image. The default value is 'unk'.
};
apiInstance.recognizePrintedText(detectOrientation, imageUrl, opts, (error, data, response) => {
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
 **detectOrientation** | **Boolean**| Whether detect the text orientation in the image. With detectOrientation&#x3D;true the OCR service tries to detect the image orientation and correct it before further processing (e.g. if it&#39;s upside-down). | [default to true]
 **imageUrl** | [**ImageUrl**](ImageUrl.md)| A JSON document with a URL pointing to the image that is to be analyzed. | 
 **language** | **String**| The BCP-47 language code of the text to be detected in the image. The default value is &#39;unk&#39;. | [optional] [default to &#39;unk&#39;]

### Return type

[**OcrResult**](OcrResult.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tagImage

> TagResult tagImage(imageUrl, opts)



This operation generates a list of words, or tags, that are relevant to the content of the supplied image. The Computer Vision API can return tags based on objects, living beings, scenery or actions found in images. Unlike categories, tags are not organized according to a hierarchical classification system, but correspond to image content. Tags may contain hints to avoid ambiguity or provide context, for example the tag \&quot;cello\&quot; may be accompanied by the hint \&quot;musical instrument\&quot;. All tags are in English.  Two input methods are supported -- (1) Uploading an image or (2) specifying an image URL.  A successful response will be returned in JSON. If the request failed, the response will contain an error code and a message to help understand what went wrong.

### Example

```javascript
import ComputerVisionClient from 'computer_vision_client';
let defaultClient = ComputerVisionClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ComputerVisionClient.DefaultApi();
let imageUrl = new ComputerVisionClient.ImageUrl(); // ImageUrl | A JSON document with a URL pointing to the image that is to be analyzed.
let opts = {
  'language': "en" // String | The desired language for output generation. If this parameter is not specified, the default value is &quot;en&quot;.Supported languages:en - English, Default. es - Spanish, ja - Japanese, pt - Portuguese, zh - Simplified Chinese.
};
apiInstance.tagImage(imageUrl, opts, (error, data, response) => {
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
 **imageUrl** | [**ImageUrl**](ImageUrl.md)| A JSON document with a URL pointing to the image that is to be analyzed. | 
 **language** | **String**| The desired language for output generation. If this parameter is not specified, the default value is &amp;quot;en&amp;quot;.Supported languages:en - English, Default. es - Spanish, ja - Japanese, pt - Portuguese, zh - Simplified Chinese. | [optional] [default to &#39;en&#39;]

### Return type

[**TagResult**](TagResult.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

