# ComputerVisionClient.DefaultApi

All URIs are relative to *https://westcentralus.api.cognitive.microsoft.com/vision/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batchReadFile**](DefaultApi.md#batchReadFile) | **POST** /read/core/asyncBatchAnalyze | 
[**getReadOperationResult**](DefaultApi.md#getReadOperationResult) | **GET** /read/operations/{operationId} | 
[**getTextOperationResult**](DefaultApi.md#getTextOperationResult) | **GET** /textOperations/{operationId} | 
[**recognizeText**](DefaultApi.md#recognizeText) | **POST** /recognizeText | 



## batchReadFile

> batchReadFile(imageUrl)



Use this interface to get the result of a Read operation, employing the state-of-the-art Optical Character Recognition (OCR) algorithms optimized for text-heavy documents. When you use the Read File interface, the response contains a field called &#39;Operation-Location&#39;. The &#39;Operation-Location&#39; field contains the URL that you must use for your &#39;GetReadOperationResult&#39; operation to access OCR results.​

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
apiInstance.batchReadFile(imageUrl, (error, data, response) => {
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
 **imageUrl** | [**ImageUrl**](ImageUrl.md)| A JSON document with a URL pointing to the image that is to be analyzed. | 

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getReadOperationResult

> ReadOperationResult getReadOperationResult(operationId)



This interface is used for getting OCR results of Read operation. The URL to this interface should be retrieved from &#39;Operation-Location&#39; field returned from Batch Read File interface.

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
let operationId = "e56ffa6e-1ee4-4042-bc07-993db706c95f"; // String | Id of read operation returned in the response of the 'Batch Read File' interface.
apiInstance.getReadOperationResult(operationId, (error, data, response) => {
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
 **operationId** | **String**| Id of read operation returned in the response of the &#39;Batch Read File&#39; interface. | 

### Return type

[**ReadOperationResult**](ReadOperationResult.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTextOperationResult

> TextOperationResult getTextOperationResult(operationId)



This interface is used for getting text operation result. The URL to this interface should be retrieved from &#39;Operation-Location&#39; field returned from Recognize Text interface.

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
let operationId = "49a36324-fc4b-4387-aa06-090cfbf0064f"; // String | Id of the text operation returned in the response of the 'Recognize Text'
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
 **operationId** | **String**| Id of the text operation returned in the response of the &#39;Recognize Text&#39; | 

### Return type

[**TextOperationResult**](TextOperationResult.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## recognizeText

> recognizeText(mode, imageUrl)



Recognize Text operation. When you use the Recognize Text interface, the response contains a field called &#39;Operation-Location&#39;. The &#39;Operation-Location&#39; field contains the URL that you must use for your Get Recognize Text Operation Result operation.

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
let mode = "Handwritten"; // String | Type of text to recognize.
let imageUrl = new ComputerVisionClient.ImageUrl(); // ImageUrl | A JSON document with a URL pointing to the image that is to be analyzed.
apiInstance.recognizeText(mode, imageUrl, (error, data, response) => {
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
 **mode** | **String**| Type of text to recognize. | 
 **imageUrl** | [**ImageUrl**](ImageUrl.md)| A JSON document with a URL pointing to the image that is to be analyzed. | 

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

