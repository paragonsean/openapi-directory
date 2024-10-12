# WrittenQuestionsServiceApi.DailyReportsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiDailyreportsDailyreportsGet**](DailyReportsApi.md#apiDailyreportsDailyreportsGet) | **GET** /api/dailyreports/dailyreports | Returns a list of daily reports



## apiDailyreportsDailyreportsGet

> DailyReportViewModelSearchResult apiDailyreportsDailyreportsGet(opts)

Returns a list of daily reports

### Example

```javascript
import WrittenQuestionsServiceApi from 'written_questions_service_api';

let apiInstance = new WrittenQuestionsServiceApi.DailyReportsApi();
let opts = {
  'dateFrom': new Date("2013-10-20T19:20:30+01:00"), // Date | Daily report with report date on or after the date specified. Date format yyyy-mm-dd
  'dateTo': new Date("2013-10-20T19:20:30+01:00"), // Date | Daily report with report date on or before the date specified. Date format yyyy-mm-dd
  'house': new WrittenQuestionsServiceApi.HouseEnum(), // HouseEnum | Daily report relating to the House specified. Defaults to Bicameral
  'skip': 56, // Number | Number of records to skip, default is 0
  'take': 56 // Number | Number of records to take, default is 20
};
apiInstance.apiDailyreportsDailyreportsGet(opts, (error, data, response) => {
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
 **dateFrom** | **Date**| Daily report with report date on or after the date specified. Date format yyyy-mm-dd | [optional] 
 **dateTo** | **Date**| Daily report with report date on or before the date specified. Date format yyyy-mm-dd | [optional] 
 **house** | [**HouseEnum**](.md)| Daily report relating to the House specified. Defaults to Bicameral | [optional] 
 **skip** | **Number**| Number of records to skip, default is 0 | [optional] 
 **take** | **Number**| Number of records to take, default is 20 | [optional] 

### Return type

[**DailyReportViewModelSearchResult**](DailyReportViewModelSearchResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

