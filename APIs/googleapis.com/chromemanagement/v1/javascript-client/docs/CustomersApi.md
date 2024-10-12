# ChromeManagementApi.CustomersApi

All URIs are relative to *https://chromemanagement.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chromemanagementCustomersAppsCountChromeAppRequests**](CustomersApi.md#chromemanagementCustomersAppsCountChromeAppRequests) | **GET** /v1/{customer}/apps:countChromeAppRequests | 
[**chromemanagementCustomersReportsCountChromeBrowsersNeedingAttention**](CustomersApi.md#chromemanagementCustomersReportsCountChromeBrowsersNeedingAttention) | **GET** /v1/{customer}/reports:countChromeBrowsersNeedingAttention | 
[**chromemanagementCustomersReportsCountChromeDevicesReachingAutoExpirationDate**](CustomersApi.md#chromemanagementCustomersReportsCountChromeDevicesReachingAutoExpirationDate) | **GET** /v1/{customer}/reports:countChromeDevicesReachingAutoExpirationDate | 
[**chromemanagementCustomersReportsCountChromeDevicesThatNeedAttention**](CustomersApi.md#chromemanagementCustomersReportsCountChromeDevicesThatNeedAttention) | **GET** /v1/{customer}/reports:countChromeDevicesThatNeedAttention | 
[**chromemanagementCustomersReportsCountChromeHardwareFleetDevices**](CustomersApi.md#chromemanagementCustomersReportsCountChromeHardwareFleetDevices) | **GET** /v1/{customer}/reports:countChromeHardwareFleetDevices | 
[**chromemanagementCustomersReportsCountChromeVersions**](CustomersApi.md#chromemanagementCustomersReportsCountChromeVersions) | **GET** /v1/{customer}/reports:countChromeVersions | 
[**chromemanagementCustomersReportsCountInstalledApps**](CustomersApi.md#chromemanagementCustomersReportsCountInstalledApps) | **GET** /v1/{customer}/reports:countInstalledApps | 
[**chromemanagementCustomersReportsCountPrintJobsByPrinter**](CustomersApi.md#chromemanagementCustomersReportsCountPrintJobsByPrinter) | **GET** /v1/{customer}/reports:countPrintJobsByPrinter | 
[**chromemanagementCustomersReportsCountPrintJobsByUser**](CustomersApi.md#chromemanagementCustomersReportsCountPrintJobsByUser) | **GET** /v1/{customer}/reports:countPrintJobsByUser | 
[**chromemanagementCustomersReportsEnumeratePrintJobs**](CustomersApi.md#chromemanagementCustomersReportsEnumeratePrintJobs) | **GET** /v1/{customer}/reports:enumeratePrintJobs | 
[**chromemanagementCustomersReportsFindInstalledAppDevices**](CustomersApi.md#chromemanagementCustomersReportsFindInstalledAppDevices) | **GET** /v1/{customer}/reports:findInstalledAppDevices | 
[**chromemanagementCustomersTelemetryDevicesList**](CustomersApi.md#chromemanagementCustomersTelemetryDevicesList) | **GET** /v1/{parent}/telemetry/devices | 
[**chromemanagementCustomersTelemetryEventsList**](CustomersApi.md#chromemanagementCustomersTelemetryEventsList) | **GET** /v1/{parent}/telemetry/events | 
[**chromemanagementCustomersTelemetryNotificationConfigsCreate**](CustomersApi.md#chromemanagementCustomersTelemetryNotificationConfigsCreate) | **POST** /v1/{parent}/telemetry/notificationConfigs | 
[**chromemanagementCustomersTelemetryNotificationConfigsDelete**](CustomersApi.md#chromemanagementCustomersTelemetryNotificationConfigsDelete) | **DELETE** /v1/{name} | 
[**chromemanagementCustomersTelemetryNotificationConfigsList**](CustomersApi.md#chromemanagementCustomersTelemetryNotificationConfigsList) | **GET** /v1/{parent}/telemetry/notificationConfigs | 
[**chromemanagementCustomersTelemetryUsersGet**](CustomersApi.md#chromemanagementCustomersTelemetryUsersGet) | **GET** /v1/{name} | 
[**chromemanagementCustomersTelemetryUsersList**](CustomersApi.md#chromemanagementCustomersTelemetryUsersList) | **GET** /v1/{parent}/telemetry/users | 



## chromemanagementCustomersAppsCountChromeAppRequests

> GoogleChromeManagementV1CountChromeAppRequestsResponse chromemanagementCustomersAppsCountChromeAppRequests(customer, opts)



Generate summary of app installation requests.

### Example

```javascript
import ChromeManagementApi from 'chrome_management_api';
let defaultClient = ChromeManagementApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ChromeManagementApi.CustomersApi();
let customer = "customer_example"; // String | Required. Customer id or \"my_customer\" to use the customer associated to the account making the request.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'orderBy': "orderBy_example", // String | Field used to order results. Supported fields: * request_count * latest_request_time
  'orgUnitId': "orgUnitId_example", // String | The ID of the organizational unit.
  'pageSize': 56, // Number | Maximum number of results to return. Maximum and default are 50, anything above will be coerced to 50.
  'pageToken': "pageToken_example" // String | Token to specify the page of the request to be returned.
};
apiInstance.chromemanagementCustomersAppsCountChromeAppRequests(customer, opts, (error, data, response) => {
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
 **customer** | **String**| Required. Customer id or \&quot;my_customer\&quot; to use the customer associated to the account making the request. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **orderBy** | **String**| Field used to order results. Supported fields: * request_count * latest_request_time | [optional] 
 **orgUnitId** | **String**| The ID of the organizational unit. | [optional] 
 **pageSize** | **Number**| Maximum number of results to return. Maximum and default are 50, anything above will be coerced to 50. | [optional] 
 **pageToken** | **String**| Token to specify the page of the request to be returned. | [optional] 

### Return type

[**GoogleChromeManagementV1CountChromeAppRequestsResponse**](GoogleChromeManagementV1CountChromeAppRequestsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## chromemanagementCustomersReportsCountChromeBrowsersNeedingAttention

> GoogleChromeManagementV1CountChromeBrowsersNeedingAttentionResponse chromemanagementCustomersReportsCountChromeBrowsersNeedingAttention(customer, opts)



Count of Chrome Browsers that have been recently enrolled, have new policy to be synced, or have no recent activity.

### Example

```javascript
import ChromeManagementApi from 'chrome_management_api';
let defaultClient = ChromeManagementApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ChromeManagementApi.CustomersApi();
let customer = "customer_example"; // String | Required. The customer ID or \"my_customer\" prefixed with \"customers/\".
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'orgUnitId': "orgUnitId_example" // String | Optional. The ID of the organizational unit. If omitted, all data will be returned.
};
apiInstance.chromemanagementCustomersReportsCountChromeBrowsersNeedingAttention(customer, opts, (error, data, response) => {
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
 **customer** | **String**| Required. The customer ID or \&quot;my_customer\&quot; prefixed with \&quot;customers/\&quot;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **orgUnitId** | **String**| Optional. The ID of the organizational unit. If omitted, all data will be returned. | [optional] 

### Return type

[**GoogleChromeManagementV1CountChromeBrowsersNeedingAttentionResponse**](GoogleChromeManagementV1CountChromeBrowsersNeedingAttentionResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## chromemanagementCustomersReportsCountChromeDevicesReachingAutoExpirationDate

> GoogleChromeManagementV1CountChromeDevicesReachingAutoExpirationDateResponse chromemanagementCustomersReportsCountChromeDevicesReachingAutoExpirationDate(customer, opts)



Generate report of the number of devices expiring in each month of the selected time frame. Devices are grouped by auto update expiration date and model. Further information can be found [here](https://support.google.com/chrome/a/answer/10564947).

### Example

```javascript
import ChromeManagementApi from 'chrome_management_api';
let defaultClient = ChromeManagementApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ChromeManagementApi.CustomersApi();
let customer = "customer_example"; // String | Required. The customer ID or \"my_customer\" prefixed with \"customers/\".
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'maxAueDate': "maxAueDate_example", // String | Optional. Maximum expiration date in format yyyy-mm-dd in UTC timezone. If included returns all devices that have already expired and devices with auto expiration date equal to or earlier than the maximum date.
  'minAueDate': "minAueDate_example", // String | Optional. Maximum expiration date in format yyyy-mm-dd in UTC timezone. If included returns all devices that have already expired and devices with auto expiration date equal to or later than the minimum date.
  'orgUnitId': "orgUnitId_example" // String | Optional. The organizational unit ID, if omitted, will return data for all organizational units.
};
apiInstance.chromemanagementCustomersReportsCountChromeDevicesReachingAutoExpirationDate(customer, opts, (error, data, response) => {
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
 **customer** | **String**| Required. The customer ID or \&quot;my_customer\&quot; prefixed with \&quot;customers/\&quot;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **maxAueDate** | **String**| Optional. Maximum expiration date in format yyyy-mm-dd in UTC timezone. If included returns all devices that have already expired and devices with auto expiration date equal to or earlier than the maximum date. | [optional] 
 **minAueDate** | **String**| Optional. Maximum expiration date in format yyyy-mm-dd in UTC timezone. If included returns all devices that have already expired and devices with auto expiration date equal to or later than the minimum date. | [optional] 
 **orgUnitId** | **String**| Optional. The organizational unit ID, if omitted, will return data for all organizational units. | [optional] 

### Return type

[**GoogleChromeManagementV1CountChromeDevicesReachingAutoExpirationDateResponse**](GoogleChromeManagementV1CountChromeDevicesReachingAutoExpirationDateResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## chromemanagementCustomersReportsCountChromeDevicesThatNeedAttention

> GoogleChromeManagementV1CountChromeDevicesThatNeedAttentionResponse chromemanagementCustomersReportsCountChromeDevicesThatNeedAttention(customer, opts)



Counts of ChromeOS devices that have not synced policies or have lacked user activity in the past 28 days, are out of date, or are not complaint. Further information can be found here https://support.google.com/chrome/a/answer/10564947

### Example

```javascript
import ChromeManagementApi from 'chrome_management_api';
let defaultClient = ChromeManagementApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ChromeManagementApi.CustomersApi();
let customer = "customer_example"; // String | Required. The customer ID or \"my_customer\" prefixed with \"customers/\".
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'orgUnitId': "orgUnitId_example", // String | Optional. The ID of the organizational unit. If omitted, all data will be returned.
  'readMask': "readMask_example" // String | Required. Mask of the fields that should be populated in the returned report.
};
apiInstance.chromemanagementCustomersReportsCountChromeDevicesThatNeedAttention(customer, opts, (error, data, response) => {
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
 **customer** | **String**| Required. The customer ID or \&quot;my_customer\&quot; prefixed with \&quot;customers/\&quot;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **orgUnitId** | **String**| Optional. The ID of the organizational unit. If omitted, all data will be returned. | [optional] 
 **readMask** | **String**| Required. Mask of the fields that should be populated in the returned report. | [optional] 

### Return type

[**GoogleChromeManagementV1CountChromeDevicesThatNeedAttentionResponse**](GoogleChromeManagementV1CountChromeDevicesThatNeedAttentionResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## chromemanagementCustomersReportsCountChromeHardwareFleetDevices

> GoogleChromeManagementV1CountChromeHardwareFleetDevicesResponse chromemanagementCustomersReportsCountChromeHardwareFleetDevices(customer, opts)



Counts of devices with a specific hardware specification from the requested hardware type (for example model name, processor type). Further information can be found here https://support.google.com/chrome/a/answer/10564947

### Example

```javascript
import ChromeManagementApi from 'chrome_management_api';
let defaultClient = ChromeManagementApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ChromeManagementApi.CustomersApi();
let customer = "customer_example"; // String | Required. The customer ID or \"my_customer\".
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'orgUnitId': "orgUnitId_example", // String | Optional. The ID of the organizational unit. If omitted, all data will be returned.
  'readMask': "readMask_example" // String | Required. Mask of the fields that should be populated in the returned report.
};
apiInstance.chromemanagementCustomersReportsCountChromeHardwareFleetDevices(customer, opts, (error, data, response) => {
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
 **customer** | **String**| Required. The customer ID or \&quot;my_customer\&quot;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **orgUnitId** | **String**| Optional. The ID of the organizational unit. If omitted, all data will be returned. | [optional] 
 **readMask** | **String**| Required. Mask of the fields that should be populated in the returned report. | [optional] 

### Return type

[**GoogleChromeManagementV1CountChromeHardwareFleetDevicesResponse**](GoogleChromeManagementV1CountChromeHardwareFleetDevicesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## chromemanagementCustomersReportsCountChromeVersions

> GoogleChromeManagementV1CountChromeVersionsResponse chromemanagementCustomersReportsCountChromeVersions(customer, opts)



Generate report of installed Chrome versions.

### Example

```javascript
import ChromeManagementApi from 'chrome_management_api';
let defaultClient = ChromeManagementApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ChromeManagementApi.CustomersApi();
let customer = "customer_example"; // String | Required. Customer id or \"my_customer\" to use the customer associated to the account making the request.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'filter': "filter_example", // String | Query string to filter results, AND-separated fields in EBNF syntax. Note: OR operations are not supported in this filter. Supported filter fields: * last_active_date
  'orgUnitId': "orgUnitId_example", // String | The ID of the organizational unit.
  'pageSize': 56, // Number | Maximum number of results to return. Maximum and default are 100.
  'pageToken': "pageToken_example" // String | Token to specify the page of the request to be returned.
};
apiInstance.chromemanagementCustomersReportsCountChromeVersions(customer, opts, (error, data, response) => {
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
 **customer** | **String**| Required. Customer id or \&quot;my_customer\&quot; to use the customer associated to the account making the request. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **filter** | **String**| Query string to filter results, AND-separated fields in EBNF syntax. Note: OR operations are not supported in this filter. Supported filter fields: * last_active_date | [optional] 
 **orgUnitId** | **String**| The ID of the organizational unit. | [optional] 
 **pageSize** | **Number**| Maximum number of results to return. Maximum and default are 100. | [optional] 
 **pageToken** | **String**| Token to specify the page of the request to be returned. | [optional] 

### Return type

[**GoogleChromeManagementV1CountChromeVersionsResponse**](GoogleChromeManagementV1CountChromeVersionsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## chromemanagementCustomersReportsCountInstalledApps

> GoogleChromeManagementV1CountInstalledAppsResponse chromemanagementCustomersReportsCountInstalledApps(customer, opts)



Generate report of app installations.

### Example

```javascript
import ChromeManagementApi from 'chrome_management_api';
let defaultClient = ChromeManagementApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ChromeManagementApi.CustomersApi();
let customer = "customer_example"; // String | Required. Customer id or \"my_customer\" to use the customer associated to the account making the request.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'filter': "filter_example", // String | Query string to filter results, AND-separated fields in EBNF syntax. Note: OR operations are not supported in this filter. Supported filter fields: * app_name * app_type * install_type * number_of_permissions * total_install_count * latest_profile_active_date * permission_name * app_id
  'orderBy': "orderBy_example", // String | Field used to order results. Supported order by fields: * app_name * app_type * install_type * number_of_permissions * total_install_count * app_id
  'orgUnitId': "orgUnitId_example", // String | The ID of the organizational unit.
  'pageSize': 56, // Number | Maximum number of results to return. Maximum and default are 100.
  'pageToken': "pageToken_example" // String | Token to specify the page of the request to be returned.
};
apiInstance.chromemanagementCustomersReportsCountInstalledApps(customer, opts, (error, data, response) => {
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
 **customer** | **String**| Required. Customer id or \&quot;my_customer\&quot; to use the customer associated to the account making the request. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **filter** | **String**| Query string to filter results, AND-separated fields in EBNF syntax. Note: OR operations are not supported in this filter. Supported filter fields: * app_name * app_type * install_type * number_of_permissions * total_install_count * latest_profile_active_date * permission_name * app_id | [optional] 
 **orderBy** | **String**| Field used to order results. Supported order by fields: * app_name * app_type * install_type * number_of_permissions * total_install_count * app_id | [optional] 
 **orgUnitId** | **String**| The ID of the organizational unit. | [optional] 
 **pageSize** | **Number**| Maximum number of results to return. Maximum and default are 100. | [optional] 
 **pageToken** | **String**| Token to specify the page of the request to be returned. | [optional] 

### Return type

[**GoogleChromeManagementV1CountInstalledAppsResponse**](GoogleChromeManagementV1CountInstalledAppsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## chromemanagementCustomersReportsCountPrintJobsByPrinter

> GoogleChromeManagementV1CountPrintJobsByPrinterResponse chromemanagementCustomersReportsCountPrintJobsByPrinter(customer, opts)



Get a summary of printing done by each printer.

### Example

```javascript
import ChromeManagementApi from 'chrome_management_api';
let defaultClient = ChromeManagementApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ChromeManagementApi.CustomersApi();
let customer = "customer_example"; // String | Required. Customer ID prefixed with \"customers/\" or \"customers/my_customer\" to use the customer associated to the account making the request.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'filter': "filter_example", // String | Query string to filter results, AND-separated fields in EBNF syntax. Note: OR operations are not supported in this filter. Note: Only >= and <= comparators are supported in this filter. Supported filter fields: * complete_time
  'orderBy': "orderBy_example", // String | Field used to order results. If omitted, results will be ordered in ascending order of the 'printer' field. Supported order_by fields: * printer * job_count * device_count * user_count
  'pageSize': 56, // Number | Maximum number of results to return. Maximum and default are 100.
  'pageToken': "pageToken_example", // String | Token to specify the page of the response to be returned.
  'printerOrgUnitId': "printerOrgUnitId_example" // String | The ID of the organizational unit for printers. If specified, only data for printers from the specified organizational unit will be returned. If omitted, data for printers from all organizational units will be returned.
};
apiInstance.chromemanagementCustomersReportsCountPrintJobsByPrinter(customer, opts, (error, data, response) => {
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
 **customer** | **String**| Required. Customer ID prefixed with \&quot;customers/\&quot; or \&quot;customers/my_customer\&quot; to use the customer associated to the account making the request. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **filter** | **String**| Query string to filter results, AND-separated fields in EBNF syntax. Note: OR operations are not supported in this filter. Note: Only &gt;&#x3D; and &lt;&#x3D; comparators are supported in this filter. Supported filter fields: * complete_time | [optional] 
 **orderBy** | **String**| Field used to order results. If omitted, results will be ordered in ascending order of the &#39;printer&#39; field. Supported order_by fields: * printer * job_count * device_count * user_count | [optional] 
 **pageSize** | **Number**| Maximum number of results to return. Maximum and default are 100. | [optional] 
 **pageToken** | **String**| Token to specify the page of the response to be returned. | [optional] 
 **printerOrgUnitId** | **String**| The ID of the organizational unit for printers. If specified, only data for printers from the specified organizational unit will be returned. If omitted, data for printers from all organizational units will be returned. | [optional] 

### Return type

[**GoogleChromeManagementV1CountPrintJobsByPrinterResponse**](GoogleChromeManagementV1CountPrintJobsByPrinterResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## chromemanagementCustomersReportsCountPrintJobsByUser

> GoogleChromeManagementV1CountPrintJobsByUserResponse chromemanagementCustomersReportsCountPrintJobsByUser(customer, opts)



Get a summary of printing done by each user.

### Example

```javascript
import ChromeManagementApi from 'chrome_management_api';
let defaultClient = ChromeManagementApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ChromeManagementApi.CustomersApi();
let customer = "customer_example"; // String | Required. Customer ID prefixed with \"customers/\" or \"customers/my_customer\" to use the customer associated to the account making the request.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'filter': "filter_example", // String | Query string to filter results, AND-separated fields in EBNF syntax. Note: OR operations are not supported in this filter. Note: Only >= and <= comparators are supported in this filter. Supported filter fields: * complete_time
  'orderBy': "orderBy_example", // String | Field used to order results. If omitted, results will be ordered in ascending order of the 'user_email' field. Supported order_by fields: * user_email * job_count * printer_count * device_count
  'pageSize': 56, // Number | Maximum number of results to return. Maximum and default are 100.
  'pageToken': "pageToken_example", // String | Token to specify the page of the response to be returned.
  'printerOrgUnitId': "printerOrgUnitId_example" // String | The ID of the organizational unit for printers. If specified, only print jobs initiated with printers from the specified organizational unit will be counted. If omitted, all print jobs will be counted.
};
apiInstance.chromemanagementCustomersReportsCountPrintJobsByUser(customer, opts, (error, data, response) => {
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
 **customer** | **String**| Required. Customer ID prefixed with \&quot;customers/\&quot; or \&quot;customers/my_customer\&quot; to use the customer associated to the account making the request. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **filter** | **String**| Query string to filter results, AND-separated fields in EBNF syntax. Note: OR operations are not supported in this filter. Note: Only &gt;&#x3D; and &lt;&#x3D; comparators are supported in this filter. Supported filter fields: * complete_time | [optional] 
 **orderBy** | **String**| Field used to order results. If omitted, results will be ordered in ascending order of the &#39;user_email&#39; field. Supported order_by fields: * user_email * job_count * printer_count * device_count | [optional] 
 **pageSize** | **Number**| Maximum number of results to return. Maximum and default are 100. | [optional] 
 **pageToken** | **String**| Token to specify the page of the response to be returned. | [optional] 
 **printerOrgUnitId** | **String**| The ID of the organizational unit for printers. If specified, only print jobs initiated with printers from the specified organizational unit will be counted. If omitted, all print jobs will be counted. | [optional] 

### Return type

[**GoogleChromeManagementV1CountPrintJobsByUserResponse**](GoogleChromeManagementV1CountPrintJobsByUserResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## chromemanagementCustomersReportsEnumeratePrintJobs

> GoogleChromeManagementV1EnumeratePrintJobsResponse chromemanagementCustomersReportsEnumeratePrintJobs(customer, opts)



Get a list of print jobs.

### Example

```javascript
import ChromeManagementApi from 'chrome_management_api';
let defaultClient = ChromeManagementApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ChromeManagementApi.CustomersApi();
let customer = "customer_example"; // String | Required. Customer ID prefixed with \"customers/\" or \"customers/my_customer\" to use the customer associated to the account making the request.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'filter': "filter_example", // String | Query string to filter results, AND-separated fields in EBNF syntax. Note: OR operations are not supported in this filter. Note: Only >= and <= comparators are supported for `complete_time`. Note: Only = comparator supported for `user_id` and `printer_id`. Supported filter fields: * complete_time * printer_id * user_id
  'orderBy': "orderBy_example", // String | Field used to order results. If not specified, results will be ordered in descending order of the `complete_time` field. Supported order by fields: * title * state * create_time * complete_time * document_page_count * color_mode * duplex_mode * printer * user_email
  'pageSize': 56, // Number | The number of print jobs in the page from 0 to 100 inclusive, if page_size is not specified or zero, the size will be 50.
  'pageToken': "pageToken_example", // String | A page token received from a previous `EnumeratePrintJobs` call. Provide this to retrieve the subsequent page. If omitted, the first page of results will be returned. When paginating, all other parameters provided to `EnumeratePrintJobs` must match the call that provided the page token.
  'printerOrgUnitId': "printerOrgUnitId_example" // String | The ID of the organizational unit for printers. If specified, only print jobs submitted to printers from the specified organizational unit will be returned.
};
apiInstance.chromemanagementCustomersReportsEnumeratePrintJobs(customer, opts, (error, data, response) => {
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
 **customer** | **String**| Required. Customer ID prefixed with \&quot;customers/\&quot; or \&quot;customers/my_customer\&quot; to use the customer associated to the account making the request. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **filter** | **String**| Query string to filter results, AND-separated fields in EBNF syntax. Note: OR operations are not supported in this filter. Note: Only &gt;&#x3D; and &lt;&#x3D; comparators are supported for &#x60;complete_time&#x60;. Note: Only &#x3D; comparator supported for &#x60;user_id&#x60; and &#x60;printer_id&#x60;. Supported filter fields: * complete_time * printer_id * user_id | [optional] 
 **orderBy** | **String**| Field used to order results. If not specified, results will be ordered in descending order of the &#x60;complete_time&#x60; field. Supported order by fields: * title * state * create_time * complete_time * document_page_count * color_mode * duplex_mode * printer * user_email | [optional] 
 **pageSize** | **Number**| The number of print jobs in the page from 0 to 100 inclusive, if page_size is not specified or zero, the size will be 50. | [optional] 
 **pageToken** | **String**| A page token received from a previous &#x60;EnumeratePrintJobs&#x60; call. Provide this to retrieve the subsequent page. If omitted, the first page of results will be returned. When paginating, all other parameters provided to &#x60;EnumeratePrintJobs&#x60; must match the call that provided the page token. | [optional] 
 **printerOrgUnitId** | **String**| The ID of the organizational unit for printers. If specified, only print jobs submitted to printers from the specified organizational unit will be returned. | [optional] 

### Return type

[**GoogleChromeManagementV1EnumeratePrintJobsResponse**](GoogleChromeManagementV1EnumeratePrintJobsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## chromemanagementCustomersReportsFindInstalledAppDevices

> GoogleChromeManagementV1FindInstalledAppDevicesResponse chromemanagementCustomersReportsFindInstalledAppDevices(customer, opts)



Generate report of managed Chrome browser devices that have a specified app installed.

### Example

```javascript
import ChromeManagementApi from 'chrome_management_api';
let defaultClient = ChromeManagementApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ChromeManagementApi.CustomersApi();
let customer = "customer_example"; // String | Required. Customer id or \"my_customer\" to use the customer associated to the account making the request.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'appId': "appId_example", // String | Unique identifier of the app. For Chrome apps and extensions, the 32-character id (e.g. ehoadneljpdggcbbknedodolkkjodefl). For Android apps, the package name (e.g. com.evernote).
  'appType': "appType_example", // String | Type of the app.
  'filter': "filter_example", // String | Query string to filter results, AND-separated fields in EBNF syntax. Note: OR operations are not supported in this filter. Supported filter fields: * last_active_date
  'orderBy': "orderBy_example", // String | Field used to order results. Supported order by fields: * machine * device_id
  'orgUnitId': "orgUnitId_example", // String | The ID of the organizational unit.
  'pageSize': 56, // Number | Maximum number of results to return. Maximum and default are 100.
  'pageToken': "pageToken_example" // String | Token to specify the page of the request to be returned.
};
apiInstance.chromemanagementCustomersReportsFindInstalledAppDevices(customer, opts, (error, data, response) => {
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
 **customer** | **String**| Required. Customer id or \&quot;my_customer\&quot; to use the customer associated to the account making the request. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **appId** | **String**| Unique identifier of the app. For Chrome apps and extensions, the 32-character id (e.g. ehoadneljpdggcbbknedodolkkjodefl). For Android apps, the package name (e.g. com.evernote). | [optional] 
 **appType** | **String**| Type of the app. | [optional] 
 **filter** | **String**| Query string to filter results, AND-separated fields in EBNF syntax. Note: OR operations are not supported in this filter. Supported filter fields: * last_active_date | [optional] 
 **orderBy** | **String**| Field used to order results. Supported order by fields: * machine * device_id | [optional] 
 **orgUnitId** | **String**| The ID of the organizational unit. | [optional] 
 **pageSize** | **Number**| Maximum number of results to return. Maximum and default are 100. | [optional] 
 **pageToken** | **String**| Token to specify the page of the request to be returned. | [optional] 

### Return type

[**GoogleChromeManagementV1FindInstalledAppDevicesResponse**](GoogleChromeManagementV1FindInstalledAppDevicesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## chromemanagementCustomersTelemetryDevicesList

> GoogleChromeManagementV1ListTelemetryDevicesResponse chromemanagementCustomersTelemetryDevicesList(parent, opts)



List all telemetry devices.

### Example

```javascript
import ChromeManagementApi from 'chrome_management_api';
let defaultClient = ChromeManagementApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ChromeManagementApi.CustomersApi();
let parent = "parent_example"; // String | Required. Customer id or \"my_customer\" to use the customer associated to the account making the request.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'filter': "filter_example", // String | Optional. Only include resources that match the filter. Supported filter fields: - org_unit_id - serial_number - device_id - reports_timestamp The \"reports_timestamp\" filter accepts either the Unix Epoch milliseconds format or the RFC3339 UTC \"Zulu\" format with nanosecond resolution and up to nine fractional digits. Both formats should be surrounded by simple double quotes. Examples: \"2014-10-02T15:01:23Z\", \"2014-10-02T15:01:23.045123456Z\", \"1679283943823\".
  'pageSize': 56, // Number | Maximum number of results to return. Default value is 100. Maximum value is 1000.
  'pageToken': "pageToken_example", // String | Token to specify next page in the list.
  'readMask': "readMask_example" // String | Required. Read mask to specify which fields to return.
};
apiInstance.chromemanagementCustomersTelemetryDevicesList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. Customer id or \&quot;my_customer\&quot; to use the customer associated to the account making the request. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **filter** | **String**| Optional. Only include resources that match the filter. Supported filter fields: - org_unit_id - serial_number - device_id - reports_timestamp The \&quot;reports_timestamp\&quot; filter accepts either the Unix Epoch milliseconds format or the RFC3339 UTC \&quot;Zulu\&quot; format with nanosecond resolution and up to nine fractional digits. Both formats should be surrounded by simple double quotes. Examples: \&quot;2014-10-02T15:01:23Z\&quot;, \&quot;2014-10-02T15:01:23.045123456Z\&quot;, \&quot;1679283943823\&quot;. | [optional] 
 **pageSize** | **Number**| Maximum number of results to return. Default value is 100. Maximum value is 1000. | [optional] 
 **pageToken** | **String**| Token to specify next page in the list. | [optional] 
 **readMask** | **String**| Required. Read mask to specify which fields to return. | [optional] 

### Return type

[**GoogleChromeManagementV1ListTelemetryDevicesResponse**](GoogleChromeManagementV1ListTelemetryDevicesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## chromemanagementCustomersTelemetryEventsList

> GoogleChromeManagementV1ListTelemetryEventsResponse chromemanagementCustomersTelemetryEventsList(parent, opts)



List telemetry events.

### Example

```javascript
import ChromeManagementApi from 'chrome_management_api';
let defaultClient = ChromeManagementApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ChromeManagementApi.CustomersApi();
let parent = "parent_example"; // String | Required. Customer id or \"my_customer\" to use the customer associated to the account making the request.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'filter': "filter_example", // String | Optional. Only include resources that match the filter. Although this parameter is currently optional, this parameter will be required- please specify at least 1 event type. Supported filter fields: - device_id - user_id - device_org_unit_id - user_org_unit_id - timestamp - event_type The \"timestamp\" filter accepts either the Unix Epoch milliseconds format or the RFC3339 UTC \"Zulu\" format with nanosecond resolution and up to nine fractional digits. Both formats should be surrounded by simple double quotes. Examples: \"2014-10-02T15:01:23Z\", \"2014-10-02T15:01:23.045123456Z\", \"1679283943823\".
  'pageSize': 56, // Number | Optional. Maximum number of results to return. Default value is 100. Maximum value is 1000.
  'pageToken': "pageToken_example", // String | Optional. Token to specify next page in the list.
  'readMask': "readMask_example" // String | Required. Read mask to specify which fields to return. Although currently required, this field will become optional, while the filter parameter with an event type will be come required.
};
apiInstance.chromemanagementCustomersTelemetryEventsList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. Customer id or \&quot;my_customer\&quot; to use the customer associated to the account making the request. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **filter** | **String**| Optional. Only include resources that match the filter. Although this parameter is currently optional, this parameter will be required- please specify at least 1 event type. Supported filter fields: - device_id - user_id - device_org_unit_id - user_org_unit_id - timestamp - event_type The \&quot;timestamp\&quot; filter accepts either the Unix Epoch milliseconds format or the RFC3339 UTC \&quot;Zulu\&quot; format with nanosecond resolution and up to nine fractional digits. Both formats should be surrounded by simple double quotes. Examples: \&quot;2014-10-02T15:01:23Z\&quot;, \&quot;2014-10-02T15:01:23.045123456Z\&quot;, \&quot;1679283943823\&quot;. | [optional] 
 **pageSize** | **Number**| Optional. Maximum number of results to return. Default value is 100. Maximum value is 1000. | [optional] 
 **pageToken** | **String**| Optional. Token to specify next page in the list. | [optional] 
 **readMask** | **String**| Required. Read mask to specify which fields to return. Although currently required, this field will become optional, while the filter parameter with an event type will be come required. | [optional] 

### Return type

[**GoogleChromeManagementV1ListTelemetryEventsResponse**](GoogleChromeManagementV1ListTelemetryEventsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## chromemanagementCustomersTelemetryNotificationConfigsCreate

> GoogleChromeManagementV1TelemetryNotificationConfig chromemanagementCustomersTelemetryNotificationConfigsCreate(parent, opts)



Create a telemetry notification config.

### Example

```javascript
import ChromeManagementApi from 'chrome_management_api';
let defaultClient = ChromeManagementApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ChromeManagementApi.CustomersApi();
let parent = "parent_example"; // String | Required. The parent resource where this notification config will be created. Format: `customers/{customer}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleChromeManagementV1TelemetryNotificationConfig': new ChromeManagementApi.GoogleChromeManagementV1TelemetryNotificationConfig() // GoogleChromeManagementV1TelemetryNotificationConfig | 
};
apiInstance.chromemanagementCustomersTelemetryNotificationConfigsCreate(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The parent resource where this notification config will be created. Format: &#x60;customers/{customer}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleChromeManagementV1TelemetryNotificationConfig** | [**GoogleChromeManagementV1TelemetryNotificationConfig**](GoogleChromeManagementV1TelemetryNotificationConfig.md)|  | [optional] 

### Return type

[**GoogleChromeManagementV1TelemetryNotificationConfig**](GoogleChromeManagementV1TelemetryNotificationConfig.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## chromemanagementCustomersTelemetryNotificationConfigsDelete

> Object chromemanagementCustomersTelemetryNotificationConfigsDelete(name, opts)



Delete a telemetry notification config.

### Example

```javascript
import ChromeManagementApi from 'chrome_management_api';
let defaultClient = ChromeManagementApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ChromeManagementApi.CustomersApi();
let name = "name_example"; // String | Required. The name of the notification config to delete. Format: `customers/{customer}/telemetry/notificationConfigs/{notification_config}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example" // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
};
apiInstance.chromemanagementCustomersTelemetryNotificationConfigsDelete(name, opts, (error, data, response) => {
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
 **name** | **String**| Required. The name of the notification config to delete. Format: &#x60;customers/{customer}/telemetry/notificationConfigs/{notification_config}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 

### Return type

**Object**

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## chromemanagementCustomersTelemetryNotificationConfigsList

> GoogleChromeManagementV1ListTelemetryNotificationConfigsResponse chromemanagementCustomersTelemetryNotificationConfigsList(parent, opts)



List all telemetry notification configs.

### Example

```javascript
import ChromeManagementApi from 'chrome_management_api';
let defaultClient = ChromeManagementApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ChromeManagementApi.CustomersApi();
let parent = "parent_example"; // String | Required. The parent which owns the notification configs.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'pageSize': 56, // Number | The maximum number of notification configs to return. The service may return fewer than this value. If unspecified, at most 100 notification configs will be returned. The maximum value is 100; values above 100 will be coerced to 100.
  'pageToken': "pageToken_example" // String | A page token, received from a previous `ListTelemetryNotificationConfigs` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListTelemetryNotificationConfigs` must match the call that provided the page token.
};
apiInstance.chromemanagementCustomersTelemetryNotificationConfigsList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The parent which owns the notification configs. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **pageSize** | **Number**| The maximum number of notification configs to return. The service may return fewer than this value. If unspecified, at most 100 notification configs will be returned. The maximum value is 100; values above 100 will be coerced to 100. | [optional] 
 **pageToken** | **String**| A page token, received from a previous &#x60;ListTelemetryNotificationConfigs&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListTelemetryNotificationConfigs&#x60; must match the call that provided the page token. | [optional] 

### Return type

[**GoogleChromeManagementV1ListTelemetryNotificationConfigsResponse**](GoogleChromeManagementV1ListTelemetryNotificationConfigsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## chromemanagementCustomersTelemetryUsersGet

> GoogleChromeManagementV1TelemetryUser chromemanagementCustomersTelemetryUsersGet(name, opts)



Get telemetry user.

### Example

```javascript
import ChromeManagementApi from 'chrome_management_api';
let defaultClient = ChromeManagementApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ChromeManagementApi.CustomersApi();
let name = "name_example"; // String | Required. Name of the `TelemetryUser` to return.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'readMask': "readMask_example" // String | Read mask to specify which fields to return.
};
apiInstance.chromemanagementCustomersTelemetryUsersGet(name, opts, (error, data, response) => {
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
 **name** | **String**| Required. Name of the &#x60;TelemetryUser&#x60; to return. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **readMask** | **String**| Read mask to specify which fields to return. | [optional] 

### Return type

[**GoogleChromeManagementV1TelemetryUser**](GoogleChromeManagementV1TelemetryUser.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## chromemanagementCustomersTelemetryUsersList

> GoogleChromeManagementV1ListTelemetryUsersResponse chromemanagementCustomersTelemetryUsersList(parent, opts)



List all telemetry users.

### Example

```javascript
import ChromeManagementApi from 'chrome_management_api';
let defaultClient = ChromeManagementApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ChromeManagementApi.CustomersApi();
let parent = "parent_example"; // String | Required. Customer id or \"my_customer\" to use the customer associated to the account making the request.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'filter': "filter_example", // String | Only include resources that match the filter. Supported filter fields: - user_id - user_org_unit_id 
  'pageSize': 56, // Number | Maximum number of results to return. Default value is 100. Maximum value is 1000.
  'pageToken': "pageToken_example", // String | Token to specify next page in the list.
  'readMask': "readMask_example" // String | Read mask to specify which fields to return.
};
apiInstance.chromemanagementCustomersTelemetryUsersList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. Customer id or \&quot;my_customer\&quot; to use the customer associated to the account making the request. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **filter** | **String**| Only include resources that match the filter. Supported filter fields: - user_id - user_org_unit_id  | [optional] 
 **pageSize** | **Number**| Maximum number of results to return. Default value is 100. Maximum value is 1000. | [optional] 
 **pageToken** | **String**| Token to specify next page in the list. | [optional] 
 **readMask** | **String**| Read mask to specify which fields to return. | [optional] 

### Return type

[**GoogleChromeManagementV1ListTelemetryUsersResponse**](GoogleChromeManagementV1ListTelemetryUsersResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

