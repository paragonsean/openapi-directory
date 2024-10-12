# FilesApi

All URIs are relative to *https://www.googleapis.com/drive/v3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**driveFilesCopy**](FilesApi.md#driveFilesCopy) | **POST** /files/{fileId}/copy |  |
| [**driveFilesCreate**](FilesApi.md#driveFilesCreate) | **POST** /files |  |
| [**driveFilesDelete**](FilesApi.md#driveFilesDelete) | **DELETE** /files/{fileId} |  |
| [**driveFilesEmptyTrash**](FilesApi.md#driveFilesEmptyTrash) | **DELETE** /files/trash |  |
| [**driveFilesExport**](FilesApi.md#driveFilesExport) | **GET** /files/{fileId}/export |  |
| [**driveFilesGenerateIds**](FilesApi.md#driveFilesGenerateIds) | **GET** /files/generateIds |  |
| [**driveFilesGet**](FilesApi.md#driveFilesGet) | **GET** /files/{fileId} |  |
| [**driveFilesList**](FilesApi.md#driveFilesList) | **GET** /files |  |
| [**driveFilesListLabels**](FilesApi.md#driveFilesListLabels) | **GET** /files/{fileId}/listLabels |  |
| [**driveFilesModifyLabels**](FilesApi.md#driveFilesModifyLabels) | **POST** /files/{fileId}/modifyLabels |  |
| [**driveFilesUpdate**](FilesApi.md#driveFilesUpdate) | **PATCH** /files/{fileId} |  |
| [**driveFilesWatch**](FilesApi.md#driveFilesWatch) | **POST** /files/{fileId}/watch |  |


<a id="driveFilesCopy"></a>
# **driveFilesCopy**
> ModelFile driveFilesCopy(fileId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, enforceSingleParent, ignoreDefaultVisibility, includeLabels, includePermissionsForView, keepRevisionForever, ocrLanguage, supportsAllDrives, supportsTeamDrives, modelFile)



Creates a copy of a file and applies any requested updates with patch semantics.

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
    defaultClient.setBasePath("https://www.googleapis.com/drive/v3");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String fileId = "fileId_example"; // String | The ID of the file.
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
    Boolean enforceSingleParent = true; // Boolean | Deprecated. Copying files into multiple folders is no longer supported. Use shortcuts instead.
    Boolean ignoreDefaultVisibility = true; // Boolean | Whether to ignore the domain's default visibility settings for the created file. Domain administrators can choose to make all uploaded files visible to the domain by default; this parameter bypasses that behavior for the request. Permissions are still inherited from parent folders.
    String includeLabels = "includeLabels_example"; // String | A comma-separated list of IDs of labels to include in the `labelInfo` part of the response.
    String includePermissionsForView = "includePermissionsForView_example"; // String | Specifies which additional view's permissions to include in the response. Only 'published' is supported.
    Boolean keepRevisionForever = true; // Boolean | Whether to set the 'keepForever' field in the new head revision. This is only applicable to files with binary content in Google Drive. Only 200 revisions for the file can be kept forever. If the limit is reached, try deleting pinned revisions.
    String ocrLanguage = "ocrLanguage_example"; // String | A language hint for OCR processing during image import (ISO 639-1 code).
    Boolean supportsAllDrives = true; // Boolean | Whether the requesting application supports both My Drives and shared drives.
    Boolean supportsTeamDrives = true; // Boolean | Deprecated: Use `supportsAllDrives` instead.
    ModelFile modelFile = new ModelFile(); // ModelFile | 
    try {
      ModelFile result = apiInstance.driveFilesCopy(fileId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, enforceSingleParent, ignoreDefaultVisibility, includeLabels, includePermissionsForView, keepRevisionForever, ocrLanguage, supportsAllDrives, supportsTeamDrives, modelFile);
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
| **fileId** | **String**| The ID of the file. | |
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
| **enforceSingleParent** | **Boolean**| Deprecated. Copying files into multiple folders is no longer supported. Use shortcuts instead. | [optional] |
| **ignoreDefaultVisibility** | **Boolean**| Whether to ignore the domain&#39;s default visibility settings for the created file. Domain administrators can choose to make all uploaded files visible to the domain by default; this parameter bypasses that behavior for the request. Permissions are still inherited from parent folders. | [optional] |
| **includeLabels** | **String**| A comma-separated list of IDs of labels to include in the &#x60;labelInfo&#x60; part of the response. | [optional] |
| **includePermissionsForView** | **String**| Specifies which additional view&#39;s permissions to include in the response. Only &#39;published&#39; is supported. | [optional] |
| **keepRevisionForever** | **Boolean**| Whether to set the &#39;keepForever&#39; field in the new head revision. This is only applicable to files with binary content in Google Drive. Only 200 revisions for the file can be kept forever. If the limit is reached, try deleting pinned revisions. | [optional] |
| **ocrLanguage** | **String**| A language hint for OCR processing during image import (ISO 639-1 code). | [optional] |
| **supportsAllDrives** | **Boolean**| Whether the requesting application supports both My Drives and shared drives. | [optional] |
| **supportsTeamDrives** | **Boolean**| Deprecated: Use &#x60;supportsAllDrives&#x60; instead. | [optional] |
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

<a id="driveFilesCreate"></a>
# **driveFilesCreate**
> ModelFile driveFilesCreate($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, enforceSingleParent, ignoreDefaultVisibility, includeLabels, includePermissionsForView, keepRevisionForever, ocrLanguage, supportsAllDrives, supportsTeamDrives, useContentAsIndexableText, modelFile)



 Creates a new file. This method supports an *_/upload* URI and accepts uploaded media with the following characteristics: - *Maximum file size:* 5,120 GB - *Accepted Media MIME types:*&#x60;*_/_*&#x60; Note: Specify a valid MIME type, rather than the literal &#x60;*_/_*&#x60; value. The literal &#x60;*_/_*&#x60; is only used to indicate that any valid MIME type can be uploaded. For more information on uploading files, see [Upload file data](/drive/api/guides/manage-uploads). Apps creating shortcuts with &#x60;files.create&#x60; must specify the MIME type &#x60;application/vnd.google-apps.shortcut&#x60;. Apps should specify a file extension in the &#x60;name&#x60; property when inserting files with the API. For example, an operation to insert a JPEG file should specify something like &#x60;\&quot;name\&quot;: \&quot;cat.jpg\&quot;&#x60; in the metadata. Subsequent &#x60;GET&#x60; requests include the read-only &#x60;fileExtension&#x60; property populated with the extension originally specified in the &#x60;title&#x60; property. When a Google Drive user requests to download a file, or when the file is downloaded through the sync client, Drive builds a full filename (with extension) based on the title. In cases where the extension is missing, Drive attempts to determine the extension based on the file&#39;s MIME type.

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
    defaultClient.setBasePath("https://www.googleapis.com/drive/v3");
    
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
    Boolean enforceSingleParent = true; // Boolean | Deprecated. Creating files in multiple folders is no longer supported.
    Boolean ignoreDefaultVisibility = true; // Boolean | Whether to ignore the domain's default visibility settings for the created file. Domain administrators can choose to make all uploaded files visible to the domain by default; this parameter bypasses that behavior for the request. Permissions are still inherited from parent folders.
    String includeLabels = "includeLabels_example"; // String | A comma-separated list of IDs of labels to include in the `labelInfo` part of the response.
    String includePermissionsForView = "includePermissionsForView_example"; // String | Specifies which additional view's permissions to include in the response. Only 'published' is supported.
    Boolean keepRevisionForever = true; // Boolean | Whether to set the 'keepForever' field in the new head revision. This is only applicable to files with binary content in Google Drive. Only 200 revisions for the file can be kept forever. If the limit is reached, try deleting pinned revisions.
    String ocrLanguage = "ocrLanguage_example"; // String | A language hint for OCR processing during image import (ISO 639-1 code).
    Boolean supportsAllDrives = true; // Boolean | Whether the requesting application supports both My Drives and shared drives.
    Boolean supportsTeamDrives = true; // Boolean | Deprecated: Use `supportsAllDrives` instead.
    Boolean useContentAsIndexableText = true; // Boolean | Whether to use the uploaded content as indexable text.
    ModelFile modelFile = new ModelFile(); // ModelFile | 
    try {
      ModelFile result = apiInstance.driveFilesCreate($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, enforceSingleParent, ignoreDefaultVisibility, includeLabels, includePermissionsForView, keepRevisionForever, ocrLanguage, supportsAllDrives, supportsTeamDrives, useContentAsIndexableText, modelFile);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#driveFilesCreate");
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
| **enforceSingleParent** | **Boolean**| Deprecated. Creating files in multiple folders is no longer supported. | [optional] |
| **ignoreDefaultVisibility** | **Boolean**| Whether to ignore the domain&#39;s default visibility settings for the created file. Domain administrators can choose to make all uploaded files visible to the domain by default; this parameter bypasses that behavior for the request. Permissions are still inherited from parent folders. | [optional] |
| **includeLabels** | **String**| A comma-separated list of IDs of labels to include in the &#x60;labelInfo&#x60; part of the response. | [optional] |
| **includePermissionsForView** | **String**| Specifies which additional view&#39;s permissions to include in the response. Only &#39;published&#39; is supported. | [optional] |
| **keepRevisionForever** | **Boolean**| Whether to set the &#39;keepForever&#39; field in the new head revision. This is only applicable to files with binary content in Google Drive. Only 200 revisions for the file can be kept forever. If the limit is reached, try deleting pinned revisions. | [optional] |
| **ocrLanguage** | **String**| A language hint for OCR processing during image import (ISO 639-1 code). | [optional] |
| **supportsAllDrives** | **Boolean**| Whether the requesting application supports both My Drives and shared drives. | [optional] |
| **supportsTeamDrives** | **Boolean**| Deprecated: Use &#x60;supportsAllDrives&#x60; instead. | [optional] |
| **useContentAsIndexableText** | **Boolean**| Whether to use the uploaded content as indexable text. | [optional] |
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
    defaultClient.setBasePath("https://www.googleapis.com/drive/v3");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String fileId = "fileId_example"; // String | The ID of the file.
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
    Boolean enforceSingleParent = true; // Boolean | Deprecated: If an item is not in a shared drive and its last parent is deleted but the item itself is not, the item will be placed under its owner's root.
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
| **fileId** | **String**| The ID of the file. | |
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
| **enforceSingleParent** | **Boolean**| Deprecated: If an item is not in a shared drive and its last parent is deleted but the item itself is not, the item will be placed under its owner&#39;s root. | [optional] |
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
    defaultClient.setBasePath("https://www.googleapis.com/drive/v3");
    
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
    Boolean enforceSingleParent = true; // Boolean | Deprecated: If an item is not in a shared drive and its last parent is deleted but the item itself is not, the item will be placed under its owner's root.
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
| **enforceSingleParent** | **Boolean**| Deprecated: If an item is not in a shared drive and its last parent is deleted but the item itself is not, the item will be placed under its owner&#39;s root. | [optional] |

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
    defaultClient.setBasePath("https://www.googleapis.com/drive/v3");
    
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
> GeneratedIds driveFilesGenerateIds($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, count, space, type)



Generates a set of file IDs which can be provided in create or copy requests.

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
    defaultClient.setBasePath("https://www.googleapis.com/drive/v3");
    
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
    Integer count = 56; // Integer | The number of IDs to return.
    String space = "space_example"; // String | The space in which the IDs can be used to create new files. Supported values are 'drive' and 'appDataFolder'. (Default: 'drive')
    String type = "type_example"; // String | The type of items which the IDs can be used for. Supported values are 'files' and 'shortcuts'. Note that 'shortcuts' are only supported in the `drive` 'space'. (Default: 'files')
    try {
      GeneratedIds result = apiInstance.driveFilesGenerateIds($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, count, space, type);
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
| **count** | **Integer**| The number of IDs to return. | [optional] |
| **space** | **String**| The space in which the IDs can be used to create new files. Supported values are &#39;drive&#39; and &#39;appDataFolder&#39;. (Default: &#39;drive&#39;) | [optional] |
| **type** | **String**| The type of items which the IDs can be used for. Supported values are &#39;files&#39; and &#39;shortcuts&#39;. Note that &#39;shortcuts&#39; are only supported in the &#x60;drive&#x60; &#39;space&#39;. (Default: &#39;files&#39;) | [optional] |

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
> ModelFile driveFilesGet(fileId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, acknowledgeAbuse, includeLabels, includePermissionsForView, supportsAllDrives, supportsTeamDrives)



 Gets a file&#39;s metadata or content by ID. If you provide the URL parameter &#x60;alt&#x3D;media&#x60;, then the response includes the file contents in the response body. Downloading content with &#x60;alt&#x3D;media&#x60; only works if the file is stored in Drive. To download Google Docs, Sheets, and Slides use [&#x60;files.export&#x60;](/drive/api/reference/rest/v3/files/export) instead. For more information, see [Download &amp; export files](/drive/api/guides/manage-downloads).

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
    defaultClient.setBasePath("https://www.googleapis.com/drive/v3");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String fileId = "fileId_example"; // String | The ID of the file.
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
    Boolean acknowledgeAbuse = true; // Boolean | Whether the user is acknowledging the risk of downloading known malware or other abusive files. This is only applicable when alt=media.
    String includeLabels = "includeLabels_example"; // String | A comma-separated list of IDs of labels to include in the `labelInfo` part of the response.
    String includePermissionsForView = "includePermissionsForView_example"; // String | Specifies which additional view's permissions to include in the response. Only 'published' is supported.
    Boolean supportsAllDrives = true; // Boolean | Whether the requesting application supports both My Drives and shared drives.
    Boolean supportsTeamDrives = true; // Boolean | Deprecated: Use `supportsAllDrives` instead.
    try {
      ModelFile result = apiInstance.driveFilesGet(fileId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, acknowledgeAbuse, includeLabels, includePermissionsForView, supportsAllDrives, supportsTeamDrives);
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
| **fileId** | **String**| The ID of the file. | |
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
| **acknowledgeAbuse** | **Boolean**| Whether the user is acknowledging the risk of downloading known malware or other abusive files. This is only applicable when alt&#x3D;media. | [optional] |
| **includeLabels** | **String**| A comma-separated list of IDs of labels to include in the &#x60;labelInfo&#x60; part of the response. | [optional] |
| **includePermissionsForView** | **String**| Specifies which additional view&#39;s permissions to include in the response. Only &#39;published&#39; is supported. | [optional] |
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

<a id="driveFilesList"></a>
# **driveFilesList**
> FileList driveFilesList($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, corpora, corpus, driveId, includeItemsFromAllDrives, includeLabels, includePermissionsForView, includeTeamDriveItems, orderBy, pageSize, pageToken, q, spaces, supportsAllDrives, supportsTeamDrives, teamDriveId)



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
    defaultClient.setBasePath("https://www.googleapis.com/drive/v3");
    
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
    String corpora = "corpora_example"; // String | Bodies of items (files/documents) to which the query applies. Supported bodies are 'user', 'domain', 'drive', and 'allDrives'. Prefer 'user' or 'drive' to 'allDrives' for efficiency. By default, corpora is set to 'user'. However, this can change depending on the filter set through the 'q' parameter.
    String corpus = "domain"; // String | Deprecated: The source of files to list. Use 'corpora' instead.
    String driveId = "driveId_example"; // String | ID of the shared drive to search.
    Boolean includeItemsFromAllDrives = true; // Boolean | Whether both My Drive and shared drive items should be included in results.
    String includeLabels = "includeLabels_example"; // String | A comma-separated list of IDs of labels to include in the `labelInfo` part of the response.
    String includePermissionsForView = "includePermissionsForView_example"; // String | Specifies which additional view's permissions to include in the response. Only 'published' is supported.
    Boolean includeTeamDriveItems = true; // Boolean | Deprecated: Use `includeItemsFromAllDrives` instead.
    String orderBy = "orderBy_example"; // String | A comma-separated list of sort keys. Valid keys are 'createdTime', 'folder', 'modifiedByMeTime', 'modifiedTime', 'name', 'name_natural', 'quotaBytesUsed', 'recency', 'sharedWithMeTime', 'starred', and 'viewedByMeTime'. Each key sorts ascending by default, but can be reversed with the 'desc' modifier. Example usage: ?orderBy=folder,modifiedTime desc,name.
    Integer pageSize = 56; // Integer | The maximum number of files to return per page. Partial or empty result pages are possible even before the end of the files list has been reached.
    String pageToken = "pageToken_example"; // String | The token for continuing a previous list request on the next page. This should be set to the value of 'nextPageToken' from the previous response.
    String q = "q_example"; // String | A query for filtering the file results. See the \"Search for files & folders\" guide for supported syntax.
    String spaces = "spaces_example"; // String | A comma-separated list of spaces to query within the corpora. Supported values are 'drive' and 'appDataFolder'.
    Boolean supportsAllDrives = true; // Boolean | Whether the requesting application supports both My Drives and shared drives.
    Boolean supportsTeamDrives = true; // Boolean | Deprecated: Use `supportsAllDrives` instead.
    String teamDriveId = "teamDriveId_example"; // String | Deprecated: Use `driveId` instead.
    try {
      FileList result = apiInstance.driveFilesList($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, corpora, corpus, driveId, includeItemsFromAllDrives, includeLabels, includePermissionsForView, includeTeamDriveItems, orderBy, pageSize, pageToken, q, spaces, supportsAllDrives, supportsTeamDrives, teamDriveId);
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
| **corpora** | **String**| Bodies of items (files/documents) to which the query applies. Supported bodies are &#39;user&#39;, &#39;domain&#39;, &#39;drive&#39;, and &#39;allDrives&#39;. Prefer &#39;user&#39; or &#39;drive&#39; to &#39;allDrives&#39; for efficiency. By default, corpora is set to &#39;user&#39;. However, this can change depending on the filter set through the &#39;q&#39; parameter. | [optional] |
| **corpus** | **String**| Deprecated: The source of files to list. Use &#39;corpora&#39; instead. | [optional] [enum: domain, user] |
| **driveId** | **String**| ID of the shared drive to search. | [optional] |
| **includeItemsFromAllDrives** | **Boolean**| Whether both My Drive and shared drive items should be included in results. | [optional] |
| **includeLabels** | **String**| A comma-separated list of IDs of labels to include in the &#x60;labelInfo&#x60; part of the response. | [optional] |
| **includePermissionsForView** | **String**| Specifies which additional view&#39;s permissions to include in the response. Only &#39;published&#39; is supported. | [optional] |
| **includeTeamDriveItems** | **Boolean**| Deprecated: Use &#x60;includeItemsFromAllDrives&#x60; instead. | [optional] |
| **orderBy** | **String**| A comma-separated list of sort keys. Valid keys are &#39;createdTime&#39;, &#39;folder&#39;, &#39;modifiedByMeTime&#39;, &#39;modifiedTime&#39;, &#39;name&#39;, &#39;name_natural&#39;, &#39;quotaBytesUsed&#39;, &#39;recency&#39;, &#39;sharedWithMeTime&#39;, &#39;starred&#39;, and &#39;viewedByMeTime&#39;. Each key sorts ascending by default, but can be reversed with the &#39;desc&#39; modifier. Example usage: ?orderBy&#x3D;folder,modifiedTime desc,name. | [optional] |
| **pageSize** | **Integer**| The maximum number of files to return per page. Partial or empty result pages are possible even before the end of the files list has been reached. | [optional] |
| **pageToken** | **String**| The token for continuing a previous list request on the next page. This should be set to the value of &#39;nextPageToken&#39; from the previous response. | [optional] |
| **q** | **String**| A query for filtering the file results. See the \&quot;Search for files &amp; folders\&quot; guide for supported syntax. | [optional] |
| **spaces** | **String**| A comma-separated list of spaces to query within the corpora. Supported values are &#39;drive&#39; and &#39;appDataFolder&#39;. | [optional] |
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
    defaultClient.setBasePath("https://www.googleapis.com/drive/v3");
    
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
    String pageToken = "pageToken_example"; // String | The token for continuing a previous list request on the next page. This should be set to the value of 'nextPageToken' from the previous response.
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
| **pageToken** | **String**| The token for continuing a previous list request on the next page. This should be set to the value of &#39;nextPageToken&#39; from the previous response. | [optional] |

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
    defaultClient.setBasePath("https://www.googleapis.com/drive/v3");
    
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

<a id="driveFilesUpdate"></a>
# **driveFilesUpdate**
> ModelFile driveFilesUpdate(fileId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, addParents, enforceSingleParent, includeLabels, includePermissionsForView, keepRevisionForever, ocrLanguage, removeParents, supportsAllDrives, supportsTeamDrives, useContentAsIndexableText, modelFile)



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
    defaultClient.setBasePath("https://www.googleapis.com/drive/v3");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String fileId = "fileId_example"; // String | The ID of the file.
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
    String addParents = "addParents_example"; // String | A comma-separated list of parent IDs to add.
    Boolean enforceSingleParent = true; // Boolean | Deprecated: Adding files to multiple folders is no longer supported. Use shortcuts instead.
    String includeLabels = "includeLabels_example"; // String | A comma-separated list of IDs of labels to include in the `labelInfo` part of the response.
    String includePermissionsForView = "includePermissionsForView_example"; // String | Specifies which additional view's permissions to include in the response. Only 'published' is supported.
    Boolean keepRevisionForever = true; // Boolean | Whether to set the 'keepForever' field in the new head revision. This is only applicable to files with binary content in Google Drive. Only 200 revisions for the file can be kept forever. If the limit is reached, try deleting pinned revisions.
    String ocrLanguage = "ocrLanguage_example"; // String | A language hint for OCR processing during image import (ISO 639-1 code).
    String removeParents = "removeParents_example"; // String | A comma-separated list of parent IDs to remove.
    Boolean supportsAllDrives = true; // Boolean | Whether the requesting application supports both My Drives and shared drives.
    Boolean supportsTeamDrives = true; // Boolean | Deprecated: Use `supportsAllDrives` instead.
    Boolean useContentAsIndexableText = true; // Boolean | Whether to use the uploaded content as indexable text.
    ModelFile modelFile = new ModelFile(); // ModelFile | 
    try {
      ModelFile result = apiInstance.driveFilesUpdate(fileId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, addParents, enforceSingleParent, includeLabels, includePermissionsForView, keepRevisionForever, ocrLanguage, removeParents, supportsAllDrives, supportsTeamDrives, useContentAsIndexableText, modelFile);
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
| **fileId** | **String**| The ID of the file. | |
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
| **addParents** | **String**| A comma-separated list of parent IDs to add. | [optional] |
| **enforceSingleParent** | **Boolean**| Deprecated: Adding files to multiple folders is no longer supported. Use shortcuts instead. | [optional] |
| **includeLabels** | **String**| A comma-separated list of IDs of labels to include in the &#x60;labelInfo&#x60; part of the response. | [optional] |
| **includePermissionsForView** | **String**| Specifies which additional view&#39;s permissions to include in the response. Only &#39;published&#39; is supported. | [optional] |
| **keepRevisionForever** | **Boolean**| Whether to set the &#39;keepForever&#39; field in the new head revision. This is only applicable to files with binary content in Google Drive. Only 200 revisions for the file can be kept forever. If the limit is reached, try deleting pinned revisions. | [optional] |
| **ocrLanguage** | **String**| A language hint for OCR processing during image import (ISO 639-1 code). | [optional] |
| **removeParents** | **String**| A comma-separated list of parent IDs to remove. | [optional] |
| **supportsAllDrives** | **Boolean**| Whether the requesting application supports both My Drives and shared drives. | [optional] |
| **supportsTeamDrives** | **Boolean**| Deprecated: Use &#x60;supportsAllDrives&#x60; instead. | [optional] |
| **useContentAsIndexableText** | **Boolean**| Whether to use the uploaded content as indexable text. | [optional] |
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
> Channel driveFilesWatch(fileId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, acknowledgeAbuse, includeLabels, includePermissionsForView, supportsAllDrives, supportsTeamDrives, channel)



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
    defaultClient.setBasePath("https://www.googleapis.com/drive/v3");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String fileId = "fileId_example"; // String | The ID of the file.
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
    Boolean acknowledgeAbuse = true; // Boolean | Whether the user is acknowledging the risk of downloading known malware or other abusive files. This is only applicable when alt=media.
    String includeLabels = "includeLabels_example"; // String | A comma-separated list of IDs of labels to include in the `labelInfo` part of the response.
    String includePermissionsForView = "includePermissionsForView_example"; // String | Specifies which additional view's permissions to include in the response. Only 'published' is supported.
    Boolean supportsAllDrives = true; // Boolean | Whether the requesting application supports both My Drives and shared drives.
    Boolean supportsTeamDrives = true; // Boolean | Deprecated: Use `supportsAllDrives` instead.
    Channel channel = new Channel(); // Channel | 
    try {
      Channel result = apiInstance.driveFilesWatch(fileId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, acknowledgeAbuse, includeLabels, includePermissionsForView, supportsAllDrives, supportsTeamDrives, channel);
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
| **fileId** | **String**| The ID of the file. | |
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
| **acknowledgeAbuse** | **Boolean**| Whether the user is acknowledging the risk of downloading known malware or other abusive files. This is only applicable when alt&#x3D;media. | [optional] |
| **includeLabels** | **String**| A comma-separated list of IDs of labels to include in the &#x60;labelInfo&#x60; part of the response. | [optional] |
| **includePermissionsForView** | **String**| Specifies which additional view&#39;s permissions to include in the response. Only &#39;published&#39; is supported. | [optional] |
| **supportsAllDrives** | **Boolean**| Whether the requesting application supports both My Drives and shared drives. | [optional] |
| **supportsTeamDrives** | **Boolean**| Deprecated: Use &#x60;supportsAllDrives&#x60; instead. | [optional] |
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

