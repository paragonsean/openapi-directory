# SeveraPublicRestApiDocumentation.HoursReadApi

All URIs are relative to *https://api.severa.visma.com/rest-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**timeEntriesGetTimeEntries**](HoursReadApi.md#timeEntriesGetTimeEntries) | **GET** /v1/timeentries | Get the time entries.
[**timeEntriesGetTimeEntriesForUser**](HoursReadApi.md#timeEntriesGetTimeEntriesForUser) | **GET** /v1/users/{userGuid}/timeentries | Get all the time entries for a user.
[**timeEntriesGetTimeEntry**](HoursReadApi.md#timeEntriesGetTimeEntry) | **GET** /v1/timeentries/{guid} | Get time entry by ID.
[**workHoursGetDeletedWorkHours**](HoursReadApi.md#workHoursGetDeletedWorkHours) | **GET** /v1/deletedworkhours | Get the deleted work hours.
[**workHoursGetProjectWorkHours**](HoursReadApi.md#workHoursGetProjectWorkHours) | **GET** /v1/projects/{projectGuid}/workhours | Get all the work hours for phases of a project for invoicing
[**workHoursGetWorkHour**](HoursReadApi.md#workHoursGetWorkHour) | **GET** /v1/workhours/{guid} | Get work hour by ID
[**workHoursGetWorkHours**](HoursReadApi.md#workHoursGetWorkHours) | **GET** /v1/workhours | Get the work hours.
[**workHoursGetWorkHoursForUser**](HoursReadApi.md#workHoursGetWorkHoursForUser) | **GET** /v1/users/{userGuid}/workhours | Get all the work hours for a user



## timeEntriesGetTimeEntries

> [TimeEntryModel] timeEntriesGetTimeEntries(opts)

Get the time entries.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.HoursReadApi();
let opts = {
  'firstRow': 0, // Number | Optional: first row to fetch. Default 0 = first row.
  'phaseGuid': ["null"], // [String] | Optional: Filters time entries for given phases.
  'timeEntryTypeGuid': ["null"], // [String] | Optional: Filters time entries for given time entry types.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'changedSince': new Date("2013-10-20T19:20:30+01:00") // Date | Optional: Get time entries that have been added or changed after this date time (greater or equal).
};
apiInstance.timeEntriesGetTimeEntries(opts, (error, data, response) => {
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
 **firstRow** | **Number**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0]
 **phaseGuid** | [**[String]**](String.md)| Optional: Filters time entries for given phases. | [optional] 
 **timeEntryTypeGuid** | [**[String]**](String.md)| Optional: Filters time entries for given time entry types. | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **changedSince** | **Date**| Optional: Get time entries that have been added or changed after this date time (greater or equal). | [optional] 

### Return type

[**[TimeEntryModel]**](TimeEntryModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## timeEntriesGetTimeEntriesForUser

> [TimeEntryModel] timeEntriesGetTimeEntriesForUser(userGuid, opts)

Get all the time entries for a user.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.HoursReadApi();
let userGuid = "userGuid_example"; // String | ID of the user.
let opts = {
  'startDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional: starting date from which to get the time entries. Default all.
  'endDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional: starting date to which to get the time entries. Default all.
  'phaseGuid': ["null"], // [String] | Optional: Filters time entries for given phases.
  'timeEntryTypeGuid': ["null"], // [String] | Optional: Filters time entries for given time entry types.
  'firstRow': 0, // Number | Optional: first row to fetch. Default 0 = first row.
  'rowCount': 56 // Number | Optional: How many rows to fetch, Default 20, maximum 100.
};
apiInstance.timeEntriesGetTimeEntriesForUser(userGuid, opts, (error, data, response) => {
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
 **userGuid** | **String**| ID of the user. | 
 **startDate** | **Date**| Optional: starting date from which to get the time entries. Default all. | [optional] 
 **endDate** | **Date**| Optional: starting date to which to get the time entries. Default all. | [optional] 
 **phaseGuid** | [**[String]**](String.md)| Optional: Filters time entries for given phases. | [optional] 
 **timeEntryTypeGuid** | [**[String]**](String.md)| Optional: Filters time entries for given time entry types. | [optional] 
 **firstRow** | **Number**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0]
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 

### Return type

[**[TimeEntryModel]**](TimeEntryModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## timeEntriesGetTimeEntry

> TimeEntryModel timeEntriesGetTimeEntry(guid)

Get time entry by ID.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.HoursReadApi();
let guid = "guid_example"; // String | Id used to get the time entry.
apiInstance.timeEntriesGetTimeEntry(guid, (error, data, response) => {
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
 **guid** | **String**| Id used to get the time entry. | 

### Return type

[**TimeEntryModel**](TimeEntryModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workHoursGetDeletedWorkHours

> [DeletedWorkHourModel] workHoursGetDeletedWorkHours(opts)

Get the deleted work hours.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.HoursReadApi();
let opts = {
  'pageToken': "pageToken_example", // String | Optional: page token to fetch the next page.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'projectGuids': ["null"], // [String] | Optional: ID of the project for the deleted work hours to be fetched. If not provided, returns for all projects. Default all.
  'userGuids': ["null"], // [String] | Optional: ID of the user. If not provided, returns for all users. Default all.
  'deletedSince': new Date("2013-10-20T19:20:30+01:00") // Date | Optional: Get work hours that have been deleted after this date time (greater or equal).
};
apiInstance.workHoursGetDeletedWorkHours(opts, (error, data, response) => {
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
 **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **projectGuids** | [**[String]**](String.md)| Optional: ID of the project for the deleted work hours to be fetched. If not provided, returns for all projects. Default all. | [optional] 
 **userGuids** | [**[String]**](String.md)| Optional: ID of the user. If not provided, returns for all users. Default all. | [optional] 
 **deletedSince** | **Date**| Optional: Get work hours that have been deleted after this date time (greater or equal). | [optional] 

### Return type

[**[DeletedWorkHourModel]**](DeletedWorkHourModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workHoursGetProjectWorkHours

> [WorkHourOutputModel] workHoursGetProjectWorkHours(projectGuid, opts)

Get all the work hours for phases of a project for invoicing

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.HoursReadApi();
let projectGuid = "projectGuid_example"; // String | ID of the project.
let opts = {
  'isBillable': true, // Boolean | Optional: Filter the work hours. If true/false, only the billable/non-billable ones are returned. If null, all are returned. Default is null.
  'isBilled': true, // Boolean | Optional: Filter the work hours. If true/false, only the ones that are/are not invoiced are returned. If null, all are returned. Default is null.
  'startDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional: starting date from which to get the hours. Default all.
  'endDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional: starting date to which to get the hours. Default all.
  'pageToken': "pageToken_example", // String | Optional: page token to fetch the next page.
  'rowCount': 56 // Number | Optional: How many rows to fetch, Default 20, maximum 100.
};
apiInstance.workHoursGetProjectWorkHours(projectGuid, opts, (error, data, response) => {
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
 **projectGuid** | **String**| ID of the project. | 
 **isBillable** | **Boolean**| Optional: Filter the work hours. If true/false, only the billable/non-billable ones are returned. If null, all are returned. Default is null. | [optional] 
 **isBilled** | **Boolean**| Optional: Filter the work hours. If true/false, only the ones that are/are not invoiced are returned. If null, all are returned. Default is null. | [optional] 
 **startDate** | **Date**| Optional: starting date from which to get the hours. Default all. | [optional] 
 **endDate** | **Date**| Optional: starting date to which to get the hours. Default all. | [optional] 
 **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 

### Return type

[**[WorkHourOutputModel]**](WorkHourOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workHoursGetWorkHour

> WorkHourOutputModel workHoursGetWorkHour(guid)

Get work hour by ID

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.HoursReadApi();
let guid = "guid_example"; // String | Id used to get the work hour.
apiInstance.workHoursGetWorkHour(guid, (error, data, response) => {
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
 **guid** | **String**| Id used to get the work hour. | 

### Return type

[**WorkHourOutputModel**](WorkHourOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workHoursGetWorkHours

> [WorkHourOutputModel] workHoursGetWorkHours(opts)

Get the work hours.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.HoursReadApi();
let opts = {
  'pageToken': "pageToken_example", // String | Optional: page token to fetch the next page.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'changedSince': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional: Get work hours that have been added or changed after this date time (greater or equal).
  'billableStatus': new SeveraPublicRestApiDocumentation.BillableStatusType(), // BillableStatusType | Billable status type
  'eventDateStart': new Date("2013-10-20"), // Date | Optional: Get work hours that have event date after this date time (greater or equal).
  'eventDateEnd': new Date("2013-10-20") // Date | Optional: Get work hours that have event date before this date time (less or equal).
};
apiInstance.workHoursGetWorkHours(opts, (error, data, response) => {
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
 **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **changedSince** | **Date**| Optional: Get work hours that have been added or changed after this date time (greater or equal). | [optional] 
 **billableStatus** | [**BillableStatusType**](.md)| Billable status type | [optional] 
 **eventDateStart** | **Date**| Optional: Get work hours that have event date after this date time (greater or equal). | [optional] 
 **eventDateEnd** | **Date**| Optional: Get work hours that have event date before this date time (less or equal). | [optional] 

### Return type

[**[WorkHourOutputModel]**](WorkHourOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workHoursGetWorkHoursForUser

> [WorkHourOutputModel] workHoursGetWorkHoursForUser(userGuid, opts)

Get all the work hours for a user

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.HoursReadApi();
let userGuid = "userGuid_example"; // String | ID of the user.
let opts = {
  'startDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional: starting date from which to get the hours. Default all.
  'endDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional: starting date to which to get the hours. Default all.
  'phaseGuid': ["null"], // [String] | Optional: ID of the phase to get the hours for. Default all.
  'workTypeGuid': ["null"], // [String] | Optional: ID of the work type. Default all.
  'pageToken': "pageToken_example", // String | Optional: page token to fetch the next page.
  'rowCount': 56 // Number | Optional: How many rows to fetch, Default 20, maximum 100.
};
apiInstance.workHoursGetWorkHoursForUser(userGuid, opts, (error, data, response) => {
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
 **userGuid** | **String**| ID of the user. | 
 **startDate** | **Date**| Optional: starting date from which to get the hours. Default all. | [optional] 
 **endDate** | **Date**| Optional: starting date to which to get the hours. Default all. | [optional] 
 **phaseGuid** | [**[String]**](String.md)| Optional: ID of the phase to get the hours for. Default all. | [optional] 
 **workTypeGuid** | [**[String]**](String.md)| Optional: ID of the work type. Default all. | [optional] 
 **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 

### Return type

[**[WorkHourOutputModel]**](WorkHourOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

