# Signl4Api.DutiesApi

All URIs are relative to *https://connect.signl4.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**teamsTeamIdDutyReportsFileNameGet**](DutiesApi.md#teamsTeamIdDutyReportsFileNameGet) | **GET** /teams/{teamId}/dutyReports/{fileName} | Download duty report with a specific fileName
[**teamsTeamIdDutyReportsGet**](DutiesApi.md#teamsTeamIdDutyReportsGet) | **GET** /teams/{teamId}/dutyReports | Get Information about downloadable reports
[**teamsTeamIdDutysummaryGet**](DutiesApi.md#teamsTeamIdDutysummaryGet) | **GET** /teams/{teamId}/dutysummary | Get duty assistant info for a team
[**teamsTeamIdSchedulesDeleteRangePost**](DutiesApi.md#teamsTeamIdSchedulesDeleteRangePost) | **POST** /teams/{teamId}/schedules/deleteRange | Delete duty schedules in range
[**teamsTeamIdSchedulesDutyIdDelete**](DutiesApi.md#teamsTeamIdSchedulesDutyIdDelete) | **DELETE** /teams/{teamId}/schedules/{dutyId} | Delete a specific duty.
[**teamsTeamIdSchedulesGet**](DutiesApi.md#teamsTeamIdSchedulesGet) | **GET** /teams/{teamId}/schedules | Returns information about all duties that belong to the team.
[**teamsTeamIdSchedulesMultiplePost**](DutiesApi.md#teamsTeamIdSchedulesMultiplePost) | **POST** /teams/{teamId}/schedules/multiple | Save multiple schedules. It is possible to override existing schedules if you wish
[**teamsTeamIdSchedulesPost**](DutiesApi.md#teamsTeamIdSchedulesPost) | **POST** /teams/{teamId}/schedules | Create/Update given duty schedule.
[**teamsTeamIdSchedulesScheduleIdGet**](DutiesApi.md#teamsTeamIdSchedulesScheduleIdGet) | **GET** /teams/{teamId}/schedules/{scheduleId} | Returns information of the duty schedule with the specified Id.



## teamsTeamIdDutyReportsFileNameGet

> File teamsTeamIdDutyReportsFileNameGet(teamId, fileName)

Download duty report with a specific fileName

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.DutiesApi();
let teamId = "teamId_example"; // String | ID of team you want to download the duty report for.
let fileName = "fileName_example"; // String | Filename of the csv to download.
apiInstance.teamsTeamIdDutyReportsFileNameGet(teamId, fileName, (error, data, response) => {
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
 **teamId** | **String**| ID of team you want to download the duty report for. | 
 **fileName** | **String**| Filename of the csv to download. | 

### Return type

**File**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## teamsTeamIdDutyReportsGet

> [Object] teamsTeamIdDutyReportsGet(teamId)

Get Information about downloadable reports

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.DutiesApi();
let teamId = "teamId_example"; // String | ID of team you want to get the duty report file infos for.
apiInstance.teamsTeamIdDutyReportsGet(teamId, (error, data, response) => {
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
 **teamId** | **String**| ID of team you want to get the duty report file infos for. | 

### Return type

**[Object]**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## teamsTeamIdDutysummaryGet

> TeamDutySummaryInfo teamsTeamIdDutysummaryGet(teamId, opts)

Get duty assistant info for a team

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.DutiesApi();
let teamId = "teamId_example"; // String | ID of the team the duty belongs to.
let opts = {
  'lastTwoDuties': true // Boolean | 
};
apiInstance.teamsTeamIdDutysummaryGet(teamId, opts, (error, data, response) => {
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
 **teamId** | **String**| ID of the team the duty belongs to. | 
 **lastTwoDuties** | **Boolean**|  | [optional] 

### Return type

[**TeamDutySummaryInfo**](TeamDutySummaryInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## teamsTeamIdSchedulesDeleteRangePost

> [ScheduleInfo] teamsTeamIdSchedulesDeleteRangePost(teamId, opts)

Delete duty schedules in range

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.DutiesApi();
let teamId = "teamId_example"; // String | Team ID you want to delete
let opts = {
  'deleteRangeInfo': new Signl4Api.DeleteRangeInfo() // DeleteRangeInfo | Information with date range to delete from to
};
apiInstance.teamsTeamIdSchedulesDeleteRangePost(teamId, opts, (error, data, response) => {
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
 **teamId** | **String**| Team ID you want to delete | 
 **deleteRangeInfo** | [**DeleteRangeInfo**](DeleteRangeInfo.md)| Information with date range to delete from to | [optional] 

### Return type

[**[ScheduleInfo]**](ScheduleInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json, text/json, text/plain


## teamsTeamIdSchedulesDutyIdDelete

> teamsTeamIdSchedulesDutyIdDelete(teamId, dutyId)

Delete a specific duty.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.DutiesApi();
let teamId = "teamId_example"; // String | ID of the team the duty belongs to.
let dutyId = "dutyId_example"; // String | ID of the duty to be deleted.
apiInstance.teamsTeamIdSchedulesDutyIdDelete(teamId, dutyId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teamId** | **String**| ID of the team the duty belongs to. | 
 **dutyId** | **String**| ID of the duty to be deleted. | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## teamsTeamIdSchedulesGet

> [ScheduleInfo] teamsTeamIdSchedulesGet(teamId, opts)

Returns information about all duties that belong to the team.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.DutiesApi();
let teamId = "teamId_example"; // String | Id of the team the schedules user belongs to
let opts = {
  'userId': "userId_example", // String | 
  'minDate': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'limit': 56 // Number | 
};
apiInstance.teamsTeamIdSchedulesGet(teamId, opts, (error, data, response) => {
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
 **teamId** | **String**| Id of the team the schedules user belongs to | 
 **userId** | **String**|  | [optional] 
 **minDate** | **Date**|  | [optional] 
 **limit** | **Number**|  | [optional] 

### Return type

[**[ScheduleInfo]**](ScheduleInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## teamsTeamIdSchedulesMultiplePost

> [ScheduleInfo] teamsTeamIdSchedulesMultiplePost(teamId, opts)

Save multiple schedules. It is possible to override existing schedules if you wish

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.DutiesApi();
let teamId = "teamId_example"; // String | Team ID to set
let opts = {
  'overrideExisting': true, // Boolean | Override or cut existing schedules if set to true.
  'scheduleInfo': [new Signl4Api.ScheduleInfo()] // [ScheduleInfo] | List of schedules to save
};
apiInstance.teamsTeamIdSchedulesMultiplePost(teamId, opts, (error, data, response) => {
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
 **teamId** | **String**| Team ID to set | 
 **overrideExisting** | **Boolean**| Override or cut existing schedules if set to true. | [optional] 
 **scheduleInfo** | [**[ScheduleInfo]**](ScheduleInfo.md)| List of schedules to save | [optional] 

### Return type

[**[ScheduleInfo]**](ScheduleInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json, text/json, text/plain


## teamsTeamIdSchedulesPost

> ScheduleInfo teamsTeamIdSchedulesPost(teamId, opts)

Create/Update given duty schedule.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.DutiesApi();
let teamId = "teamId_example"; // String | Id of the team the duty is to be assigned to.
let opts = {
  'scheduleInfo': new Signl4Api.ScheduleInfo() // ScheduleInfo | information about the duty schedule to be created
};
apiInstance.teamsTeamIdSchedulesPost(teamId, opts, (error, data, response) => {
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
 **teamId** | **String**| Id of the team the duty is to be assigned to. | 
 **scheduleInfo** | [**ScheduleInfo**](ScheduleInfo.md)| information about the duty schedule to be created | [optional] 

### Return type

[**ScheduleInfo**](ScheduleInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json, text/json, text/plain


## teamsTeamIdSchedulesScheduleIdGet

> ScheduleInfo teamsTeamIdSchedulesScheduleIdGet(teamId, scheduleId)

Returns information of the duty schedule with the specified Id.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.DutiesApi();
let teamId = "teamId_example"; // String | Id of the team the duty belongs to
let scheduleId = "scheduleId_example"; // String | Id of the requested duty schedule.
apiInstance.teamsTeamIdSchedulesScheduleIdGet(teamId, scheduleId, (error, data, response) => {
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
 **teamId** | **String**| Id of the team the duty belongs to | 
 **scheduleId** | **String**| Id of the requested duty schedule. | 

### Return type

[**ScheduleInfo**](ScheduleInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

