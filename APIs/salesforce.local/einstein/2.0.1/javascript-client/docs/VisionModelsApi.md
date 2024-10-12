# EinsteinVisionAndEinsteinLanguage.VisionModelsApi

All URIs are relative to *http://salesforce.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteModel1**](VisionModelsApi.md#deleteModel1) | **DELETE** /v2/vision/models/{modelId} | Delete a Model
[**getTrainedModelLearningCurve1**](VisionModelsApi.md#getTrainedModelLearningCurve1) | **GET** /v2/vision/models/{modelId}/lc | Get Model Learning Curve
[**getTrainedModelMetrics1**](VisionModelsApi.md#getTrainedModelMetrics1) | **GET** /v2/vision/models/{modelId} | Get Model Metrics
[**getTrainedModels1**](VisionModelsApi.md#getTrainedModels1) | **GET** /v2/vision/datasets/{datasetId}/models | Get All Models



## deleteModel1

> DeletionResponse deleteModel1(modelId)

Delete a Model

Deletes the specified model.

### Example

```javascript
import EinsteinVisionAndEinsteinLanguage from 'einstein_vision_and_einstein_language';
let defaultClient = EinsteinVisionAndEinsteinLanguage.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_token
let bearer_token = defaultClient.authentications['bearer_token'];
bearer_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new EinsteinVisionAndEinsteinLanguage.VisionModelsApi();
let modelId = "SomeModelId"; // String | 
apiInstance.deleteModel1(modelId, (error, data, response) => {
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
 **modelId** | **String**|  | 

### Return type

[**DeletionResponse**](DeletionResponse.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTrainedModelLearningCurve1

> LearningCurveList getTrainedModelLearningCurve1(modelId, opts)

Get Model Learning Curve

Returns the metrics for each epoch in a model.

### Example

```javascript
import EinsteinVisionAndEinsteinLanguage from 'einstein_vision_and_einstein_language';
let defaultClient = EinsteinVisionAndEinsteinLanguage.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_token
let bearer_token = defaultClient.authentications['bearer_token'];
bearer_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new EinsteinVisionAndEinsteinLanguage.VisionModelsApi();
let modelId = "SomeModelId"; // String | 
let opts = {
  'offset': "'0'", // String | Index of the epoch from which you want to start paging
  'count': "'25'" // String | Number of epoch to return. Maximum valid value is 25.
};
apiInstance.getTrainedModelLearningCurve1(modelId, opts, (error, data, response) => {
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
 **modelId** | **String**|  | 
 **offset** | **String**| Index of the epoch from which you want to start paging | [optional] [default to &#39;0&#39;]
 **count** | **String**| Number of epoch to return. Maximum valid value is 25. | [optional] [default to &#39;25&#39;]

### Return type

[**LearningCurveList**](LearningCurveList.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTrainedModelMetrics1

> Metrics getTrainedModelMetrics1(modelId)

Get Model Metrics

Returns the metrics for a model

### Example

```javascript
import EinsteinVisionAndEinsteinLanguage from 'einstein_vision_and_einstein_language';
let defaultClient = EinsteinVisionAndEinsteinLanguage.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_token
let bearer_token = defaultClient.authentications['bearer_token'];
bearer_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new EinsteinVisionAndEinsteinLanguage.VisionModelsApi();
let modelId = "SomeModelId"; // String | 
apiInstance.getTrainedModelMetrics1(modelId, (error, data, response) => {
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
 **modelId** | **String**|  | 

### Return type

[**Metrics**](Metrics.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTrainedModels1

> ModelList getTrainedModels1(datasetId, opts)

Get All Models

Returns all models for the specified dataset.

### Example

```javascript
import EinsteinVisionAndEinsteinLanguage from 'einstein_vision_and_einstein_language';
let defaultClient = EinsteinVisionAndEinsteinLanguage.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_token
let bearer_token = defaultClient.authentications['bearer_token'];
bearer_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new EinsteinVisionAndEinsteinLanguage.VisionModelsApi();
let datasetId = "SomeDatasetId"; // String | Dataset Id
let opts = {
  'offset': "'0'", // String | Index of the model from which you want to start paging.
  'count': "'100'" // String | Number of models to return.
};
apiInstance.getTrainedModels1(datasetId, opts, (error, data, response) => {
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
 **datasetId** | **String**| Dataset Id | 
 **offset** | **String**| Index of the model from which you want to start paging. | [optional] [default to &#39;0&#39;]
 **count** | **String**| Number of models to return. | [optional] [default to &#39;100&#39;]

### Return type

[**ModelList**](ModelList.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

