# CustomVisionPredictionClient.ImagePredictionApiApi

All URIs are relative to *https://southcentralus.api.cognitive.microsoft.com/customvision/v3.0/prediction*

Method | HTTP request | Description
------------- | ------------- | -------------
[**classifyImage**](ImagePredictionApiApi.md#classifyImage) | **POST** /{projectId}/classify/iterations/{publishedName}/image | Classify an image and saves the result.
[**classifyImageUrl**](ImagePredictionApiApi.md#classifyImageUrl) | **POST** /{projectId}/classify/iterations/{publishedName}/url | Classify an image url and saves the result.
[**classifyImageUrlWithNoStore**](ImagePredictionApiApi.md#classifyImageUrlWithNoStore) | **POST** /{projectId}/classify/iterations/{publishedName}/url/nostore | Classify an image url without saving the result.
[**classifyImageWithNoStore**](ImagePredictionApiApi.md#classifyImageWithNoStore) | **POST** /{projectId}/classify/iterations/{publishedName}/image/nostore | Classify an image without saving the result.
[**detectImage**](ImagePredictionApiApi.md#detectImage) | **POST** /{projectId}/detect/iterations/{publishedName}/image | Detect objects in an image and saves the result.
[**detectImageUrl**](ImagePredictionApiApi.md#detectImageUrl) | **POST** /{projectId}/detect/iterations/{publishedName}/url | Detect objects in an image url and saves the result.
[**detectImageUrlWithNoStore**](ImagePredictionApiApi.md#detectImageUrlWithNoStore) | **POST** /{projectId}/detect/iterations/{publishedName}/url/nostore | Detect objects in an image url without saving the result.
[**detectImageWithNoStore**](ImagePredictionApiApi.md#detectImageWithNoStore) | **POST** /{projectId}/detect/iterations/{publishedName}/image/nostore | Detect objects in an image without saving the result.



## classifyImage

> ImagePrediction classifyImage(projectId, publishedName, imageData, opts)

Classify an image and saves the result.

### Example

```javascript
import CustomVisionPredictionClient from 'custom_vision_prediction_client';
let defaultClient = CustomVisionPredictionClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new CustomVisionPredictionClient.ImagePredictionApiApi();
let projectId = "64b822c5-8082-4b36-a426-27225f4aa18c"; // String | The project id.
let publishedName = "MyModel1"; // String | Specifies the name of the model to evaluate against.
let imageData = "/path/to/file"; // File | Binary image data. Supported formats are JPEG, GIF, PNG, and BMP. Supports images up to 4MB.
let opts = {
  'application': "application_example" // String | Optional. Specifies the name of application using the endpoint.
};
apiInstance.classifyImage(projectId, publishedName, imageData, opts, (error, data, response) => {
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
 **publishedName** | **String**| Specifies the name of the model to evaluate against. | 
 **imageData** | **File**| Binary image data. Supported formats are JPEG, GIF, PNG, and BMP. Supports images up to 4MB. | 
 **application** | **String**| Optional. Specifies the name of application using the endpoint. | [optional] 

### Return type

[**ImagePrediction**](ImagePrediction.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json, application/xml, text/xml


## classifyImageUrl

> ImagePrediction classifyImageUrl(projectId, publishedName, imageUrl, opts)

Classify an image url and saves the result.

### Example

```javascript
import CustomVisionPredictionClient from 'custom_vision_prediction_client';
let defaultClient = CustomVisionPredictionClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new CustomVisionPredictionClient.ImagePredictionApiApi();
let projectId = "64b822c5-8082-4b36-a426-27225f4aa18c"; // String | The project id.
let publishedName = "MyModel1"; // String | Specifies the name of the model to evaluate against.
let imageUrl = new CustomVisionPredictionClient.ImageUrl(); // ImageUrl | An ImageUrl that contains the url of the image to be evaluated.
let opts = {
  'application': "application_example" // String | Optional. Specifies the name of application using the endpoint.
};
apiInstance.classifyImageUrl(projectId, publishedName, imageUrl, opts, (error, data, response) => {
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
 **publishedName** | **String**| Specifies the name of the model to evaluate against. | 
 **imageUrl** | [**ImageUrl**](ImageUrl.md)| An ImageUrl that contains the url of the image to be evaluated. | 
 **application** | **String**| Optional. Specifies the name of application using the endpoint. | [optional] 

### Return type

[**ImagePrediction**](ImagePrediction.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
- **Accept**: application/json, application/xml, text/xml


## classifyImageUrlWithNoStore

> ImagePrediction classifyImageUrlWithNoStore(projectId, publishedName, imageUrl, opts)

Classify an image url without saving the result.

### Example

```javascript
import CustomVisionPredictionClient from 'custom_vision_prediction_client';
let defaultClient = CustomVisionPredictionClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new CustomVisionPredictionClient.ImagePredictionApiApi();
let projectId = "64b822c5-8082-4b36-a426-27225f4aa18c"; // String | The project id.
let publishedName = "MyModel1"; // String | Specifies the name of the model to evaluate against.
let imageUrl = new CustomVisionPredictionClient.ImageUrl(); // ImageUrl | An {Iris.Web.Api.Models.ImageUrl} that contains the url of the image to be evaluated.
let opts = {
  'application': "application_example" // String | Optional. Specifies the name of application using the endpoint.
};
apiInstance.classifyImageUrlWithNoStore(projectId, publishedName, imageUrl, opts, (error, data, response) => {
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
 **publishedName** | **String**| Specifies the name of the model to evaluate against. | 
 **imageUrl** | [**ImageUrl**](ImageUrl.md)| An {Iris.Web.Api.Models.ImageUrl} that contains the url of the image to be evaluated. | 
 **application** | **String**| Optional. Specifies the name of application using the endpoint. | [optional] 

### Return type

[**ImagePrediction**](ImagePrediction.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
- **Accept**: application/json, application/xml, text/xml


## classifyImageWithNoStore

> ImagePrediction classifyImageWithNoStore(projectId, publishedName, imageData, opts)

Classify an image without saving the result.

### Example

```javascript
import CustomVisionPredictionClient from 'custom_vision_prediction_client';
let defaultClient = CustomVisionPredictionClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new CustomVisionPredictionClient.ImagePredictionApiApi();
let projectId = "64b822c5-8082-4b36-a426-27225f4aa18c"; // String | The project id.
let publishedName = "MyModel1"; // String | Specifies the name of the model to evaluate against.
let imageData = "/path/to/file"; // File | Binary image data. Supported formats are JPEG, GIF, PNG, and BMP. Supports images up to 0MB.
let opts = {
  'application': "application_example" // String | Optional. Specifies the name of application using the endpoint.
};
apiInstance.classifyImageWithNoStore(projectId, publishedName, imageData, opts, (error, data, response) => {
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
 **publishedName** | **String**| Specifies the name of the model to evaluate against. | 
 **imageData** | **File**| Binary image data. Supported formats are JPEG, GIF, PNG, and BMP. Supports images up to 0MB. | 
 **application** | **String**| Optional. Specifies the name of application using the endpoint. | [optional] 

### Return type

[**ImagePrediction**](ImagePrediction.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json, application/xml, text/xml


## detectImage

> ImagePrediction detectImage(projectId, publishedName, imageData, opts)

Detect objects in an image and saves the result.

### Example

```javascript
import CustomVisionPredictionClient from 'custom_vision_prediction_client';
let defaultClient = CustomVisionPredictionClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new CustomVisionPredictionClient.ImagePredictionApiApi();
let projectId = "64b822c5-8082-4b36-a426-27225f4aa18c"; // String | The project id.
let publishedName = "MyModel1"; // String | Specifies the name of the model to evaluate against.
let imageData = "/path/to/file"; // File | Binary image data. Supported formats are JPEG, GIF, PNG, and BMP. Supports images up to 4MB.
let opts = {
  'application': "application_example" // String | Optional. Specifies the name of application using the endpoint.
};
apiInstance.detectImage(projectId, publishedName, imageData, opts, (error, data, response) => {
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
 **publishedName** | **String**| Specifies the name of the model to evaluate against. | 
 **imageData** | **File**| Binary image data. Supported formats are JPEG, GIF, PNG, and BMP. Supports images up to 4MB. | 
 **application** | **String**| Optional. Specifies the name of application using the endpoint. | [optional] 

### Return type

[**ImagePrediction**](ImagePrediction.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json, application/xml, text/xml


## detectImageUrl

> ImagePrediction detectImageUrl(projectId, publishedName, imageUrl, opts)

Detect objects in an image url and saves the result.

### Example

```javascript
import CustomVisionPredictionClient from 'custom_vision_prediction_client';
let defaultClient = CustomVisionPredictionClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new CustomVisionPredictionClient.ImagePredictionApiApi();
let projectId = "64b822c5-8082-4b36-a426-27225f4aa18c"; // String | The project id.
let publishedName = "MyModel1"; // String | Specifies the name of the model to evaluate against.
let imageUrl = new CustomVisionPredictionClient.ImageUrl(); // ImageUrl | An ImageUrl that contains the url of the image to be evaluated.
let opts = {
  'application': "application_example" // String | Optional. Specifies the name of application using the endpoint.
};
apiInstance.detectImageUrl(projectId, publishedName, imageUrl, opts, (error, data, response) => {
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
 **publishedName** | **String**| Specifies the name of the model to evaluate against. | 
 **imageUrl** | [**ImageUrl**](ImageUrl.md)| An ImageUrl that contains the url of the image to be evaluated. | 
 **application** | **String**| Optional. Specifies the name of application using the endpoint. | [optional] 

### Return type

[**ImagePrediction**](ImagePrediction.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
- **Accept**: application/json, application/xml, text/xml


## detectImageUrlWithNoStore

> ImagePrediction detectImageUrlWithNoStore(projectId, publishedName, imageUrl, opts)

Detect objects in an image url without saving the result.

### Example

```javascript
import CustomVisionPredictionClient from 'custom_vision_prediction_client';
let defaultClient = CustomVisionPredictionClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new CustomVisionPredictionClient.ImagePredictionApiApi();
let projectId = "64b822c5-8082-4b36-a426-27225f4aa18c"; // String | The project id.
let publishedName = "MyModel1"; // String | Specifies the name of the model to evaluate against.
let imageUrl = new CustomVisionPredictionClient.ImageUrl(); // ImageUrl | An {Iris.Web.Api.Models.ImageUrl} that contains the url of the image to be evaluated.
let opts = {
  'application': "application_example" // String | Optional. Specifies the name of application using the endpoint.
};
apiInstance.detectImageUrlWithNoStore(projectId, publishedName, imageUrl, opts, (error, data, response) => {
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
 **publishedName** | **String**| Specifies the name of the model to evaluate against. | 
 **imageUrl** | [**ImageUrl**](ImageUrl.md)| An {Iris.Web.Api.Models.ImageUrl} that contains the url of the image to be evaluated. | 
 **application** | **String**| Optional. Specifies the name of application using the endpoint. | [optional] 

### Return type

[**ImagePrediction**](ImagePrediction.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
- **Accept**: application/json, application/xml, text/xml


## detectImageWithNoStore

> ImagePrediction detectImageWithNoStore(projectId, publishedName, imageData, opts)

Detect objects in an image without saving the result.

### Example

```javascript
import CustomVisionPredictionClient from 'custom_vision_prediction_client';
let defaultClient = CustomVisionPredictionClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new CustomVisionPredictionClient.ImagePredictionApiApi();
let projectId = "64b822c5-8082-4b36-a426-27225f4aa18c"; // String | The project id.
let publishedName = "MyModel1"; // String | Specifies the name of the model to evaluate against.
let imageData = "/path/to/file"; // File | Binary image data. Supported formats are JPEG, GIF, PNG, and BMP. Supports images up to 0MB.
let opts = {
  'application': "application_example" // String | Optional. Specifies the name of application using the endpoint.
};
apiInstance.detectImageWithNoStore(projectId, publishedName, imageData, opts, (error, data, response) => {
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
 **publishedName** | **String**| Specifies the name of the model to evaluate against. | 
 **imageData** | **File**| Binary image data. Supported formats are JPEG, GIF, PNG, and BMP. Supports images up to 0MB. | 
 **application** | **String**| Optional. Specifies the name of application using the endpoint. | [optional] 

### Return type

[**ImagePrediction**](ImagePrediction.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json, application/xml, text/xml

