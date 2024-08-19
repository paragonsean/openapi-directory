# SeveraPublicRestApiDocumentation.HoursWriteApi

All URIs are relative to *https://api.severa.visma.com/rest-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**timeEntriesPatchTimeEntry**](HoursWriteApi.md#timeEntriesPatchTimeEntry) | **PATCH** /v1/timeentries/{guid} | Update (Patch) a time entry or a part of it.
[**timeEntriesPostTimeEntry**](HoursWriteApi.md#timeEntriesPostTimeEntry) | **POST** /v1/timeentries | Insert a time entry.
[**workHoursPatchWorkHour**](HoursWriteApi.md#workHoursPatchWorkHour) | **PATCH** /v1/workhours/{guid} | Update (Patch) a work hour or a part of it
[**workHoursPostWorkHour**](HoursWriteApi.md#workHoursPostWorkHour) | **POST** /v1/workhours | Insert a work hour



## timeEntriesPatchTimeEntry

> [TimeEntryModel] timeEntriesPatchTimeEntry(guid, opts)

Update (Patch) a time entry or a part of it.

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

let apiInstance = new SeveraPublicRestApiDocumentation.HoursWriteApi();
let guid = "guid_example"; // String | ID of the time entry.
let opts = {
  'patchOperation': [new SeveraPublicRestApiDocumentation.PatchOperation()] // [PatchOperation] | JSON Patch document of TimeEntryModel.
};
apiInstance.timeEntriesPatchTimeEntry(guid, opts, (error, data, response) => {
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
 **guid** | **String**| ID of the time entry. | 
 **patchOperation** | [**[PatchOperation]**](PatchOperation.md)| JSON Patch document of TimeEntryModel. | [optional] 

### Return type

[**[TimeEntryModel]**](TimeEntryModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## timeEntriesPostTimeEntry

> [TimeEntryModel] timeEntriesPostTimeEntry(opts)

Insert a time entry.

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

let apiInstance = new SeveraPublicRestApiDocumentation.HoursWriteApi();
let opts = {
  'timeEntryModel': new SeveraPublicRestApiDocumentation.TimeEntryModel() // TimeEntryModel | TimeEntryModel.
};
apiInstance.timeEntriesPostTimeEntry(opts, (error, data, response) => {
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
 **timeEntryModel** | [**TimeEntryModel**](TimeEntryModel.md)| TimeEntryModel. | [optional] 

### Return type

[**[TimeEntryModel]**](TimeEntryModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## workHoursPatchWorkHour

> [WorkHourOutputModel] workHoursPatchWorkHour(guid, opts)

Update (Patch) a work hour or a part of it

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

let apiInstance = new SeveraPublicRestApiDocumentation.HoursWriteApi();
let guid = "guid_example"; // String | ID of the work hour. Can also be comma separate list of IDs to patch multiple work hours with one call. When multiple IDs are given, returns model which has list of succeeded work hours and list of errors.
let opts = {
  'patchOperation': [new SeveraPublicRestApiDocumentation.PatchOperation()] // [PatchOperation] | JSON Patch document of WorkHourInputModel
};
apiInstance.workHoursPatchWorkHour(guid, opts, (error, data, response) => {
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
 **guid** | **String**| ID of the work hour. Can also be comma separate list of IDs to patch multiple work hours with one call. When multiple IDs are given, returns model which has list of succeeded work hours and list of errors. | 
 **patchOperation** | [**[PatchOperation]**](PatchOperation.md)| JSON Patch document of WorkHourInputModel | [optional] 

### Return type

[**[WorkHourOutputModel]**](WorkHourOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## workHoursPostWorkHour

> WorkHourOutputModel workHoursPostWorkHour(opts)

Insert a work hour

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

let apiInstance = new SeveraPublicRestApiDocumentation.HoursWriteApi();
let opts = {
  'workHourInputModel': new SeveraPublicRestApiDocumentation.WorkHourInputModel() // WorkHourInputModel | WorkHourInputModel
};
apiInstance.workHoursPostWorkHour(opts, (error, data, response) => {
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
 **workHourInputModel** | [**WorkHourInputModel**](WorkHourInputModel.md)| WorkHourInputModel | [optional] 

### Return type

[**WorkHourOutputModel**](WorkHourOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

