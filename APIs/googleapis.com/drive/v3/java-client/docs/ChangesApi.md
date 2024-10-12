# ChangesApi

All URIs are relative to *https://www.googleapis.com/drive/v3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**driveChangesGetStartPageToken**](ChangesApi.md#driveChangesGetStartPageToken) | **GET** /changes/startPageToken |  |
| [**driveChangesList**](ChangesApi.md#driveChangesList) | **GET** /changes |  |
| [**driveChangesWatch**](ChangesApi.md#driveChangesWatch) | **POST** /changes/watch |  |


<a id="driveChangesGetStartPageToken"></a>
# **driveChangesGetStartPageToken**
> StartPageToken driveChangesGetStartPageToken($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, driveId, supportsAllDrives, supportsTeamDrives, teamDriveId)



Gets the starting pageToken for listing future changes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChangesApi;

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

    ChangesApi apiInstance = new ChangesApi(defaultClient);
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
    String driveId = "driveId_example"; // String | The ID of the shared drive for which the starting pageToken for listing future changes from that shared drive will be returned.
    Boolean supportsAllDrives = true; // Boolean | Whether the requesting application supports both My Drives and shared drives.
    Boolean supportsTeamDrives = true; // Boolean | Deprecated: Use `supportsAllDrives` instead.
    String teamDriveId = "teamDriveId_example"; // String | Deprecated: Use `driveId` instead.
    try {
      StartPageToken result = apiInstance.driveChangesGetStartPageToken($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, driveId, supportsAllDrives, supportsTeamDrives, teamDriveId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChangesApi#driveChangesGetStartPageToken");
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
| **driveId** | **String**| The ID of the shared drive for which the starting pageToken for listing future changes from that shared drive will be returned. | [optional] |
| **supportsAllDrives** | **Boolean**| Whether the requesting application supports both My Drives and shared drives. | [optional] |
| **supportsTeamDrives** | **Boolean**| Deprecated: Use &#x60;supportsAllDrives&#x60; instead. | [optional] |
| **teamDriveId** | **String**| Deprecated: Use &#x60;driveId&#x60; instead. | [optional] |

### Return type

[**StartPageToken**](StartPageToken.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="driveChangesList"></a>
# **driveChangesList**
> ChangeList driveChangesList(pageToken, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, driveId, includeCorpusRemovals, includeItemsFromAllDrives, includeLabels, includePermissionsForView, includeRemoved, includeTeamDriveItems, pageSize, restrictToMyDrive, spaces, supportsAllDrives, supportsTeamDrives, teamDriveId)



Lists the changes for a user or shared drive.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChangesApi;

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

    ChangesApi apiInstance = new ChangesApi(defaultClient);
    String pageToken = "pageToken_example"; // String | The token for continuing a previous list request on the next page. This should be set to the value of 'nextPageToken' from the previous response or to the response from the getStartPageToken method.
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
    String driveId = "driveId_example"; // String | The shared drive from which changes will be returned. If specified the change IDs will be reflective of the shared drive; use the combined drive ID and change ID as an identifier.
    Boolean includeCorpusRemovals = true; // Boolean | Whether changes should include the file resource if the file is still accessible by the user at the time of the request, even when a file was removed from the list of changes and there will be no further change entries for this file.
    Boolean includeItemsFromAllDrives = true; // Boolean | Whether both My Drive and shared drive items should be included in results.
    String includeLabels = "includeLabels_example"; // String | A comma-separated list of IDs of labels to include in the `labelInfo` part of the response.
    String includePermissionsForView = "includePermissionsForView_example"; // String | Specifies which additional view's permissions to include in the response. Only 'published' is supported.
    Boolean includeRemoved = true; // Boolean | Whether to include changes indicating that items have been removed from the list of changes, for example by deletion or loss of access.
    Boolean includeTeamDriveItems = true; // Boolean | Deprecated: Use `includeItemsFromAllDrives` instead.
    Integer pageSize = 56; // Integer | The maximum number of changes to return per page.
    Boolean restrictToMyDrive = true; // Boolean | Whether to restrict the results to changes inside the My Drive hierarchy. This omits changes to files such as those in the Application Data folder or shared files which have not been added to My Drive.
    String spaces = "spaces_example"; // String | A comma-separated list of spaces to query within the corpora. Supported values are 'drive' and 'appDataFolder'.
    Boolean supportsAllDrives = true; // Boolean | Whether the requesting application supports both My Drives and shared drives.
    Boolean supportsTeamDrives = true; // Boolean | Deprecated: Use `supportsAllDrives` instead.
    String teamDriveId = "teamDriveId_example"; // String | Deprecated: Use `driveId` instead.
    try {
      ChangeList result = apiInstance.driveChangesList(pageToken, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, driveId, includeCorpusRemovals, includeItemsFromAllDrives, includeLabels, includePermissionsForView, includeRemoved, includeTeamDriveItems, pageSize, restrictToMyDrive, spaces, supportsAllDrives, supportsTeamDrives, teamDriveId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChangesApi#driveChangesList");
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
| **pageToken** | **String**| The token for continuing a previous list request on the next page. This should be set to the value of &#39;nextPageToken&#39; from the previous response or to the response from the getStartPageToken method. | |
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
| **driveId** | **String**| The shared drive from which changes will be returned. If specified the change IDs will be reflective of the shared drive; use the combined drive ID and change ID as an identifier. | [optional] |
| **includeCorpusRemovals** | **Boolean**| Whether changes should include the file resource if the file is still accessible by the user at the time of the request, even when a file was removed from the list of changes and there will be no further change entries for this file. | [optional] |
| **includeItemsFromAllDrives** | **Boolean**| Whether both My Drive and shared drive items should be included in results. | [optional] |
| **includeLabels** | **String**| A comma-separated list of IDs of labels to include in the &#x60;labelInfo&#x60; part of the response. | [optional] |
| **includePermissionsForView** | **String**| Specifies which additional view&#39;s permissions to include in the response. Only &#39;published&#39; is supported. | [optional] |
| **includeRemoved** | **Boolean**| Whether to include changes indicating that items have been removed from the list of changes, for example by deletion or loss of access. | [optional] |
| **includeTeamDriveItems** | **Boolean**| Deprecated: Use &#x60;includeItemsFromAllDrives&#x60; instead. | [optional] |
| **pageSize** | **Integer**| The maximum number of changes to return per page. | [optional] |
| **restrictToMyDrive** | **Boolean**| Whether to restrict the results to changes inside the My Drive hierarchy. This omits changes to files such as those in the Application Data folder or shared files which have not been added to My Drive. | [optional] |
| **spaces** | **String**| A comma-separated list of spaces to query within the corpora. Supported values are &#39;drive&#39; and &#39;appDataFolder&#39;. | [optional] |
| **supportsAllDrives** | **Boolean**| Whether the requesting application supports both My Drives and shared drives. | [optional] |
| **supportsTeamDrives** | **Boolean**| Deprecated: Use &#x60;supportsAllDrives&#x60; instead. | [optional] |
| **teamDriveId** | **String**| Deprecated: Use &#x60;driveId&#x60; instead. | [optional] |

### Return type

[**ChangeList**](ChangeList.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="driveChangesWatch"></a>
# **driveChangesWatch**
> Channel driveChangesWatch(pageToken, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, driveId, includeCorpusRemovals, includeItemsFromAllDrives, includeLabels, includePermissionsForView, includeRemoved, includeTeamDriveItems, pageSize, restrictToMyDrive, spaces, supportsAllDrives, supportsTeamDrives, teamDriveId, channel)



Subscribes to changes for a user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChangesApi;

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

    ChangesApi apiInstance = new ChangesApi(defaultClient);
    String pageToken = "pageToken_example"; // String | The token for continuing a previous list request on the next page. This should be set to the value of 'nextPageToken' from the previous response or to the response from the getStartPageToken method.
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
    String driveId = "driveId_example"; // String | The shared drive from which changes will be returned. If specified the change IDs will be reflective of the shared drive; use the combined drive ID and change ID as an identifier.
    Boolean includeCorpusRemovals = true; // Boolean | Whether changes should include the file resource if the file is still accessible by the user at the time of the request, even when a file was removed from the list of changes and there will be no further change entries for this file.
    Boolean includeItemsFromAllDrives = true; // Boolean | Whether both My Drive and shared drive items should be included in results.
    String includeLabels = "includeLabels_example"; // String | A comma-separated list of IDs of labels to include in the `labelInfo` part of the response.
    String includePermissionsForView = "includePermissionsForView_example"; // String | Specifies which additional view's permissions to include in the response. Only 'published' is supported.
    Boolean includeRemoved = true; // Boolean | Whether to include changes indicating that items have been removed from the list of changes, for example by deletion or loss of access.
    Boolean includeTeamDriveItems = true; // Boolean | Deprecated: Use `includeItemsFromAllDrives` instead.
    Integer pageSize = 56; // Integer | The maximum number of changes to return per page.
    Boolean restrictToMyDrive = true; // Boolean | Whether to restrict the results to changes inside the My Drive hierarchy. This omits changes to files such as those in the Application Data folder or shared files which have not been added to My Drive.
    String spaces = "spaces_example"; // String | A comma-separated list of spaces to query within the corpora. Supported values are 'drive' and 'appDataFolder'.
    Boolean supportsAllDrives = true; // Boolean | Whether the requesting application supports both My Drives and shared drives.
    Boolean supportsTeamDrives = true; // Boolean | Deprecated: Use `supportsAllDrives` instead.
    String teamDriveId = "teamDriveId_example"; // String | Deprecated: Use `driveId` instead.
    Channel channel = new Channel(); // Channel | 
    try {
      Channel result = apiInstance.driveChangesWatch(pageToken, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, driveId, includeCorpusRemovals, includeItemsFromAllDrives, includeLabels, includePermissionsForView, includeRemoved, includeTeamDriveItems, pageSize, restrictToMyDrive, spaces, supportsAllDrives, supportsTeamDrives, teamDriveId, channel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChangesApi#driveChangesWatch");
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
| **pageToken** | **String**| The token for continuing a previous list request on the next page. This should be set to the value of &#39;nextPageToken&#39; from the previous response or to the response from the getStartPageToken method. | |
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
| **driveId** | **String**| The shared drive from which changes will be returned. If specified the change IDs will be reflective of the shared drive; use the combined drive ID and change ID as an identifier. | [optional] |
| **includeCorpusRemovals** | **Boolean**| Whether changes should include the file resource if the file is still accessible by the user at the time of the request, even when a file was removed from the list of changes and there will be no further change entries for this file. | [optional] |
| **includeItemsFromAllDrives** | **Boolean**| Whether both My Drive and shared drive items should be included in results. | [optional] |
| **includeLabels** | **String**| A comma-separated list of IDs of labels to include in the &#x60;labelInfo&#x60; part of the response. | [optional] |
| **includePermissionsForView** | **String**| Specifies which additional view&#39;s permissions to include in the response. Only &#39;published&#39; is supported. | [optional] |
| **includeRemoved** | **Boolean**| Whether to include changes indicating that items have been removed from the list of changes, for example by deletion or loss of access. | [optional] |
| **includeTeamDriveItems** | **Boolean**| Deprecated: Use &#x60;includeItemsFromAllDrives&#x60; instead. | [optional] |
| **pageSize** | **Integer**| The maximum number of changes to return per page. | [optional] |
| **restrictToMyDrive** | **Boolean**| Whether to restrict the results to changes inside the My Drive hierarchy. This omits changes to files such as those in the Application Data folder or shared files which have not been added to My Drive. | [optional] |
| **spaces** | **String**| A comma-separated list of spaces to query within the corpora. Supported values are &#39;drive&#39; and &#39;appDataFolder&#39;. | [optional] |
| **supportsAllDrives** | **Boolean**| Whether the requesting application supports both My Drives and shared drives. | [optional] |
| **supportsTeamDrives** | **Boolean**| Deprecated: Use &#x60;supportsAllDrives&#x60; instead. | [optional] |
| **teamDriveId** | **String**| Deprecated: Use &#x60;driveId&#x60; instead. | [optional] |
| **channel** | [**Channel**](Channel.md)|  | [optional] |

### Return type

[**Channel**](Channel.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

