# BitbucketApi.PullrequestsApi

All URIs are relative to *https://api.bitbucket.org/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getPullrequestsForCommit**](PullrequestsApi.md#getPullrequestsForCommit) | **GET** /repositories/{workspace}/{repo_slug}/commit/{commit}/pullrequests | List pull requests that contain a commit
[**pullrequestsSelectedUserGet**](PullrequestsApi.md#pullrequestsSelectedUserGet) | **GET** /pullrequests/{selected_user} | List pull requests for a user
[**repositoriesWorkspaceRepoSlugDefaultReviewersGet**](PullrequestsApi.md#repositoriesWorkspaceRepoSlugDefaultReviewersGet) | **GET** /repositories/{workspace}/{repo_slug}/default-reviewers | List default reviewers
[**repositoriesWorkspaceRepoSlugDefaultReviewersTargetUsernameDelete**](PullrequestsApi.md#repositoriesWorkspaceRepoSlugDefaultReviewersTargetUsernameDelete) | **DELETE** /repositories/{workspace}/{repo_slug}/default-reviewers/{target_username} | Remove a user from the default reviewers
[**repositoriesWorkspaceRepoSlugDefaultReviewersTargetUsernameGet**](PullrequestsApi.md#repositoriesWorkspaceRepoSlugDefaultReviewersTargetUsernameGet) | **GET** /repositories/{workspace}/{repo_slug}/default-reviewers/{target_username} | Get a default reviewer
[**repositoriesWorkspaceRepoSlugDefaultReviewersTargetUsernamePut**](PullrequestsApi.md#repositoriesWorkspaceRepoSlugDefaultReviewersTargetUsernamePut) | **PUT** /repositories/{workspace}/{repo_slug}/default-reviewers/{target_username} | Add a user to the default reviewers
[**repositoriesWorkspaceRepoSlugEffectiveDefaultReviewersGet**](PullrequestsApi.md#repositoriesWorkspaceRepoSlugEffectiveDefaultReviewersGet) | **GET** /repositories/{workspace}/{repo_slug}/effective-default-reviewers | List effective default reviewers
[**repositoriesWorkspaceRepoSlugPullrequestsActivityGet**](PullrequestsApi.md#repositoriesWorkspaceRepoSlugPullrequestsActivityGet) | **GET** /repositories/{workspace}/{repo_slug}/pullrequests/activity | List a pull request activity log
[**repositoriesWorkspaceRepoSlugPullrequestsGet**](PullrequestsApi.md#repositoriesWorkspaceRepoSlugPullrequestsGet) | **GET** /repositories/{workspace}/{repo_slug}/pullrequests | List pull requests
[**repositoriesWorkspaceRepoSlugPullrequestsPost**](PullrequestsApi.md#repositoriesWorkspaceRepoSlugPullrequestsPost) | **POST** /repositories/{workspace}/{repo_slug}/pullrequests | Create a pull request
[**repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdActivityGet**](PullrequestsApi.md#repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdActivityGet) | **GET** /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/activity | List a pull request activity log
[**repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdApproveDelete**](PullrequestsApi.md#repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdApproveDelete) | **DELETE** /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/approve | Unapprove a pull request
[**repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdApprovePost**](PullrequestsApi.md#repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdApprovePost) | **POST** /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/approve | Approve a pull request
[**repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdCommentsCommentIdDelete**](PullrequestsApi.md#repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdCommentsCommentIdDelete) | **DELETE** /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/comments/{comment_id} | Delete a comment on a pull request
[**repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdCommentsCommentIdGet**](PullrequestsApi.md#repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdCommentsCommentIdGet) | **GET** /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/comments/{comment_id} | Get a comment on a pull request
[**repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdCommentsCommentIdPut**](PullrequestsApi.md#repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdCommentsCommentIdPut) | **PUT** /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/comments/{comment_id} | Update a comment on a pull request
[**repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdCommentsCommentIdResolveDelete**](PullrequestsApi.md#repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdCommentsCommentIdResolveDelete) | **DELETE** /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/comments/{comment_id}/resolve | Reopen a comment thread
[**repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdCommentsCommentIdResolvePost**](PullrequestsApi.md#repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdCommentsCommentIdResolvePost) | **POST** /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/comments/{comment_id}/resolve | Resolve a comment thread
[**repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdCommentsGet**](PullrequestsApi.md#repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdCommentsGet) | **GET** /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/comments | List comments on a pull request
[**repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdCommentsPost**](PullrequestsApi.md#repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdCommentsPost) | **POST** /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/comments | Create a comment on a pull request
[**repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdCommitsGet**](PullrequestsApi.md#repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdCommitsGet) | **GET** /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/commits | List commits on a pull request
[**repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdDeclinePost**](PullrequestsApi.md#repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdDeclinePost) | **POST** /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/decline | Decline a pull request
[**repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdDiffGet**](PullrequestsApi.md#repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdDiffGet) | **GET** /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/diff | List changes in a pull request
[**repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdDiffstatGet**](PullrequestsApi.md#repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdDiffstatGet) | **GET** /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/diffstat | Get the diff stat for a pull request
[**repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdGet**](PullrequestsApi.md#repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdGet) | **GET** /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id} | Get a pull request
[**repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdMergePost**](PullrequestsApi.md#repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdMergePost) | **POST** /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/merge | Merge a pull request
[**repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdMergeTaskStatusTaskIdGet**](PullrequestsApi.md#repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdMergeTaskStatusTaskIdGet) | **GET** /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/merge/task-status/{task_id} | Get the merge task status for a pull request
[**repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdPatchGet**](PullrequestsApi.md#repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdPatchGet) | **GET** /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/patch | Get the patch for a pull request
[**repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdPut**](PullrequestsApi.md#repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdPut) | **PUT** /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id} | Update a pull request
[**repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdRequestChangesDelete**](PullrequestsApi.md#repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdRequestChangesDelete) | **DELETE** /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/request-changes | Remove change request for a pull request
[**repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdRequestChangesPost**](PullrequestsApi.md#repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdRequestChangesPost) | **POST** /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/request-changes | Request changes for a pull request
[**repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdStatusesGet**](PullrequestsApi.md#repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdStatusesGet) | **GET** /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/statuses | List commit statuses for a pull request



## getPullrequestsForCommit

> PaginatedPullrequests getPullrequestsForCommit(workspace, repoSlug, commit, opts)

List pull requests that contain a commit

Returns a paginated list of all pull requests as part of which this commit was reviewed. Pull Request Commit Links app must be installed first before using this API; installation automatically occurs when &#39;Go to pull request&#39; is clicked from the web interface for a commit&#39;s details.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PullrequestsApi();
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces
let repoSlug = "repoSlug_example"; // String | The repository; either the UUID in curly braces, or the slug
let commit = "commit_example"; // String | The SHA1 of the commit
let opts = {
  'page': 1, // Number | Which page to retrieve
  'pagelen': 30 // Number | How many pull requests to retrieve per page
};
apiInstance.getPullrequestsForCommit(workspace, repoSlug, commit, opts, (error, data, response) => {
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
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces | 
 **repoSlug** | **String**| The repository; either the UUID in curly braces, or the slug | 
 **commit** | **String**| The SHA1 of the commit | 
 **page** | **Number**| Which page to retrieve | [optional] [default to 1]
 **pagelen** | **Number**| How many pull requests to retrieve per page | [optional] [default to 30]

### Return type

[**PaginatedPullrequests**](PaginatedPullrequests.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## pullrequestsSelectedUserGet

> PaginatedPullrequests pullrequestsSelectedUserGet(selectedUser, opts)

List pull requests for a user

Returns all pull requests authored by the specified user.  By default only open pull requests are returned. This can be controlled using the &#x60;state&#x60; query parameter. To retrieve pull requests that are in one of multiple states, repeat the &#x60;state&#x60; parameter for each individual state.  This endpoint also supports filtering and sorting of the results. See [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering) for more details.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';
let defaultClient = BitbucketApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BitbucketApi.PullrequestsApi();
let selectedUser = "selectedUser_example"; // String | This can either be the username of the pull request author, the author's UUID surrounded by curly-braces, for example: `{account UUID}`, or the author's Atlassian ID. 
let opts = {
  'state': "state_example" // String | Only return pull requests that are in this state. This parameter can be repeated.
};
apiInstance.pullrequestsSelectedUserGet(selectedUser, opts, (error, data, response) => {
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
 **selectedUser** | **String**| This can either be the username of the pull request author, the author&#39;s UUID surrounded by curly-braces, for example: &#x60;{account UUID}&#x60;, or the author&#39;s Atlassian ID.  | 
 **state** | **String**| Only return pull requests that are in this state. This parameter can be repeated. | [optional] 

### Return type

[**PaginatedPullrequests**](PaginatedPullrequests.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## repositoriesWorkspaceRepoSlugDefaultReviewersGet

> PaginatedAccounts repositoriesWorkspaceRepoSlugDefaultReviewersGet(repoSlug, workspace)

List default reviewers

Returns the repository&#39;s default reviewers.  These are the users that are automatically added as reviewers on every new pull request that is created. To obtain the repository&#39;s default reviewers as well as the default reviewers inherited from the project, use the [effective-default-reveiwers](#api-repositories-workspace-repo-slug-effective-default-reviewers-get) endpoint.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';
let defaultClient = BitbucketApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BitbucketApi.PullrequestsApi();
let repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
apiInstance.repositoriesWorkspaceRepoSlugDefaultReviewersGet(repoSlug, workspace, (error, data, response) => {
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
 **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | 

### Return type

[**PaginatedAccounts**](PaginatedAccounts.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## repositoriesWorkspaceRepoSlugDefaultReviewersTargetUsernameDelete

> repositoriesWorkspaceRepoSlugDefaultReviewersTargetUsernameDelete(repoSlug, targetUsername, workspace)

Remove a user from the default reviewers

Removes a default reviewer from the repository.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';
let defaultClient = BitbucketApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BitbucketApi.PullrequestsApi();
let repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
let targetUsername = "targetUsername_example"; // String | This can either be the username or the UUID of the default reviewer, surrounded by curly-braces, for example: `{account UUID}`. 
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
apiInstance.repositoriesWorkspaceRepoSlugDefaultReviewersTargetUsernameDelete(repoSlug, targetUsername, workspace, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 
 **targetUsername** | **String**| This can either be the username or the UUID of the default reviewer, surrounded by curly-braces, for example: &#x60;{account UUID}&#x60;.  | 
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## repositoriesWorkspaceRepoSlugDefaultReviewersTargetUsernameGet

> Account repositoriesWorkspaceRepoSlugDefaultReviewersTargetUsernameGet(repoSlug, targetUsername, workspace)

Get a default reviewer

Returns the specified reviewer.  This can be used to test whether a user is among the repository&#39;s default reviewers list. A 404 indicates that that specified user is not a default reviewer.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';
let defaultClient = BitbucketApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BitbucketApi.PullrequestsApi();
let repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
let targetUsername = "targetUsername_example"; // String | This can either be the username or the UUID of the default reviewer, surrounded by curly-braces, for example: `{account UUID}`. 
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
apiInstance.repositoriesWorkspaceRepoSlugDefaultReviewersTargetUsernameGet(repoSlug, targetUsername, workspace, (error, data, response) => {
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
 **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 
 **targetUsername** | **String**| This can either be the username or the UUID of the default reviewer, surrounded by curly-braces, for example: &#x60;{account UUID}&#x60;.  | 
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | 

### Return type

[**Account**](Account.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## repositoriesWorkspaceRepoSlugDefaultReviewersTargetUsernamePut

> Account repositoriesWorkspaceRepoSlugDefaultReviewersTargetUsernamePut(repoSlug, targetUsername, workspace)

Add a user to the default reviewers

Adds the specified user to the repository&#39;s list of default reviewers.  This method is idempotent. Adding a user a second time has no effect.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';
let defaultClient = BitbucketApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BitbucketApi.PullrequestsApi();
let repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
let targetUsername = "targetUsername_example"; // String | This can either be the username or the UUID of the default reviewer, surrounded by curly-braces, for example: `{account UUID}`. 
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
apiInstance.repositoriesWorkspaceRepoSlugDefaultReviewersTargetUsernamePut(repoSlug, targetUsername, workspace, (error, data, response) => {
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
 **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 
 **targetUsername** | **String**| This can either be the username or the UUID of the default reviewer, surrounded by curly-braces, for example: &#x60;{account UUID}&#x60;.  | 
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | 

### Return type

[**Account**](Account.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## repositoriesWorkspaceRepoSlugEffectiveDefaultReviewersGet

> PaginatedDefaultReviewerAndType repositoriesWorkspaceRepoSlugEffectiveDefaultReviewersGet(repoSlug, workspace)

List effective default reviewers

Returns the repository&#39;s effective default reviewers. This includes both default reviewers defined at the repository level as well as those inherited from its project.  These are the users that are automatically added as reviewers on every new pull request that is created.  &#x60;&#x60;&#x60; $ curl https://api.bitbucket.org/2.0/repositories/{workspace_slug}/{repo_slug}/effective-default-reviewers?page&#x3D;1&amp;pagelen&#x3D;20 {     \&quot;pagelen\&quot;: 20,     \&quot;values\&quot;: [         {             \&quot;user\&quot;: {                 \&quot;display_name\&quot;: \&quot;Patrick Wolf\&quot;,                 \&quot;uuid\&quot;: \&quot;{9565301a-a3cf-4b5d-88f4-dd6af8078d7e}\&quot;             },             \&quot;reviewer_type\&quot;: \&quot;project\&quot;,             \&quot;type\&quot;: \&quot;default_reviewer\&quot;,         },         {             \&quot;user\&quot;: {                 \&quot;display_name\&quot;: \&quot;Davis Lee\&quot;,                 \&quot;uuid\&quot;: \&quot;{f0e0e8e9-66c1-4b85-a784-44a9eb9ef1a6}\&quot;             },             \&quot;reviewer_type\&quot;: \&quot;repository\&quot;,             \&quot;type\&quot;: \&quot;default_reviewer\&quot;,         }     ],     \&quot;page\&quot;: 1,     \&quot;size\&quot;: 2 } &#x60;&#x60;&#x60;

### Example

```javascript
import BitbucketApi from 'bitbucket_api';
let defaultClient = BitbucketApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BitbucketApi.PullrequestsApi();
let repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
apiInstance.repositoriesWorkspaceRepoSlugEffectiveDefaultReviewersGet(repoSlug, workspace, (error, data, response) => {
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
 **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | 

### Return type

[**PaginatedDefaultReviewerAndType**](PaginatedDefaultReviewerAndType.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## repositoriesWorkspaceRepoSlugPullrequestsActivityGet

> repositoriesWorkspaceRepoSlugPullrequestsActivityGet(repoSlug, workspace)

List a pull request activity log

Returns a paginated list of the pull request&#39;s activity log.  This handler serves both a v20 and internal endpoint. The v20 endpoint returns reviewer comments, updates, approvals and request changes. The internal endpoint includes those plus tasks and attachments.  Comments created on a file or a line of code have an inline property.  Comment example: &#x60;&#x60;&#x60; {     \&quot;pagelen\&quot;: 20,     \&quot;values\&quot;: [         {             \&quot;comment\&quot;: {                 \&quot;links\&quot;: {                     \&quot;self\&quot;: {                         \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2/pullrequests/5695/comments/118571088\&quot;                     },                     \&quot;html\&quot;: {                         \&quot;href\&quot;: \&quot;https://bitbucket.org/atlassian/atlaskit-mk-2/pull-requests/5695/_/diff#comment-118571088\&quot;                     }                 },                 \&quot;deleted\&quot;: false,                 \&quot;pullrequest\&quot;: {                     \&quot;type\&quot;: \&quot;pullrequest\&quot;,                     \&quot;id\&quot;: 5695,                     \&quot;links\&quot;: {                         \&quot;self\&quot;: {                             \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2/pullrequests/5695\&quot;                         },                         \&quot;html\&quot;: {                             \&quot;href\&quot;: \&quot;https://bitbucket.org/atlassian/atlaskit-mk-2/pull-requests/5695\&quot;                         }                     },                     \&quot;title\&quot;: \&quot;username/NONE: small change from onFocus to onClick to handle tabbing through the page and not expand the editor unless a click event triggers it\&quot;                 },                 \&quot;content\&quot;: {                     \&quot;raw\&quot;: \&quot;inline with to a dn from lines\&quot;,                     \&quot;markup\&quot;: \&quot;markdown\&quot;,                     \&quot;html\&quot;: \&quot;&lt;p&gt;inline with to a dn from lines&lt;/p&gt;\&quot;,                     \&quot;type\&quot;: \&quot;rendered\&quot;                 },                 \&quot;created_on\&quot;: \&quot;2019-09-27T00:33:46.039178+00:00\&quot;,                 \&quot;user\&quot;: {                     \&quot;display_name\&quot;: \&quot;Name Lastname\&quot;,                     \&quot;uuid\&quot;: \&quot;{}\&quot;,                     \&quot;links\&quot;: {                         \&quot;self\&quot;: {                             \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/users/%7B%7D\&quot;                         },                         \&quot;html\&quot;: {                             \&quot;href\&quot;: \&quot;https://bitbucket.org/%7B%7D/\&quot;                         },                         \&quot;avatar\&quot;: {                             \&quot;href\&quot;: \&quot;https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/:/128\&quot;                         }                     },                     \&quot;type\&quot;: \&quot;user\&quot;,                     \&quot;nickname\&quot;: \&quot;Name\&quot;,                     \&quot;account_id\&quot;: \&quot;\&quot;                 },                 \&quot;created_on\&quot;: \&quot;2019-09-27T00:33:46.039178+00:00\&quot;,                 \&quot;user\&quot;: {                     \&quot;display_name\&quot;: \&quot;Name Lastname\&quot;,                     \&quot;uuid\&quot;: \&quot;{}\&quot;,                     \&quot;links\&quot;: {                         \&quot;self\&quot;: {                             \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/users/%7B%7D\&quot;                         },                         \&quot;html\&quot;: {                             \&quot;href\&quot;: \&quot;https://bitbucket.org/%7B%7D/\&quot;                         },                         \&quot;avatar\&quot;: {                             \&quot;href\&quot;: \&quot;https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/:/128\&quot;                         }                     },                     \&quot;type\&quot;: \&quot;user\&quot;,                     \&quot;nickname\&quot;: \&quot;Name\&quot;,                     \&quot;account_id\&quot;: \&quot;\&quot;                 },                 \&quot;updated_on\&quot;: \&quot;2019-09-27T00:33:46.055384+00:00\&quot;,                 \&quot;inline\&quot;: {                     \&quot;context_lines\&quot;: \&quot;\&quot;,                     \&quot;to\&quot;: null,                     \&quot;path\&quot;: \&quot;\&quot;,                     \&quot;outdated\&quot;: false,                     \&quot;from\&quot;: 211                 },                 \&quot;type\&quot;: \&quot;pullrequest_comment\&quot;,                 \&quot;id\&quot;: 118571088             },             \&quot;pull_request\&quot;: {                 \&quot;type\&quot;: \&quot;pullrequest\&quot;,                 \&quot;id\&quot;: 5695,                 \&quot;links\&quot;: {                     \&quot;self\&quot;: {                         \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2/pullrequests/5695\&quot;                     },                     \&quot;html\&quot;: {                         \&quot;href\&quot;: \&quot;https://bitbucket.org/atlassian/atlaskit-mk-2/pull-requests/5695\&quot;                     }                 },                 \&quot;title\&quot;: \&quot;username/NONE: small change from onFocus to onClick to handle tabbing through the page and not expand the editor unless a click event triggers it\&quot;             }         }     ] } &#x60;&#x60;&#x60;  Updates include a state property of OPEN, MERGED, or DECLINED.  Update example: &#x60;&#x60;&#x60; {     \&quot;pagelen\&quot;: 20,     \&quot;values\&quot;: [         {             \&quot;update\&quot;: {                 \&quot;description\&quot;: \&quot;\&quot;,                 \&quot;title\&quot;: \&quot;username/NONE: small change from onFocus to onClick to handle tabbing through the page and not expand the editor unless a click event triggers it\&quot;,                 \&quot;destination\&quot;: {                     \&quot;commit\&quot;: {                         \&quot;type\&quot;: \&quot;commit\&quot;,                         \&quot;hash\&quot;: \&quot;6a2c16e4a152\&quot;,                         \&quot;links\&quot;: {                             \&quot;self\&quot;: {                                 \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2/commit/6a2c16e4a152\&quot;                             },                             \&quot;html\&quot;: {                                 \&quot;href\&quot;: \&quot;https://bitbucket.org/atlassian/atlaskit-mk-2/commits/6a2c16e4a152\&quot;                             }                         }                     },                     \&quot;branch\&quot;: {                         \&quot;name\&quot;: \&quot;master\&quot;                     },                     \&quot;repository\&quot;: {                         \&quot;name\&quot;: \&quot;Atlaskit-MK-2\&quot;,                         \&quot;type\&quot;: \&quot;repository\&quot;,                         \&quot;full_name\&quot;: \&quot;atlassian/atlaskit-mk-2\&quot;,                         \&quot;links\&quot;: {                             \&quot;self\&quot;: {                                 \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2\&quot;                             },                             \&quot;html\&quot;: {                                 \&quot;href\&quot;: \&quot;https://bitbucket.org/atlassian/atlaskit-mk-2\&quot;                             },                             \&quot;avatar\&quot;: {                                 \&quot;href\&quot;: \&quot;https://bytebucket.org/ravatar/%7B%7D?ts&#x3D;js\&quot;                             }                         },                         \&quot;uuid\&quot;: \&quot;{}\&quot;                     }                 },                 \&quot;reason\&quot;: \&quot;\&quot;,                 \&quot;source\&quot;: {                     \&quot;commit\&quot;: {                         \&quot;type\&quot;: \&quot;commit\&quot;,                         \&quot;hash\&quot;: \&quot;728c8bad1813\&quot;,                         \&quot;links\&quot;: {                             \&quot;self\&quot;: {                                 \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2/commit/728c8bad1813\&quot;                             },                             \&quot;html\&quot;: {                                 \&quot;href\&quot;: \&quot;https://bitbucket.org/atlassian/atlaskit-mk-2/commits/728c8bad1813\&quot;                             }                         }                     },                     \&quot;branch\&quot;: {                         \&quot;name\&quot;: \&quot;username/NONE-add-onClick-prop-for-accessibility\&quot;                     },                     \&quot;repository\&quot;: {                         \&quot;name\&quot;: \&quot;Atlaskit-MK-2\&quot;,                         \&quot;type\&quot;: \&quot;repository\&quot;,                         \&quot;full_name\&quot;: \&quot;atlassian/atlaskit-mk-2\&quot;,                         \&quot;links\&quot;: {                             \&quot;self\&quot;: {                                 \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2\&quot;                             },                             \&quot;html\&quot;: {                                 \&quot;href\&quot;: \&quot;https://bitbucket.org/atlassian/atlaskit-mk-2\&quot;                             },                             \&quot;avatar\&quot;: {                                 \&quot;href\&quot;: \&quot;https://bytebucket.org/ravatar/%7B%7D?ts&#x3D;js\&quot;                             }                         },                         \&quot;uuid\&quot;: \&quot;{}\&quot;                     }                 },                 \&quot;state\&quot;: \&quot;OPEN\&quot;,                 \&quot;author\&quot;: {                     \&quot;display_name\&quot;: \&quot;Name Lastname\&quot;,                     \&quot;uuid\&quot;: \&quot;{}\&quot;,                     \&quot;links\&quot;: {                         \&quot;self\&quot;: {                             \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/users/%7B%7D\&quot;                         },                         \&quot;html\&quot;: {                             \&quot;href\&quot;: \&quot;https://bitbucket.org/%7B%7D/\&quot;                         },                         \&quot;avatar\&quot;: {                             \&quot;href\&quot;: \&quot;https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/:/128\&quot;                         }                     },                     \&quot;type\&quot;: \&quot;user\&quot;,                     \&quot;nickname\&quot;: \&quot;Name\&quot;,                     \&quot;account_id\&quot;: \&quot;\&quot;                 },                 \&quot;date\&quot;: \&quot;2019-05-10T06:48:25.305565+00:00\&quot;             },             \&quot;pull_request\&quot;: {                 \&quot;type\&quot;: \&quot;pullrequest\&quot;,                 \&quot;id\&quot;: 5695,                 \&quot;links\&quot;: {                     \&quot;self\&quot;: {                         \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2/pullrequests/5695\&quot;                     },                     \&quot;html\&quot;: {                         \&quot;href\&quot;: \&quot;https://bitbucket.org/atlassian/atlaskit-mk-2/pull-requests/5695\&quot;                     }                 },                 \&quot;title\&quot;: \&quot;username/NONE: small change from onFocus to onClick to handle tabbing through the page and not expand the editor unless a click event triggers it\&quot;             }         }     ] } &#x60;&#x60;&#x60;  Approval example: &#x60;&#x60;&#x60; {     \&quot;pagelen\&quot;: 20,     \&quot;values\&quot;: [         {             \&quot;approval\&quot;: {                 \&quot;date\&quot;: \&quot;2019-09-27T00:37:19.849534+00:00\&quot;,                 \&quot;pullrequest\&quot;: {                     \&quot;type\&quot;: \&quot;pullrequest\&quot;,                     \&quot;id\&quot;: 5695,                     \&quot;links\&quot;: {                         \&quot;self\&quot;: {                             \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2/pullrequests/5695\&quot;                         },                         \&quot;html\&quot;: {                             \&quot;href\&quot;: \&quot;https://bitbucket.org/atlassian/atlaskit-mk-2/pull-requests/5695\&quot;                         }                     },                     \&quot;title\&quot;: \&quot;username/NONE: small change from onFocus to onClick to handle tabbing through the page and not expand the editor unless a click event triggers it\&quot;                 },                 \&quot;user\&quot;: {                     \&quot;display_name\&quot;: \&quot;Name Lastname\&quot;,                     \&quot;uuid\&quot;: \&quot;{}\&quot;,                     \&quot;links\&quot;: {                         \&quot;self\&quot;: {                             \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/users/%7B%7D\&quot;                         },                         \&quot;html\&quot;: {                             \&quot;href\&quot;: \&quot;https://bitbucket.org/%7B%7D/\&quot;                         },                         \&quot;avatar\&quot;: {                             \&quot;href\&quot;: \&quot;https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/:/128\&quot;                         }                     },                     \&quot;type\&quot;: \&quot;user\&quot;,                     \&quot;nickname\&quot;: \&quot;Name\&quot;,                     \&quot;account_id\&quot;: \&quot;\&quot;                 }             },             \&quot;pull_request\&quot;: {                 \&quot;type\&quot;: \&quot;pullrequest\&quot;,                 \&quot;id\&quot;: 5695,                 \&quot;links\&quot;: {                     \&quot;self\&quot;: {                         \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2/pullrequests/5695\&quot;                     },                     \&quot;html\&quot;: {                         \&quot;href\&quot;: \&quot;https://bitbucket.org/atlassian/atlaskit-mk-2/pull-requests/5695\&quot;                     }                 },                 \&quot;title\&quot;: \&quot;username/NONE: small change from onFocus to onClick to handle tabbing through the page and not expand the editor unless a click event triggers it\&quot;             }         }     ] } &#x60;&#x60;&#x60;

### Example

```javascript
import BitbucketApi from 'bitbucket_api';
let defaultClient = BitbucketApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BitbucketApi.PullrequestsApi();
let repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
apiInstance.repositoriesWorkspaceRepoSlugPullrequestsActivityGet(repoSlug, workspace, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## repositoriesWorkspaceRepoSlugPullrequestsGet

> PaginatedPullrequests repositoriesWorkspaceRepoSlugPullrequestsGet(repoSlug, workspace, opts)

List pull requests

Returns all pull requests on the specified repository.  By default only open pull requests are returned. This can be controlled using the &#x60;state&#x60; query parameter. To retrieve pull requests that are in one of multiple states, repeat the &#x60;state&#x60; parameter for each individual state.  This endpoint also supports filtering and sorting of the results. See [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering) for more details.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';
let defaultClient = BitbucketApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BitbucketApi.PullrequestsApi();
let repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
let opts = {
  'state': "state_example" // String | Only return pull requests that are in this state. This parameter can be repeated.
};
apiInstance.repositoriesWorkspaceRepoSlugPullrequestsGet(repoSlug, workspace, opts, (error, data, response) => {
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
 **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | 
 **state** | **String**| Only return pull requests that are in this state. This parameter can be repeated. | [optional] 

### Return type

[**PaginatedPullrequests**](PaginatedPullrequests.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## repositoriesWorkspaceRepoSlugPullrequestsPost

> Pullrequest repositoriesWorkspaceRepoSlugPullrequestsPost(repoSlug, workspace, opts)

Create a pull request

Creates a new pull request where the destination repository is this repository and the author is the authenticated user.  The minimum required fields to create a pull request are &#x60;title&#x60; and &#x60;source&#x60;, specified by a branch name.  &#x60;&#x60;&#x60; curl https://api.bitbucket.org/2.0/repositories/my-workspace/my-repository/pullrequests \\     -u my-username:my-password \\     --request POST \\     --header &#39;Content-Type: application/json&#39; \\     --data &#39;{         \&quot;title\&quot;: \&quot;My Title\&quot;,         \&quot;source\&quot;: {             \&quot;branch\&quot;: {                 \&quot;name\&quot;: \&quot;staging\&quot;             }         }     }&#39; &#x60;&#x60;&#x60;  If the pull request&#39;s &#x60;destination&#x60; is not specified, it will default to the &#x60;repository.mainbranch&#x60;. To open a pull request to a different branch, say from a feature branch to a staging branch, specify a &#x60;destination&#x60; (same format as the &#x60;source&#x60;):  &#x60;&#x60;&#x60; {     \&quot;title\&quot;: \&quot;My Title\&quot;,     \&quot;source\&quot;: {         \&quot;branch\&quot;: {             \&quot;name\&quot;: \&quot;my-feature-branch\&quot;         }     },     \&quot;destination\&quot;: {         \&quot;branch\&quot;: {             \&quot;name\&quot;: \&quot;staging\&quot;         }     } } &#x60;&#x60;&#x60;  Reviewers can be specified by adding an array of user objects as the &#x60;reviewers&#x60; property.  &#x60;&#x60;&#x60; {     \&quot;title\&quot;: \&quot;My Title\&quot;,     \&quot;source\&quot;: {         \&quot;branch\&quot;: {             \&quot;name\&quot;: \&quot;my-feature-branch\&quot;         }     },     \&quot;reviewers\&quot;: [         {             \&quot;uuid\&quot;: \&quot;{504c3b62-8120-4f0c-a7bc-87800b9d6f70}\&quot;         }     ] } &#x60;&#x60;&#x60;  Other fields:  * &#x60;description&#x60; - a string * &#x60;close_source_branch&#x60; - boolean that specifies if the source branch should be closed upon merging

### Example

```javascript
import BitbucketApi from 'bitbucket_api';
let defaultClient = BitbucketApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BitbucketApi.PullrequestsApi();
let repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
let opts = {
  'pullrequest': new BitbucketApi.Pullrequest() // Pullrequest | The new pull request.  The request URL you POST to becomes the destination repository URL. For this reason, you must specify an explicit source repository in the request object if you want to pull from a different repository (fork).  Since not all elements are required or even mutable, you only need to include the elements you want to initialize, such as the source branch and the title.
};
apiInstance.repositoriesWorkspaceRepoSlugPullrequestsPost(repoSlug, workspace, opts, (error, data, response) => {
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
 **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | 
 **pullrequest** | [**Pullrequest**](Pullrequest.md)| The new pull request.  The request URL you POST to becomes the destination repository URL. For this reason, you must specify an explicit source repository in the request object if you want to pull from a different repository (fork).  Since not all elements are required or even mutable, you only need to include the elements you want to initialize, such as the source branch and the title. | [optional] 

### Return type

[**Pullrequest**](Pullrequest.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdActivityGet

> repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdActivityGet(pullRequestId, repoSlug, workspace)

List a pull request activity log

Returns a paginated list of the pull request&#39;s activity log.  This handler serves both a v20 and internal endpoint. The v20 endpoint returns reviewer comments, updates, approvals and request changes. The internal endpoint includes those plus tasks and attachments.  Comments created on a file or a line of code have an inline property.  Comment example: &#x60;&#x60;&#x60; {     \&quot;pagelen\&quot;: 20,     \&quot;values\&quot;: [         {             \&quot;comment\&quot;: {                 \&quot;links\&quot;: {                     \&quot;self\&quot;: {                         \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2/pullrequests/5695/comments/118571088\&quot;                     },                     \&quot;html\&quot;: {                         \&quot;href\&quot;: \&quot;https://bitbucket.org/atlassian/atlaskit-mk-2/pull-requests/5695/_/diff#comment-118571088\&quot;                     }                 },                 \&quot;deleted\&quot;: false,                 \&quot;pullrequest\&quot;: {                     \&quot;type\&quot;: \&quot;pullrequest\&quot;,                     \&quot;id\&quot;: 5695,                     \&quot;links\&quot;: {                         \&quot;self\&quot;: {                             \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2/pullrequests/5695\&quot;                         },                         \&quot;html\&quot;: {                             \&quot;href\&quot;: \&quot;https://bitbucket.org/atlassian/atlaskit-mk-2/pull-requests/5695\&quot;                         }                     },                     \&quot;title\&quot;: \&quot;username/NONE: small change from onFocus to onClick to handle tabbing through the page and not expand the editor unless a click event triggers it\&quot;                 },                 \&quot;content\&quot;: {                     \&quot;raw\&quot;: \&quot;inline with to a dn from lines\&quot;,                     \&quot;markup\&quot;: \&quot;markdown\&quot;,                     \&quot;html\&quot;: \&quot;&lt;p&gt;inline with to a dn from lines&lt;/p&gt;\&quot;,                     \&quot;type\&quot;: \&quot;rendered\&quot;                 },                 \&quot;created_on\&quot;: \&quot;2019-09-27T00:33:46.039178+00:00\&quot;,                 \&quot;user\&quot;: {                     \&quot;display_name\&quot;: \&quot;Name Lastname\&quot;,                     \&quot;uuid\&quot;: \&quot;{}\&quot;,                     \&quot;links\&quot;: {                         \&quot;self\&quot;: {                             \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/users/%7B%7D\&quot;                         },                         \&quot;html\&quot;: {                             \&quot;href\&quot;: \&quot;https://bitbucket.org/%7B%7D/\&quot;                         },                         \&quot;avatar\&quot;: {                             \&quot;href\&quot;: \&quot;https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/:/128\&quot;                         }                     },                     \&quot;type\&quot;: \&quot;user\&quot;,                     \&quot;nickname\&quot;: \&quot;Name\&quot;,                     \&quot;account_id\&quot;: \&quot;\&quot;                 },                 \&quot;created_on\&quot;: \&quot;2019-09-27T00:33:46.039178+00:00\&quot;,                 \&quot;user\&quot;: {                     \&quot;display_name\&quot;: \&quot;Name Lastname\&quot;,                     \&quot;uuid\&quot;: \&quot;{}\&quot;,                     \&quot;links\&quot;: {                         \&quot;self\&quot;: {                             \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/users/%7B%7D\&quot;                         },                         \&quot;html\&quot;: {                             \&quot;href\&quot;: \&quot;https://bitbucket.org/%7B%7D/\&quot;                         },                         \&quot;avatar\&quot;: {                             \&quot;href\&quot;: \&quot;https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/:/128\&quot;                         }                     },                     \&quot;type\&quot;: \&quot;user\&quot;,                     \&quot;nickname\&quot;: \&quot;Name\&quot;,                     \&quot;account_id\&quot;: \&quot;\&quot;                 },                 \&quot;updated_on\&quot;: \&quot;2019-09-27T00:33:46.055384+00:00\&quot;,                 \&quot;inline\&quot;: {                     \&quot;context_lines\&quot;: \&quot;\&quot;,                     \&quot;to\&quot;: null,                     \&quot;path\&quot;: \&quot;\&quot;,                     \&quot;outdated\&quot;: false,                     \&quot;from\&quot;: 211                 },                 \&quot;type\&quot;: \&quot;pullrequest_comment\&quot;,                 \&quot;id\&quot;: 118571088             },             \&quot;pull_request\&quot;: {                 \&quot;type\&quot;: \&quot;pullrequest\&quot;,                 \&quot;id\&quot;: 5695,                 \&quot;links\&quot;: {                     \&quot;self\&quot;: {                         \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2/pullrequests/5695\&quot;                     },                     \&quot;html\&quot;: {                         \&quot;href\&quot;: \&quot;https://bitbucket.org/atlassian/atlaskit-mk-2/pull-requests/5695\&quot;                     }                 },                 \&quot;title\&quot;: \&quot;username/NONE: small change from onFocus to onClick to handle tabbing through the page and not expand the editor unless a click event triggers it\&quot;             }         }     ] } &#x60;&#x60;&#x60;  Updates include a state property of OPEN, MERGED, or DECLINED.  Update example: &#x60;&#x60;&#x60; {     \&quot;pagelen\&quot;: 20,     \&quot;values\&quot;: [         {             \&quot;update\&quot;: {                 \&quot;description\&quot;: \&quot;\&quot;,                 \&quot;title\&quot;: \&quot;username/NONE: small change from onFocus to onClick to handle tabbing through the page and not expand the editor unless a click event triggers it\&quot;,                 \&quot;destination\&quot;: {                     \&quot;commit\&quot;: {                         \&quot;type\&quot;: \&quot;commit\&quot;,                         \&quot;hash\&quot;: \&quot;6a2c16e4a152\&quot;,                         \&quot;links\&quot;: {                             \&quot;self\&quot;: {                                 \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2/commit/6a2c16e4a152\&quot;                             },                             \&quot;html\&quot;: {                                 \&quot;href\&quot;: \&quot;https://bitbucket.org/atlassian/atlaskit-mk-2/commits/6a2c16e4a152\&quot;                             }                         }                     },                     \&quot;branch\&quot;: {                         \&quot;name\&quot;: \&quot;master\&quot;                     },                     \&quot;repository\&quot;: {                         \&quot;name\&quot;: \&quot;Atlaskit-MK-2\&quot;,                         \&quot;type\&quot;: \&quot;repository\&quot;,                         \&quot;full_name\&quot;: \&quot;atlassian/atlaskit-mk-2\&quot;,                         \&quot;links\&quot;: {                             \&quot;self\&quot;: {                                 \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2\&quot;                             },                             \&quot;html\&quot;: {                                 \&quot;href\&quot;: \&quot;https://bitbucket.org/atlassian/atlaskit-mk-2\&quot;                             },                             \&quot;avatar\&quot;: {                                 \&quot;href\&quot;: \&quot;https://bytebucket.org/ravatar/%7B%7D?ts&#x3D;js\&quot;                             }                         },                         \&quot;uuid\&quot;: \&quot;{}\&quot;                     }                 },                 \&quot;reason\&quot;: \&quot;\&quot;,                 \&quot;source\&quot;: {                     \&quot;commit\&quot;: {                         \&quot;type\&quot;: \&quot;commit\&quot;,                         \&quot;hash\&quot;: \&quot;728c8bad1813\&quot;,                         \&quot;links\&quot;: {                             \&quot;self\&quot;: {                                 \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2/commit/728c8bad1813\&quot;                             },                             \&quot;html\&quot;: {                                 \&quot;href\&quot;: \&quot;https://bitbucket.org/atlassian/atlaskit-mk-2/commits/728c8bad1813\&quot;                             }                         }                     },                     \&quot;branch\&quot;: {                         \&quot;name\&quot;: \&quot;username/NONE-add-onClick-prop-for-accessibility\&quot;                     },                     \&quot;repository\&quot;: {                         \&quot;name\&quot;: \&quot;Atlaskit-MK-2\&quot;,                         \&quot;type\&quot;: \&quot;repository\&quot;,                         \&quot;full_name\&quot;: \&quot;atlassian/atlaskit-mk-2\&quot;,                         \&quot;links\&quot;: {                             \&quot;self\&quot;: {                                 \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2\&quot;                             },                             \&quot;html\&quot;: {                                 \&quot;href\&quot;: \&quot;https://bitbucket.org/atlassian/atlaskit-mk-2\&quot;                             },                             \&quot;avatar\&quot;: {                                 \&quot;href\&quot;: \&quot;https://bytebucket.org/ravatar/%7B%7D?ts&#x3D;js\&quot;                             }                         },                         \&quot;uuid\&quot;: \&quot;{}\&quot;                     }                 },                 \&quot;state\&quot;: \&quot;OPEN\&quot;,                 \&quot;author\&quot;: {                     \&quot;display_name\&quot;: \&quot;Name Lastname\&quot;,                     \&quot;uuid\&quot;: \&quot;{}\&quot;,                     \&quot;links\&quot;: {                         \&quot;self\&quot;: {                             \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/users/%7B%7D\&quot;                         },                         \&quot;html\&quot;: {                             \&quot;href\&quot;: \&quot;https://bitbucket.org/%7B%7D/\&quot;                         },                         \&quot;avatar\&quot;: {                             \&quot;href\&quot;: \&quot;https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/:/128\&quot;                         }                     },                     \&quot;type\&quot;: \&quot;user\&quot;,                     \&quot;nickname\&quot;: \&quot;Name\&quot;,                     \&quot;account_id\&quot;: \&quot;\&quot;                 },                 \&quot;date\&quot;: \&quot;2019-05-10T06:48:25.305565+00:00\&quot;             },             \&quot;pull_request\&quot;: {                 \&quot;type\&quot;: \&quot;pullrequest\&quot;,                 \&quot;id\&quot;: 5695,                 \&quot;links\&quot;: {                     \&quot;self\&quot;: {                         \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2/pullrequests/5695\&quot;                     },                     \&quot;html\&quot;: {                         \&quot;href\&quot;: \&quot;https://bitbucket.org/atlassian/atlaskit-mk-2/pull-requests/5695\&quot;                     }                 },                 \&quot;title\&quot;: \&quot;username/NONE: small change from onFocus to onClick to handle tabbing through the page and not expand the editor unless a click event triggers it\&quot;             }         }     ] } &#x60;&#x60;&#x60;  Approval example: &#x60;&#x60;&#x60; {     \&quot;pagelen\&quot;: 20,     \&quot;values\&quot;: [         {             \&quot;approval\&quot;: {                 \&quot;date\&quot;: \&quot;2019-09-27T00:37:19.849534+00:00\&quot;,                 \&quot;pullrequest\&quot;: {                     \&quot;type\&quot;: \&quot;pullrequest\&quot;,                     \&quot;id\&quot;: 5695,                     \&quot;links\&quot;: {                         \&quot;self\&quot;: {                             \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2/pullrequests/5695\&quot;                         },                         \&quot;html\&quot;: {                             \&quot;href\&quot;: \&quot;https://bitbucket.org/atlassian/atlaskit-mk-2/pull-requests/5695\&quot;                         }                     },                     \&quot;title\&quot;: \&quot;username/NONE: small change from onFocus to onClick to handle tabbing through the page and not expand the editor unless a click event triggers it\&quot;                 },                 \&quot;user\&quot;: {                     \&quot;display_name\&quot;: \&quot;Name Lastname\&quot;,                     \&quot;uuid\&quot;: \&quot;{}\&quot;,                     \&quot;links\&quot;: {                         \&quot;self\&quot;: {                             \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/users/%7B%7D\&quot;                         },                         \&quot;html\&quot;: {                             \&quot;href\&quot;: \&quot;https://bitbucket.org/%7B%7D/\&quot;                         },                         \&quot;avatar\&quot;: {                             \&quot;href\&quot;: \&quot;https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/:/128\&quot;                         }                     },                     \&quot;type\&quot;: \&quot;user\&quot;,                     \&quot;nickname\&quot;: \&quot;Name\&quot;,                     \&quot;account_id\&quot;: \&quot;\&quot;                 }             },             \&quot;pull_request\&quot;: {                 \&quot;type\&quot;: \&quot;pullrequest\&quot;,                 \&quot;id\&quot;: 5695,                 \&quot;links\&quot;: {                     \&quot;self\&quot;: {                         \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2/pullrequests/5695\&quot;                     },                     \&quot;html\&quot;: {                         \&quot;href\&quot;: \&quot;https://bitbucket.org/atlassian/atlaskit-mk-2/pull-requests/5695\&quot;                     }                 },                 \&quot;title\&quot;: \&quot;username/NONE: small change from onFocus to onClick to handle tabbing through the page and not expand the editor unless a click event triggers it\&quot;             }         }     ] } &#x60;&#x60;&#x60;

### Example

```javascript
import BitbucketApi from 'bitbucket_api';
let defaultClient = BitbucketApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BitbucketApi.PullrequestsApi();
let pullRequestId = 56; // Number | The id of the pull request.
let repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
apiInstance.repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdActivityGet(pullRequestId, repoSlug, workspace, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pullRequestId** | **Number**| The id of the pull request. | 
 **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdApproveDelete

> repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdApproveDelete(pullRequestId, repoSlug, workspace)

Unapprove a pull request

Redact the authenticated user&#39;s approval of the specified pull request.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';
let defaultClient = BitbucketApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BitbucketApi.PullrequestsApi();
let pullRequestId = 56; // Number | The id of the pull request.
let repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
apiInstance.repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdApproveDelete(pullRequestId, repoSlug, workspace, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pullRequestId** | **Number**| The id of the pull request. | 
 **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdApprovePost

> Participant repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdApprovePost(pullRequestId, repoSlug, workspace)

Approve a pull request

Approve the specified pull request as the authenticated user.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';
let defaultClient = BitbucketApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BitbucketApi.PullrequestsApi();
let pullRequestId = 56; // Number | The id of the pull request.
let repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
apiInstance.repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdApprovePost(pullRequestId, repoSlug, workspace, (error, data, response) => {
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
 **pullRequestId** | **Number**| The id of the pull request. | 
 **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | 

### Return type

[**Participant**](Participant.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdCommentsCommentIdDelete

> repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdCommentsCommentIdDelete(commentId, pullRequestId, repoSlug, workspace)

Delete a comment on a pull request

Deletes a specific pull request comment.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';
let defaultClient = BitbucketApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BitbucketApi.PullrequestsApi();
let commentId = 56; // Number | The id of the comment.
let pullRequestId = 56; // Number | The id of the pull request.
let repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
apiInstance.repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdCommentsCommentIdDelete(commentId, pullRequestId, repoSlug, workspace, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **commentId** | **Number**| The id of the comment. | 
 **pullRequestId** | **Number**| The id of the pull request. | 
 **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdCommentsCommentIdGet

> PullrequestComment repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdCommentsCommentIdGet(commentId, pullRequestId, repoSlug, workspace)

Get a comment on a pull request

Returns a specific pull request comment.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';
let defaultClient = BitbucketApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BitbucketApi.PullrequestsApi();
let commentId = 56; // Number | The id of the comment.
let pullRequestId = 56; // Number | The id of the pull request.
let repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
apiInstance.repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdCommentsCommentIdGet(commentId, pullRequestId, repoSlug, workspace, (error, data, response) => {
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
 **commentId** | **Number**| The id of the comment. | 
 **pullRequestId** | **Number**| The id of the pull request. | 
 **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | 

### Return type

[**PullrequestComment**](PullrequestComment.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdCommentsCommentIdPut

> PullrequestComment repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdCommentsCommentIdPut(commentId, pullRequestId, repoSlug, workspace, pullrequestComment)

Update a comment on a pull request

Updates a specific pull request comment.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';
let defaultClient = BitbucketApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BitbucketApi.PullrequestsApi();
let commentId = 56; // Number | The id of the comment.
let pullRequestId = 56; // Number | The id of the pull request.
let repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
let pullrequestComment = new BitbucketApi.PullrequestComment(); // PullrequestComment | The contents of the updated comment.
apiInstance.repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdCommentsCommentIdPut(commentId, pullRequestId, repoSlug, workspace, pullrequestComment, (error, data, response) => {
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
 **commentId** | **Number**| The id of the comment. | 
 **pullRequestId** | **Number**| The id of the pull request. | 
 **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | 
 **pullrequestComment** | [**PullrequestComment**](PullrequestComment.md)| The contents of the updated comment. | 

### Return type

[**PullrequestComment**](PullrequestComment.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdCommentsCommentIdResolveDelete

> repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdCommentsCommentIdResolveDelete(commentId, pullRequestId, repoSlug, workspace)

Reopen a comment thread



### Example

```javascript
import BitbucketApi from 'bitbucket_api';
let defaultClient = BitbucketApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BitbucketApi.PullrequestsApi();
let commentId = 56; // Number | The id of the comment.
let pullRequestId = 56; // Number | The id of the pull request.
let repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
apiInstance.repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdCommentsCommentIdResolveDelete(commentId, pullRequestId, repoSlug, workspace, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **commentId** | **Number**| The id of the comment. | 
 **pullRequestId** | **Number**| The id of the pull request. | 
 **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdCommentsCommentIdResolvePost

> CommentResolution repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdCommentsCommentIdResolvePost(commentId, pullRequestId, repoSlug, workspace)

Resolve a comment thread



### Example

```javascript
import BitbucketApi from 'bitbucket_api';
let defaultClient = BitbucketApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BitbucketApi.PullrequestsApi();
let commentId = 56; // Number | The id of the comment.
let pullRequestId = 56; // Number | The id of the pull request.
let repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
apiInstance.repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdCommentsCommentIdResolvePost(commentId, pullRequestId, repoSlug, workspace, (error, data, response) => {
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
 **commentId** | **Number**| The id of the comment. | 
 **pullRequestId** | **Number**| The id of the pull request. | 
 **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | 

### Return type

[**CommentResolution**](CommentResolution.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdCommentsGet

> PaginatedPullrequestComments repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdCommentsGet(pullRequestId, repoSlug, workspace)

List comments on a pull request

Returns a paginated list of the pull request&#39;s comments.  This includes both global, inline comments and replies.  The default sorting is oldest to newest and can be overridden with the &#x60;sort&#x60; query parameter.  This endpoint also supports filtering and sorting of the results. See [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering) for more details.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';
let defaultClient = BitbucketApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BitbucketApi.PullrequestsApi();
let pullRequestId = 56; // Number | The id of the pull request.
let repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
apiInstance.repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdCommentsGet(pullRequestId, repoSlug, workspace, (error, data, response) => {
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
 **pullRequestId** | **Number**| The id of the pull request. | 
 **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | 

### Return type

[**PaginatedPullrequestComments**](PaginatedPullrequestComments.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdCommentsPost

> PullrequestComment repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdCommentsPost(pullRequestId, repoSlug, workspace, pullrequestComment)

Create a comment on a pull request

Creates a new pull request comment.  Returns the newly created pull request comment.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';
let defaultClient = BitbucketApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BitbucketApi.PullrequestsApi();
let pullRequestId = 56; // Number | The id of the pull request.
let repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
let pullrequestComment = new BitbucketApi.PullrequestComment(); // PullrequestComment | The comment object.
apiInstance.repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdCommentsPost(pullRequestId, repoSlug, workspace, pullrequestComment, (error, data, response) => {
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
 **pullRequestId** | **Number**| The id of the pull request. | 
 **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | 
 **pullrequestComment** | [**PullrequestComment**](PullrequestComment.md)| The comment object. | 

### Return type

[**PullrequestComment**](PullrequestComment.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdCommitsGet

> repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdCommitsGet(pullRequestId, repoSlug, workspace)

List commits on a pull request

Returns a paginated list of the pull request&#39;s commits.  These are the commits that are being merged into the destination branch when the pull requests gets accepted.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';
let defaultClient = BitbucketApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BitbucketApi.PullrequestsApi();
let pullRequestId = 56; // Number | The id of the pull request.
let repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
apiInstance.repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdCommitsGet(pullRequestId, repoSlug, workspace, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pullRequestId** | **Number**| The id of the pull request. | 
 **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdDeclinePost

> Pullrequest repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdDeclinePost(pullRequestId, repoSlug, workspace)

Decline a pull request

Declines the pull request.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';
let defaultClient = BitbucketApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BitbucketApi.PullrequestsApi();
let pullRequestId = 56; // Number | The id of the pull request.
let repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
apiInstance.repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdDeclinePost(pullRequestId, repoSlug, workspace, (error, data, response) => {
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
 **pullRequestId** | **Number**| The id of the pull request. | 
 **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | 

### Return type

[**Pullrequest**](Pullrequest.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdDiffGet

> repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdDiffGet(pullRequestId, repoSlug, workspace)

List changes in a pull request

Redirects to the [repository diff](/cloud/bitbucket/rest/api-group-commits/#api-repositories-workspace-repo-slug-diff-spec-get) with the revspec that corresponds to the pull request.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';
let defaultClient = BitbucketApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BitbucketApi.PullrequestsApi();
let pullRequestId = 56; // Number | The id of the pull request.
let repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
apiInstance.repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdDiffGet(pullRequestId, repoSlug, workspace, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pullRequestId** | **Number**| The id of the pull request. | 
 **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdDiffstatGet

> repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdDiffstatGet(pullRequestId, repoSlug, workspace)

Get the diff stat for a pull request

Redirects to the [repository diffstat](/cloud/bitbucket/rest/api-group-commits/#api-repositories-workspace-repo-slug-diffstat-spec-get) with the revspec that corresponds to the pull request.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';
let defaultClient = BitbucketApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BitbucketApi.PullrequestsApi();
let pullRequestId = 56; // Number | The id of the pull request.
let repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
apiInstance.repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdDiffstatGet(pullRequestId, repoSlug, workspace, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pullRequestId** | **Number**| The id of the pull request. | 
 **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdGet

> Pullrequest repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdGet(pullRequestId, repoSlug, workspace)

Get a pull request

Returns the specified pull request.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';
let defaultClient = BitbucketApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BitbucketApi.PullrequestsApi();
let pullRequestId = 56; // Number | The id of the pull request.
let repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
apiInstance.repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdGet(pullRequestId, repoSlug, workspace, (error, data, response) => {
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
 **pullRequestId** | **Number**| The id of the pull request. | 
 **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | 

### Return type

[**Pullrequest**](Pullrequest.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdMergePost

> Pullrequest repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdMergePost(pullRequestId, repoSlug, workspace, opts)

Merge a pull request

Merges the pull request.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';
let defaultClient = BitbucketApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BitbucketApi.PullrequestsApi();
let pullRequestId = 56; // Number | The id of the pull request.
let repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
let opts = {
  'async': true, // Boolean | Default value is false.   When set to true, runs merge asynchronously and immediately returns a 202 with polling link to the task-status API in the Location header.   When set to false, runs merge and waits for it to complete, returning 200 when it succeeds. If the duration of the merge exceeds a timeout threshold, the API returns a 202 with polling link to the task-status API in the Location header.
  'pullrequestMergeParameters': new BitbucketApi.PullrequestMergeParameters() // PullrequestMergeParameters | 
};
apiInstance.repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdMergePost(pullRequestId, repoSlug, workspace, opts, (error, data, response) => {
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
 **pullRequestId** | **Number**| The id of the pull request. | 
 **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | 
 **async** | **Boolean**| Default value is false.   When set to true, runs merge asynchronously and immediately returns a 202 with polling link to the task-status API in the Location header.   When set to false, runs merge and waits for it to complete, returning 200 when it succeeds. If the duration of the merge exceeds a timeout threshold, the API returns a 202 with polling link to the task-status API in the Location header. | [optional] 
 **pullrequestMergeParameters** | [**PullrequestMergeParameters**](PullrequestMergeParameters.md)|  | [optional] 

### Return type

[**Pullrequest**](Pullrequest.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdMergeTaskStatusTaskIdGet

> repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdMergeTaskStatusTaskIdGet(pullRequestId, repoSlug, taskId, workspace)

Get the merge task status for a pull request

When merging a pull request takes too long, the client receives a task ID along with a 202 status code. The task ID can be used in a call to this endpoint to check the status of a merge task.  &#x60;&#x60;&#x60; curl -X GET https://api.bitbucket.org/2.0/repositories/atlassian/bitbucket/pullrequests/2286/merge/task-status/&lt;task_id&gt; &#x60;&#x60;&#x60;  If the merge task is not yet finished, a PENDING status will be returned.  &#x60;&#x60;&#x60; HTTP/2 200 {     \&quot;task_status\&quot;: \&quot;PENDING\&quot;,     \&quot;links\&quot;: {         \&quot;self\&quot;: {             \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/atlassian/bitbucket/pullrequests/2286/merge/task-status/&lt;task_id&gt;\&quot;         }     } } &#x60;&#x60;&#x60;  If the merge was successful, a SUCCESS status will be returned.  &#x60;&#x60;&#x60; HTTP/2 200 {     \&quot;task_status\&quot;: \&quot;SUCCESS\&quot;,     \&quot;links\&quot;: {         \&quot;self\&quot;: {             \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/atlassian/bitbucket/pullrequests/2286/merge/task-status/&lt;task_id&gt;\&quot;         }     },     \&quot;merge_result\&quot;: &lt;the merged pull request object&gt; } &#x60;&#x60;&#x60;  If the merge task failed, an error will be returned.  &#x60;&#x60;&#x60; {     \&quot;type\&quot;: \&quot;error\&quot;,     \&quot;error\&quot;: {         \&quot;message\&quot;: \&quot;&lt;error message&gt;\&quot;     } } &#x60;&#x60;&#x60;

### Example

```javascript
import BitbucketApi from 'bitbucket_api';
let defaultClient = BitbucketApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BitbucketApi.PullrequestsApi();
let pullRequestId = 56; // Number | The id of the pull request.
let repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
let taskId = "taskId_example"; // String | ID of the merge task
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
apiInstance.repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdMergeTaskStatusTaskIdGet(pullRequestId, repoSlug, taskId, workspace, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pullRequestId** | **Number**| The id of the pull request. | 
 **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 
 **taskId** | **String**| ID of the merge task | 
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdPatchGet

> repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdPatchGet(pullRequestId, repoSlug, workspace)

Get the patch for a pull request

Redirects to the [repository patch](/cloud/bitbucket/rest/api-group-commits/#api-repositories-workspace-repo-slug-patch-spec-get) with the revspec that corresponds to pull request.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';
let defaultClient = BitbucketApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BitbucketApi.PullrequestsApi();
let pullRequestId = 56; // Number | The id of the pull request.
let repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
apiInstance.repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdPatchGet(pullRequestId, repoSlug, workspace, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pullRequestId** | **Number**| The id of the pull request. | 
 **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdPut

> Pullrequest repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdPut(pullRequestId, repoSlug, workspace, opts)

Update a pull request

Mutates the specified pull request.  This can be used to change the pull request&#39;s branches or description.  Only open pull requests can be mutated.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';
let defaultClient = BitbucketApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BitbucketApi.PullrequestsApi();
let pullRequestId = 56; // Number | The id of the pull request.
let repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
let opts = {
  'pullrequest': new BitbucketApi.Pullrequest() // Pullrequest | The pull request that is to be updated.
};
apiInstance.repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdPut(pullRequestId, repoSlug, workspace, opts, (error, data, response) => {
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
 **pullRequestId** | **Number**| The id of the pull request. | 
 **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | 
 **pullrequest** | [**Pullrequest**](Pullrequest.md)| The pull request that is to be updated. | [optional] 

### Return type

[**Pullrequest**](Pullrequest.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdRequestChangesDelete

> repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdRequestChangesDelete(pullRequestId, repoSlug, workspace)

Remove change request for a pull request



### Example

```javascript
import BitbucketApi from 'bitbucket_api';
let defaultClient = BitbucketApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BitbucketApi.PullrequestsApi();
let pullRequestId = 56; // Number | The id of the pull request.
let repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
apiInstance.repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdRequestChangesDelete(pullRequestId, repoSlug, workspace, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pullRequestId** | **Number**| The id of the pull request. | 
 **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdRequestChangesPost

> Participant repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdRequestChangesPost(pullRequestId, repoSlug, workspace)

Request changes for a pull request



### Example

```javascript
import BitbucketApi from 'bitbucket_api';
let defaultClient = BitbucketApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BitbucketApi.PullrequestsApi();
let pullRequestId = 56; // Number | The id of the pull request.
let repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
apiInstance.repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdRequestChangesPost(pullRequestId, repoSlug, workspace, (error, data, response) => {
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
 **pullRequestId** | **Number**| The id of the pull request. | 
 **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | 

### Return type

[**Participant**](Participant.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdStatusesGet

> PaginatedCommitstatuses repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdStatusesGet(pullRequestId, repoSlug, workspace, opts)

List commit statuses for a pull request

Returns all statuses (e.g. build results) for the given pull request.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';
let defaultClient = BitbucketApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BitbucketApi.PullrequestsApi();
let pullRequestId = 56; // Number | The id of the pull request.
let repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
let opts = {
  'q': "q_example", // String | Query string to narrow down the response as per [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering). 
  'sort': "sort_example" // String | Field by which the results should be sorted as per [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering). Defaults to `created_on`. 
};
apiInstance.repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdStatusesGet(pullRequestId, repoSlug, workspace, opts, (error, data, response) => {
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
 **pullRequestId** | **Number**| The id of the pull request. | 
 **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | 
 **q** | **String**| Query string to narrow down the response as per [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering).  | [optional] 
 **sort** | **String**| Field by which the results should be sorted as per [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering). Defaults to &#x60;created_on&#x60;.  | [optional] 

### Return type

[**PaginatedCommitstatuses**](PaginatedCommitstatuses.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

