# AppCenterClient.CrashApi

All URIs are relative to *https://api.appcenter.ms*

Method | HTTP request | Description
------------- | ------------- | -------------
[**crashGroupsGet**](CrashApi.md#crashGroupsGet) | **GET** /v0.1/apps/{owner_name}/{app_name}/crash_groups/{crash_group_id} | 
[**crashGroupsGetStacktrace**](CrashApi.md#crashGroupsGetStacktrace) | **GET** /v0.1/apps/{owner_name}/{app_name}/crash_groups/{crash_group_id}/stacktrace | 
[**crashGroupsList**](CrashApi.md#crashGroupsList) | **GET** /v0.1/apps/{owner_name}/{app_name}/crash_groups | 
[**crashGroupsUpdate**](CrashApi.md#crashGroupsUpdate) | **PATCH** /v0.1/apps/{owner_name}/{app_name}/crash_groups/{crash_group_id} | 
[**crashesDelete**](CrashApi.md#crashesDelete) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/crash_groups/{crash_group_id}/crashes/{crash_id} | 
[**crashesGet**](CrashApi.md#crashesGet) | **GET** /v0.1/apps/{owner_name}/{app_name}/crash_groups/{crash_group_id}/crashes/{crash_id} | 
[**crashesGetAppCrashesInfo**](CrashApi.md#crashesGetAppCrashesInfo) | **GET** /v0.1/apps/{owner_name}/{app_name}/crashes_info | 
[**crashesGetAppVersions**](CrashApi.md#crashesGetAppVersions) | **GET** /v0.1/apps/{owner_name}/{app_name}/versions | 
[**crashesGetCrashAttachmentLocation**](CrashApi.md#crashesGetCrashAttachmentLocation) | **GET** /v0.1/apps/{owner_name}/{app_name}/crashes/{crash_id}/attachments/{attachment_id}/location | 
[**crashesGetCrashTextAttachmentContent**](CrashApi.md#crashesGetCrashTextAttachmentContent) | **GET** /v0.1/apps/{owner_name}/{app_name}/crashes/{crash_id}/attachments/{attachment_id}/text | 
[**crashesGetNativeCrash**](CrashApi.md#crashesGetNativeCrash) | **GET** /v0.1/apps/{owner_name}/{app_name}/crash_groups/{crash_group_id}/crashes/{crash_id}/native | 
[**crashesGetNativeCrashDownload**](CrashApi.md#crashesGetNativeCrashDownload) | **GET** /v0.1/apps/{owner_name}/{app_name}/crash_groups/{crash_group_id}/crashes/{crash_id}/native/download | 
[**crashesGetRawCrashLocation**](CrashApi.md#crashesGetRawCrashLocation) | **GET** /v0.1/apps/{owner_name}/{app_name}/crash_groups/{crash_group_id}/crashes/{crash_id}/raw/location | 
[**crashesGetStacktrace**](CrashApi.md#crashesGetStacktrace) | **GET** /v0.1/apps/{owner_name}/{app_name}/crash_groups/{crash_group_id}/crashes/{crash_id}/stacktrace | 
[**crashesList**](CrashApi.md#crashesList) | **GET** /v0.1/apps/{owner_name}/{app_name}/crash_groups/{crash_group_id}/crashes | 
[**crashesListAttachments**](CrashApi.md#crashesListAttachments) | **GET** /v0.1/apps/{owner_name}/{app_name}/crashes/{crash_id}/attachments | 
[**missingSymbolGroupsGet**](CrashApi.md#missingSymbolGroupsGet) | **GET** /v0.1/apps/{owner_name}/{app_name}/diagnostics/symbol_groups/{symbol_group_id} | Gets missing symbol crash group by its id
[**missingSymbolGroupsInfo**](CrashApi.md#missingSymbolGroupsInfo) | **GET** /v0.1/apps/{owner_name}/{app_name}/diagnostics/symbol_groups_info | Gets application level statistics for all missing symbol groups
[**missingSymbolGroupsList**](CrashApi.md#missingSymbolGroupsList) | **GET** /v0.1/apps/{owner_name}/{app_name}/diagnostics/symbol_groups | Gets top N (ordered by crash count) of crash groups by missing symbol
[**symbolUploadsComplete**](CrashApi.md#symbolUploadsComplete) | **PATCH** /v0.1/apps/{owner_name}/{app_name}/symbol_uploads/{symbol_upload_id} | 
[**symbolUploadsCreate**](CrashApi.md#symbolUploadsCreate) | **POST** /v0.1/apps/{owner_name}/{app_name}/symbol_uploads | 
[**symbolUploadsDelete**](CrashApi.md#symbolUploadsDelete) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/symbol_uploads/{symbol_upload_id} | 
[**symbolUploadsGet**](CrashApi.md#symbolUploadsGet) | **GET** /v0.1/apps/{owner_name}/{app_name}/symbol_uploads/{symbol_upload_id} | 
[**symbolUploadsGetLocation**](CrashApi.md#symbolUploadsGetLocation) | **GET** /v0.1/apps/{owner_name}/{app_name}/symbol_uploads/{symbol_upload_id}/location | 
[**symbolUploadsList**](CrashApi.md#symbolUploadsList) | **GET** /v0.1/apps/{owner_name}/{app_name}/symbol_uploads | 
[**symbolsGet**](CrashApi.md#symbolsGet) | **GET** /v0.1/apps/{owner_name}/{app_name}/symbols/{symbol_id} | 
[**symbolsGetLocation**](CrashApi.md#symbolsGetLocation) | **GET** /v0.1/apps/{owner_name}/{app_name}/symbols/{symbol_id}/location | 
[**symbolsGetStatus**](CrashApi.md#symbolsGetStatus) | **GET** /v0.1/apps/{owner_name}/{app_name}/symbols/{symbol_id}/status | 
[**symbolsIgnore**](CrashApi.md#symbolsIgnore) | **POST** /v0.1/apps/{owner_name}/{app_name}/symbols/{symbol_id}/ignore | 
[**symbolsList**](CrashApi.md#symbolsList) | **GET** /v0.1/apps/{owner_name}/{app_name}/symbols | 



## crashGroupsGet

> CrashGroupsList200ResponseCrashGroupsInner crashGroupsGet(crashGroupId, ownerName, appName)



Gets a specific group.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.CrashApi();
let crashGroupId = "crashGroupId_example"; // String | id of a specific group
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.crashGroupsGet(crashGroupId, ownerName, appName, (error, data, response) => {
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
 **crashGroupId** | **String**| id of a specific group | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

[**CrashGroupsList200ResponseCrashGroupsInner**](CrashGroupsList200ResponseCrashGroupsInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## crashGroupsGetStacktrace

> Stacktrace crashGroupsGetStacktrace(crashGroupId, ownerName, appName, opts)



Gets a stacktrace for a specific crash.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.CrashApi();
let crashGroupId = "crashGroupId_example"; // String | id of a specific group
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'groupingOnly': false // Boolean | true if the stacktrace should be only the relevant thread / exception. Default is false
};
apiInstance.crashGroupsGetStacktrace(crashGroupId, ownerName, appName, opts, (error, data, response) => {
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
 **crashGroupId** | **String**| id of a specific group | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **groupingOnly** | **Boolean**| true if the stacktrace should be only the relevant thread / exception. Default is false | [optional] [default to false]

### Return type

[**Stacktrace**](Stacktrace.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## crashGroupsList

> CrashGroupsList200Response crashGroupsList(ownerName, appName, opts)



Gets a list of crash groups and whether the list contains all available groups.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.CrashApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'lastOccurrenceFrom': new Date("2013-10-20T19:20:30+01:00"), // Date | Earliest date when the last time a crash occured in a crash group
  'lastOccurrenceTo': new Date("2013-10-20T19:20:30+01:00"), // Date | Latest date when the last time a crash occured in a crash group
  'appVersion': "appVersion_example", // String | version
  'groupType': "groupType_example", // String | 
  'groupStatus': "groupStatus_example", // String | 
  'groupTextSearch': "groupTextSearch_example", // String | A freetext search that matches in crash, crash types, crash stack_traces and crash user
  'orderby': "'last_occurrence desc'", // String | the OData-like $orderby argument
  'continuationToken': "continuationToken_example" // String | Cassandra request continuation token. The token is used for pagination.
};
apiInstance.crashGroupsList(ownerName, appName, opts, (error, data, response) => {
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
 **lastOccurrenceFrom** | **Date**| Earliest date when the last time a crash occured in a crash group | [optional] 
 **lastOccurrenceTo** | **Date**| Latest date when the last time a crash occured in a crash group | [optional] 
 **appVersion** | **String**| version | [optional] 
 **groupType** | **String**|  | [optional] 
 **groupStatus** | **String**|  | [optional] 
 **groupTextSearch** | **String**| A freetext search that matches in crash, crash types, crash stack_traces and crash user | [optional] 
 **orderby** | **String**| the OData-like $orderby argument | [optional] [default to &#39;last_occurrence desc&#39;]
 **continuationToken** | **String**| Cassandra request continuation token. The token is used for pagination. | [optional] 

### Return type

[**CrashGroupsList200Response**](CrashGroupsList200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## crashGroupsUpdate

> CrashGroupsList200ResponseCrashGroupsInner crashGroupsUpdate(crashGroupId, ownerName, appName, crashGroupsUpdateRequest)



Updates a group.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.CrashApi();
let crashGroupId = "crashGroupId_example"; // String | id of a specific group
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let crashGroupsUpdateRequest = new AppCenterClient.CrashGroupsUpdateRequest(); // CrashGroupsUpdateRequest | Group change object. All fields are optional and only provided fields will get updated.
apiInstance.crashGroupsUpdate(crashGroupId, ownerName, appName, crashGroupsUpdateRequest, (error, data, response) => {
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
 **crashGroupId** | **String**| id of a specific group | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **crashGroupsUpdateRequest** | [**CrashGroupsUpdateRequest**](CrashGroupsUpdateRequest.md)| Group change object. All fields are optional and only provided fields will get updated. | 

### Return type

[**CrashGroupsList200ResponseCrashGroupsInner**](CrashGroupsList200ResponseCrashGroupsInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## crashesDelete

> CrashesDelete200Response crashesDelete(crashGroupId, crashId, ownerName, appName, opts)



Delete a specific crash and related attachments and blobs for an app.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.CrashApi();
let crashGroupId = "crashGroupId_example"; // String | id of a specific group
let crashId = "crashId_example"; // String | id of a specific crash
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'retentionDelete': false // Boolean | true in that case if the method should skip update counts
};
apiInstance.crashesDelete(crashGroupId, crashId, ownerName, appName, opts, (error, data, response) => {
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
 **crashGroupId** | **String**| id of a specific group | 
 **crashId** | **String**| id of a specific crash | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **retentionDelete** | **Boolean**| true in that case if the method should skip update counts | [optional] [default to false]

### Return type

[**CrashesDelete200Response**](CrashesDelete200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## crashesGet

> Crash crashesGet(crashGroupId, crashId, ownerName, appName, opts)



Gets a specific crash for an app.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.CrashApi();
let crashGroupId = "crashGroupId_example"; // String | id of a specific group
let crashId = "crashId_example"; // String | id of a specific crash
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'includeReport': false, // Boolean | true if the crash should include the raw crash report. Default is false
  'includeLog': false, // Boolean | true if the crash should include the custom log report. Default is false
  'includeDetails': false, // Boolean | true if the crash should include in depth crash details
  'includeStacktrace': false, // Boolean | true if the crash should include the stacktrace information
  'groupingOnly': false // Boolean | true if the stacktrace should be only the relevant thread / exception. Default is false
};
apiInstance.crashesGet(crashGroupId, crashId, ownerName, appName, opts, (error, data, response) => {
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
 **crashGroupId** | **String**| id of a specific group | 
 **crashId** | **String**| id of a specific crash | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **includeReport** | **Boolean**| true if the crash should include the raw crash report. Default is false | [optional] [default to false]
 **includeLog** | **Boolean**| true if the crash should include the custom log report. Default is false | [optional] [default to false]
 **includeDetails** | **Boolean**| true if the crash should include in depth crash details | [optional] [default to false]
 **includeStacktrace** | **Boolean**| true if the crash should include the stacktrace information | [optional] [default to false]
 **groupingOnly** | **Boolean**| true if the stacktrace should be only the relevant thread / exception. Default is false | [optional] [default to false]

### Return type

[**Crash**](Crash.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## crashesGetAppCrashesInfo

> CrashesGetAppCrashesInfo200Response crashesGetAppCrashesInfo(ownerName, appName)



Gets whether the application has any crashes.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.CrashApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.crashesGetAppCrashesInfo(ownerName, appName, (error, data, response) => {
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

[**CrashesGetAppCrashesInfo200Response**](CrashesGetAppCrashesInfo200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## crashesGetAppVersions

> [CrashesGetAppVersions200ResponseInner] crashesGetAppVersions(ownerName, appName)



Gets a list of application versions.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.CrashApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.crashesGetAppVersions(ownerName, appName, (error, data, response) => {
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

[**[CrashesGetAppVersions200ResponseInner]**](CrashesGetAppVersions200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## crashesGetCrashAttachmentLocation

> CrashesGetCrashAttachmentLocation200Response crashesGetCrashAttachmentLocation(crashId, attachmentId, ownerName, appName)



Gets the URI location to download crash attachment.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.CrashApi();
let crashId = "crashId_example"; // String | id of a specific crash
let attachmentId = "attachmentId_example"; // String | attachment id
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.crashesGetCrashAttachmentLocation(crashId, attachmentId, ownerName, appName, (error, data, response) => {
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
 **crashId** | **String**| id of a specific crash | 
 **attachmentId** | **String**| attachment id | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

[**CrashesGetCrashAttachmentLocation200Response**](CrashesGetCrashAttachmentLocation200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## crashesGetCrashTextAttachmentContent

> String crashesGetCrashTextAttachmentContent(crashId, attachmentId, ownerName, appName)



Gets content of the text attachment.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.CrashApi();
let crashId = "crashId_example"; // String | id of a specific crash
let attachmentId = "attachmentId_example"; // String | attachment id
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.crashesGetCrashTextAttachmentContent(crashId, attachmentId, ownerName, appName, (error, data, response) => {
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
 **crashId** | **String**| id of a specific crash | 
 **attachmentId** | **String**| attachment id | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

**String**

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## crashesGetNativeCrash

> String crashesGetNativeCrash(crashGroupId, crashId, ownerName, appName)



Gets the native log of a specific crash.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.CrashApi();
let crashGroupId = "crashGroupId_example"; // String | id of a specific group
let crashId = "crashId_example"; // String | id of a specific crash
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.crashesGetNativeCrash(crashGroupId, crashId, ownerName, appName, (error, data, response) => {
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
 **crashGroupId** | **String**| id of a specific group | 
 **crashId** | **String**| id of a specific crash | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

**String**

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## crashesGetNativeCrashDownload

> String crashesGetNativeCrashDownload(crashGroupId, crashId, ownerName, appName)



Gets the native log of a specific crash as a text attachment.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.CrashApi();
let crashGroupId = "crashGroupId_example"; // String | id of a specific group
let crashId = "crashId_example"; // String | id of a specific crash
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.crashesGetNativeCrashDownload(crashGroupId, crashId, ownerName, appName, (error, data, response) => {
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
 **crashGroupId** | **String**| id of a specific group | 
 **crashId** | **String**| id of a specific crash | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

**String**

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## crashesGetRawCrashLocation

> CrashesGetRawCrashLocation200Response crashesGetRawCrashLocation(crashGroupId, crashId, ownerName, appName)



Gets the URI location to download json of a specific crash.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.CrashApi();
let crashGroupId = "crashGroupId_example"; // String | id of a specific group
let crashId = "crashId_example"; // String | id of a specific crash
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.crashesGetRawCrashLocation(crashGroupId, crashId, ownerName, appName, (error, data, response) => {
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
 **crashGroupId** | **String**| id of a specific group | 
 **crashId** | **String**| id of a specific crash | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

[**CrashesGetRawCrashLocation200Response**](CrashesGetRawCrashLocation200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## crashesGetStacktrace

> Stacktrace crashesGetStacktrace(crashGroupId, crashId, ownerName, appName, opts)



Gets a stacktrace for a specific crash.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.CrashApi();
let crashGroupId = "crashGroupId_example"; // String | id of a specific group
let crashId = "crashId_example"; // String | id of a specific crash
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'groupingOnly': false // Boolean | true if the stacktrace should be only the relevant thread / exception. Default is false
};
apiInstance.crashesGetStacktrace(crashGroupId, crashId, ownerName, appName, opts, (error, data, response) => {
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
 **crashGroupId** | **String**| id of a specific group | 
 **crashId** | **String**| id of a specific crash | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **groupingOnly** | **Boolean**| true if the stacktrace should be only the relevant thread / exception. Default is false | [optional] [default to false]

### Return type

[**Stacktrace**](Stacktrace.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## crashesList

> [Crash] crashesList(crashGroupId, ownerName, appName, opts)



Gets all crashes of a group.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.CrashApi();
let crashGroupId = "crashGroupId_example"; // String | id of a specific group
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'includeReport': false, // Boolean | true if the crash should include the raw crash report. Default is false
  'includeLog': false, // Boolean | true if the crash should include the custom log report. Default is false
  'dateFrom': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'dateTo': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'appVersion': "appVersion_example", // String | version
  'errorType': "errorType_example" // String | 
};
apiInstance.crashesList(crashGroupId, ownerName, appName, opts, (error, data, response) => {
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
 **crashGroupId** | **String**| id of a specific group | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **includeReport** | **Boolean**| true if the crash should include the raw crash report. Default is false | [optional] [default to false]
 **includeLog** | **Boolean**| true if the crash should include the custom log report. Default is false | [optional] [default to false]
 **dateFrom** | **Date**|  | [optional] 
 **dateTo** | **Date**|  | [optional] 
 **appVersion** | **String**| version | [optional] 
 **errorType** | **String**|  | [optional] 

### Return type

[**[Crash]**](Crash.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## crashesListAttachments

> [CrashesListAttachments200ResponseInner] crashesListAttachments(crashId, ownerName, appName)



Gets all attachments for a specific crash.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.CrashApi();
let crashId = "crashId_example"; // String | id of a specific crash
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.crashesListAttachments(crashId, ownerName, appName, (error, data, response) => {
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
 **crashId** | **String**| id of a specific crash | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

[**[CrashesListAttachments200ResponseInner]**](CrashesListAttachments200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## missingSymbolGroupsGet

> MissingSymbolGroupsList200Response missingSymbolGroupsGet(symbolGroupId, ownerName, appName)

Gets missing symbol crash group by its id

Gets missing symbol crash group by its id

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.CrashApi();
let symbolGroupId = "symbolGroupId_example"; // String | missing symbol crash group id
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.missingSymbolGroupsGet(symbolGroupId, ownerName, appName, (error, data, response) => {
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
 **symbolGroupId** | **String**| missing symbol crash group id | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

[**MissingSymbolGroupsList200Response**](MissingSymbolGroupsList200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## missingSymbolGroupsInfo

> MissingSymbolGroupsInfo200Response missingSymbolGroupsInfo(ownerName, appName)

Gets application level statistics for all missing symbol groups

Gets application level statistics for all missing symbol groups

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.CrashApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.missingSymbolGroupsInfo(ownerName, appName, (error, data, response) => {
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

[**MissingSymbolGroupsInfo200Response**](MissingSymbolGroupsInfo200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## missingSymbolGroupsList

> MissingSymbolGroupsList200Response missingSymbolGroupsList(top, ownerName, appName)

Gets top N (ordered by crash count) of crash groups by missing symbol

Gets top N (ordered by crash count) of crash groups by missing symbol

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.CrashApi();
let top = 56; // Number | top N elements
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.missingSymbolGroupsList(top, ownerName, appName, (error, data, response) => {
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
 **top** | **Number**| top N elements | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

[**MissingSymbolGroupsList200Response**](MissingSymbolGroupsList200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## symbolUploadsComplete

> SymbolUploadsList200ResponseInner symbolUploadsComplete(symbolUploadId, ownerName, appName, symbolUploadsCompleteRequest)



Commits or aborts the symbol upload process for a new set of symbols for the specified application

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.CrashApi();
let symbolUploadId = "symbolUploadId_example"; // String | The ID of the symbol upload
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let symbolUploadsCompleteRequest = new AppCenterClient.SymbolUploadsCompleteRequest(); // SymbolUploadsCompleteRequest | The symbol information
apiInstance.symbolUploadsComplete(symbolUploadId, ownerName, appName, symbolUploadsCompleteRequest, (error, data, response) => {
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
 **symbolUploadId** | **String**| The ID of the symbol upload | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **symbolUploadsCompleteRequest** | [**SymbolUploadsCompleteRequest**](SymbolUploadsCompleteRequest.md)| The symbol information | 

### Return type

[**SymbolUploadsList200ResponseInner**](SymbolUploadsList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## symbolUploadsCreate

> SymbolUploadsCreate200Response symbolUploadsCreate(ownerName, appName, symbolUploadsCreateRequest)



Begins the symbol upload process for a new set of symbols for the specified application

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.CrashApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let symbolUploadsCreateRequest = new AppCenterClient.SymbolUploadsCreateRequest(); // SymbolUploadsCreateRequest | The symbol information
apiInstance.symbolUploadsCreate(ownerName, appName, symbolUploadsCreateRequest, (error, data, response) => {
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
 **symbolUploadsCreateRequest** | [**SymbolUploadsCreateRequest**](SymbolUploadsCreateRequest.md)| The symbol information | 

### Return type

[**SymbolUploadsCreate200Response**](SymbolUploadsCreate200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## symbolUploadsDelete

> SymbolUploadsList200ResponseInner symbolUploadsDelete(symbolUploadId, ownerName, appName)



Deletes a symbol upload by id for the specified application

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.CrashApi();
let symbolUploadId = "symbolUploadId_example"; // String | The ID of the symbol upload
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.symbolUploadsDelete(symbolUploadId, ownerName, appName, (error, data, response) => {
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
 **symbolUploadId** | **String**| The ID of the symbol upload | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

[**SymbolUploadsList200ResponseInner**](SymbolUploadsList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## symbolUploadsGet

> SymbolUploadsList200ResponseInner symbolUploadsGet(symbolUploadId, ownerName, appName)



Gets a symbol upload by id for the specified application

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.CrashApi();
let symbolUploadId = "symbolUploadId_example"; // String | The ID of the symbol upload
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.symbolUploadsGet(symbolUploadId, ownerName, appName, (error, data, response) => {
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
 **symbolUploadId** | **String**| The ID of the symbol upload | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

[**SymbolUploadsList200ResponseInner**](SymbolUploadsList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## symbolUploadsGetLocation

> SymbolUploadsGetLocation200Response symbolUploadsGetLocation(symbolUploadId, ownerName, appName)



Gets the URL to download the symbol upload

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.CrashApi();
let symbolUploadId = "symbolUploadId_example"; // String | The ID of the symbol upload
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.symbolUploadsGetLocation(symbolUploadId, ownerName, appName, (error, data, response) => {
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
 **symbolUploadId** | **String**| The ID of the symbol upload | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

[**SymbolUploadsGetLocation200Response**](SymbolUploadsGetLocation200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## symbolUploadsList

> [SymbolUploadsList200ResponseInner] symbolUploadsList(ownerName, appName, opts)



Gets a list of all uploads for the specified application

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.CrashApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'top': 30, // Number | The maximum number of results to return.
  'status': "status_example", // String | Filter results by the current status of a symbol upload: * all: all states in the symbol upload process. Includes created, aborted, committed, processing, indexed and failed states * uploaded: all states after package is uploaded. Includes committed, processing, indexed and failed states * processed: symbol upload processing is completed. Includes indexed and failed states. 
  'symbolType': "symbolType_example" // String | The type of symbols
};
apiInstance.symbolUploadsList(ownerName, appName, opts, (error, data, response) => {
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
 **top** | **Number**| The maximum number of results to return. | [optional] [default to 30]
 **status** | **String**| Filter results by the current status of a symbol upload: * all: all states in the symbol upload process. Includes created, aborted, committed, processing, indexed and failed states * uploaded: all states after package is uploaded. Includes committed, processing, indexed and failed states * processed: symbol upload processing is completed. Includes indexed and failed states.  | [optional] 
 **symbolType** | **String**| The type of symbols | [optional] 

### Return type

[**[SymbolUploadsList200ResponseInner]**](SymbolUploadsList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## symbolsGet

> SymbolsList200ResponseInner symbolsGet(symbolId, ownerName, appName)



Returns a particular symbol by id (uuid) for the provided application

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.CrashApi();
let symbolId = "symbolId_example"; // String | The ID of the symbol (uuid of the symbol)
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.symbolsGet(symbolId, ownerName, appName, (error, data, response) => {
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
 **symbolId** | **String**| The ID of the symbol (uuid of the symbol) | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

[**SymbolsList200ResponseInner**](SymbolsList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## symbolsGetLocation

> SymbolsGetLocation200Response symbolsGetLocation(symbolId, ownerName, appName)



Gets the URL to download the symbol

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.CrashApi();
let symbolId = "symbolId_example"; // String | The ID of the symbol (uuid of the symbol)
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.symbolsGetLocation(symbolId, ownerName, appName, (error, data, response) => {
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
 **symbolId** | **String**| The ID of the symbol (uuid of the symbol) | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

[**SymbolsGetLocation200Response**](SymbolsGetLocation200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## symbolsGetStatus

> SymbolsGetStatus200Response symbolsGetStatus(symbolId, ownerName, appName)



Returns a particular symbol by id (uuid) for the provided application

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.CrashApi();
let symbolId = "symbolId_example"; // String | The ID of the symbol (uuid of the symbol)
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.symbolsGetStatus(symbolId, ownerName, appName, (error, data, response) => {
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
 **symbolId** | **String**| The ID of the symbol (uuid of the symbol) | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

[**SymbolsGetStatus200Response**](SymbolsGetStatus200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## symbolsIgnore

> SymbolsList200ResponseInner symbolsIgnore(symbolId, ownerName, appName)



Marks a symbol by id (uuid) as ignored

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.CrashApi();
let symbolId = "symbolId_example"; // String | The ID of the symbol (uuid of the symbol)
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.symbolsIgnore(symbolId, ownerName, appName, (error, data, response) => {
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
 **symbolId** | **String**| The ID of the symbol (uuid of the symbol) | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

[**SymbolsList200ResponseInner**](SymbolsList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## symbolsList

> [SymbolsList200ResponseInner] symbolsList(ownerName, appName)



Returns the list of all symbols for the provided application

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.CrashApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.symbolsList(ownerName, appName, (error, data, response) => {
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

[**[SymbolsList200ResponseInner]**](SymbolsList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

