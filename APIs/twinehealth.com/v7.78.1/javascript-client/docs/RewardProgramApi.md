# FitbitPlusApi.RewardProgramApi

All URIs are relative to *https://api.twinehealth.com/pub*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createRewardProgram**](RewardProgramApi.md#createRewardProgram) | **POST** /reward_program | Create a reward program
[**fetchRewardProgram**](RewardProgramApi.md#fetchRewardProgram) | **GET** /reward_program/{id} | Get a reward program
[**fetchRewardProgramGroup**](RewardProgramApi.md#fetchRewardProgramGroup) | **GET** /reward_program/{id}/group | Get group for a reward program
[**fetchRewardPrograms**](RewardProgramApi.md#fetchRewardPrograms) | **GET** /reward_program | List reward programs



## createRewardProgram

> CreateRewardProgramResponse createRewardProgram(createRewardProgramRequest)

Create a reward program

Create a reward program for a group.

### Example

```javascript
import FitbitPlusApi from 'fitbit_plus_api';

let apiInstance = new FitbitPlusApi.RewardProgramApi();
let createRewardProgramRequest = new FitbitPlusApi.CreateRewardProgramRequest(); // CreateRewardProgramRequest | 
apiInstance.createRewardProgram(createRewardProgramRequest, (error, data, response) => {
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
 **createRewardProgramRequest** | [**CreateRewardProgramRequest**](CreateRewardProgramRequest.md)|  | 

### Return type

[**CreateRewardProgramResponse**](CreateRewardProgramResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/vnd.api+json
- **Accept**: application/vnd.api+json


## fetchRewardProgram

> FetchRewardProgramResponse fetchRewardProgram(id)

Get a reward program

Get a reward program record by id.

### Example

```javascript
import FitbitPlusApi from 'fitbit_plus_api';

let apiInstance = new FitbitPlusApi.RewardProgramApi();
let id = "id_example"; // String | Reward program identifier
apiInstance.fetchRewardProgram(id, (error, data, response) => {
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
 **id** | **String**| Reward program identifier | 

### Return type

[**FetchRewardProgramResponse**](FetchRewardProgramResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.api+json


## fetchRewardProgramGroup

> FetchGroupsResponse fetchRewardProgramGroup(id)

Get group for a reward program

Get the group related to a reward program.

### Example

```javascript
import FitbitPlusApi from 'fitbit_plus_api';

let apiInstance = new FitbitPlusApi.RewardProgramApi();
let id = "id_example"; // String | Reward program identifier
apiInstance.fetchRewardProgramGroup(id, (error, data, response) => {
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
 **id** | **String**| Reward program identifier | 

### Return type

[**FetchGroupsResponse**](FetchGroupsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.api+json


## fetchRewardPrograms

> FetchRewardProgramsResponse fetchRewardPrograms(opts)

List reward programs

Get a list of reward programs matching the specified filters.

### Example

```javascript
import FitbitPlusApi from 'fitbit_plus_api';

let apiInstance = new FitbitPlusApi.RewardProgramApi();
let opts = {
  'filterGroups': "filterGroups_example", // String | Comma-separated list of group identifiers. Note that one of the following filters must be specified: `filter[groups]`, `filter[organization]`. 
  'filterOrganization': "filterOrganization_example" // String | Fitbit Plus organization id. Note that one of the following filters must be specified: `filter[groups]`, `filter[organization]`. 
};
apiInstance.fetchRewardPrograms(opts, (error, data, response) => {
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
 **filterGroups** | **String**| Comma-separated list of group identifiers. Note that one of the following filters must be specified: &#x60;filter[groups]&#x60;, &#x60;filter[organization]&#x60;.  | [optional] 
 **filterOrganization** | **String**| Fitbit Plus organization id. Note that one of the following filters must be specified: &#x60;filter[groups]&#x60;, &#x60;filter[organization]&#x60;.  | [optional] 

### Return type

[**FetchRewardProgramsResponse**](FetchRewardProgramsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.api+json

