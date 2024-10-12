# AvazaApiDocumentation.TimesheetSubmissionApi

All URIs are relative to *https://api.avaza.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**timesheetSubmissionPost**](TimesheetSubmissionApi.md#timesheetSubmissionPost) | **POST** /api/TimesheetSubmission | Submit Timesheets for Approval.



## timesheetSubmissionPost

> Object timesheetSubmissionPost(opts)

Submit Timesheets for Approval.

Either provide a a specific Day (WholeDayOf) or any day in a Week (WholeWeekOf) to submit all draft timesheets in that day or week

### Example

```javascript
import AvazaApiDocumentation from 'avaza_api_documentation';
let defaultClient = AvazaApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AvazaApiDocumentation.TimesheetSubmissionApi();
let opts = {
  'sendNotifications': true, // Boolean | Send email alerts to timesheet approvers. Defaults to true
  'wholeWeekOf': new Date("2013-10-20T19:20:30+01:00"), // Date | A date (yyyy-MM-dd) that falls within  a Week to have all timesheets in that week submitted. Respects the First Day of Week setting in your account Timesheet Settings to determine the week range.
  'wholeDayOf': new Date("2013-10-20T19:20:30+01:00"), // Date | A date (yyyy-MM-dd) to submit all timesheets on this day
  'userID': 56 // Number | The user to submit timesheets for. Defaults to current user. Only allowed to be different from the current user when the current user has rights to Impersonate other users.
};
apiInstance.timesheetSubmissionPost(opts, (error, data, response) => {
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
 **sendNotifications** | **Boolean**| Send email alerts to timesheet approvers. Defaults to true | [optional] 
 **wholeWeekOf** | **Date**| A date (yyyy-MM-dd) that falls within  a Week to have all timesheets in that week submitted. Respects the First Day of Week setting in your account Timesheet Settings to determine the week range. | [optional] 
 **wholeDayOf** | **Date**| A date (yyyy-MM-dd) to submit all timesheets on this day | [optional] 
 **userID** | **Number**| The user to submit timesheets for. Defaults to current user. Only allowed to be different from the current user when the current user has rights to Impersonate other users. | [optional] 

### Return type

**Object**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml

