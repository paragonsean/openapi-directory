# SnippetsApi

All URIs are relative to *https://api.bitbucket.org/2.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**snippetsGet**](SnippetsApi.md#snippetsGet) | **GET** /snippets | List snippets |
| [**snippetsPost**](SnippetsApi.md#snippetsPost) | **POST** /snippets | Create a snippet |
| [**snippetsWorkspaceEncodedIdCommentsCommentIdDelete**](SnippetsApi.md#snippetsWorkspaceEncodedIdCommentsCommentIdDelete) | **DELETE** /snippets/{workspace}/{encoded_id}/comments/{comment_id} | Delete a comment on a snippet |
| [**snippetsWorkspaceEncodedIdCommentsCommentIdGet**](SnippetsApi.md#snippetsWorkspaceEncodedIdCommentsCommentIdGet) | **GET** /snippets/{workspace}/{encoded_id}/comments/{comment_id} | Get a comment on a snippet |
| [**snippetsWorkspaceEncodedIdCommentsCommentIdPut**](SnippetsApi.md#snippetsWorkspaceEncodedIdCommentsCommentIdPut) | **PUT** /snippets/{workspace}/{encoded_id}/comments/{comment_id} | Update a comment on a snippet |
| [**snippetsWorkspaceEncodedIdCommentsGet**](SnippetsApi.md#snippetsWorkspaceEncodedIdCommentsGet) | **GET** /snippets/{workspace}/{encoded_id}/comments | List comments on a snippet |
| [**snippetsWorkspaceEncodedIdCommentsPost**](SnippetsApi.md#snippetsWorkspaceEncodedIdCommentsPost) | **POST** /snippets/{workspace}/{encoded_id}/comments | Create a comment on a snippet |
| [**snippetsWorkspaceEncodedIdCommitsGet**](SnippetsApi.md#snippetsWorkspaceEncodedIdCommitsGet) | **GET** /snippets/{workspace}/{encoded_id}/commits | List snippet changes |
| [**snippetsWorkspaceEncodedIdCommitsRevisionGet**](SnippetsApi.md#snippetsWorkspaceEncodedIdCommitsRevisionGet) | **GET** /snippets/{workspace}/{encoded_id}/commits/{revision} | Get a previous snippet change |
| [**snippetsWorkspaceEncodedIdDelete**](SnippetsApi.md#snippetsWorkspaceEncodedIdDelete) | **DELETE** /snippets/{workspace}/{encoded_id} | Delete a snippet |
| [**snippetsWorkspaceEncodedIdFilesPathGet**](SnippetsApi.md#snippetsWorkspaceEncodedIdFilesPathGet) | **GET** /snippets/{workspace}/{encoded_id}/files/{path} | Get a snippet&#39;s raw file at HEAD |
| [**snippetsWorkspaceEncodedIdGet**](SnippetsApi.md#snippetsWorkspaceEncodedIdGet) | **GET** /snippets/{workspace}/{encoded_id} | Get a snippet |
| [**snippetsWorkspaceEncodedIdNodeIdDelete**](SnippetsApi.md#snippetsWorkspaceEncodedIdNodeIdDelete) | **DELETE** /snippets/{workspace}/{encoded_id}/{node_id} | Delete a previous revision of a snippet |
| [**snippetsWorkspaceEncodedIdNodeIdFilesPathGet**](SnippetsApi.md#snippetsWorkspaceEncodedIdNodeIdFilesPathGet) | **GET** /snippets/{workspace}/{encoded_id}/{node_id}/files/{path} | Get a snippet&#39;s raw file |
| [**snippetsWorkspaceEncodedIdNodeIdGet**](SnippetsApi.md#snippetsWorkspaceEncodedIdNodeIdGet) | **GET** /snippets/{workspace}/{encoded_id}/{node_id} | Get a previous revision of a snippet |
| [**snippetsWorkspaceEncodedIdNodeIdPut**](SnippetsApi.md#snippetsWorkspaceEncodedIdNodeIdPut) | **PUT** /snippets/{workspace}/{encoded_id}/{node_id} | Update a previous revision of a snippet |
| [**snippetsWorkspaceEncodedIdPut**](SnippetsApi.md#snippetsWorkspaceEncodedIdPut) | **PUT** /snippets/{workspace}/{encoded_id} | Update a snippet |
| [**snippetsWorkspaceEncodedIdRevisionDiffGet**](SnippetsApi.md#snippetsWorkspaceEncodedIdRevisionDiffGet) | **GET** /snippets/{workspace}/{encoded_id}/{revision}/diff | Get snippet changes between versions |
| [**snippetsWorkspaceEncodedIdRevisionPatchGet**](SnippetsApi.md#snippetsWorkspaceEncodedIdRevisionPatchGet) | **GET** /snippets/{workspace}/{encoded_id}/{revision}/patch | Get snippet patch between versions |
| [**snippetsWorkspaceEncodedIdWatchDelete**](SnippetsApi.md#snippetsWorkspaceEncodedIdWatchDelete) | **DELETE** /snippets/{workspace}/{encoded_id}/watch | Stop watching a snippet |
| [**snippetsWorkspaceEncodedIdWatchGet**](SnippetsApi.md#snippetsWorkspaceEncodedIdWatchGet) | **GET** /snippets/{workspace}/{encoded_id}/watch | Check if the current user is watching a snippet |
| [**snippetsWorkspaceEncodedIdWatchPut**](SnippetsApi.md#snippetsWorkspaceEncodedIdWatchPut) | **PUT** /snippets/{workspace}/{encoded_id}/watch | Watch a snippet |
| [**snippetsWorkspaceEncodedIdWatchersGet**](SnippetsApi.md#snippetsWorkspaceEncodedIdWatchersGet) | **GET** /snippets/{workspace}/{encoded_id}/watchers | List users watching a snippet |
| [**snippetsWorkspaceGet**](SnippetsApi.md#snippetsWorkspaceGet) | **GET** /snippets/{workspace} | List snippets in a workspace |
| [**snippetsWorkspacePost**](SnippetsApi.md#snippetsWorkspacePost) | **POST** /snippets/{workspace} | Create a snippet for a workspace |


<a id="snippetsGet"></a>
# **snippetsGet**
> PaginatedSnippets snippetsGet(role)

List snippets

Returns all snippets. Like pull requests, repositories and workspaces, the full set of snippets is defined by what the current user has access to.  This includes all snippets owned by any of the workspaces the user is a member of, or snippets by other users that the current user is either watching or has collaborated on (for instance by commenting on it).  To limit the set of returned snippets, apply the &#x60;?role&#x3D;[owner|contributor|member]&#x60; query parameter where the roles are defined as follows:  * &#x60;owner&#x60;: all snippets owned by the current user * &#x60;contributor&#x60;: all snippets owned by, or watched by the current user * &#x60;member&#x60;: created in a workspaces or watched by the current user  When no role is specified, all public snippets are returned, as well as all privately owned snippets watched or commented on.  The returned response is a normal paginated JSON list. This endpoint only supports &#x60;application/json&#x60; responses and no &#x60;multipart/form-data&#x60; or &#x60;multipart/related&#x60;. As a result, it is not possible to include the file contents.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnippetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    SnippetsApi apiInstance = new SnippetsApi(defaultClient);
    String role = "owner"; // String | Filter down the result based on the authenticated user's role (`owner`, `contributor`, or `member`).
    try {
      PaginatedSnippets result = apiInstance.snippetsGet(role);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnippetsApi#snippetsGet");
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
| **role** | **String**| Filter down the result based on the authenticated user&#39;s role (&#x60;owner&#x60;, &#x60;contributor&#x60;, or &#x60;member&#x60;). | [optional] [enum: owner, contributor, member] |

### Return type

[**PaginatedSnippets**](PaginatedSnippets.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A paginated list of snippets. |  -  |
| **404** | If the snippet does not exist. |  -  |

<a id="snippetsPost"></a>
# **snippetsPost**
> Snippet snippetsPost(snippet)

Create a snippet

Creates a new snippet under the authenticated user&#39;s account.  Snippets can contain multiple files. Both text and binary files are supported.  The simplest way to create a new snippet from a local file:      $ curl -u username:password -X POST https://api.bitbucket.org/2.0/snippets               -F file&#x3D;@image.png  Creating snippets through curl has a few limitations and so let&#39;s look at a more complicated scenario.  Snippets are created with a multipart POST. Both &#x60;multipart/form-data&#x60; and &#x60;multipart/related&#x60; are supported. Both allow the creation of snippets with both meta data (title, etc), as well as multiple text and binary files.  The main difference is that &#x60;multipart/related&#x60; can use rich encoding for the meta data (currently JSON).   multipart/related (RFC-2387) ----------------------------  This is the most advanced and efficient way to create a paste.      POST /2.0/snippets/evzijst HTTP/1.1     Content-Length: 1188     Content-Type: multipart/related; start&#x3D;\&quot;snippet\&quot;; boundary&#x3D;\&quot;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;1438169132528273974&#x3D;&#x3D;\&quot;     MIME-Version: 1.0      --&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;1438169132528273974&#x3D;&#x3D;     Content-Type: application/json; charset&#x3D;\&quot;utf-8\&quot;     MIME-Version: 1.0     Content-ID: snippet      {       \&quot;title\&quot;: \&quot;My snippet\&quot;,       \&quot;is_private\&quot;: true,       \&quot;scm\&quot;: \&quot;git\&quot;,       \&quot;files\&quot;: {           \&quot;foo.txt\&quot;: {},           \&quot;image.png\&quot;: {}         }     }      --&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;1438169132528273974&#x3D;&#x3D;     Content-Type: text/plain; charset&#x3D;\&quot;us-ascii\&quot;     MIME-Version: 1.0     Content-Transfer-Encoding: 7bit     Content-ID: \&quot;foo.txt\&quot;     Content-Disposition: attachment; filename&#x3D;\&quot;foo.txt\&quot;      foo      --&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;1438169132528273974&#x3D;&#x3D;     Content-Type: image/png     MIME-Version: 1.0     Content-Transfer-Encoding: base64     Content-ID: \&quot;image.png\&quot;     Content-Disposition: attachment; filename&#x3D;\&quot;image.png\&quot;      iVBORw0KGgoAAAANSUhEUgAAABQAAAAoCAYAAAD+MdrbAAABD0lEQVR4Ae3VMUoDQRTG8ccUaW2m     TKONFxArJYJamCvkCnZTaa+VnQdJSBFl2SMsLFrEWNjZBZs0JgiL/+KrhhVmJRbCLPx4O+/DT2TB     cbblJxf+UWFVVRNsEGAtgvJxnLm2H+A5RQ93uIl+3632PZyl/skjfOn9Gvdwmlcw5aPUwimG+NT5     EnNN036IaZePUuIcK533NVfal7/5yjWeot2z9ta1cAczHEf7I+3J0ws9Cgx0fsOFpmlfwKcWPuBQ     73Oc4FHzBaZ8llq4q1mr5B2mOUCt815qYR8eB1hG2VJ7j35q4RofaH7IG+Xrf/PfJhfmwtfFYoIN     AqxFUD6OMxcvkO+UfKfkOyXfKdsv/AYCHMLVkHAFWgAAAABJRU5ErkJggg&#x3D;&#x3D;     --&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;1438169132528273974&#x3D;&#x3D;--  The request contains multiple parts and is structured as follows.  The first part is the JSON document that describes the snippet&#39;s properties or meta data. It either has to be the first part, or the request&#39;s &#x60;Content-Type&#x60; header must contain the &#x60;start&#x60; parameter to point to it.  The remaining parts are the files of which there can be zero or more. Each file part should contain the &#x60;Content-ID&#x60; MIME header through which the JSON meta data&#39;s &#x60;files&#x60; element addresses it. The value should be the name of the file.  &#x60;Content-Disposition&#x60; is an optional MIME header. The header&#39;s optional &#x60;filename&#x60; parameter can be used to specify the file name that Bitbucket should use when writing the file to disk. When present, &#x60;filename&#x60; takes precedence over the value of &#x60;Content-ID&#x60;.  When the JSON body omits the &#x60;files&#x60; element, the remaining parts are not ignored. Instead, each file is added to the new snippet as if its name was explicitly linked (the use of the &#x60;files&#x60; elements is mandatory for some operations like deleting or renaming files).   multipart/form-data -------------------  The use of JSON for the snippet&#39;s meta data is optional. Meta data can also be supplied as regular form fields in a more conventional &#x60;multipart/form-data&#x60; request:      $ curl -X POST -u credentials https://api.bitbucket.org/2.0/snippets               -F title&#x3D;\&quot;My snippet\&quot;               -F file&#x3D;@foo.txt -F file&#x3D;@image.png      POST /2.0/snippets HTTP/1.1     Content-Length: 951     Content-Type: multipart/form-data; boundary&#x3D;----------------------------63a4b224c59f      ------------------------------63a4b224c59f     Content-Disposition: form-data; name&#x3D;\&quot;file\&quot;; filename&#x3D;\&quot;foo.txt\&quot;     Content-Type: text/plain      foo      ------------------------------63a4b224c59f     Content-Disposition: form-data; name&#x3D;\&quot;file\&quot;; filename&#x3D;\&quot;image.png\&quot;     Content-Type: application/octet-stream      ?PNG      IHDR?1??I.....     ------------------------------63a4b224c59f     Content-Disposition: form-data; name&#x3D;\&quot;title\&quot;      My snippet     ------------------------------63a4b224c59f--  Here the meta data properties are included as flat, top-level form fields. The file attachments use the &#x60;file&#x60; field name. To attach multiple files, simply repeat the field.  The advantage of &#x60;multipart/form-data&#x60; over &#x60;multipart/related&#x60; is that it can be easier to build clients.  Essentially all properties are optional, &#x60;title&#x60; and &#x60;files&#x60; included.   Sharing and Visibility ----------------------  Snippets can be either public (visible to anyone on Bitbucket, as well as anonymous users), or private (visible only to members of the workspace). This is controlled through the snippet&#39;s &#x60;is_private&#x60; element:  * **is_private&#x3D;false** -- everyone, including anonymous users can view   the snippet * **is_private&#x3D;true** -- only workspace members can view the snippet  To create the snippet under a workspace, just append the workspace ID to the URL. See [&#x60;/2.0/snippets/{workspace}&#x60;](/cloud/bitbucket/rest/api-group-snippets/#api-snippets-workspace-post).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnippetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    SnippetsApi apiInstance = new SnippetsApi(defaultClient);
    Snippet snippet = new Snippet(); // Snippet | The new snippet object.
    try {
      Snippet result = apiInstance.snippetsPost(snippet);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnippetsApi#snippetsPost");
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
| **snippet** | [**Snippet**](Snippet.md)| The new snippet object. | |

### Return type

[**Snippet**](Snippet.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The newly created snippet object. |  * Location - The location of the project. This header is only provided when the project key is updated. <br>  |
| **401** | If the request was not authenticated |  -  |

<a id="snippetsWorkspaceEncodedIdCommentsCommentIdDelete"></a>
# **snippetsWorkspaceEncodedIdCommentsCommentIdDelete**
> snippetsWorkspaceEncodedIdCommentsCommentIdDelete(commentId, encodedId, workspace)

Delete a comment on a snippet

Deletes a snippet comment.  Comments can only be removed by the comment author, snippet creator, or workspace admin.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnippetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    SnippetsApi apiInstance = new SnippetsApi(defaultClient);
    Integer commentId = 56; // Integer | The id of the comment.
    String encodedId = "encodedId_example"; // String | The snippet id.
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      apiInstance.snippetsWorkspaceEncodedIdCommentsCommentIdDelete(commentId, encodedId, workspace);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnippetsApi#snippetsWorkspaceEncodedIdCommentsCommentIdDelete");
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
| **commentId** | **Integer**| The id of the comment. | |
| **encodedId** | **String**| The snippet id. | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Indicates the comment was deleted successfully. |  -  |
| **403** | If the authenticated user is not the author of the comment. |  -  |
| **404** | If the comment or the snippet does not exist. |  -  |

<a id="snippetsWorkspaceEncodedIdCommentsCommentIdGet"></a>
# **snippetsWorkspaceEncodedIdCommentsCommentIdGet**
> SnippetComment snippetsWorkspaceEncodedIdCommentsCommentIdGet(commentId, encodedId, workspace)

Get a comment on a snippet

Returns the specific snippet comment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnippetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    SnippetsApi apiInstance = new SnippetsApi(defaultClient);
    Integer commentId = 56; // Integer | The id of the comment.
    String encodedId = "encodedId_example"; // String | The snippet id.
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      SnippetComment result = apiInstance.snippetsWorkspaceEncodedIdCommentsCommentIdGet(commentId, encodedId, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnippetsApi#snippetsWorkspaceEncodedIdCommentsCommentIdGet");
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
| **commentId** | **Integer**| The id of the comment. | |
| **encodedId** | **String**| The snippet id. | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |

### Return type

[**SnippetComment**](SnippetComment.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The specified comment. |  -  |
| **403** | If the authenticated user does not have access to the snippet. |  -  |
| **404** | If the comment or snippet does not exist. |  -  |

<a id="snippetsWorkspaceEncodedIdCommentsCommentIdPut"></a>
# **snippetsWorkspaceEncodedIdCommentsCommentIdPut**
> SnippetComment snippetsWorkspaceEncodedIdCommentsCommentIdPut(commentId, encodedId, workspace, snippetComment)

Update a comment on a snippet

Updates a comment.  The only required field in the body is &#x60;content.raw&#x60;.  Comments can only be updated by their author.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnippetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    SnippetsApi apiInstance = new SnippetsApi(defaultClient);
    Integer commentId = 56; // Integer | The id of the comment.
    String encodedId = "encodedId_example"; // String | The snippet id.
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    SnippetComment snippetComment = new SnippetComment(); // SnippetComment | The contents to update the comment to.
    try {
      SnippetComment result = apiInstance.snippetsWorkspaceEncodedIdCommentsCommentIdPut(commentId, encodedId, workspace, snippetComment);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnippetsApi#snippetsWorkspaceEncodedIdCommentsCommentIdPut");
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
| **commentId** | **Integer**| The id of the comment. | |
| **encodedId** | **String**| The snippet id. | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |
| **snippetComment** | [**SnippetComment**](SnippetComment.md)| The contents to update the comment to. | |

### Return type

[**SnippetComment**](SnippetComment.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated comment object. |  -  |
| **403** | If the authenticated user does not have access to the snippet. |  -  |
| **404** | If the comment or snippet does not exist. |  -  |

<a id="snippetsWorkspaceEncodedIdCommentsGet"></a>
# **snippetsWorkspaceEncodedIdCommentsGet**
> PaginatedSnippetComments snippetsWorkspaceEncodedIdCommentsGet(encodedId, workspace)

List comments on a snippet

Used to retrieve a paginated list of all comments for a specific snippet.  This resource works identical to commit and pull request comments.  The default sorting is oldest to newest and can be overridden with the &#x60;sort&#x60; query parameter.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnippetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    SnippetsApi apiInstance = new SnippetsApi(defaultClient);
    String encodedId = "encodedId_example"; // String | The snippet id.
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      PaginatedSnippetComments result = apiInstance.snippetsWorkspaceEncodedIdCommentsGet(encodedId, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnippetsApi#snippetsWorkspaceEncodedIdCommentsGet");
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
| **encodedId** | **String**| The snippet id. | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |

### Return type

[**PaginatedSnippetComments**](PaginatedSnippetComments.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A paginated list of snippet comments, ordered by creation date. |  -  |
| **403** | If the authenticated user does not have access to the snippet. |  -  |
| **404** | If the snippet does not exist. |  -  |

<a id="snippetsWorkspaceEncodedIdCommentsPost"></a>
# **snippetsWorkspaceEncodedIdCommentsPost**
> SnippetComment snippetsWorkspaceEncodedIdCommentsPost(encodedId, workspace, snippetComment)

Create a comment on a snippet

Creates a new comment.  The only required field in the body is &#x60;content.raw&#x60;.  To create a threaded reply to an existing comment, include &#x60;parent.id&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnippetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    SnippetsApi apiInstance = new SnippetsApi(defaultClient);
    String encodedId = "encodedId_example"; // String | The snippet id.
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    SnippetComment snippetComment = new SnippetComment(); // SnippetComment | The contents of the new comment.
    try {
      SnippetComment result = apiInstance.snippetsWorkspaceEncodedIdCommentsPost(encodedId, workspace, snippetComment);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnippetsApi#snippetsWorkspaceEncodedIdCommentsPost");
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
| **encodedId** | **String**| The snippet id. | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |
| **snippetComment** | [**SnippetComment**](SnippetComment.md)| The contents of the new comment. | |

### Return type

[**SnippetComment**](SnippetComment.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The newly created comment. |  * Location - The location of the project. This header is only provided when the project key is updated. <br>  |
| **403** | If the authenticated user does not have access to the snippet. |  -  |
| **404** | If the snippet does not exist. |  -  |

<a id="snippetsWorkspaceEncodedIdCommitsGet"></a>
# **snippetsWorkspaceEncodedIdCommitsGet**
> PaginatedSnippetCommit snippetsWorkspaceEncodedIdCommitsGet(encodedId, workspace)

List snippet changes

Returns the changes (commits) made on this snippet.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnippetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    SnippetsApi apiInstance = new SnippetsApi(defaultClient);
    String encodedId = "encodedId_example"; // String | The snippet id.
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      PaginatedSnippetCommit result = apiInstance.snippetsWorkspaceEncodedIdCommitsGet(encodedId, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnippetsApi#snippetsWorkspaceEncodedIdCommitsGet");
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
| **encodedId** | **String**| The snippet id. | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |

### Return type

[**PaginatedSnippetCommit**](PaginatedSnippetCommit.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The paginated list of snippet commits. |  -  |
| **403** | If the authenticated user does not have access to the snippet. |  -  |
| **404** | If the snippet does not exist. |  -  |

<a id="snippetsWorkspaceEncodedIdCommitsRevisionGet"></a>
# **snippetsWorkspaceEncodedIdCommitsRevisionGet**
> SnippetCommit snippetsWorkspaceEncodedIdCommitsRevisionGet(encodedId, revision, workspace)

Get a previous snippet change

Returns the changes made on this snippet in this commit.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnippetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    SnippetsApi apiInstance = new SnippetsApi(defaultClient);
    String encodedId = "encodedId_example"; // String | The snippet id.
    String revision = "revision_example"; // String | The commit's SHA1.
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      SnippetCommit result = apiInstance.snippetsWorkspaceEncodedIdCommitsRevisionGet(encodedId, revision, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnippetsApi#snippetsWorkspaceEncodedIdCommitsRevisionGet");
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
| **encodedId** | **String**| The snippet id. | |
| **revision** | **String**| The commit&#39;s SHA1. | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |

### Return type

[**SnippetCommit**](SnippetCommit.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The specified snippet commit. |  -  |
| **403** | If the authenticated user does not have access to the snippet. |  -  |
| **404** | If the commit or the snippet does not exist. |  -  |

<a id="snippetsWorkspaceEncodedIdDelete"></a>
# **snippetsWorkspaceEncodedIdDelete**
> snippetsWorkspaceEncodedIdDelete(encodedId, workspace)

Delete a snippet

Deletes a snippet and returns an empty response.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnippetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    SnippetsApi apiInstance = new SnippetsApi(defaultClient);
    String encodedId = "encodedId_example"; // String | The snippet id.
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      apiInstance.snippetsWorkspaceEncodedIdDelete(encodedId, workspace);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnippetsApi#snippetsWorkspaceEncodedIdDelete");
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
| **encodedId** | **String**| The snippet id. | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | If the snippet was deleted successfully. |  -  |
| **401** | If the snippet is private and the request was not authenticated. |  -  |
| **403** | If authenticated user does not have permission to delete the private snippet. |  -  |
| **404** | If the snippet does not exist. |  -  |

<a id="snippetsWorkspaceEncodedIdFilesPathGet"></a>
# **snippetsWorkspaceEncodedIdFilesPathGet**
> snippetsWorkspaceEncodedIdFilesPathGet(encodedId, path, workspace)

Get a snippet&#39;s raw file at HEAD

Convenience resource for getting to a snippet&#39;s raw files without the need for first having to retrieve the snippet itself and having to pull out the versioned file links.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnippetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    SnippetsApi apiInstance = new SnippetsApi(defaultClient);
    String encodedId = "encodedId_example"; // String | The snippet id.
    String path = "path_example"; // String | Path to the file.
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      apiInstance.snippetsWorkspaceEncodedIdFilesPathGet(encodedId, path, workspace);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnippetsApi#snippetsWorkspaceEncodedIdFilesPathGet");
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
| **encodedId** | **String**| The snippet id. | |
| **path** | **String**| Path to the file. | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **302** | A redirect to the most recent revision of the specified file. |  * Location - The location of the project. This header is only provided when the project key is updated. <br>  |
| **403** | If the authenticated user does not have access to the snippet. |  -  |
| **404** | If the snippet does not exist. |  -  |

<a id="snippetsWorkspaceEncodedIdGet"></a>
# **snippetsWorkspaceEncodedIdGet**
> Snippet snippetsWorkspaceEncodedIdGet(encodedId, workspace)

Get a snippet

Retrieves a single snippet.  Snippets support multiple content types:  * application/json * multipart/related * multipart/form-data   application/json ----------------  The default content type of the response is &#x60;application/json&#x60;. Since JSON is always &#x60;utf-8&#x60;, it cannot reliably contain file contents for files that are not text. Therefore, JSON snippet documents only contain the filename and links to the file contents.  This means that in order to retrieve all parts of a snippet, N+1 requests need to be made (where N is the number of files in the snippet).   multipart/related -----------------  To retrieve an entire snippet in a single response, use the &#x60;Accept: multipart/related&#x60; HTTP request header.      $ curl -H \&quot;Accept: multipart/related\&quot; https://api.bitbucket.org/2.0/snippets/evzijst/1  Response:      HTTP/1.1 200 OK     Content-Length: 2214     Content-Type: multipart/related; start&#x3D;\&quot;snippet\&quot;; boundary&#x3D;\&quot;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;1438169132528273974&#x3D;&#x3D;\&quot;     MIME-Version: 1.0      --&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;1438169132528273974&#x3D;&#x3D;     Content-Type: application/json; charset&#x3D;\&quot;utf-8\&quot;     MIME-Version: 1.0     Content-ID: snippet      {       \&quot;links\&quot;: {         \&quot;self\&quot;: {           \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/snippets/evzijst/kypj\&quot;         },         \&quot;html\&quot;: {           \&quot;href\&quot;: \&quot;https://bitbucket.org/snippets/evzijst/kypj\&quot;         },         \&quot;comments\&quot;: {           \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/snippets/evzijst/kypj/comments\&quot;         },         \&quot;watchers\&quot;: {           \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/snippets/evzijst/kypj/watchers\&quot;         },         \&quot;commits\&quot;: {           \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/snippets/evzijst/kypj/commits\&quot;         }       },       \&quot;id\&quot;: kypj,       \&quot;title\&quot;: \&quot;My snippet\&quot;,       \&quot;created_on\&quot;: \&quot;2014-12-29T22:22:04.790331+00:00\&quot;,       \&quot;updated_on\&quot;: \&quot;2014-12-29T22:22:04.790331+00:00\&quot;,       \&quot;is_private\&quot;: false,       \&quot;files\&quot;: {         \&quot;foo.txt\&quot;: {           \&quot;links\&quot;: {             \&quot;self\&quot;: {               \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/snippets/evzijst/kypj/files/367ab19/foo.txt\&quot;             },             \&quot;html\&quot;: {               \&quot;href\&quot;: \&quot;https://bitbucket.org/snippets/evzijst/kypj#file-foo.txt\&quot;             }           }         },         \&quot;image.png\&quot;: {           \&quot;links\&quot;: {             \&quot;self\&quot;: {               \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/snippets/evzijst/kypj/files/367ab19/image.png\&quot;             },             \&quot;html\&quot;: {               \&quot;href\&quot;: \&quot;https://bitbucket.org/snippets/evzijst/kypj#file-image.png\&quot;             }           }         }       ],       \&quot;owner\&quot;: {         \&quot;username\&quot;: \&quot;evzijst\&quot;,         \&quot;nickname\&quot;: \&quot;evzijst\&quot;,         \&quot;display_name\&quot;: \&quot;Erik van Zijst\&quot;,         \&quot;uuid\&quot;: \&quot;{d301aafa-d676-4ee0-88be-962be7417567}\&quot;,         \&quot;links\&quot;: {           \&quot;self\&quot;: {             \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/users/evzijst\&quot;           },           \&quot;html\&quot;: {             \&quot;href\&quot;: \&quot;https://bitbucket.org/evzijst\&quot;           },           \&quot;avatar\&quot;: {             \&quot;href\&quot;: \&quot;https://bitbucket-staging-assetroot.s3.amazonaws.com/c/photos/2013/Jul/31/erik-avatar-725122544-0_avatar.png\&quot;           }         }       },       \&quot;creator\&quot;: {         \&quot;username\&quot;: \&quot;evzijst\&quot;,         \&quot;nickname\&quot;: \&quot;evzijst\&quot;,         \&quot;display_name\&quot;: \&quot;Erik van Zijst\&quot;,         \&quot;uuid\&quot;: \&quot;{d301aafa-d676-4ee0-88be-962be7417567}\&quot;,         \&quot;links\&quot;: {           \&quot;self\&quot;: {             \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/users/evzijst\&quot;           },           \&quot;html\&quot;: {             \&quot;href\&quot;: \&quot;https://bitbucket.org/evzijst\&quot;           },           \&quot;avatar\&quot;: {             \&quot;href\&quot;: \&quot;https://bitbucket-staging-assetroot.s3.amazonaws.com/c/photos/2013/Jul/31/erik-avatar-725122544-0_avatar.png\&quot;           }         }       }     }      --&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;1438169132528273974&#x3D;&#x3D;     Content-Type: text/plain; charset&#x3D;\&quot;us-ascii\&quot;     MIME-Version: 1.0     Content-Transfer-Encoding: 7bit     Content-ID: \&quot;foo.txt\&quot;     Content-Disposition: attachment; filename&#x3D;\&quot;foo.txt\&quot;      foo      --&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;1438169132528273974&#x3D;&#x3D;     Content-Type: image/png     MIME-Version: 1.0     Content-Transfer-Encoding: base64     Content-ID: \&quot;image.png\&quot;     Content-Disposition: attachment; filename&#x3D;\&quot;image.png\&quot;      iVBORw0KGgoAAAANSUhEUgAAABQAAAAoCAYAAAD+MdrbAAABD0lEQVR4Ae3VMUoDQRTG8ccUaW2m     TKONFxArJYJamCvkCnZTaa+VnQdJSBFl2SMsLFrEWNjZBZs0JgiL/+KrhhVmJRbCLPx4O+/DT2TB     cbblJxf+UWFVVRNsEGAtgvJxnLm2H+A5RQ93uIl+3632PZyl/skjfOn9Gvdwmlcw5aPUwimG+NT5     EnNN036IaZePUuIcK533NVfal7/5yjWeot2z9ta1cAczHEf7I+3J0ws9Cgx0fsOFpmlfwKcWPuBQ     73Oc4FHzBaZ8llq4q1mr5B2mOUCt815qYR8eB1hG2VJ7j35q4RofaH7IG+Xrf/PfJhfmwtfFYoIN     AqxFUD6OMxcvkO+UfKfkOyXfKdsv/AYCHMLVkHAFWgAAAABJRU5ErkJggg&#x3D;&#x3D;     --&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;1438169132528273974&#x3D;&#x3D;--  multipart/form-data -------------------  As with creating new snippets, &#x60;multipart/form-data&#x60; can be used as an alternative to &#x60;multipart/related&#x60;. However, the inherently flat structure of form-data means that only basic, root-level properties can be returned, while nested elements like &#x60;links&#x60; are omitted:      $ curl -H \&quot;Accept: multipart/form-data\&quot; https://api.bitbucket.org/2.0/snippets/evzijst/kypj  Response:      HTTP/1.1 200 OK     Content-Length: 951     Content-Type: multipart/form-data; boundary&#x3D;----------------------------63a4b224c59f      ------------------------------63a4b224c59f     Content-Disposition: form-data; name&#x3D;\&quot;title\&quot;     Content-Type: text/plain; charset&#x3D;\&quot;utf-8\&quot;      My snippet     ------------------------------63a4b224c59f--     Content-Disposition: attachment; name&#x3D;\&quot;file\&quot;; filename&#x3D;\&quot;foo.txt\&quot;     Content-Type: text/plain      foo      ------------------------------63a4b224c59f     Content-Disposition: attachment; name&#x3D;\&quot;file\&quot;; filename&#x3D;\&quot;image.png\&quot;     Content-Transfer-Encoding: base64     Content-Type: application/octet-stream      iVBORw0KGgoAAAANSUhEUgAAABQAAAAoCAYAAAD+MdrbAAABD0lEQVR4Ae3VMUoDQRTG8ccUaW2m     TKONFxArJYJamCvkCnZTaa+VnQdJSBFl2SMsLFrEWNjZBZs0JgiL/+KrhhVmJRbCLPx4O+/DT2TB     cbblJxf+UWFVVRNsEGAtgvJxnLm2H+A5RQ93uIl+3632PZyl/skjfOn9Gvdwmlcw5aPUwimG+NT5     EnNN036IaZePUuIcK533NVfal7/5yjWeot2z9ta1cAczHEf7I+3J0ws9Cgx0fsOFpmlfwKcWPuBQ     73Oc4FHzBaZ8llq4q1mr5B2mOUCt815qYR8eB1hG2VJ7j35q4RofaH7IG+Xrf/PfJhfmwtfFYoIN     AqxFUD6OMxcvkO+UfKfkOyXfKdsv/AYCHMLVkHAFWgAAAABJRU5ErkJggg&#x3D;&#x3D;     ------------------------------5957323a6b76--

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnippetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    SnippetsApi apiInstance = new SnippetsApi(defaultClient);
    String encodedId = "encodedId_example"; // String | The snippet id.
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      Snippet result = apiInstance.snippetsWorkspaceEncodedIdGet(encodedId, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnippetsApi#snippetsWorkspaceEncodedIdGet");
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
| **encodedId** | **String**| The snippet id. | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |

### Return type

[**Snippet**](Snippet.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, multipart/form-data, multipart/related

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The snippet object. |  -  |
| **401** | If the snippet is private and the request was not authenticated. |  -  |
| **403** | If authenticated user does not have access to the private snippet. |  -  |
| **404** | If the snippet does not exist. |  -  |
| **410** | If the snippet marked as spam. |  -  |

<a id="snippetsWorkspaceEncodedIdNodeIdDelete"></a>
# **snippetsWorkspaceEncodedIdNodeIdDelete**
> snippetsWorkspaceEncodedIdNodeIdDelete(encodedId, nodeId, workspace)

Delete a previous revision of a snippet

Deletes the snippet.  Note that this only works for versioned URLs that point to the latest commit of the snippet. Pointing to an older commit results in a 405 status code.  To delete a snippet, regardless of whether or not concurrent changes are being made to it, use &#x60;DELETE /snippets/{encoded_id}&#x60; instead.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnippetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    SnippetsApi apiInstance = new SnippetsApi(defaultClient);
    String encodedId = "encodedId_example"; // String | The snippet id.
    String nodeId = "nodeId_example"; // String | A commit revision (SHA1).
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      apiInstance.snippetsWorkspaceEncodedIdNodeIdDelete(encodedId, nodeId, workspace);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnippetsApi#snippetsWorkspaceEncodedIdNodeIdDelete");
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
| **encodedId** | **String**| The snippet id. | |
| **nodeId** | **String**| A commit revision (SHA1). | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | If the snippet was deleted successfully. |  -  |
| **401** | If the snippet is private and the request was not authenticated. |  -  |
| **403** | If authenticated user does not have permission to delete the private snippet. |  -  |
| **404** | If the snippet does not exist. |  -  |
| **405** | If &#x60;{node_id}&#x60; is not the latest revision. |  -  |

<a id="snippetsWorkspaceEncodedIdNodeIdFilesPathGet"></a>
# **snippetsWorkspaceEncodedIdNodeIdFilesPathGet**
> snippetsWorkspaceEncodedIdNodeIdFilesPathGet(encodedId, nodeId, path, workspace)

Get a snippet&#39;s raw file

Retrieves the raw contents of a specific file in the snippet. The &#x60;Content-Disposition&#x60; header will be \&quot;attachment\&quot; to avoid issues with malevolent executable files.  The file&#39;s mime type is derived from its filename and returned in the &#x60;Content-Type&#x60; header.  Note that for text files, no character encoding is included as part of the content type.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnippetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    SnippetsApi apiInstance = new SnippetsApi(defaultClient);
    String encodedId = "encodedId_example"; // String | The snippet id.
    String nodeId = "nodeId_example"; // String | A commit revision (SHA1).
    String path = "path_example"; // String | Path to the file.
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      apiInstance.snippetsWorkspaceEncodedIdNodeIdFilesPathGet(encodedId, nodeId, path, workspace);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnippetsApi#snippetsWorkspaceEncodedIdNodeIdFilesPathGet");
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
| **encodedId** | **String**| The snippet id. | |
| **nodeId** | **String**| A commit revision (SHA1). | |
| **path** | **String**| Path to the file. | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the contents of the specified file. |  * Content-Disposition - attachment <br>  * Content-Type - The mime type as derived from the filename <br>  |
| **403** | If the authenticated user does not have access to the snippet. |  -  |
| **404** | If the file or snippet does not exist. |  -  |

<a id="snippetsWorkspaceEncodedIdNodeIdGet"></a>
# **snippetsWorkspaceEncodedIdNodeIdGet**
> Snippet snippetsWorkspaceEncodedIdNodeIdGet(encodedId, nodeId, workspace)

Get a previous revision of a snippet

Identical to &#x60;GET /snippets/encoded_id&#x60;, except that this endpoint can be used to retrieve the contents of the snippet as it was at an older revision, while &#x60;/snippets/encoded_id&#x60; always returns the snippet&#39;s current revision.  Note that only the snippet&#39;s file contents are versioned, not its meta data properties like the title.  Other than that, the two endpoints are identical in behavior.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnippetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    SnippetsApi apiInstance = new SnippetsApi(defaultClient);
    String encodedId = "encodedId_example"; // String | The snippet id.
    String nodeId = "nodeId_example"; // String | A commit revision (SHA1).
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      Snippet result = apiInstance.snippetsWorkspaceEncodedIdNodeIdGet(encodedId, nodeId, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnippetsApi#snippetsWorkspaceEncodedIdNodeIdGet");
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
| **encodedId** | **String**| The snippet id. | |
| **nodeId** | **String**| A commit revision (SHA1). | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |

### Return type

[**Snippet**](Snippet.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, multipart/form-data, multipart/related

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The snippet object. |  -  |
| **401** | If the snippet is private and the request was not authenticated. |  -  |
| **403** | If authenticated user does not have access to the private snippet. |  -  |
| **404** | If the snippet, or the revision does not exist. |  -  |

<a id="snippetsWorkspaceEncodedIdNodeIdPut"></a>
# **snippetsWorkspaceEncodedIdNodeIdPut**
> Snippet snippetsWorkspaceEncodedIdNodeIdPut(encodedId, nodeId, workspace)

Update a previous revision of a snippet

Identical to &#x60;UPDATE /snippets/encoded_id&#x60;, except that this endpoint takes an explicit commit revision. Only the snippet&#39;s \&quot;HEAD\&quot;/\&quot;tip\&quot; (most recent) version can be updated and requests on all other, older revisions fail by returning a 405 status.  Usage of this endpoint over the unrestricted &#x60;/snippets/encoded_id&#x60; could be desired if the caller wants to be sure no concurrent modifications have taken place between the moment of the UPDATE request and the original GET.  This can be considered a so-called \&quot;Compare And Swap\&quot;, or CAS operation.  Other than that, the two endpoints are identical in behavior.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnippetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    SnippetsApi apiInstance = new SnippetsApi(defaultClient);
    String encodedId = "encodedId_example"; // String | The snippet id.
    String nodeId = "nodeId_example"; // String | A commit revision (SHA1).
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      Snippet result = apiInstance.snippetsWorkspaceEncodedIdNodeIdPut(encodedId, nodeId, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnippetsApi#snippetsWorkspaceEncodedIdNodeIdPut");
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
| **encodedId** | **String**| The snippet id. | |
| **nodeId** | **String**| A commit revision (SHA1). | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |

### Return type

[**Snippet**](Snippet.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, multipart/form-data, multipart/related

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated snippet object. |  -  |
| **401** | If the snippet is private and the request was not authenticated. |  -  |
| **403** | If authenticated user does not have permission to update the private snippet. |  -  |
| **404** | If the snippet or the revision does not exist. |  -  |
| **405** | If &#x60;{node_id}&#x60; is not the latest revision. |  -  |

<a id="snippetsWorkspaceEncodedIdPut"></a>
# **snippetsWorkspaceEncodedIdPut**
> Snippet snippetsWorkspaceEncodedIdPut(encodedId, workspace)

Update a snippet

Used to update a snippet. Use this to add and delete files and to change a snippet&#39;s title.  To update a snippet, one can either PUT a full snapshot, or only the parts that need to be changed.  The contract for PUT on this API is that properties missing from the request remain untouched so that snippets can be efficiently manipulated with differential payloads.  To delete a property (e.g. the title, or a file), include its name in the request, but omit its value (use &#x60;null&#x60;).  As in Git, explicit renaming of files is not supported. Instead, to rename a file, delete it and add it again under another name. This can be done atomically in a single request. Rename detection is left to the SCM.  PUT supports three different content types for both request and response bodies:  * &#x60;application/json&#x60; * &#x60;multipart/related&#x60; * &#x60;multipart/form-data&#x60;  The content type used for the request body can be different than that used for the response. Content types are specified using standard HTTP headers.  Use the &#x60;Content-Type&#x60; and &#x60;Accept&#x60; headers to select the desired request and response format.   application/json ----------------  As with creation and retrieval, the content type determines what properties can be manipulated. &#x60;application/json&#x60; does not support file contents and is therefore limited to a snippet&#39;s meta data.  To update the title, without changing any of its files:      $ curl -X POST -H \&quot;Content-Type: application/json\&quot; https://api.bitbucket.org/2.0/snippets/evzijst/kypj             -d &#39;{\&quot;title\&quot;: \&quot;Updated title\&quot;}&#39;   To delete the title:      $ curl -X POST -H \&quot;Content-Type: application/json\&quot; https://api.bitbucket.org/2.0/snippets/evzijst/kypj             -d &#39;{\&quot;title\&quot;: null}&#39;  Not all parts of a snippet can be manipulated. The owner and creator for instance are immutable.   multipart/related -----------------  &#x60;multipart/related&#x60; can be used to manipulate all of a snippet&#39;s properties. The body is identical to a POST. properties omitted from the request are left unchanged. Since the &#x60;start&#x60; part contains JSON, the mechanism for manipulating the snippet&#39;s meta data is identical to &#x60;application/json&#x60; requests.  To update one of a snippet&#39;s file contents, while also changing its title:      PUT /2.0/snippets/evzijst/kypj HTTP/1.1     Content-Length: 288     Content-Type: multipart/related; start&#x3D;\&quot;snippet\&quot;; boundary&#x3D;\&quot;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;1438169132528273974&#x3D;&#x3D;\&quot;     MIME-Version: 1.0      --&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;1438169132528273974&#x3D;&#x3D;     Content-Type: application/json; charset&#x3D;\&quot;utf-8\&quot;     MIME-Version: 1.0     Content-ID: snippet      {       \&quot;title\&quot;: \&quot;My updated snippet\&quot;,       \&quot;files\&quot;: {           \&quot;foo.txt\&quot;: {}         }     }      --&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;1438169132528273974&#x3D;&#x3D;     Content-Type: text/plain; charset&#x3D;\&quot;us-ascii\&quot;     MIME-Version: 1.0     Content-Transfer-Encoding: 7bit     Content-ID: \&quot;foo.txt\&quot;     Content-Disposition: attachment; filename&#x3D;\&quot;foo.txt\&quot;      Updated file contents.      --&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;1438169132528273974&#x3D;&#x3D;--  Here only the parts that are changed are included in the body. The other files remain untouched.  Note the use of the &#x60;files&#x60; list in the JSON part. This list contains the files that are being manipulated. This list should have corresponding multiparts in the request that contain the new contents of these files.  If a filename in the &#x60;files&#x60; list does not have a corresponding part, it will be deleted from the snippet, as shown below:      PUT /2.0/snippets/evzijst/kypj HTTP/1.1     Content-Length: 188     Content-Type: multipart/related; start&#x3D;\&quot;snippet\&quot;; boundary&#x3D;\&quot;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;1438169132528273974&#x3D;&#x3D;\&quot;     MIME-Version: 1.0      --&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;1438169132528273974&#x3D;&#x3D;     Content-Type: application/json; charset&#x3D;\&quot;utf-8\&quot;     MIME-Version: 1.0     Content-ID: snippet      {       \&quot;files\&quot;: {         \&quot;image.png\&quot;: {}       }     }      --&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;1438169132528273974&#x3D;&#x3D;--  To simulate a rename, delete a file and add the same file under another name:      PUT /2.0/snippets/evzijst/kypj HTTP/1.1     Content-Length: 212     Content-Type: multipart/related; start&#x3D;\&quot;snippet\&quot;; boundary&#x3D;\&quot;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;1438169132528273974&#x3D;&#x3D;\&quot;     MIME-Version: 1.0      --&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;1438169132528273974&#x3D;&#x3D;     Content-Type: application/json; charset&#x3D;\&quot;utf-8\&quot;     MIME-Version: 1.0     Content-ID: snippet      {         \&quot;files\&quot;: {           \&quot;foo.txt\&quot;: {},           \&quot;bar.txt\&quot;: {}         }     }      --&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;1438169132528273974&#x3D;&#x3D;     Content-Type: text/plain; charset&#x3D;\&quot;us-ascii\&quot;     MIME-Version: 1.0     Content-Transfer-Encoding: 7bit     Content-ID: \&quot;bar.txt\&quot;     Content-Disposition: attachment; filename&#x3D;\&quot;bar.txt\&quot;      foo      --&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;1438169132528273974&#x3D;&#x3D;--   multipart/form-data -----------------  Again, one can also use &#x60;multipart/form-data&#x60; to manipulate file contents and meta data atomically.      $ curl -X PUT http://localhost:12345/2.0/snippets/evzijst/kypj             -F title&#x3D;\&quot;My updated snippet\&quot; -F file&#x3D;@foo.txt      PUT /2.0/snippets/evzijst/kypj HTTP/1.1     Content-Length: 351     Content-Type: multipart/form-data; boundary&#x3D;----------------------------63a4b224c59f      ------------------------------63a4b224c59f     Content-Disposition: form-data; name&#x3D;\&quot;file\&quot;; filename&#x3D;\&quot;foo.txt\&quot;     Content-Type: text/plain      foo      ------------------------------63a4b224c59f     Content-Disposition: form-data; name&#x3D;\&quot;title\&quot;      My updated snippet     ------------------------------63a4b224c59f  To delete a file, omit its contents while including its name in the &#x60;files&#x60; field:      $ curl -X PUT https://api.bitbucket.org/2.0/snippets/evzijst/kypj -F files&#x3D;image.png      PUT /2.0/snippets/evzijst/kypj HTTP/1.1     Content-Length: 149     Content-Type: multipart/form-data; boundary&#x3D;----------------------------ef8871065a86      ------------------------------ef8871065a86     Content-Disposition: form-data; name&#x3D;\&quot;files\&quot;      image.png     ------------------------------ef8871065a86--  The explicit use of the &#x60;files&#x60; element in &#x60;multipart/related&#x60; and &#x60;multipart/form-data&#x60; is only required when deleting files. The default mode of operation is for file parts to be processed, regardless of whether or not they are listed in &#x60;files&#x60;, as a convenience to the client.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnippetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    SnippetsApi apiInstance = new SnippetsApi(defaultClient);
    String encodedId = "encodedId_example"; // String | The snippet id.
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      Snippet result = apiInstance.snippetsWorkspaceEncodedIdPut(encodedId, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnippetsApi#snippetsWorkspaceEncodedIdPut");
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
| **encodedId** | **String**| The snippet id. | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |

### Return type

[**Snippet**](Snippet.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, multipart/form-data, multipart/related

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated snippet object. |  -  |
| **401** | If the snippet is private and the request was not authenticated. |  -  |
| **403** | If authenticated user does not have permission to update the private snippet. |  -  |
| **404** | If the snippet does not exist. |  -  |

<a id="snippetsWorkspaceEncodedIdRevisionDiffGet"></a>
# **snippetsWorkspaceEncodedIdRevisionDiffGet**
> snippetsWorkspaceEncodedIdRevisionDiffGet(encodedId, revision, workspace, path)

Get snippet changes between versions

Returns the diff of the specified commit against its first parent.  Note that this resource is different in functionality from the &#x60;patch&#x60; resource.  The differences between a diff and a patch are:  * patches have a commit header with the username, message, etc * diffs support the optional &#x60;path&#x3D;foo/bar.py&#x60; query param to filter the   diff to just that one file diff (not supported for patches) * for a merge, the diff will show the diff between the merge commit and   its first parent (identical to how PRs work), while patch returns a   response containing separate patches for each commit on the second   parent&#39;s ancestry, up to the oldest common ancestor (identical to   its reachability).  Note that the character encoding of the contents of the diff is unspecified as Git does not track this, making it hard for Bitbucket to reliably determine this.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnippetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    SnippetsApi apiInstance = new SnippetsApi(defaultClient);
    String encodedId = "encodedId_example"; // String | The snippet id.
    String revision = "revision_example"; // String | A revspec expression. This can simply be a commit SHA1, a ref name, or a compare expression like `staging..production`.
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    String path = "path_example"; // String | When used, only one the diff of the specified file will be returned.
    try {
      apiInstance.snippetsWorkspaceEncodedIdRevisionDiffGet(encodedId, revision, workspace, path);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnippetsApi#snippetsWorkspaceEncodedIdRevisionDiffGet");
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
| **encodedId** | **String**| The snippet id. | |
| **revision** | **String**| A revspec expression. This can simply be a commit SHA1, a ref name, or a compare expression like &#x60;staging..production&#x60;. | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |
| **path** | **String**| When used, only one the diff of the specified file will be returned. | [optional] |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The raw diff contents. |  -  |
| **403** | If the authenticated user does not have access to the snippet. |  -  |
| **404** | If the snippet does not exist. |  -  |

<a id="snippetsWorkspaceEncodedIdRevisionPatchGet"></a>
# **snippetsWorkspaceEncodedIdRevisionPatchGet**
> snippetsWorkspaceEncodedIdRevisionPatchGet(encodedId, revision, workspace)

Get snippet patch between versions

Returns the patch of the specified commit against its first parent.  Note that this resource is different in functionality from the &#x60;diff&#x60; resource.  The differences between a diff and a patch are:  * patches have a commit header with the username, message, etc * diffs support the optional &#x60;path&#x3D;foo/bar.py&#x60; query param to filter the   diff to just that one file diff (not supported for patches) * for a merge, the diff will show the diff between the merge commit and   its first parent (identical to how PRs work), while patch returns a   response containing separate patches for each commit on the second   parent&#39;s ancestry, up to the oldest common ancestor (identical to   its reachability).  Note that the character encoding of the contents of the patch is unspecified as Git does not track this, making it hard for Bitbucket to reliably determine this.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnippetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    SnippetsApi apiInstance = new SnippetsApi(defaultClient);
    String encodedId = "encodedId_example"; // String | The snippet id.
    String revision = "revision_example"; // String | A revspec expression. This can simply be a commit SHA1, a ref name, or a compare expression like `staging..production`.
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      apiInstance.snippetsWorkspaceEncodedIdRevisionPatchGet(encodedId, revision, workspace);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnippetsApi#snippetsWorkspaceEncodedIdRevisionPatchGet");
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
| **encodedId** | **String**| The snippet id. | |
| **revision** | **String**| A revspec expression. This can simply be a commit SHA1, a ref name, or a compare expression like &#x60;staging..production&#x60;. | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The raw patch contents. |  -  |
| **403** | If the authenticated user does not have access to the snippet. |  -  |
| **404** | If the snippet does not exist. |  -  |

<a id="snippetsWorkspaceEncodedIdWatchDelete"></a>
# **snippetsWorkspaceEncodedIdWatchDelete**
> snippetsWorkspaceEncodedIdWatchDelete(encodedId, workspace)

Stop watching a snippet

Used to stop watching a specific snippet. Returns 204 (No Content) to indicate success.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnippetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    SnippetsApi apiInstance = new SnippetsApi(defaultClient);
    String encodedId = "encodedId_example"; // String | The snippet id.
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      apiInstance.snippetsWorkspaceEncodedIdWatchDelete(encodedId, workspace);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnippetsApi#snippetsWorkspaceEncodedIdWatchDelete");
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
| **encodedId** | **String**| The snippet id. | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Indicates the user stopped watching the snippet successfully. |  -  |
| **401** | If the request was not authenticated. |  -  |
| **404** | If the snippet does not exist. |  -  |

<a id="snippetsWorkspaceEncodedIdWatchGet"></a>
# **snippetsWorkspaceEncodedIdWatchGet**
> snippetsWorkspaceEncodedIdWatchGet(encodedId, workspace)

Check if the current user is watching a snippet

Used to check if the current user is watching a specific snippet.  Returns 204 (No Content) if the user is watching the snippet and 404 if not.  Hitting this endpoint anonymously always returns a 404.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnippetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    SnippetsApi apiInstance = new SnippetsApi(defaultClient);
    String encodedId = "encodedId_example"; // String | The snippet id.
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      apiInstance.snippetsWorkspaceEncodedIdWatchGet(encodedId, workspace);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnippetsApi#snippetsWorkspaceEncodedIdWatchGet");
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
| **encodedId** | **String**| The snippet id. | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | If the authenticated user is watching the snippet. |  -  |
| **404** | If the snippet does not exist, or if the authenticated user is not watching the snippet. |  -  |

<a id="snippetsWorkspaceEncodedIdWatchPut"></a>
# **snippetsWorkspaceEncodedIdWatchPut**
> snippetsWorkspaceEncodedIdWatchPut(encodedId, workspace)

Watch a snippet

Used to start watching a specific snippet. Returns 204 (No Content).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnippetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    SnippetsApi apiInstance = new SnippetsApi(defaultClient);
    String encodedId = "encodedId_example"; // String | The snippet id.
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      apiInstance.snippetsWorkspaceEncodedIdWatchPut(encodedId, workspace);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnippetsApi#snippetsWorkspaceEncodedIdWatchPut");
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
| **encodedId** | **String**| The snippet id. | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Indicates the authenticated user is now watching the snippet. |  -  |
| **401** | If the request was not authenticated. |  -  |
| **404** | If the snippet does not exist. |  -  |

<a id="snippetsWorkspaceEncodedIdWatchersGet"></a>
# **snippetsWorkspaceEncodedIdWatchersGet**
> PaginatedAccounts snippetsWorkspaceEncodedIdWatchersGet(encodedId, workspace)

List users watching a snippet

Returns a paginated list of all users watching a specific snippet.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnippetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    SnippetsApi apiInstance = new SnippetsApi(defaultClient);
    String encodedId = "encodedId_example"; // String | The snippet id.
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      PaginatedAccounts result = apiInstance.snippetsWorkspaceEncodedIdWatchersGet(encodedId, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnippetsApi#snippetsWorkspaceEncodedIdWatchersGet");
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
| **encodedId** | **String**| The snippet id. | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |

### Return type

[**PaginatedAccounts**](PaginatedAccounts.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The paginated list of users watching this snippet |  -  |
| **404** | If the snippet does not exist. |  -  |

<a id="snippetsWorkspaceGet"></a>
# **snippetsWorkspaceGet**
> PaginatedSnippets snippetsWorkspaceGet(workspace, role)

List snippets in a workspace

Identical to [&#x60;/snippets&#x60;](/cloud/bitbucket/rest/api-group-snippets/#api-snippets-get), except that the result is further filtered by the snippet owner and only those that are owned by &#x60;{workspace}&#x60; are returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnippetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    SnippetsApi apiInstance = new SnippetsApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    String role = "owner"; // String | Filter down the result based on the authenticated user's role (`owner`, `contributor`, or `member`).
    try {
      PaginatedSnippets result = apiInstance.snippetsWorkspaceGet(workspace, role);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnippetsApi#snippetsWorkspaceGet");
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
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |
| **role** | **String**| Filter down the result based on the authenticated user&#39;s role (&#x60;owner&#x60;, &#x60;contributor&#x60;, or &#x60;member&#x60;). | [optional] [enum: owner, contributor, member] |

### Return type

[**PaginatedSnippets**](PaginatedSnippets.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A paginated list of snippets. |  -  |
| **404** | If the user does not exist. |  -  |

<a id="snippetsWorkspacePost"></a>
# **snippetsWorkspacePost**
> Snippet snippetsWorkspacePost(workspace, snippet)

Create a snippet for a workspace

Identical to [&#x60;/snippets&#x60;](/cloud/bitbucket/rest/api-group-snippets/#api-snippets-post), except that the new snippet will be created under the workspace specified in the path parameter &#x60;{workspace}&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnippetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    SnippetsApi apiInstance = new SnippetsApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    Snippet snippet = new Snippet(); // Snippet | The new snippet object.
    try {
      Snippet result = apiInstance.snippetsWorkspacePost(workspace, snippet);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnippetsApi#snippetsWorkspacePost");
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
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |
| **snippet** | [**Snippet**](Snippet.md)| The new snippet object. | |

### Return type

[**Snippet**](Snippet.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The newly created snippet object. |  * Location - The location of the project. This header is only provided when the project key is updated. <br>  |
| **401** | If the request was not authenticated |  -  |
| **403** | If the authenticated user does not have permission to create snippets in the specified workspace. |  -  |

