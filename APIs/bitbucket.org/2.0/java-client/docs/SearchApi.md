# SearchApi

All URIs are relative to *https://api.bitbucket.org/2.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**searchAccount**](SearchApi.md#searchAccount) | **GET** /users/{selected_user}/search/code | Search for code in a user&#39;s repositories |
| [**searchTeam**](SearchApi.md#searchTeam) | **GET** /teams/{username}/search/code | Search for code in a team&#39;s repositories |
| [**searchWorkspace**](SearchApi.md#searchWorkspace) | **GET** /workspaces/{workspace}/search/code | Search for code in a workspace |


<a id="searchAccount"></a>
# **searchAccount**
> SearchResultPage searchAccount(selectedUser, searchQuery, page, pagelen)

Search for code in a user&#39;s repositories

Search for code in the repositories of the specified user.  Searching across all repositories:  &#x60;&#x60;&#x60; curl &#39;https://api.bitbucket.org/2.0/users/{ed08f5e1-605b-4f4a-aee4-6c97628a673e}/search/code?search_query&#x3D;foo&#39; {   \&quot;size\&quot;: 1,   \&quot;page\&quot;: 1,   \&quot;pagelen\&quot;: 10,   \&quot;query_substituted\&quot;: false,   \&quot;values\&quot;: [     {       \&quot;type\&quot;: \&quot;code_search_result\&quot;,       \&quot;content_match_count\&quot;: 2,       \&quot;content_matches\&quot;: [         {           \&quot;lines\&quot;: [             {               \&quot;line\&quot;: 2,               \&quot;segments\&quot;: []             },             {               \&quot;line\&quot;: 3,               \&quot;segments\&quot;: [                 {                   \&quot;text\&quot;: \&quot;def \&quot;                 },                 {                   \&quot;text\&quot;: \&quot;foo\&quot;,                   \&quot;match\&quot;: true                 },                 {                   \&quot;text\&quot;: \&quot;():\&quot;                 }               ]             },             {               \&quot;line\&quot;: 4,               \&quot;segments\&quot;: [                 {                   \&quot;text\&quot;: \&quot;    print(\\\&quot;snek\\\&quot;)\&quot;                 }               ]             },             {               \&quot;line\&quot;: 5,               \&quot;segments\&quot;: []             }           ]         }       ],       \&quot;path_matches\&quot;: [         {           \&quot;text\&quot;: \&quot;src/\&quot;         },         {           \&quot;text\&quot;: \&quot;foo\&quot;,           \&quot;match\&quot;: true         },         {           \&quot;text\&quot;: \&quot;.py\&quot;         }       ],       \&quot;file\&quot;: {         \&quot;path\&quot;: \&quot;src/foo.py\&quot;,         \&quot;type\&quot;: \&quot;commit_file\&quot;,         \&quot;links\&quot;: {           \&quot;self\&quot;: {             \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/my-workspace/demo/src/ad6964b5fe2880dbd9ddcad1c89000f1dbcbc24b/src/foo.py\&quot;           }         }       }     }   ] } &#x60;&#x60;&#x60;  Note that searches can match in the file&#39;s text (&#x60;content_matches&#x60;), the path (&#x60;path_matches&#x60;), or both as in the example above.  You can use the same syntax for the search query as in the UI, e.g. to only search within a specific repository:  &#x60;&#x60;&#x60; curl &#39;https://api.bitbucket.org/2.0/users/{ed08f5e1-605b-4f4a-aee4-6c97628a673e}/search/code?search_query&#x3D;foo+repo:demo&#39; # results from the \&quot;demo\&quot; repository &#x60;&#x60;&#x60;  Similar to other APIs, you can request more fields using a &#x60;fields&#x60; query parameter. E.g. to get some more information about the repository of matched files (the &#x60;%2B&#x60; is a URL-encoded &#x60;+&#x60;):  &#x60;&#x60;&#x60; curl &#39;https://api.bitbucket.org/2.0/users/{ed08f5e1-605b-4f4a-aee4-6c97628a673e}/search/code&#39;\\      &#39;?search_query&#x3D;foo&amp;fields&#x3D;%2Bvalues.file.commit.repository&#39; {   \&quot;size\&quot;: 1,   \&quot;page\&quot;: 1,   \&quot;pagelen\&quot;: 10,   \&quot;query_substituted\&quot;: false,   \&quot;values\&quot;: [     {       \&quot;type\&quot;: \&quot;code_search_result\&quot;,       \&quot;content_match_count\&quot;: 1,       \&quot;content_matches\&quot;: [...],       \&quot;path_matches\&quot;: [...],       \&quot;file\&quot;: {         \&quot;commit\&quot;: {           \&quot;type\&quot;: \&quot;commit\&quot;,           \&quot;hash\&quot;: \&quot;ad6964b5fe2880dbd9ddcad1c89000f1dbcbc24b\&quot;,           \&quot;links\&quot;: {             \&quot;self\&quot;: {               \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/my-workspace/demo/commit/ad6964b5fe2880dbd9ddcad1c89000f1dbcbc24b\&quot;             },             \&quot;html\&quot;: {               \&quot;href\&quot;: \&quot;https://bitbucket.org/my-workspace/demo/commits/ad6964b5fe2880dbd9ddcad1c89000f1dbcbc24b\&quot;             }           },           \&quot;repository\&quot;: {             \&quot;name\&quot;: \&quot;demo\&quot;,             \&quot;type\&quot;: \&quot;repository\&quot;,             \&quot;full_name\&quot;: \&quot;my-workspace/demo\&quot;,             \&quot;links\&quot;: {               \&quot;self\&quot;: {                 \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/my-workspace/demo\&quot;               },               \&quot;html\&quot;: {                 \&quot;href\&quot;: \&quot;https://bitbucket.org/my-workspace/demo\&quot;               },               \&quot;avatar\&quot;: {                 \&quot;href\&quot;: \&quot;https://bytebucket.org/ravatar/%7B850e1749-781a-4115-9316-df39d0600e7a%7D?ts&#x3D;default\&quot;               }             },             \&quot;uuid\&quot;: \&quot;{850e1749-781a-4115-9316-df39d0600e7a}\&quot;           }         },         \&quot;type\&quot;: \&quot;commit_file\&quot;,         \&quot;links\&quot;: {           \&quot;self\&quot;: {             \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/my-workspace/demo/src/ad6964b5fe2880dbd9ddcad1c89000f1dbcbc24b/src/foo.py\&quot;           }         },         \&quot;path\&quot;: \&quot;src/foo.py\&quot;       }     }   ] } &#x60;&#x60;&#x60;  Try &#x60;fields&#x3D;%2Bvalues.*.*.*.*&#x60; to get an idea what&#39;s possible. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    SearchApi apiInstance = new SearchApi(defaultClient);
    String selectedUser = "selectedUser_example"; // String | Either the UUID of the account surrounded by curly-braces, for example `{account UUID}`, OR an Atlassian Account ID.
    String searchQuery = "searchQuery_example"; // String | The search query
    Integer page = 1; // Integer | Which page of the search results to retrieve
    Integer pagelen = 10; // Integer | How many search results to retrieve per page
    try {
      SearchResultPage result = apiInstance.searchAccount(selectedUser, searchQuery, page, pagelen);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#searchAccount");
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
| **selectedUser** | **String**| Either the UUID of the account surrounded by curly-braces, for example &#x60;{account UUID}&#x60;, OR an Atlassian Account ID. | |
| **searchQuery** | **String**| The search query | |
| **page** | **Integer**| Which page of the search results to retrieve | [optional] [default to 1] |
| **pagelen** | **Integer**| How many search results to retrieve per page | [optional] [default to 10] |

### Return type

[**SearchResultPage**](SearchResultPage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful search |  -  |
| **400** | If the search request was invalid due to one of the following reasons:  * the specified type of target account doesn&#39;&#39;t match the actual account type;  * malformed pagination properties;  * missing or malformed search query, in the latter case an error key will be returned in &#x60;error.data.key&#x60; property.  |  -  |
| **404** | Search is not enabled for the requested user, navigate to [https://bitbucket.org/search](https://bitbucket.org/search) to turn it on |  -  |
| **429** | Too many requests, try again later |  -  |

<a id="searchTeam"></a>
# **searchTeam**
> SearchResultPage searchTeam(username, searchQuery, page, pagelen)

Search for code in a team&#39;s repositories

Search for code in the repositories of the specified team.  Searching across all repositories:  &#x60;&#x60;&#x60; curl &#39;https://api.bitbucket.org/2.0/teams/team_name/search/code?search_query&#x3D;foo&#39; {   \&quot;size\&quot;: 1,   \&quot;page\&quot;: 1,   \&quot;pagelen\&quot;: 10,   \&quot;query_substituted\&quot;: false,   \&quot;values\&quot;: [     {       \&quot;type\&quot;: \&quot;code_search_result\&quot;,       \&quot;content_match_count\&quot;: 2,       \&quot;content_matches\&quot;: [         {           \&quot;lines\&quot;: [             {               \&quot;line\&quot;: 2,               \&quot;segments\&quot;: []             },             {               \&quot;line\&quot;: 3,               \&quot;segments\&quot;: [                 {                   \&quot;text\&quot;: \&quot;def \&quot;                 },                 {                   \&quot;text\&quot;: \&quot;foo\&quot;,                   \&quot;match\&quot;: true                 },                 {                   \&quot;text\&quot;: \&quot;():\&quot;                 }               ]             },             {               \&quot;line\&quot;: 4,               \&quot;segments\&quot;: [                 {                   \&quot;text\&quot;: \&quot;    print(\\\&quot;snek\\\&quot;)\&quot;                 }               ]             },             {               \&quot;line\&quot;: 5,               \&quot;segments\&quot;: []             }           ]         }       ],       \&quot;path_matches\&quot;: [         {           \&quot;text\&quot;: \&quot;src/\&quot;         },         {           \&quot;text\&quot;: \&quot;foo\&quot;,           \&quot;match\&quot;: true         },         {           \&quot;text\&quot;: \&quot;.py\&quot;         }       ],       \&quot;file\&quot;: {         \&quot;path\&quot;: \&quot;src/foo.py\&quot;,         \&quot;type\&quot;: \&quot;commit_file\&quot;,         \&quot;links\&quot;: {           \&quot;self\&quot;: {             \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/my-workspace/demo/src/ad6964b5fe2880dbd9ddcad1c89000f1dbcbc24b/src/foo.py\&quot;           }         }       }     }   ] } &#x60;&#x60;&#x60;  Note that searches can match in the file&#39;s text (&#x60;content_matches&#x60;), the path (&#x60;path_matches&#x60;), or both as in the example above.  You can use the same syntax for the search query as in the UI, e.g. to only search within a specific repository:  &#x60;&#x60;&#x60; curl &#39;https://api.bitbucket.org/2.0/teams/team_name/search/code?search_query&#x3D;foo+repo:demo&#39; # results from the \&quot;demo\&quot; repository &#x60;&#x60;&#x60;  Similar to other APIs, you can request more fields using a &#x60;fields&#x60; query parameter. E.g. to get some more information about the repository of matched files (the &#x60;%2B&#x60; is a URL-encoded &#x60;+&#x60;):  &#x60;&#x60;&#x60; curl &#39;https://api.bitbucket.org/2.0/teams/team_name/search/code&#39;\\      &#39;?search_query&#x3D;foo&amp;fields&#x3D;%2Bvalues.file.commit.repository&#39; {   \&quot;size\&quot;: 1,   \&quot;page\&quot;: 1,   \&quot;pagelen\&quot;: 10,   \&quot;query_substituted\&quot;: false,   \&quot;values\&quot;: [     {       \&quot;type\&quot;: \&quot;code_search_result\&quot;,       \&quot;content_match_count\&quot;: 1,       \&quot;content_matches\&quot;: [...],       \&quot;path_matches\&quot;: [...],       \&quot;file\&quot;: {         \&quot;commit\&quot;: {           \&quot;type\&quot;: \&quot;commit\&quot;,           \&quot;hash\&quot;: \&quot;ad6964b5fe2880dbd9ddcad1c89000f1dbcbc24b\&quot;,           \&quot;links\&quot;: {             \&quot;self\&quot;: {               \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/my-workspace/demo/commit/ad6964b5fe2880dbd9ddcad1c89000f1dbcbc24b\&quot;             },             \&quot;html\&quot;: {               \&quot;href\&quot;: \&quot;https://bitbucket.org/my-workspace/demo/commits/ad6964b5fe2880dbd9ddcad1c89000f1dbcbc24b\&quot;             }           },           \&quot;repository\&quot;: {             \&quot;name\&quot;: \&quot;demo\&quot;,             \&quot;type\&quot;: \&quot;repository\&quot;,             \&quot;full_name\&quot;: \&quot;my-workspace/demo\&quot;,             \&quot;links\&quot;: {               \&quot;self\&quot;: {                 \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/my-workspace/demo\&quot;               },               \&quot;html\&quot;: {                 \&quot;href\&quot;: \&quot;https://bitbucket.org/my-workspace/demo\&quot;               },               \&quot;avatar\&quot;: {                 \&quot;href\&quot;: \&quot;https://bytebucket.org/ravatar/%7B850e1749-781a-4115-9316-df39d0600e7a%7D?ts&#x3D;default\&quot;               }             },             \&quot;uuid\&quot;: \&quot;{850e1749-781a-4115-9316-df39d0600e7a}\&quot;           }         },         \&quot;type\&quot;: \&quot;commit_file\&quot;,         \&quot;links\&quot;: {           \&quot;self\&quot;: {             \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/my-workspace/demo/src/ad6964b5fe2880dbd9ddcad1c89000f1dbcbc24b/src/foo.py\&quot;           }         },         \&quot;path\&quot;: \&quot;src/foo.py\&quot;       }     }   ] } &#x60;&#x60;&#x60;  Try &#x60;fields&#x3D;%2Bvalues.*.*.*.*&#x60; to get an idea what&#39;s possible. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    SearchApi apiInstance = new SearchApi(defaultClient);
    String username = "username_example"; // String | The account to search in; either the username or the UUID in curly braces
    String searchQuery = "searchQuery_example"; // String | The search query
    Integer page = 1; // Integer | Which page of the search results to retrieve
    Integer pagelen = 10; // Integer | How many search results to retrieve per page
    try {
      SearchResultPage result = apiInstance.searchTeam(username, searchQuery, page, pagelen);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#searchTeam");
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
| **username** | **String**| The account to search in; either the username or the UUID in curly braces | |
| **searchQuery** | **String**| The search query | |
| **page** | **Integer**| Which page of the search results to retrieve | [optional] [default to 1] |
| **pagelen** | **Integer**| How many search results to retrieve per page | [optional] [default to 10] |

### Return type

[**SearchResultPage**](SearchResultPage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful search |  -  |
| **400** | If the search request was invalid due to one of the following reasons:  * the specified type of target account doesn&#39;&#39;t match the actual account type;  * malformed pagination properties;  * missing or malformed search query, in the latter case an error key will be returned in &#x60;error.data.key&#x60; property.  |  -  |
| **404** | Search is not enabled for the requested team, navigate to [https://bitbucket.org/search](https://bitbucket.org/search) to turn it on |  -  |
| **429** | Too many requests, try again later |  -  |

<a id="searchWorkspace"></a>
# **searchWorkspace**
> SearchResultPage searchWorkspace(workspace, searchQuery, page, pagelen)

Search for code in a workspace

Search for code in the repositories of the specified workspace.  Searching across all repositories:  &#x60;&#x60;&#x60; curl &#39;https://api.bitbucket.org/2.0/workspaces/workspace_slug_or_uuid/search/code?search_query&#x3D;foo&#39; {   \&quot;size\&quot;: 1,   \&quot;page\&quot;: 1,   \&quot;pagelen\&quot;: 10,   \&quot;query_substituted\&quot;: false,   \&quot;values\&quot;: [     {       \&quot;type\&quot;: \&quot;code_search_result\&quot;,       \&quot;content_match_count\&quot;: 2,       \&quot;content_matches\&quot;: [         {           \&quot;lines\&quot;: [             {               \&quot;line\&quot;: 2,               \&quot;segments\&quot;: []             },             {               \&quot;line\&quot;: 3,               \&quot;segments\&quot;: [                 {                   \&quot;text\&quot;: \&quot;def \&quot;                 },                 {                   \&quot;text\&quot;: \&quot;foo\&quot;,                   \&quot;match\&quot;: true                 },                 {                   \&quot;text\&quot;: \&quot;():\&quot;                 }               ]             },             {               \&quot;line\&quot;: 4,               \&quot;segments\&quot;: [                 {                   \&quot;text\&quot;: \&quot;    print(\\\&quot;snek\\\&quot;)\&quot;                 }               ]             },             {               \&quot;line\&quot;: 5,               \&quot;segments\&quot;: []             }           ]         }       ],       \&quot;path_matches\&quot;: [         {           \&quot;text\&quot;: \&quot;src/\&quot;         },         {           \&quot;text\&quot;: \&quot;foo\&quot;,           \&quot;match\&quot;: true         },         {           \&quot;text\&quot;: \&quot;.py\&quot;         }       ],       \&quot;file\&quot;: {         \&quot;path\&quot;: \&quot;src/foo.py\&quot;,         \&quot;type\&quot;: \&quot;commit_file\&quot;,         \&quot;links\&quot;: {           \&quot;self\&quot;: {             \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/my-workspace/demo/src/ad6964b5fe2880dbd9ddcad1c89000f1dbcbc24b/src/foo.py\&quot;           }         }       }     }   ] } &#x60;&#x60;&#x60;  Note that searches can match in the file&#39;s text (&#x60;content_matches&#x60;), the path (&#x60;path_matches&#x60;), or both as in the example above.  You can use the same syntax for the search query as in the UI, e.g. to only search within a specific repository:  &#x60;&#x60;&#x60; curl &#39;https://api.bitbucket.org/2.0/workspaces/my-workspace/search/code?search_query&#x3D;foo+repo:demo&#39; # results from the \&quot;demo\&quot; repository &#x60;&#x60;&#x60;  Similar to other APIs, you can request more fields using a &#x60;fields&#x60; query parameter. E.g. to get some more information about the repository of matched files (the &#x60;%2B&#x60; is a URL-encoded &#x60;+&#x60;):  &#x60;&#x60;&#x60; curl &#39;https://api.bitbucket.org/2.0/workspaces/my-workspace/search/code&#39;\\      &#39;?search_query&#x3D;foo&amp;fields&#x3D;%2Bvalues.file.commit.repository&#39; {   \&quot;size\&quot;: 1,   \&quot;page\&quot;: 1,   \&quot;pagelen\&quot;: 10,   \&quot;query_substituted\&quot;: false,   \&quot;values\&quot;: [     {       \&quot;type\&quot;: \&quot;code_search_result\&quot;,       \&quot;content_match_count\&quot;: 1,       \&quot;content_matches\&quot;: [...],       \&quot;path_matches\&quot;: [...],       \&quot;file\&quot;: {         \&quot;commit\&quot;: {           \&quot;type\&quot;: \&quot;commit\&quot;,           \&quot;hash\&quot;: \&quot;ad6964b5fe2880dbd9ddcad1c89000f1dbcbc24b\&quot;,           \&quot;links\&quot;: {             \&quot;self\&quot;: {               \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/my-workspace/demo/commit/ad6964b5fe2880dbd9ddcad1c89000f1dbcbc24b\&quot;             },             \&quot;html\&quot;: {               \&quot;href\&quot;: \&quot;https://bitbucket.org/my-workspace/demo/commits/ad6964b5fe2880dbd9ddcad1c89000f1dbcbc24b\&quot;             }           },           \&quot;repository\&quot;: {             \&quot;name\&quot;: \&quot;demo\&quot;,             \&quot;type\&quot;: \&quot;repository\&quot;,             \&quot;full_name\&quot;: \&quot;my-workspace/demo\&quot;,             \&quot;links\&quot;: {               \&quot;self\&quot;: {                 \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/my-workspace/demo\&quot;               },               \&quot;html\&quot;: {                 \&quot;href\&quot;: \&quot;https://bitbucket.org/my-workspace/demo\&quot;               },               \&quot;avatar\&quot;: {                 \&quot;href\&quot;: \&quot;https://bytebucket.org/ravatar/%7B850e1749-781a-4115-9316-df39d0600e7a%7D?ts&#x3D;default\&quot;               }             },             \&quot;uuid\&quot;: \&quot;{850e1749-781a-4115-9316-df39d0600e7a}\&quot;           }         },         \&quot;type\&quot;: \&quot;commit_file\&quot;,         \&quot;links\&quot;: {           \&quot;self\&quot;: {             \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/my-workspace/demo/src/ad6964b5fe2880dbd9ddcad1c89000f1dbcbc24b/src/foo.py\&quot;           }         },         \&quot;path\&quot;: \&quot;src/foo.py\&quot;       }     }   ] } &#x60;&#x60;&#x60;  Try &#x60;fields&#x3D;%2Bvalues.*.*.*.*&#x60; to get an idea what&#39;s possible. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    SearchApi apiInstance = new SearchApi(defaultClient);
    String workspace = "workspace_example"; // String | The workspace to search in; either the slug or the UUID in curly braces
    String searchQuery = "searchQuery_example"; // String | The search query
    Integer page = 1; // Integer | Which page of the search results to retrieve
    Integer pagelen = 10; // Integer | How many search results to retrieve per page
    try {
      SearchResultPage result = apiInstance.searchWorkspace(workspace, searchQuery, page, pagelen);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#searchWorkspace");
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
| **workspace** | **String**| The workspace to search in; either the slug or the UUID in curly braces | |
| **searchQuery** | **String**| The search query | |
| **page** | **Integer**| Which page of the search results to retrieve | [optional] [default to 1] |
| **pagelen** | **Integer**| How many search results to retrieve per page | [optional] [default to 10] |

### Return type

[**SearchResultPage**](SearchResultPage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful search |  -  |
| **400** | If the search request was invalid due to one of the following reasons:  * the specified type of target account doesn&#39;&#39;t match the actual account type;  * malformed pagination properties;  * missing or malformed search query, in the latter case an error key will be returned in &#x60;error.data.key&#x60; property.  |  -  |
| **404** | Search is not enabled for the requested workspace, navigate to [https://bitbucket.org/search](https://bitbucket.org/search) to turn it on |  -  |
| **429** | Too many requests, try again later |  -  |

