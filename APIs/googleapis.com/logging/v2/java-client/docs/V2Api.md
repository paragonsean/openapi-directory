# V2Api

All URIs are relative to *https://logging.googleapis.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**loggingGetCmekSettings**](V2Api.md#loggingGetCmekSettings) | **GET** /v2/{name}/cmekSettings |  |
| [**loggingGetSettings**](V2Api.md#loggingGetSettings) | **GET** /v2/{name}/settings |  |
| [**loggingUpdateCmekSettings**](V2Api.md#loggingUpdateCmekSettings) | **PATCH** /v2/{name}/cmekSettings |  |
| [**loggingUpdateSettings**](V2Api.md#loggingUpdateSettings) | **PATCH** /v2/{name}/settings |  |


<a id="loggingGetCmekSettings"></a>
# **loggingGetCmekSettings**
> CmekSettings loggingGetCmekSettings(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType)



Gets the Logging CMEK settings for the given resource.Note: CMEK for the Log Router can be configured for Google Cloud projects, folders, organizations, and billing accounts. Once configured for an organization, it applies to all projects and folders in the Google Cloud organization.See Enabling CMEK for Log Router (https://cloud.google.com/logging/docs/routing/managed-encryption) for more information.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://logging.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    V2Api apiInstance = new V2Api(defaultClient);
    String name = "name_example"; // String | Required. The resource for which to retrieve CMEK settings. \"projects/[PROJECT_ID]/cmekSettings\" \"organizations/[ORGANIZATION_ID]/cmekSettings\" \"billingAccounts/[BILLING_ACCOUNT_ID]/cmekSettings\" \"folders/[FOLDER_ID]/cmekSettings\" For example:\"organizations/12345/cmekSettings\"Note: CMEK for the Log Router can be configured for Google Cloud projects, folders, organizations, and billing accounts. Once configured for an organization, it applies to all projects and folders in the Google Cloud organization.
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
    try {
      CmekSettings result = apiInstance.loggingGetCmekSettings(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V2Api#loggingGetCmekSettings");
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
| **name** | **String**| Required. The resource for which to retrieve CMEK settings. \&quot;projects/[PROJECT_ID]/cmekSettings\&quot; \&quot;organizations/[ORGANIZATION_ID]/cmekSettings\&quot; \&quot;billingAccounts/[BILLING_ACCOUNT_ID]/cmekSettings\&quot; \&quot;folders/[FOLDER_ID]/cmekSettings\&quot; For example:\&quot;organizations/12345/cmekSettings\&quot;Note: CMEK for the Log Router can be configured for Google Cloud projects, folders, organizations, and billing accounts. Once configured for an organization, it applies to all projects and folders in the Google Cloud organization. | |
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

### Return type

[**CmekSettings**](CmekSettings.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="loggingGetSettings"></a>
# **loggingGetSettings**
> Settings loggingGetSettings(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType)



Gets the settings for the given resource.Note: Settings can be retrieved for Google Cloud projects, folders, organizations, and billing accounts.See View default resource settings for Logging (https://cloud.google.com/logging/docs/default-settings#view-org-settings) for more information.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://logging.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    V2Api apiInstance = new V2Api(defaultClient);
    String name = "name_example"; // String | Required. The resource for which to retrieve settings. \"projects/[PROJECT_ID]/settings\" \"organizations/[ORGANIZATION_ID]/settings\" \"billingAccounts/[BILLING_ACCOUNT_ID]/settings\" \"folders/[FOLDER_ID]/settings\" For example:\"organizations/12345/settings\"Note: Settings can be retrieved for Google Cloud projects, folders, organizations, and billing accounts.
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
    try {
      Settings result = apiInstance.loggingGetSettings(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V2Api#loggingGetSettings");
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
| **name** | **String**| Required. The resource for which to retrieve settings. \&quot;projects/[PROJECT_ID]/settings\&quot; \&quot;organizations/[ORGANIZATION_ID]/settings\&quot; \&quot;billingAccounts/[BILLING_ACCOUNT_ID]/settings\&quot; \&quot;folders/[FOLDER_ID]/settings\&quot; For example:\&quot;organizations/12345/settings\&quot;Note: Settings can be retrieved for Google Cloud projects, folders, organizations, and billing accounts. | |
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

### Return type

[**Settings**](Settings.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="loggingUpdateCmekSettings"></a>
# **loggingUpdateCmekSettings**
> CmekSettings loggingUpdateCmekSettings(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, updateMask, cmekSettings)



Updates the Log Router CMEK settings for the given resource.Note: CMEK for the Log Router can currently only be configured for Google Cloud organizations. Once configured, it applies to all projects and folders in the Google Cloud organization.UpdateCmekSettings fails when any of the following are true: The value of kms_key_name is invalid. The associated service account doesn&#39;t have the required roles/cloudkms.cryptoKeyEncrypterDecrypter role assigned for the key. Access to the key is disabled.See Enabling CMEK for Log Router (https://cloud.google.com/logging/docs/routing/managed-encryption) for more information.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://logging.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    V2Api apiInstance = new V2Api(defaultClient);
    String name = "name_example"; // String | Required. The resource name for the CMEK settings to update. \"projects/[PROJECT_ID]/cmekSettings\" \"organizations/[ORGANIZATION_ID]/cmekSettings\" \"billingAccounts/[BILLING_ACCOUNT_ID]/cmekSettings\" \"folders/[FOLDER_ID]/cmekSettings\" For example:\"organizations/12345/cmekSettings\"Note: CMEK for the Log Router can currently only be configured for Google Cloud organizations. Once configured, it applies to all projects and folders in the Google Cloud organization.
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
    String updateMask = "updateMask_example"; // String | Optional. Field mask identifying which fields from cmek_settings should be updated. A field will be overwritten if and only if it is in the update mask. Output only fields cannot be updated.See FieldMask for more information.For example: \"updateMask=kmsKeyName\"
    CmekSettings cmekSettings = new CmekSettings(); // CmekSettings | 
    try {
      CmekSettings result = apiInstance.loggingUpdateCmekSettings(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, updateMask, cmekSettings);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V2Api#loggingUpdateCmekSettings");
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
| **name** | **String**| Required. The resource name for the CMEK settings to update. \&quot;projects/[PROJECT_ID]/cmekSettings\&quot; \&quot;organizations/[ORGANIZATION_ID]/cmekSettings\&quot; \&quot;billingAccounts/[BILLING_ACCOUNT_ID]/cmekSettings\&quot; \&quot;folders/[FOLDER_ID]/cmekSettings\&quot; For example:\&quot;organizations/12345/cmekSettings\&quot;Note: CMEK for the Log Router can currently only be configured for Google Cloud organizations. Once configured, it applies to all projects and folders in the Google Cloud organization. | |
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
| **updateMask** | **String**| Optional. Field mask identifying which fields from cmek_settings should be updated. A field will be overwritten if and only if it is in the update mask. Output only fields cannot be updated.See FieldMask for more information.For example: \&quot;updateMask&#x3D;kmsKeyName\&quot; | [optional] |
| **cmekSettings** | [**CmekSettings**](CmekSettings.md)|  | [optional] |

### Return type

[**CmekSettings**](CmekSettings.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="loggingUpdateSettings"></a>
# **loggingUpdateSettings**
> Settings loggingUpdateSettings(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, updateMask, settings)



Updates the settings for the given resource. This method applies to all feature configurations for organization and folders.UpdateSettings fails when any of the following are true: The value of storage_location either isn&#39;t supported by Logging or violates the location OrgPolicy. The default_sink_config field is set, but it has an unspecified filter write mode. The value of kms_key_name is invalid. The associated service account doesn&#39;t have the required roles/cloudkms.cryptoKeyEncrypterDecrypter role assigned for the key. Access to the key is disabled.See Configure default settings for organizations and folders (https://cloud.google.com/logging/docs/default-settings) for more information.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://logging.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    V2Api apiInstance = new V2Api(defaultClient);
    String name = "name_example"; // String | Required. The resource name for the settings to update. \"organizations/[ORGANIZATION_ID]/settings\" For example:\"organizations/12345/settings\"
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
    String updateMask = "updateMask_example"; // String | Optional. Field mask identifying which fields from settings should be updated. A field will be overwritten if and only if it is in the update mask. Output only fields cannot be updated.See FieldMask for more information.For example: \"updateMask=kmsKeyName\"
    Settings settings = new Settings(); // Settings | 
    try {
      Settings result = apiInstance.loggingUpdateSettings(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, updateMask, settings);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V2Api#loggingUpdateSettings");
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
| **name** | **String**| Required. The resource name for the settings to update. \&quot;organizations/[ORGANIZATION_ID]/settings\&quot; For example:\&quot;organizations/12345/settings\&quot; | |
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
| **updateMask** | **String**| Optional. Field mask identifying which fields from settings should be updated. A field will be overwritten if and only if it is in the update mask. Output only fields cannot be updated.See FieldMask for more information.For example: \&quot;updateMask&#x3D;kmsKeyName\&quot; | [optional] |
| **settings** | [**Settings**](Settings.md)|  | [optional] |

### Return type

[**Settings**](Settings.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

