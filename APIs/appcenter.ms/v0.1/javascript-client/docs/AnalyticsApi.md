# AppCenterClient.AnalyticsApi

All URIs are relative to *https://api.appcenter.ms*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analyticsAudienceNameExists**](AnalyticsApi.md#analyticsAudienceNameExists) | **HEAD** /v0.1/apps/{owner_name}/{app_name}/analytics/audiences/{audience_name} | 
[**analyticsCrashCounts**](AnalyticsApi.md#analyticsCrashCounts) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/crash_counts | Available for UWP apps only.
[**analyticsCrashFreeDevicePercentages**](AnalyticsApi.md#analyticsCrashFreeDevicePercentages) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/crashfree_device_percentages | 
[**analyticsCrashGroupCounts**](AnalyticsApi.md#analyticsCrashGroupCounts) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/crash_groups/{crash_group_id}/crash_counts | Available for UWP apps only.
[**analyticsCrashGroupModelCounts**](AnalyticsApi.md#analyticsCrashGroupModelCounts) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/crash_groups/{crash_group_id}/models | Available for UWP apps only.
[**analyticsCrashGroupOperatingSystemCounts**](AnalyticsApi.md#analyticsCrashGroupOperatingSystemCounts) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/crash_groups/{crash_group_id}/operating_systems | Available for UWP apps only.
[**analyticsCrashGroupTotals**](AnalyticsApi.md#analyticsCrashGroupTotals) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/crash_groups/{crash_group_id}/overall | Available for UWP apps only.
[**analyticsCrashGroupsTotals**](AnalyticsApi.md#analyticsCrashGroupsTotals) | **POST** /v0.1/apps/{owner_name}/{app_name}/analytics/crash_groups | 
[**analyticsCreateOrUpdateAudience**](AnalyticsApi.md#analyticsCreateOrUpdateAudience) | **PUT** /v0.1/apps/{owner_name}/{app_name}/analytics/audiences/{audience_name} | 
[**analyticsDeleteAudience**](AnalyticsApi.md#analyticsDeleteAudience) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/analytics/audiences/{audience_name} | 
[**analyticsDeviceCounts**](AnalyticsApi.md#analyticsDeviceCounts) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/active_device_counts | 
[**analyticsDistributionReleaseCounts**](AnalyticsApi.md#analyticsDistributionReleaseCounts) | **POST** /v0.1/apps/{owner_name}/{app_name}/analytics/distribution/release_counts | 
[**analyticsEventCount**](AnalyticsApi.md#analyticsEventCount) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/events/{event_name}/event_count | 
[**analyticsEventDeviceCount**](AnalyticsApi.md#analyticsEventDeviceCount) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/events/{event_name}/device_count | 
[**analyticsEventPerDeviceCount**](AnalyticsApi.md#analyticsEventPerDeviceCount) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/events/{event_name}/count_per_device | 
[**analyticsEventPerSessionCount**](AnalyticsApi.md#analyticsEventPerSessionCount) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/events/{event_name}/count_per_session | 
[**analyticsEventProperties**](AnalyticsApi.md#analyticsEventProperties) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/events/{event_name}/properties | 
[**analyticsEventPropertyCounts**](AnalyticsApi.md#analyticsEventPropertyCounts) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/events/{event_name}/properties/{event_property_name}/counts | 
[**analyticsEvents**](AnalyticsApi.md#analyticsEvents) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/events | 
[**analyticsEventsDelete**](AnalyticsApi.md#analyticsEventsDelete) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/analytics/events/{event_name} | 
[**analyticsEventsDeleteLogs**](AnalyticsApi.md#analyticsEventsDeleteLogs) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/analytics/event_logs/{event_name} | 
[**analyticsGenericLogFlow**](AnalyticsApi.md#analyticsGenericLogFlow) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/generic_log_flow | 
[**analyticsGetAudience**](AnalyticsApi.md#analyticsGetAudience) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/audiences/{audience_name} | 
[**analyticsLanguageCounts**](AnalyticsApi.md#analyticsLanguageCounts) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/languages | 
[**analyticsListAudiences**](AnalyticsApi.md#analyticsListAudiences) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/audiences | 
[**analyticsListCustomProperties**](AnalyticsApi.md#analyticsListCustomProperties) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/audiences/metadata/custom_properties | 
[**analyticsListDeviceProperties**](AnalyticsApi.md#analyticsListDeviceProperties) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/audiences/metadata/device_properties | 
[**analyticsListDevicePropertyValues**](AnalyticsApi.md#analyticsListDevicePropertyValues) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/audiences/metadata/device_properties/{property_name}/values | 
[**analyticsLogFlow**](AnalyticsApi.md#analyticsLogFlow) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/log_flow | 
[**analyticsModelCounts**](AnalyticsApi.md#analyticsModelCounts) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/models | 
[**analyticsOperatingSystemCounts**](AnalyticsApi.md#analyticsOperatingSystemCounts) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/oses | 
[**analyticsPerDeviceCounts**](AnalyticsApi.md#analyticsPerDeviceCounts) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/sessions_per_device | 
[**analyticsPlaceCounts**](AnalyticsApi.md#analyticsPlaceCounts) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/places | 
[**analyticsSessionCounts**](AnalyticsApi.md#analyticsSessionCounts) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/session_counts | 
[**analyticsSessionDurationsDistribution**](AnalyticsApi.md#analyticsSessionDurationsDistribution) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/session_durations_distribution | 
[**analyticsTestAudience**](AnalyticsApi.md#analyticsTestAudience) | **POST** /v0.1/apps/{owner_name}/{app_name}/analytics/audiences/definition/test | 
[**analyticsVersions**](AnalyticsApi.md#analyticsVersions) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/versions | 
[**appBlockLogs**](AnalyticsApi.md#appBlockLogs) | **PUT** /v0.1/apps/{owner_name}/{app_name}/devices/block_logs | 
[**crashesListSessionLogs**](AnalyticsApi.md#crashesListSessionLogs) | **GET** /v0.1/apps/{owner_name}/{app_name}/crashes/{crash_id}/session_logs | 
[**devicesBlockLogs**](AnalyticsApi.md#devicesBlockLogs) | **PUT** /v0.1/apps/{owner_name}/{app_name}/devices/block_logs/{install_id} | 



## analyticsAudienceNameExists

> analyticsAudienceNameExists(audienceName, ownerName, appName)



Returns whether audience definition exists.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AnalyticsApi();
let audienceName = "audienceName_example"; // String | The name of the audience
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.analyticsAudienceNameExists(audienceName, ownerName, appName, (error, data, response) => {
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
 **audienceName** | **String**| The name of the audience | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## analyticsCrashCounts

> AnalyticsCrashCounts200Response analyticsCrashCounts(start, ownerName, appName, opts)

Available for UWP apps only.

Count of crashes by day in the time range based the selected versions. Available for UWP apps only.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AnalyticsApi();
let start = new Date("2013-10-20T19:20:30+01:00"); // Date | Start date time in data in ISO 8601 date time format.
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'end': new Date("2013-10-20T19:20:30+01:00"), // Date | Last date time in data in ISO 8601 date time format.
  'versions': ["null"] // [String] | To select specific application versions
};
apiInstance.analyticsCrashCounts(start, ownerName, appName, opts, (error, data, response) => {
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
 **start** | **Date**| Start date time in data in ISO 8601 date time format. | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **end** | **Date**| Last date time in data in ISO 8601 date time format. | [optional] 
 **versions** | [**[String]**](String.md)| To select specific application versions | [optional] 

### Return type

[**AnalyticsCrashCounts200Response**](AnalyticsCrashCounts200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## analyticsCrashFreeDevicePercentages

> AnalyticsCrashFreeDevicePercentages200Response analyticsCrashFreeDevicePercentages(start, version, ownerName, appName, opts)



Percentage of crash-free device by day in the time range based on the selected versions. Api will return -1 if crash devices is greater than active devices.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AnalyticsApi();
let start = new Date("2013-10-20T19:20:30+01:00"); // Date | Start date time in data in ISO 8601 date time format.
let version = "version_example"; // String | 
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'end': new Date("2013-10-20T19:20:30+01:00") // Date | Last date time in data in ISO 8601 date time format.
};
apiInstance.analyticsCrashFreeDevicePercentages(start, version, ownerName, appName, opts, (error, data, response) => {
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
 **start** | **Date**| Start date time in data in ISO 8601 date time format. | 
 **version** | **String**|  | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **end** | **Date**| Last date time in data in ISO 8601 date time format. | [optional] 

### Return type

[**AnalyticsCrashFreeDevicePercentages200Response**](AnalyticsCrashFreeDevicePercentages200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## analyticsCrashGroupCounts

> AnalyticsCrashCounts200Response analyticsCrashGroupCounts(crashGroupId, version, start, ownerName, appName, opts)

Available for UWP apps only.

Count of crashes by day in the time range of the selected crash group with selected version. Available for UWP apps only.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AnalyticsApi();
let crashGroupId = "crashGroupId_example"; // String | The id of the crash group.
let version = "version_example"; // String | 
let start = new Date("2013-10-20T19:20:30+01:00"); // Date | Start date time in data in ISO 8601 date time format.
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'end': new Date("2013-10-20T19:20:30+01:00") // Date | Last date time in data in ISO 8601 date time format.
};
apiInstance.analyticsCrashGroupCounts(crashGroupId, version, start, ownerName, appName, opts, (error, data, response) => {
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
 **crashGroupId** | **String**| The id of the crash group. | 
 **version** | **String**|  | 
 **start** | **Date**| Start date time in data in ISO 8601 date time format. | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **end** | **Date**| Last date time in data in ISO 8601 date time format. | [optional] 

### Return type

[**AnalyticsCrashCounts200Response**](AnalyticsCrashCounts200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## analyticsCrashGroupModelCounts

> AnalyticsCrashGroupModelCounts200Response analyticsCrashGroupModelCounts(crashGroupId, version, ownerName, appName, opts)

Available for UWP apps only.

Top models of the selected crash group with selected version. Available for UWP apps only.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AnalyticsApi();
let crashGroupId = "crashGroupId_example"; // String | The id of the crash group.
let version = "version_example"; // String | 
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'top': 30 // Number | The maximum number of results to return. (0 will fetch all results)
};
apiInstance.analyticsCrashGroupModelCounts(crashGroupId, version, ownerName, appName, opts, (error, data, response) => {
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
 **crashGroupId** | **String**| The id of the crash group. | 
 **version** | **String**|  | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **top** | **Number**| The maximum number of results to return. (0 will fetch all results) | [optional] [default to 30]

### Return type

[**AnalyticsCrashGroupModelCounts200Response**](AnalyticsCrashGroupModelCounts200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## analyticsCrashGroupOperatingSystemCounts

> AnalyticsCrashGroupOperatingSystemCounts200Response analyticsCrashGroupOperatingSystemCounts(crashGroupId, version, ownerName, appName, opts)

Available for UWP apps only.

Top OSes of the selected crash group with selected version. Available for UWP apps only.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AnalyticsApi();
let crashGroupId = "crashGroupId_example"; // String | The id of the crash group.
let version = "version_example"; // String | 
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'top': 30 // Number | The maximum number of results to return. (0 will fetch all results)
};
apiInstance.analyticsCrashGroupOperatingSystemCounts(crashGroupId, version, ownerName, appName, opts, (error, data, response) => {
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
 **crashGroupId** | **String**| The id of the crash group. | 
 **version** | **String**|  | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **top** | **Number**| The maximum number of results to return. (0 will fetch all results) | [optional] [default to 30]

### Return type

[**AnalyticsCrashGroupOperatingSystemCounts200Response**](AnalyticsCrashGroupOperatingSystemCounts200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## analyticsCrashGroupTotals

> AnalyticsCrashGroupsTotals200ResponseInnerOverall analyticsCrashGroupTotals(crashGroupId, version, ownerName, appName)

Available for UWP apps only.

Overall crashes and affected users count of the selected crash group with selected version. Available for UWP apps only.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AnalyticsApi();
let crashGroupId = "crashGroupId_example"; // String | The id of the crash group.
let version = "version_example"; // String | 
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.analyticsCrashGroupTotals(crashGroupId, version, ownerName, appName, (error, data, response) => {
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
 **crashGroupId** | **String**| The id of the crash group. | 
 **version** | **String**|  | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

[**AnalyticsCrashGroupsTotals200ResponseInnerOverall**](AnalyticsCrashGroupsTotals200ResponseInnerOverall.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## analyticsCrashGroupsTotals

> [AnalyticsCrashGroupsTotals200ResponseInner] analyticsCrashGroupsTotals(ownerName, appName, analyticsCrashGroupsTotalsRequest)



Overall crashes and affected users count of the selected crash groups with selected versions.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AnalyticsApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let analyticsCrashGroupsTotalsRequest = new AppCenterClient.AnalyticsCrashGroupsTotalsRequest(); // AnalyticsCrashGroupsTotalsRequest | 
apiInstance.analyticsCrashGroupsTotals(ownerName, appName, analyticsCrashGroupsTotalsRequest, (error, data, response) => {
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
 **analyticsCrashGroupsTotalsRequest** | [**AnalyticsCrashGroupsTotalsRequest**](AnalyticsCrashGroupsTotalsRequest.md)|  | 

### Return type

[**[AnalyticsCrashGroupsTotals200ResponseInner]**](AnalyticsCrashGroupsTotals200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## analyticsCreateOrUpdateAudience

> AnalyticsGetAudience200Response analyticsCreateOrUpdateAudience(audienceName, ownerName, appName, analyticsTestAudienceRequest)



Creates or updates audience definition.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AnalyticsApi();
let audienceName = "audienceName_example"; // String | The name of the audience
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let analyticsTestAudienceRequest = new AppCenterClient.AnalyticsTestAudienceRequest(); // AnalyticsTestAudienceRequest | Audience definition
apiInstance.analyticsCreateOrUpdateAudience(audienceName, ownerName, appName, analyticsTestAudienceRequest, (error, data, response) => {
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
 **audienceName** | **String**| The name of the audience | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **analyticsTestAudienceRequest** | [**AnalyticsTestAudienceRequest**](AnalyticsTestAudienceRequest.md)| Audience definition | 

### Return type

[**AnalyticsGetAudience200Response**](AnalyticsGetAudience200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## analyticsDeleteAudience

> analyticsDeleteAudience(audienceName, ownerName, appName)



Deletes audience definition.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AnalyticsApi();
let audienceName = "audienceName_example"; // String | The name of the audience
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.analyticsDeleteAudience(audienceName, ownerName, appName, (error, data, response) => {
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
 **audienceName** | **String**| The name of the audience | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## analyticsDeviceCounts

> AnalyticsDeviceCounts200Response analyticsDeviceCounts(start, ownerName, appName, opts)



Count of active devices by interval in the time range.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AnalyticsApi();
let start = new Date("2013-10-20T19:20:30+01:00"); // Date | Start date time in data in ISO 8601 date time format.
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'end': new Date("2013-10-20T19:20:30+01:00"), // Date | Last date time in data in ISO 8601 date time format.
  'versions': ["null"], // [String] | To select specific application versions
  'appBuild': "appBuild_example" // String | Application build number. If build number is specified than multiple versions are not allowed.
};
apiInstance.analyticsDeviceCounts(start, ownerName, appName, opts, (error, data, response) => {
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
 **start** | **Date**| Start date time in data in ISO 8601 date time format. | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **end** | **Date**| Last date time in data in ISO 8601 date time format. | [optional] 
 **versions** | [**[String]**](String.md)| To select specific application versions | [optional] 
 **appBuild** | **String**| Application build number. If build number is specified than multiple versions are not allowed. | [optional] 

### Return type

[**AnalyticsDeviceCounts200Response**](AnalyticsDeviceCounts200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## analyticsDistributionReleaseCounts

> AnalyticsDistributionReleaseCounts200Response analyticsDistributionReleaseCounts(ownerName, appName, analyticsDistributionReleaseCountsRequest)



Count of total downloads for the provided distribution releases.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AnalyticsApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let analyticsDistributionReleaseCountsRequest = new AppCenterClient.AnalyticsDistributionReleaseCountsRequest(); // AnalyticsDistributionReleaseCountsRequest | The releases to retrieve.
apiInstance.analyticsDistributionReleaseCounts(ownerName, appName, analyticsDistributionReleaseCountsRequest, (error, data, response) => {
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
 **analyticsDistributionReleaseCountsRequest** | [**AnalyticsDistributionReleaseCountsRequest**](AnalyticsDistributionReleaseCountsRequest.md)| The releases to retrieve. | 

### Return type

[**AnalyticsDistributionReleaseCounts200Response**](AnalyticsDistributionReleaseCounts200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## analyticsEventCount

> AnalyticsEventCount200Response analyticsEventCount(eventName, start, ownerName, appName, opts)



Count of events by interval in the time range.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AnalyticsApi();
let eventName = "eventName_example"; // String | The id of the event.
let start = new Date("2013-10-20T19:20:30+01:00"); // Date | Start date time in data in ISO 8601 date time format.
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'end': new Date("2013-10-20T19:20:30+01:00"), // Date | Last date time in data in ISO 8601 date time format.
  'versions': ["null"] // [String] | To select specific application versions
};
apiInstance.analyticsEventCount(eventName, start, ownerName, appName, opts, (error, data, response) => {
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
 **eventName** | **String**| The id of the event. | 
 **start** | **Date**| Start date time in data in ISO 8601 date time format. | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **end** | **Date**| Last date time in data in ISO 8601 date time format. | [optional] 
 **versions** | [**[String]**](String.md)| To select specific application versions | [optional] 

### Return type

[**AnalyticsEventCount200Response**](AnalyticsEventCount200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## analyticsEventDeviceCount

> AnalyticsEventDeviceCount200Response analyticsEventDeviceCount(eventName, start, ownerName, appName, opts)



Count of devices for an event by interval in the time range.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AnalyticsApi();
let eventName = "eventName_example"; // String | The id of the event.
let start = new Date("2013-10-20T19:20:30+01:00"); // Date | Start date time in data in ISO 8601 date time format.
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'end': new Date("2013-10-20T19:20:30+01:00"), // Date | Last date time in data in ISO 8601 date time format.
  'versions': ["null"] // [String] | To select specific application versions
};
apiInstance.analyticsEventDeviceCount(eventName, start, ownerName, appName, opts, (error, data, response) => {
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
 **eventName** | **String**| The id of the event. | 
 **start** | **Date**| Start date time in data in ISO 8601 date time format. | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **end** | **Date**| Last date time in data in ISO 8601 date time format. | [optional] 
 **versions** | [**[String]**](String.md)| To select specific application versions | [optional] 

### Return type

[**AnalyticsEventDeviceCount200Response**](AnalyticsEventDeviceCount200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## analyticsEventPerDeviceCount

> AnalyticsEventPerDeviceCount200Response analyticsEventPerDeviceCount(eventName, start, ownerName, appName, opts)



Count of events per device by interval in the time range.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AnalyticsApi();
let eventName = "eventName_example"; // String | The id of the event.
let start = new Date("2013-10-20T19:20:30+01:00"); // Date | Start date time in data in ISO 8601 date time format.
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'end': new Date("2013-10-20T19:20:30+01:00"), // Date | Last date time in data in ISO 8601 date time format.
  'versions': ["null"] // [String] | To select specific application versions
};
apiInstance.analyticsEventPerDeviceCount(eventName, start, ownerName, appName, opts, (error, data, response) => {
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
 **eventName** | **String**| The id of the event. | 
 **start** | **Date**| Start date time in data in ISO 8601 date time format. | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **end** | **Date**| Last date time in data in ISO 8601 date time format. | [optional] 
 **versions** | [**[String]**](String.md)| To select specific application versions | [optional] 

### Return type

[**AnalyticsEventPerDeviceCount200Response**](AnalyticsEventPerDeviceCount200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## analyticsEventPerSessionCount

> AnalyticsEventPerSessionCount200Response analyticsEventPerSessionCount(eventName, start, ownerName, appName, opts)



Count of events per session by interval in the time range.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AnalyticsApi();
let eventName = "eventName_example"; // String | The id of the event.
let start = new Date("2013-10-20T19:20:30+01:00"); // Date | Start date time in data in ISO 8601 date time format.
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'end': new Date("2013-10-20T19:20:30+01:00"), // Date | Last date time in data in ISO 8601 date time format.
  'versions': ["null"] // [String] | To select specific application versions
};
apiInstance.analyticsEventPerSessionCount(eventName, start, ownerName, appName, opts, (error, data, response) => {
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
 **eventName** | **String**| The id of the event. | 
 **start** | **Date**| Start date time in data in ISO 8601 date time format. | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **end** | **Date**| Last date time in data in ISO 8601 date time format. | [optional] 
 **versions** | [**[String]**](String.md)| To select specific application versions | [optional] 

### Return type

[**AnalyticsEventPerSessionCount200Response**](AnalyticsEventPerSessionCount200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## analyticsEventProperties

> AnalyticsEventProperties200Response analyticsEventProperties(eventName, ownerName, appName)



Event properties.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AnalyticsApi();
let eventName = "eventName_example"; // String | The id of the event.
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.analyticsEventProperties(eventName, ownerName, appName, (error, data, response) => {
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
 **eventName** | **String**| The id of the event. | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

[**AnalyticsEventProperties200Response**](AnalyticsEventProperties200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## analyticsEventPropertyCounts

> AnalyticsEventPropertyCounts200Response analyticsEventPropertyCounts(eventName, eventPropertyName, start, ownerName, appName, opts)



Event properties value counts during the time range in descending order.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AnalyticsApi();
let eventName = "eventName_example"; // String | The id of the event.
let eventPropertyName = "eventPropertyName_example"; // String | The id of the event property.
let start = new Date("2013-10-20T19:20:30+01:00"); // Date | Start date time in data in ISO 8601 date time format.
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'end': new Date("2013-10-20T19:20:30+01:00"), // Date | Last date time in data in ISO 8601 date time format.
  'versions': ["null"], // [String] | To select specific application versions
  'top': 10 // Number | The number of property values to return. Set to 0 in order to fetch all results available.
};
apiInstance.analyticsEventPropertyCounts(eventName, eventPropertyName, start, ownerName, appName, opts, (error, data, response) => {
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
 **eventName** | **String**| The id of the event. | 
 **eventPropertyName** | **String**| The id of the event property. | 
 **start** | **Date**| Start date time in data in ISO 8601 date time format. | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **end** | **Date**| Last date time in data in ISO 8601 date time format. | [optional] 
 **versions** | [**[String]**](String.md)| To select specific application versions | [optional] 
 **top** | **Number**| The number of property values to return. Set to 0 in order to fetch all results available. | [optional] [default to 10]

### Return type

[**AnalyticsEventPropertyCounts200Response**](AnalyticsEventPropertyCounts200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## analyticsEvents

> AnalyticsEvents200Response analyticsEvents(start, ownerName, appName, opts)



Count of active events in the time range ordered by event.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AnalyticsApi();
let start = new Date("2013-10-20T19:20:30+01:00"); // Date | Start date time in data in ISO 8601 date time format.
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'end': new Date("2013-10-20T19:20:30+01:00"), // Date | Last date time in data in ISO 8601 date time format.
  'versions': ["null"], // [String] | To select specific application versions
  'eventName': ["null"], // [String] | To select the specific events.
  'top': 30, // Number | The maximum number of results to return. (0 will fetch all results)
  'skip': 0, // Number | The offset (starting at 0) of the first result to return. This parameter along with limit is used to perform pagination.
  'inlinecount': "'none'", // String | Controls whether or not to include a count of all the items across all pages.
  'orderby': "'count desc'" // String | controls the sorting order and sorting based on which column
};
apiInstance.analyticsEvents(start, ownerName, appName, opts, (error, data, response) => {
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
 **start** | **Date**| Start date time in data in ISO 8601 date time format. | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **end** | **Date**| Last date time in data in ISO 8601 date time format. | [optional] 
 **versions** | [**[String]**](String.md)| To select specific application versions | [optional] 
 **eventName** | [**[String]**](String.md)| To select the specific events. | [optional] 
 **top** | **Number**| The maximum number of results to return. (0 will fetch all results) | [optional] [default to 30]
 **skip** | **Number**| The offset (starting at 0) of the first result to return. This parameter along with limit is used to perform pagination. | [optional] [default to 0]
 **inlinecount** | **String**| Controls whether or not to include a count of all the items across all pages. | [optional] [default to &#39;none&#39;]
 **orderby** | **String**| controls the sorting order and sorting based on which column | [optional] [default to &#39;count desc&#39;]

### Return type

[**AnalyticsEvents200Response**](AnalyticsEvents200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## analyticsEventsDelete

> analyticsEventsDelete(eventName, ownerName, appName)



Delete the set of Events with the specified event names.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AnalyticsApi();
let eventName = "eventName_example"; // String | The id of the event.
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.analyticsEventsDelete(eventName, ownerName, appName, (error, data, response) => {
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
 **eventName** | **String**| The id of the event. | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## analyticsEventsDeleteLogs

> analyticsEventsDeleteLogs(eventName, ownerName, appName)



Delete the set of Events with the specified event names.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AnalyticsApi();
let eventName = "eventName_example"; // String | The id of the event.
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.analyticsEventsDeleteLogs(eventName, ownerName, appName, (error, data, response) => {
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
 **eventName** | **String**| The id of the event. | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## analyticsGenericLogFlow

> AnalyticsGenericLogFlow200Response analyticsGenericLogFlow(ownerName, appName, opts)



Logs received between the specified start time and the current time. The API will return a maximum of 100 logs per call.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AnalyticsApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'start': new Date("2013-10-20T19:20:30+01:00") // Date | Start date time in data in ISO 8601 date time format. It must be within the current day in the UTC timezone. The default value is the start time of the current day in UTC timezone.
};
apiInstance.analyticsGenericLogFlow(ownerName, appName, opts, (error, data, response) => {
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
 **start** | **Date**| Start date time in data in ISO 8601 date time format. It must be within the current day in the UTC timezone. The default value is the start time of the current day in UTC timezone. | [optional] 

### Return type

[**AnalyticsGenericLogFlow200Response**](AnalyticsGenericLogFlow200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## analyticsGetAudience

> AnalyticsGetAudience200Response analyticsGetAudience(audienceName, ownerName, appName)



Gets audience definition.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AnalyticsApi();
let audienceName = "audienceName_example"; // String | The name of the audience
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.analyticsGetAudience(audienceName, ownerName, appName, (error, data, response) => {
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
 **audienceName** | **String**| The name of the audience | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

[**AnalyticsGetAudience200Response**](AnalyticsGetAudience200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## analyticsLanguageCounts

> AnalyticsLanguageCounts200Response analyticsLanguageCounts(start, ownerName, appName, opts)



Languages in the time range.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AnalyticsApi();
let start = new Date("2013-10-20T19:20:30+01:00"); // Date | Start date time in data in ISO 8601 date time format.
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'end': new Date("2013-10-20T19:20:30+01:00"), // Date | Last date time in data in ISO 8601 date time format.
  'top': 30, // Number | The maximum number of results to return. (0 will fetch all results)
  'versions': ["null"] // [String] | To select specific application versions
};
apiInstance.analyticsLanguageCounts(start, ownerName, appName, opts, (error, data, response) => {
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
 **start** | **Date**| Start date time in data in ISO 8601 date time format. | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **end** | **Date**| Last date time in data in ISO 8601 date time format. | [optional] 
 **top** | **Number**| The maximum number of results to return. (0 will fetch all results) | [optional] [default to 30]
 **versions** | [**[String]**](String.md)| To select specific application versions | [optional] 

### Return type

[**AnalyticsLanguageCounts200Response**](AnalyticsLanguageCounts200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## analyticsListAudiences

> AnalyticsListAudiences200Response analyticsListAudiences(ownerName, appName, opts)



Get list of audiences.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AnalyticsApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'includeDisabled': true // Boolean | Include disabled audience definitions
};
apiInstance.analyticsListAudiences(ownerName, appName, opts, (error, data, response) => {
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
 **includeDisabled** | **Boolean**| Include disabled audience definitions | [optional] 

### Return type

[**AnalyticsListAudiences200Response**](AnalyticsListAudiences200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## analyticsListCustomProperties

> AnalyticsListCustomProperties200Response analyticsListCustomProperties(ownerName, appName)



Get list of custom properties.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AnalyticsApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.analyticsListCustomProperties(ownerName, appName, (error, data, response) => {
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

[**AnalyticsListCustomProperties200Response**](AnalyticsListCustomProperties200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## analyticsListDeviceProperties

> AnalyticsListCustomProperties200Response analyticsListDeviceProperties(ownerName, appName)



Get list of device properties.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AnalyticsApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.analyticsListDeviceProperties(ownerName, appName, (error, data, response) => {
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

[**AnalyticsListCustomProperties200Response**](AnalyticsListCustomProperties200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## analyticsListDevicePropertyValues

> AnalyticsListDevicePropertyValues200Response analyticsListDevicePropertyValues(propertyName, ownerName, appName, opts)



Get list of device property values.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AnalyticsApi();
let propertyName = "propertyName_example"; // String | Device property
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'contains': "contains_example" // String | Contains string
};
apiInstance.analyticsListDevicePropertyValues(propertyName, ownerName, appName, opts, (error, data, response) => {
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
 **propertyName** | **String**| Device property | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **contains** | **String**| Contains string | [optional] 

### Return type

[**AnalyticsListDevicePropertyValues200Response**](AnalyticsListDevicePropertyValues200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## analyticsLogFlow

> AnalyticsLogFlow200Response analyticsLogFlow(ownerName, appName, opts)



Logs received between the specified start time and the current time. The API will return a maximum of 100 logs per call.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AnalyticsApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'start': new Date("2013-10-20T19:20:30+01:00") // Date | Start date time in data in ISO 8601 date time format. It must be within the current day in the UTC timezone. The default value is the start time of the current day in UTC timezone.
};
apiInstance.analyticsLogFlow(ownerName, appName, opts, (error, data, response) => {
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
 **start** | **Date**| Start date time in data in ISO 8601 date time format. It must be within the current day in the UTC timezone. The default value is the start time of the current day in UTC timezone. | [optional] 

### Return type

[**AnalyticsLogFlow200Response**](AnalyticsLogFlow200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## analyticsModelCounts

> AnalyticsModelCounts200Response analyticsModelCounts(start, ownerName, appName, opts)



Models in the time range.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AnalyticsApi();
let start = new Date("2013-10-20T19:20:30+01:00"); // Date | Start date time in data in ISO 8601 date time format.
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'end': new Date("2013-10-20T19:20:30+01:00"), // Date | Last date time in data in ISO 8601 date time format.
  'top': 30, // Number | The maximum number of results to return. (0 will fetch all results)
  'versions': ["null"] // [String] | To select specific application versions
};
apiInstance.analyticsModelCounts(start, ownerName, appName, opts, (error, data, response) => {
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
 **start** | **Date**| Start date time in data in ISO 8601 date time format. | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **end** | **Date**| Last date time in data in ISO 8601 date time format. | [optional] 
 **top** | **Number**| The maximum number of results to return. (0 will fetch all results) | [optional] [default to 30]
 **versions** | [**[String]**](String.md)| To select specific application versions | [optional] 

### Return type

[**AnalyticsModelCounts200Response**](AnalyticsModelCounts200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## analyticsOperatingSystemCounts

> AnalyticsOperatingSystemCounts200Response analyticsOperatingSystemCounts(start, ownerName, appName, opts)



OSes in the time range.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AnalyticsApi();
let start = new Date("2013-10-20T19:20:30+01:00"); // Date | Start date time in data in ISO 8601 date time format.
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'end': new Date("2013-10-20T19:20:30+01:00"), // Date | Last date time in data in ISO 8601 date time format.
  'top': 30, // Number | The maximum number of results to return. (0 will fetch all results)
  'versions': ["null"] // [String] | To select specific application versions
};
apiInstance.analyticsOperatingSystemCounts(start, ownerName, appName, opts, (error, data, response) => {
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
 **start** | **Date**| Start date time in data in ISO 8601 date time format. | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **end** | **Date**| Last date time in data in ISO 8601 date time format. | [optional] 
 **top** | **Number**| The maximum number of results to return. (0 will fetch all results) | [optional] [default to 30]
 **versions** | [**[String]**](String.md)| To select specific application versions | [optional] 

### Return type

[**AnalyticsOperatingSystemCounts200Response**](AnalyticsOperatingSystemCounts200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## analyticsPerDeviceCounts

> AnalyticsPerDeviceCounts200Response analyticsPerDeviceCounts(start, ownerName, appName, opts)



Count of sessions per device in the time range.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AnalyticsApi();
let start = new Date("2013-10-20T19:20:30+01:00"); // Date | Start date time in data in ISO 8601 date time format.
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'end': new Date("2013-10-20T19:20:30+01:00"), // Date | Last date time in data in ISO 8601 date time format.
  'versions': ["null"] // [String] | To select specific application versions
};
apiInstance.analyticsPerDeviceCounts(start, ownerName, appName, opts, (error, data, response) => {
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
 **start** | **Date**| Start date time in data in ISO 8601 date time format. | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **end** | **Date**| Last date time in data in ISO 8601 date time format. | [optional] 
 **versions** | [**[String]**](String.md)| To select specific application versions | [optional] 

### Return type

[**AnalyticsPerDeviceCounts200Response**](AnalyticsPerDeviceCounts200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## analyticsPlaceCounts

> AnalyticsPlaceCounts200Response analyticsPlaceCounts(start, ownerName, appName, opts)



Places in the time range.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AnalyticsApi();
let start = new Date("2013-10-20T19:20:30+01:00"); // Date | Start date time in data in ISO 8601 date time format.
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'end': new Date("2013-10-20T19:20:30+01:00"), // Date | Last date time in data in ISO 8601 date time format.
  'top': 30, // Number | The maximum number of results to return. (0 will fetch all results)
  'versions': ["null"] // [String] | To select specific application versions
};
apiInstance.analyticsPlaceCounts(start, ownerName, appName, opts, (error, data, response) => {
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
 **start** | **Date**| Start date time in data in ISO 8601 date time format. | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **end** | **Date**| Last date time in data in ISO 8601 date time format. | [optional] 
 **top** | **Number**| The maximum number of results to return. (0 will fetch all results) | [optional] [default to 30]
 **versions** | [**[String]**](String.md)| To select specific application versions | [optional] 

### Return type

[**AnalyticsPlaceCounts200Response**](AnalyticsPlaceCounts200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## analyticsSessionCounts

> [AnalyticsDeviceCounts200ResponseDailyInner] analyticsSessionCounts(start, ownerName, appName, opts)



Count of sessions in the time range.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AnalyticsApi();
let start = new Date("2013-10-20T19:20:30+01:00"); // Date | Start date time in data in ISO 8601 date time format.
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'end': new Date("2013-10-20T19:20:30+01:00"), // Date | Last date time in data in ISO 8601 date time format.
  'versions': ["null"] // [String] | To select specific application versions
};
apiInstance.analyticsSessionCounts(start, ownerName, appName, opts, (error, data, response) => {
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
 **start** | **Date**| Start date time in data in ISO 8601 date time format. | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **end** | **Date**| Last date time in data in ISO 8601 date time format. | [optional] 
 **versions** | [**[String]**](String.md)| To select specific application versions | [optional] 

### Return type

[**[AnalyticsDeviceCounts200ResponseDailyInner]**](AnalyticsDeviceCounts200ResponseDailyInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## analyticsSessionDurationsDistribution

> AnalyticsSessionDurationsDistribution200Response analyticsSessionDurationsDistribution(start, ownerName, appName, opts)



Gets session duration.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AnalyticsApi();
let start = new Date("2013-10-20T19:20:30+01:00"); // Date | Start date time in data in ISO 8601 date time format.
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'end': new Date("2013-10-20T19:20:30+01:00"), // Date | Last date time in data in ISO 8601 date time format.
  'versions': ["null"] // [String] | To select specific application versions
};
apiInstance.analyticsSessionDurationsDistribution(start, ownerName, appName, opts, (error, data, response) => {
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
 **start** | **Date**| Start date time in data in ISO 8601 date time format. | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **end** | **Date**| Last date time in data in ISO 8601 date time format. | [optional] 
 **versions** | [**[String]**](String.md)| To select specific application versions | [optional] 

### Return type

[**AnalyticsSessionDurationsDistribution200Response**](AnalyticsSessionDurationsDistribution200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## analyticsTestAudience

> AnalyticsTestAudience200Response analyticsTestAudience(ownerName, appName, analyticsTestAudienceRequest)



Tests audience definition.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AnalyticsApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let analyticsTestAudienceRequest = new AppCenterClient.AnalyticsTestAudienceRequest(); // AnalyticsTestAudienceRequest | Audience definition
apiInstance.analyticsTestAudience(ownerName, appName, analyticsTestAudienceRequest, (error, data, response) => {
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
 **analyticsTestAudienceRequest** | [**AnalyticsTestAudienceRequest**](AnalyticsTestAudienceRequest.md)| Audience definition | 

### Return type

[**AnalyticsTestAudience200Response**](AnalyticsTestAudience200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## analyticsVersions

> AnalyticsVersions200Response analyticsVersions(start, ownerName, appName, opts)



Count of active versions in the time range ordered by version.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AnalyticsApi();
let start = new Date("2013-10-20T19:20:30+01:00"); // Date | Start date time in data in ISO 8601 date time format.
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'end': new Date("2013-10-20T19:20:30+01:00"), // Date | Last date time in data in ISO 8601 date time format.
  'top': 30, // Number | The maximum number of results to return. (0 will fetch all results)
  'versions': ["null"] // [String] | To select specific application versions
};
apiInstance.analyticsVersions(start, ownerName, appName, opts, (error, data, response) => {
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
 **start** | **Date**| Start date time in data in ISO 8601 date time format. | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **end** | **Date**| Last date time in data in ISO 8601 date time format. | [optional] 
 **top** | **Number**| The maximum number of results to return. (0 will fetch all results) | [optional] [default to 30]
 **versions** | [**[String]**](String.md)| To select specific application versions | [optional] 

### Return type

[**AnalyticsVersions200Response**](AnalyticsVersions200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appBlockLogs

> String appBlockLogs(ownerName, appName)



**Warning, this operation is not reversible.**   A successful call to this API will permanently stop ingesting any logs received via SDK by app_id, and cannot be restored. We advise caution when using this API, it is designed to permanently disable an app_id. 

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AnalyticsApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.appBlockLogs(ownerName, appName, (error, data, response) => {
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

**String**

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## crashesListSessionLogs

> CrashesListSessionLogs200Response crashesListSessionLogs(crashId, ownerName, appName, opts)



Get session logs by crash ID

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AnalyticsApi();
let crashId = "crashId_example"; // String | The id of the a crash
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'date': new Date("2013-10-20T19:20:30+01:00") // Date | Date of data requested
};
apiInstance.crashesListSessionLogs(crashId, ownerName, appName, opts, (error, data, response) => {
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
 **crashId** | **String**| The id of the a crash | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **date** | **Date**| Date of data requested | [optional] 

### Return type

[**CrashesListSessionLogs200Response**](CrashesListSessionLogs200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## devicesBlockLogs

> String devicesBlockLogs(installId, ownerName, appName)



**Warning, this operation is not reversible.**   A successful call to this API will permanently stop ingesting any logs received via SDK for the given installation ID, and cannot be restored. We advise caution when using this API, it is designed to permanently disable collection from a specific installation of the app on a device, usually following the request from a user. 

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AnalyticsApi();
let installId = "installId_example"; // String | The id of the device
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.devicesBlockLogs(installId, ownerName, appName, (error, data, response) => {
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
 **installId** | **String**| The id of the device | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

**String**

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

