# FitbitPlusApi.RewardProgramActivationApi

All URIs are relative to *https://api.twinehealth.com/pub*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createRewardProgramActivation**](RewardProgramActivationApi.md#createRewardProgramActivation) | **POST** /reward_program_activation | Create a reward program activation
[**fetchRewardProgramActivation**](RewardProgramActivationApi.md#fetchRewardProgramActivation) | **GET** /reward_program_activation/{id} | Get a reward program activation
[**fetchRewardProgramActivations**](RewardProgramActivationApi.md#fetchRewardProgramActivations) | **GET** /reward_program_activation | List reward program activations



## createRewardProgramActivation

> CreateRewardProgramActivationResponse createRewardProgramActivation(createRewardProgramActivationRequest)

Create a reward program activation

Create a reward program activation for a patient. There can only be one activation for a patient for a given reward program.

### Example

```javascript
import FitbitPlusApi from 'fitbit_plus_api';

let apiInstance = new FitbitPlusApi.RewardProgramActivationApi();
let createRewardProgramActivationRequest = new FitbitPlusApi.CreateRewardProgramActivationRequest(); // CreateRewardProgramActivationRequest | 
apiInstance.createRewardProgramActivation(createRewardProgramActivationRequest, (error, data, response) => {
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
 **createRewardProgramActivationRequest** | [**CreateRewardProgramActivationRequest**](CreateRewardProgramActivationRequest.md)|  | 

### Return type

[**CreateRewardProgramActivationResponse**](CreateRewardProgramActivationResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/vnd.api+json
- **Accept**: application/vnd.api+json


## fetchRewardProgramActivation

> FetchRewardProgramActivationResponse fetchRewardProgramActivation(id)

Get a reward program activation

Get a reward program activationrecord by id.

### Example

```javascript
import FitbitPlusApi from 'fitbit_plus_api';

let apiInstance = new FitbitPlusApi.RewardProgramActivationApi();
let id = "id_example"; // String | Reward program activation identifier
apiInstance.fetchRewardProgramActivation(id, (error, data, response) => {
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
 **id** | **String**| Reward program activation identifier | 

### Return type

[**FetchRewardProgramActivationResponse**](FetchRewardProgramActivationResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.api+json


## fetchRewardProgramActivations

> FetchRewardProgramActivationsResponse fetchRewardProgramActivations(opts)

List reward program activations

Get a list of reward program activations matching the specified filters.

### Example

```javascript
import FitbitPlusApi from 'fitbit_plus_api';

let apiInstance = new FitbitPlusApi.RewardProgramActivationApi();
let opts = {
  'filterPatient': "filterPatient_example", // String | Patient identifier. Note that one of the following filters must be specified: `filter[patient]`, `filter[groups]`, `filter[organization]`. 
  'filterGroups': "filterGroups_example", // String | Comma-separated list of group ids. Note that one of the following filters must be specified: `filter[patient]`, `filter[groups]`, `filter[organization]`. 
  'filterOrganization': "filterOrganization_example" // String | Fitbit Plus organization id. Note that one of the following filters must be specified: `filter[patient]`, `filter[groups]`, `filter[organization]`. 
};
apiInstance.fetchRewardProgramActivations(opts, (error, data, response) => {
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
 **filterPatient** | **String**| Patient identifier. Note that one of the following filters must be specified: &#x60;filter[patient]&#x60;, &#x60;filter[groups]&#x60;, &#x60;filter[organization]&#x60;.  | [optional] 
 **filterGroups** | **String**| Comma-separated list of group ids. Note that one of the following filters must be specified: &#x60;filter[patient]&#x60;, &#x60;filter[groups]&#x60;, &#x60;filter[organization]&#x60;.  | [optional] 
 **filterOrganization** | **String**| Fitbit Plus organization id. Note that one of the following filters must be specified: &#x60;filter[patient]&#x60;, &#x60;filter[groups]&#x60;, &#x60;filter[organization]&#x60;.  | [optional] 

### Return type

[**FetchRewardProgramActivationsResponse**](FetchRewardProgramActivationsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.api+json

