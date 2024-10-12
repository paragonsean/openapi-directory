# EinsteinVisionAndEinsteinLanguage.LanguageTrainingApi

All URIs are relative to *http://salesforce.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getTrainStatusAndProgress**](LanguageTrainingApi.md#getTrainStatusAndProgress) | **GET** /v2/language/train/{modelId} | Get Training Status
[**retrain**](LanguageTrainingApi.md#retrain) | **POST** /v2/language/retrain | Retrain a Dataset
[**train**](LanguageTrainingApi.md#train) | **POST** /v2/language/train | Train a Dataset



## getTrainStatusAndProgress

> TrainResponse getTrainStatusAndProgress(modelId)

Get Training Status

Returns the status of a model&#39;s training process. Use the progress field to determine how far the training has progressed. When training completes successfully, the status is SUCCEEDED and the progress is 1.

### Example

```javascript
import EinsteinVisionAndEinsteinLanguage from 'einstein_vision_and_einstein_language';
let defaultClient = EinsteinVisionAndEinsteinLanguage.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_token
let bearer_token = defaultClient.authentications['bearer_token'];
bearer_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new EinsteinVisionAndEinsteinLanguage.LanguageTrainingApi();
let modelId = "SomeModelId"; // String | Model Id
apiInstance.getTrainStatusAndProgress(modelId, (error, data, response) => {
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
 **modelId** | **String**| Model Id | 

### Return type

[**TrainResponse**](TrainResponse.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrain

> TrainResponse retrain(opts)

Retrain a Dataset

Retrains a dataset and updates a model. Use this API call when you want to update a model and keep the model ID instead of creating a new model.

### Example

```javascript
import EinsteinVisionAndEinsteinLanguage from 'einstein_vision_and_einstein_language';
let defaultClient = EinsteinVisionAndEinsteinLanguage.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_token
let bearer_token = defaultClient.authentications['bearer_token'];
bearer_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new EinsteinVisionAndEinsteinLanguage.LanguageTrainingApi();
let opts = {
  'algorithm': "algorithm_example", // String | Algorithm used for train
  'epochs': 56, // Number | Number of training iterations for the neural network. Optional.
  'learningRate': 3.4, // Number | N/A for intent or sentiment models.
  'modelId': "modelId_example", // String | ID of the model to be updated from the training.
  'trainParams': new EinsteinVisionAndEinsteinLanguage.V2LanguageTrainParams() // V2LanguageTrainParams | 
};
apiInstance.retrain(opts, (error, data, response) => {
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
 **algorithm** | **String**| Algorithm used for train | [optional] 
 **epochs** | **Number**| Number of training iterations for the neural network. Optional. | [optional] 
 **learningRate** | **Number**| N/A for intent or sentiment models. | [optional] 
 **modelId** | **String**| ID of the model to be updated from the training. | [optional] 
 **trainParams** | [**V2LanguageTrainParams**](V2LanguageTrainParams.md)|  | [optional] 

### Return type

[**TrainResponse**](TrainResponse.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## train

> TrainResponse train(opts)

Train a Dataset

Trains a dataset and creates a model.

### Example

```javascript
import EinsteinVisionAndEinsteinLanguage from 'einstein_vision_and_einstein_language';
let defaultClient = EinsteinVisionAndEinsteinLanguage.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_token
let bearer_token = defaultClient.authentications['bearer_token'];
bearer_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new EinsteinVisionAndEinsteinLanguage.LanguageTrainingApi();
let opts = {
  'algorithm': "algorithm_example", // String | Algorithm used for train
  'datasetId': 789, // Number | ID of the dataset to train.
  'epochs': 56, // Number | Number of training iterations for the neural network. Optional.
  'learningRate': 3.4, // Number | N/A for intent or sentiment models.
  'name': "name_example", // String | Name of the model. Maximum length is 180 characters.
  'trainParams': new EinsteinVisionAndEinsteinLanguage.V2LanguageTrainParams() // V2LanguageTrainParams | 
};
apiInstance.train(opts, (error, data, response) => {
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
 **algorithm** | **String**| Algorithm used for train | [optional] 
 **datasetId** | **Number**| ID of the dataset to train. | [optional] 
 **epochs** | **Number**| Number of training iterations for the neural network. Optional. | [optional] 
 **learningRate** | **Number**| N/A for intent or sentiment models. | [optional] 
 **name** | **String**| Name of the model. Maximum length is 180 characters. | [optional] 
 **trainParams** | [**V2LanguageTrainParams**](V2LanguageTrainParams.md)|  | [optional] 

### Return type

[**TrainResponse**](TrainResponse.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

