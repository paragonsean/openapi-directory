# AvazaApiDocumentation.TimesheetTimerApi

All URIs are relative to *https://api.avaza.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**timesheetTimerGetRunningTimer**](TimesheetTimerApi.md#timesheetTimerGetRunningTimer) | **GET** /api/TimesheetTimer | Gets the  Running Timer if there is one for a user.
[**timesheetTimerStartTimer**](TimesheetTimerApi.md#timesheetTimerStartTimer) | **POST** /api/TimesheetTimer/{id} | Starts a Timer running on an existing Timesheet Entry
[**timesheetTimerStopTimer**](TimesheetTimerApi.md#timesheetTimerStopTimer) | **DELETE** /api/TimesheetTimer/{id} | Stop the timer running on an existing Timesheet Entry



## timesheetTimerGetRunningTimer

> Object timesheetTimerGetRunningTimer(opts)

Gets the  Running Timer if there is one for a user.

### Example

```javascript
import AvazaApiDocumentation from 'avaza_api_documentation';
let defaultClient = AvazaApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AvazaApiDocumentation.TimesheetTimerApi();
let opts = {
  'userID': 56 // Number | Optional - User ID number if impersonating a different user. Otherwise assumes the current user. Only users with certain security roles have permission to impersonate other users
};
apiInstance.timesheetTimerGetRunningTimer(opts, (error, data, response) => {
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
 **userID** | **Number**| Optional - User ID number if impersonating a different user. Otherwise assumes the current user. Only users with certain security roles have permission to impersonate other users | [optional] 

### Return type

**Object**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## timesheetTimerStartTimer

> Object timesheetTimerStartTimer(id, opts)

Starts a Timer running on an existing Timesheet Entry

### Example

```javascript
import AvazaApiDocumentation from 'avaza_api_documentation';
let defaultClient = AvazaApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AvazaApiDocumentation.TimesheetTimerApi();
let id = 789; // Number | id of timesheet entry that should be used as the basis for running a timer. If the existing timesheet is not on the current day, or you have start/end times enabled, then a new timesheet will be created for the timer.
let opts = {
  'userID': 56 // Number | Optional - User ID number if impersonating a different user. Otherwise assumes the current user. Only users with certain security roles have permission to impersonate other users
};
apiInstance.timesheetTimerStartTimer(id, opts, (error, data, response) => {
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
 **id** | **Number**| id of timesheet entry that should be used as the basis for running a timer. If the existing timesheet is not on the current day, or you have start/end times enabled, then a new timesheet will be created for the timer. | 
 **userID** | **Number**| Optional - User ID number if impersonating a different user. Otherwise assumes the current user. Only users with certain security roles have permission to impersonate other users | [optional] 

### Return type

**Object**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## timesheetTimerStopTimer

> Object timesheetTimerStopTimer(id, opts)

Stop the timer running on an existing Timesheet Entry

### Example

```javascript
import AvazaApiDocumentation from 'avaza_api_documentation';
let defaultClient = AvazaApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AvazaApiDocumentation.TimesheetTimerApi();
let id = 789; // Number | The ID of the existing timesheet entry that needs its timer stopped
let opts = {
  'userID': 56 // Number | Optional - User ID number if impersonating a different user. Otherwise assumes the current user. Only users with certain security roles have permission to impersonate other users
};
apiInstance.timesheetTimerStopTimer(id, opts, (error, data, response) => {
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
 **id** | **Number**| The ID of the existing timesheet entry that needs its timer stopped | 
 **userID** | **Number**| Optional - User ID number if impersonating a different user. Otherwise assumes the current user. Only users with certain security roles have permission to impersonate other users | [optional] 

### Return type

**Object**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml

