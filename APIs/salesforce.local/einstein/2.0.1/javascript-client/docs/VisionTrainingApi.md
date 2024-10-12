# EinsteinVisionAndEinsteinLanguage.VisionTrainingApi

All URIs are relative to *http://salesforce.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getTrainStatusAndProgress1**](VisionTrainingApi.md#getTrainStatusAndProgress1) | **GET** /v2/vision/train/{modelId} | Get Training Status
[**retrain1**](VisionTrainingApi.md#retrain1) | **POST** /v2/vision/retrain | Retrain a Dataset
[**train1**](VisionTrainingApi.md#train1) | **POST** /v2/vision/train | Train a Dataset



## getTrainStatusAndProgress1

> TrainResponse getTrainStatusAndProgress1(modelId)

Get Training Status

Returns the status of a model&#39;s training process. Use the progress field to determine how far the training has progressed. When training completes successfully, the status is SUCCEEDED and the progress is 1.

### Example

```javascript
import EinsteinVisionAndEinsteinLanguage from 'einstein_vision_and_einstein_language';
let defaultClient = EinsteinVisionAndEinsteinLanguage.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_token
let bearer_token = defaultClient.authentications['bearer_token'];
bearer_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new EinsteinVisionAndEinsteinLanguage.VisionTrainingApi();
let modelId = "SomeModelId"; // String | 
apiInstance.getTrainStatusAndProgress1(modelId, (error, data, response) => {
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

[**TrainResponse**](TrainResponse.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrain1

> TrainResponse retrain1(opts)

Retrain a Dataset

Retrains a dataset and updates a model. Use this API call when you want to update a model and keep the model ID instead of creating a new model.

### Example

```javascript
import EinsteinVisionAndEinsteinLanguage from 'einstein_vision_and_einstein_language';
let defaultClient = EinsteinVisionAndEinsteinLanguage.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_token
let bearer_token = defaultClient.authentications['bearer_token'];
bearer_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new EinsteinVisionAndEinsteinLanguage.VisionTrainingApi();
let opts = {
  'algorithm': "algorithm_example", // String | Specifies the algorithm used to train the dataset. Optional. Use this parameter only when training a dataset with a type of image-detection. Valid values are object-detection-v1 and retail-execution.
  'epochs': 56, // Number | Number of training iterations for the neural network. Optional.
  'learningRate': 3.4, // Number | Specifies how much the gradient affects the optimization of the model at each time step. Optional.
  'modelId': "modelId_example", // String | ID of the model to be updated from the training.
  'trainParams': new EinsteinVisionAndEinsteinLanguage.V2VisionTrainParams() // V2VisionTrainParams | 
};
apiInstance.retrain1(opts, (error, data, response) => {
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
 **algorithm** | **String**| Specifies the algorithm used to train the dataset. Optional. Use this parameter only when training a dataset with a type of image-detection. Valid values are object-detection-v1 and retail-execution. | [optional] 
 **epochs** | **Number**| Number of training iterations for the neural network. Optional. | [optional] 
 **learningRate** | **Number**| Specifies how much the gradient affects the optimization of the model at each time step. Optional. | [optional] 
 **modelId** | **String**| ID of the model to be updated from the training. | [optional] 
 **trainParams** | [**V2VisionTrainParams**](V2VisionTrainParams.md)|  | [optional] 

### Return type

[**TrainResponse**](TrainResponse.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## train1

> TrainResponse train1(opts)

Train a Dataset

Trains a dataset and creates a model.

### Example

```javascript
import EinsteinVisionAndEinsteinLanguage from 'einstein_vision_and_einstein_language';
let defaultClient = EinsteinVisionAndEinsteinLanguage.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_token
let bearer_token = defaultClient.authentications['bearer_token'];
bearer_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new EinsteinVisionAndEinsteinLanguage.VisionTrainingApi();
let opts = {
  'algorithm': "algorithm_example", // String | Specifies the algorithm used to train the dataset. Optional. Use this parameter only when training a dataset with a type of image-detection. Valid values are object-detection-v1 and retail-execution.
  'datasetId': 789, // Number | ID of the dataset to train.
  'epochs': 56, // Number | Number of training iterations for the neural network. Optional.
  'learningRate': 3.4, // Number | Specifies how much the gradient affects the optimization of the model at each time step. Optional.
  'name': "name_example", // String | Name of the model. Maximum length is 180 characters.
  'trainParams': new EinsteinVisionAndEinsteinLanguage.V2VisionTrainParams() // V2VisionTrainParams | 
};
apiInstance.train1(opts, (error, data, response) => {
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
 **algorithm** | **String**| Specifies the algorithm used to train the dataset. Optional. Use this parameter only when training a dataset with a type of image-detection. Valid values are object-detection-v1 and retail-execution. | [optional] 
 **datasetId** | **Number**| ID of the dataset to train. | [optional] 
 **epochs** | **Number**| Number of training iterations for the neural network. Optional. | [optional] 
 **learningRate** | **Number**| Specifies how much the gradient affects the optimization of the model at each time step. Optional. | [optional] 
 **name** | **String**| Name of the model. Maximum length is 180 characters. | [optional] 
 **trainParams** | [**V2VisionTrainParams**](V2VisionTrainParams.md)|  | [optional] 

### Return type

[**TrainResponse**](TrainResponse.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

