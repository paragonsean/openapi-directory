# LabelsApi

All URIs are relative to *https://drivelabels.googleapis.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**drivelabelsLabelsCreate**](LabelsApi.md#drivelabelsLabelsCreate) | **POST** /v2beta/labels |  |
| [**drivelabelsLabelsDelta**](LabelsApi.md#drivelabelsLabelsDelta) | **POST** /v2beta/{name}:delta |  |
| [**drivelabelsLabelsDisable**](LabelsApi.md#drivelabelsLabelsDisable) | **POST** /v2beta/{name}:disable |  |
| [**drivelabelsLabelsEnable**](LabelsApi.md#drivelabelsLabelsEnable) | **POST** /v2beta/{name}:enable |  |
| [**drivelabelsLabelsList**](LabelsApi.md#drivelabelsLabelsList) | **GET** /v2beta/labels |  |
| [**drivelabelsLabelsPublish**](LabelsApi.md#drivelabelsLabelsPublish) | **POST** /v2beta/{name}:publish |  |
| [**drivelabelsLabelsRevisionsLocksList**](LabelsApi.md#drivelabelsLabelsRevisionsLocksList) | **GET** /v2beta/{parent}/locks |  |
| [**drivelabelsLabelsRevisionsPermissionsBatchDelete**](LabelsApi.md#drivelabelsLabelsRevisionsPermissionsBatchDelete) | **POST** /v2beta/{parent}/permissions:batchDelete |  |
| [**drivelabelsLabelsRevisionsPermissionsBatchUpdate**](LabelsApi.md#drivelabelsLabelsRevisionsPermissionsBatchUpdate) | **POST** /v2beta/{parent}/permissions:batchUpdate |  |
| [**drivelabelsLabelsRevisionsPermissionsCreate**](LabelsApi.md#drivelabelsLabelsRevisionsPermissionsCreate) | **POST** /v2beta/{parent}/permissions |  |
| [**drivelabelsLabelsRevisionsPermissionsDelete**](LabelsApi.md#drivelabelsLabelsRevisionsPermissionsDelete) | **DELETE** /v2beta/{name} |  |
| [**drivelabelsLabelsRevisionsPermissionsList**](LabelsApi.md#drivelabelsLabelsRevisionsPermissionsList) | **GET** /v2beta/{parent}/permissions |  |
| [**drivelabelsLabelsRevisionsUpdatePermissions**](LabelsApi.md#drivelabelsLabelsRevisionsUpdatePermissions) | **PATCH** /v2beta/{parent}/permissions |  |
| [**drivelabelsLabelsUpdateLabelCopyMode**](LabelsApi.md#drivelabelsLabelsUpdateLabelCopyMode) | **POST** /v2beta/{name}:updateLabelCopyMode |  |


<a id="drivelabelsLabelsCreate"></a>
# **drivelabelsLabelsCreate**
> GoogleAppsDriveLabelsV2betaLabel drivelabelsLabelsCreate($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, languageCode, useAdminAccess, googleAppsDriveLabelsV2betaLabel)



Creates a new Label.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LabelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://drivelabels.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    LabelsApi apiInstance = new LabelsApi(defaultClient);
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
    String languageCode = "languageCode_example"; // String | The BCP-47 language code to use for evaluating localized Field labels in response. When not specified, values in the default configured language will be used.
    Boolean useAdminAccess = true; // Boolean | Set to `true` in order to use the user's admin privileges. The server will verify the user is an admin before allowing access.
    GoogleAppsDriveLabelsV2betaLabel googleAppsDriveLabelsV2betaLabel = new GoogleAppsDriveLabelsV2betaLabel(); // GoogleAppsDriveLabelsV2betaLabel | 
    try {
      GoogleAppsDriveLabelsV2betaLabel result = apiInstance.drivelabelsLabelsCreate($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, languageCode, useAdminAccess, googleAppsDriveLabelsV2betaLabel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LabelsApi#drivelabelsLabelsCreate");
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
| **languageCode** | **String**| The BCP-47 language code to use for evaluating localized Field labels in response. When not specified, values in the default configured language will be used. | [optional] |
| **useAdminAccess** | **Boolean**| Set to &#x60;true&#x60; in order to use the user&#39;s admin privileges. The server will verify the user is an admin before allowing access. | [optional] |
| **googleAppsDriveLabelsV2betaLabel** | [**GoogleAppsDriveLabelsV2betaLabel**](GoogleAppsDriveLabelsV2betaLabel.md)|  | [optional] |

### Return type

[**GoogleAppsDriveLabelsV2betaLabel**](GoogleAppsDriveLabelsV2betaLabel.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="drivelabelsLabelsDelta"></a>
# **drivelabelsLabelsDelta**
> GoogleAppsDriveLabelsV2betaDeltaUpdateLabelResponse drivelabelsLabelsDelta(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleAppsDriveLabelsV2betaDeltaUpdateLabelRequest)



Updates a single Label by applying a set of update requests resulting in a new draft revision. The batch update is all-or-nothing: If any of the update requests are invalid, no changes are applied. The resulting draft revision must be published before the changes may be used with Drive Items.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LabelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://drivelabels.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    LabelsApi apiInstance = new LabelsApi(defaultClient);
    String name = "name_example"; // String | Required. The resource name of the Label to update.
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
    GoogleAppsDriveLabelsV2betaDeltaUpdateLabelRequest googleAppsDriveLabelsV2betaDeltaUpdateLabelRequest = new GoogleAppsDriveLabelsV2betaDeltaUpdateLabelRequest(); // GoogleAppsDriveLabelsV2betaDeltaUpdateLabelRequest | 
    try {
      GoogleAppsDriveLabelsV2betaDeltaUpdateLabelResponse result = apiInstance.drivelabelsLabelsDelta(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleAppsDriveLabelsV2betaDeltaUpdateLabelRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LabelsApi#drivelabelsLabelsDelta");
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
| **name** | **String**| Required. The resource name of the Label to update. | |
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
| **googleAppsDriveLabelsV2betaDeltaUpdateLabelRequest** | [**GoogleAppsDriveLabelsV2betaDeltaUpdateLabelRequest**](GoogleAppsDriveLabelsV2betaDeltaUpdateLabelRequest.md)|  | [optional] |

### Return type

[**GoogleAppsDriveLabelsV2betaDeltaUpdateLabelResponse**](GoogleAppsDriveLabelsV2betaDeltaUpdateLabelResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="drivelabelsLabelsDisable"></a>
# **drivelabelsLabelsDisable**
> GoogleAppsDriveLabelsV2betaLabel drivelabelsLabelsDisable(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleAppsDriveLabelsV2betaDisableLabelRequest)



Disable a published Label. Disabling a Label will result in a new disabled published revision based on the current published revision. If there is a draft revision, a new disabled draft revision will be created based on the latest draft revision. Older draft revisions will be deleted. Once disabled, a label may be deleted with &#x60;DeleteLabel&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LabelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://drivelabels.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    LabelsApi apiInstance = new LabelsApi(defaultClient);
    String name = "name_example"; // String | Required. Label resource name.
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
    GoogleAppsDriveLabelsV2betaDisableLabelRequest googleAppsDriveLabelsV2betaDisableLabelRequest = new GoogleAppsDriveLabelsV2betaDisableLabelRequest(); // GoogleAppsDriveLabelsV2betaDisableLabelRequest | 
    try {
      GoogleAppsDriveLabelsV2betaLabel result = apiInstance.drivelabelsLabelsDisable(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleAppsDriveLabelsV2betaDisableLabelRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LabelsApi#drivelabelsLabelsDisable");
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
| **name** | **String**| Required. Label resource name. | |
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
| **googleAppsDriveLabelsV2betaDisableLabelRequest** | [**GoogleAppsDriveLabelsV2betaDisableLabelRequest**](GoogleAppsDriveLabelsV2betaDisableLabelRequest.md)|  | [optional] |

### Return type

[**GoogleAppsDriveLabelsV2betaLabel**](GoogleAppsDriveLabelsV2betaLabel.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="drivelabelsLabelsEnable"></a>
# **drivelabelsLabelsEnable**
> GoogleAppsDriveLabelsV2betaLabel drivelabelsLabelsEnable(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleAppsDriveLabelsV2betaEnableLabelRequest)



Enable a disabled Label and restore it to its published state. This will result in a new published revision based on the current disabled published revision. If there is an existing disabled draft revision, a new revision will be created based on that draft and will be enabled.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LabelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://drivelabels.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    LabelsApi apiInstance = new LabelsApi(defaultClient);
    String name = "name_example"; // String | Required. Label resource name.
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
    GoogleAppsDriveLabelsV2betaEnableLabelRequest googleAppsDriveLabelsV2betaEnableLabelRequest = new GoogleAppsDriveLabelsV2betaEnableLabelRequest(); // GoogleAppsDriveLabelsV2betaEnableLabelRequest | 
    try {
      GoogleAppsDriveLabelsV2betaLabel result = apiInstance.drivelabelsLabelsEnable(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleAppsDriveLabelsV2betaEnableLabelRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LabelsApi#drivelabelsLabelsEnable");
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
| **name** | **String**| Required. Label resource name. | |
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
| **googleAppsDriveLabelsV2betaEnableLabelRequest** | [**GoogleAppsDriveLabelsV2betaEnableLabelRequest**](GoogleAppsDriveLabelsV2betaEnableLabelRequest.md)|  | [optional] |

### Return type

[**GoogleAppsDriveLabelsV2betaLabel**](GoogleAppsDriveLabelsV2betaLabel.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="drivelabelsLabelsList"></a>
# **drivelabelsLabelsList**
> GoogleAppsDriveLabelsV2betaListLabelsResponse drivelabelsLabelsList($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, customer, languageCode, minimumRole, pageSize, pageToken, publishedOnly, useAdminAccess, view)



List labels.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LabelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://drivelabels.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    LabelsApi apiInstance = new LabelsApi(defaultClient);
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
    String customer = "customer_example"; // String | The customer to scope this list request to. For example: \"customers/abcd1234\". If unset, will return all labels within the current customer.
    String languageCode = "languageCode_example"; // String | The BCP-47 language code to use for evaluating localized field labels. When not specified, values in the default configured language are used.
    String minimumRole = "LABEL_ROLE_UNSPECIFIED"; // String | Specifies the level of access the user must have on the returned Labels. The minimum role a user must have on a label. Defaults to `READER`.
    Integer pageSize = 56; // Integer | Maximum number of labels to return per page. Default: 50. Max: 200.
    String pageToken = "pageToken_example"; // String | The token of the page to return.
    Boolean publishedOnly = true; // Boolean | Whether to include only published labels in the results. * When `true`, only the current published label revisions are returned. Disabled labels are included. Returned label resource names reference the published revision (`labels/{id}/{revision_id}`). * When `false`, the current label revisions are returned, which might not be published. Returned label resource names don't reference a specific revision (`labels/{id}`).
    Boolean useAdminAccess = true; // Boolean | Set to `true` in order to use the user's admin credentials. This will return all Labels within the customer.
    String view = "LABEL_VIEW_BASIC"; // String | When specified, only certain fields belonging to the indicated view are returned.
    try {
      GoogleAppsDriveLabelsV2betaListLabelsResponse result = apiInstance.drivelabelsLabelsList($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, customer, languageCode, minimumRole, pageSize, pageToken, publishedOnly, useAdminAccess, view);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LabelsApi#drivelabelsLabelsList");
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
| **customer** | **String**| The customer to scope this list request to. For example: \&quot;customers/abcd1234\&quot;. If unset, will return all labels within the current customer. | [optional] |
| **languageCode** | **String**| The BCP-47 language code to use for evaluating localized field labels. When not specified, values in the default configured language are used. | [optional] |
| **minimumRole** | **String**| Specifies the level of access the user must have on the returned Labels. The minimum role a user must have on a label. Defaults to &#x60;READER&#x60;. | [optional] [enum: LABEL_ROLE_UNSPECIFIED, READER, APPLIER, ORGANIZER, EDITOR] |
| **pageSize** | **Integer**| Maximum number of labels to return per page. Default: 50. Max: 200. | [optional] |
| **pageToken** | **String**| The token of the page to return. | [optional] |
| **publishedOnly** | **Boolean**| Whether to include only published labels in the results. * When &#x60;true&#x60;, only the current published label revisions are returned. Disabled labels are included. Returned label resource names reference the published revision (&#x60;labels/{id}/{revision_id}&#x60;). * When &#x60;false&#x60;, the current label revisions are returned, which might not be published. Returned label resource names don&#39;t reference a specific revision (&#x60;labels/{id}&#x60;). | [optional] |
| **useAdminAccess** | **Boolean**| Set to &#x60;true&#x60; in order to use the user&#39;s admin credentials. This will return all Labels within the customer. | [optional] |
| **view** | **String**| When specified, only certain fields belonging to the indicated view are returned. | [optional] [enum: LABEL_VIEW_BASIC, LABEL_VIEW_FULL] |

### Return type

[**GoogleAppsDriveLabelsV2betaListLabelsResponse**](GoogleAppsDriveLabelsV2betaListLabelsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="drivelabelsLabelsPublish"></a>
# **drivelabelsLabelsPublish**
> GoogleAppsDriveLabelsV2betaLabel drivelabelsLabelsPublish(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleAppsDriveLabelsV2betaPublishLabelRequest)



Publish all draft changes to the Label. Once published, the Label may not return to its draft state. See &#x60;google.apps.drive.labels.v2.Lifecycle&#x60; for more information. Publishing a Label will result in a new published revision. All previous draft revisions will be deleted. Previous published revisions will be kept but are subject to automated deletion as needed. Once published, some changes are no longer permitted. Generally, any change that would invalidate or cause new restrictions on existing metadata related to the Label will be rejected. For example, the following changes to a Label will be rejected after the Label is published: * The label cannot be directly deleted. It must be disabled first, then deleted. * Field.FieldType cannot be changed. * Changes to Field validation options cannot reject something that was previously accepted. * Reducing the max entries.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LabelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://drivelabels.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    LabelsApi apiInstance = new LabelsApi(defaultClient);
    String name = "name_example"; // String | Required. Label resource name.
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
    GoogleAppsDriveLabelsV2betaPublishLabelRequest googleAppsDriveLabelsV2betaPublishLabelRequest = new GoogleAppsDriveLabelsV2betaPublishLabelRequest(); // GoogleAppsDriveLabelsV2betaPublishLabelRequest | 
    try {
      GoogleAppsDriveLabelsV2betaLabel result = apiInstance.drivelabelsLabelsPublish(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleAppsDriveLabelsV2betaPublishLabelRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LabelsApi#drivelabelsLabelsPublish");
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
| **name** | **String**| Required. Label resource name. | |
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
| **googleAppsDriveLabelsV2betaPublishLabelRequest** | [**GoogleAppsDriveLabelsV2betaPublishLabelRequest**](GoogleAppsDriveLabelsV2betaPublishLabelRequest.md)|  | [optional] |

### Return type

[**GoogleAppsDriveLabelsV2betaLabel**](GoogleAppsDriveLabelsV2betaLabel.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="drivelabelsLabelsRevisionsLocksList"></a>
# **drivelabelsLabelsRevisionsLocksList**
> GoogleAppsDriveLabelsV2betaListLabelLocksResponse drivelabelsLabelsRevisionsLocksList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, pageSize, pageToken)



Lists the LabelLocks on a Label.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LabelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://drivelabels.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    LabelsApi apiInstance = new LabelsApi(defaultClient);
    String parent = "parent_example"; // String | Required. Label on which Locks are applied. Format: labels/{label}
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
    Integer pageSize = 56; // Integer | Maximum number of Locks to return per page. Default: 100. Max: 200.
    String pageToken = "pageToken_example"; // String | The token of the page to return.
    try {
      GoogleAppsDriveLabelsV2betaListLabelLocksResponse result = apiInstance.drivelabelsLabelsRevisionsLocksList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, pageSize, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LabelsApi#drivelabelsLabelsRevisionsLocksList");
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
| **parent** | **String**| Required. Label on which Locks are applied. Format: labels/{label} | |
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
| **pageSize** | **Integer**| Maximum number of Locks to return per page. Default: 100. Max: 200. | [optional] |
| **pageToken** | **String**| The token of the page to return. | [optional] |

### Return type

[**GoogleAppsDriveLabelsV2betaListLabelLocksResponse**](GoogleAppsDriveLabelsV2betaListLabelLocksResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="drivelabelsLabelsRevisionsPermissionsBatchDelete"></a>
# **drivelabelsLabelsRevisionsPermissionsBatchDelete**
> Object drivelabelsLabelsRevisionsPermissionsBatchDelete(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleAppsDriveLabelsV2betaBatchDeleteLabelPermissionsRequest)



Deletes Label permissions. Permissions affect the Label resource as a whole, are not revisioned, and do not require publishing.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LabelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://drivelabels.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    LabelsApi apiInstance = new LabelsApi(defaultClient);
    String parent = "parent_example"; // String | Required. The parent Label resource name shared by all permissions being deleted. Format: labels/{label} If this is set, the parent field in the UpdateLabelPermissionRequest messages must either be empty or match this field.
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
    GoogleAppsDriveLabelsV2betaBatchDeleteLabelPermissionsRequest googleAppsDriveLabelsV2betaBatchDeleteLabelPermissionsRequest = new GoogleAppsDriveLabelsV2betaBatchDeleteLabelPermissionsRequest(); // GoogleAppsDriveLabelsV2betaBatchDeleteLabelPermissionsRequest | 
    try {
      Object result = apiInstance.drivelabelsLabelsRevisionsPermissionsBatchDelete(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleAppsDriveLabelsV2betaBatchDeleteLabelPermissionsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LabelsApi#drivelabelsLabelsRevisionsPermissionsBatchDelete");
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
| **parent** | **String**| Required. The parent Label resource name shared by all permissions being deleted. Format: labels/{label} If this is set, the parent field in the UpdateLabelPermissionRequest messages must either be empty or match this field. | |
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
| **googleAppsDriveLabelsV2betaBatchDeleteLabelPermissionsRequest** | [**GoogleAppsDriveLabelsV2betaBatchDeleteLabelPermissionsRequest**](GoogleAppsDriveLabelsV2betaBatchDeleteLabelPermissionsRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="drivelabelsLabelsRevisionsPermissionsBatchUpdate"></a>
# **drivelabelsLabelsRevisionsPermissionsBatchUpdate**
> GoogleAppsDriveLabelsV2betaBatchUpdateLabelPermissionsResponse drivelabelsLabelsRevisionsPermissionsBatchUpdate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleAppsDriveLabelsV2betaBatchUpdateLabelPermissionsRequest)



Updates Label permissions. If a permission for the indicated principal doesn&#39;t exist, a new Label Permission is created, otherwise the existing permission is updated. Permissions affect the Label resource as a whole, are not revisioned, and do not require publishing.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LabelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://drivelabels.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    LabelsApi apiInstance = new LabelsApi(defaultClient);
    String parent = "parent_example"; // String | Required. The parent Label resource name shared by all permissions being updated. Format: labels/{label} If this is set, the parent field in the UpdateLabelPermissionRequest messages must either be empty or match this field.
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
    GoogleAppsDriveLabelsV2betaBatchUpdateLabelPermissionsRequest googleAppsDriveLabelsV2betaBatchUpdateLabelPermissionsRequest = new GoogleAppsDriveLabelsV2betaBatchUpdateLabelPermissionsRequest(); // GoogleAppsDriveLabelsV2betaBatchUpdateLabelPermissionsRequest | 
    try {
      GoogleAppsDriveLabelsV2betaBatchUpdateLabelPermissionsResponse result = apiInstance.drivelabelsLabelsRevisionsPermissionsBatchUpdate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleAppsDriveLabelsV2betaBatchUpdateLabelPermissionsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LabelsApi#drivelabelsLabelsRevisionsPermissionsBatchUpdate");
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
| **parent** | **String**| Required. The parent Label resource name shared by all permissions being updated. Format: labels/{label} If this is set, the parent field in the UpdateLabelPermissionRequest messages must either be empty or match this field. | |
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
| **googleAppsDriveLabelsV2betaBatchUpdateLabelPermissionsRequest** | [**GoogleAppsDriveLabelsV2betaBatchUpdateLabelPermissionsRequest**](GoogleAppsDriveLabelsV2betaBatchUpdateLabelPermissionsRequest.md)|  | [optional] |

### Return type

[**GoogleAppsDriveLabelsV2betaBatchUpdateLabelPermissionsResponse**](GoogleAppsDriveLabelsV2betaBatchUpdateLabelPermissionsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="drivelabelsLabelsRevisionsPermissionsCreate"></a>
# **drivelabelsLabelsRevisionsPermissionsCreate**
> GoogleAppsDriveLabelsV2betaLabelPermission drivelabelsLabelsRevisionsPermissionsCreate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, useAdminAccess, googleAppsDriveLabelsV2betaLabelPermission)



Updates a Label&#39;s permissions. If a permission for the indicated principal doesn&#39;t exist, a new Label Permission is created, otherwise the existing permission is updated. Permissions affect the Label resource as a whole, are not revisioned, and do not require publishing.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LabelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://drivelabels.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    LabelsApi apiInstance = new LabelsApi(defaultClient);
    String parent = "parent_example"; // String | Required. The parent Label resource name on the Label Permission is created. Format: labels/{label}
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
    Boolean useAdminAccess = true; // Boolean | Set to `true` in order to use the user's admin credentials. The server will verify the user is an admin for the Label before allowing access.
    GoogleAppsDriveLabelsV2betaLabelPermission googleAppsDriveLabelsV2betaLabelPermission = new GoogleAppsDriveLabelsV2betaLabelPermission(); // GoogleAppsDriveLabelsV2betaLabelPermission | 
    try {
      GoogleAppsDriveLabelsV2betaLabelPermission result = apiInstance.drivelabelsLabelsRevisionsPermissionsCreate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, useAdminAccess, googleAppsDriveLabelsV2betaLabelPermission);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LabelsApi#drivelabelsLabelsRevisionsPermissionsCreate");
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
| **parent** | **String**| Required. The parent Label resource name on the Label Permission is created. Format: labels/{label} | |
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
| **useAdminAccess** | **Boolean**| Set to &#x60;true&#x60; in order to use the user&#39;s admin credentials. The server will verify the user is an admin for the Label before allowing access. | [optional] |
| **googleAppsDriveLabelsV2betaLabelPermission** | [**GoogleAppsDriveLabelsV2betaLabelPermission**](GoogleAppsDriveLabelsV2betaLabelPermission.md)|  | [optional] |

### Return type

[**GoogleAppsDriveLabelsV2betaLabelPermission**](GoogleAppsDriveLabelsV2betaLabelPermission.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="drivelabelsLabelsRevisionsPermissionsDelete"></a>
# **drivelabelsLabelsRevisionsPermissionsDelete**
> Object drivelabelsLabelsRevisionsPermissionsDelete(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, useAdminAccess, writeControlRequiredRevisionId)



Deletes a Label&#39;s permission. Permissions affect the Label resource as a whole, are not revisioned, and do not require publishing.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LabelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://drivelabels.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    LabelsApi apiInstance = new LabelsApi(defaultClient);
    String name = "name_example"; // String | Required. Label Permission resource name.
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
    Boolean useAdminAccess = true; // Boolean | Set to `true` in order to use the user's admin credentials. The server will verify the user is an admin for the Label before allowing access.
    String writeControlRequiredRevisionId = "writeControlRequiredRevisionId_example"; // String | The revision_id of the label that the write request will be applied to. If this is not the latest revision of the label, the request will not be processed and will return a 400 Bad Request error.
    try {
      Object result = apiInstance.drivelabelsLabelsRevisionsPermissionsDelete(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, useAdminAccess, writeControlRequiredRevisionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LabelsApi#drivelabelsLabelsRevisionsPermissionsDelete");
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
| **name** | **String**| Required. Label Permission resource name. | |
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
| **useAdminAccess** | **Boolean**| Set to &#x60;true&#x60; in order to use the user&#39;s admin credentials. The server will verify the user is an admin for the Label before allowing access. | [optional] |
| **writeControlRequiredRevisionId** | **String**| The revision_id of the label that the write request will be applied to. If this is not the latest revision of the label, the request will not be processed and will return a 400 Bad Request error. | [optional] |

### Return type

**Object**

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="drivelabelsLabelsRevisionsPermissionsList"></a>
# **drivelabelsLabelsRevisionsPermissionsList**
> GoogleAppsDriveLabelsV2betaListLabelPermissionsResponse drivelabelsLabelsRevisionsPermissionsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, pageSize, pageToken, useAdminAccess)



Lists a Label&#39;s permissions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LabelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://drivelabels.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    LabelsApi apiInstance = new LabelsApi(defaultClient);
    String parent = "parent_example"; // String | Required. The parent Label resource name on which Label Permission are listed. Format: labels/{label}
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
    Integer pageSize = 56; // Integer | Maximum number of permissions to return per page. Default: 50. Max: 200.
    String pageToken = "pageToken_example"; // String | The token of the page to return.
    Boolean useAdminAccess = true; // Boolean | Set to `true` in order to use the user's admin credentials. The server will verify the user is an admin for the Label before allowing access.
    try {
      GoogleAppsDriveLabelsV2betaListLabelPermissionsResponse result = apiInstance.drivelabelsLabelsRevisionsPermissionsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, pageSize, pageToken, useAdminAccess);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LabelsApi#drivelabelsLabelsRevisionsPermissionsList");
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
| **parent** | **String**| Required. The parent Label resource name on which Label Permission are listed. Format: labels/{label} | |
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
| **pageSize** | **Integer**| Maximum number of permissions to return per page. Default: 50. Max: 200. | [optional] |
| **pageToken** | **String**| The token of the page to return. | [optional] |
| **useAdminAccess** | **Boolean**| Set to &#x60;true&#x60; in order to use the user&#39;s admin credentials. The server will verify the user is an admin for the Label before allowing access. | [optional] |

### Return type

[**GoogleAppsDriveLabelsV2betaListLabelPermissionsResponse**](GoogleAppsDriveLabelsV2betaListLabelPermissionsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="drivelabelsLabelsRevisionsUpdatePermissions"></a>
# **drivelabelsLabelsRevisionsUpdatePermissions**
> GoogleAppsDriveLabelsV2betaLabelPermission drivelabelsLabelsRevisionsUpdatePermissions(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, useAdminAccess, googleAppsDriveLabelsV2betaLabelPermission)



Updates a Label&#39;s permissions. If a permission for the indicated principal doesn&#39;t exist, a new Label Permission is created, otherwise the existing permission is updated. Permissions affect the Label resource as a whole, are not revisioned, and do not require publishing.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LabelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://drivelabels.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    LabelsApi apiInstance = new LabelsApi(defaultClient);
    String parent = "parent_example"; // String | Required. The parent Label resource name.
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
    Boolean useAdminAccess = true; // Boolean | Set to `true` in order to use the user's admin credentials. The server will verify the user is an admin for the Label before allowing access.
    GoogleAppsDriveLabelsV2betaLabelPermission googleAppsDriveLabelsV2betaLabelPermission = new GoogleAppsDriveLabelsV2betaLabelPermission(); // GoogleAppsDriveLabelsV2betaLabelPermission | 
    try {
      GoogleAppsDriveLabelsV2betaLabelPermission result = apiInstance.drivelabelsLabelsRevisionsUpdatePermissions(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, useAdminAccess, googleAppsDriveLabelsV2betaLabelPermission);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LabelsApi#drivelabelsLabelsRevisionsUpdatePermissions");
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
| **parent** | **String**| Required. The parent Label resource name. | |
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
| **useAdminAccess** | **Boolean**| Set to &#x60;true&#x60; in order to use the user&#39;s admin credentials. The server will verify the user is an admin for the Label before allowing access. | [optional] |
| **googleAppsDriveLabelsV2betaLabelPermission** | [**GoogleAppsDriveLabelsV2betaLabelPermission**](GoogleAppsDriveLabelsV2betaLabelPermission.md)|  | [optional] |

### Return type

[**GoogleAppsDriveLabelsV2betaLabelPermission**](GoogleAppsDriveLabelsV2betaLabelPermission.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="drivelabelsLabelsUpdateLabelCopyMode"></a>
# **drivelabelsLabelsUpdateLabelCopyMode**
> GoogleAppsDriveLabelsV2betaLabel drivelabelsLabelsUpdateLabelCopyMode(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleAppsDriveLabelsV2betaUpdateLabelCopyModeRequest)



Updates a Label&#39;s &#x60;CopyMode&#x60;. Changes to this policy are not revisioned, do not require publishing, and take effect immediately.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LabelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://drivelabels.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    LabelsApi apiInstance = new LabelsApi(defaultClient);
    String name = "name_example"; // String | Required. The resource name of the Label to update.
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
    GoogleAppsDriveLabelsV2betaUpdateLabelCopyModeRequest googleAppsDriveLabelsV2betaUpdateLabelCopyModeRequest = new GoogleAppsDriveLabelsV2betaUpdateLabelCopyModeRequest(); // GoogleAppsDriveLabelsV2betaUpdateLabelCopyModeRequest | 
    try {
      GoogleAppsDriveLabelsV2betaLabel result = apiInstance.drivelabelsLabelsUpdateLabelCopyMode(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleAppsDriveLabelsV2betaUpdateLabelCopyModeRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LabelsApi#drivelabelsLabelsUpdateLabelCopyMode");
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
| **name** | **String**| Required. The resource name of the Label to update. | |
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
| **googleAppsDriveLabelsV2betaUpdateLabelCopyModeRequest** | [**GoogleAppsDriveLabelsV2betaUpdateLabelCopyModeRequest**](GoogleAppsDriveLabelsV2betaUpdateLabelCopyModeRequest.md)|  | [optional] |

### Return type

[**GoogleAppsDriveLabelsV2betaLabel**](GoogleAppsDriveLabelsV2betaLabel.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

