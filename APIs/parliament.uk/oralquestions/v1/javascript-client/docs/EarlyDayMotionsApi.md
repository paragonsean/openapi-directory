# HouseOfCommonsOralAndWrittenQuestionsApi.EarlyDayMotionsApi

All URIs are relative to *http://oralquestionsandmotions-api.parliament.uk*

Method | HTTP request | Description
------------- | ------------- | -------------
[**earlyDayMotionsListGet**](EarlyDayMotionsApi.md#earlyDayMotionsListGet) | **GET** /EarlyDayMotions/list | Returns a list of Early Day Motions
[**publishedEarlyDayMotionGet**](EarlyDayMotionsApi.md#publishedEarlyDayMotionGet) | **GET** /EarlyDayMotion/{id} | Returns a single Early Day Motion by ID



## earlyDayMotionsListGet

> ApiResponseListPublishedWrittenQuestion earlyDayMotionsListGet(opts)

Returns a list of Early Day Motions

Get a list of Early Day Motions which meet the specified criteria. Only supports Published and Withdrawn status.

### Example

```javascript
import HouseOfCommonsOralAndWrittenQuestionsApi from 'house_of_commons_oral_and_written_questions_api';

let apiInstance = new HouseOfCommonsOralAndWrittenQuestionsApi.EarlyDayMotionsApi();
let opts = {
  'parametersEdmIds': [null], // [Number] | Early Day Motions with an ID in the list provided.
  'parametersUINWithAmendmentSuffix': "parametersUINWithAmendmentSuffix_example", // String | Early Day Motions with an UINWithAmendmentSuffix provided.
  'parametersSearchTerm': "parametersSearchTerm_example", // String | Early Day Motions where the title includes the search term provided.
  'parametersCurrentStatusDateStart': new Date("2013-10-20T19:20:30+01:00"), // Date | Early Day Motions where the current status has been set on or after the date provided. Date format YYYY-MM-DD.
  'parametersCurrentStatusDateEnd': new Date("2013-10-20T19:20:30+01:00"), // Date | Early Day Motions where the current status has been set on or before the date provided. Date format YYYY-MM-DD.
  'parametersIsPrayer': true, // Boolean | Early Day Motions which are a prayer against a Negative Statutory Instrument.
  'parametersMemberId': 56, // Number | Return Early Day Motions tabled by Member with ID provided.
  'parametersIncludeSponsoredByMember': true, // Boolean | Include Early Day Motions sponsored by Member specified
  'parametersTabledStartDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Early Day Motions where the date tabled is on or after the date provided. Date format YYYY-MM-DD.
  'parametersTabledEndDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Early Day Motions where the date tabled is on or before the date provided. Date format YYYY-MM-DD.
  'parametersStatuses': ["null"], // [String] | Early Day Motions where current status is in the selected list.
  'parametersOrderBy': "parametersOrderBy_example", // String | Order results by date tabled, title or signature count. Default is date tabled.
  'parametersSkip': 56, // Number | The number of records to skip from the first, default is 0.
  'parametersTake': 56 // Number | The number of records to return, default is 25, maximum is 100.
};
apiInstance.earlyDayMotionsListGet(opts, (error, data, response) => {
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
 **parametersEdmIds** | [**[Number]**](Number.md)| Early Day Motions with an ID in the list provided. | [optional] 
 **parametersUINWithAmendmentSuffix** | **String**| Early Day Motions with an UINWithAmendmentSuffix provided. | [optional] 
 **parametersSearchTerm** | **String**| Early Day Motions where the title includes the search term provided. | [optional] 
 **parametersCurrentStatusDateStart** | **Date**| Early Day Motions where the current status has been set on or after the date provided. Date format YYYY-MM-DD. | [optional] 
 **parametersCurrentStatusDateEnd** | **Date**| Early Day Motions where the current status has been set on or before the date provided. Date format YYYY-MM-DD. | [optional] 
 **parametersIsPrayer** | **Boolean**| Early Day Motions which are a prayer against a Negative Statutory Instrument. | [optional] 
 **parametersMemberId** | **Number**| Return Early Day Motions tabled by Member with ID provided. | [optional] 
 **parametersIncludeSponsoredByMember** | **Boolean**| Include Early Day Motions sponsored by Member specified | [optional] 
 **parametersTabledStartDate** | **Date**| Early Day Motions where the date tabled is on or after the date provided. Date format YYYY-MM-DD. | [optional] 
 **parametersTabledEndDate** | **Date**| Early Day Motions where the date tabled is on or before the date provided. Date format YYYY-MM-DD. | [optional] 
 **parametersStatuses** | [**[String]**](String.md)| Early Day Motions where current status is in the selected list. | [optional] 
 **parametersOrderBy** | **String**| Order results by date tabled, title or signature count. Default is date tabled. | [optional] 
 **parametersSkip** | **Number**| The number of records to skip from the first, default is 0. | [optional] 
 **parametersTake** | **Number**| The number of records to return, default is 25, maximum is 100. | [optional] 

### Return type

[**ApiResponseListPublishedWrittenQuestion**](ApiResponseListPublishedWrittenQuestion.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## publishedEarlyDayMotionGet

> ApiResponseListPublishedWrittenQuestion publishedEarlyDayMotionGet(id)

Returns a single Early Day Motion by ID

Get a single Early Day Motion which has the ID specified.

### Example

```javascript
import HouseOfCommonsOralAndWrittenQuestionsApi from 'house_of_commons_oral_and_written_questions_api';

let apiInstance = new HouseOfCommonsOralAndWrittenQuestionsApi.EarlyDayMotionsApi();
let id = 56; // Number | Early Day Motion with the ID specified.
apiInstance.publishedEarlyDayMotionGet(id, (error, data, response) => {
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
 **id** | **Number**| Early Day Motion with the ID specified. | 

### Return type

[**ApiResponseListPublishedWrittenQuestion**](ApiResponseListPublishedWrittenQuestion.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

