# FormRecognizerClient.DefaultApi

All URIs are relative to *https://azure.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analyzeWithCustomModel**](DefaultApi.md#analyzeWithCustomModel) | **POST** /custom/models/{id}/analyze | Analyze Form
[**deleteCustomModel**](DefaultApi.md#deleteCustomModel) | **DELETE** /custom/models/{id} | Delete Model
[**getCustomModel**](DefaultApi.md#getCustomModel) | **GET** /custom/models/{id} | Get Model
[**getCustomModels**](DefaultApi.md#getCustomModels) | **GET** /custom/models | Get Models
[**getExtractedKeys**](DefaultApi.md#getExtractedKeys) | **GET** /custom/models/{id}/keys | Get Keys
[**trainCustomModel**](DefaultApi.md#trainCustomModel) | **POST** /custom/train | Train Model



## analyzeWithCustomModel

> AnalyzeResult analyzeWithCustomModel(id, analyzeWithCustomModelRequest, opts)

Analyze Form

Extract key-value pairs from a given document. The input document must be of one of the supported content types - &#39;application/pdf&#39;, &#39;image/jpeg&#39; or &#39;image/png&#39;. A success response is returned in JSON.

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
let id = "id_example"; // String | Model Identifier to analyze the document with.
let analyzeWithCustomModelRequest = new FormRecognizerClient.AnalyzeWithCustomModelRequest(); // AnalyzeWithCustomModelRequest | 
let opts = {
  'keys': ["null"] // [String] | An optional list of known keys to extract the values for.
};
apiInstance.analyzeWithCustomModel(id, analyzeWithCustomModelRequest, opts, (error, data, response) => {
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
 **id** | **String**| Model Identifier to analyze the document with. | 
 **analyzeWithCustomModelRequest** | [**AnalyzeWithCustomModelRequest**](AnalyzeWithCustomModelRequest.md)|  | 
 **keys** | [**[String]**](String.md)| An optional list of known keys to extract the values for. | [optional] 

### Return type

[**AnalyzeResult**](AnalyzeResult.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/pdf, image/jpeg, image/png, multipart/form-data
- **Accept**: application/json


## deleteCustomModel

> deleteCustomModel(id)

Delete Model

Delete model artifacts.

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
let id = "id_example"; // String | The identifier of the model to delete.
apiInstance.deleteCustomModel(id, (error, data, response) => {
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
 **id** | **String**| The identifier of the model to delete. | 

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCustomModel

> ModelResult getCustomModel(id)

Get Model

Get information about a model.

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
let id = "id_example"; // String | Model identifier.
apiInstance.getCustomModel(id, (error, data, response) => {
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
 **id** | **String**| Model identifier. | 

### Return type

[**ModelResult**](ModelResult.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCustomModels

> ModelsResult getCustomModels()

Get Models

Get information about all trained custom models

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
apiInstance.getCustomModels((error, data, response) => {
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

[**ModelsResult**](ModelsResult.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getExtractedKeys

> KeysResult getExtractedKeys(id)

Get Keys

Retrieve the keys that were   extracted during the training of the specified model.

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
let id = "id_example"; // String | Model identifier.
apiInstance.getExtractedKeys(id, (error, data, response) => {
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
 **id** | **String**| Model identifier. | 

### Return type

[**KeysResult**](KeysResult.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## trainCustomModel

> TrainResult trainCustomModel(trainRequest)

Train Model

Create and train a custom model. The train request must include a source parameter that is either an externally accessible Azure Storage blob container Uri (preferably a Shared Access Signature Uri) or valid path to a data folder in a locally mounted drive. When local paths are specified, they must follow the Linux/Unix path format and be an absolute path rooted to the input mount configuration   setting value e.g., if &#39;{Mounts:Input}&#39; configuration setting value is &#39;/input&#39; then a valid source path would be &#39;/input/contosodataset&#39;. All data to be trained is expected to be directly under the source folder. Subfolders are not supported. Models are trained using documents that are of the following content type - &#39;application/pdf&#39;, &#39;image/jpeg&#39; and &#39;image/png&#39;.\&quot;   Other type of content is ignored.

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
let trainRequest = new FormRecognizerClient.TrainRequest(); // TrainRequest | Request object for training.
apiInstance.trainCustomModel(trainRequest, (error, data, response) => {
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
 **trainRequest** | [**TrainRequest**](TrainRequest.md)| Request object for training. | 

### Return type

[**TrainResult**](TrainResult.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

