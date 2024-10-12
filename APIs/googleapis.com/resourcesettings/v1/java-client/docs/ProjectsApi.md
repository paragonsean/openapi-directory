# ProjectsApi

All URIs are relative to *https://resourcesettings.googleapis.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**resourcesettingsProjectsSettingsGet**](ProjectsApi.md#resourcesettingsProjectsSettingsGet) | **GET** /v1/{name} |  |
| [**resourcesettingsProjectsSettingsList**](ProjectsApi.md#resourcesettingsProjectsSettingsList) | **GET** /v1/{parent}/settings |  |
| [**resourcesettingsProjectsSettingsPatch**](ProjectsApi.md#resourcesettingsProjectsSettingsPatch) | **PATCH** /v1/{name} |  |


<a id="resourcesettingsProjectsSettingsGet"></a>
# **resourcesettingsProjectsSettingsGet**
> GoogleCloudResourcesettingsV1Setting resourcesettingsProjectsSettingsGet(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, view)



Returns a specified setting. Returns a &#x60;google.rpc.Status&#x60; with &#x60;google.rpc.Code.NOT_FOUND&#x60; if the setting does not exist.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://resourcesettings.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String name = "name_example"; // String | Required. The name of the setting to get. See Setting for naming requirements.
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
    String view = "SETTING_VIEW_UNSPECIFIED"; // String | The SettingView for this request.
    try {
      GoogleCloudResourcesettingsV1Setting result = apiInstance.resourcesettingsProjectsSettingsGet(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, view);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#resourcesettingsProjectsSettingsGet");
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
| **name** | **String**| Required. The name of the setting to get. See Setting for naming requirements. | |
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
| **view** | **String**| The SettingView for this request. | [optional] [enum: SETTING_VIEW_UNSPECIFIED, SETTING_VIEW_BASIC, SETTING_VIEW_EFFECTIVE_VALUE, SETTING_VIEW_LOCAL_VALUE] |

### Return type

[**GoogleCloudResourcesettingsV1Setting**](GoogleCloudResourcesettingsV1Setting.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="resourcesettingsProjectsSettingsList"></a>
# **resourcesettingsProjectsSettingsList**
> GoogleCloudResourcesettingsV1ListSettingsResponse resourcesettingsProjectsSettingsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, pageSize, pageToken, view)



Lists all the settings that are available on the Cloud resource &#x60;parent&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://resourcesettings.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String parent = "parent_example"; // String | Required. The project, folder, or organization that is the parent resource for this setting. Must be in one of the following forms: * `projects/{project_number}` * `projects/{project_id}` * `folders/{folder_id}` * `organizations/{organization_id}`
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
    Integer pageSize = 56; // Integer | Unused. The size of the page to be returned.
    String pageToken = "pageToken_example"; // String | Unused. A page token used to retrieve the next page.
    String view = "SETTING_VIEW_UNSPECIFIED"; // String | The SettingView for this request.
    try {
      GoogleCloudResourcesettingsV1ListSettingsResponse result = apiInstance.resourcesettingsProjectsSettingsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, pageSize, pageToken, view);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#resourcesettingsProjectsSettingsList");
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
| **parent** | **String**| Required. The project, folder, or organization that is the parent resource for this setting. Must be in one of the following forms: * &#x60;projects/{project_number}&#x60; * &#x60;projects/{project_id}&#x60; * &#x60;folders/{folder_id}&#x60; * &#x60;organizations/{organization_id}&#x60; | |
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
| **pageSize** | **Integer**| Unused. The size of the page to be returned. | [optional] |
| **pageToken** | **String**| Unused. A page token used to retrieve the next page. | [optional] |
| **view** | **String**| The SettingView for this request. | [optional] [enum: SETTING_VIEW_UNSPECIFIED, SETTING_VIEW_BASIC, SETTING_VIEW_EFFECTIVE_VALUE, SETTING_VIEW_LOCAL_VALUE] |

### Return type

[**GoogleCloudResourcesettingsV1ListSettingsResponse**](GoogleCloudResourcesettingsV1ListSettingsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="resourcesettingsProjectsSettingsPatch"></a>
# **resourcesettingsProjectsSettingsPatch**
> GoogleCloudResourcesettingsV1Setting resourcesettingsProjectsSettingsPatch(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudResourcesettingsV1Setting)



Updates a specified setting. Returns a &#x60;google.rpc.Status&#x60; with &#x60;google.rpc.Code.NOT_FOUND&#x60; if the setting does not exist. Returns a &#x60;google.rpc.Status&#x60; with &#x60;google.rpc.Code.FAILED_PRECONDITION&#x60; if the setting is flagged as read only. Returns a &#x60;google.rpc.Status&#x60; with &#x60;google.rpc.Code.ABORTED&#x60; if the etag supplied in the request does not match the persisted etag of the setting value. On success, the response will contain only &#x60;name&#x60;, &#x60;local_value&#x60; and &#x60;etag&#x60;. The &#x60;metadata&#x60; and &#x60;effective_value&#x60; cannot be updated through this API. Note: the supplied setting will perform a full overwrite of the &#x60;local_value&#x60; field.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://resourcesettings.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String name = "name_example"; // String | The resource name of the setting. Must be in one of the following forms: * `projects/{project_number}/settings/{setting_name}` * `folders/{folder_id}/settings/{setting_name}` * `organizations/{organization_id}/settings/{setting_name}` For example, \"/projects/123/settings/gcp-enableMyFeature\"
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
    GoogleCloudResourcesettingsV1Setting googleCloudResourcesettingsV1Setting = new GoogleCloudResourcesettingsV1Setting(); // GoogleCloudResourcesettingsV1Setting | 
    try {
      GoogleCloudResourcesettingsV1Setting result = apiInstance.resourcesettingsProjectsSettingsPatch(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudResourcesettingsV1Setting);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#resourcesettingsProjectsSettingsPatch");
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
| **name** | **String**| The resource name of the setting. Must be in one of the following forms: * &#x60;projects/{project_number}/settings/{setting_name}&#x60; * &#x60;folders/{folder_id}/settings/{setting_name}&#x60; * &#x60;organizations/{organization_id}/settings/{setting_name}&#x60; For example, \&quot;/projects/123/settings/gcp-enableMyFeature\&quot; | |
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
| **googleCloudResourcesettingsV1Setting** | [**GoogleCloudResourcesettingsV1Setting**](GoogleCloudResourcesettingsV1Setting.md)|  | [optional] |

### Return type

[**GoogleCloudResourcesettingsV1Setting**](GoogleCloudResourcesettingsV1Setting.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

