# BrazeEndpoints.KPIApi

All URIs are relative to *https://rest.iad-01.braze.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dailyActiveUsersByDate_0**](KPIApi.md#dailyActiveUsersByDate_0) | **GET** /kpi/dau/data_series | Daily Active Users by Date
[**dailyNewUsersByDate_0**](KPIApi.md#dailyNewUsersByDate_0) | **GET** /kpi/new_users/data_series | Daily New Users by Date
[**kpIsForDailyAppUninstallsByDate_0**](KPIApi.md#kpIsForDailyAppUninstallsByDate_0) | **GET** /kpi/uninstalls/data_series | KPIs for Daily App Uninstalls by Date
[**monthlyActiveUsersForLast30Days_0**](KPIApi.md#monthlyActiveUsersForLast30Days_0) | **GET** /kpi/mau/data_series | Monthly Active Users for Last 30 Days



## dailyActiveUsersByDate_0

> dailyActiveUsersByDate_0(opts)

Daily Active Users by Date

This endpoint allows you to retrieve a daily series of the total number of unique active users on each date.   ## Response  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     \&quot;message\&quot;: (required, string) the status of the export, returns &#39;success&#39; when completed without errors,     \&quot;data\&quot; : [         {             \&quot;time\&quot; : (string) date as ISO 8601 date,             \&quot;dau\&quot; : (int)         },         ...     ] } &#x60;&#x60;&#x60;

### Example

```javascript
import BrazeEndpoints from 'braze_endpoints';

let apiInstance = new BrazeEndpoints.KPIApi();
let opts = {
  'length': "10", // String | (Required) Integer  Max number of days before ending_at to include in the returned series - must be between 1 and 100 inclusive
  'endingAt': "2018-06-28T23:59:59-5:00", // String | (Optional) DateTime (ISO 8601 string)  Point in time when the data series should end - defaults to time of the request
  'appId': "{{app_identifier}}" // String | (Optional) String  App API identifier; if excluded, results for all apps in app group will be returned
};
apiInstance.dailyActiveUsersByDate_0(opts, (error, data, response) => {
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
 **length** | **String**| (Required) Integer  Max number of days before ending_at to include in the returned series - must be between 1 and 100 inclusive | [optional] 
 **endingAt** | **String**| (Optional) DateTime (ISO 8601 string)  Point in time when the data series should end - defaults to time of the request | [optional] 
 **appId** | **String**| (Optional) String  App API identifier; if excluded, results for all apps in app group will be returned | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## dailyNewUsersByDate_0

> dailyNewUsersByDate_0(opts)

Daily New Users by Date

This endpoint allows you to retrieve a daily series of the total number of new users on each date.   ## Response  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     \&quot;message\&quot;: (required, string) the status of the export, returns &#39;success&#39; when completed without errors,     \&quot;data\&quot; : [         {             \&quot;time\&quot; : (string) date as ISO 8601 date,             \&quot;new_users\&quot; : (int)         },         ...     ] } &#x60;&#x60;&#x60;

### Example

```javascript
import BrazeEndpoints from 'braze_endpoints';

let apiInstance = new BrazeEndpoints.KPIApi();
let opts = {
  'length': "14", // String | (Required) Integer  Max number of days before ending_at to include in the returned series - must be between 1 and 100 inclusive
  'endingAt': "2018-06-28T23:59:59-5:00", // String | (Optional) DateTime (ISO 8601 string)  Point in time when the data series should end - defaults to time of the request
  'appId': "{{app_identifier}}" // String | (Optional) String  App API identifier; if excluded, results for all apps in app group will be returned
};
apiInstance.dailyNewUsersByDate_0(opts, (error, data, response) => {
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
 **length** | **String**| (Required) Integer  Max number of days before ending_at to include in the returned series - must be between 1 and 100 inclusive | [optional] 
 **endingAt** | **String**| (Optional) DateTime (ISO 8601 string)  Point in time when the data series should end - defaults to time of the request | [optional] 
 **appId** | **String**| (Optional) String  App API identifier; if excluded, results for all apps in app group will be returned | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## kpIsForDailyAppUninstallsByDate_0

> kpIsForDailyAppUninstallsByDate_0(opts)

KPIs for Daily App Uninstalls by Date

This endpoint allows you to retrieve a daily series of the total number of uninstalls on each date.  ## Response  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     \&quot;message\&quot;: (required, string) the status of the export, returns &#39;success&#39; when completed without errors,     \&quot;data\&quot; : [         {             \&quot;time\&quot; : (string) date as ISO 8601 date,             \&quot;uninstalls\&quot; : (int)         },         ...     ] } &#x60;&#x60;&#x60;

### Example

```javascript
import BrazeEndpoints from 'braze_endpoints';

let apiInstance = new BrazeEndpoints.KPIApi();
let opts = {
  'length': "14", // String | (Required) Integer  Max number of days before ending_at to include in the returned series - must be between 1 and 100 inclusive
  'endingAt': "2018-06-28T23:59:59-5:00", // String | (Optional) DateTime (ISO 8601 string)  Point in time when the data series should end - defaults to time of the request
  'appId': "{{app_identifier}}" // String | (Optional) String  App API identifier; if excluded, results for all apps in app group will be returned
};
apiInstance.kpIsForDailyAppUninstallsByDate_0(opts, (error, data, response) => {
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
 **length** | **String**| (Required) Integer  Max number of days before ending_at to include in the returned series - must be between 1 and 100 inclusive | [optional] 
 **endingAt** | **String**| (Optional) DateTime (ISO 8601 string)  Point in time when the data series should end - defaults to time of the request | [optional] 
 **appId** | **String**| (Optional) String  App API identifier; if excluded, results for all apps in app group will be returned | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## monthlyActiveUsersForLast30Days_0

> monthlyActiveUsersForLast30Days_0(opts)

Monthly Active Users for Last 30 Days

This endpoint allows you to retrieve a daily series of the total number of unique active users over a 30-day rolling window.  ## Response  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     \&quot;message\&quot;: (required, string) the status of the export, returns &#39;success&#39; when completed without errors,     \&quot;data\&quot; : [         {             \&quot;time\&quot; : (string) date as ISO 8601 date,             \&quot;mau\&quot; : (int)         },         ...     ] } &#x60;&#x60;&#x60;

### Example

```javascript
import BrazeEndpoints from 'braze_endpoints';

let apiInstance = new BrazeEndpoints.KPIApi();
let opts = {
  'length': "7", // String | (Required) Integer  Max number of days before ending_at to include in the returned series - must be between 1 and 100 inclusive
  'endingAt': "2018-06-28T23:59:59-05:00", // String | (Optional) DateTime (ISO 8601 string)  Point in time when the data series should end - defaults to time of the request
  'appId': "{{app_identifier}}" // String | (Optional) String  App API identifier; if excluded, results for all apps in app group will be returned
};
apiInstance.monthlyActiveUsersForLast30Days_0(opts, (error, data, response) => {
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
 **length** | **String**| (Required) Integer  Max number of days before ending_at to include in the returned series - must be between 1 and 100 inclusive | [optional] 
 **endingAt** | **String**| (Optional) DateTime (ISO 8601 string)  Point in time when the data series should end - defaults to time of the request | [optional] 
 **appId** | **String**| (Optional) String  App API identifier; if excluded, results for all apps in app group will be returned | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

