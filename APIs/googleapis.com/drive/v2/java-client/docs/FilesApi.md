# FilesApi

All URIs are relative to *https://www.googleapis.com/drive/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**driveFilesCopy**](FilesApi.md#driveFilesCopy) | **POST** /files/{fileId}/copy |  |
| [**driveFilesDelete**](FilesApi.md#driveFilesDelete) | **DELETE** /files/{fileId} |  |
| [**driveFilesEmptyTrash**](FilesApi.md#driveFilesEmptyTrash) | **DELETE** /files/trash |  |
| [**driveFilesExport**](FilesApi.md#driveFilesExport) | **GET** /files/{fileId}/export |  |
| [**driveFilesGenerateIds**](FilesApi.md#driveFilesGenerateIds) | **GET** /files/generateIds |  |
| [**driveFilesGet**](FilesApi.md#driveFilesGet) | **GET** /files/{fileId} |  |
| [**driveFilesInsert**](FilesApi.md#driveFilesInsert) | **POST** /files |  |
| [**driveFilesList**](FilesApi.md#driveFilesList) | **GET** /files |  |
| [**driveFilesListLabels**](FilesApi.md#driveFilesListLabels) | **GET** /files/{fileId}/listLabels |  |
| [**driveFilesModifyLabels**](FilesApi.md#driveFilesModifyLabels) | **POST** /files/{fileId}/modifyLabels |  |
| [**driveFilesPatch**](FilesApi.md#driveFilesPatch) | **PATCH** /files/{fileId} |  |
| [**driveFilesTouch**](FilesApi.md#driveFilesTouch) | **POST** /files/{fileId}/touch |  |
| [**driveFilesTrash**](FilesApi.md#driveFilesTrash) | **POST** /files/{fileId}/trash |  |
| [**driveFilesUntrash**](FilesApi.md#driveFilesUntrash) | **POST** /files/{fileId}/untrash |  |
| [**driveFilesUpdate**](FilesApi.md#driveFilesUpdate) | **PUT** /files/{fileId} |  |
| [**driveFilesWatch**](FilesApi.md#driveFilesWatch) | **POST** /files/{fileId}/watch |  |


<a id="driveFilesCopy"></a>
# **driveFilesCopy**
> ModelFile driveFilesCopy(fileId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, convert, enforceSingleParent, includeLabels, includePermissionsForView, ocr, ocrLanguage, pinned, supportsAllDrives, supportsTeamDrives, timedTextLanguage, timedTextTrackName, visibility, modelFile)



Creates a copy of the specified file.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/drive/v2");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String fileId = "fileId_example"; // String | The ID of the file to copy.
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
    Boolean convert = true; // Boolean | Whether to convert this file to the corresponding Docs Editors format.
    Boolean enforceSingleParent = true; // Boolean | Deprecated: Copying files into multiple folders is no longer supported. Use shortcuts instead.
    String includeLabels = "includeLabels_example"; // String | A comma-separated list of IDs of labels to include in the `labelInfo` part of the response.
    String includePermissionsForView = "includePermissionsForView_example"; // String | Specifies which additional view's permissions to include in the response. Only `published` is supported.
    Boolean ocr = true; // Boolean | Whether to attempt OCR on .jpg, .png, .gif, or .pdf uploads.
    String ocrLanguage = "ocrLanguage_example"; // String | If `ocr` is true, hints at the language to use. Valid values are BCP 47 codes.
    Boolean pinned = true; // Boolean | Whether to pin the head revision of the new copy. A file can have a maximum of 200 pinned revisions.
    Boolean supportsAllDrives = true; // Boolean | Whether the requesting application supports both My Drives and shared drives.
    Boolean supportsTeamDrives = true; // Boolean | Deprecated: Use `supportsAllDrives` instead.
    String timedTextLanguage = "timedTextLanguage_example"; // String | The language of the timed text.
    String timedTextTrackName = "timedTextTrackName_example"; // String | The timed text track name.
    String visibility = "DEFAULT"; // String | The visibility of the new file. This parameter is only relevant when the source is not a native Google Doc and convert=false.
    ModelFile modelFile = new ModelFile(); // ModelFile | 
    try {
      ModelFile result = apiInstance.driveFilesCopy(fileId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, convert, enforceSingleParent, includeLabels, includePermissionsForView, ocr, ocrLanguage, pinned, supportsAllDrives, supportsTeamDrives, timedTextLanguage, timedTextTrackName, visibility, modelFile);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#driveFilesCopy");
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
| **fileId** | **String**| The ID of the file to copy. | |
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
| **convert** | **Boolean**| Whether to convert this file to the corresponding Docs Editors format. | [optional] |
| **enforceSingleParent** | **Boolean**| Deprecated: Copying files into multiple folders is no longer supported. Use shortcuts instead. | [optional] |
| **includeLabels** | **String**| A comma-separated list of IDs of labels to include in the &#x60;labelInfo&#x60; part of the response. | [optional] |
| **includePermissionsForView** | **String**| Specifies which additional view&#39;s permissions to include in the response. Only &#x60;published&#x60; is supported. | [optional] |
| **ocr** | **Boolean**| Whether to attempt OCR on .jpg, .png, .gif, or .pdf uploads. | [optional] |
| **ocrLanguage** | **String**| If &#x60;ocr&#x60; is true, hints at the language to use. Valid values are BCP 47 codes. | [optional] |
| **pinned** | **Boolean**| Whether to pin the head revision of the new copy. A file can have a maximum of 200 pinned revisions. | [optional] |
| **supportsAllDrives** | **Boolean**| Whether the requesting application supports both My Drives and shared drives. | [optional] |
| **supportsTeamDrives** | **Boolean**| Deprecated: Use &#x60;supportsAllDrives&#x60; instead. | [optional] |
| **timedTextLanguage** | **String**| The language of the timed text. | [optional] |
| **timedTextTrackName** | **String**| The timed text track name. | [optional] |
| **visibility** | **String**| The visibility of the new file. This parameter is only relevant when the source is not a native Google Doc and convert&#x3D;false. | [optional] [enum: DEFAULT, PRIVATE] |
| **modelFile** | [**ModelFile**](ModelFile.md)|  | [optional] |

### Return type

[**ModelFile**](ModelFile.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="driveFilesDelete"></a>
# **driveFilesDelete**
> driveFilesDelete(fileId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, enforceSingleParent, supportsAllDrives, supportsTeamDrives)



Permanently deletes a file owned by the user without moving it to the trash. If the file belongs to a shared drive, the user must be an &#x60;organizer&#x60; on the parent folder. If the target is a folder, all descendants owned by the user are also deleted.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/drive/v2");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String fileId = "fileId_example"; // String | The ID of the file to delete.
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
    Boolean enforceSingleParent = true; // Boolean | Deprecated: If an item is not in a shared drive and its last parent is deleted but the item itself is not, the item is placed under its owner's root.
    Boolean supportsAllDrives = true; // Boolean | Whether the requesting application supports both My Drives and shared drives.
    Boolean supportsTeamDrives = true; // Boolean | Deprecated: Use `supportsAllDrives` instead.
    try {
      apiInstance.driveFilesDelete(fileId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, enforceSingleParent, supportsAllDrives, supportsTeamDrives);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#driveFilesDelete");
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
| **fileId** | **String**| The ID of the file to delete. | |
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
| **enforceSingleParent** | **Boolean**| Deprecated: If an item is not in a shared drive and its last parent is deleted but the item itself is not, the item is placed under its owner&#39;s root. | [optional] |
| **supportsAllDrives** | **Boolean**| Whether the requesting application supports both My Drives and shared drives. | [optional] |
| **supportsTeamDrives** | **Boolean**| Deprecated: Use &#x60;supportsAllDrives&#x60; instead. | [optional] |

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

<a id="driveFilesEmptyTrash"></a>
# **driveFilesEmptyTrash**
> driveFilesEmptyTrash($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, driveId, enforceSingleParent)



Permanently deletes all of the user&#39;s trashed files.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/drive/v2");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    FilesApi apiInstance = new FilesApi(defaultClient);
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
    String driveId = "driveId_example"; // String | If set, empties the trash of the provided shared drive.
    Boolean enforceSingleParent = true; // Boolean | Deprecated: If an item is not in a shared drive and its last parent is deleted but the item itself is not, the item is placed under its owner's root.
    try {
      apiInstance.driveFilesEmptyTrash($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, driveId, enforceSingleParent);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#driveFilesEmptyTrash");
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
| **driveId** | **String**| If set, empties the trash of the provided shared drive. | [optional] |
| **enforceSingleParent** | **Boolean**| Deprecated: If an item is not in a shared drive and its last parent is deleted but the item itself is not, the item is placed under its owner&#39;s root. | [optional] |

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

<a id="driveFilesExport"></a>
# **driveFilesExport**
> driveFilesExport(fileId, mimeType, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType)



Exports a Google Workspace document to the requested MIME type and returns exported byte content. Note that the exported content is limited to 10MB.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/drive/v2");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String fileId = "fileId_example"; // String | The ID of the file.
    String mimeType = "mimeType_example"; // String | Required. The MIME type of the format requested for this export.
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
      apiInstance.driveFilesExport(fileId, mimeType, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#driveFilesExport");
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
| **mimeType** | **String**| Required. The MIME type of the format requested for this export. | |
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

<a id="driveFilesGenerateIds"></a>
# **driveFilesGenerateIds**
> GeneratedIds driveFilesGenerateIds($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, maxResults, space, type)



Generates a set of file IDs which can be provided in insert or copy requests.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/drive/v2");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    FilesApi apiInstance = new FilesApi(defaultClient);
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
    Integer maxResults = 56; // Integer | Maximum number of IDs to return.
    String space = "space_example"; // String | The space in which the IDs can be used to create new files. Supported values are `drive` and `appDataFolder`. (Default: `drive`)
    String type = "type_example"; // String | The type of items which the IDs can be used for. Supported values are `files` and `shortcuts`. Note that `shortcuts` are only supported in the `drive` `space`. (Default: `files`)
    try {
      GeneratedIds result = apiInstance.driveFilesGenerateIds($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, maxResults, space, type);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#driveFilesGenerateIds");
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
| **maxResults** | **Integer**| Maximum number of IDs to return. | [optional] |
| **space** | **String**| The space in which the IDs can be used to create new files. Supported values are &#x60;drive&#x60; and &#x60;appDataFolder&#x60;. (Default: &#x60;drive&#x60;) | [optional] |
| **type** | **String**| The type of items which the IDs can be used for. Supported values are &#x60;files&#x60; and &#x60;shortcuts&#x60;. Note that &#x60;shortcuts&#x60; are only supported in the &#x60;drive&#x60; &#x60;space&#x60;. (Default: &#x60;files&#x60;) | [optional] |

### Return type

[**GeneratedIds**](GeneratedIds.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="driveFilesGet"></a>
# **driveFilesGet**
> ModelFile driveFilesGet(fileId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, acknowledgeAbuse, includeLabels, includePermissionsForView, projection, revisionId, supportsAllDrives, supportsTeamDrives, updateViewedDate)



 Gets a file&#39;s metadata or content by ID. If you provide the URL parameter &#x60;alt&#x3D;media&#x60;, then the response includes the file contents in the response body. Downloading content with &#x60;alt&#x3D;media&#x60; only works if the file is stored in Drive. To download Google Docs, Sheets, and Slides use [&#x60;files.export&#x60;](/drive/api/reference/rest/v2/files/export) instead. For more information, see [Download &amp; export files](/drive/api/guides/manage-downloads).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/drive/v2");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String fileId = "fileId_example"; // String | The ID for the file in question.
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
    Boolean acknowledgeAbuse = true; // Boolean | Whether the user is acknowledging the risk of downloading known malware or other abusive files.
    String includeLabels = "includeLabels_example"; // String | A comma-separated list of IDs of labels to include in the `labelInfo` part of the response.
    String includePermissionsForView = "includePermissionsForView_example"; // String | Specifies which additional view's permissions to include in the response. Only `published` is supported.
    String projection = "BASIC"; // String | Deprecated: This parameter has no function.
    String revisionId = "revisionId_example"; // String | Specifies the Revision ID that should be downloaded. Ignored unless alt=media is specified.
    Boolean supportsAllDrives = true; // Boolean | Whether the requesting application supports both My Drives and shared drives.
    Boolean supportsTeamDrives = true; // Boolean | Deprecated: Use `supportsAllDrives` instead.
    Boolean updateViewedDate = true; // Boolean | Deprecated: Use `files.update` with `modifiedDateBehavior=noChange, updateViewedDate=true` and an empty request body.
    try {
      ModelFile result = apiInstance.driveFilesGet(fileId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, acknowledgeAbuse, includeLabels, includePermissionsForView, projection, revisionId, supportsAllDrives, supportsTeamDrives, updateViewedDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#driveFilesGet");
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
| **fileId** | **String**| The ID for the file in question. | |
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
| **acknowledgeAbuse** | **Boolean**| Whether the user is acknowledging the risk of downloading known malware or other abusive files. | [optional] |
| **includeLabels** | **String**| A comma-separated list of IDs of labels to include in the &#x60;labelInfo&#x60; part of the response. | [optional] |
| **includePermissionsForView** | **String**| Specifies which additional view&#39;s permissions to include in the response. Only &#x60;published&#x60; is supported. | [optional] |
| **projection** | **String**| Deprecated: This parameter has no function. | [optional] [enum: BASIC, FULL] |
| **revisionId** | **String**| Specifies the Revision ID that should be downloaded. Ignored unless alt&#x3D;media is specified. | [optional] |
| **supportsAllDrives** | **Boolean**| Whether the requesting application supports both My Drives and shared drives. | [optional] |
| **supportsTeamDrives** | **Boolean**| Deprecated: Use &#x60;supportsAllDrives&#x60; instead. | [optional] |
| **updateViewedDate** | **Boolean**| Deprecated: Use &#x60;files.update&#x60; with &#x60;modifiedDateBehavior&#x3D;noChange, updateViewedDate&#x3D;true&#x60; and an empty request body. | [optional] |

### Return type

[**ModelFile**](ModelFile.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="driveFilesInsert"></a>
# **driveFilesInsert**
> ModelFile driveFilesInsert($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, convert, enforceSingleParent, includeLabels, includePermissionsForView, ocr, ocrLanguage, pinned, supportsAllDrives, supportsTeamDrives, timedTextLanguage, timedTextTrackName, useContentAsIndexableText, visibility, modelFile)



 Inserts a new file. This method supports an *_/upload* URI and accepts uploaded media with the following characteristics: - *Maximum file size:* 5,120 GB - *Accepted Media MIME types:*&#x60;*_/_*&#x60; Note: Specify a valid MIME type, rather than the literal &#x60;*_/_*&#x60; value. The literal &#x60;*_/_*&#x60; is only used to indicate that any valid MIME type can be uploaded. For more information on uploading files, see [Upload file data](/drive/api/guides/manage-uploads). Apps creating shortcuts with &#x60;files.insert&#x60; must specify the MIME type &#x60;application/vnd.google-apps.shortcut&#x60;. Apps should specify a file extension in the &#x60;title&#x60; property when inserting files with the API. For example, an operation to insert a JPEG file should specify something like &#x60;\&quot;title\&quot;: \&quot;cat.jpg\&quot;&#x60; in the metadata. Subsequent &#x60;GET&#x60; requests include the read-only &#x60;fileExtension&#x60; property populated with the extension originally specified in the &#x60;title&#x60; property. When a Google Drive user requests to download a file, or when the file is downloaded through the sync client, Drive builds a full filename (with extension) based on the title. In cases where the extension is missing, Drive attempts to determine the extension based on the file&#39;s MIME type.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/drive/v2");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    FilesApi apiInstance = new FilesApi(defaultClient);
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
    Boolean convert = true; // Boolean | Whether to convert this file to the corresponding Docs Editors format.
    Boolean enforceSingleParent = true; // Boolean | Deprecated: Creating files in multiple folders is no longer supported.
    String includeLabels = "includeLabels_example"; // String | A comma-separated list of IDs of labels to include in the `labelInfo` part of the response.
    String includePermissionsForView = "includePermissionsForView_example"; // String | Specifies which additional view's permissions to include in the response. Only `published` is supported.
    Boolean ocr = true; // Boolean | Whether to attempt OCR on .jpg, .png, .gif, or .pdf uploads.
    String ocrLanguage = "ocrLanguage_example"; // String | If ocr is true, hints at the language to use. Valid values are BCP 47 codes.
    Boolean pinned = true; // Boolean | Whether to pin the head revision of the uploaded file. A file can have a maximum of 200 pinned revisions.
    Boolean supportsAllDrives = true; // Boolean | Whether the requesting application supports both My Drives and shared drives.
    Boolean supportsTeamDrives = true; // Boolean | Deprecated: Use `supportsAllDrives` instead.
    String timedTextLanguage = "timedTextLanguage_example"; // String | The language of the timed text.
    String timedTextTrackName = "timedTextTrackName_example"; // String | The timed text track name.
    Boolean useContentAsIndexableText = true; // Boolean | Whether to use the content as indexable text.
    String visibility = "DEFAULT"; // String | The visibility of the new file. This parameter is only relevant when convert=false.
    ModelFile modelFile = new ModelFile(); // ModelFile | 
    try {
      ModelFile result = apiInstance.driveFilesInsert($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, convert, enforceSingleParent, includeLabels, includePermissionsForView, ocr, ocrLanguage, pinned, supportsAllDrives, supportsTeamDrives, timedTextLanguage, timedTextTrackName, useContentAsIndexableText, visibility, modelFile);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#driveFilesInsert");
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
| **convert** | **Boolean**| Whether to convert this file to the corresponding Docs Editors format. | [optional] |
| **enforceSingleParent** | **Boolean**| Deprecated: Creating files in multiple folders is no longer supported. | [optional] |
| **includeLabels** | **String**| A comma-separated list of IDs of labels to include in the &#x60;labelInfo&#x60; part of the response. | [optional] |
| **includePermissionsForView** | **String**| Specifies which additional view&#39;s permissions to include in the response. Only &#x60;published&#x60; is supported. | [optional] |
| **ocr** | **Boolean**| Whether to attempt OCR on .jpg, .png, .gif, or .pdf uploads. | [optional] |
| **ocrLanguage** | **String**| If ocr is true, hints at the language to use. Valid values are BCP 47 codes. | [optional] |
| **pinned** | **Boolean**| Whether to pin the head revision of the uploaded file. A file can have a maximum of 200 pinned revisions. | [optional] |
| **supportsAllDrives** | **Boolean**| Whether the requesting application supports both My Drives and shared drives. | [optional] |
| **supportsTeamDrives** | **Boolean**| Deprecated: Use &#x60;supportsAllDrives&#x60; instead. | [optional] |
| **timedTextLanguage** | **String**| The language of the timed text. | [optional] |
| **timedTextTrackName** | **String**| The timed text track name. | [optional] |
| **useContentAsIndexableText** | **Boolean**| Whether to use the content as indexable text. | [optional] |
| **visibility** | **String**| The visibility of the new file. This parameter is only relevant when convert&#x3D;false. | [optional] [enum: DEFAULT, PRIVATE] |
| **modelFile** | [**ModelFile**](ModelFile.md)|  | [optional] |

### Return type

[**ModelFile**](ModelFile.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="driveFilesList"></a>
# **driveFilesList**
> FileList driveFilesList($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, corpora, corpus, driveId, includeItemsFromAllDrives, includeLabels, includePermissionsForView, includeTeamDriveItems, maxResults, orderBy, pageToken, projection, q, spaces, supportsAllDrives, supportsTeamDrives, teamDriveId)



 Lists the user&#39;s files. This method accepts the &#x60;q&#x60; parameter, which is a search query combining one or more search terms. For more information, see the [Search for files &amp; folders](/drive/api/guides/search-files) guide. *Note:* This method returns *all* files by default, including trashed files. If you don&#39;t want trashed files to appear in the list, use the &#x60;trashed&#x3D;false&#x60; query parameter to remove trashed files from the results.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/drive/v2");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    FilesApi apiInstance = new FilesApi(defaultClient);
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
    String corpora = "corpora_example"; // String | Bodies of items (files/documents) to which the query applies. Supported bodies are `default`, `domain`, `drive` and `allDrives`. Prefer `default` or `drive` to `allDrives` for efficiency.
    String corpus = "DEFAULT"; // String | Deprecated: The body of items (files/documents) to which the query applies. Use `corpora` instead.
    String driveId = "driveId_example"; // String | ID of the shared drive to search.
    Boolean includeItemsFromAllDrives = true; // Boolean | Whether both My Drive and shared drive items should be included in results.
    String includeLabels = "includeLabels_example"; // String | A comma-separated list of IDs of labels to include in the `labelInfo` part of the response.
    String includePermissionsForView = "includePermissionsForView_example"; // String | Specifies which additional view's permissions to include in the response. Only `published` is supported.
    Boolean includeTeamDriveItems = true; // Boolean | Deprecated: Use `includeItemsFromAllDrives` instead.
    Integer maxResults = 56; // Integer | The maximum number of files to return per page. Partial or empty result pages are possible even before the end of the files list has been reached.
    String orderBy = "orderBy_example"; // String | A comma-separated list of sort keys. Valid keys are `createdDate`, `folder`, `lastViewedByMeDate`, `modifiedByMeDate`, `modifiedDate`, `quotaBytesUsed`, `recency`, `sharedWithMeDate`, `starred`, `title`, and `title_natural`. Each key sorts ascending by default, but may be reversed with the `desc` modifier. Example usage: ?orderBy=folder,modifiedDate desc,title. Please note that there is a current limitation for users with approximately one million files in which the requested sort order is ignored.
    String pageToken = "pageToken_example"; // String | Page token for files.
    String projection = "BASIC"; // String | Deprecated: This parameter has no function.
    String q = "q_example"; // String | Query string for searching files.
    String spaces = "spaces_example"; // String | A comma-separated list of spaces to query. Supported values are `drive`, and `appDataFolder`.
    Boolean supportsAllDrives = true; // Boolean | Whether the requesting application supports both My Drives and shared drives.
    Boolean supportsTeamDrives = true; // Boolean | Deprecated: Use `supportsAllDrives` instead.
    String teamDriveId = "teamDriveId_example"; // String | Deprecated: Use `driveId` instead.
    try {
      FileList result = apiInstance.driveFilesList($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, corpora, corpus, driveId, includeItemsFromAllDrives, includeLabels, includePermissionsForView, includeTeamDriveItems, maxResults, orderBy, pageToken, projection, q, spaces, supportsAllDrives, supportsTeamDrives, teamDriveId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#driveFilesList");
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
| **corpora** | **String**| Bodies of items (files/documents) to which the query applies. Supported bodies are &#x60;default&#x60;, &#x60;domain&#x60;, &#x60;drive&#x60; and &#x60;allDrives&#x60;. Prefer &#x60;default&#x60; or &#x60;drive&#x60; to &#x60;allDrives&#x60; for efficiency. | [optional] |
| **corpus** | **String**| Deprecated: The body of items (files/documents) to which the query applies. Use &#x60;corpora&#x60; instead. | [optional] [enum: DEFAULT, DOMAIN] |
| **driveId** | **String**| ID of the shared drive to search. | [optional] |
| **includeItemsFromAllDrives** | **Boolean**| Whether both My Drive and shared drive items should be included in results. | [optional] |
| **includeLabels** | **String**| A comma-separated list of IDs of labels to include in the &#x60;labelInfo&#x60; part of the response. | [optional] |
| **includePermissionsForView** | **String**| Specifies which additional view&#39;s permissions to include in the response. Only &#x60;published&#x60; is supported. | [optional] |
| **includeTeamDriveItems** | **Boolean**| Deprecated: Use &#x60;includeItemsFromAllDrives&#x60; instead. | [optional] |
| **maxResults** | **Integer**| The maximum number of files to return per page. Partial or empty result pages are possible even before the end of the files list has been reached. | [optional] |
| **orderBy** | **String**| A comma-separated list of sort keys. Valid keys are &#x60;createdDate&#x60;, &#x60;folder&#x60;, &#x60;lastViewedByMeDate&#x60;, &#x60;modifiedByMeDate&#x60;, &#x60;modifiedDate&#x60;, &#x60;quotaBytesUsed&#x60;, &#x60;recency&#x60;, &#x60;sharedWithMeDate&#x60;, &#x60;starred&#x60;, &#x60;title&#x60;, and &#x60;title_natural&#x60;. Each key sorts ascending by default, but may be reversed with the &#x60;desc&#x60; modifier. Example usage: ?orderBy&#x3D;folder,modifiedDate desc,title. Please note that there is a current limitation for users with approximately one million files in which the requested sort order is ignored. | [optional] |
| **pageToken** | **String**| Page token for files. | [optional] |
| **projection** | **String**| Deprecated: This parameter has no function. | [optional] [enum: BASIC, FULL] |
| **q** | **String**| Query string for searching files. | [optional] |
| **spaces** | **String**| A comma-separated list of spaces to query. Supported values are &#x60;drive&#x60;, and &#x60;appDataFolder&#x60;. | [optional] |
| **supportsAllDrives** | **Boolean**| Whether the requesting application supports both My Drives and shared drives. | [optional] |
| **supportsTeamDrives** | **Boolean**| Deprecated: Use &#x60;supportsAllDrives&#x60; instead. | [optional] |
| **teamDriveId** | **String**| Deprecated: Use &#x60;driveId&#x60; instead. | [optional] |

### Return type

[**FileList**](FileList.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="driveFilesListLabels"></a>
# **driveFilesListLabels**
> LabelList driveFilesListLabels(fileId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, maxResults, pageToken)



Lists the labels on a file.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/drive/v2");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String fileId = "fileId_example"; // String | The ID for the file.
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
    Integer maxResults = 56; // Integer | The maximum number of labels to return per page. When not set, defaults to 100.
    String pageToken = "pageToken_example"; // String | The token for continuing a previous list request on the next page. This should be set to the value of `nextPageToken` from the previous response.
    try {
      LabelList result = apiInstance.driveFilesListLabels(fileId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, maxResults, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#driveFilesListLabels");
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
| **fileId** | **String**| The ID for the file. | |
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
| **maxResults** | **Integer**| The maximum number of labels to return per page. When not set, defaults to 100. | [optional] |
| **pageToken** | **String**| The token for continuing a previous list request on the next page. This should be set to the value of &#x60;nextPageToken&#x60; from the previous response. | [optional] |

### Return type

[**LabelList**](LabelList.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="driveFilesModifyLabels"></a>
# **driveFilesModifyLabels**
> ModifyLabelsResponse driveFilesModifyLabels(fileId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, modifyLabelsRequest)



Modifies the set of labels applied to a file. Returns a list of the labels that were added or modified.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/drive/v2");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String fileId = "fileId_example"; // String | The ID of the file to which the labels belong.
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
    ModifyLabelsRequest modifyLabelsRequest = new ModifyLabelsRequest(); // ModifyLabelsRequest | 
    try {
      ModifyLabelsResponse result = apiInstance.driveFilesModifyLabels(fileId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, modifyLabelsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#driveFilesModifyLabels");
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
| **fileId** | **String**| The ID of the file to which the labels belong. | |
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
| **modifyLabelsRequest** | [**ModifyLabelsRequest**](ModifyLabelsRequest.md)|  | [optional] |

### Return type

[**ModifyLabelsResponse**](ModifyLabelsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="driveFilesPatch"></a>
# **driveFilesPatch**
> ModelFile driveFilesPatch(fileId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, addParents, convert, enforceSingleParent, includeLabels, includePermissionsForView, modifiedDateBehavior, newRevision, ocr, ocrLanguage, pinned, removeParents, setModifiedDate, supportsAllDrives, supportsTeamDrives, timedTextLanguage, timedTextTrackName, updateViewedDate, useContentAsIndexableText, modelFile)



Updates a file&#39;s metadata and/or content. When calling this method, only populate fields in the request that you want to modify. When updating fields, some fields might change automatically, such as modifiedDate. This method supports patch semantics.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/drive/v2");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String fileId = "fileId_example"; // String | The ID of the file to update.
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
    String addParents = "addParents_example"; // String | Comma-separated list of parent IDs to add.
    Boolean convert = true; // Boolean | Deprecated: This parameter has no function.
    Boolean enforceSingleParent = true; // Boolean | Deprecated: Adding files to multiple folders is no longer supported. Use `shortcuts` instead.
    String includeLabels = "includeLabels_example"; // String | A comma-separated list of IDs of labels to include in the `labelInfo` part of the response.
    String includePermissionsForView = "includePermissionsForView_example"; // String | Specifies which additional view's permissions to include in the response. Only `published` is supported.
    String modifiedDateBehavior = "fromBody"; // String | Determines the behavior in which `modifiedDate` is updated. This overrides `setModifiedDate`.
    Boolean newRevision = true; // Boolean | Whether a blob upload should create a new revision. If false, the blob data in the current head revision is replaced. If true or not set, a new blob is created as head revision, and previous unpinned revisions are preserved for a short period of time. Pinned revisions are stored indefinitely, using additional storage quota, up to a maximum of 200 revisions. For details on how revisions are retained, see the [Drive Help Center](https://support.google.com/drive/answer/2409045). Note that this field is ignored if there is no payload in the request.
    Boolean ocr = true; // Boolean | Whether to attempt OCR on .jpg, .png, .gif, or .pdf uploads.
    String ocrLanguage = "ocrLanguage_example"; // String | If ocr is true, hints at the language to use. Valid values are BCP 47 codes.
    Boolean pinned = true; // Boolean | Whether to pin the new revision. A file can have a maximum of 200 pinned revisions. Note that this field is ignored if there is no payload in the request.
    String removeParents = "removeParents_example"; // String | Comma-separated list of parent IDs to remove.
    Boolean setModifiedDate = true; // Boolean | Whether to set the modified date using the value supplied in the request body. Setting this field to `true` is equivalent to `modifiedDateBehavior=fromBodyOrNow`, and `false` is equivalent to `modifiedDateBehavior=now`. To prevent any changes to the modified date set `modifiedDateBehavior=noChange`.
    Boolean supportsAllDrives = true; // Boolean | Whether the requesting application supports both My Drives and shared drives.
    Boolean supportsTeamDrives = true; // Boolean | Deprecated: Use `supportsAllDrives` instead.
    String timedTextLanguage = "timedTextLanguage_example"; // String | The language of the timed text.
    String timedTextTrackName = "timedTextTrackName_example"; // String | The timed text track name.
    Boolean updateViewedDate = true; // Boolean | Whether to update the view date after successfully updating the file.
    Boolean useContentAsIndexableText = true; // Boolean | Whether to use the content as indexable text.
    ModelFile modelFile = new ModelFile(); // ModelFile | 
    try {
      ModelFile result = apiInstance.driveFilesPatch(fileId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, addParents, convert, enforceSingleParent, includeLabels, includePermissionsForView, modifiedDateBehavior, newRevision, ocr, ocrLanguage, pinned, removeParents, setModifiedDate, supportsAllDrives, supportsTeamDrives, timedTextLanguage, timedTextTrackName, updateViewedDate, useContentAsIndexableText, modelFile);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#driveFilesPatch");
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
| **fileId** | **String**| The ID of the file to update. | |
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
| **addParents** | **String**| Comma-separated list of parent IDs to add. | [optional] |
| **convert** | **Boolean**| Deprecated: This parameter has no function. | [optional] |
| **enforceSingleParent** | **Boolean**| Deprecated: Adding files to multiple folders is no longer supported. Use &#x60;shortcuts&#x60; instead. | [optional] |
| **includeLabels** | **String**| A comma-separated list of IDs of labels to include in the &#x60;labelInfo&#x60; part of the response. | [optional] |
| **includePermissionsForView** | **String**| Specifies which additional view&#39;s permissions to include in the response. Only &#x60;published&#x60; is supported. | [optional] |
| **modifiedDateBehavior** | **String**| Determines the behavior in which &#x60;modifiedDate&#x60; is updated. This overrides &#x60;setModifiedDate&#x60;. | [optional] [enum: fromBody, fromBodyIfNeeded, fromBodyOrNow, noChange, now, nowIfNeeded] |
| **newRevision** | **Boolean**| Whether a blob upload should create a new revision. If false, the blob data in the current head revision is replaced. If true or not set, a new blob is created as head revision, and previous unpinned revisions are preserved for a short period of time. Pinned revisions are stored indefinitely, using additional storage quota, up to a maximum of 200 revisions. For details on how revisions are retained, see the [Drive Help Center](https://support.google.com/drive/answer/2409045). Note that this field is ignored if there is no payload in the request. | [optional] |
| **ocr** | **Boolean**| Whether to attempt OCR on .jpg, .png, .gif, or .pdf uploads. | [optional] |
| **ocrLanguage** | **String**| If ocr is true, hints at the language to use. Valid values are BCP 47 codes. | [optional] |
| **pinned** | **Boolean**| Whether to pin the new revision. A file can have a maximum of 200 pinned revisions. Note that this field is ignored if there is no payload in the request. | [optional] |
| **removeParents** | **String**| Comma-separated list of parent IDs to remove. | [optional] |
| **setModifiedDate** | **Boolean**| Whether to set the modified date using the value supplied in the request body. Setting this field to &#x60;true&#x60; is equivalent to &#x60;modifiedDateBehavior&#x3D;fromBodyOrNow&#x60;, and &#x60;false&#x60; is equivalent to &#x60;modifiedDateBehavior&#x3D;now&#x60;. To prevent any changes to the modified date set &#x60;modifiedDateBehavior&#x3D;noChange&#x60;. | [optional] |
| **supportsAllDrives** | **Boolean**| Whether the requesting application supports both My Drives and shared drives. | [optional] |
| **supportsTeamDrives** | **Boolean**| Deprecated: Use &#x60;supportsAllDrives&#x60; instead. | [optional] |
| **timedTextLanguage** | **String**| The language of the timed text. | [optional] |
| **timedTextTrackName** | **String**| The timed text track name. | [optional] |
| **updateViewedDate** | **Boolean**| Whether to update the view date after successfully updating the file. | [optional] |
| **useContentAsIndexableText** | **Boolean**| Whether to use the content as indexable text. | [optional] |
| **modelFile** | [**ModelFile**](ModelFile.md)|  | [optional] |

### Return type

[**ModelFile**](ModelFile.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="driveFilesTouch"></a>
# **driveFilesTouch**
> ModelFile driveFilesTouch(fileId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, includeLabels, includePermissionsForView, supportsAllDrives, supportsTeamDrives)



Set the file&#39;s updated time to the current server time.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/drive/v2");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String fileId = "fileId_example"; // String | The ID of the file to update.
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
    String includeLabels = "includeLabels_example"; // String | A comma-separated list of IDs of labels to include in the `labelInfo` part of the response.
    String includePermissionsForView = "includePermissionsForView_example"; // String | Specifies which additional view's permissions to include in the response. Only `published` is supported.
    Boolean supportsAllDrives = true; // Boolean | Whether the requesting application supports both My Drives and shared drives.
    Boolean supportsTeamDrives = true; // Boolean | Deprecated: Use `supportsAllDrives` instead.
    try {
      ModelFile result = apiInstance.driveFilesTouch(fileId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, includeLabels, includePermissionsForView, supportsAllDrives, supportsTeamDrives);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#driveFilesTouch");
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
| **fileId** | **String**| The ID of the file to update. | |
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
| **includeLabels** | **String**| A comma-separated list of IDs of labels to include in the &#x60;labelInfo&#x60; part of the response. | [optional] |
| **includePermissionsForView** | **String**| Specifies which additional view&#39;s permissions to include in the response. Only &#x60;published&#x60; is supported. | [optional] |
| **supportsAllDrives** | **Boolean**| Whether the requesting application supports both My Drives and shared drives. | [optional] |
| **supportsTeamDrives** | **Boolean**| Deprecated: Use &#x60;supportsAllDrives&#x60; instead. | [optional] |

### Return type

[**ModelFile**](ModelFile.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="driveFilesTrash"></a>
# **driveFilesTrash**
> ModelFile driveFilesTrash(fileId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, includeLabels, includePermissionsForView, supportsAllDrives, supportsTeamDrives)



Moves a file to the trash. The currently authenticated user must own the file or be at least a &#x60;fileOrganizer&#x60; on the parent for shared drive files.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/drive/v2");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String fileId = "fileId_example"; // String | The ID of the file to trash.
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
    String includeLabels = "includeLabels_example"; // String | A comma-separated list of IDs of labels to include in the `labelInfo` part of the response.
    String includePermissionsForView = "includePermissionsForView_example"; // String | Specifies which additional view's permissions to include in the response. Only `published` is supported.
    Boolean supportsAllDrives = true; // Boolean | Whether the requesting application supports both My Drives and shared drives.
    Boolean supportsTeamDrives = true; // Boolean | Deprecated: Use `supportsAllDrives` instead.
    try {
      ModelFile result = apiInstance.driveFilesTrash(fileId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, includeLabels, includePermissionsForView, supportsAllDrives, supportsTeamDrives);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#driveFilesTrash");
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
| **fileId** | **String**| The ID of the file to trash. | |
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
| **includeLabels** | **String**| A comma-separated list of IDs of labels to include in the &#x60;labelInfo&#x60; part of the response. | [optional] |
| **includePermissionsForView** | **String**| Specifies which additional view&#39;s permissions to include in the response. Only &#x60;published&#x60; is supported. | [optional] |
| **supportsAllDrives** | **Boolean**| Whether the requesting application supports both My Drives and shared drives. | [optional] |
| **supportsTeamDrives** | **Boolean**| Deprecated: Use &#x60;supportsAllDrives&#x60; instead. | [optional] |

### Return type

[**ModelFile**](ModelFile.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="driveFilesUntrash"></a>
# **driveFilesUntrash**
> ModelFile driveFilesUntrash(fileId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, includeLabels, includePermissionsForView, supportsAllDrives, supportsTeamDrives)



Restores a file from the trash. The currently authenticated user must own the file or be at least a &#x60;fileOrganizer&#x60; on the parent for shared drive files.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/drive/v2");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String fileId = "fileId_example"; // String | The ID of the file to untrash.
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
    String includeLabels = "includeLabels_example"; // String | A comma-separated list of IDs of labels to include in the `labelInfo` part of the response.
    String includePermissionsForView = "includePermissionsForView_example"; // String | Specifies which additional view's permissions to include in the response. Only `published` is supported.
    Boolean supportsAllDrives = true; // Boolean | Whether the requesting application supports both My Drives and shared drives.
    Boolean supportsTeamDrives = true; // Boolean | Deprecated: Use `supportsAllDrives` instead.
    try {
      ModelFile result = apiInstance.driveFilesUntrash(fileId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, includeLabels, includePermissionsForView, supportsAllDrives, supportsTeamDrives);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#driveFilesUntrash");
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
| **fileId** | **String**| The ID of the file to untrash. | |
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
| **includeLabels** | **String**| A comma-separated list of IDs of labels to include in the &#x60;labelInfo&#x60; part of the response. | [optional] |
| **includePermissionsForView** | **String**| Specifies which additional view&#39;s permissions to include in the response. Only &#x60;published&#x60; is supported. | [optional] |
| **supportsAllDrives** | **Boolean**| Whether the requesting application supports both My Drives and shared drives. | [optional] |
| **supportsTeamDrives** | **Boolean**| Deprecated: Use &#x60;supportsAllDrives&#x60; instead. | [optional] |

### Return type

[**ModelFile**](ModelFile.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="driveFilesUpdate"></a>
# **driveFilesUpdate**
> ModelFile driveFilesUpdate(fileId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, addParents, convert, enforceSingleParent, includeLabels, includePermissionsForView, modifiedDateBehavior, newRevision, ocr, ocrLanguage, pinned, removeParents, setModifiedDate, supportsAllDrives, supportsTeamDrives, timedTextLanguage, timedTextTrackName, updateViewedDate, useContentAsIndexableText, modelFile)



 Updates a file&#39;s metadata and/or content. When calling this method, only populate fields in the request that you want to modify. When updating fields, some fields might be changed automatically, such as &#x60;modifiedDate&#x60;. This method supports patch semantics. This method supports an *_/upload* URI and accepts uploaded media with the following characteristics: - *Maximum file size:* 5,120 GB - *Accepted Media MIME types:*&#x60;*_/_*&#x60; Note: Specify a valid MIME type, rather than the literal &#x60;*_/_*&#x60; value. The literal &#x60;*_/_*&#x60; is only used to indicate that any valid MIME type can be uploaded. For more information on uploading files, see [Upload file data](/drive/api/guides/manage-uploads).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/drive/v2");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String fileId = "fileId_example"; // String | The ID of the file to update.
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
    String addParents = "addParents_example"; // String | Comma-separated list of parent IDs to add.
    Boolean convert = true; // Boolean | Deprecated: This parameter has no function.
    Boolean enforceSingleParent = true; // Boolean | Deprecated: Adding files to multiple folders is no longer supported. Use `shortcuts` instead.
    String includeLabels = "includeLabels_example"; // String | A comma-separated list of IDs of labels to include in the `labelInfo` part of the response.
    String includePermissionsForView = "includePermissionsForView_example"; // String | Specifies which additional view's permissions to include in the response. Only `published` is supported.
    String modifiedDateBehavior = "fromBody"; // String | Determines the behavior in which `modifiedDate` is updated. This overrides `setModifiedDate`.
    Boolean newRevision = true; // Boolean | Whether a blob upload should create a new revision. If false, the blob data in the current head revision is replaced. If true or not set, a new blob is created as head revision, and previous unpinned revisions are preserved for a short period of time. Pinned revisions are stored indefinitely, using additional storage quota, up to a maximum of 200 revisions. For details on how revisions are retained, see the [Drive Help Center](https://support.google.com/drive/answer/2409045).
    Boolean ocr = true; // Boolean | Whether to attempt OCR on .jpg, .png, .gif, or .pdf uploads.
    String ocrLanguage = "ocrLanguage_example"; // String | If ocr is true, hints at the language to use. Valid values are BCP 47 codes.
    Boolean pinned = true; // Boolean | Whether to pin the new revision. A file can have a maximum of 200 pinned revisions.
    String removeParents = "removeParents_example"; // String | Comma-separated list of parent IDs to remove.
    Boolean setModifiedDate = true; // Boolean | Whether to set the modified date using the value supplied in the request body. Setting this field to `true` is equivalent to `modifiedDateBehavior=fromBodyOrNow`, and `false` is equivalent to `modifiedDateBehavior=now`. To prevent any changes to the modified date set `modifiedDateBehavior=noChange`.
    Boolean supportsAllDrives = true; // Boolean | Whether the requesting application supports both My Drives and shared drives.
    Boolean supportsTeamDrives = true; // Boolean | Deprecated: Use `supportsAllDrives` instead.
    String timedTextLanguage = "timedTextLanguage_example"; // String | The language of the timed text.
    String timedTextTrackName = "timedTextTrackName_example"; // String | The timed text track name.
    Boolean updateViewedDate = true; // Boolean | Whether to update the view date after successfully updating the file.
    Boolean useContentAsIndexableText = true; // Boolean | Whether to use the content as indexable text.
    ModelFile modelFile = new ModelFile(); // ModelFile | 
    try {
      ModelFile result = apiInstance.driveFilesUpdate(fileId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, addParents, convert, enforceSingleParent, includeLabels, includePermissionsForView, modifiedDateBehavior, newRevision, ocr, ocrLanguage, pinned, removeParents, setModifiedDate, supportsAllDrives, supportsTeamDrives, timedTextLanguage, timedTextTrackName, updateViewedDate, useContentAsIndexableText, modelFile);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#driveFilesUpdate");
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
| **fileId** | **String**| The ID of the file to update. | |
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
| **addParents** | **String**| Comma-separated list of parent IDs to add. | [optional] |
| **convert** | **Boolean**| Deprecated: This parameter has no function. | [optional] |
| **enforceSingleParent** | **Boolean**| Deprecated: Adding files to multiple folders is no longer supported. Use &#x60;shortcuts&#x60; instead. | [optional] |
| **includeLabels** | **String**| A comma-separated list of IDs of labels to include in the &#x60;labelInfo&#x60; part of the response. | [optional] |
| **includePermissionsForView** | **String**| Specifies which additional view&#39;s permissions to include in the response. Only &#x60;published&#x60; is supported. | [optional] |
| **modifiedDateBehavior** | **String**| Determines the behavior in which &#x60;modifiedDate&#x60; is updated. This overrides &#x60;setModifiedDate&#x60;. | [optional] [enum: fromBody, fromBodyIfNeeded, fromBodyOrNow, noChange, now, nowIfNeeded] |
| **newRevision** | **Boolean**| Whether a blob upload should create a new revision. If false, the blob data in the current head revision is replaced. If true or not set, a new blob is created as head revision, and previous unpinned revisions are preserved for a short period of time. Pinned revisions are stored indefinitely, using additional storage quota, up to a maximum of 200 revisions. For details on how revisions are retained, see the [Drive Help Center](https://support.google.com/drive/answer/2409045). | [optional] |
| **ocr** | **Boolean**| Whether to attempt OCR on .jpg, .png, .gif, or .pdf uploads. | [optional] |
| **ocrLanguage** | **String**| If ocr is true, hints at the language to use. Valid values are BCP 47 codes. | [optional] |
| **pinned** | **Boolean**| Whether to pin the new revision. A file can have a maximum of 200 pinned revisions. | [optional] |
| **removeParents** | **String**| Comma-separated list of parent IDs to remove. | [optional] |
| **setModifiedDate** | **Boolean**| Whether to set the modified date using the value supplied in the request body. Setting this field to &#x60;true&#x60; is equivalent to &#x60;modifiedDateBehavior&#x3D;fromBodyOrNow&#x60;, and &#x60;false&#x60; is equivalent to &#x60;modifiedDateBehavior&#x3D;now&#x60;. To prevent any changes to the modified date set &#x60;modifiedDateBehavior&#x3D;noChange&#x60;. | [optional] |
| **supportsAllDrives** | **Boolean**| Whether the requesting application supports both My Drives and shared drives. | [optional] |
| **supportsTeamDrives** | **Boolean**| Deprecated: Use &#x60;supportsAllDrives&#x60; instead. | [optional] |
| **timedTextLanguage** | **String**| The language of the timed text. | [optional] |
| **timedTextTrackName** | **String**| The timed text track name. | [optional] |
| **updateViewedDate** | **Boolean**| Whether to update the view date after successfully updating the file. | [optional] |
| **useContentAsIndexableText** | **Boolean**| Whether to use the content as indexable text. | [optional] |
| **modelFile** | [**ModelFile**](ModelFile.md)|  | [optional] |

### Return type

[**ModelFile**](ModelFile.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="driveFilesWatch"></a>
# **driveFilesWatch**
> Channel driveFilesWatch(fileId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, acknowledgeAbuse, includeLabels, includePermissionsForView, projection, revisionId, supportsAllDrives, supportsTeamDrives, updateViewedDate, channel)



Subscribes to changes to a file.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/drive/v2");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String fileId = "fileId_example"; // String | The ID for the file in question.
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
    Boolean acknowledgeAbuse = true; // Boolean | Whether the user is acknowledging the risk of downloading known malware or other abusive files.
    String includeLabels = "includeLabels_example"; // String | A comma-separated list of IDs of labels to include in the `labelInfo` part of the response.
    String includePermissionsForView = "includePermissionsForView_example"; // String | Specifies which additional view's permissions to include in the response. Only `published` is supported.
    String projection = "BASIC"; // String | Deprecated: This parameter has no function.
    String revisionId = "revisionId_example"; // String | Specifies the Revision ID that should be downloaded. Ignored unless alt=media is specified.
    Boolean supportsAllDrives = true; // Boolean | Whether the requesting application supports both My Drives and shared drives.
    Boolean supportsTeamDrives = true; // Boolean | Deprecated: Use `supportsAllDrives` instead.
    Boolean updateViewedDate = true; // Boolean | Deprecated: Use files.update with modifiedDateBehavior=noChange, updateViewedDate=true and an empty request body.
    Channel channel = new Channel(); // Channel | 
    try {
      Channel result = apiInstance.driveFilesWatch(fileId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, acknowledgeAbuse, includeLabels, includePermissionsForView, projection, revisionId, supportsAllDrives, supportsTeamDrives, updateViewedDate, channel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#driveFilesWatch");
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
| **fileId** | **String**| The ID for the file in question. | |
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
| **acknowledgeAbuse** | **Boolean**| Whether the user is acknowledging the risk of downloading known malware or other abusive files. | [optional] |
| **includeLabels** | **String**| A comma-separated list of IDs of labels to include in the &#x60;labelInfo&#x60; part of the response. | [optional] |
| **includePermissionsForView** | **String**| Specifies which additional view&#39;s permissions to include in the response. Only &#x60;published&#x60; is supported. | [optional] |
| **projection** | **String**| Deprecated: This parameter has no function. | [optional] [enum: BASIC, FULL] |
| **revisionId** | **String**| Specifies the Revision ID that should be downloaded. Ignored unless alt&#x3D;media is specified. | [optional] |
| **supportsAllDrives** | **Boolean**| Whether the requesting application supports both My Drives and shared drives. | [optional] |
| **supportsTeamDrives** | **Boolean**| Deprecated: Use &#x60;supportsAllDrives&#x60; instead. | [optional] |
| **updateViewedDate** | **Boolean**| Deprecated: Use files.update with modifiedDateBehavior&#x3D;noChange, updateViewedDate&#x3D;true and an empty request body. | [optional] |
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

