# PermissionsApi

All URIs are relative to *https://www.googleapis.com/drive/v3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**drivePermissionsCreate**](PermissionsApi.md#drivePermissionsCreate) | **POST** /files/{fileId}/permissions |  |
| [**drivePermissionsDelete**](PermissionsApi.md#drivePermissionsDelete) | **DELETE** /files/{fileId}/permissions/{permissionId} |  |
| [**drivePermissionsGet**](PermissionsApi.md#drivePermissionsGet) | **GET** /files/{fileId}/permissions/{permissionId} |  |
| [**drivePermissionsList**](PermissionsApi.md#drivePermissionsList) | **GET** /files/{fileId}/permissions |  |
| [**drivePermissionsUpdate**](PermissionsApi.md#drivePermissionsUpdate) | **PATCH** /files/{fileId}/permissions/{permissionId} |  |


<a id="drivePermissionsCreate"></a>
# **drivePermissionsCreate**
> Permission drivePermissionsCreate(fileId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, emailMessage, enforceSingleParent, moveToNewOwnersRoot, sendNotificationEmail, supportsAllDrives, supportsTeamDrives, transferOwnership, useDomainAdminAccess, permission)



Creates a permission for a file or shared drive. **Warning:** Concurrent permissions operations on the same file are not supported; only the last update is applied.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PermissionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/drive/v3");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PermissionsApi apiInstance = new PermissionsApi(defaultClient);
    String fileId = "fileId_example"; // String | The ID of the file or shared drive.
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
    String emailMessage = "emailMessage_example"; // String | A plain text custom message to include in the notification email.
    Boolean enforceSingleParent = true; // Boolean | Deprecated: See `moveToNewOwnersRoot` for details.
    Boolean moveToNewOwnersRoot = true; // Boolean | This parameter will only take effect if the item is not in a shared drive and the request is attempting to transfer the ownership of the item. If set to `true`, the item will be moved to the new owner's My Drive root folder and all prior parents removed. If set to `false`, parents are not changed.
    Boolean sendNotificationEmail = true; // Boolean | Whether to send a notification email when sharing to users or groups. This defaults to true for users and groups, and is not allowed for other requests. It must not be disabled for ownership transfers.
    Boolean supportsAllDrives = true; // Boolean | Whether the requesting application supports both My Drives and shared drives.
    Boolean supportsTeamDrives = true; // Boolean | Deprecated: Use `supportsAllDrives` instead.
    Boolean transferOwnership = true; // Boolean | Whether to transfer ownership to the specified user and downgrade the current owner to a writer. This parameter is required as an acknowledgement of the side effect.
    Boolean useDomainAdminAccess = true; // Boolean | Issue the request as a domain administrator; if set to true, then the requester will be granted access if the file ID parameter refers to a shared drive and the requester is an administrator of the domain to which the shared drive belongs.
    Permission permission = new Permission(); // Permission | 
    try {
      Permission result = apiInstance.drivePermissionsCreate(fileId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, emailMessage, enforceSingleParent, moveToNewOwnersRoot, sendNotificationEmail, supportsAllDrives, supportsTeamDrives, transferOwnership, useDomainAdminAccess, permission);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PermissionsApi#drivePermissionsCreate");
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
| **fileId** | **String**| The ID of the file or shared drive. | |
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
| **emailMessage** | **String**| A plain text custom message to include in the notification email. | [optional] |
| **enforceSingleParent** | **Boolean**| Deprecated: See &#x60;moveToNewOwnersRoot&#x60; for details. | [optional] |
| **moveToNewOwnersRoot** | **Boolean**| This parameter will only take effect if the item is not in a shared drive and the request is attempting to transfer the ownership of the item. If set to &#x60;true&#x60;, the item will be moved to the new owner&#39;s My Drive root folder and all prior parents removed. If set to &#x60;false&#x60;, parents are not changed. | [optional] |
| **sendNotificationEmail** | **Boolean**| Whether to send a notification email when sharing to users or groups. This defaults to true for users and groups, and is not allowed for other requests. It must not be disabled for ownership transfers. | [optional] |
| **supportsAllDrives** | **Boolean**| Whether the requesting application supports both My Drives and shared drives. | [optional] |
| **supportsTeamDrives** | **Boolean**| Deprecated: Use &#x60;supportsAllDrives&#x60; instead. | [optional] |
| **transferOwnership** | **Boolean**| Whether to transfer ownership to the specified user and downgrade the current owner to a writer. This parameter is required as an acknowledgement of the side effect. | [optional] |
| **useDomainAdminAccess** | **Boolean**| Issue the request as a domain administrator; if set to true, then the requester will be granted access if the file ID parameter refers to a shared drive and the requester is an administrator of the domain to which the shared drive belongs. | [optional] |
| **permission** | [**Permission**](Permission.md)|  | [optional] |

### Return type

[**Permission**](Permission.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="drivePermissionsDelete"></a>
# **drivePermissionsDelete**
> drivePermissionsDelete(fileId, permissionId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, supportsAllDrives, supportsTeamDrives, useDomainAdminAccess)



Deletes a permission. **Warning:** Concurrent permissions operations on the same file are not supported; only the last update is applied.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PermissionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/drive/v3");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PermissionsApi apiInstance = new PermissionsApi(defaultClient);
    String fileId = "fileId_example"; // String | The ID of the file or shared drive.
    String permissionId = "permissionId_example"; // String | The ID of the permission.
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
    Boolean supportsAllDrives = true; // Boolean | Whether the requesting application supports both My Drives and shared drives.
    Boolean supportsTeamDrives = true; // Boolean | Deprecated: Use `supportsAllDrives` instead.
    Boolean useDomainAdminAccess = true; // Boolean | Issue the request as a domain administrator; if set to true, then the requester will be granted access if the file ID parameter refers to a shared drive and the requester is an administrator of the domain to which the shared drive belongs.
    try {
      apiInstance.drivePermissionsDelete(fileId, permissionId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, supportsAllDrives, supportsTeamDrives, useDomainAdminAccess);
    } catch (ApiException e) {
      System.err.println("Exception when calling PermissionsApi#drivePermissionsDelete");
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
| **fileId** | **String**| The ID of the file or shared drive. | |
| **permissionId** | **String**| The ID of the permission. | |
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
| **supportsAllDrives** | **Boolean**| Whether the requesting application supports both My Drives and shared drives. | [optional] |
| **supportsTeamDrives** | **Boolean**| Deprecated: Use &#x60;supportsAllDrives&#x60; instead. | [optional] |
| **useDomainAdminAccess** | **Boolean**| Issue the request as a domain administrator; if set to true, then the requester will be granted access if the file ID parameter refers to a shared drive and the requester is an administrator of the domain to which the shared drive belongs. | [optional] |

### Return type

null (empty response body)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="drivePermissionsGet"></a>
# **drivePermissionsGet**
> Permission drivePermissionsGet(fileId, permissionId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, supportsAllDrives, supportsTeamDrives, useDomainAdminAccess)



Gets a permission by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PermissionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/drive/v3");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PermissionsApi apiInstance = new PermissionsApi(defaultClient);
    String fileId = "fileId_example"; // String | The ID of the file.
    String permissionId = "permissionId_example"; // String | The ID of the permission.
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
    Boolean supportsAllDrives = true; // Boolean | Whether the requesting application supports both My Drives and shared drives.
    Boolean supportsTeamDrives = true; // Boolean | Deprecated: Use `supportsAllDrives` instead.
    Boolean useDomainAdminAccess = true; // Boolean | Issue the request as a domain administrator; if set to true, then the requester will be granted access if the file ID parameter refers to a shared drive and the requester is an administrator of the domain to which the shared drive belongs.
    try {
      Permission result = apiInstance.drivePermissionsGet(fileId, permissionId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, supportsAllDrives, supportsTeamDrives, useDomainAdminAccess);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PermissionsApi#drivePermissionsGet");
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
| **fileId** | **String**| The ID of the file. | |
| **permissionId** | **String**| The ID of the permission. | |
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
| **supportsAllDrives** | **Boolean**| Whether the requesting application supports both My Drives and shared drives. | [optional] |
| **supportsTeamDrives** | **Boolean**| Deprecated: Use &#x60;supportsAllDrives&#x60; instead. | [optional] |
| **useDomainAdminAccess** | **Boolean**| Issue the request as a domain administrator; if set to true, then the requester will be granted access if the file ID parameter refers to a shared drive and the requester is an administrator of the domain to which the shared drive belongs. | [optional] |

### Return type

[**Permission**](Permission.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="drivePermissionsList"></a>
# **drivePermissionsList**
> PermissionList drivePermissionsList(fileId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, includePermissionsForView, pageSize, pageToken, supportsAllDrives, supportsTeamDrives, useDomainAdminAccess)



Lists a file&#39;s or shared drive&#39;s permissions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PermissionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/drive/v3");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PermissionsApi apiInstance = new PermissionsApi(defaultClient);
    String fileId = "fileId_example"; // String | The ID of the file or shared drive.
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
    String includePermissionsForView = "includePermissionsForView_example"; // String | Specifies which additional view's permissions to include in the response. Only 'published' is supported.
    Integer pageSize = 56; // Integer | The maximum number of permissions to return per page. When not set for files in a shared drive, at most 100 results will be returned. When not set for files that are not in a shared drive, the entire list will be returned.
    String pageToken = "pageToken_example"; // String | The token for continuing a previous list request on the next page. This should be set to the value of 'nextPageToken' from the previous response.
    Boolean supportsAllDrives = true; // Boolean | Whether the requesting application supports both My Drives and shared drives.
    Boolean supportsTeamDrives = true; // Boolean | Deprecated: Use `supportsAllDrives` instead.
    Boolean useDomainAdminAccess = true; // Boolean | Issue the request as a domain administrator; if set to true, then the requester will be granted access if the file ID parameter refers to a shared drive and the requester is an administrator of the domain to which the shared drive belongs.
    try {
      PermissionList result = apiInstance.drivePermissionsList(fileId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, includePermissionsForView, pageSize, pageToken, supportsAllDrives, supportsTeamDrives, useDomainAdminAccess);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PermissionsApi#drivePermissionsList");
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
| **fileId** | **String**| The ID of the file or shared drive. | |
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
| **includePermissionsForView** | **String**| Specifies which additional view&#39;s permissions to include in the response. Only &#39;published&#39; is supported. | [optional] |
| **pageSize** | **Integer**| The maximum number of permissions to return per page. When not set for files in a shared drive, at most 100 results will be returned. When not set for files that are not in a shared drive, the entire list will be returned. | [optional] |
| **pageToken** | **String**| The token for continuing a previous list request on the next page. This should be set to the value of &#39;nextPageToken&#39; from the previous response. | [optional] |
| **supportsAllDrives** | **Boolean**| Whether the requesting application supports both My Drives and shared drives. | [optional] |
| **supportsTeamDrives** | **Boolean**| Deprecated: Use &#x60;supportsAllDrives&#x60; instead. | [optional] |
| **useDomainAdminAccess** | **Boolean**| Issue the request as a domain administrator; if set to true, then the requester will be granted access if the file ID parameter refers to a shared drive and the requester is an administrator of the domain to which the shared drive belongs. | [optional] |

### Return type

[**PermissionList**](PermissionList.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="drivePermissionsUpdate"></a>
# **drivePermissionsUpdate**
> Permission drivePermissionsUpdate(fileId, permissionId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, removeExpiration, supportsAllDrives, supportsTeamDrives, transferOwnership, useDomainAdminAccess, permission)



Updates a permission with patch semantics. **Warning:** Concurrent permissions operations on the same file are not supported; only the last update is applied.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PermissionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/drive/v3");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PermissionsApi apiInstance = new PermissionsApi(defaultClient);
    String fileId = "fileId_example"; // String | The ID of the file or shared drive.
    String permissionId = "permissionId_example"; // String | The ID of the permission.
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
    Boolean removeExpiration = true; // Boolean | Whether to remove the expiration date.
    Boolean supportsAllDrives = true; // Boolean | Whether the requesting application supports both My Drives and shared drives.
    Boolean supportsTeamDrives = true; // Boolean | Deprecated: Use `supportsAllDrives` instead.
    Boolean transferOwnership = true; // Boolean | Whether to transfer ownership to the specified user and downgrade the current owner to a writer. This parameter is required as an acknowledgement of the side effect.
    Boolean useDomainAdminAccess = true; // Boolean | Issue the request as a domain administrator; if set to true, then the requester will be granted access if the file ID parameter refers to a shared drive and the requester is an administrator of the domain to which the shared drive belongs.
    Permission permission = new Permission(); // Permission | 
    try {
      Permission result = apiInstance.drivePermissionsUpdate(fileId, permissionId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, removeExpiration, supportsAllDrives, supportsTeamDrives, transferOwnership, useDomainAdminAccess, permission);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PermissionsApi#drivePermissionsUpdate");
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
| **fileId** | **String**| The ID of the file or shared drive. | |
| **permissionId** | **String**| The ID of the permission. | |
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
| **removeExpiration** | **Boolean**| Whether to remove the expiration date. | [optional] |
| **supportsAllDrives** | **Boolean**| Whether the requesting application supports both My Drives and shared drives. | [optional] |
| **supportsTeamDrives** | **Boolean**| Deprecated: Use &#x60;supportsAllDrives&#x60; instead. | [optional] |
| **transferOwnership** | **Boolean**| Whether to transfer ownership to the specified user and downgrade the current owner to a writer. This parameter is required as an acknowledgement of the side effect. | [optional] |
| **useDomainAdminAccess** | **Boolean**| Issue the request as a domain administrator; if set to true, then the requester will be granted access if the file ID parameter refers to a shared drive and the requester is an administrator of the domain to which the shared drive belongs. | [optional] |
| **permission** | [**Permission**](Permission.md)|  | [optional] |

### Return type

[**Permission**](Permission.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

