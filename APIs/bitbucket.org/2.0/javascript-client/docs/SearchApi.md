# BitbucketApi.SearchApi

All URIs are relative to *https://api.bitbucket.org/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**searchAccount**](SearchApi.md#searchAccount) | **GET** /users/{selected_user}/search/code | Search for code in a user&#39;s repositories
[**searchTeam**](SearchApi.md#searchTeam) | **GET** /teams/{username}/search/code | Search for code in a team&#39;s repositories
[**searchWorkspace**](SearchApi.md#searchWorkspace) | **GET** /workspaces/{workspace}/search/code | Search for code in a workspace



## searchAccount

> SearchResultPage searchAccount(selectedUser, searchQuery, opts)

Search for code in a user&#39;s repositories

Search for code in the repositories of the specified user.  Searching across all repositories:  &#x60;&#x60;&#x60; curl &#39;https://api.bitbucket.org/2.0/users/{ed08f5e1-605b-4f4a-aee4-6c97628a673e}/search/code?search_query&#x3D;foo&#39; {   \&quot;size\&quot;: 1,   \&quot;page\&quot;: 1,   \&quot;pagelen\&quot;: 10,   \&quot;query_substituted\&quot;: false,   \&quot;values\&quot;: [     {       \&quot;type\&quot;: \&quot;code_search_result\&quot;,       \&quot;content_match_count\&quot;: 2,       \&quot;content_matches\&quot;: [         {           \&quot;lines\&quot;: [             {               \&quot;line\&quot;: 2,               \&quot;segments\&quot;: []             },             {               \&quot;line\&quot;: 3,               \&quot;segments\&quot;: [                 {                   \&quot;text\&quot;: \&quot;def \&quot;                 },                 {                   \&quot;text\&quot;: \&quot;foo\&quot;,                   \&quot;match\&quot;: true                 },                 {                   \&quot;text\&quot;: \&quot;():\&quot;                 }               ]             },             {               \&quot;line\&quot;: 4,               \&quot;segments\&quot;: [                 {                   \&quot;text\&quot;: \&quot;    print(\\\&quot;snek\\\&quot;)\&quot;                 }               ]             },             {               \&quot;line\&quot;: 5,               \&quot;segments\&quot;: []             }           ]         }       ],       \&quot;path_matches\&quot;: [         {           \&quot;text\&quot;: \&quot;src/\&quot;         },         {           \&quot;text\&quot;: \&quot;foo\&quot;,           \&quot;match\&quot;: true         },         {           \&quot;text\&quot;: \&quot;.py\&quot;         }       ],       \&quot;file\&quot;: {         \&quot;path\&quot;: \&quot;src/foo.py\&quot;,         \&quot;type\&quot;: \&quot;commit_file\&quot;,         \&quot;links\&quot;: {           \&quot;self\&quot;: {             \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/my-workspace/demo/src/ad6964b5fe2880dbd9ddcad1c89000f1dbcbc24b/src/foo.py\&quot;           }         }       }     }   ] } &#x60;&#x60;&#x60;  Note that searches can match in the file&#39;s text (&#x60;content_matches&#x60;), the path (&#x60;path_matches&#x60;), or both as in the example above.  You can use the same syntax for the search query as in the UI, e.g. to only search within a specific repository:  &#x60;&#x60;&#x60; curl &#39;https://api.bitbucket.org/2.0/users/{ed08f5e1-605b-4f4a-aee4-6c97628a673e}/search/code?search_query&#x3D;foo+repo:demo&#39; # results from the \&quot;demo\&quot; repository &#x60;&#x60;&#x60;  Similar to other APIs, you can request more fields using a &#x60;fields&#x60; query parameter. E.g. to get some more information about the repository of matched files (the &#x60;%2B&#x60; is a URL-encoded &#x60;+&#x60;):  &#x60;&#x60;&#x60; curl &#39;https://api.bitbucket.org/2.0/users/{ed08f5e1-605b-4f4a-aee4-6c97628a673e}/search/code&#39;\\      &#39;?search_query&#x3D;foo&amp;fields&#x3D;%2Bvalues.file.commit.repository&#39; {   \&quot;size\&quot;: 1,   \&quot;page\&quot;: 1,   \&quot;pagelen\&quot;: 10,   \&quot;query_substituted\&quot;: false,   \&quot;values\&quot;: [     {       \&quot;type\&quot;: \&quot;code_search_result\&quot;,       \&quot;content_match_count\&quot;: 1,       \&quot;content_matches\&quot;: [...],       \&quot;path_matches\&quot;: [...],       \&quot;file\&quot;: {         \&quot;commit\&quot;: {           \&quot;type\&quot;: \&quot;commit\&quot;,           \&quot;hash\&quot;: \&quot;ad6964b5fe2880dbd9ddcad1c89000f1dbcbc24b\&quot;,           \&quot;links\&quot;: {             \&quot;self\&quot;: {               \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/my-workspace/demo/commit/ad6964b5fe2880dbd9ddcad1c89000f1dbcbc24b\&quot;             },             \&quot;html\&quot;: {               \&quot;href\&quot;: \&quot;https://bitbucket.org/my-workspace/demo/commits/ad6964b5fe2880dbd9ddcad1c89000f1dbcbc24b\&quot;             }           },           \&quot;repository\&quot;: {             \&quot;name\&quot;: \&quot;demo\&quot;,             \&quot;type\&quot;: \&quot;repository\&quot;,             \&quot;full_name\&quot;: \&quot;my-workspace/demo\&quot;,             \&quot;links\&quot;: {               \&quot;self\&quot;: {                 \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/my-workspace/demo\&quot;               },               \&quot;html\&quot;: {                 \&quot;href\&quot;: \&quot;https://bitbucket.org/my-workspace/demo\&quot;               },               \&quot;avatar\&quot;: {                 \&quot;href\&quot;: \&quot;https://bytebucket.org/ravatar/%7B850e1749-781a-4115-9316-df39d0600e7a%7D?ts&#x3D;default\&quot;               }             },             \&quot;uuid\&quot;: \&quot;{850e1749-781a-4115-9316-df39d0600e7a}\&quot;           }         },         \&quot;type\&quot;: \&quot;commit_file\&quot;,         \&quot;links\&quot;: {           \&quot;self\&quot;: {             \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/my-workspace/demo/src/ad6964b5fe2880dbd9ddcad1c89000f1dbcbc24b/src/foo.py\&quot;           }         },         \&quot;path\&quot;: \&quot;src/foo.py\&quot;       }     }   ] } &#x60;&#x60;&#x60;  Try &#x60;fields&#x3D;%2Bvalues.*.*.*.*&#x60; to get an idea what&#39;s possible. 

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.SearchApi();
let selectedUser = "selectedUser_example"; // String | Either the UUID of the account surrounded by curly-braces, for example `{account UUID}`, OR an Atlassian Account ID.
let searchQuery = "searchQuery_example"; // String | The search query
let opts = {
  'page': 1, // Number | Which page of the search results to retrieve
  'pagelen': 10 // Number | How many search results to retrieve per page
};
apiInstance.searchAccount(selectedUser, searchQuery, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **selectedUser** | **String**| Either the UUID of the account surrounded by curly-braces, for example &#x60;{account UUID}&#x60;, OR an Atlassian Account ID. | 
 **searchQuery** | **String**| The search query | 
 **page** | **Number**| Which page of the search results to retrieve | [optional] [default to 1]
 **pagelen** | **Number**| How many search results to retrieve per page | [optional] [default to 10]

### Return type

[**SearchResultPage**](SearchResultPage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## searchTeam

> SearchResultPage searchTeam(username, searchQuery, opts)

Search for code in a team&#39;s repositories

Search for code in the repositories of the specified team.  Searching across all repositories:  &#x60;&#x60;&#x60; curl &#39;https://api.bitbucket.org/2.0/teams/team_name/search/code?search_query&#x3D;foo&#39; {   \&quot;size\&quot;: 1,   \&quot;page\&quot;: 1,   \&quot;pagelen\&quot;: 10,   \&quot;query_substituted\&quot;: false,   \&quot;values\&quot;: [     {       \&quot;type\&quot;: \&quot;code_search_result\&quot;,       \&quot;content_match_count\&quot;: 2,       \&quot;content_matches\&quot;: [         {           \&quot;lines\&quot;: [             {               \&quot;line\&quot;: 2,               \&quot;segments\&quot;: []             },             {               \&quot;line\&quot;: 3,               \&quot;segments\&quot;: [                 {                   \&quot;text\&quot;: \&quot;def \&quot;                 },                 {                   \&quot;text\&quot;: \&quot;foo\&quot;,                   \&quot;match\&quot;: true                 },                 {                   \&quot;text\&quot;: \&quot;():\&quot;                 }               ]             },             {               \&quot;line\&quot;: 4,               \&quot;segments\&quot;: [                 {                   \&quot;text\&quot;: \&quot;    print(\\\&quot;snek\\\&quot;)\&quot;                 }               ]             },             {               \&quot;line\&quot;: 5,               \&quot;segments\&quot;: []             }           ]         }       ],       \&quot;path_matches\&quot;: [         {           \&quot;text\&quot;: \&quot;src/\&quot;         },         {           \&quot;text\&quot;: \&quot;foo\&quot;,           \&quot;match\&quot;: true         },         {           \&quot;text\&quot;: \&quot;.py\&quot;         }       ],       \&quot;file\&quot;: {         \&quot;path\&quot;: \&quot;src/foo.py\&quot;,         \&quot;type\&quot;: \&quot;commit_file\&quot;,         \&quot;links\&quot;: {           \&quot;self\&quot;: {             \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/my-workspace/demo/src/ad6964b5fe2880dbd9ddcad1c89000f1dbcbc24b/src/foo.py\&quot;           }         }       }     }   ] } &#x60;&#x60;&#x60;  Note that searches can match in the file&#39;s text (&#x60;content_matches&#x60;), the path (&#x60;path_matches&#x60;), or both as in the example above.  You can use the same syntax for the search query as in the UI, e.g. to only search within a specific repository:  &#x60;&#x60;&#x60; curl &#39;https://api.bitbucket.org/2.0/teams/team_name/search/code?search_query&#x3D;foo+repo:demo&#39; # results from the \&quot;demo\&quot; repository &#x60;&#x60;&#x60;  Similar to other APIs, you can request more fields using a &#x60;fields&#x60; query parameter. E.g. to get some more information about the repository of matched files (the &#x60;%2B&#x60; is a URL-encoded &#x60;+&#x60;):  &#x60;&#x60;&#x60; curl &#39;https://api.bitbucket.org/2.0/teams/team_name/search/code&#39;\\      &#39;?search_query&#x3D;foo&amp;fields&#x3D;%2Bvalues.file.commit.repository&#39; {   \&quot;size\&quot;: 1,   \&quot;page\&quot;: 1,   \&quot;pagelen\&quot;: 10,   \&quot;query_substituted\&quot;: false,   \&quot;values\&quot;: [     {       \&quot;type\&quot;: \&quot;code_search_result\&quot;,       \&quot;content_match_count\&quot;: 1,       \&quot;content_matches\&quot;: [...],       \&quot;path_matches\&quot;: [...],       \&quot;file\&quot;: {         \&quot;commit\&quot;: {           \&quot;type\&quot;: \&quot;commit\&quot;,           \&quot;hash\&quot;: \&quot;ad6964b5fe2880dbd9ddcad1c89000f1dbcbc24b\&quot;,           \&quot;links\&quot;: {             \&quot;self\&quot;: {               \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/my-workspace/demo/commit/ad6964b5fe2880dbd9ddcad1c89000f1dbcbc24b\&quot;             },             \&quot;html\&quot;: {               \&quot;href\&quot;: \&quot;https://bitbucket.org/my-workspace/demo/commits/ad6964b5fe2880dbd9ddcad1c89000f1dbcbc24b\&quot;             }           },           \&quot;repository\&quot;: {             \&quot;name\&quot;: \&quot;demo\&quot;,             \&quot;type\&quot;: \&quot;repository\&quot;,             \&quot;full_name\&quot;: \&quot;my-workspace/demo\&quot;,             \&quot;links\&quot;: {               \&quot;self\&quot;: {                 \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/my-workspace/demo\&quot;               },               \&quot;html\&quot;: {                 \&quot;href\&quot;: \&quot;https://bitbucket.org/my-workspace/demo\&quot;               },               \&quot;avatar\&quot;: {                 \&quot;href\&quot;: \&quot;https://bytebucket.org/ravatar/%7B850e1749-781a-4115-9316-df39d0600e7a%7D?ts&#x3D;default\&quot;               }             },             \&quot;uuid\&quot;: \&quot;{850e1749-781a-4115-9316-df39d0600e7a}\&quot;           }         },         \&quot;type\&quot;: \&quot;commit_file\&quot;,         \&quot;links\&quot;: {           \&quot;self\&quot;: {             \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/my-workspace/demo/src/ad6964b5fe2880dbd9ddcad1c89000f1dbcbc24b/src/foo.py\&quot;           }         },         \&quot;path\&quot;: \&quot;src/foo.py\&quot;       }     }   ] } &#x60;&#x60;&#x60;  Try &#x60;fields&#x3D;%2Bvalues.*.*.*.*&#x60; to get an idea what&#39;s possible. 

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.SearchApi();
let username = "username_example"; // String | The account to search in; either the username or the UUID in curly braces
let searchQuery = "searchQuery_example"; // String | The search query
let opts = {
  'page': 1, // Number | Which page of the search results to retrieve
  'pagelen': 10 // Number | How many search results to retrieve per page
};
apiInstance.searchTeam(username, searchQuery, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **String**| The account to search in; either the username or the UUID in curly braces | 
 **searchQuery** | **String**| The search query | 
 **page** | **Number**| Which page of the search results to retrieve | [optional] [default to 1]
 **pagelen** | **Number**| How many search results to retrieve per page | [optional] [default to 10]

### Return type

[**SearchResultPage**](SearchResultPage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## searchWorkspace

> SearchResultPage searchWorkspace(workspace, searchQuery, opts)

Search for code in a workspace

Search for code in the repositories of the specified workspace.  Searching across all repositories:  &#x60;&#x60;&#x60; curl &#39;https://api.bitbucket.org/2.0/workspaces/workspace_slug_or_uuid/search/code?search_query&#x3D;foo&#39; {   \&quot;size\&quot;: 1,   \&quot;page\&quot;: 1,   \&quot;pagelen\&quot;: 10,   \&quot;query_substituted\&quot;: false,   \&quot;values\&quot;: [     {       \&quot;type\&quot;: \&quot;code_search_result\&quot;,       \&quot;content_match_count\&quot;: 2,       \&quot;content_matches\&quot;: [         {           \&quot;lines\&quot;: [             {               \&quot;line\&quot;: 2,               \&quot;segments\&quot;: []             },             {               \&quot;line\&quot;: 3,               \&quot;segments\&quot;: [                 {                   \&quot;text\&quot;: \&quot;def \&quot;                 },                 {                   \&quot;text\&quot;: \&quot;foo\&quot;,                   \&quot;match\&quot;: true                 },                 {                   \&quot;text\&quot;: \&quot;():\&quot;                 }               ]             },             {               \&quot;line\&quot;: 4,               \&quot;segments\&quot;: [                 {                   \&quot;text\&quot;: \&quot;    print(\\\&quot;snek\\\&quot;)\&quot;                 }               ]             },             {               \&quot;line\&quot;: 5,               \&quot;segments\&quot;: []             }           ]         }       ],       \&quot;path_matches\&quot;: [         {           \&quot;text\&quot;: \&quot;src/\&quot;         },         {           \&quot;text\&quot;: \&quot;foo\&quot;,           \&quot;match\&quot;: true         },         {           \&quot;text\&quot;: \&quot;.py\&quot;         }       ],       \&quot;file\&quot;: {         \&quot;path\&quot;: \&quot;src/foo.py\&quot;,         \&quot;type\&quot;: \&quot;commit_file\&quot;,         \&quot;links\&quot;: {           \&quot;self\&quot;: {             \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/my-workspace/demo/src/ad6964b5fe2880dbd9ddcad1c89000f1dbcbc24b/src/foo.py\&quot;           }         }       }     }   ] } &#x60;&#x60;&#x60;  Note that searches can match in the file&#39;s text (&#x60;content_matches&#x60;), the path (&#x60;path_matches&#x60;), or both as in the example above.  You can use the same syntax for the search query as in the UI, e.g. to only search within a specific repository:  &#x60;&#x60;&#x60; curl &#39;https://api.bitbucket.org/2.0/workspaces/my-workspace/search/code?search_query&#x3D;foo+repo:demo&#39; # results from the \&quot;demo\&quot; repository &#x60;&#x60;&#x60;  Similar to other APIs, you can request more fields using a &#x60;fields&#x60; query parameter. E.g. to get some more information about the repository of matched files (the &#x60;%2B&#x60; is a URL-encoded &#x60;+&#x60;):  &#x60;&#x60;&#x60; curl &#39;https://api.bitbucket.org/2.0/workspaces/my-workspace/search/code&#39;\\      &#39;?search_query&#x3D;foo&amp;fields&#x3D;%2Bvalues.file.commit.repository&#39; {   \&quot;size\&quot;: 1,   \&quot;page\&quot;: 1,   \&quot;pagelen\&quot;: 10,   \&quot;query_substituted\&quot;: false,   \&quot;values\&quot;: [     {       \&quot;type\&quot;: \&quot;code_search_result\&quot;,       \&quot;content_match_count\&quot;: 1,       \&quot;content_matches\&quot;: [...],       \&quot;path_matches\&quot;: [...],       \&quot;file\&quot;: {         \&quot;commit\&quot;: {           \&quot;type\&quot;: \&quot;commit\&quot;,           \&quot;hash\&quot;: \&quot;ad6964b5fe2880dbd9ddcad1c89000f1dbcbc24b\&quot;,           \&quot;links\&quot;: {             \&quot;self\&quot;: {               \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/my-workspace/demo/commit/ad6964b5fe2880dbd9ddcad1c89000f1dbcbc24b\&quot;             },             \&quot;html\&quot;: {               \&quot;href\&quot;: \&quot;https://bitbucket.org/my-workspace/demo/commits/ad6964b5fe2880dbd9ddcad1c89000f1dbcbc24b\&quot;             }           },           \&quot;repository\&quot;: {             \&quot;name\&quot;: \&quot;demo\&quot;,             \&quot;type\&quot;: \&quot;repository\&quot;,             \&quot;full_name\&quot;: \&quot;my-workspace/demo\&quot;,             \&quot;links\&quot;: {               \&quot;self\&quot;: {                 \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/my-workspace/demo\&quot;               },               \&quot;html\&quot;: {                 \&quot;href\&quot;: \&quot;https://bitbucket.org/my-workspace/demo\&quot;               },               \&quot;avatar\&quot;: {                 \&quot;href\&quot;: \&quot;https://bytebucket.org/ravatar/%7B850e1749-781a-4115-9316-df39d0600e7a%7D?ts&#x3D;default\&quot;               }             },             \&quot;uuid\&quot;: \&quot;{850e1749-781a-4115-9316-df39d0600e7a}\&quot;           }         },         \&quot;type\&quot;: \&quot;commit_file\&quot;,         \&quot;links\&quot;: {           \&quot;self\&quot;: {             \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/my-workspace/demo/src/ad6964b5fe2880dbd9ddcad1c89000f1dbcbc24b/src/foo.py\&quot;           }         },         \&quot;path\&quot;: \&quot;src/foo.py\&quot;       }     }   ] } &#x60;&#x60;&#x60;  Try &#x60;fields&#x3D;%2Bvalues.*.*.*.*&#x60; to get an idea what&#39;s possible. 

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.SearchApi();
let workspace = "workspace_example"; // String | The workspace to search in; either the slug or the UUID in curly braces
let searchQuery = "searchQuery_example"; // String | The search query
let opts = {
  'page': 1, // Number | Which page of the search results to retrieve
  'pagelen': 10 // Number | How many search results to retrieve per page
};
apiInstance.searchWorkspace(workspace, searchQuery, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **String**| The workspace to search in; either the slug or the UUID in curly braces | 
 **searchQuery** | **String**| The search query | 
 **page** | **Number**| Which page of the search results to retrieve | [optional] [default to 1]
 **pagelen** | **Number**| How many search results to retrieve per page | [optional] [default to 10]

### Return type

[**SearchResultPage**](SearchResultPage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

