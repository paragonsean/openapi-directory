# HouseOfCommonsOralAndWrittenQuestionsApi.OralQuestionsApi

All URIs are relative to *http://oralquestionsandmotions-api.parliament.uk*

Method | HTTP request | Description
------------- | ------------- | -------------
[**publishedOralQuestionGet**](OralQuestionsApi.md#publishedOralQuestionGet) | **GET** /oralquestions/list | Returns a list of oral questions



## publishedOralQuestionGet

> ApiResponseListPublishedWrittenQuestion publishedOralQuestionGet(opts)

Returns a list of oral questions

A list of oral questions meeting the specified criteria.

### Example

```javascript
import HouseOfCommonsOralAndWrittenQuestionsApi from 'house_of_commons_oral_and_written_questions_api';

let apiInstance = new HouseOfCommonsOralAndWrittenQuestionsApi.OralQuestionsApi();
let opts = {
  'parametersAnsweringDateStart': new Date("2013-10-20T19:20:30+01:00"), // Date | Oral Questions where the answering date has been set on or after the date provided. Date format YYYY-MM-DD.
  'parametersAnsweringDateEnd': new Date("2013-10-20T19:20:30+01:00"), // Date | Oral Questions where the answering date has been set on or before the date provided. Date format YYYY-MM-DD.
  'parametersQuestionType': "parametersQuestionType_example", // String | Oral Questions where the question type is the selected type, substantive or topical.
  'parametersOralQuestionTimeId': 56, // Number | Oral Questions where the question is within the question time with the ID provided
  'parametersAskingMemberIds': [null], // [Number] | The ID of the member asking the question. Lists of member IDs for each house are available <a href=\"http://data.parliament.uk/membersdataplatform/services/mnis/members/query/house=Commons\" target=\"_blank\">Commons</a> and <a href=\"http://data.parliament.uk/membersdataplatform/services/mnis/members/query/house=Lords\" target=\"_blank\">Lords</a>.
  'parametersUINs': [null], // [Number] | The UIN for the question - note that UINs reset at the start of each Parliamentary session.
  'parametersAnsweringBodyIds': [null], // [Number] | Which answering body is to respond. A list of answering bodies can be found <a target=\"_blank\" href=\"http://data.parliament.uk/membersdataplatform/services/mnis/referencedata/AnsweringBodies/\">here</a>.
  'parametersSkip': 56, // Number | The number of records to skip from the first, default is 0.
  'parametersTake': 56 // Number | The number of records to return, default is 25, maximum is 100.
};
apiInstance.publishedOralQuestionGet(opts, (error, data, response) => {
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
 **parametersAnsweringDateStart** | **Date**| Oral Questions where the answering date has been set on or after the date provided. Date format YYYY-MM-DD. | [optional] 
 **parametersAnsweringDateEnd** | **Date**| Oral Questions where the answering date has been set on or before the date provided. Date format YYYY-MM-DD. | [optional] 
 **parametersQuestionType** | **String**| Oral Questions where the question type is the selected type, substantive or topical. | [optional] 
 **parametersOralQuestionTimeId** | **Number**| Oral Questions where the question is within the question time with the ID provided | [optional] 
 **parametersAskingMemberIds** | [**[Number]**](Number.md)| The ID of the member asking the question. Lists of member IDs for each house are available &lt;a href&#x3D;\&quot;http://data.parliament.uk/membersdataplatform/services/mnis/members/query/house&#x3D;Commons\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Commons&lt;/a&gt; and &lt;a href&#x3D;\&quot;http://data.parliament.uk/membersdataplatform/services/mnis/members/query/house&#x3D;Lords\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Lords&lt;/a&gt;. | [optional] 
 **parametersUINs** | [**[Number]**](Number.md)| The UIN for the question - note that UINs reset at the start of each Parliamentary session. | [optional] 
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

