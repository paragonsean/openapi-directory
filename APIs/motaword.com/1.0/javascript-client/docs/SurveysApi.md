# MotaWordApi.SurveysApi

All URIs are relative to *https://api.motaword.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getQuestions**](SurveysApi.md#getQuestions) | **GET** /surveys/{scope}/{type} | Get survey questions in given scope and type
[**submitAnswers**](SurveysApi.md#submitAnswers) | **POST** /surveys/{scope}/{type} | Post survey answers for scope and type



## getQuestions

> [SurveyQuestion] getQuestions(scope, type, opts)

Get survey questions in given scope and type

Get survey questions in given scope and type

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.SurveysApi();
let scope = "vendor"; // String | Scope
let type = "profile"; // String | Type
let opts = {
  'attachAnswersForProject': 74 // Number | Project ID
};
apiInstance.getQuestions(scope, type, opts, (error, data, response) => {
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
 **scope** | **String**| Scope | 
 **type** | **String**| Type | 
 **attachAnswersForProject** | **Number**| Project ID | [optional] 

### Return type

[**[SurveyQuestion]**](SurveyQuestion.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## submitAnswers

> OperationStatus submitAnswers(scope, type, opts)

Post survey answers for scope and type

Post survey answers for scope and type

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.SurveysApi();
let scope = "vendor"; // String | Scope
let type = "profile"; // String | Type
let opts = {
  'surveyAnswers': new MotaWordApi.SurveyAnswers() // SurveyAnswers | 
};
apiInstance.submitAnswers(scope, type, opts, (error, data, response) => {
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
 **scope** | **String**| Scope | 
 **type** | **String**| Type | 
 **surveyAnswers** | [**SurveyAnswers**](SurveyAnswers.md)|  | [optional] 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

