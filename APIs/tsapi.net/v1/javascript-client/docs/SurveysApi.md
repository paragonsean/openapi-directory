# Tsapi.SurveysApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**surveysGet**](SurveysApi.md#surveysGet) | **GET** /Surveys | Returns a list of available Surveys
[**surveysSurveyIdInterviewsGet**](SurveysApi.md#surveysSurveyIdInterviewsGet) | **GET** /Surveys/{surveyId}/Interviews | Fetches some interview records for a specific survey
[**surveysSurveyIdMetadataGet**](SurveysApi.md#surveysSurveyIdMetadataGet) | **GET** /Surveys/{surveyId}/Metadata | Fetches the metadata for a specific survey



## surveysGet

> [SurveyDetail] surveysGet()

Returns a list of available Surveys

### Example

```javascript
import Tsapi from 'tsapi';
let defaultClient = Tsapi.ApiClient.instance;
// Configure API key authorization: basic
let basic = defaultClient.authentications['basic'];
basic.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//basic.apiKeyPrefix = 'Token';

let apiInstance = new Tsapi.SurveysApi();
apiInstance.surveysGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[SurveyDetail]**](SurveyDetail.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## surveysSurveyIdInterviewsGet

> [Interview] surveysSurveyIdInterviewsGet(surveyId, opts)

Fetches some interview records for a specific survey

### Example

```javascript
import Tsapi from 'tsapi';
let defaultClient = Tsapi.ApiClient.instance;
// Configure API key authorization: basic
let basic = defaultClient.authentications['basic'];
basic.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//basic.apiKeyPrefix = 'Token';

let apiInstance = new Tsapi.SurveysApi();
let surveyId = "surveyId_example"; // String | 
let opts = {
  'start': 56, // Number | 
  'maxLength': 56 // Number | 
};
apiInstance.surveysSurveyIdInterviewsGet(surveyId, opts, (error, data, response) => {
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
 **surveyId** | **String**|  | 
 **start** | **Number**|  | [optional] 
 **maxLength** | **Number**|  | [optional] 

### Return type

[**[Interview]**](Interview.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## surveysSurveyIdMetadataGet

> SurveyMetadata surveysSurveyIdMetadataGet(surveyId)

Fetches the metadata for a specific survey

### Example

```javascript
import Tsapi from 'tsapi';
let defaultClient = Tsapi.ApiClient.instance;
// Configure API key authorization: basic
let basic = defaultClient.authentications['basic'];
basic.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//basic.apiKeyPrefix = 'Token';

let apiInstance = new Tsapi.SurveysApi();
let surveyId = "surveyId_example"; // String | 
apiInstance.surveysSurveyIdMetadataGet(surveyId, (error, data, response) => {
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
 **surveyId** | **String**|  | 

### Return type

[**SurveyMetadata**](SurveyMetadata.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

