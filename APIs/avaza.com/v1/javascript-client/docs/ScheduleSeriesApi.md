# AvazaApiDocumentation.ScheduleSeriesApi

All URIs are relative to *https://api.avaza.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**scheduleSeriesAddBooking**](ScheduleSeriesApi.md#scheduleSeriesAddBooking) | **POST** /ScheduleSeries/AddBooking | Create new Schedule Booking
[**scheduleSeriesAddLeave**](ScheduleSeriesApi.md#scheduleSeriesAddLeave) | **POST** /ScheduleSeries/AddLeave | Create new Leave Booking
[**scheduleSeriesEditBooking**](ScheduleSeriesApi.md#scheduleSeriesEditBooking) | **PUT** /ScheduleSeries/EditBooking | Edit Booking
[**scheduleSeriesEditLeave**](ScheduleSeriesApi.md#scheduleSeriesEditLeave) | **PUT** /ScheduleSeries/EditLeave | Edit Leave Booking
[**scheduleSeriesGet**](ScheduleSeriesApi.md#scheduleSeriesGet) | **GET** /api/ScheduleSeries | Gets list of Schedule Series



## scheduleSeriesAddBooking

> ScheduleSeriesDetails scheduleSeriesAddBooking(model)

Create new Schedule Booking

### Example

```javascript
import AvazaApiDocumentation from 'avaza_api_documentation';
let defaultClient = AvazaApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AvazaApiDocumentation.ScheduleSeriesApi();
let model = new AvazaApiDocumentation.CreateBooking(); // CreateBooking | 
apiInstance.scheduleSeriesAddBooking(model, (error, data, response) => {
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
 **model** | [**CreateBooking**](CreateBooking.md)|  | 

### Return type

[**ScheduleSeriesDetails**](ScheduleSeriesDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## scheduleSeriesAddLeave

> ScheduleSeriesDetails scheduleSeriesAddLeave(model)

Create new Leave Booking

### Example

```javascript
import AvazaApiDocumentation from 'avaza_api_documentation';
let defaultClient = AvazaApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AvazaApiDocumentation.ScheduleSeriesApi();
let model = new AvazaApiDocumentation.CreateLeave(); // CreateLeave | 
apiInstance.scheduleSeriesAddLeave(model, (error, data, response) => {
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
 **model** | [**CreateLeave**](CreateLeave.md)|  | 

### Return type

[**ScheduleSeriesDetails**](ScheduleSeriesDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## scheduleSeriesEditBooking

> ScheduleSeriesDetails scheduleSeriesEditBooking(model)

Edit Booking

### Example

```javascript
import AvazaApiDocumentation from 'avaza_api_documentation';
let defaultClient = AvazaApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AvazaApiDocumentation.ScheduleSeriesApi();
let model = new AvazaApiDocumentation.EditBooking(); // EditBooking | 
apiInstance.scheduleSeriesEditBooking(model, (error, data, response) => {
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
 **model** | [**EditBooking**](EditBooking.md)|  | 

### Return type

[**ScheduleSeriesDetails**](ScheduleSeriesDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## scheduleSeriesEditLeave

> ScheduleSeriesDetails scheduleSeriesEditLeave(model)

Edit Leave Booking

### Example

```javascript
import AvazaApiDocumentation from 'avaza_api_documentation';
let defaultClient = AvazaApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AvazaApiDocumentation.ScheduleSeriesApi();
let model = new AvazaApiDocumentation.EditLeave(); // EditLeave | 
apiInstance.scheduleSeriesEditLeave(model, (error, data, response) => {
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
 **model** | [**EditLeave**](EditLeave.md)|  | 

### Return type

[**ScheduleSeriesDetails**](ScheduleSeriesDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## scheduleSeriesGet

> ScheduleSeriesList scheduleSeriesGet(opts)

Gets list of Schedule Series

Schedule Series represents a strip of time assigned to a user over a date range, for a certain number of hours per day. They can be for Leave or for project work Bookings.

### Example

```javascript
import AvazaApiDocumentation from 'avaza_api_documentation';
let defaultClient = AvazaApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AvazaApiDocumentation.ScheduleSeriesApi();
let opts = {
  'updatedAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | Limit results to records updated after the specified date
  'scheduleStartDateFrom': new Date("2013-10-20T19:20:30+01:00"), // Date | Filter for schedules that start on or after a specific date
  'scheduleStartDateTo': new Date("2013-10-20T19:20:30+01:00"), // Date | Filter for schedules that start on or before a specific date
  'scheduleEndDateFrom': new Date("2013-10-20T19:20:30+01:00"), // Date | Filter for schedules that end on or after a specific date
  'scheduleEndDateTo': new Date("2013-10-20T19:20:30+01:00"), // Date | Filter for schedules that end on or before a specific date
  'userID': 56, // Number | The UserID of a schedule user to filter assignments for. Only api users with Admin role can see all schedules across all users. Users with ScheduleUser role can access their own ScheduleSeries.
  'userEmail': "userEmail_example", // String | The email of the user who has been scheduled
  'timeSheetCategoryID': 56, // Number | Filter for schedule records linked to a specific timesheeet category
  'timeSheetCategoryName': "timeSheetCategoryName_example", // String | Filter for schedule records with a specific timesheeet category name (exact string match)
  'leaveTypeID': 56, // Number | Filter to records of a particular leave type
  'projectID': 56, // Number | Filter to only include books linked to a specific project
  'companyID': 56, // Number | Filter to only include records linked to projects, where that project belongs to a specific customer company
  'pageSize': 56, // Number | Number of items per page (max 1000)
  'pageNumber': 56, // Number | Page to display. Starts from 1.
  'sort': "sort_example" // String | Optional sorting instruction. Currently possible values: \"DateUpdated\", \"DateCreated\", \"DateUpdated desc\", \"DateCreated desc\"
};
apiInstance.scheduleSeriesGet(opts, (error, data, response) => {
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
 **scheduleStartDateFrom** | **Date**| Filter for schedules that start on or after a specific date | [optional] 
 **scheduleStartDateTo** | **Date**| Filter for schedules that start on or before a specific date | [optional] 
 **scheduleEndDateFrom** | **Date**| Filter for schedules that end on or after a specific date | [optional] 
 **scheduleEndDateTo** | **Date**| Filter for schedules that end on or before a specific date | [optional] 
 **userID** | **Number**| The UserID of a schedule user to filter assignments for. Only api users with Admin role can see all schedules across all users. Users with ScheduleUser role can access their own ScheduleSeries. | [optional] 
 **userEmail** | **String**| The email of the user who has been scheduled | [optional] 
 **timeSheetCategoryID** | **Number**| Filter for schedule records linked to a specific timesheeet category | [optional] 
 **timeSheetCategoryName** | **String**| Filter for schedule records with a specific timesheeet category name (exact string match) | [optional] 
 **leaveTypeID** | **Number**| Filter to records of a particular leave type | [optional] 
 **projectID** | **Number**| Filter to only include books linked to a specific project | [optional] 
 **companyID** | **Number**| Filter to only include records linked to projects, where that project belongs to a specific customer company | [optional] 
 **pageSize** | **Number**| Number of items per page (max 1000) | [optional] 
 **pageNumber** | **Number**| Page to display. Starts from 1. | [optional] 
 **sort** | **String**| Optional sorting instruction. Currently possible values: \&quot;DateUpdated\&quot;, \&quot;DateCreated\&quot;, \&quot;DateUpdated desc\&quot;, \&quot;DateCreated desc\&quot; | [optional] 

### Return type

[**ScheduleSeriesList**](ScheduleSeriesList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml

