# SnapshotsApi

All URIs are relative to *https://lgtm.com/api/v1.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**abortUpload**](SnapshotsApi.md#abortUpload) | **DELETE** /snapshots/uploads/{session-id} | Abort database upload process |
| [**completeUpload**](SnapshotsApi.md#completeUpload) | **POST** /snapshots/uploads/{session-id} | Complete snapshot upload session |
| [**getSnapshot**](SnapshotsApi.md#getSnapshot) | **GET** /snapshots/{project-id}/{language} | Download a snapshot |
| [**initSnapshotUpload**](SnapshotsApi.md#initSnapshotUpload) | **POST** /snapshots/{project-id}/{language} | Start snapshot upload session |
| [**uploadPart**](SnapshotsApi.md#uploadPart) | **PUT** /snapshots/uploads/{session-id} | Upload snapshot |


<a id="abortUpload"></a>
# **abortUpload**
> Operation abortUpload(sessionId)

Abort database upload process

Aborts the specified upload session and deletes any uploaded parts. After the session is aborted it cannot be restarted. If any part uploads are in progress when the session is aborted, their data may not be deleted. To ensure that uploaded parts are deleted correctly, you should only abort an upload session after all part uploads have completed. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnapshotsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://lgtm.com/api/v1.0");
    
    // Configure HTTP bearer authorization: access-token
    HttpBearerAuth access-token = (HttpBearerAuth) defaultClient.getAuthentication("access-token");
    access-token.setBearerToken("BEARER TOKEN");

    SnapshotsApi apiInstance = new SnapshotsApi(defaultClient);
    String sessionId = "sessionId_example"; // String | The id of the upload session.
    try {
      Operation result = apiInstance.abortUpload(sessionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnapshotsApi#abortUpload");
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
| **sessionId** | **String**| The id of the upload session. | |

### Return type

[**Operation**](Operation.md)

### Authorization

[access-token](../README.md#access-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Aborted. |  -  |

<a id="completeUpload"></a>
# **completeUpload**
> Operation completeUpload(sessionId)

Complete snapshot upload session

Completes the database upload by closing the upload session, upgrading the database if appropriate, and scheduling analysis of that snapshot of the codebase.  You can view the analysis progress and access the results using the &#x60;task-result-url&#x60;. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnapshotsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://lgtm.com/api/v1.0");
    
    // Configure HTTP bearer authorization: access-token
    HttpBearerAuth access-token = (HttpBearerAuth) defaultClient.getAuthentication("access-token");
    access-token.setBearerToken("BEARER TOKEN");

    SnapshotsApi apiInstance = new SnapshotsApi(defaultClient);
    String sessionId = "sessionId_example"; // String | The id of the upload session.
    try {
      Operation result = apiInstance.completeUpload(sessionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnapshotsApi#completeUpload");
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
| **sessionId** | **String**| The id of the upload session. | |

### Return type

[**Operation**](Operation.md)

### Authorization

[access-token](../README.md#access-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Accepted. Analysis triggered. Tracking data returned. |  -  |

<a id="getSnapshot"></a>
# **getSnapshot**
> getSnapshot(projectId, language)

Download a snapshot

Download a CodeQL database from LGTM, representing a snapshot of the codebase, to run queries in your IDE.  This endpoint works for projects that have been successfully analyzed for the language specified in the request.  A successful request redirects you to a URL for downloading a database that represents the code snapshot, as specified in the &#x60;Location:&#x60; header in the response. Therefore, your HTTP client should be configured to follow redirects. For example, if you are using &#x60;curl&#x60;, you can add the&#x60;-L&#x60; flag to the command.  The database is downloaded as a zip file that can be imported into an IDE equipped with a  CodeQL extension. The extension must be up to date to analyze databases downloaded from LGTM. For more information on running queries locally in your IDE, see [Runnning queries in your IDE](https://lgtm.com/help/lgtm/running-queries-ide).  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnapshotsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://lgtm.com/api/v1.0");
    
    // Configure HTTP bearer authorization: access-token
    HttpBearerAuth access-token = (HttpBearerAuth) defaultClient.getAuthentication("access-token");
    access-token.setBearerToken("BEARER TOKEN");

    SnapshotsApi apiInstance = new SnapshotsApi(defaultClient);
    Long projectId = 56L; // Long | The numeric project identifier.
    String language = "language_example"; // String | The language of the database to download.
    try {
      apiInstance.getSnapshot(projectId, language);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnapshotsApi#getSnapshot");
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
| **projectId** | **Long**| The numeric project identifier. | |
| **language** | **String**| The language of the database to download. | |

### Return type

null (empty response body)

### Authorization

[access-token](../README.md#access-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **303** | Redirects to a URL for downloading the CodeQL database as indicated by the &#x60;Location:&#x60; header. |  * Location -  <br>  |

<a id="initSnapshotUpload"></a>
# **initSnapshotUpload**
> UploadSession initSnapshotUpload(projectId, language, commit, date)

Start snapshot upload session

Start a session to upload an externally-built database (which represents a snapshot of a codebase) to a project on LGTM.   This endpoint works for projects that are already on LGTM, and the selected language of  the database must already be configured. The project must be configured with &#39;upload&#39; analysis mode. You can upload a \&quot;bundled\&quot; CodeQL database or a database exported by  the QL command-line tools (&#x60;odasa&#x60;).  If your database was generated using a version of the  command line that is older than LGTM,  LGTM will try to upgrade and analyze it when the upload is complete. You can include cached predicates in the upload, but they are ignored as the cache is  repopulated after the database has been upgraded and analyzed. However, if you want to include results with your database, make sure the database is  compatible before you start the upload session.  Incompatible databases with results won&#39;t be upgraded and therefore cannot be uploaded.  For further information on externally-built databases,  see [Preparing snapshots to upload to LGTM using the QL command-line tools](https://help.semmle.com/wiki/display/SD/Preparing+snapshots+to+upload+to+LGTM).       When the upload session has been successfully started, upload the database to the  upload URL returned in the response. The database can be uploaded to the upload URL in parts using  the [&#x60;PUT /snapshots/uploads/{session-id}&#x60;](https://lgtm.com/help/lgtm/api/api-v1#opIduploadPart) endpoint. After uploading all the parts you must call  the [&#x60;POST /snapshots/uploads/{session-id}&#x60;](https://lgtm.com/help/lgtm/api/api-v1#opIdcompleteUpload) endpoint to complete the upload session. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnapshotsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://lgtm.com/api/v1.0");
    
    // Configure HTTP bearer authorization: access-token
    HttpBearerAuth access-token = (HttpBearerAuth) defaultClient.getAuthentication("access-token");
    access-token.setBearerToken("BEARER TOKEN");

    SnapshotsApi apiInstance = new SnapshotsApi(defaultClient);
    Long projectId = 56L; // Long | The numeric project identifier.
    String language = "language_example"; // String | The language of the database to upload.
    String commit = "commit_example"; // String | The identifier of the analyzed commit.
    OffsetDateTime date = OffsetDateTime.now(); // OffsetDateTime | The date and time of the analyzed commit (default the current time).
    try {
      UploadSession result = apiInstance.initSnapshotUpload(projectId, language, commit, date);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnapshotsApi#initSnapshotUpload");
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
| **projectId** | **Long**| The numeric project identifier. | |
| **language** | **String**| The language of the database to upload. | |
| **commit** | **String**| The identifier of the analyzed commit. | |
| **date** | **OffsetDateTime**| The date and time of the analyzed commit (default the current time). | [optional] |

### Return type

[**UploadSession**](UploadSession.md)

### Authorization

[access-token](../README.md#access-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success. |  -  |

<a id="uploadPart"></a>
# **uploadPart**
> uploadPart(sessionId, body)

Upload snapshot

Upload a database representing a snapshot of a codebase.  The database is sent in one or more parts. Each part is sent in the request body.  Use the [&#x60;POST /snapshots/{project-id}/{language}&#x60;](https://lgtm.com/help/lgtm/api/api-v1#opIdinitSnapshotUpload) endpoint  to start an upload session before uploading a database part. Database parts must have been generated and prepared for upload using the CodeQL CLI or the QL command-line tools. For further information on exporting externally-built databases,  see [Preparing snapshots to upload to LGTM](https://help.semmle.com/wiki/display/SD/Preparing+snapshots+to+upload+to+LGTM).  Split large databases into multiple parts. Upload the parts by making a separate request for each part.  Don&#39;t upload the next part until you&#39;ve successfully uploaded the previous part.  If the upload fails you should retry it with the same data. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnapshotsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://lgtm.com/api/v1.0");
    
    // Configure HTTP bearer authorization: access-token
    HttpBearerAuth access-token = (HttpBearerAuth) defaultClient.getAuthentication("access-token");
    access-token.setBearerToken("BEARER TOKEN");

    SnapshotsApi apiInstance = new SnapshotsApi(defaultClient);
    String sessionId = "sessionId_example"; // String | The id of the upload session.
    File body = new File("/path/to/file"); // File | The database or database part to upload.
    try {
      apiInstance.uploadPart(sessionId, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnapshotsApi#uploadPart");
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
| **sessionId** | **String**| The id of the upload session. | |
| **body** | **File**| The database or database part to upload. | |

### Return type

null (empty response body)

### Authorization

[access-token](../README.md#access-token)

### HTTP request headers

 - **Content-Type**: application/octet-stream, application/zip
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success. |  -  |

