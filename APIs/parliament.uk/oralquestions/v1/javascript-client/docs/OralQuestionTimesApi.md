# HouseOfCommonsOralAndWrittenQuestionsApi.OralQuestionTimesApi

All URIs are relative to *http://oralquestionsandmotions-api.parliament.uk*

Method | HTTP request | Description
------------- | ------------- | -------------
[**publishedOralQuestionTimeGet**](OralQuestionTimesApi.md#publishedOralQuestionTimeGet) | **GET** /oralquestiontimes/list | Returns a list of oral question times



## publishedOralQuestionTimeGet

> ApiResponseListPublishedWrittenQuestion publishedOralQuestionTimeGet(opts)

Returns a list of oral question times

A list of oral question times meeting the specified criteria.

### Example

```javascript
import HouseOfCommonsOralAndWrittenQuestionsApi from 'house_of_commons_oral_and_written_questions_api';

let apiInstance = new HouseOfCommonsOralAndWrittenQuestionsApi.OralQuestionTimesApi();
let opts = {
  'parametersAnsweringDateStart': new Date("2013-10-20T19:20:30+01:00"), // Date | Oral Questions Time where the answering date has been set on or after the date provided. Date format YYYY-MM-DD.
  'parametersAnsweringDateEnd': new Date("2013-10-20T19:20:30+01:00"), // Date | Oral Questions Time where the answering date has been set on or before the date provided. Date format YYYY-MM-DD.
  'parametersDeadlineDateStart': new Date("2013-10-20T19:20:30+01:00"), // Date | Oral Questions Time where the deadline date has been set on or after the date provided. Date format YYYY-MM-DD.
  'parametersDeadlineDateEnd': new Date("2013-10-20T19:20:30+01:00"), // Date | Oral Questions Time where the deadline date has been set on or before the date provided. Date format YYYY-MM-DD.
  'parametersOralQuestionTimeId': 56, // Number | Identifier of the OQT
  'parametersAnsweringBodyIds': [null], // [Number] | Which answering body is to respond. A list of answering bodies can be found <a target=\"_blank\" href=\"http://data.parliament.uk/membersdataplatform/services/mnis/referencedata/AnsweringBodies/\">here</a>.
  'parametersSkip': 56, // Number | The number of records to skip from the first, default is 0.
  'parametersTake': 56 // Number | The number of records to return, default is 25, maximum is 100.
};
apiInstance.publishedOralQuestionTimeGet(opts, (error, data, response) => {
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
 **parametersAnsweringDateStart** | **Date**| Oral Questions Time where the answering date has been set on or after the date provided. Date format YYYY-MM-DD. | [optional] 
 **parametersAnsweringDateEnd** | **Date**| Oral Questions Time where the answering date has been set on or before the date provided. Date format YYYY-MM-DD. | [optional] 
 **parametersDeadlineDateStart** | **Date**| Oral Questions Time where the deadline date has been set on or after the date provided. Date format YYYY-MM-DD. | [optional] 
 **parametersDeadlineDateEnd** | **Date**| Oral Questions Time where the deadline date has been set on or before the date provided. Date format YYYY-MM-DD. | [optional] 
 **parametersOralQuestionTimeId** | **Number**| Identifier of the OQT | [optional] 
 **parametersAnsweringBodyIds** | [**[Number]**](Number.md)| Which answering body is to respond. A list of answering bodies can be found &lt;a target&#x3D;\&quot;_blank\&quot; href&#x3D;\&quot;http://data.parliament.uk/membersdataplatform/services/mnis/referencedata/AnsweringBodies/\&quot;&gt;here&lt;/a&gt;. | [optional] 
 **parametersSkip** | **Number**| The number of records to skip from the first, default is 0. | [optional] 
 **parametersTake** | **Number**| The number of records to return, default is 25, maximum is 100. | [optional] 

### Return type

[**ApiResponseListPublishedWrittenQuestion**](ApiResponseListPublishedWrittenQuestion.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml

