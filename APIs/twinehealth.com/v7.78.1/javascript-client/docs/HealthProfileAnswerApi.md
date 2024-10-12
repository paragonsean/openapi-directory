# FitbitPlusApi.HealthProfileAnswerApi

All URIs are relative to *https://api.twinehealth.com/pub*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchHealthProfileAnswer**](HealthProfileAnswerApi.md#fetchHealthProfileAnswer) | **GET** /health_profile_answer/{id} | Get a health profile answer
[**fetchHealthProfileAnswers**](HealthProfileAnswerApi.md#fetchHealthProfileAnswers) | **GET** /health_profile_answer | List health profile answers



## fetchHealthProfileAnswer

> FetchHealthProfileAnswerResponse fetchHealthProfileAnswer(id, opts)

Get a health profile answer

Get a health profile answer by id

### Example

```javascript
import FitbitPlusApi from 'fitbit_plus_api';

let apiInstance = new FitbitPlusApi.HealthProfileAnswerApi();
let id = "id_example"; // String | Health profile answer identifier
let opts = {
  'include': "include_example" // String | List of related resources to include in the response
};
apiInstance.fetchHealthProfileAnswer(id, opts, (error, data, response) => {
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
 **id** | **String**| Health profile answer identifier | 
 **include** | **String**| List of related resources to include in the response | [optional] 

### Return type

[**FetchHealthProfileAnswerResponse**](FetchHealthProfileAnswerResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.api+json


## fetchHealthProfileAnswers

> FetchHealthProfileAnswersResponse fetchHealthProfileAnswers(opts)

List health profile answers

Get a list of health profile answers

### Example

```javascript
import FitbitPlusApi from 'fitbit_plus_api';

let apiInstance = new FitbitPlusApi.HealthProfileAnswerApi();
let opts = {
  'filterPatient': "filterPatient_example", // String | Patient id to fetch healt profile answers. Note that one of the following filters must be specified: `filter[patient]`, `filter[group]`, or `filter[organization]`. 
  'filterGroups': "filterGroups_example", // String | Comma-separated list of group ids. Note that one of the following filters must be specified: `filter[patient]`, `filter[group]`, or `filter[organization]`. 
  'filterOrganization': "filterOrganization_example", // String | Fitbit Plus organization id. Note that one of the following filters must be specified: `filter[patient]`, `filter[group]`, or `filter[organization]`. 
  'pageNumber': 1, // Number | Page number
  'pageSize': 50, // Number | Page size
  'pageLimit': 50, // Number | Page limit
  'pageCursor': "pageCursor_example", // String | Page cursor
  'include': "include_example" // String | List of related resources to include in the response
};
apiInstance.fetchHealthProfileAnswers(opts, (error, data, response) => {
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
 **filterPatient** | **String**| Patient id to fetch healt profile answers. Note that one of the following filters must be specified: &#x60;filter[patient]&#x60;, &#x60;filter[group]&#x60;, or &#x60;filter[organization]&#x60;.  | [optional] 
 **filterGroups** | **String**| Comma-separated list of group ids. Note that one of the following filters must be specified: &#x60;filter[patient]&#x60;, &#x60;filter[group]&#x60;, or &#x60;filter[organization]&#x60;.  | [optional] 
 **filterOrganization** | **String**| Fitbit Plus organization id. Note that one of the following filters must be specified: &#x60;filter[patient]&#x60;, &#x60;filter[group]&#x60;, or &#x60;filter[organization]&#x60;.  | [optional] 
 **pageNumber** | **Number**| Page number | [optional] [default to 1]
 **pageSize** | **Number**| Page size | [optional] [default to 50]
 **pageLimit** | **Number**| Page limit | [optional] [default to 50]
 **pageCursor** | **String**| Page cursor | [optional] 
 **include** | **String**| List of related resources to include in the response | [optional] 

### Return type

[**FetchHealthProfileAnswersResponse**](FetchHealthProfileAnswersResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.api+json

