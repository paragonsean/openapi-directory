# SourceApi

All URIs are relative to *https://api.bitbucket.org/2.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**repositoriesWorkspaceRepoSlugFilehistoryCommitPathGet**](SourceApi.md#repositoriesWorkspaceRepoSlugFilehistoryCommitPathGet) | **GET** /repositories/{workspace}/{repo_slug}/filehistory/{commit}/{path} | List commits that modified a file |
| [**repositoriesWorkspaceRepoSlugSrcCommitPathGet**](SourceApi.md#repositoriesWorkspaceRepoSlugSrcCommitPathGet) | **GET** /repositories/{workspace}/{repo_slug}/src/{commit}/{path} | Get file or directory contents |
| [**repositoriesWorkspaceRepoSlugSrcGet**](SourceApi.md#repositoriesWorkspaceRepoSlugSrcGet) | **GET** /repositories/{workspace}/{repo_slug}/src | Get the root directory of the main branch |
| [**repositoriesWorkspaceRepoSlugSrcPost**](SourceApi.md#repositoriesWorkspaceRepoSlugSrcPost) | **POST** /repositories/{workspace}/{repo_slug}/src | Create a commit by uploading a file |


<a id="repositoriesWorkspaceRepoSlugFilehistoryCommitPathGet"></a>
# **repositoriesWorkspaceRepoSlugFilehistoryCommitPathGet**
> PaginatedFiles repositoriesWorkspaceRepoSlugFilehistoryCommitPathGet(commit, path, repoSlug, workspace, renames, q, sort)

List commits that modified a file

Returns a paginated list of commits that modified the specified file.  Commits are returned in reverse chronological order. This is roughly equivalent to the following commands:      $ git log --follow --date-order &lt;sha&gt; &lt;path&gt;  By default, Bitbucket will follow renames and the path name in the returned entries reflects that. This can be turned off using the &#x60;?renames&#x3D;false&#x60; query parameter.  Results are returned in descending chronological order by default, and like most endpoints you can [filter and sort](/cloud/bitbucket/rest/intro/#filtering) the response to only provide exactly the data you want.  For example, if you wanted to find commits made before 2011-05-18 against a file named &#x60;README.rst&#x60;, but you only wanted the path and date, your query would look like this:  &#x60;&#x60;&#x60; $ curl &#39;https://api.bitbucket.org/2.0/repositories/evzijst/dogslow/filehistory/master/README.rst&#39;\\   &#39;?fields&#x3D;values.next,values.path,values.commit.date&amp;q&#x3D;commit.date&lt;&#x3D;2011-05-18&#39; {   \&quot;values\&quot;: [     {       \&quot;commit\&quot;: {         \&quot;date\&quot;: \&quot;2011-05-17T07:32:09+00:00\&quot;       },       \&quot;path\&quot;: \&quot;README.rst\&quot;     },     {       \&quot;commit\&quot;: {         \&quot;date\&quot;: \&quot;2011-05-16T06:33:28+00:00\&quot;       },       \&quot;path\&quot;: \&quot;README.txt\&quot;     },     {       \&quot;commit\&quot;: {         \&quot;date\&quot;: \&quot;2011-05-16T06:15:39+00:00\&quot;       },       \&quot;path\&quot;: \&quot;README.txt\&quot;     }   ] } &#x60;&#x60;&#x60;  In the response you can see that the file was renamed to &#x60;README.rst&#x60; by the commit made on 2011-05-16, and was previously named &#x60;README.txt&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SourceApi;

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

    SourceApi apiInstance = new SourceApi(defaultClient);
    String commit = "commit_example"; // String | The commit's SHA1.
    String path = "path_example"; // String | Path to the file.
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    String renames = "renames_example"; // String |  When `true`, Bitbucket will follow the history of the file across renames (this is the default behavior). This can be turned off by specifying `false`.
    String q = "q_example"; // String |  Query string to narrow down the response as per [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering).
    String sort = "sort_example"; // String |  Name of a response property sort the result by as per [filtering and sorting](/cloud/bitbucket/rest/intro/#sorting-query-results). 
    try {
      PaginatedFiles result = apiInstance.repositoriesWorkspaceRepoSlugFilehistoryCommitPathGet(commit, path, repoSlug, workspace, renames, q, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SourceApi#repositoriesWorkspaceRepoSlugFilehistoryCommitPathGet");
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
| **commit** | **String**| The commit&#39;s SHA1. | |
| **path** | **String**| Path to the file. | |
| **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |
| **renames** | **String**|  When &#x60;true&#x60;, Bitbucket will follow the history of the file across renames (this is the default behavior). This can be turned off by specifying &#x60;false&#x60;. | [optional] |
| **q** | **String**|  Query string to narrow down the response as per [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering). | [optional] |
| **sort** | **String**|  Name of a response property sort the result by as per [filtering and sorting](/cloud/bitbucket/rest/intro/#sorting-query-results).  | [optional] |

### Return type

[**PaginatedFiles**](PaginatedFiles.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A paginated list of commits that modified the specified file |  -  |
| **404** | If the repository does not exist. |  -  |

<a id="repositoriesWorkspaceRepoSlugSrcCommitPathGet"></a>
# **repositoriesWorkspaceRepoSlugSrcCommitPathGet**
> PaginatedTreeentries repositoriesWorkspaceRepoSlugSrcCommitPathGet(commit, path, repoSlug, workspace, format, q, sort, maxDepth)

Get file or directory contents

This endpoints is used to retrieve the contents of a single file, or the contents of a directory at a specified revision.  #### Raw file contents  When &#x60;path&#x60; points to a file, this endpoint returns the raw contents. The response&#39;s Content-Type is derived from the filename extension (not from the contents). The file contents are not processed and no character encoding/recoding is performed and as a result no character encoding is included as part of the Content-Type.  The &#x60;Content-Disposition&#x60; header will be \&quot;attachment\&quot; to prevent browsers from running executable files.  If the file is managed by LFS, then a 301 redirect pointing to Atlassian&#39;s media services platform is returned.  The response includes an ETag that is based on the contents of the file and its attributes. This means that an empty &#x60;__init__.py&#x60; always returns the same ETag, regardless on the directory it lives in, or the commit it is on.  #### File meta data  When the request for a file path includes the query parameter &#x60;?format&#x3D;meta&#x60;, instead of returning the file&#39;s raw contents, Bitbucket instead returns the JSON object describing the file&#39;s properties:  &#x60;&#x60;&#x60;javascript $ curl https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef/tests/__init__.py?format&#x3D;meta {   \&quot;links\&quot;: {     \&quot;self\&quot;: {       \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef5d3df01aed629f650959d6706d54cd335/tests/__init__.py\&quot;     },     \&quot;meta\&quot;: {       \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef5d3df01aed629f650959d6706d54cd335/tests/__init__.py?format&#x3D;meta\&quot;     }   },   \&quot;path\&quot;: \&quot;tests/__init__.py\&quot;,   \&quot;commit\&quot;: {     \&quot;type\&quot;: \&quot;commit\&quot;,     \&quot;hash\&quot;: \&quot;eefd5ef5d3df01aed629f650959d6706d54cd335\&quot;,     \&quot;links\&quot;: {       \&quot;self\&quot;: {         \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/atlassian/bbql/commit/eefd5ef5d3df01aed629f650959d6706d54cd335\&quot;       },       \&quot;html\&quot;: {         \&quot;href\&quot;: \&quot;https://bitbucket.org/atlassian/bbql/commits/eefd5ef5d3df01aed629f650959d6706d54cd335\&quot;       }     }   },   \&quot;attributes\&quot;: [],   \&quot;type\&quot;: \&quot;commit_file\&quot;,   \&quot;size\&quot;: 0 } &#x60;&#x60;&#x60;  File objects contain an &#x60;attributes&#x60; element that contains a list of possible modifiers. Currently defined values are:  * &#x60;link&#x60; -- indicates that the entry is a symbolic link. The contents     of the file represent the path the link points to. * &#x60;executable&#x60; -- indicates that the file has the executable bit set. * &#x60;subrepository&#x60; -- indicates that the entry points to a submodule or     subrepo. The contents of the file is the SHA1 of the repository     pointed to. * &#x60;binary&#x60; -- indicates whether Bitbucket thinks the file is binary.  This endpoint can provide an alternative to how a HEAD request can be used to check for the existence of a file, or a file&#39;s size without incurring the overhead of receiving its full contents.   #### Directory listings  When &#x60;path&#x60; points to a directory instead of a file, the response is a paginated list of directory and file objects in the same order as the underlying SCM system would return them.  For example:  &#x60;&#x60;&#x60;javascript $ curl https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef/tests {   \&quot;pagelen\&quot;: 10,   \&quot;values\&quot;: [     {       \&quot;path\&quot;: \&quot;tests/test_project\&quot;,       \&quot;type\&quot;: \&quot;commit_directory\&quot;,       \&quot;links\&quot;: {         \&quot;self\&quot;: {           \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef5d3df01aed629f650959d6706d54cd335/tests/test_project/\&quot;         },         \&quot;meta\&quot;: {           \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef5d3df01aed629f650959d6706d54cd335/tests/test_project/?format&#x3D;meta\&quot;         }       },       \&quot;commit\&quot;: {         \&quot;type\&quot;: \&quot;commit\&quot;,         \&quot;hash\&quot;: \&quot;eefd5ef5d3df01aed629f650959d6706d54cd335\&quot;,         \&quot;links\&quot;: {           \&quot;self\&quot;: {             \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/atlassian/bbql/commit/eefd5ef5d3df01aed629f650959d6706d54cd335\&quot;           },           \&quot;html\&quot;: {             \&quot;href\&quot;: \&quot;https://bitbucket.org/atlassian/bbql/commits/eefd5ef5d3df01aed629f650959d6706d54cd335\&quot;           }         }       }     },     {       \&quot;links\&quot;: {         \&quot;self\&quot;: {           \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef5d3df01aed629f650959d6706d54cd335/tests/__init__.py\&quot;         },         \&quot;meta\&quot;: {           \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef5d3df01aed629f650959d6706d54cd335/tests/__init__.py?format&#x3D;meta\&quot;         }       },       \&quot;path\&quot;: \&quot;tests/__init__.py\&quot;,       \&quot;commit\&quot;: {         \&quot;type\&quot;: \&quot;commit\&quot;,         \&quot;hash\&quot;: \&quot;eefd5ef5d3df01aed629f650959d6706d54cd335\&quot;,         \&quot;links\&quot;: {           \&quot;self\&quot;: {             \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/atlassian/bbql/commit/eefd5ef5d3df01aed629f650959d6706d54cd335\&quot;           },           \&quot;html\&quot;: {             \&quot;href\&quot;: \&quot;https://bitbucket.org/atlassian/bbql/commits/eefd5ef5d3df01aed629f650959d6706d54cd335\&quot;           }         }       },       \&quot;attributes\&quot;: [],       \&quot;type\&quot;: \&quot;commit_file\&quot;,       \&quot;size\&quot;: 0     }   ],   \&quot;page\&quot;: 1,   \&quot;size\&quot;: 2 } &#x60;&#x60;&#x60;  When listing the contents of the repo&#39;s root directory, the use of a trailing slash at the end of the URL is required.  The response by default is not recursive, meaning that only the direct contents of a path are returned. The response does not recurse down into subdirectories. In order to \&quot;walk\&quot; the entire directory tree, the client can either parse each response and follow the &#x60;self&#x60; links of each &#x60;commit_directory&#x60; object, or can specify a &#x60;max_depth&#x60; to recurse to.  The max_depth parameter will do a breadth-first search to return the contents of the subdirectories up to the depth specified. Breadth-first search was chosen as it leads to the least amount of file system operations for git. If the &#x60;max_depth&#x60; parameter is specified to be too large, the call will time out and return a 555.  Each returned object is either a &#x60;commit_file&#x60;, or a &#x60;commit_directory&#x60;, both of which contain a &#x60;path&#x60; element. This path is the absolute path from the root of the repository. Each object also contains a &#x60;commit&#x60; object which embeds the commit the file is on. Note that this is merely the commit that was used in the URL. It is *not* the commit that last modified the file.  Directory objects have 2 representations. Their &#x60;self&#x60; link returns the paginated contents of the directory. The &#x60;meta&#x60; link on the other hand returns the actual &#x60;directory&#x60; object itself, e.g.:  &#x60;&#x60;&#x60;javascript {   \&quot;path\&quot;: \&quot;tests/test_project\&quot;,   \&quot;type\&quot;: \&quot;commit_directory\&quot;,   \&quot;links\&quot;: {     \&quot;self\&quot;: {       \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef5d3df01aed629f650959d6706d54cd335/tests/test_project/\&quot;     },     \&quot;meta\&quot;: {       \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef5d3df01aed629f650959d6706d54cd335/tests/test_project/?format&#x3D;meta\&quot;     }   },   \&quot;commit\&quot;: { ... } } &#x60;&#x60;&#x60;  #### Querying, filtering and sorting  Like most API endpoints, this API supports the Bitbucket querying/filtering syntax and so you could filter a directory listing to only include entries that match certain criteria. For instance, to list all binary files over 1kb use the expression:  &#x60;size &gt; 1024 and attributes &#x3D; \&quot;binary\&quot;&#x60;  which after urlencoding yields the query string:  &#x60;?q&#x3D;size%3E1024+and+attributes%3D%22binary%22&#x60;  To change the ordering of the response, use the &#x60;?sort&#x60; parameter:  &#x60;.../src/eefd5ef/?sort&#x3D;-size&#x60;  See [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering) for more details.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SourceApi;

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

    SourceApi apiInstance = new SourceApi(defaultClient);
    String commit = "commit_example"; // String | The commit's SHA1.
    String path = "path_example"; // String | Path to the file.
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    String format = "meta"; // String | If 'meta' is provided, returns the (json) meta data for the contents of the file.  If 'rendered' is provided, returns the contents of a non-binary file in HTML-formatted rendered markup. Since Git does not generally track what text encoding scheme is used, this endpoint attempts to detect the most appropriate character encoding. While usually correct, determining the character encoding can be ambiguous which in exceptional cases can lead to misinterpretation of the characters. As such, the raw element in the response object should not be treated as equivalent to the file's actual contents.
    String q = "q_example"; // String | Optional filter expression as per [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering).
    String sort = "sort_example"; // String | Optional sorting parameter as per [filtering and sorting](/cloud/bitbucket/rest/intro/#sorting-query-results).
    Integer maxDepth = 56; // Integer | If provided, returns the contents of the repository and its subdirectories recursively until the specified max_depth of nested directories. When omitted, this defaults to 1.
    try {
      PaginatedTreeentries result = apiInstance.repositoriesWorkspaceRepoSlugSrcCommitPathGet(commit, path, repoSlug, workspace, format, q, sort, maxDepth);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SourceApi#repositoriesWorkspaceRepoSlugSrcCommitPathGet");
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
| **commit** | **String**| The commit&#39;s SHA1. | |
| **path** | **String**| Path to the file. | |
| **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |
| **format** | **String**| If &#39;meta&#39; is provided, returns the (json) meta data for the contents of the file.  If &#39;rendered&#39; is provided, returns the contents of a non-binary file in HTML-formatted rendered markup. Since Git does not generally track what text encoding scheme is used, this endpoint attempts to detect the most appropriate character encoding. While usually correct, determining the character encoding can be ambiguous which in exceptional cases can lead to misinterpretation of the characters. As such, the raw element in the response object should not be treated as equivalent to the file&#39;s actual contents. | [optional] [enum: meta, rendered] |
| **q** | **String**| Optional filter expression as per [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering). | [optional] |
| **sort** | **String**| Optional sorting parameter as per [filtering and sorting](/cloud/bitbucket/rest/intro/#sorting-query-results). | [optional] |
| **maxDepth** | **Integer**| If provided, returns the contents of the repository and its subdirectories recursively until the specified max_depth of nested directories. When omitted, this defaults to 1. | [optional] |

### Return type

[**PaginatedTreeentries**](PaginatedTreeentries.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | If the path matches a file, then the raw contents of the file are returned.  If the &#x60;format&#x3D;meta&#x60; query parameter is provided, a json document containing the file&#39;s meta data is returned.  If the &#x60;format&#x3D;rendered&#x60; query parameter is provided, the contents of the file in HTML-formated rendered markup is returned. If the path matches a directory, then a paginated list of file and directory entries is returned (if the &#x60;format&#x3D;meta&#x60; query parameter was provided, then the json document containing the directory&#39;s meta data is returned.)  |  -  |
| **404** | If the path or commit in the URL does not exist. |  -  |
| **555** | If the call times out, possibly because the specified recursion depth is too large. |  -  |

<a id="repositoriesWorkspaceRepoSlugSrcGet"></a>
# **repositoriesWorkspaceRepoSlugSrcGet**
> PaginatedTreeentries repositoriesWorkspaceRepoSlugSrcGet(repoSlug, workspace, format)

Get the root directory of the main branch

This endpoint redirects the client to the directory listing of the root directory on the main branch.  This is equivalent to directly hitting [/2.0/repositories/{username}/{repo_slug}/src/{commit}/{path}](src/%7Bcommit%7D/%7Bpath%7D) without having to know the name or SHA1 of the repo&#39;s main branch.  To create new commits, [POST to this endpoint](#post)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SourceApi;

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

    SourceApi apiInstance = new SourceApi(defaultClient);
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    String format = "meta"; // String | Instead of returning the file's contents, return the (json) meta data for it.
    try {
      PaginatedTreeentries result = apiInstance.repositoriesWorkspaceRepoSlugSrcGet(repoSlug, workspace, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SourceApi#repositoriesWorkspaceRepoSlugSrcGet");
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
| **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |
| **format** | **String**| Instead of returning the file&#39;s contents, return the (json) meta data for it. | [optional] [enum: meta] |

### Return type

[**PaginatedTreeentries**](PaginatedTreeentries.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | If the path matches a file, then the raw contents of the file are returned (unless the &#x60;format&#x3D;meta&#x60; query parameter was provided, in which case a json document containing the file&#39;s meta data is returned). If the path matches a directory, then a paginated list of file and directory entries is returned (if the &#x60;format&#x3D;meta&#x60; query parameter was provided, then the json document containing the directory&#39;s meta data is returned).  |  -  |
| **404** | If the path or commit in the URL does not exist. |  -  |

<a id="repositoriesWorkspaceRepoSlugSrcPost"></a>
# **repositoriesWorkspaceRepoSlugSrcPost**
> repositoriesWorkspaceRepoSlugSrcPost(repoSlug, workspace, message, author, parents, files, branch)

Create a commit by uploading a file

This endpoint is used to create new commits in the repository by uploading files.  To add a new file to a repository:  &#x60;&#x60;&#x60; $ curl https://api.bitbucket.org/2.0/repositories/username/slug/src \\   -F /repo/path/to/image.png&#x3D;@image.png &#x60;&#x60;&#x60;  This will create a new commit on top of the main branch, inheriting the contents of the main branch, but adding (or overwriting) the &#x60;image.png&#x60; file to the repository in the &#x60;/repo/path/to&#x60; directory.  To create a commit that deletes files, use the &#x60;files&#x60; parameter:  &#x60;&#x60;&#x60; $ curl https://api.bitbucket.org/2.0/repositories/username/slug/src \\   -F files&#x3D;/file/to/delete/1.txt \\   -F files&#x3D;/file/to/delete/2.txt &#x60;&#x60;&#x60;  You can add/modify/delete multiple files in a request. Rename/move a file by deleting the old path and adding the content at the new path.  This endpoint accepts &#x60;multipart/form-data&#x60; (as in the examples above), as well as &#x60;application/x-www-form-urlencoded&#x60;.  #### multipart/form-data  A &#x60;multipart/form-data&#x60; post contains a series of \&quot;form fields\&quot; that identify both the individual files that are being uploaded, as well as additional, optional meta data.  Files are uploaded in file form fields (those that have a &#x60;Content-Disposition&#x60; parameter) whose field names point to the remote path in the repository where the file should be stored. Path field names are always interpreted to be absolute from the root of the repository, regardless whether the client uses a leading slash (as the above &#x60;curl&#x60; example did).  File contents are treated as bytes and are not decoded as text.  The commit message, as well as other non-file meta data for the request, is sent along as normal form field elements. Meta data fields share the same namespace as the file objects. For &#x60;multipart/form-data&#x60; bodies that should not lead to any ambiguity, as the &#x60;Content-Disposition&#x60; header will contain the &#x60;filename&#x60; parameter to distinguish between a file named \&quot;message\&quot; and the commit message field.  #### application/x-www-form-urlencoded  It is also possible to upload new files using a simple &#x60;application/x-www-form-urlencoded&#x60; POST. This can be convenient when uploading pure text files:  &#x60;&#x60;&#x60; $ curl https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src \\   --data-urlencode \&quot;/path/to/me.txt&#x3D;Lorem ipsum.\&quot; \\   --data-urlencode \&quot;message&#x3D;Initial commit\&quot; \\   --data-urlencode \&quot;author&#x3D;Erik van Zijst &lt;erik.van.zijst@gmail.com&gt;\&quot; &#x60;&#x60;&#x60;  There could be a field name clash if a client were to upload a file named \&quot;message\&quot;, as this filename clashes with the meta data property for the commit message. To avoid this and to upload files whose names clash with the meta data properties, use a leading slash for the files, e.g. &#x60;curl --data-urlencode \&quot;/message&#x3D;file contents\&quot;&#x60;.  When an explicit slash is omitted for a file whose path matches that of a meta data parameter, then it is interpreted as meta data, not as a file.  #### Executables and links  While this API aims to facilitate the most common use cases, it is possible to perform some more advanced operations like creating a new symlink in the repository, or creating an executable file.  Files can be supplied with a &#x60;x-attributes&#x60; value in the &#x60;Content-Disposition&#x60; header. For example, to upload an executable file, as well as create a symlink from &#x60;README.txt&#x60; to &#x60;README&#x60;:  &#x60;&#x60;&#x60; --&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;1438169132528273974&#x3D;&#x3D; Content-Type: text/plain; charset&#x3D;\&quot;us-ascii\&quot; MIME-Version: 1.0 Content-Transfer-Encoding: 7bit Content-ID: \&quot;bin/shutdown.sh\&quot; Content-Disposition: attachment; filename&#x3D;\&quot;shutdown.sh\&quot;; x-attributes:\&quot;executable\&quot;  #!/bin/sh halt  --&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;1438169132528273974&#x3D;&#x3D; Content-Type: text/plain; charset&#x3D;\&quot;us-ascii\&quot; MIME-Version: 1.0 Content-Transfer-Encoding: 7bit Content-ID: \&quot;/README.txt\&quot; Content-Disposition: attachment; filename&#x3D;\&quot;README.txt\&quot;; x-attributes:\&quot;link\&quot;  README --&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;1438169132528273974&#x3D;&#x3D;-- &#x60;&#x60;&#x60;  Links are files that contain the target path and have &#x60;x-attributes:\&quot;link\&quot;&#x60; set.  When overwriting links with files, or vice versa, the newly uploaded file determines both the new contents, as well as the attributes. That means uploading a file without specifying &#x60;x-attributes&#x3D;\&quot;link\&quot;&#x60; will create a regular file, even if the parent commit hosted a symlink at the same path.  The same applies to executables. When modifying an existing executable file, the form-data file element must include &#x60;x-attributes&#x3D;\&quot;executable\&quot;&#x60; in order to preserve the executable status of the file.  Note that this API does not support the creation or manipulation of subrepos / submodules.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SourceApi;

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

    SourceApi apiInstance = new SourceApi(defaultClient);
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    String message = "message_example"; // String | The commit message. When omitted, Bitbucket uses a canned string.
    String author = "author_example"; // String |  The raw string to be used as the new commit's author. This string follows the format `Erik van Zijst <evzijst@atlassian.com>`.  When omitted, Bitbucket uses the authenticated user's full/display name and primary email address. Commits cannot be created anonymously.
    String parents = "parents_example"; // String |  A comma-separated list of SHA1s of the commits that should be the parents of the newly created commit.  When omitted, the new commit will inherit from and become a child of the main branch's tip/HEAD commit.  When more than one SHA1 is provided, the first SHA1 identifies the commit from which the content will be inherited.\".
    String files = "files_example"; // String |  Optional field that declares the files that the request is manipulating. When adding a new file to a repo, or when overwriting an existing file, the client can just upload the full contents of the file in a normal form field and the use of this `files` meta data field is redundant. However, when the `files` field contains a file path that does not have a corresponding, identically-named form field, then Bitbucket interprets that as the client wanting to replace the named file with the null set and the file is deleted instead.  Paths in the repo that are referenced in neither files nor an individual file field, remain unchanged and carry over from the parent to the new commit.  This API does not support renaming as an explicit feature. To rename a file, simply delete it and recreate it under the new name in the same commit. 
    String branch = "branch_example"; // String |  The name of the branch that the new commit should be created on. When omitted, the commit will be created on top of the main branch and will become the main branch's new head.  When a branch name is provided that already exists in the repo, then the commit will be created on top of that branch. In this case, *if* a parent SHA1 was also provided, then it is asserted that the parent is the branch's tip/HEAD at the time the request is made. When this is not the case, a 409 is returned.  When a new branch name is specified (that does not already exist in the repo), and no parent SHA1s are provided, then the new commit will inherit from the current main branch's tip/HEAD commit, but not advance the main branch. The new commit will be the new branch. When the request *also* specifies a parent SHA1, then the new commit and branch are created directly on top of the parent commit, regardless of the state of the main branch.  When a branch name is not specified, but a parent SHA1 is provided, then Bitbucket asserts that it represents the main branch's current HEAD/tip, or a 409 is returned.  When a branch name is not specified and the repo is empty, the new commit will become the repo's root commit and will be on the main branch.  When a branch name is specified and the repo is empty, the new commit will become the repo's root commit and also define the repo's main branch going forward.  This API cannot be used to create additional root commits in non-empty repos.  The branch field cannot be repeated.  As a side effect, this API can be used to create a new branch without modifying any files, by specifying a new branch name in this field, together with `parents`, but omitting the `files` fields, while not sending any files. This will create a new commit and branch with the same contents as the first parent. The diff of this commit against its first parent will be empty. 
    try {
      apiInstance.repositoriesWorkspaceRepoSlugSrcPost(repoSlug, workspace, message, author, parents, files, branch);
    } catch (ApiException e) {
      System.err.println("Exception when calling SourceApi#repositoriesWorkspaceRepoSlugSrcPost");
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
| **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |
| **message** | **String**| The commit message. When omitted, Bitbucket uses a canned string. | [optional] |
| **author** | **String**|  The raw string to be used as the new commit&#39;s author. This string follows the format &#x60;Erik van Zijst &lt;evzijst@atlassian.com&gt;&#x60;.  When omitted, Bitbucket uses the authenticated user&#39;s full/display name and primary email address. Commits cannot be created anonymously. | [optional] |
| **parents** | **String**|  A comma-separated list of SHA1s of the commits that should be the parents of the newly created commit.  When omitted, the new commit will inherit from and become a child of the main branch&#39;s tip/HEAD commit.  When more than one SHA1 is provided, the first SHA1 identifies the commit from which the content will be inherited.\&quot;. | [optional] |
| **files** | **String**|  Optional field that declares the files that the request is manipulating. When adding a new file to a repo, or when overwriting an existing file, the client can just upload the full contents of the file in a normal form field and the use of this &#x60;files&#x60; meta data field is redundant. However, when the &#x60;files&#x60; field contains a file path that does not have a corresponding, identically-named form field, then Bitbucket interprets that as the client wanting to replace the named file with the null set and the file is deleted instead.  Paths in the repo that are referenced in neither files nor an individual file field, remain unchanged and carry over from the parent to the new commit.  This API does not support renaming as an explicit feature. To rename a file, simply delete it and recreate it under the new name in the same commit.  | [optional] |
| **branch** | **String**|  The name of the branch that the new commit should be created on. When omitted, the commit will be created on top of the main branch and will become the main branch&#39;s new head.  When a branch name is provided that already exists in the repo, then the commit will be created on top of that branch. In this case, *if* a parent SHA1 was also provided, then it is asserted that the parent is the branch&#39;s tip/HEAD at the time the request is made. When this is not the case, a 409 is returned.  When a new branch name is specified (that does not already exist in the repo), and no parent SHA1s are provided, then the new commit will inherit from the current main branch&#39;s tip/HEAD commit, but not advance the main branch. The new commit will be the new branch. When the request *also* specifies a parent SHA1, then the new commit and branch are created directly on top of the parent commit, regardless of the state of the main branch.  When a branch name is not specified, but a parent SHA1 is provided, then Bitbucket asserts that it represents the main branch&#39;s current HEAD/tip, or a 409 is returned.  When a branch name is not specified and the repo is empty, the new commit will become the repo&#39;s root commit and will be on the main branch.  When a branch name is specified and the repo is empty, the new commit will become the repo&#39;s root commit and also define the repo&#39;s main branch going forward.  This API cannot be used to create additional root commits in non-empty repos.  The branch field cannot be repeated.  As a side effect, this API can be used to create a new branch without modifying any files, by specifying a new branch name in this field, together with &#x60;parents&#x60;, but omitting the &#x60;files&#x60; fields, while not sending any files. This will create a new commit and branch with the same contents as the first parent. The diff of this commit against its first parent will be empty.  | [optional] |

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
| **201** |   |  -  |
| **403** | If the authenticated user does not have write or admin access |  -  |
| **404** | If the repository does not exist. |  -  |

