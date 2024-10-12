# FitbitPlusApi.RewardEarningFulfillmentApi

All URIs are relative to *https://api.twinehealth.com/pub*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createRewardEarningFulfillment**](RewardEarningFulfillmentApi.md#createRewardEarningFulfillment) | **POST** /reward_earning_fulfillment | Create a reward earning fulfillment
[**fetchRewardEarningFulfillment**](RewardEarningFulfillmentApi.md#fetchRewardEarningFulfillment) | **GET** /reward_earning_fulfillment/{id} | Get a reward earning fulfillment
[**fetchRewardEarningFulfillments**](RewardEarningFulfillmentApi.md#fetchRewardEarningFulfillments) | **GET** /reward_earning_fulfillment | List reward earning fulfillments



## createRewardEarningFulfillment

> CreateRewardEarningFulfillmentResponse createRewardEarningFulfillment(createRewardEarningFulfillmentRequest)

Create a reward earning fulfillment

Create a reward earning fulfillment for a reward earning. There can only be one fulfillment for each earning.

### Example

```javascript
import FitbitPlusApi from 'fitbit_plus_api';

let apiInstance = new FitbitPlusApi.RewardEarningFulfillmentApi();
let createRewardEarningFulfillmentRequest = new FitbitPlusApi.CreateRewardEarningFulfillmentRequest(); // CreateRewardEarningFulfillmentRequest | 
apiInstance.createRewardEarningFulfillment(createRewardEarningFulfillmentRequest, (error, data, response) => {
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
 **createRewardEarningFulfillmentRequest** | [**CreateRewardEarningFulfillmentRequest**](CreateRewardEarningFulfillmentRequest.md)|  | 

### Return type

[**CreateRewardEarningFulfillmentResponse**](CreateRewardEarningFulfillmentResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/vnd.api+json
- **Accept**: application/vnd.api+json


## fetchRewardEarningFulfillment

> FetchRewardEarningFulfillmentResponse fetchRewardEarningFulfillment(id)

Get a reward earning fulfillment

Get a reward earning fulfillment record by id.

### Example

```javascript
import FitbitPlusApi from 'fitbit_plus_api';

let apiInstance = new FitbitPlusApi.RewardEarningFulfillmentApi();
let id = "id_example"; // String | Reward earning fulfillment identifier
apiInstance.fetchRewardEarningFulfillment(id, (error, data, response) => {
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
 **id** | **String**| Reward earning fulfillment identifier | 

### Return type

[**FetchRewardEarningFulfillmentResponse**](FetchRewardEarningFulfillmentResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.api+json


## fetchRewardEarningFulfillments

> FetchRewardEarningFulfillmentsResponse fetchRewardEarningFulfillments(filterPatient)

List reward earning fulfillments

Get a list of reward earning fulfillments matching the specified filters.

### Example

```javascript
import FitbitPlusApi from 'fitbit_plus_api';

let apiInstance = new FitbitPlusApi.RewardEarningFulfillmentApi();
let filterPatient = "filterPatient_example"; // String | Patient identifier
apiInstance.fetchRewardEarningFulfillments(filterPatient, (error, data, response) => {
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
 **filterPatient** | **String**| Patient identifier | 

### Return type

[**FetchRewardEarningFulfillmentsResponse**](FetchRewardEarningFulfillmentsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.api+json

