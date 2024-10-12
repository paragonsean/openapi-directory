# FitbitPlusApi.RewardEarningApi

All URIs are relative to *https://api.twinehealth.com/pub*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createRewardEarning**](RewardEarningApi.md#createRewardEarning) | **POST** /reward_earning | Create a reward earning
[**fetchRewardEarning**](RewardEarningApi.md#fetchRewardEarning) | **GET** /reward_earning/{id} | Get a reward earning
[**fetchRewardEarnings**](RewardEarningApi.md#fetchRewardEarnings) | **GET** /reward_earning | List reward earnings



## createRewardEarning

> CreateRewardEarningResponse createRewardEarning(createRewardEarningRequest)

Create a reward earning

Create a reward earning for a reward. There can only be one earning for a reward. It is possilble to create multiple reward earnings simultaneously by providing and array of reward earnings in the data property.

### Example

```javascript
import FitbitPlusApi from 'fitbit_plus_api';

let apiInstance = new FitbitPlusApi.RewardEarningApi();
let createRewardEarningRequest = new FitbitPlusApi.CreateRewardEarningRequest(); // CreateRewardEarningRequest | 
apiInstance.createRewardEarning(createRewardEarningRequest, (error, data, response) => {
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
 **createRewardEarningRequest** | [**CreateRewardEarningRequest**](CreateRewardEarningRequest.md)|  | 

### Return type

[**CreateRewardEarningResponse**](CreateRewardEarningResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/vnd.api+json
- **Accept**: application/vnd.api+json


## fetchRewardEarning

> FetchRewardEarningResponse fetchRewardEarning(id)

Get a reward earning

Get a reward earning record by id.

### Example

```javascript
import FitbitPlusApi from 'fitbit_plus_api';

let apiInstance = new FitbitPlusApi.RewardEarningApi();
let id = "id_example"; // String | Reward earning identifier
apiInstance.fetchRewardEarning(id, (error, data, response) => {
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
 **id** | **String**| Reward earning identifier | 

### Return type

[**FetchRewardEarningResponse**](FetchRewardEarningResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.api+json


## fetchRewardEarnings

> FetchRewardEarningsResponse fetchRewardEarnings(filterGroups, filterPatient, opts)

List reward earnings

Get a list of reward earnings matching the specified filters.

### Example

```javascript
import FitbitPlusApi from 'fitbit_plus_api';

let apiInstance = new FitbitPlusApi.RewardEarningApi();
let filterGroups = "filterGroups_example"; // String | Group identifiers
let filterPatient = "filterPatient_example"; // String | Patient identifier
let opts = {
  'filterReadyForFulfillment': true // Boolean | If true, only returns those reward earnings for which ready_for_fulfillment is true and fulfilled_at is null. If false, only returns those reward earnings for which ready_for_fulfillment is false and fulfilled_at is null.
};
apiInstance.fetchRewardEarnings(filterGroups, filterPatient, opts, (error, data, response) => {
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
 **filterGroups** | **String**| Group identifiers | 
 **filterPatient** | **String**| Patient identifier | 
 **filterReadyForFulfillment** | **Boolean**| If true, only returns those reward earnings for which ready_for_fulfillment is true and fulfilled_at is null. If false, only returns those reward earnings for which ready_for_fulfillment is false and fulfilled_at is null. | [optional] 

### Return type

[**FetchRewardEarningsResponse**](FetchRewardEarningsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.api+json

