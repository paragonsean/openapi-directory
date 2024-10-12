# AppsScriptApi.ProcessesApi

All URIs are relative to *https://script.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**scriptProcessesList**](ProcessesApi.md#scriptProcessesList) | **GET** /v1/processes | 
[**scriptProcessesListScriptProcesses**](ProcessesApi.md#scriptProcessesListScriptProcesses) | **GET** /v1/processes:listScriptProcesses | 



## scriptProcessesList

> ListUserProcessesResponse scriptProcessesList(opts)



List information about processes made by or on behalf of a user, such as process type and current status.

### Example

```javascript
import AppsScriptApi from 'apps_script_api';
let defaultClient = AppsScriptApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppsScriptApi.ProcessesApi();
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
  'pageSize': 56, // Number | The maximum number of returned processes per page of results. Defaults to 50.
  'pageToken': "pageToken_example", // String | The token for continuing a previous list request on the next page. This should be set to the value of `nextPageToken` from a previous response.
  'userProcessFilterDeploymentId': "userProcessFilterDeploymentId_example", // String | Optional field used to limit returned processes to those originating from projects with a specific deployment ID.
  'userProcessFilterEndTime': "userProcessFilterEndTime_example", // String | Optional field used to limit returned processes to those that completed on or before the given timestamp.
  'userProcessFilterFunctionName': "userProcessFilterFunctionName_example", // String | Optional field used to limit returned processes to those originating from a script function with the given function name.
  'userProcessFilterProjectName': "userProcessFilterProjectName_example", // String | Optional field used to limit returned processes to those originating from projects with project names containing a specific string.
  'userProcessFilterScriptId': "userProcessFilterScriptId_example", // String | Optional field used to limit returned processes to those originating from projects with a specific script ID.
  'userProcessFilterStartTime': "userProcessFilterStartTime_example", // String | Optional field used to limit returned processes to those that were started on or after the given timestamp.
  'userProcessFilterStatuses': ["null"], // [String] | Optional field used to limit returned processes to those having one of the specified process statuses.
  'userProcessFilterTypes': ["null"], // [String] | Optional field used to limit returned processes to those having one of the specified process types.
  'userProcessFilterUserAccessLevels': ["null"] // [String] | Optional field used to limit returned processes to those having one of the specified user access levels.
};
apiInstance.scriptProcessesList(opts, (error, data, response) => {
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
 **pageSize** | **Number**| The maximum number of returned processes per page of results. Defaults to 50. | [optional] 
 **pageToken** | **String**| The token for continuing a previous list request on the next page. This should be set to the value of &#x60;nextPageToken&#x60; from a previous response. | [optional] 
 **userProcessFilterDeploymentId** | **String**| Optional field used to limit returned processes to those originating from projects with a specific deployment ID. | [optional] 
 **userProcessFilterEndTime** | **String**| Optional field used to limit returned processes to those that completed on or before the given timestamp. | [optional] 
 **userProcessFilterFunctionName** | **String**| Optional field used to limit returned processes to those originating from a script function with the given function name. | [optional] 
 **userProcessFilterProjectName** | **String**| Optional field used to limit returned processes to those originating from projects with project names containing a specific string. | [optional] 
 **userProcessFilterScriptId** | **String**| Optional field used to limit returned processes to those originating from projects with a specific script ID. | [optional] 
 **userProcessFilterStartTime** | **String**| Optional field used to limit returned processes to those that were started on or after the given timestamp. | [optional] 
 **userProcessFilterStatuses** | [**[String]**](String.md)| Optional field used to limit returned processes to those having one of the specified process statuses. | [optional] 
 **userProcessFilterTypes** | [**[String]**](String.md)| Optional field used to limit returned processes to those having one of the specified process types. | [optional] 
 **userProcessFilterUserAccessLevels** | [**[String]**](String.md)| Optional field used to limit returned processes to those having one of the specified user access levels. | [optional] 

### Return type

[**ListUserProcessesResponse**](ListUserProcessesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## scriptProcessesListScriptProcesses

> ListScriptProcessesResponse scriptProcessesListScriptProcesses(opts)



List information about a script&#39;s executed processes, such as process type and current status.

### Example

```javascript
import AppsScriptApi from 'apps_script_api';
let defaultClient = AppsScriptApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppsScriptApi.ProcessesApi();
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
  'pageSize': 56, // Number | The maximum number of returned processes per page of results. Defaults to 50.
  'pageToken': "pageToken_example", // String | The token for continuing a previous list request on the next page. This should be set to the value of `nextPageToken` from a previous response.
  'scriptId': "scriptId_example", // String | The script ID of the project whose processes are listed.
  'scriptProcessFilterDeploymentId': "scriptProcessFilterDeploymentId_example", // String | Optional field used to limit returned processes to those originating from projects with a specific deployment ID.
  'scriptProcessFilterEndTime': "scriptProcessFilterEndTime_example", // String | Optional field used to limit returned processes to those that completed on or before the given timestamp.
  'scriptProcessFilterFunctionName': "scriptProcessFilterFunctionName_example", // String | Optional field used to limit returned processes to those originating from a script function with the given function name.
  'scriptProcessFilterStartTime': "scriptProcessFilterStartTime_example", // String | Optional field used to limit returned processes to those that were started on or after the given timestamp.
  'scriptProcessFilterStatuses': ["null"], // [String] | Optional field used to limit returned processes to those having one of the specified process statuses.
  'scriptProcessFilterTypes': ["null"], // [String] | Optional field used to limit returned processes to those having one of the specified process types.
  'scriptProcessFilterUserAccessLevels': ["null"] // [String] | Optional field used to limit returned processes to those having one of the specified user access levels.
};
apiInstance.scriptProcessesListScriptProcesses(opts, (error, data, response) => {
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
 **pageSize** | **Number**| The maximum number of returned processes per page of results. Defaults to 50. | [optional] 
 **pageToken** | **String**| The token for continuing a previous list request on the next page. This should be set to the value of &#x60;nextPageToken&#x60; from a previous response. | [optional] 
 **scriptId** | **String**| The script ID of the project whose processes are listed. | [optional] 
 **scriptProcessFilterDeploymentId** | **String**| Optional field used to limit returned processes to those originating from projects with a specific deployment ID. | [optional] 
 **scriptProcessFilterEndTime** | **String**| Optional field used to limit returned processes to those that completed on or before the given timestamp. | [optional] 
 **scriptProcessFilterFunctionName** | **String**| Optional field used to limit returned processes to those originating from a script function with the given function name. | [optional] 
 **scriptProcessFilterStartTime** | **String**| Optional field used to limit returned processes to those that were started on or after the given timestamp. | [optional] 
 **scriptProcessFilterStatuses** | [**[String]**](String.md)| Optional field used to limit returned processes to those having one of the specified process statuses. | [optional] 
 **scriptProcessFilterTypes** | [**[String]**](String.md)| Optional field used to limit returned processes to those having one of the specified process types. | [optional] 
 **scriptProcessFilterUserAccessLevels** | [**[String]**](String.md)| Optional field used to limit returned processes to those having one of the specified user access levels. | [optional] 

### Return type

[**ListScriptProcessesResponse**](ListScriptProcessesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

