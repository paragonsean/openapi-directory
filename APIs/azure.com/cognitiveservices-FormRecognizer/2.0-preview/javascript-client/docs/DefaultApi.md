# FormRecognizerClient.DefaultApi

All URIs are relative to *https://azure.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analyzeLayoutAsync**](DefaultApi.md#analyzeLayoutAsync) | **POST** /layout/analyze | Analyze Layout
[**analyzeReceiptAsync**](DefaultApi.md#analyzeReceiptAsync) | **POST** /prebuilt/receipt/analyze | Analyze Receipt
[**analyzeWithCustomModel**](DefaultApi.md#analyzeWithCustomModel) | **POST** /custom/models/{modelId}/analyze | Analyze Form
[**deleteCustomModel**](DefaultApi.md#deleteCustomModel) | **DELETE** /custom/models/{modelId} | Delete Custom Model
[**getAnalyzeFormResult**](DefaultApi.md#getAnalyzeFormResult) | **GET** /custom/models/{modelId}/analyzeResults/{resultId} | Get Analyze Form Result
[**getAnalyzeLayoutResult**](DefaultApi.md#getAnalyzeLayoutResult) | **GET** /layout/analyzeResults/{resultId} | Get Analyze Layout Result
[**getAnalyzeReceiptResult**](DefaultApi.md#getAnalyzeReceiptResult) | **GET** /prebuilt/receipt/analyzeResults/{resultId} | Get Analyze Receipt Result
[**getCustomModel**](DefaultApi.md#getCustomModel) | **GET** /custom/models/{modelId} | Get Custom Model
[**getCustomModels**](DefaultApi.md#getCustomModels) | **GET** /custom/models | List Custom Models
[**trainCustomModelAsync**](DefaultApi.md#trainCustomModelAsync) | **POST** /custom/models | Train Custom Model



## analyzeLayoutAsync

> analyzeLayoutAsync(opts)

Analyze Layout

Extract text and layout information from a given document. The input document must be of one of the supported content types - &#39;application/pdf&#39;, &#39;image/jpeg&#39;, &#39;image/png&#39; or &#39;image/tiff&#39;. Alternatively, use &#39;application/json&#39; type to specify the location (Uri or local path) of the document to be analyzed.

### Example

```javascript
import FormRecognizerClient from 'form_recognizer_client';
let defaultClient = FormRecognizerClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FormRecognizerClient.DefaultApi();
let opts = {
  'fileStream': {key: null} // Object | .json, .pdf, .jpg, .png or .tiff type file stream.
};
apiInstance.analyzeLayoutAsync(opts, (error, data, response) => {
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
 **fileStream** | **Object**| .json, .pdf, .jpg, .png or .tiff type file stream. | [optional] 

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/pdf, application/json, image/jpeg, image/png, image/tiff
- **Accept**: application/json


## analyzeReceiptAsync

> analyzeReceiptAsync(opts)

Analyze Receipt

Extract field text and semantic values from a given receipt document. The input document must be of one of the supported content types - &#39;application/pdf&#39;, &#39;image/jpeg&#39;, &#39;image/png&#39; or &#39;image/tiff&#39;. Alternatively, use &#39;application/json&#39; type to specify the location (Uri or local path) of the document to be analyzed.

### Example

```javascript
import FormRecognizerClient from 'form_recognizer_client';
let defaultClient = FormRecognizerClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FormRecognizerClient.DefaultApi();
let opts = {
  'includeTextDetails': false, // Boolean | Include text lines and element references in the result.
  'fileStream': {key: null} // Object | .json, .pdf, .jpg, .png or .tiff type file stream.
};
apiInstance.analyzeReceiptAsync(opts, (error, data, response) => {
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
 **includeTextDetails** | **Boolean**| Include text lines and element references in the result. | [optional] [default to false]
 **fileStream** | **Object**| .json, .pdf, .jpg, .png or .tiff type file stream. | [optional] 

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/pdf, application/json, image/jpeg, image/png, image/tiff
- **Accept**: application/json


## analyzeWithCustomModel

> analyzeWithCustomModel(modelId, opts)

Analyze Form

Extract key-value pairs, tables, and semantic values from a given document. The input document must be of one of the supported content types - &#39;application/pdf&#39;, &#39;image/jpeg&#39;, &#39;image/png&#39; or &#39;image/tiff&#39;. Alternatively, use &#39;application/json&#39; type to specify the location (Uri or local path) of the document to be analyzed.

### Example

```javascript
import FormRecognizerClient from 'form_recognizer_client';
let defaultClient = FormRecognizerClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FormRecognizerClient.DefaultApi();
let modelId = "modelId_example"; // String | Model identifier.
let opts = {
  'includeTextDetails': false, // Boolean | Include text lines and element references in the result.
  'fileStream': {key: null} // Object | .json, .pdf, .jpg, .png or .tiff type file stream.
};
apiInstance.analyzeWithCustomModel(modelId, opts, (error, data, response) => {
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
 **modelId** | **String**| Model identifier. | 
 **includeTextDetails** | **Boolean**| Include text lines and element references in the result. | [optional] [default to false]
 **fileStream** | **Object**| .json, .pdf, .jpg, .png or .tiff type file stream. | [optional] 

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/pdf, application/json, image/jpeg, image/png, image/tiff
- **Accept**: */*


## deleteCustomModel

> deleteCustomModel(modelId)

Delete Custom Model

Mark model for deletion. Model artifacts will be permanently removed within a predetermined period.

### Example

```javascript
import FormRecognizerClient from 'form_recognizer_client';
let defaultClient = FormRecognizerClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FormRecognizerClient.DefaultApi();
let modelId = "modelId_example"; // String | Model identifier.
apiInstance.deleteCustomModel(modelId, (error, data, response) => {
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
 **modelId** | **String**| Model identifier. | 

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAnalyzeFormResult

> AnalyzeOperationResult getAnalyzeFormResult(modelId, resultId)

Get Analyze Form Result

Obtain current status and the result of the analyze form operation.

### Example

```javascript
import FormRecognizerClient from 'form_recognizer_client';
let defaultClient = FormRecognizerClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FormRecognizerClient.DefaultApi();
let modelId = "modelId_example"; // String | Model identifier.
let resultId = "resultId_example"; // String | Analyze operation result identifier.
apiInstance.getAnalyzeFormResult(modelId, resultId, (error, data, response) => {
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
 **modelId** | **String**| Model identifier. | 
 **resultId** | **String**| Analyze operation result identifier. | 

### Return type

[**AnalyzeOperationResult**](AnalyzeOperationResult.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAnalyzeLayoutResult

> AnalyzeOperationResult getAnalyzeLayoutResult(resultId)

Get Analyze Layout Result

Track the progress and obtain the result of the analyze layout operation

### Example

```javascript
import FormRecognizerClient from 'form_recognizer_client';
let defaultClient = FormRecognizerClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FormRecognizerClient.DefaultApi();
let resultId = "resultId_example"; // String | Analyze operation result identifier.
apiInstance.getAnalyzeLayoutResult(resultId, (error, data, response) => {
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
 **resultId** | **String**| Analyze operation result identifier. | 

### Return type

[**AnalyzeOperationResult**](AnalyzeOperationResult.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAnalyzeReceiptResult

> AnalyzeOperationResult getAnalyzeReceiptResult(resultId)

Get Analyze Receipt Result

Track the progress and obtain the result of the analyze receipt operation.

### Example

```javascript
import FormRecognizerClient from 'form_recognizer_client';
let defaultClient = FormRecognizerClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FormRecognizerClient.DefaultApi();
let resultId = "resultId_example"; // String | Analyze operation result identifier.
apiInstance.getAnalyzeReceiptResult(resultId, (error, data, response) => {
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
 **resultId** | **String**| Analyze operation result identifier. | 

### Return type

[**AnalyzeOperationResult**](AnalyzeOperationResult.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCustomModel

> Model getCustomModel(modelId, opts)

Get Custom Model

Get detailed information about a custom model.

### Example

```javascript
import FormRecognizerClient from 'form_recognizer_client';
let defaultClient = FormRecognizerClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FormRecognizerClient.DefaultApi();
let modelId = "modelId_example"; // String | Model identifier.
let opts = {
  'includeKeys': false // Boolean | Include list of extracted keys in model information.
};
apiInstance.getCustomModel(modelId, opts, (error, data, response) => {
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
 **modelId** | **String**| Model identifier. | 
 **includeKeys** | **Boolean**| Include list of extracted keys in model information. | [optional] [default to false]

### Return type

[**Model**](Model.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCustomModels

> Models getCustomModels(opts)

List Custom Models

Get information about all custom models

### Example

```javascript
import FormRecognizerClient from 'form_recognizer_client';
let defaultClient = FormRecognizerClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FormRecognizerClient.DefaultApi();
let opts = {
  'op': "'full'" // String | Specify whether to return summary or full list of models.
};
apiInstance.getCustomModels(opts, (error, data, response) => {
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
 **op** | **String**| Specify whether to return summary or full list of models. | [optional] [default to &#39;full&#39;]

### Return type

[**Models**](Models.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## trainCustomModelAsync

> trainCustomModelAsync(trainRequest)

Train Custom Model

Create and train a custom model. The request must include a source parameter that is either an externally accessible Azure storage blob container Uri (preferably a Shared Access Signature Uri) or valid path to a data folder in a locally mounted drive. When local paths are specified, they must follow the Linux/Unix path format and be an absolute path rooted to the input mount configuration setting value e.g., if &#39;{Mounts:Input}&#39; configuration setting value is &#39;/input&#39; then a valid source path would be &#39;/input/contosodataset&#39;. All data to be trained is expected to be under the source folder or sub folders under it. Models are trained using documents that are of the following content type - &#39;application/pdf&#39;, &#39;image/jpeg&#39;, &#39;image/png&#39;, &#39;image/tiff&#39;. Other type of content is ignored.

### Example

```javascript
import FormRecognizerClient from 'form_recognizer_client';
let defaultClient = FormRecognizerClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FormRecognizerClient.DefaultApi();
let trainRequest = new FormRecognizerClient.TrainRequest(); // TrainRequest | Training request parameters.
apiInstance.trainCustomModelAsync(trainRequest, (error, data, response) => {
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
 **trainRequest** | [**TrainRequest**](TrainRequest.md)| Training request parameters. | 

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*

