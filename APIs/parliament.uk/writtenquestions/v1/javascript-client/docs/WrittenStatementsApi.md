# WrittenQuestionsServiceApi.WrittenStatementsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiWrittenstatementsStatementsDateUinGet**](WrittenStatementsApi.md#apiWrittenstatementsStatementsDateUinGet) | **GET** /api/writtenstatements/statements/{date}/{uin} | Returns a written statemnet
[**apiWrittenstatementsStatementsGet**](WrittenStatementsApi.md#apiWrittenstatementsStatementsGet) | **GET** /api/writtenstatements/statements | Returns a list of written statements
[**apiWrittenstatementsStatementsIdGet**](WrittenStatementsApi.md#apiWrittenstatementsStatementsIdGet) | **GET** /api/writtenstatements/statements/{id} | Returns a written statement



## apiWrittenstatementsStatementsDateUinGet

> StatementsViewModelItem apiWrittenstatementsStatementsDateUinGet(date, uin, opts)

Returns a written statemnet

### Example

```javascript
import WrittenQuestionsServiceApi from 'written_questions_service_api';

let apiInstance = new WrittenQuestionsServiceApi.WrittenStatementsApi();
let date = new Date("2013-10-20T19:20:30+01:00"); // Date | Written statement on date specified
let uin = "uin_example"; // String | Written statement with uid specified
let opts = {
  'expandMember': true // Boolean | Expand the details of Members in the results
};
apiInstance.apiWrittenstatementsStatementsDateUinGet(date, uin, opts, (error, data, response) => {
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
 **date** | **Date**| Written statement on date specified | 
 **uin** | **String**| Written statement with uid specified | 
 **expandMember** | **Boolean**| Expand the details of Members in the results | [optional] 

### Return type

[**StatementsViewModelItem**](StatementsViewModelItem.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiWrittenstatementsStatementsGet

> StatementsViewModelSearchResult apiWrittenstatementsStatementsGet(opts)

Returns a list of written statements

### Example

```javascript
import WrittenQuestionsServiceApi from 'written_questions_service_api';

let apiInstance = new WrittenQuestionsServiceApi.WrittenStatementsApi();
let opts = {
  'madeWhenFrom': new Date("2013-10-20T19:20:30+01:00"), // Date | Written statements made on or after the date specified. Date format yyyy-mm-dd
  'madeWhenTo': new Date("2013-10-20T19:20:30+01:00"), // Date | Written statements made on or before the date specified. Date format yyyy-mm-dd
  'searchTerm': "searchTerm_example", // String | Written questions / statements containing the search term specified, searches item content
  'uIN': "uIN_example", // String | Written questions / statements with the uin specified
  'answeringBodies': [null], // [Number] | Written questions / statements relating to the answering bodies with the IDs specified
  'members': [null], // [Number] | Written questions / statements relating to the members with the IDs specified
  'house': new WrittenQuestionsServiceApi.HouseEnum(), // HouseEnum | Written questions / statements relating to the House specified
  'skip': 56, // Number | Number of records to skip, default is 0
  'take': 56, // Number | Number of records to take, default is 20
  'expandMember': true // Boolean | Expand the details of Members in the results
};
apiInstance.apiWrittenstatementsStatementsGet(opts, (error, data, response) => {
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
 **madeWhenFrom** | **Date**| Written statements made on or after the date specified. Date format yyyy-mm-dd | [optional] 
 **madeWhenTo** | **Date**| Written statements made on or before the date specified. Date format yyyy-mm-dd | [optional] 
 **searchTerm** | **String**| Written questions / statements containing the search term specified, searches item content | [optional] 
 **uIN** | **String**| Written questions / statements with the uin specified | [optional] 
 **answeringBodies** | [**[Number]**](Number.md)| Written questions / statements relating to the answering bodies with the IDs specified | [optional] 
 **members** | [**[Number]**](Number.md)| Written questions / statements relating to the members with the IDs specified | [optional] 
 **house** | [**HouseEnum**](.md)| Written questions / statements relating to the House specified | [optional] 
 **skip** | **Number**| Number of records to skip, default is 0 | [optional] 
 **take** | **Number**| Number of records to take, default is 20 | [optional] 
 **expandMember** | **Boolean**| Expand the details of Members in the results | [optional] 

### Return type

[**StatementsViewModelSearchResult**](StatementsViewModelSearchResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiWrittenstatementsStatementsIdGet

> StatementsViewModelSearchResult apiWrittenstatementsStatementsIdGet(id, opts)

Returns a written statement

### Example

```javascript
import WrittenQuestionsServiceApi from 'written_questions_service_api';

let apiInstance = new WrittenQuestionsServiceApi.WrittenStatementsApi();
let id = 56; // Number | Written statement with ID specified
let opts = {
  'expandMember': true // Boolean | Expand the details of Members in the results
};
apiInstance.apiWrittenstatementsStatementsIdGet(id, opts, (error, data, response) => {
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
 **id** | **Number**| Written statement with ID specified | 
 **expandMember** | **Boolean**| Expand the details of Members in the results | [optional] 

### Return type

[**StatementsViewModelSearchResult**](StatementsViewModelSearchResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

