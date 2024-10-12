# ComputerVision.DefaultApi

All URIs are relative to *https://azure.local/vision/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analyzeImage**](DefaultApi.md#analyzeImage) | **POST** /analyze | 
[**analyzeImageByDomain**](DefaultApi.md#analyzeImageByDomain) | **POST** /models/{model}/analyze | 
[**describeImage**](DefaultApi.md#describeImage) | **POST** /describe | 
[**generateThumbnail**](DefaultApi.md#generateThumbnail) | **POST** /generateThumbnail | 
[**getTextOperationResult**](DefaultApi.md#getTextOperationResult) | **GET** /textOperations/{operationId} | 
[**listModels**](DefaultApi.md#listModels) | **GET** /models | 
[**recognizePrintedText**](DefaultApi.md#recognizePrintedText) | **POST** /ocr | 
[**recognizeText**](DefaultApi.md#recognizeText) | **POST** /recognizeText | 
[**tagImage**](DefaultApi.md#tagImage) | **POST** /tag | 



## analyzeImage

> ImageAnalysis analyzeImage(imageUrl, opts)



This operation extracts a rich set of visual features based on the image content. Two input methods are supported -- (1) Uploading an image or (2) specifying an image URL.  Within your request, there is an optional parameter to allow you to choose which features to return.  By default, image categories are returned in the response.

### Example

```javascript
import ComputerVision from 'computer_vision';
let defaultClient = ComputerVision.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ComputerVision.DefaultApi();
let imageUrl = new ComputerVision.AnalyzeImageRequest(); // AnalyzeImageRequest | A JSON document with a URL pointing to the image that is to be analyzed.
let opts = {
  'visualFeatures': ["null"], // [String] | A string indicating what visual feature types to return. Multiple values should be comma-separated. Valid visual feature types include:Categories - categorizes image content according to a taxonomy defined in documentation. Tags - tags the image with a detailed list of words related to the image content. Description - describes the image content with a complete English sentence. Faces - detects if faces are present. If present, generate coordinates, gender and age. ImageType - detects if image is clipart or a line drawing. Color - determines the accent color, dominant color, and whether an image is black&white.Adult - detects if the image is pornographic in nature (depicts nudity or a sex act).  Sexually suggestive content is also detected.
  'details': ["null"], // [String] | A string indicating which domain-specific details to return. Multiple values should be comma-separated. Valid visual feature types include:Celebrities - identifies celebrities if detected in the image.
  'language': "'en'" // String | The desired language for output generation. If this parameter is not specified, the default value is &quot;en&quot;.Supported languages:en - English, Default. es - Spanish, ja - Japanese, pt - Portuguese, zh - Simplified Chinese.
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
 **imageUrl** | [**AnalyzeImageRequest**](AnalyzeImageRequest.md)| A JSON document with a URL pointing to the image that is to be analyzed. | 
 **visualFeatures** | [**[String]**](String.md)| A string indicating what visual feature types to return. Multiple values should be comma-separated. Valid visual feature types include:Categories - categorizes image content according to a taxonomy defined in documentation. Tags - tags the image with a detailed list of words related to the image content. Description - describes the image content with a complete English sentence. Faces - detects if faces are present. If present, generate coordinates, gender and age. ImageType - detects if image is clipart or a line drawing. Color - determines the accent color, dominant color, and whether an image is black&amp;white.Adult - detects if the image is pornographic in nature (depicts nudity or a sex act).  Sexually suggestive content is also detected. | [optional] 
 **details** | [**[String]**](String.md)| A string indicating which domain-specific details to return. Multiple values should be comma-separated. Valid visual feature types include:Celebrities - identifies celebrities if detected in the image. | [optional] 
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



This operation recognizes content within an image by applying a domain-specific model.  The list of domain-specific models that are supported by the Computer Vision API can be retrieved using the /models GET request.  Currently, the API only provides a single domain-specific model: celebrities. Two input methods are supported -- (1) Uploading an image or (2) specifying an image URL. A successful response will be returned in JSON.  If the request failed, the response will contain an error code and a message to help understand what went wrong.

### Example

```javascript
import ComputerVision from 'computer_vision';
let defaultClient = ComputerVision.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ComputerVision.DefaultApi();
let model = "model_example"; // String | The domain-specific content to recognize.
let imageUrl = new ComputerVision.AnalyzeImageRequest(); // AnalyzeImageRequest | A JSON document with a URL pointing to the image that is to be analyzed.
let opts = {
  'language': "'en'" // String | The desired language for output generation. If this parameter is not specified, the default value is &quot;en&quot;.Supported languages:en - English, Default. es - Spanish, ja - Japanese, pt - Portuguese, zh - Simplified Chinese.
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
 **imageUrl** | [**AnalyzeImageRequest**](AnalyzeImageRequest.md)| A JSON document with a URL pointing to the image that is to be analyzed. | 
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



This operation generates a description of an image in human readable language with complete sentences.  The description is based on a collection of content tags, which are also returned by the operation. More than one description can be generated for each image.  Descriptions are ordered by their confidence score. All descriptions are in English. Two input methods are supported -- (1) Uploading an image or (2) specifying an image URL.A successful response will be returned in JSON.  If the request failed, the response will contain an error code and a message to help understand what went wrong.

### Example

```javascript
import ComputerVision from 'computer_vision';
let defaultClient = ComputerVision.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ComputerVision.DefaultApi();
let imageUrl = new ComputerVision.AnalyzeImageRequest(); // AnalyzeImageRequest | A JSON document with a URL pointing to the image that is to be analyzed.
let opts = {
  'maxCandidates': "'1'", // String | Maximum number of candidate descriptions to be returned.  The default is 1.
  'language': "'en'" // String | The desired language for output generation. If this parameter is not specified, the default value is &quot;en&quot;.Supported languages:en - English, Default. es - Spanish, ja - Japanese, pt - Portuguese, zh - Simplified Chinese.
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
 **imageUrl** | [**AnalyzeImageRequest**](AnalyzeImageRequest.md)| A JSON document with a URL pointing to the image that is to be analyzed. | 
 **maxCandidates** | **String**| Maximum number of candidate descriptions to be returned.  The default is 1. | [optional] [default to &#39;1&#39;]
 **language** | **String**| The desired language for output generation. If this parameter is not specified, the default value is &amp;quot;en&amp;quot;.Supported languages:en - English, Default. es - Spanish, ja - Japanese, pt - Portuguese, zh - Simplified Chinese. | [optional] [default to &#39;en&#39;]

### Return type

[**ImageDescription**](ImageDescription.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## generateThumbnail

> File generateThumbnail(width, height, imageUrl, opts)



This operation generates a thumbnail image with the user-specified width and height. By default, the service analyzes the image, identifies the region of interest (ROI), and generates smart cropping coordinates based on the ROI. Smart cropping helps when you specify an aspect ratio that differs from that of the input image. A successful response contains the thumbnail image binary. If the request failed, the response contains an error code and a message to help determine what went wrong.

### Example

```javascript
import ComputerVision from 'computer_vision';
let defaultClient = ComputerVision.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ComputerVision.DefaultApi();
let width = 56; // Number | Width of the thumbnail. It must be between 1 and 1024. Recommended minimum of 50.
let height = 56; // Number | Height of the thumbnail. It must be between 1 and 1024. Recommended minimum of 50.
let imageUrl = new ComputerVision.AnalyzeImageRequest(); // AnalyzeImageRequest | A JSON document with a URL pointing to the image that is to be analyzed.
let opts = {
  'smartCropping': false // Boolean | Boolean flag for enabling smart cropping.
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
 **width** | **Number**| Width of the thumbnail. It must be between 1 and 1024. Recommended minimum of 50. | 
 **height** | **Number**| Height of the thumbnail. It must be between 1 and 1024. Recommended minimum of 50. | 
 **imageUrl** | [**AnalyzeImageRequest**](AnalyzeImageRequest.md)| A JSON document with a URL pointing to the image that is to be analyzed. | 
 **smartCropping** | **Boolean**| Boolean flag for enabling smart cropping. | [optional] [default to false]

### Return type

**File**

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/octet-stream


## getTextOperationResult

> TextOperationResult getTextOperationResult(operationId)



This interface is used for getting text operation result. The URL to this interface should be retrieved from &#39;Operation-Location&#39; field returned from Recognize Text interface.

### Example

```javascript
import ComputerVision from 'computer_vision';
let defaultClient = ComputerVision.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ComputerVision.DefaultApi();
let operationId = "operationId_example"; // String | Id of the text operation returned in the response of the 'Recognize Handwritten Text'
apiInstance.getTextOperationResult(operationId, (error, data, response) => {
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
 **operationId** | **String**| Id of the text operation returned in the response of the &#39;Recognize Handwritten Text&#39; | 

### Return type

[**TextOperationResult**](TextOperationResult.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listModels

> ListModelsResult listModels()



This operation returns the list of domain-specific models that are supported by the Computer Vision API.  Currently, the API only supports one domain-specific model: a celebrity recognizer. A successful response will be returned in JSON.  If the request failed, the response will contain an error code and a message to help understand what went wrong.

### Example

```javascript
import ComputerVision from 'computer_vision';
let defaultClient = ComputerVision.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ComputerVision.DefaultApi();
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



Optical Character Recognition (OCR) detects printed text in an image and extracts the recognized characters into a machine-usable character stream.   Upon success, the OCR results will be returned. Upon failure, the error code together with an error message will be returned. The error code can be one of InvalidImageUrl, InvalidImageFormat, InvalidImageSize, NotSupportedImage,  NotSupportedLanguage, or InternalServerError.

### Example

```javascript
import ComputerVision from 'computer_vision';
let defaultClient = ComputerVision.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ComputerVision.DefaultApi();
let detectOrientation = true; // Boolean | Whether detect the text orientation in the image. With detectOrientation=true the OCR service tries to detect the image orientation and correct it before further processing (e.g. if it's upside-down). 
let imageUrl = new ComputerVision.AnalyzeImageRequest(); // AnalyzeImageRequest | A JSON document with a URL pointing to the image that is to be analyzed.
let opts = {
  'language': "'unk'" // String | The BCP-47 language code of the text to be detected in the image. The default value is 'unk'
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
 **detectOrientation** | **Boolean**| Whether detect the text orientation in the image. With detectOrientation&#x3D;true the OCR service tries to detect the image orientation and correct it before further processing (e.g. if it&#39;s upside-down).  | [default to true]
 **imageUrl** | [**AnalyzeImageRequest**](AnalyzeImageRequest.md)| A JSON document with a URL pointing to the image that is to be analyzed. | 
 **language** | **String**| The BCP-47 language code of the text to be detected in the image. The default value is &#39;unk&#39; | [optional] [default to &#39;unk&#39;]

### Return type

[**OcrResult**](OcrResult.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## recognizeText

> recognizeText(imageUrl, opts)



Recognize Text operation. When you use the Recognize Text interface, the response contains a field called &#39;Operation-Location&#39;. The &#39;Operation-Location&#39; field contains the URL that you must use for your Get Handwritten Text Operation Result operation.

### Example

```javascript
import ComputerVision from 'computer_vision';
let defaultClient = ComputerVision.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ComputerVision.DefaultApi();
let imageUrl = new ComputerVision.AnalyzeImageRequest(); // AnalyzeImageRequest | A JSON document with a URL pointing to the image that is to be analyzed.
let opts = {
  'detectHandwriting': false // Boolean | If 'true' is specified, handwriting recognition is performed. If this parameter is set to 'false' or is not specified, printed text recognition is performed.
};
apiInstance.recognizeText(imageUrl, opts, (error, data, response) => {
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
 **imageUrl** | [**AnalyzeImageRequest**](AnalyzeImageRequest.md)| A JSON document with a URL pointing to the image that is to be analyzed. | 
 **detectHandwriting** | **Boolean**| If &#39;true&#39; is specified, handwriting recognition is performed. If this parameter is set to &#39;false&#39; or is not specified, printed text recognition is performed. | [optional] [default to false]

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tagImage

> TagResult tagImage(imageUrl, opts)



This operation generates a list of words, or tags, that are relevant to the content of the supplied image. The Computer Vision API can return tags based on objects, living beings, scenery or actions found in images. Unlike categories, tags are not organized according to a hierarchical classification system, but correspond to image content. Tags may contain hints to avoid ambiguity or provide context, for example the tag &#39;cello&#39; may be accompanied by the hint &#39;musical instrument&#39;. All tags are in English.

### Example

```javascript
import ComputerVision from 'computer_vision';
let defaultClient = ComputerVision.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ComputerVision.DefaultApi();
let imageUrl = new ComputerVision.AnalyzeImageRequest(); // AnalyzeImageRequest | A JSON document with a URL pointing to the image that is to be analyzed.
let opts = {
  'language': "'en'" // String | The desired language for output generation. If this parameter is not specified, the default value is &quot;en&quot;.Supported languages:en - English, Default. es - Spanish, ja - Japanese, pt - Portuguese, zh - Simplified Chinese.
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
 **imageUrl** | [**AnalyzeImageRequest**](AnalyzeImageRequest.md)| A JSON document with a URL pointing to the image that is to be analyzed. | 
 **language** | **String**| The desired language for output generation. If this parameter is not specified, the default value is &amp;quot;en&amp;quot;.Supported languages:en - English, Default. es - Spanish, ja - Japanese, pt - Portuguese, zh - Simplified Chinese. | [optional] [default to &#39;en&#39;]

### Return type

[**TagResult**](TagResult.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

