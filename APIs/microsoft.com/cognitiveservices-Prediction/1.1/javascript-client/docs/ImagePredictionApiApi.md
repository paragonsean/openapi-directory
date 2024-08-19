# PredictionEndpoint.ImagePredictionApiApi

All URIs are relative to *https://southcentralus.api.cognitive.microsoft.com/customvision/v1.1/Prediction*

Method | HTTP request | Description
------------- | ------------- | -------------
[**predictImage**](ImagePredictionApiApi.md#predictImage) | **POST** /{projectId}/image | Predict an image and saves the result
[**predictImageUrl**](ImagePredictionApiApi.md#predictImageUrl) | **POST** /{projectId}/url | Predict an image url and saves the result
[**predictImageUrlWithNoStore**](ImagePredictionApiApi.md#predictImageUrlWithNoStore) | **POST** /{projectId}/url/nostore | Predict an image url without saving the result
[**predictImageWithNoStore**](ImagePredictionApiApi.md#predictImageWithNoStore) | **POST** /{projectId}/image/nostore | Predict an image without saving the result



## predictImage

> ImagePredictionResultModel predictImage(projectId, predictionKey, imageData, opts)

Predict an image and saves the result

### Example

```javascript
import PredictionEndpoint from 'prediction_endpoint';

let apiInstance = new PredictionEndpoint.ImagePredictionApiApi();
let projectId = "64b822c5-8082-4b36-a426-27225f4aa18c"; // String | The project id
let predictionKey = "{API Key}"; // String | 
let imageData = "/path/to/file"; // File | 
let opts = {
  'iterationId': "fe1e83c4-6f50-4899-9544-6bb08cf0e15a", // String | Optional. Specifies the id of a particular iteration to evaluate against.              The default iteration for the project will be used when not specified
  'application': "application_example" // String | Optional. Specifies the name of application using the endpoint
};
apiInstance.predictImage(projectId, predictionKey, imageData, opts, (error, data, response) => {
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
 **projectId** | **String**| The project id | 
 **predictionKey** | **String**|  | 
 **imageData** | **File**|  | 
 **iterationId** | **String**| Optional. Specifies the id of a particular iteration to evaluate against.              The default iteration for the project will be used when not specified | [optional] 
 **application** | **String**| Optional. Specifies the name of application using the endpoint | [optional] 

### Return type

[**ImagePredictionResultModel**](ImagePredictionResultModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json, application/xml, text/json, text/xml


## predictImageUrl

> ImagePredictionResultModel predictImageUrl(projectId, predictionKey, imageUrl, opts)

Predict an image url and saves the result

### Example

```javascript
import PredictionEndpoint from 'prediction_endpoint';

let apiInstance = new PredictionEndpoint.ImagePredictionApiApi();
let projectId = "64b822c5-8082-4b36-a426-27225f4aa18c"; // String | The project id
let predictionKey = "{API Key}"; // String | 
let imageUrl = new PredictionEndpoint.ImageUrl(); // ImageUrl | An {Iris.Web.Api.Models.ImageUrl} that contains the url of the image to be evaluated
let opts = {
  'iterationId': "fe1e83c4-6f50-4899-9544-6bb08cf0e15a", // String | Optional. Specifies the id of a particular iteration to evaluate against.              The default iteration for the project will be used when not specified
  'application': "application_example" // String | Optional. Specifies the name of application using the endpoint
};
apiInstance.predictImageUrl(projectId, predictionKey, imageUrl, opts, (error, data, response) => {
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
 **projectId** | **String**| The project id | 
 **predictionKey** | **String**|  | 
 **imageUrl** | [**ImageUrl**](ImageUrl.md)| An {Iris.Web.Api.Models.ImageUrl} that contains the url of the image to be evaluated | 
 **iterationId** | **String**| Optional. Specifies the id of a particular iteration to evaluate against.              The default iteration for the project will be used when not specified | [optional] 
 **application** | **String**| Optional. Specifies the name of application using the endpoint | [optional] 

### Return type

[**ImagePredictionResultModel**](ImagePredictionResultModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## predictImageUrlWithNoStore

> ImagePredictionResultModel predictImageUrlWithNoStore(projectId, predictionKey, imageUrl, opts)

Predict an image url without saving the result

### Example

```javascript
import PredictionEndpoint from 'prediction_endpoint';

let apiInstance = new PredictionEndpoint.ImagePredictionApiApi();
let projectId = "projectId_example"; // String | The project id
let predictionKey = "{API Key}"; // String | 
let imageUrl = new PredictionEndpoint.ImageUrl(); // ImageUrl | An {Iris.Web.Api.Models.ImageUrl} that contains the url of the image to be evaluated
let opts = {
  'iterationId': "iterationId_example", // String | Optional. Specifies the id of a particular iteration to evaluate against.              The default iteration for the project will be used when not specified
  'application': "application_example" // String | Optional. Specifies the name of application using the endpoint
};
apiInstance.predictImageUrlWithNoStore(projectId, predictionKey, imageUrl, opts, (error, data, response) => {
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
 **projectId** | **String**| The project id | 
 **predictionKey** | **String**|  | 
 **imageUrl** | [**ImageUrl**](ImageUrl.md)| An {Iris.Web.Api.Models.ImageUrl} that contains the url of the image to be evaluated | 
 **iterationId** | **String**| Optional. Specifies the id of a particular iteration to evaluate against.              The default iteration for the project will be used when not specified | [optional] 
 **application** | **String**| Optional. Specifies the name of application using the endpoint | [optional] 

### Return type

[**ImagePredictionResultModel**](ImagePredictionResultModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## predictImageWithNoStore

> ImagePredictionResultModel predictImageWithNoStore(projectId, predictionKey, imageData, opts)

Predict an image without saving the result

### Example

```javascript
import PredictionEndpoint from 'prediction_endpoint';

let apiInstance = new PredictionEndpoint.ImagePredictionApiApi();
let projectId = "projectId_example"; // String | The project id
let predictionKey = "{API Key}"; // String | 
let imageData = "/path/to/file"; // File | 
let opts = {
  'iterationId': "iterationId_example", // String | Optional. Specifies the id of a particular iteration to evaluate against.              The default iteration for the project will be used when not specified
  'application': "application_example" // String | Optional. Specifies the name of application using the endpoint
};
apiInstance.predictImageWithNoStore(projectId, predictionKey, imageData, opts, (error, data, response) => {
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
 **projectId** | **String**| The project id | 
 **predictionKey** | **String**|  | 
 **imageData** | **File**|  | 
 **iterationId** | **String**| Optional. Specifies the id of a particular iteration to evaluate against.              The default iteration for the project will be used when not specified | [optional] 
 **application** | **String**| Optional. Specifies the name of application using the endpoint | [optional] 

### Return type

[**ImagePredictionResultModel**](ImagePredictionResultModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json, application/xml, text/json, text/xml

