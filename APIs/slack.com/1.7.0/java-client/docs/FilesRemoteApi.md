# FilesRemoteApi

All URIs are relative to *https://slack.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**filesRemoteAdd**](FilesRemoteApi.md#filesRemoteAdd) | **POST** /files.remote.add |  |
| [**filesRemoteInfo**](FilesRemoteApi.md#filesRemoteInfo) | **GET** /files.remote.info |  |
| [**filesRemoteList**](FilesRemoteApi.md#filesRemoteList) | **GET** /files.remote.list |  |
| [**filesRemoteRemove**](FilesRemoteApi.md#filesRemoteRemove) | **POST** /files.remote.remove |  |
| [**filesRemoteShare**](FilesRemoteApi.md#filesRemoteShare) | **GET** /files.remote.share |  |
| [**filesRemoteUpdate**](FilesRemoteApi.md#filesRemoteUpdate) | **POST** /files.remote.update |  |


<a id="filesRemoteAdd"></a>
# **filesRemoteAdd**
> DefaultSuccessTemplate filesRemoteAdd(externalId, externalUrl, filetype, indexableFileContents, previewImage, title, token)



Adds a file from a remote service

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesRemoteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    FilesRemoteApi apiInstance = new FilesRemoteApi(defaultClient);
    String externalId = "externalId_example"; // String | Creator defined GUID for the file.
    String externalUrl = "externalUrl_example"; // String | URL of the remote file.
    String filetype = "filetype_example"; // String | type of file
    String indexableFileContents = "indexableFileContents_example"; // String | A text file (txt, pdf, doc, etc.) containing textual search terms that are used to improve discovery of the remote file.
    String previewImage = "previewImage_example"; // String | Preview of the document via `multipart/form-data`.
    String title = "title_example"; // String | Title of the file being shared.
    String token = "token_example"; // String | Authentication token. Requires scope: `remote_files:write`
    try {
      DefaultSuccessTemplate result = apiInstance.filesRemoteAdd(externalId, externalUrl, filetype, indexableFileContents, previewImage, title, token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesRemoteApi#filesRemoteAdd");
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
| **externalId** | **String**| Creator defined GUID for the file. | [optional] |
| **externalUrl** | **String**| URL of the remote file. | [optional] |
| **filetype** | **String**| type of file | [optional] |
| **indexableFileContents** | **String**| A text file (txt, pdf, doc, etc.) containing textual search terms that are used to improve discovery of the remote file. | [optional] |
| **previewImage** | **String**| Preview of the document via &#x60;multipart/form-data&#x60;. | [optional] |
| **title** | **String**| Title of the file being shared. | [optional] |
| **token** | **String**| Authentication token. Requires scope: &#x60;remote_files:write&#x60; | [optional] |

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response |  -  |
| **0** | Typical error response |  -  |

<a id="filesRemoteInfo"></a>
# **filesRemoteInfo**
> DefaultSuccessTemplate filesRemoteInfo(token, _file, externalId)



Retrieve information about a remote file added to Slack

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesRemoteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    FilesRemoteApi apiInstance = new FilesRemoteApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `remote_files:read`
    String _file = "_file_example"; // String | Specify a file by providing its ID.
    String externalId = "externalId_example"; // String | Creator defined GUID for the file.
    try {
      DefaultSuccessTemplate result = apiInstance.filesRemoteInfo(token, _file, externalId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesRemoteApi#filesRemoteInfo");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;remote_files:read&#x60; | [optional] |
| **_file** | **String**| Specify a file by providing its ID. | [optional] |
| **externalId** | **String**| Creator defined GUID for the file. | [optional] |

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response |  -  |
| **0** | Typical error response |  -  |

<a id="filesRemoteList"></a>
# **filesRemoteList**
> DefaultSuccessTemplate filesRemoteList(token, channel, tsFrom, tsTo, limit, cursor)



Retrieve information about a remote file added to Slack

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesRemoteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    FilesRemoteApi apiInstance = new FilesRemoteApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `remote_files:read`
    String channel = "channel_example"; // String | Filter files appearing in a specific channel, indicated by its ID.
    BigDecimal tsFrom = new BigDecimal(78); // BigDecimal | Filter files created after this timestamp (inclusive).
    BigDecimal tsTo = new BigDecimal(78); // BigDecimal | Filter files created before this timestamp (inclusive).
    Integer limit = 56; // Integer | The maximum number of items to return.
    String cursor = "cursor_example"; // String | Paginate through collections of data by setting the `cursor` parameter to a `next_cursor` attribute returned by a previous request's `response_metadata`. Default value fetches the first \"page\" of the collection. See [pagination](/docs/pagination) for more detail.
    try {
      DefaultSuccessTemplate result = apiInstance.filesRemoteList(token, channel, tsFrom, tsTo, limit, cursor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesRemoteApi#filesRemoteList");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;remote_files:read&#x60; | [optional] |
| **channel** | **String**| Filter files appearing in a specific channel, indicated by its ID. | [optional] |
| **tsFrom** | **BigDecimal**| Filter files created after this timestamp (inclusive). | [optional] |
| **tsTo** | **BigDecimal**| Filter files created before this timestamp (inclusive). | [optional] |
| **limit** | **Integer**| The maximum number of items to return. | [optional] |
| **cursor** | **String**| Paginate through collections of data by setting the &#x60;cursor&#x60; parameter to a &#x60;next_cursor&#x60; attribute returned by a previous request&#39;s &#x60;response_metadata&#x60;. Default value fetches the first \&quot;page\&quot; of the collection. See [pagination](/docs/pagination) for more detail. | [optional] |

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response |  -  |
| **0** | Typical error response |  -  |

<a id="filesRemoteRemove"></a>
# **filesRemoteRemove**
> DefaultSuccessTemplate filesRemoteRemove(externalId, _file, token)



Remove a remote file.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesRemoteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    FilesRemoteApi apiInstance = new FilesRemoteApi(defaultClient);
    String externalId = "externalId_example"; // String | Creator defined GUID for the file.
    String _file = "_file_example"; // String | Specify a file by providing its ID.
    String token = "token_example"; // String | Authentication token. Requires scope: `remote_files:write`
    try {
      DefaultSuccessTemplate result = apiInstance.filesRemoteRemove(externalId, _file, token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesRemoteApi#filesRemoteRemove");
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
| **externalId** | **String**| Creator defined GUID for the file. | [optional] |
| **_file** | **String**| Specify a file by providing its ID. | [optional] |
| **token** | **String**| Authentication token. Requires scope: &#x60;remote_files:write&#x60; | [optional] |

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response |  -  |
| **0** | Typical error response |  -  |

<a id="filesRemoteShare"></a>
# **filesRemoteShare**
> DefaultSuccessTemplate filesRemoteShare(token, _file, externalId, channels)



Share a remote file into a channel.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesRemoteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    FilesRemoteApi apiInstance = new FilesRemoteApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `remote_files:share`
    String _file = "_file_example"; // String | Specify a file registered with Slack by providing its ID. Either this field or `external_id` or both are required.
    String externalId = "externalId_example"; // String | The globally unique identifier (GUID) for the file, as set by the app registering the file with Slack.  Either this field or `file` or both are required.
    String channels = "channels_example"; // String | Comma-separated list of channel IDs where the file will be shared.
    try {
      DefaultSuccessTemplate result = apiInstance.filesRemoteShare(token, _file, externalId, channels);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesRemoteApi#filesRemoteShare");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;remote_files:share&#x60; | [optional] |
| **_file** | **String**| Specify a file registered with Slack by providing its ID. Either this field or &#x60;external_id&#x60; or both are required. | [optional] |
| **externalId** | **String**| The globally unique identifier (GUID) for the file, as set by the app registering the file with Slack.  Either this field or &#x60;file&#x60; or both are required. | [optional] |
| **channels** | **String**| Comma-separated list of channel IDs where the file will be shared. | [optional] |

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response |  -  |
| **0** | Typical error response |  -  |

<a id="filesRemoteUpdate"></a>
# **filesRemoteUpdate**
> DefaultSuccessTemplate filesRemoteUpdate(externalId, externalUrl, _file, filetype, indexableFileContents, previewImage, title, token)



Updates an existing remote file.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesRemoteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    FilesRemoteApi apiInstance = new FilesRemoteApi(defaultClient);
    String externalId = "externalId_example"; // String | Creator defined GUID for the file.
    String externalUrl = "externalUrl_example"; // String | URL of the remote file.
    String _file = "_file_example"; // String | Specify a file by providing its ID.
    String filetype = "filetype_example"; // String | type of file
    String indexableFileContents = "indexableFileContents_example"; // String | File containing contents that can be used to improve searchability for the remote file.
    String previewImage = "previewImage_example"; // String | Preview of the document via `multipart/form-data`.
    String title = "title_example"; // String | Title of the file being shared.
    String token = "token_example"; // String | Authentication token. Requires scope: `remote_files:write`
    try {
      DefaultSuccessTemplate result = apiInstance.filesRemoteUpdate(externalId, externalUrl, _file, filetype, indexableFileContents, previewImage, title, token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesRemoteApi#filesRemoteUpdate");
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
| **externalId** | **String**| Creator defined GUID for the file. | [optional] |
| **externalUrl** | **String**| URL of the remote file. | [optional] |
| **_file** | **String**| Specify a file by providing its ID. | [optional] |
| **filetype** | **String**| type of file | [optional] |
| **indexableFileContents** | **String**| File containing contents that can be used to improve searchability for the remote file. | [optional] |
| **previewImage** | **String**| Preview of the document via &#x60;multipart/form-data&#x60;. | [optional] |
| **title** | **String**| Title of the file being shared. | [optional] |
| **token** | **String**| Authentication token. Requires scope: &#x60;remote_files:write&#x60; | [optional] |

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response |  -  |
| **0** | Typical error response |  -  |

