# FitbitPlusApi.RewardApi

All URIs are relative to *https://api.twinehealth.com/pub*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createReward**](RewardApi.md#createReward) | **POST** /reward | Create a reward
[**fetchReward**](RewardApi.md#fetchReward) | **GET** /reward/{id} | Get a reward
[**fetchRewards**](RewardApi.md#fetchRewards) | **GET** /reward | List rewards



## createReward

> CreateRewardResponse createReward(createRewardRequest)

Create a reward

Create a reward for a patient.

### Example

```javascript
import FitbitPlusApi from 'fitbit_plus_api';

let apiInstance = new FitbitPlusApi.RewardApi();
let createRewardRequest = new FitbitPlusApi.CreateRewardRequest(); // CreateRewardRequest | 
apiInstance.createReward(createRewardRequest, (error, data, response) => {
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
 **createRewardRequest** | [**CreateRewardRequest**](CreateRewardRequest.md)|  | 

### Return type

[**CreateRewardResponse**](CreateRewardResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/vnd.api+json
- **Accept**: application/vnd.api+json


## fetchReward

> FetchRewardResponse fetchReward(id)

Get a reward

Get a reward record by id.

### Example

```javascript
import FitbitPlusApi from 'fitbit_plus_api';

let apiInstance = new FitbitPlusApi.RewardApi();
let id = "id_example"; // String | Reward identifier
apiInstance.fetchReward(id, (error, data, response) => {
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
 **id** | **String**| Reward identifier | 

### Return type

[**FetchRewardResponse**](FetchRewardResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.api+json


## fetchRewards

> FetchRewardsResponse fetchRewards(opts)

List rewards

Get a list of rewards matching the specified filters.

### Example

```javascript
import FitbitPlusApi from 'fitbit_plus_api';

let apiInstance = new FitbitPlusApi.RewardApi();
let opts = {
  'filterPatient': "filterPatient_example", // String | Patient identifier. Note that one of the following filters must be specified: `filter[patient]`, `filter[groups]`, `filter[organization]`. 
  'filterRewardProgramActivation': "filterRewardProgramActivation_example", // String | Reward program activation identifier
  'filterThread': "filterThread_example", // String | Thread identifier
  'filterGroups': "filterGroups_example", // String | Comma-separated list of group ids. Note that one of the following filters must be specified: `filter[patient]`, `filter[groups]`, `filter[organization]`. 
  'filterOrganization': "filterOrganization_example" // String | Fitbit Plus organization id. Note that one of the following filters must be specified: `filter[patient]`, `filter[groups]`, `filter[organization]`. 
};
apiInstance.fetchRewards(opts, (error, data, response) => {
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
 **filterRewardProgramActivation** | **String**| Reward program activation identifier | [optional] 
 **filterThread** | **String**| Thread identifier | [optional] 
 **filterGroups** | **String**| Comma-separated list of group ids. Note that one of the following filters must be specified: &#x60;filter[patient]&#x60;, &#x60;filter[groups]&#x60;, &#x60;filter[organization]&#x60;.  | [optional] 
 **filterOrganization** | **String**| Fitbit Plus organization id. Note that one of the following filters must be specified: &#x60;filter[patient]&#x60;, &#x60;filter[groups]&#x60;, &#x60;filter[organization]&#x60;.  | [optional] 

### Return type

[**FetchRewardsResponse**](FetchRewardsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.api+json

