# FilesApi

All URIs are relative to *https://slack.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**filesCommentsDelete_0**](FilesApi.md#filesCommentsDelete_0) | **POST** /files.comments.delete |  |
| [**filesDelete**](FilesApi.md#filesDelete) | **POST** /files.delete |  |
| [**filesInfo**](FilesApi.md#filesInfo) | **GET** /files.info |  |
| [**filesList**](FilesApi.md#filesList) | **GET** /files.list |  |
| [**filesRemoteAdd_0**](FilesApi.md#filesRemoteAdd_0) | **POST** /files.remote.add |  |
| [**filesRemoteInfo_0**](FilesApi.md#filesRemoteInfo_0) | **GET** /files.remote.info |  |
| [**filesRemoteList_0**](FilesApi.md#filesRemoteList_0) | **GET** /files.remote.list |  |
| [**filesRemoteRemove_0**](FilesApi.md#filesRemoteRemove_0) | **POST** /files.remote.remove |  |
| [**filesRemoteShare_0**](FilesApi.md#filesRemoteShare_0) | **GET** /files.remote.share |  |
| [**filesRemoteUpdate_0**](FilesApi.md#filesRemoteUpdate_0) | **POST** /files.remote.update |  |
| [**filesRevokePublicURL**](FilesApi.md#filesRevokePublicURL) | **POST** /files.revokePublicURL |  |
| [**filesSharedPublicURL**](FilesApi.md#filesSharedPublicURL) | **POST** /files.sharedPublicURL |  |
| [**filesUpload**](FilesApi.md#filesUpload) | **POST** /files.upload |  |


<a id="filesCommentsDelete_0"></a>
# **filesCommentsDelete_0**
> FilesCommentsDeleteSchema filesCommentsDelete_0(token, _file, id)



Deletes an existing comment on a file.

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
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `files:write:user`
    String _file = "_file_example"; // String | File to delete a comment from.
    String id = "id_example"; // String | The comment to delete.
    try {
      FilesCommentsDeleteSchema result = apiInstance.filesCommentsDelete_0(token, _file, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#filesCommentsDelete_0");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;files:write:user&#x60; | [optional] |
| **_file** | **String**| File to delete a comment from. | [optional] |
| **id** | **String**| The comment to delete. | [optional] |

### Return type

[**FilesCommentsDeleteSchema**](FilesCommentsDeleteSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Standard success response is very simple |  -  |
| **0** | Standard failure response when used with an invalid token |  -  |

<a id="filesDelete"></a>
# **filesDelete**
> FilesDeleteSchema filesDelete(token, _file)



Deletes a file.

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
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `files:write:user`
    String _file = "_file_example"; // String | ID of file to delete.
    try {
      FilesDeleteSchema result = apiInstance.filesDelete(token, _file);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#filesDelete");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;files:write:user&#x60; | [optional] |
| **_file** | **String**| ID of file to delete. | [optional] |

### Return type

[**FilesDeleteSchema**](FilesDeleteSchema.md)

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

<a id="filesInfo"></a>
# **filesInfo**
> FilesInfoSchema filesInfo(token, _file, count, page, limit, cursor)



Gets information about a file.

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
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `files:read`
    String _file = "_file_example"; // String | Specify a file by providing its ID.
    String count = "count_example"; // String | 
    String page = "page_example"; // String | 
    Integer limit = 56; // Integer | The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the list hasn't been reached.
    String cursor = "cursor_example"; // String | Parameter for pagination. File comments are paginated for a single file. Set `cursor` equal to the `next_cursor` attribute returned by the previous request's `response_metadata`. This parameter is optional, but pagination is mandatory: the default value simply fetches the first \"page\" of the collection of comments. See [pagination](/docs/pagination) for more details.
    try {
      FilesInfoSchema result = apiInstance.filesInfo(token, _file, count, page, limit, cursor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#filesInfo");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;files:read&#x60; | [optional] |
| **_file** | **String**| Specify a file by providing its ID. | [optional] |
| **count** | **String**|  | [optional] |
| **page** | **String**|  | [optional] |
| **limit** | **Integer**| The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the list hasn&#39;t been reached. | [optional] |
| **cursor** | **String**| Parameter for pagination. File comments are paginated for a single file. Set &#x60;cursor&#x60; equal to the &#x60;next_cursor&#x60; attribute returned by the previous request&#39;s &#x60;response_metadata&#x60;. This parameter is optional, but pagination is mandatory: the default value simply fetches the first \&quot;page\&quot; of the collection of comments. See [pagination](/docs/pagination) for more details. | [optional] |

### Return type

[**FilesInfoSchema**](FilesInfoSchema.md)

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

<a id="filesList"></a>
# **filesList**
> FilesListSchema filesList(token, user, channel, tsFrom, tsTo, types, count, page, showFilesHiddenByLimit)



List for a team, in a channel, or from a user with applied filters.

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
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `files:read`
    String user = "user_example"; // String | Filter files created by a single user.
    String channel = "channel_example"; // String | Filter files appearing in a specific channel, indicated by its ID.
    BigDecimal tsFrom = new BigDecimal(78); // BigDecimal | Filter files created after this timestamp (inclusive).
    BigDecimal tsTo = new BigDecimal(78); // BigDecimal | Filter files created before this timestamp (inclusive).
    String types = "types_example"; // String | Filter files by type ([see below](#file_types)). You can pass multiple values in the types argument, like `types=spaces,snippets`.The default value is `all`, which does not filter the list.
    String count = "count_example"; // String | 
    String page = "page_example"; // String | 
    Boolean showFilesHiddenByLimit = true; // Boolean | Show truncated file info for files hidden due to being too old, and the team who owns the file being over the file limit.
    try {
      FilesListSchema result = apiInstance.filesList(token, user, channel, tsFrom, tsTo, types, count, page, showFilesHiddenByLimit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#filesList");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;files:read&#x60; | [optional] |
| **user** | **String**| Filter files created by a single user. | [optional] |
| **channel** | **String**| Filter files appearing in a specific channel, indicated by its ID. | [optional] |
| **tsFrom** | **BigDecimal**| Filter files created after this timestamp (inclusive). | [optional] |
| **tsTo** | **BigDecimal**| Filter files created before this timestamp (inclusive). | [optional] |
| **types** | **String**| Filter files by type ([see below](#file_types)). You can pass multiple values in the types argument, like &#x60;types&#x3D;spaces,snippets&#x60;.The default value is &#x60;all&#x60;, which does not filter the list. | [optional] |
| **count** | **String**|  | [optional] |
| **page** | **String**|  | [optional] |
| **showFilesHiddenByLimit** | **Boolean**| Show truncated file info for files hidden due to being too old, and the team who owns the file being over the file limit. | [optional] |

### Return type

[**FilesListSchema**](FilesListSchema.md)

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

<a id="filesRemoteAdd_0"></a>
# **filesRemoteAdd_0**
> DefaultSuccessTemplate filesRemoteAdd_0(externalId, externalUrl, filetype, indexableFileContents, previewImage, title, token)



Adds a file from a remote service

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
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String externalId = "externalId_example"; // String | Creator defined GUID for the file.
    String externalUrl = "externalUrl_example"; // String | URL of the remote file.
    String filetype = "filetype_example"; // String | type of file
    String indexableFileContents = "indexableFileContents_example"; // String | A text file (txt, pdf, doc, etc.) containing textual search terms that are used to improve discovery of the remote file.
    String previewImage = "previewImage_example"; // String | Preview of the document via `multipart/form-data`.
    String title = "title_example"; // String | Title of the file being shared.
    String token = "token_example"; // String | Authentication token. Requires scope: `remote_files:write`
    try {
      DefaultSuccessTemplate result = apiInstance.filesRemoteAdd_0(externalId, externalUrl, filetype, indexableFileContents, previewImage, title, token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#filesRemoteAdd_0");
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

<a id="filesRemoteInfo_0"></a>
# **filesRemoteInfo_0**
> DefaultSuccessTemplate filesRemoteInfo_0(token, _file, externalId)



Retrieve information about a remote file added to Slack

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
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `remote_files:read`
    String _file = "_file_example"; // String | Specify a file by providing its ID.
    String externalId = "externalId_example"; // String | Creator defined GUID for the file.
    try {
      DefaultSuccessTemplate result = apiInstance.filesRemoteInfo_0(token, _file, externalId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#filesRemoteInfo_0");
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

<a id="filesRemoteList_0"></a>
# **filesRemoteList_0**
> DefaultSuccessTemplate filesRemoteList_0(token, channel, tsFrom, tsTo, limit, cursor)



Retrieve information about a remote file added to Slack

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
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `remote_files:read`
    String channel = "channel_example"; // String | Filter files appearing in a specific channel, indicated by its ID.
    BigDecimal tsFrom = new BigDecimal(78); // BigDecimal | Filter files created after this timestamp (inclusive).
    BigDecimal tsTo = new BigDecimal(78); // BigDecimal | Filter files created before this timestamp (inclusive).
    Integer limit = 56; // Integer | The maximum number of items to return.
    String cursor = "cursor_example"; // String | Paginate through collections of data by setting the `cursor` parameter to a `next_cursor` attribute returned by a previous request's `response_metadata`. Default value fetches the first \"page\" of the collection. See [pagination](/docs/pagination) for more detail.
    try {
      DefaultSuccessTemplate result = apiInstance.filesRemoteList_0(token, channel, tsFrom, tsTo, limit, cursor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#filesRemoteList_0");
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

<a id="filesRemoteRemove_0"></a>
# **filesRemoteRemove_0**
> DefaultSuccessTemplate filesRemoteRemove_0(externalId, _file, token)



Remove a remote file.

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
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String externalId = "externalId_example"; // String | Creator defined GUID for the file.
    String _file = "_file_example"; // String | Specify a file by providing its ID.
    String token = "token_example"; // String | Authentication token. Requires scope: `remote_files:write`
    try {
      DefaultSuccessTemplate result = apiInstance.filesRemoteRemove_0(externalId, _file, token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#filesRemoteRemove_0");
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

<a id="filesRemoteShare_0"></a>
# **filesRemoteShare_0**
> DefaultSuccessTemplate filesRemoteShare_0(token, _file, externalId, channels)



Share a remote file into a channel.

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
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `remote_files:share`
    String _file = "_file_example"; // String | Specify a file registered with Slack by providing its ID. Either this field or `external_id` or both are required.
    String externalId = "externalId_example"; // String | The globally unique identifier (GUID) for the file, as set by the app registering the file with Slack.  Either this field or `file` or both are required.
    String channels = "channels_example"; // String | Comma-separated list of channel IDs where the file will be shared.
    try {
      DefaultSuccessTemplate result = apiInstance.filesRemoteShare_0(token, _file, externalId, channels);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#filesRemoteShare_0");
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

<a id="filesRemoteUpdate_0"></a>
# **filesRemoteUpdate_0**
> DefaultSuccessTemplate filesRemoteUpdate_0(externalId, externalUrl, _file, filetype, indexableFileContents, previewImage, title, token)



Updates an existing remote file.

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
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String externalId = "externalId_example"; // String | Creator defined GUID for the file.
    String externalUrl = "externalUrl_example"; // String | URL of the remote file.
    String _file = "_file_example"; // String | Specify a file by providing its ID.
    String filetype = "filetype_example"; // String | type of file
    String indexableFileContents = "indexableFileContents_example"; // String | File containing contents that can be used to improve searchability for the remote file.
    String previewImage = "previewImage_example"; // String | Preview of the document via `multipart/form-data`.
    String title = "title_example"; // String | Title of the file being shared.
    String token = "token_example"; // String | Authentication token. Requires scope: `remote_files:write`
    try {
      DefaultSuccessTemplate result = apiInstance.filesRemoteUpdate_0(externalId, externalUrl, _file, filetype, indexableFileContents, previewImage, title, token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#filesRemoteUpdate_0");
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

<a id="filesRevokePublicURL"></a>
# **filesRevokePublicURL**
> FilesRevokePublicURLSchema filesRevokePublicURL(token, _file)



Revokes public/external sharing access for a file

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
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `files:write:user`
    String _file = "_file_example"; // String | File to revoke
    try {
      FilesRevokePublicURLSchema result = apiInstance.filesRevokePublicURL(token, _file);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#filesRevokePublicURL");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;files:write:user&#x60; | [optional] |
| **_file** | **String**| File to revoke | [optional] |

### Return type

[**FilesRevokePublicURLSchema**](FilesRevokePublicURLSchema.md)

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

<a id="filesSharedPublicURL"></a>
# **filesSharedPublicURL**
> FilesSharedPublicURLSchema filesSharedPublicURL(token, _file)



Enables a file for public/external sharing.

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
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `files:write:user`
    String _file = "_file_example"; // String | File to share
    try {
      FilesSharedPublicURLSchema result = apiInstance.filesSharedPublicURL(token, _file);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#filesSharedPublicURL");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;files:write:user&#x60; | [optional] |
| **_file** | **String**| File to share | [optional] |

### Return type

[**FilesSharedPublicURLSchema**](FilesSharedPublicURLSchema.md)

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

<a id="filesUpload"></a>
# **filesUpload**
> FilesUploadSchema filesUpload(channels, content, _file, filename, filetype, initialComment, threadTs, title, token)



Uploads or creates a file.

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
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String channels = "channels_example"; // String | Comma-separated list of channel names or IDs where the file will be shared.
    String content = "content_example"; // String | File contents via a POST variable. If omitting this parameter, you must provide a `file`.
    String _file = "_file_example"; // String | File contents via `multipart/form-data`. If omitting this parameter, you must submit `content`.
    String filename = "filename_example"; // String | Filename of file.
    String filetype = "filetype_example"; // String | A [file type](/types/file#file_types) identifier.
    String initialComment = "initialComment_example"; // String | The message text introducing the file in specified `channels`.
    BigDecimal threadTs = new BigDecimal(78); // BigDecimal | Provide another message's `ts` value to upload this file as a reply. Never use a reply's `ts` value; use its parent instead.
    String title = "title_example"; // String | Title of file.
    String token = "token_example"; // String | Authentication token. Requires scope: `files:write:user`
    try {
      FilesUploadSchema result = apiInstance.filesUpload(channels, content, _file, filename, filetype, initialComment, threadTs, title, token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#filesUpload");
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
| **channels** | **String**| Comma-separated list of channel names or IDs where the file will be shared. | [optional] |
| **content** | **String**| File contents via a POST variable. If omitting this parameter, you must provide a &#x60;file&#x60;. | [optional] |
| **_file** | **String**| File contents via &#x60;multipart/form-data&#x60;. If omitting this parameter, you must submit &#x60;content&#x60;. | [optional] |
| **filename** | **String**| Filename of file. | [optional] |
| **filetype** | **String**| A [file type](/types/file#file_types) identifier. | [optional] |
| **initialComment** | **String**| The message text introducing the file in specified &#x60;channels&#x60;. | [optional] |
| **threadTs** | **BigDecimal**| Provide another message&#39;s &#x60;ts&#x60; value to upload this file as a reply. Never use a reply&#39;s &#x60;ts&#x60; value; use its parent instead. | [optional] |
| **title** | **String**| Title of file. | [optional] |
| **token** | **String**| Authentication token. Requires scope: &#x60;files:write:user&#x60; | [optional] |

### Return type

[**FilesUploadSchema**](FilesUploadSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success response after uploading a file to a channel with an initial message |  -  |
| **0** | Typical error response |  -  |

