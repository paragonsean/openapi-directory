# ProcessesApi

All URIs are relative to *https://script.googleapis.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**scriptProcessesList**](ProcessesApi.md#scriptProcessesList) | **GET** /v1/processes |  |
| [**scriptProcessesListScriptProcesses**](ProcessesApi.md#scriptProcessesListScriptProcesses) | **GET** /v1/processes:listScriptProcesses |  |


<a id="scriptProcessesList"></a>
# **scriptProcessesList**
> ListUserProcessesResponse scriptProcessesList($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, pageSize, pageToken, userProcessFilterDeploymentId, userProcessFilterEndTime, userProcessFilterFunctionName, userProcessFilterProjectName, userProcessFilterScriptId, userProcessFilterStartTime, userProcessFilterStatuses, userProcessFilterTypes, userProcessFilterUserAccessLevels)



List information about processes made by or on behalf of a user, such as process type and current status.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProcessesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://script.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProcessesApi apiInstance = new ProcessesApi(defaultClient);
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    Integer pageSize = 56; // Integer | The maximum number of returned processes per page of results. Defaults to 50.
    String pageToken = "pageToken_example"; // String | The token for continuing a previous list request on the next page. This should be set to the value of `nextPageToken` from a previous response.
    String userProcessFilterDeploymentId = "userProcessFilterDeploymentId_example"; // String | Optional field used to limit returned processes to those originating from projects with a specific deployment ID.
    String userProcessFilterEndTime = "userProcessFilterEndTime_example"; // String | Optional field used to limit returned processes to those that completed on or before the given timestamp.
    String userProcessFilterFunctionName = "userProcessFilterFunctionName_example"; // String | Optional field used to limit returned processes to those originating from a script function with the given function name.
    String userProcessFilterProjectName = "userProcessFilterProjectName_example"; // String | Optional field used to limit returned processes to those originating from projects with project names containing a specific string.
    String userProcessFilterScriptId = "userProcessFilterScriptId_example"; // String | Optional field used to limit returned processes to those originating from projects with a specific script ID.
    String userProcessFilterStartTime = "userProcessFilterStartTime_example"; // String | Optional field used to limit returned processes to those that were started on or after the given timestamp.
    List<String> userProcessFilterStatuses = Arrays.asList(); // List<String> | Optional field used to limit returned processes to those having one of the specified process statuses.
    List<String> userProcessFilterTypes = Arrays.asList(); // List<String> | Optional field used to limit returned processes to those having one of the specified process types.
    List<String> userProcessFilterUserAccessLevels = Arrays.asList(); // List<String> | Optional field used to limit returned processes to those having one of the specified user access levels.
    try {
      ListUserProcessesResponse result = apiInstance.scriptProcessesList($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, pageSize, pageToken, userProcessFilterDeploymentId, userProcessFilterEndTime, userProcessFilterFunctionName, userProcessFilterProjectName, userProcessFilterScriptId, userProcessFilterStartTime, userProcessFilterStatuses, userProcessFilterTypes, userProcessFilterUserAccessLevels);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProcessesApi#scriptProcessesList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **pageSize** | **Integer**| The maximum number of returned processes per page of results. Defaults to 50. | [optional] |
| **pageToken** | **String**| The token for continuing a previous list request on the next page. This should be set to the value of &#x60;nextPageToken&#x60; from a previous response. | [optional] |
| **userProcessFilterDeploymentId** | **String**| Optional field used to limit returned processes to those originating from projects with a specific deployment ID. | [optional] |
| **userProcessFilterEndTime** | **String**| Optional field used to limit returned processes to those that completed on or before the given timestamp. | [optional] |
| **userProcessFilterFunctionName** | **String**| Optional field used to limit returned processes to those originating from a script function with the given function name. | [optional] |
| **userProcessFilterProjectName** | **String**| Optional field used to limit returned processes to those originating from projects with project names containing a specific string. | [optional] |
| **userProcessFilterScriptId** | **String**| Optional field used to limit returned processes to those originating from projects with a specific script ID. | [optional] |
| **userProcessFilterStartTime** | **String**| Optional field used to limit returned processes to those that were started on or after the given timestamp. | [optional] |
| **userProcessFilterStatuses** | [**List&lt;String&gt;**](String.md)| Optional field used to limit returned processes to those having one of the specified process statuses. | [optional] [enum: PROCESS_STATUS_UNSPECIFIED, RUNNING, PAUSED, COMPLETED, CANCELED, FAILED, TIMED_OUT, UNKNOWN, DELAYED, EXECUTION_DISABLED] |
| **userProcessFilterTypes** | [**List&lt;String&gt;**](String.md)| Optional field used to limit returned processes to those having one of the specified process types. | [optional] [enum: PROCESS_TYPE_UNSPECIFIED, ADD_ON, EXECUTION_API, TIME_DRIVEN, TRIGGER, WEBAPP, EDITOR, SIMPLE_TRIGGER, MENU, BATCH_TASK] |
| **userProcessFilterUserAccessLevels** | [**List&lt;String&gt;**](String.md)| Optional field used to limit returned processes to those having one of the specified user access levels. | [optional] [enum: USER_ACCESS_LEVEL_UNSPECIFIED, NONE, READ, WRITE, OWNER] |

### Return type

[**ListUserProcessesResponse**](ListUserProcessesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="scriptProcessesListScriptProcesses"></a>
# **scriptProcessesListScriptProcesses**
> ListScriptProcessesResponse scriptProcessesListScriptProcesses($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, pageSize, pageToken, scriptId, scriptProcessFilterDeploymentId, scriptProcessFilterEndTime, scriptProcessFilterFunctionName, scriptProcessFilterStartTime, scriptProcessFilterStatuses, scriptProcessFilterTypes, scriptProcessFilterUserAccessLevels)



List information about a script&#39;s executed processes, such as process type and current status.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProcessesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://script.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProcessesApi apiInstance = new ProcessesApi(defaultClient);
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    Integer pageSize = 56; // Integer | The maximum number of returned processes per page of results. Defaults to 50.
    String pageToken = "pageToken_example"; // String | The token for continuing a previous list request on the next page. This should be set to the value of `nextPageToken` from a previous response.
    String scriptId = "scriptId_example"; // String | The script ID of the project whose processes are listed.
    String scriptProcessFilterDeploymentId = "scriptProcessFilterDeploymentId_example"; // String | Optional field used to limit returned processes to those originating from projects with a specific deployment ID.
    String scriptProcessFilterEndTime = "scriptProcessFilterEndTime_example"; // String | Optional field used to limit returned processes to those that completed on or before the given timestamp.
    String scriptProcessFilterFunctionName = "scriptProcessFilterFunctionName_example"; // String | Optional field used to limit returned processes to those originating from a script function with the given function name.
    String scriptProcessFilterStartTime = "scriptProcessFilterStartTime_example"; // String | Optional field used to limit returned processes to those that were started on or after the given timestamp.
    List<String> scriptProcessFilterStatuses = Arrays.asList(); // List<String> | Optional field used to limit returned processes to those having one of the specified process statuses.
    List<String> scriptProcessFilterTypes = Arrays.asList(); // List<String> | Optional field used to limit returned processes to those having one of the specified process types.
    List<String> scriptProcessFilterUserAccessLevels = Arrays.asList(); // List<String> | Optional field used to limit returned processes to those having one of the specified user access levels.
    try {
      ListScriptProcessesResponse result = apiInstance.scriptProcessesListScriptProcesses($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, pageSize, pageToken, scriptId, scriptProcessFilterDeploymentId, scriptProcessFilterEndTime, scriptProcessFilterFunctionName, scriptProcessFilterStartTime, scriptProcessFilterStatuses, scriptProcessFilterTypes, scriptProcessFilterUserAccessLevels);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProcessesApi#scriptProcessesListScriptProcesses");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **pageSize** | **Integer**| The maximum number of returned processes per page of results. Defaults to 50. | [optional] |
| **pageToken** | **String**| The token for continuing a previous list request on the next page. This should be set to the value of &#x60;nextPageToken&#x60; from a previous response. | [optional] |
| **scriptId** | **String**| The script ID of the project whose processes are listed. | [optional] |
| **scriptProcessFilterDeploymentId** | **String**| Optional field used to limit returned processes to those originating from projects with a specific deployment ID. | [optional] |
| **scriptProcessFilterEndTime** | **String**| Optional field used to limit returned processes to those that completed on or before the given timestamp. | [optional] |
| **scriptProcessFilterFunctionName** | **String**| Optional field used to limit returned processes to those originating from a script function with the given function name. | [optional] |
| **scriptProcessFilterStartTime** | **String**| Optional field used to limit returned processes to those that were started on or after the given timestamp. | [optional] |
| **scriptProcessFilterStatuses** | [**List&lt;String&gt;**](String.md)| Optional field used to limit returned processes to those having one of the specified process statuses. | [optional] [enum: PROCESS_STATUS_UNSPECIFIED, RUNNING, PAUSED, COMPLETED, CANCELED, FAILED, TIMED_OUT, UNKNOWN, DELAYED, EXECUTION_DISABLED] |
| **scriptProcessFilterTypes** | [**List&lt;String&gt;**](String.md)| Optional field used to limit returned processes to those having one of the specified process types. | [optional] [enum: PROCESS_TYPE_UNSPECIFIED, ADD_ON, EXECUTION_API, TIME_DRIVEN, TRIGGER, WEBAPP, EDITOR, SIMPLE_TRIGGER, MENU, BATCH_TASK] |
| **scriptProcessFilterUserAccessLevels** | [**List&lt;String&gt;**](String.md)| Optional field used to limit returned processes to those having one of the specified user access levels. | [optional] [enum: USER_ACCESS_LEVEL_UNSPECIFIED, NONE, READ, WRITE, OWNER] |

### Return type

[**ListScriptProcessesResponse**](ListScriptProcessesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

