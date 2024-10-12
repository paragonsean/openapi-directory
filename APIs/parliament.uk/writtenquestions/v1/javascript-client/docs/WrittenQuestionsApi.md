# WrittenQuestionsServiceApi.WrittenQuestionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiWrittenquestionsQuestionsDateUinGet**](WrittenQuestionsApi.md#apiWrittenquestionsQuestionsDateUinGet) | **GET** /api/writtenquestions/questions/{date}/{uin} | Returns a written question
[**apiWrittenquestionsQuestionsGet**](WrittenQuestionsApi.md#apiWrittenquestionsQuestionsGet) | **GET** /api/writtenquestions/questions | Returns a list of written questions
[**apiWrittenquestionsQuestionsIdGet**](WrittenQuestionsApi.md#apiWrittenquestionsQuestionsIdGet) | **GET** /api/writtenquestions/questions/{id} | Returns a written question



## apiWrittenquestionsQuestionsDateUinGet

> QuestionsViewModelItem apiWrittenquestionsQuestionsDateUinGet(date, uin, opts)

Returns a written question

### Example

```javascript
import WrittenQuestionsServiceApi from 'written_questions_service_api';

let apiInstance = new WrittenQuestionsServiceApi.WrittenQuestionsApi();
let date = new Date("2013-10-20T19:20:30+01:00"); // Date | Written question on date specified
let uin = "uin_example"; // String | Written question with uid specified
let opts = {
  'expandMember': true // Boolean | Expand the details of Members in the results
};
apiInstance.apiWrittenquestionsQuestionsDateUinGet(date, uin, opts, (error, data, response) => {
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
 **date** | **Date**| Written question on date specified | 
 **uin** | **String**| Written question with uid specified | 
 **expandMember** | **Boolean**| Expand the details of Members in the results | [optional] 

### Return type

[**QuestionsViewModelItem**](QuestionsViewModelItem.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiWrittenquestionsQuestionsGet

> QuestionsViewModelSearchResult apiWrittenquestionsQuestionsGet(opts)

Returns a list of written questions

### Example

```javascript
import WrittenQuestionsServiceApi from 'written_questions_service_api';

let apiInstance = new WrittenQuestionsServiceApi.WrittenQuestionsApi();
let opts = {
  'askingMemberId': 56, // Number | Written questions asked by member with member ID specified
  'answeringMemberId': 56, // Number | Written questions answered by member with member ID specified
  'tabledWhenFrom': new Date("2013-10-20T19:20:30+01:00"), // Date | Written questions tabled on or after the date specified. Date format yyyy-mm-dd
  'tabledWhenTo': new Date("2013-10-20T19:20:30+01:00"), // Date | Written questions tabled on or before the date specified. Date format yyyy-mm-dd
  'answered': new WrittenQuestionsServiceApi.Answered(), // Answered | Written questions that have been answered, unanswered or either.
  'answeredWhenFrom': new Date("2013-10-20T19:20:30+01:00"), // Date | Written questions answered on or after the date specified. Date format yyyy-mm-dd
  'answeredWhenTo': new Date("2013-10-20T19:20:30+01:00"), // Date | Written questions answered on or before the date specified. Date format yyyy-mm-dd
  'questionStatus': new WrittenQuestionsServiceApi.QuestionStatusEnum(), // QuestionStatusEnum | Written questions with the status specified
  'includeWithdrawn': true, // Boolean | Include written questions that have been withdrawn
  'expandMember': true, // Boolean | Expand the details of Members in the results
  'correctedWhenFrom': new Date("2013-10-20T19:20:30+01:00"), // Date | Written questions corrected on or after the date specified. Date format yyyy-mm-dd
  'correctedWhenTo': new Date("2013-10-20T19:20:30+01:00"), // Date | Written questions corrected on or before the date specified. Date format yyyy-mm-dd
  'searchTerm': "searchTerm_example", // String | Written questions / statements containing the search term specified, searches item content
  'uIN': "uIN_example", // String | Written questions / statements with the uin specified
  'answeringBodies': [null], // [Number] | Written questions / statements relating to the answering bodies with the IDs specified
  'members': [null], // [Number] | Written questions / statements relating to the members with the IDs specified
  'house': new WrittenQuestionsServiceApi.HouseEnum(), // HouseEnum | Written questions / statements relating to the House specified
  'skip': 56, // Number | Number of records to skip, default is 0
  'take': 56 // Number | Number of records to take, default is 20
};
apiInstance.apiWrittenquestionsQuestionsGet(opts, (error, data, response) => {
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
 **askingMemberId** | **Number**| Written questions asked by member with member ID specified | [optional] 
 **answeringMemberId** | **Number**| Written questions answered by member with member ID specified | [optional] 
 **tabledWhenFrom** | **Date**| Written questions tabled on or after the date specified. Date format yyyy-mm-dd | [optional] 
 **tabledWhenTo** | **Date**| Written questions tabled on or before the date specified. Date format yyyy-mm-dd | [optional] 
 **answered** | [**Answered**](.md)| Written questions that have been answered, unanswered or either. | [optional] 
 **answeredWhenFrom** | **Date**| Written questions answered on or after the date specified. Date format yyyy-mm-dd | [optional] 
 **answeredWhenTo** | **Date**| Written questions answered on or before the date specified. Date format yyyy-mm-dd | [optional] 
 **questionStatus** | [**QuestionStatusEnum**](.md)| Written questions with the status specified | [optional] 
 **includeWithdrawn** | **Boolean**| Include written questions that have been withdrawn | [optional] 
 **expandMember** | **Boolean**| Expand the details of Members in the results | [optional] 
 **correctedWhenFrom** | **Date**| Written questions corrected on or after the date specified. Date format yyyy-mm-dd | [optional] 
 **correctedWhenTo** | **Date**| Written questions corrected on or before the date specified. Date format yyyy-mm-dd | [optional] 
 **searchTerm** | **String**| Written questions / statements containing the search term specified, searches item content | [optional] 
 **uIN** | **String**| Written questions / statements with the uin specified | [optional] 
 **answeringBodies** | [**[Number]**](Number.md)| Written questions / statements relating to the answering bodies with the IDs specified | [optional] 
 **members** | [**[Number]**](Number.md)| Written questions / statements relating to the members with the IDs specified | [optional] 
 **house** | [**HouseEnum**](.md)| Written questions / statements relating to the House specified | [optional] 
 **skip** | **Number**| Number of records to skip, default is 0 | [optional] 
 **take** | **Number**| Number of records to take, default is 20 | [optional] 

### Return type

[**QuestionsViewModelSearchResult**](QuestionsViewModelSearchResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiWrittenquestionsQuestionsIdGet

> QuestionsViewModelItem apiWrittenquestionsQuestionsIdGet(id, opts)

Returns a written question

### Example

```javascript
import WrittenQuestionsServiceApi from 'written_questions_service_api';

let apiInstance = new WrittenQuestionsServiceApi.WrittenQuestionsApi();
let id = 56; // Number | written question with ID specified
let opts = {
  'expandMember': true // Boolean | Expand the details of Members in the result
};
apiInstance.apiWrittenquestionsQuestionsIdGet(id, opts, (error, data, response) => {
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
 **id** | **Number**| written question with ID specified | 
 **expandMember** | **Boolean**| Expand the details of Members in the result | [optional] 

### Return type

[**QuestionsViewModelItem**](QuestionsViewModelItem.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

