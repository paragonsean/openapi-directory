# FitbitPlusApi.HealthProfileQuestionApi

All URIs are relative to *https://api.twinehealth.com/pub*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchHealthProfileQuestion**](HealthProfileQuestionApi.md#fetchHealthProfileQuestion) | **GET** /health_profile_question/{id} | Get a health profile question
[**fetchHealthProfileQuestions**](HealthProfileQuestionApi.md#fetchHealthProfileQuestions) | **GET** /health_profile_question | List health profile questions



## fetchHealthProfileQuestion

> FetchHealthProfileQuestionResponse fetchHealthProfileQuestion(id, opts)

Get a health profile question

Get a health profile by id

### Example

```javascript
import FitbitPlusApi from 'fitbit_plus_api';

let apiInstance = new FitbitPlusApi.HealthProfileQuestionApi();
let id = "id_example"; // String | Health profile question identifier
let opts = {
  'include': "include_example" // String | List of related resources to include in the response
};
apiInstance.fetchHealthProfileQuestion(id, opts, (error, data, response) => {
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
 **id** | **String**| Health profile question identifier | 
 **include** | **String**| List of related resources to include in the response | [optional] 

### Return type

[**FetchHealthProfileQuestionResponse**](FetchHealthProfileQuestionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.api+json


## fetchHealthProfileQuestions

> FetchHealthProfileQuestionsResponse fetchHealthProfileQuestions(opts)

List health profile questions

Get a list of health profile questions

### Example

```javascript
import FitbitPlusApi from 'fitbit_plus_api';

let apiInstance = new FitbitPlusApi.HealthProfileQuestionApi();
let opts = {
  'filterPatient': "filterPatient_example", // String | Patient id to fetch healt profile questions. Note that one of the following filters must be specified: `filter[patient]`, `filter[group]`, or `filter[organization]`. 
  'filterGroups': "filterGroups_example", // String | Comma-separated list of group ids. Note that one of the following filters must be specified: `filter[patient]`, `filter[group]`, or `filter[organization]`. 
  'filterOrganization': "filterOrganization_example", // String | Fitbit Plus organization id. Note that one of the following filters must be specified: `filter[patient]`, `filter[group]`, or `filter[organization]`. 
  'include': "include_example" // String | List of related resources to include in the response
};
apiInstance.fetchHealthProfileQuestions(opts, (error, data, response) => {
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
 **filterPatient** | **String**| Patient id to fetch healt profile questions. Note that one of the following filters must be specified: &#x60;filter[patient]&#x60;, &#x60;filter[group]&#x60;, or &#x60;filter[organization]&#x60;.  | [optional] 
 **filterGroups** | **String**| Comma-separated list of group ids. Note that one of the following filters must be specified: &#x60;filter[patient]&#x60;, &#x60;filter[group]&#x60;, or &#x60;filter[organization]&#x60;.  | [optional] 
 **filterOrganization** | **String**| Fitbit Plus organization id. Note that one of the following filters must be specified: &#x60;filter[patient]&#x60;, &#x60;filter[group]&#x60;, or &#x60;filter[organization]&#x60;.  | [optional] 
 **include** | **String**| List of related resources to include in the response | [optional] 

### Return type

[**FetchHealthProfileQuestionsResponse**](FetchHealthProfileQuestionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.api+json

