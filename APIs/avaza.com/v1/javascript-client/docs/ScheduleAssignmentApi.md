# AvazaApiDocumentation.ScheduleAssignmentApi

All URIs are relative to *https://api.avaza.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**scheduleAssignmentGet**](ScheduleAssignmentApi.md#scheduleAssignmentGet) | **GET** /api/ScheduleAssignment | Gets list of Schedule Assignments.



## scheduleAssignmentGet

> ScheduleAssignmentList scheduleAssignmentGet(opts)

Gets list of Schedule Assignments.

Schedule assignments are per-day, and link to a parent Schedule Series.

### Example

```javascript
import AvazaApiDocumentation from 'avaza_api_documentation';
let defaultClient = AvazaApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AvazaApiDocumentation.ScheduleAssignmentApi();
let opts = {
  'updatedAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | Limit results to records updated after the specified date
  'scheduleDateFrom': new Date("2013-10-20T19:20:30+01:00"), // Date | Filter for schedule assignement  that are  on or after a specific date
  'scheduleDateTo': new Date("2013-10-20T19:20:30+01:00"), // Date | Filter for schedules that are on or before a specific date
  'scheduleSeriesID': 789, // Number | Filter to records for a particular Schedule Series
  'userID': 56, // Number | The UserID of a schedule user to filter assignments for. Only api users with Admin role can see all schedules across all users. Users with ScheduleUser role can access their own ScheduleSeries.
  'userEmail': "userEmail_example", // String | The email of the user who has been scheduled
  'pageSize': 56, // Number | Number of items per page (max 1000)
  'pageNumber': 56, // Number | Page to display. Starts from 1.
  'sort': "sort_example" // String | Optional sorting instruction. Currently possible values: \"DateUpdated\", \"DateCreated\", \"DateUpdated desc\", \"DateCreated desc\"
};
apiInstance.scheduleAssignmentGet(opts, (error, data, response) => {
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
 **updatedAfter** | **Date**| Limit results to records updated after the specified date | [optional] 
 **scheduleDateFrom** | **Date**| Filter for schedule assignement  that are  on or after a specific date | [optional] 
 **scheduleDateTo** | **Date**| Filter for schedules that are on or before a specific date | [optional] 
 **scheduleSeriesID** | **Number**| Filter to records for a particular Schedule Series | [optional] 
 **userID** | **Number**| The UserID of a schedule user to filter assignments for. Only api users with Admin role can see all schedules across all users. Users with ScheduleUser role can access their own ScheduleSeries. | [optional] 
 **userEmail** | **String**| The email of the user who has been scheduled | [optional] 
 **pageSize** | **Number**| Number of items per page (max 1000) | [optional] 
 **pageNumber** | **Number**| Page to display. Starts from 1. | [optional] 
 **sort** | **String**| Optional sorting instruction. Currently possible values: \&quot;DateUpdated\&quot;, \&quot;DateCreated\&quot;, \&quot;DateUpdated desc\&quot;, \&quot;DateCreated desc\&quot; | [optional] 

### Return type

[**ScheduleAssignmentList**](ScheduleAssignmentList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml

