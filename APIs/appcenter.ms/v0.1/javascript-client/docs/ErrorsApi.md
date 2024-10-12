# AppCenterClient.ErrorsApi

All URIs are relative to *https://api.appcenter.ms*

Method | HTTP request | Description
------------- | ------------- | -------------
[**errorsAppBuildsList**](ErrorsApi.md#errorsAppBuildsList) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/availableAppBuilds | 
[**errorsAvailableVersions**](ErrorsApi.md#errorsAvailableVersions) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/available_versions | 
[**errorsCountsPerDay**](ErrorsApi.md#errorsCountsPerDay) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/errorCountsPerDay | 
[**errorsDeleteError**](ErrorsApi.md#errorsDeleteError) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/errors/errorGroups/{errorGroupId}/errors/{errorId} | 
[**errorsErrorAttachmentLocation**](ErrorsApi.md#errorsErrorAttachmentLocation) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/{errorId}/attachments/{attachmentId}/location | 
[**errorsErrorAttachmentText**](ErrorsApi.md#errorsErrorAttachmentText) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/{errorId}/attachments/{attachmentId}/text | 
[**errorsErrorAttachments**](ErrorsApi.md#errorsErrorAttachments) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/{errorId}/attachments | 
[**errorsErrorDownload**](ErrorsApi.md#errorsErrorDownload) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/errorGroups/{errorGroupId}/errors/{errorId}/download | 
[**errorsErrorFreeDevicePercentages**](ErrorsApi.md#errorsErrorFreeDevicePercentages) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/errorfreeDevicePercentages | 
[**errorsErrorGroupsSearch**](ErrorsApi.md#errorsErrorGroupsSearch) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/errorGroups/search | 
[**errorsErrorLocation**](ErrorsApi.md#errorsErrorLocation) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/errorGroups/{errorGroupId}/errors/{errorId}/location | 
[**errorsErrorSearch**](ErrorsApi.md#errorsErrorSearch) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/search | 
[**errorsErrorStackTrace**](ErrorsApi.md#errorsErrorStackTrace) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/errorGroups/{errorGroupId}/errors/{errorId}/stacktrace | 
[**errorsGetErrorDetails**](ErrorsApi.md#errorsGetErrorDetails) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/errorGroups/{errorGroupId}/errors/{errorId} | 
[**errorsGetRetentionSettings**](ErrorsApi.md#errorsGetRetentionSettings) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/retention_settings | gets the retention settings in days
[**errorsGroupCountsPerDay**](ErrorsApi.md#errorsGroupCountsPerDay) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/errorGroups/{errorGroupId}/errorCountsPerDay | 
[**errorsGroupDetails**](ErrorsApi.md#errorsGroupDetails) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/errorGroups/{errorGroupId} | 
[**errorsGroupErrorFreeDevicePercentages**](ErrorsApi.md#errorsGroupErrorFreeDevicePercentages) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/errorGroups/{errorGroupId}/errorfreeDevicePercentages | 
[**errorsGroupErrorStackTrace**](ErrorsApi.md#errorsGroupErrorStackTrace) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/errorGroups/{errorGroupId}/stacktrace | 
[**errorsGroupList**](ErrorsApi.md#errorsGroupList) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/errorGroups | 
[**errorsGroupModelCounts**](ErrorsApi.md#errorsGroupModelCounts) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/errorGroups/{errorGroupId}/models | 
[**errorsGroupOperatingSystemCounts**](ErrorsApi.md#errorsGroupOperatingSystemCounts) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/errorGroups/{errorGroupId}/operatingSystems | 
[**errorsLatestErrorDetails**](ErrorsApi.md#errorsLatestErrorDetails) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/errorGroups/{errorGroupId}/errors/latest | 
[**errorsListForGroup**](ErrorsApi.md#errorsListForGroup) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/errorGroups/{errorGroupId}/errors | 
[**errorsListSessionLogs**](ErrorsApi.md#errorsListSessionLogs) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/{errorId}/sessionLogs | 
[**errorsUpdateState**](ErrorsApi.md#errorsUpdateState) | **PATCH** /v0.1/apps/{owner_name}/{app_name}/errors/errorGroups/{errorGroupId} | 



## errorsAppBuildsList

> ErrorsAppBuildsList200Response errorsAppBuildsList(version, start, ownerName, appName, opts)



List of app builds

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.ErrorsApi();
let version = "version_example"; // String | 
let start = new Date("2013-10-20T19:20:30+01:00"); // Date | Start date time in data in ISO 8601 date time format
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'end': new Date("2013-10-20T19:20:30+01:00"), // Date | Last date time in data in ISO 8601 date time format
  'top': 30, // Number | The maximum number of results to return. (0 will fetch all results till the max number.)
  'errorType': "errorType_example" // String | Type of error (handled vs unhandled), including All
};
apiInstance.errorsAppBuildsList(version, start, ownerName, appName, opts, (error, data, response) => {
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
 **version** | **String**|  | 
 **start** | **Date**| Start date time in data in ISO 8601 date time format | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **end** | **Date**| Last date time in data in ISO 8601 date time format | [optional] 
 **top** | **Number**| The maximum number of results to return. (0 will fetch all results till the max number.) | [optional] [default to 30]
 **errorType** | **String**| Type of error (handled vs unhandled), including All | [optional] 

### Return type

[**ErrorsAppBuildsList200Response**](ErrorsAppBuildsList200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## errorsAvailableVersions

> ErrorsAvailableVersions200Response errorsAvailableVersions(start, ownerName, appName, opts)



Get all available versions in the time range.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.ErrorsApi();
let start = new Date("2013-10-20T19:20:30+01:00"); // Date | Start date time in data in ISO 8601 date time format
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'end': new Date("2013-10-20T19:20:30+01:00"), // Date | Last date time in data in ISO 8601 date time format
  'top': 30, // Number | The maximum number of results to return. (0 will fetch all results till the max number.)
  'skip': 0, // Number | The offset (starting at 0) of the first result to return. This parameter along with limit is used to perform pagination.
  'filter': "filter_example", // String | A filter as specified in https://github.com/Microsoft/api-guidelines/blob/master/Guidelines.md#97-filtering.
  'inlinecount': "'none'", // String | Controls whether or not to include a count of all the items across all pages.
  'errorType': "errorType_example" // String | Type of error (handled vs unhandled), including All
};
apiInstance.errorsAvailableVersions(start, ownerName, appName, opts, (error, data, response) => {
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
 **start** | **Date**| Start date time in data in ISO 8601 date time format | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **end** | **Date**| Last date time in data in ISO 8601 date time format | [optional] 
 **top** | **Number**| The maximum number of results to return. (0 will fetch all results till the max number.) | [optional] [default to 30]
 **skip** | **Number**| The offset (starting at 0) of the first result to return. This parameter along with limit is used to perform pagination. | [optional] [default to 0]
 **filter** | **String**| A filter as specified in https://github.com/Microsoft/api-guidelines/blob/master/Guidelines.md#97-filtering. | [optional] 
 **inlinecount** | **String**| Controls whether or not to include a count of all the items across all pages. | [optional] [default to &#39;none&#39;]
 **errorType** | **String**| Type of error (handled vs unhandled), including All | [optional] 

### Return type

[**ErrorsAvailableVersions200Response**](ErrorsAvailableVersions200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## errorsCountsPerDay

> ErrorsCountsPerDay200Response errorsCountsPerDay(start, ownerName, appName, opts)



Count of crashes or errors by day in the time range based the selected versions. If SingleErrorTypeParameter is not provided, defaults to handlederror.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.ErrorsApi();
let start = new Date("2013-10-20T19:20:30+01:00"); // Date | Start date time in data in ISO 8601 date time format
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'version': "version_example", // String | 
  'end': new Date("2013-10-20T19:20:30+01:00"), // Date | Last date time in data in ISO 8601 date time format
  'appBuild': "appBuild_example", // String | app build
  'errorType': "errorType_example" // String | Type of error (handled vs unhandled), excluding All
};
apiInstance.errorsCountsPerDay(start, ownerName, appName, opts, (error, data, response) => {
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
 **start** | **Date**| Start date time in data in ISO 8601 date time format | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **version** | **String**|  | [optional] 
 **end** | **Date**| Last date time in data in ISO 8601 date time format | [optional] 
 **appBuild** | **String**| app build | [optional] 
 **errorType** | **String**| Type of error (handled vs unhandled), excluding All | [optional] 

### Return type

[**ErrorsCountsPerDay200Response**](ErrorsCountsPerDay200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## errorsDeleteError

> ErrorsDeleteError200Response errorsDeleteError(errorGroupId, errorId, ownerName, appName)



Delete a specific error and related attachments and blobs for an app. Searchable data will not be deleted immediately and may take up to 30 days.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.ErrorsApi();
let errorGroupId = "errorGroupId_example"; // String | The id of the error group
let errorId = "errorId_example"; // String | The id of the error
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.errorsDeleteError(errorGroupId, errorId, ownerName, appName, (error, data, response) => {
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
 **errorGroupId** | **String**| The id of the error group | 
 **errorId** | **String**| The id of the error | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

[**ErrorsDeleteError200Response**](ErrorsDeleteError200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## errorsErrorAttachmentLocation

> ErrorsErrorLocation200Response errorsErrorAttachmentLocation(errorId, attachmentId, ownerName, appName)



Error attachment location.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.ErrorsApi();
let errorId = "errorId_example"; // String | The id of the error
let attachmentId = "attachmentId_example"; // String | Error attachment id.
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.errorsErrorAttachmentLocation(errorId, attachmentId, ownerName, appName, (error, data, response) => {
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
 **errorId** | **String**| The id of the error | 
 **attachmentId** | **String**| Error attachment id. | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

[**ErrorsErrorLocation200Response**](ErrorsErrorLocation200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## errorsErrorAttachmentText

> ErrorsErrorAttachmentText200Response errorsErrorAttachmentText(errorId, attachmentId, ownerName, appName)



Error attachment text.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.ErrorsApi();
let errorId = "errorId_example"; // String | The id of the error
let attachmentId = "attachmentId_example"; // String | Error attachment id.
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.errorsErrorAttachmentText(errorId, attachmentId, ownerName, appName, (error, data, response) => {
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
 **errorId** | **String**| The id of the error | 
 **attachmentId** | **String**| Error attachment id. | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

[**ErrorsErrorAttachmentText200Response**](ErrorsErrorAttachmentText200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## errorsErrorAttachments

> [ErrorsErrorAttachments200ResponseInner] errorsErrorAttachments(errorId, ownerName, appName)



List error attachments.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.ErrorsApi();
let errorId = "errorId_example"; // String | The id of the error
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.errorsErrorAttachments(errorId, ownerName, appName, (error, data, response) => {
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
 **errorId** | **String**| The id of the error | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

[**[ErrorsErrorAttachments200ResponseInner]**](ErrorsErrorAttachments200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## errorsErrorDownload

> Object errorsErrorDownload(errorGroupId, errorId, ownerName, appName, opts)



Download details for a specific error.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.ErrorsApi();
let errorGroupId = "errorGroupId_example"; // String | The id of the error group
let errorId = "errorId_example"; // String | The id of the error
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'format': "format_example" // String | the format of the crash log
};
apiInstance.errorsErrorDownload(errorGroupId, errorId, ownerName, appName, opts, (error, data, response) => {
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
 **errorGroupId** | **String**| The id of the error group | 
 **errorId** | **String**| The id of the error | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **format** | **String**| the format of the crash log | [optional] 

### Return type

**Object**

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## errorsErrorFreeDevicePercentages

> ErrorsGroupErrorFreeDevicePercentages200Response errorsErrorFreeDevicePercentages(start, ownerName, appName, opts)



Percentage of error-free devices by day in the time range based on the selected versions. If SingleErrorTypeParameter is not provided, defaults to handlederror. API will return -1 if crash devices is greater than active devices

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.ErrorsApi();
let start = new Date("2013-10-20T19:20:30+01:00"); // Date | Start date time in data in ISO 8601 date time format
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'end': new Date("2013-10-20T19:20:30+01:00"), // Date | Last date time in data in ISO 8601 date time format
  'versions': ["null"], // [String] | 
  'appBuild': "appBuild_example", // String | app build
  'errorType': "errorType_example" // String | Type of error (handled vs unhandled), excluding All
};
apiInstance.errorsErrorFreeDevicePercentages(start, ownerName, appName, opts, (error, data, response) => {
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
 **start** | **Date**| Start date time in data in ISO 8601 date time format | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **end** | **Date**| Last date time in data in ISO 8601 date time format | [optional] 
 **versions** | [**[String]**](String.md)|  | [optional] 
 **appBuild** | **String**| app build | [optional] 
 **errorType** | **String**| Type of error (handled vs unhandled), excluding All | [optional] 

### Return type

[**ErrorsGroupErrorFreeDevicePercentages200Response**](ErrorsGroupErrorFreeDevicePercentages200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## errorsErrorGroupsSearch

> ErrorsErrorGroupsSearch200Response errorsErrorGroupsSearch(ownerName, appName, opts)



Error groups list based on search parameters

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.ErrorsApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'filter': "filter_example", // String | A filter as specified in OData notation
  'q': "q_example", // String | A query string
  'order': "'desc'", // String | It controls the order of sorting
  'sort': "'matchingReportsCount'", // String | It controls the sort based on specified field
  'top': 100, // Number | The maximum number of results to return
  'skip': 0 // Number | The offset (starting at 0) of the first result to return. This parameter along with limit is used to perform pagination.
};
apiInstance.errorsErrorGroupsSearch(ownerName, appName, opts, (error, data, response) => {
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
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **filter** | **String**| A filter as specified in OData notation | [optional] 
 **q** | **String**| A query string | [optional] 
 **order** | **String**| It controls the order of sorting | [optional] [default to &#39;desc&#39;]
 **sort** | **String**| It controls the sort based on specified field | [optional] [default to &#39;matchingReportsCount&#39;]
 **top** | **Number**| The maximum number of results to return | [optional] [default to 100]
 **skip** | **Number**| The offset (starting at 0) of the first result to return. This parameter along with limit is used to perform pagination. | [optional] [default to 0]

### Return type

[**ErrorsErrorGroupsSearch200Response**](ErrorsErrorGroupsSearch200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## errorsErrorLocation

> ErrorsErrorLocation200Response errorsErrorLocation(errorGroupId, errorId, ownerName, appName)



Error location.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.ErrorsApi();
let errorGroupId = "errorGroupId_example"; // String | The id of the error group
let errorId = "errorId_example"; // String | The id of the error
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.errorsErrorLocation(errorGroupId, errorId, ownerName, appName, (error, data, response) => {
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
 **errorGroupId** | **String**| The id of the error group | 
 **errorId** | **String**| The id of the error | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

[**ErrorsErrorLocation200Response**](ErrorsErrorLocation200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## errorsErrorSearch

> ErrorsErrorSearch200Response errorsErrorSearch(ownerName, appName, opts)



Errors list based on search parameters

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.ErrorsApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'filter': "filter_example", // String | A filter as specified in OData notation
  'q': "q_example", // String | A query string
  'order': "'desc'", // String | It controls the order of sorting
  'sort': "'timestamp'", // String | It controls the sort based on specified field
  'top': 100, // Number | The maximum number of results to return
  'skip': 0 // Number | The offset (starting at 0) of the first result to return. This parameter along with limit is used to perform pagination.
};
apiInstance.errorsErrorSearch(ownerName, appName, opts, (error, data, response) => {
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
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **filter** | **String**| A filter as specified in OData notation | [optional] 
 **q** | **String**| A query string | [optional] 
 **order** | **String**| It controls the order of sorting | [optional] [default to &#39;desc&#39;]
 **sort** | **String**| It controls the sort based on specified field | [optional] [default to &#39;timestamp&#39;]
 **top** | **Number**| The maximum number of results to return | [optional] [default to 100]
 **skip** | **Number**| The offset (starting at 0) of the first result to return. This parameter along with limit is used to perform pagination. | [optional] [default to 0]

### Return type

[**ErrorsErrorSearch200Response**](ErrorsErrorSearch200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## errorsErrorStackTrace

> DiagnosticsStackTrace errorsErrorStackTrace(errorGroupId, errorId, ownerName, appName)



Error Stacktrace details.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.ErrorsApi();
let errorGroupId = "errorGroupId_example"; // String | The id of the error group
let errorId = "errorId_example"; // String | The id of the error
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.errorsErrorStackTrace(errorGroupId, errorId, ownerName, appName, (error, data, response) => {
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
 **errorGroupId** | **String**| The id of the error group | 
 **errorId** | **String**| The id of the error | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

[**DiagnosticsStackTrace**](DiagnosticsStackTrace.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## errorsGetErrorDetails

> ErrorsLatestErrorDetails200Response errorsGetErrorDetails(errorGroupId, errorId, ownerName, appName)



Error details.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.ErrorsApi();
let errorGroupId = "errorGroupId_example"; // String | The id of the error group
let errorId = "errorId_example"; // String | The id of the error
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.errorsGetErrorDetails(errorGroupId, errorId, ownerName, appName, (error, data, response) => {
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
 **errorGroupId** | **String**| The id of the error group | 
 **errorId** | **String**| The id of the error | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

[**ErrorsLatestErrorDetails200Response**](ErrorsLatestErrorDetails200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## errorsGetRetentionSettings

> ErrorsGetRetentionSettings200Response errorsGetRetentionSettings(ownerName, appName)

gets the retention settings in days

gets the retention settings in days

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.ErrorsApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.errorsGetRetentionSettings(ownerName, appName, (error, data, response) => {
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
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

[**ErrorsGetRetentionSettings200Response**](ErrorsGetRetentionSettings200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## errorsGroupCountsPerDay

> ErrorsCountsPerDay200Response errorsGroupCountsPerDay(errorGroupId, start, ownerName, appName, opts)



Count of errors by day in the time range of the selected error group with selected version

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.ErrorsApi();
let errorGroupId = "errorGroupId_example"; // String | The id of the error group
let start = new Date("2013-10-20T19:20:30+01:00"); // Date | Start date time in data in ISO 8601 date time format
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'version': "version_example", // String | 
  'end': new Date("2013-10-20T19:20:30+01:00") // Date | Last date time in data in ISO 8601 date time format
};
apiInstance.errorsGroupCountsPerDay(errorGroupId, start, ownerName, appName, opts, (error, data, response) => {
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
 **errorGroupId** | **String**| The id of the error group | 
 **start** | **Date**| Start date time in data in ISO 8601 date time format | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **version** | **String**|  | [optional] 
 **end** | **Date**| Last date time in data in ISO 8601 date time format | [optional] 

### Return type

[**ErrorsCountsPerDay200Response**](ErrorsCountsPerDay200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## errorsGroupDetails

> ErrorsGroupDetails200Response errorsGroupDetails(errorGroupId, ownerName, appName)



Error group details

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.ErrorsApi();
let errorGroupId = "errorGroupId_example"; // String | The id of the error group
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.errorsGroupDetails(errorGroupId, ownerName, appName, (error, data, response) => {
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
 **errorGroupId** | **String**| The id of the error group | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

[**ErrorsGroupDetails200Response**](ErrorsGroupDetails200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## errorsGroupErrorFreeDevicePercentages

> ErrorsGroupErrorFreeDevicePercentages200Response errorsGroupErrorFreeDevicePercentages(errorGroupId, start, ownerName, appName, opts)



Percentage of error-free devices by day in the time range. Api will return -1 if crash devices is greater than active devices

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.ErrorsApi();
let errorGroupId = "errorGroupId_example"; // String | The id of the error group
let start = new Date("2013-10-20T19:20:30+01:00"); // Date | Start date time in data in ISO 8601 date time format
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'end': new Date("2013-10-20T19:20:30+01:00") // Date | Last date time in data in ISO 8601 date time format
};
apiInstance.errorsGroupErrorFreeDevicePercentages(errorGroupId, start, ownerName, appName, opts, (error, data, response) => {
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
 **errorGroupId** | **String**| The id of the error group | 
 **start** | **Date**| Start date time in data in ISO 8601 date time format | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **end** | **Date**| Last date time in data in ISO 8601 date time format | [optional] 

### Return type

[**ErrorsGroupErrorFreeDevicePercentages200Response**](ErrorsGroupErrorFreeDevicePercentages200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## errorsGroupErrorStackTrace

> DiagnosticsStackTrace errorsGroupErrorStackTrace(errorGroupId, ownerName, appName)



Gets the stack trace for the error group.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.ErrorsApi();
let errorGroupId = "errorGroupId_example"; // String | The id of the error group
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.errorsGroupErrorStackTrace(errorGroupId, ownerName, appName, (error, data, response) => {
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
 **errorGroupId** | **String**| The id of the error group | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

[**DiagnosticsStackTrace**](DiagnosticsStackTrace.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## errorsGroupList

> ErrorsGroupList200Response errorsGroupList(start, ownerName, appName, opts)



List of error groups

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.ErrorsApi();
let start = new Date("2013-10-20T19:20:30+01:00"); // Date | Start date time in data in ISO 8601 date time format
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'version': "version_example", // String | 
  'appBuild': "appBuild_example", // String | app build
  'groupState': "groupState_example", // String | 
  'end': new Date("2013-10-20T19:20:30+01:00"), // Date | Last date time in data in ISO 8601 date time format
  'orderby': "'count desc'", // String | controls the sorting order and sorting based on which column
  'top': 30, // Number | The maximum number of results to return. (0 will fetch all results till the max number.)
  'errorType': "errorType_example" // String | Type of error (handled vs unhandled), including All
};
apiInstance.errorsGroupList(start, ownerName, appName, opts, (error, data, response) => {
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
 **start** | **Date**| Start date time in data in ISO 8601 date time format | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **version** | **String**|  | [optional] 
 **appBuild** | **String**| app build | [optional] 
 **groupState** | **String**|  | [optional] 
 **end** | **Date**| Last date time in data in ISO 8601 date time format | [optional] 
 **orderby** | **String**| controls the sorting order and sorting based on which column | [optional] [default to &#39;count desc&#39;]
 **top** | **Number**| The maximum number of results to return. (0 will fetch all results till the max number.) | [optional] [default to 30]
 **errorType** | **String**| Type of error (handled vs unhandled), including All | [optional] 

### Return type

[**ErrorsGroupList200Response**](ErrorsGroupList200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## errorsGroupModelCounts

> ErrorsGroupModelCounts200Response errorsGroupModelCounts(errorGroupId, ownerName, appName, opts)



Top models of the selected error group.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.ErrorsApi();
let errorGroupId = "errorGroupId_example"; // String | The id of the error group
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'top': 30 // Number | The maximum number of results to return. (0 will fetch all results till the max number.)
};
apiInstance.errorsGroupModelCounts(errorGroupId, ownerName, appName, opts, (error, data, response) => {
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
 **errorGroupId** | **String**| The id of the error group | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **top** | **Number**| The maximum number of results to return. (0 will fetch all results till the max number.) | [optional] [default to 30]

### Return type

[**ErrorsGroupModelCounts200Response**](ErrorsGroupModelCounts200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## errorsGroupOperatingSystemCounts

> ErrorsGroupOperatingSystemCounts200Response errorsGroupOperatingSystemCounts(errorGroupId, ownerName, appName, opts)



Top OSes of the selected error group.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.ErrorsApi();
let errorGroupId = "errorGroupId_example"; // String | The id of the error group
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'top': 30 // Number | The maximum number of results to return. (0 will fetch all results till the max number.)
};
apiInstance.errorsGroupOperatingSystemCounts(errorGroupId, ownerName, appName, opts, (error, data, response) => {
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
 **errorGroupId** | **String**| The id of the error group | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **top** | **Number**| The maximum number of results to return. (0 will fetch all results till the max number.) | [optional] [default to 30]

### Return type

[**ErrorsGroupOperatingSystemCounts200Response**](ErrorsGroupOperatingSystemCounts200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## errorsLatestErrorDetails

> ErrorsLatestErrorDetails200Response errorsLatestErrorDetails(errorGroupId, ownerName, appName)



Latest error details.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.ErrorsApi();
let errorGroupId = "errorGroupId_example"; // String | The id of the error group
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.errorsLatestErrorDetails(errorGroupId, ownerName, appName, (error, data, response) => {
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
 **errorGroupId** | **String**| The id of the error group | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

[**ErrorsLatestErrorDetails200Response**](ErrorsLatestErrorDetails200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## errorsListForGroup

> ErrorsListForGroup200Response errorsListForGroup(errorGroupId, start, ownerName, appName, opts)



Get all errors for group

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.ErrorsApi();
let errorGroupId = "errorGroupId_example"; // String | The id of the error group
let start = new Date("2013-10-20T19:20:30+01:00"); // Date | Start date time in data in ISO 8601 date time format
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'end': new Date("2013-10-20T19:20:30+01:00"), // Date | Last date time in data in ISO 8601 date time format
  'top': 30, // Number | The maximum number of results to return. (0 will fetch all results till the max number.)
  'model': "model_example", // String | 
  'os': "os_example" // String | 
};
apiInstance.errorsListForGroup(errorGroupId, start, ownerName, appName, opts, (error, data, response) => {
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
 **errorGroupId** | **String**| The id of the error group | 
 **start** | **Date**| Start date time in data in ISO 8601 date time format | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **end** | **Date**| Last date time in data in ISO 8601 date time format | [optional] 
 **top** | **Number**| The maximum number of results to return. (0 will fetch all results till the max number.) | [optional] [default to 30]
 **model** | **String**|  | [optional] 
 **os** | **String**|  | [optional] 

### Return type

[**ErrorsListForGroup200Response**](ErrorsListForGroup200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## errorsListSessionLogs

> ErrorsListSessionLogs200Response errorsListSessionLogs(errorId, ownerName, appName, opts)



Get session logs by error ID

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.ErrorsApi();
let errorId = "errorId_example"; // String | The id of the error
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'date': new Date("2013-10-20T19:20:30+01:00") // Date | Date of data requested
};
apiInstance.errorsListSessionLogs(errorId, ownerName, appName, opts, (error, data, response) => {
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
 **errorId** | **String**| The id of the error | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **date** | **Date**| Date of data requested | [optional] 

### Return type

[**ErrorsListSessionLogs200Response**](ErrorsListSessionLogs200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## errorsUpdateState

> ErrorsGroupDetails200Response errorsUpdateState(errorGroupId, ownerName, appName, errorsUpdateStateRequest)



Update error group state

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.ErrorsApi();
let errorGroupId = "errorGroupId_example"; // String | The id of the error group
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let errorsUpdateStateRequest = new AppCenterClient.ErrorsUpdateStateRequest(); // ErrorsUpdateStateRequest | The state of the error group
apiInstance.errorsUpdateState(errorGroupId, ownerName, appName, errorsUpdateStateRequest, (error, data, response) => {
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
 **errorGroupId** | **String**| The id of the error group | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **errorsUpdateStateRequest** | [**ErrorsUpdateStateRequest**](ErrorsUpdateStateRequest.md)| The state of the error group | 

### Return type

[**ErrorsGroupDetails200Response**](ErrorsGroupDetails200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

