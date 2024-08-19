# GitHubV3RestApi.ReactionsApi

All URIs are relative to *http://HOSTNAME/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reactionsCreateForCommitComment**](ReactionsApi.md#reactionsCreateForCommitComment) | **POST** /repos/{owner}/{repo}/comments/{comment_id}/reactions | Create reaction for a commit comment
[**reactionsCreateForIssue**](ReactionsApi.md#reactionsCreateForIssue) | **POST** /repos/{owner}/{repo}/issues/{issue_number}/reactions | Create reaction for an issue
[**reactionsCreateForIssueComment**](ReactionsApi.md#reactionsCreateForIssueComment) | **POST** /repos/{owner}/{repo}/issues/comments/{comment_id}/reactions | Create reaction for an issue comment
[**reactionsCreateForPullRequestReviewComment**](ReactionsApi.md#reactionsCreateForPullRequestReviewComment) | **POST** /repos/{owner}/{repo}/pulls/comments/{comment_id}/reactions | Create reaction for a pull request review comment
[**reactionsCreateForTeamDiscussion**](ReactionsApi.md#reactionsCreateForTeamDiscussion) | **POST** /teams/{team_id}/discussions/{discussion_number}/reactions | Create reaction for a team discussion
[**reactionsCreateForTeamDiscussionComment**](ReactionsApi.md#reactionsCreateForTeamDiscussionComment) | **POST** /teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}/reactions | Create reaction for a team discussion comment
[**reactionsDelete**](ReactionsApi.md#reactionsDelete) | **DELETE** /reactions/{reaction_id} | Delete a reaction
[**reactionsListForCommitComment**](ReactionsApi.md#reactionsListForCommitComment) | **GET** /repos/{owner}/{repo}/comments/{comment_id}/reactions | List reactions for a commit comment
[**reactionsListForIssue**](ReactionsApi.md#reactionsListForIssue) | **GET** /repos/{owner}/{repo}/issues/{issue_number}/reactions | List reactions for an issue
[**reactionsListForIssueComment**](ReactionsApi.md#reactionsListForIssueComment) | **GET** /repos/{owner}/{repo}/issues/comments/{comment_id}/reactions | List reactions for an issue comment
[**reactionsListForPullRequestReviewComment**](ReactionsApi.md#reactionsListForPullRequestReviewComment) | **GET** /repos/{owner}/{repo}/pulls/comments/{comment_id}/reactions | List reactions for a pull request review comment
[**reactionsListForTeamDiscussion**](ReactionsApi.md#reactionsListForTeamDiscussion) | **GET** /teams/{team_id}/discussions/{discussion_number}/reactions | List reactions for a team discussion
[**reactionsListForTeamDiscussionComment**](ReactionsApi.md#reactionsListForTeamDiscussionComment) | **GET** /teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}/reactions | List reactions for a team discussion comment



## reactionsCreateForCommitComment

> Reaction reactionsCreateForCommitComment(owner, repo, commentId, reactionsCreateForCommitCommentRequest)

Create reaction for a commit comment

Create a reaction to a [commit comment](https://docs.github.com/enterprise-server@2.18/rest/reference/repos#comments). A response with an HTTP &#x60;200&#x60; status means that you already added the reaction type to this commit comment.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.ReactionsApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let commentId = 56; // Number | comment_id parameter
let reactionsCreateForCommitCommentRequest = {"content":"heart"}; // ReactionsCreateForCommitCommentRequest | 
apiInstance.reactionsCreateForCommitComment(owner, repo, commentId, reactionsCreateForCommitCommentRequest, (error, data, response) => {
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
 **owner** | **String**|  | 
 **repo** | **String**|  | 
 **commentId** | **Number**| comment_id parameter | 
 **reactionsCreateForCommitCommentRequest** | [**ReactionsCreateForCommitCommentRequest**](ReactionsCreateForCommitCommentRequest.md)|  | 

### Return type

[**Reaction**](Reaction.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## reactionsCreateForIssue

> Reaction reactionsCreateForIssue(owner, repo, issueNumber, reactionsCreateForIssueRequest)

Create reaction for an issue

Create a reaction to an [issue](https://docs.github.com/enterprise-server@2.18/rest/reference/issues/). A response with an HTTP &#x60;200&#x60; status means that you already added the reaction type to this issue.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.ReactionsApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let issueNumber = 56; // Number | issue_number parameter
let reactionsCreateForIssueRequest = {"content":"heart"}; // ReactionsCreateForIssueRequest | 
apiInstance.reactionsCreateForIssue(owner, repo, issueNumber, reactionsCreateForIssueRequest, (error, data, response) => {
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
 **owner** | **String**|  | 
 **repo** | **String**|  | 
 **issueNumber** | **Number**| issue_number parameter | 
 **reactionsCreateForIssueRequest** | [**ReactionsCreateForIssueRequest**](ReactionsCreateForIssueRequest.md)|  | 

### Return type

[**Reaction**](Reaction.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## reactionsCreateForIssueComment

> Reaction reactionsCreateForIssueComment(owner, repo, commentId, reactionsCreateForIssueCommentRequest)

Create reaction for an issue comment

Create a reaction to an [issue comment](https://docs.github.com/enterprise-server@2.18/rest/reference/issues#comments). A response with an HTTP &#x60;200&#x60; status means that you already added the reaction type to this issue comment.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.ReactionsApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let commentId = 56; // Number | comment_id parameter
let reactionsCreateForIssueCommentRequest = {"content":"heart"}; // ReactionsCreateForIssueCommentRequest | 
apiInstance.reactionsCreateForIssueComment(owner, repo, commentId, reactionsCreateForIssueCommentRequest, (error, data, response) => {
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
 **owner** | **String**|  | 
 **repo** | **String**|  | 
 **commentId** | **Number**| comment_id parameter | 
 **reactionsCreateForIssueCommentRequest** | [**ReactionsCreateForIssueCommentRequest**](ReactionsCreateForIssueCommentRequest.md)|  | 

### Return type

[**Reaction**](Reaction.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## reactionsCreateForPullRequestReviewComment

> Reaction reactionsCreateForPullRequestReviewComment(owner, repo, commentId, reactionsCreateForPullRequestReviewCommentRequest)

Create reaction for a pull request review comment

Create a reaction to a [pull request review comment](https://docs.github.com/enterprise-server@2.18/rest/reference/pulls#comments). A response with an HTTP &#x60;200&#x60; status means that you already added the reaction type to this pull request review comment.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.ReactionsApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let commentId = 56; // Number | comment_id parameter
let reactionsCreateForPullRequestReviewCommentRequest = {"content":"heart"}; // ReactionsCreateForPullRequestReviewCommentRequest | 
apiInstance.reactionsCreateForPullRequestReviewComment(owner, repo, commentId, reactionsCreateForPullRequestReviewCommentRequest, (error, data, response) => {
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
 **owner** | **String**|  | 
 **repo** | **String**|  | 
 **commentId** | **Number**| comment_id parameter | 
 **reactionsCreateForPullRequestReviewCommentRequest** | [**ReactionsCreateForPullRequestReviewCommentRequest**](ReactionsCreateForPullRequestReviewCommentRequest.md)|  | 

### Return type

[**Reaction**](Reaction.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## reactionsCreateForTeamDiscussion

> Reaction reactionsCreateForTeamDiscussion(accept, teamId, discussionNumber, reactionsCreateForTeamDiscussionRequest)

Create reaction for a team discussion

Create a reaction to a [team discussion](https://docs.github.com/enterprise-server@2.18/rest/reference/teams#discussions). OAuth access tokens require the &#x60;write:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.18/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/). A response with an HTTP &#x60;200&#x60; status means that you already added the reaction type to this team discussion.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.ReactionsApi();
let accept = "'application/vnd.github.echo-preview+json,application/vnd.github.squirrel-girl-preview+json'"; // String | This API is under preview and subject to change.
let teamId = 56; // Number | 
let discussionNumber = 56; // Number | 
let reactionsCreateForTeamDiscussionRequest = {"content":"heart"}; // ReactionsCreateForTeamDiscussionRequest | 
apiInstance.reactionsCreateForTeamDiscussion(accept, teamId, discussionNumber, reactionsCreateForTeamDiscussionRequest, (error, data, response) => {
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
 **accept** | **String**| This API is under preview and subject to change. | [default to &#39;application/vnd.github.echo-preview+json,application/vnd.github.squirrel-girl-preview+json&#39;]
 **teamId** | **Number**|  | 
 **discussionNumber** | **Number**|  | 
 **reactionsCreateForTeamDiscussionRequest** | [**ReactionsCreateForTeamDiscussionRequest**](ReactionsCreateForTeamDiscussionRequest.md)|  | 

### Return type

[**Reaction**](Reaction.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## reactionsCreateForTeamDiscussionComment

> Reaction reactionsCreateForTeamDiscussionComment(accept, teamId, discussionNumber, commentNumber, reactionsCreateForTeamDiscussionCommentRequest)

Create reaction for a team discussion comment

Create a reaction to a [team discussion comment](https://docs.github.com/enterprise-server@2.18/rest/reference/teams#discussion-comments). OAuth access tokens require the &#x60;write:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.18/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/). A response with an HTTP &#x60;200&#x60; status means that you already added the reaction type to this team discussion comment.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.ReactionsApi();
let accept = "'application/vnd.github.echo-preview+json,application/vnd.github.squirrel-girl-preview+json'"; // String | This API is under preview and subject to change.
let teamId = 56; // Number | 
let discussionNumber = 56; // Number | 
let commentNumber = 56; // Number | 
let reactionsCreateForTeamDiscussionCommentRequest = {"content":"heart"}; // ReactionsCreateForTeamDiscussionCommentRequest | 
apiInstance.reactionsCreateForTeamDiscussionComment(accept, teamId, discussionNumber, commentNumber, reactionsCreateForTeamDiscussionCommentRequest, (error, data, response) => {
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
 **accept** | **String**| This API is under preview and subject to change. | [default to &#39;application/vnd.github.echo-preview+json,application/vnd.github.squirrel-girl-preview+json&#39;]
 **teamId** | **Number**|  | 
 **discussionNumber** | **Number**|  | 
 **commentNumber** | **Number**|  | 
 **reactionsCreateForTeamDiscussionCommentRequest** | [**ReactionsCreateForTeamDiscussionCommentRequest**](ReactionsCreateForTeamDiscussionCommentRequest.md)|  | 

### Return type

[**Reaction**](Reaction.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## reactionsDelete

> reactionsDelete(accept, reactionId)

Delete a reaction

OAuth access tokens require the &#x60;write:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.18/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/), when deleting a [team discussion](https://docs.github.com/enterprise-server@2.18/rest/reference/teams#discussions) or [team discussion comment](https://docs.github.com/enterprise-server@2.18/rest/reference/teams#discussion-comments).

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.ReactionsApi();
let accept = "'application/vnd.github.echo-preview+json,application/vnd.github.squirrel-girl-preview+json'"; // String | This API is under preview and subject to change.
let reactionId = 56; // Number | 
apiInstance.reactionsDelete(accept, reactionId, (error, data, response) => {
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
 **accept** | **String**| This API is under preview and subject to change. | [default to &#39;application/vnd.github.echo-preview+json,application/vnd.github.squirrel-girl-preview+json&#39;]
 **reactionId** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## reactionsListForCommitComment

> [Reaction] reactionsListForCommitComment(owner, repo, commentId, opts)

List reactions for a commit comment

List the reactions to a [commit comment](https://docs.github.com/enterprise-server@2.18/rest/reference/repos#comments).

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.ReactionsApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let commentId = 56; // Number | comment_id parameter
let opts = {
  'content': "content_example", // String | Returns a single [reaction type](https://docs.github.com/enterprise-server@2.18/rest/reference/reactions#reaction-types). Omit this parameter to list all reactions to a commit comment.
  'perPage': 30, // Number | Results per page (max 100)
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.reactionsListForCommitComment(owner, repo, commentId, opts, (error, data, response) => {
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
 **owner** | **String**|  | 
 **repo** | **String**|  | 
 **commentId** | **Number**| comment_id parameter | 
 **content** | **String**| Returns a single [reaction type](https://docs.github.com/enterprise-server@2.18/rest/reference/reactions#reaction-types). Omit this parameter to list all reactions to a commit comment. | [optional] 
 **perPage** | **Number**| Results per page (max 100) | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[Reaction]**](Reaction.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reactionsListForIssue

> [Reaction] reactionsListForIssue(owner, repo, issueNumber, opts)

List reactions for an issue

List the reactions to an [issue](https://docs.github.com/enterprise-server@2.18/rest/reference/issues).

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.ReactionsApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let issueNumber = 56; // Number | issue_number parameter
let opts = {
  'content': "content_example", // String | Returns a single [reaction type](https://docs.github.com/enterprise-server@2.18/rest/reference/reactions#reaction-types). Omit this parameter to list all reactions to an issue.
  'perPage': 30, // Number | Results per page (max 100)
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.reactionsListForIssue(owner, repo, issueNumber, opts, (error, data, response) => {
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
 **owner** | **String**|  | 
 **repo** | **String**|  | 
 **issueNumber** | **Number**| issue_number parameter | 
 **content** | **String**| Returns a single [reaction type](https://docs.github.com/enterprise-server@2.18/rest/reference/reactions#reaction-types). Omit this parameter to list all reactions to an issue. | [optional] 
 **perPage** | **Number**| Results per page (max 100) | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[Reaction]**](Reaction.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reactionsListForIssueComment

> [Reaction] reactionsListForIssueComment(owner, repo, commentId, opts)

List reactions for an issue comment

List the reactions to an [issue comment](https://docs.github.com/enterprise-server@2.18/rest/reference/issues#comments).

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.ReactionsApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let commentId = 56; // Number | comment_id parameter
let opts = {
  'content': "content_example", // String | Returns a single [reaction type](https://docs.github.com/enterprise-server@2.18/rest/reference/reactions#reaction-types). Omit this parameter to list all reactions to an issue comment.
  'perPage': 30, // Number | Results per page (max 100)
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.reactionsListForIssueComment(owner, repo, commentId, opts, (error, data, response) => {
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
 **owner** | **String**|  | 
 **repo** | **String**|  | 
 **commentId** | **Number**| comment_id parameter | 
 **content** | **String**| Returns a single [reaction type](https://docs.github.com/enterprise-server@2.18/rest/reference/reactions#reaction-types). Omit this parameter to list all reactions to an issue comment. | [optional] 
 **perPage** | **Number**| Results per page (max 100) | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[Reaction]**](Reaction.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reactionsListForPullRequestReviewComment

> [Reaction] reactionsListForPullRequestReviewComment(owner, repo, commentId, opts)

List reactions for a pull request review comment

List the reactions to a [pull request review comment](https://docs.github.com/enterprise-server@2.18/rest/reference/pulls#review-comments).

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.ReactionsApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let commentId = 56; // Number | comment_id parameter
let opts = {
  'content': "content_example", // String | Returns a single [reaction type](https://docs.github.com/enterprise-server@2.18/rest/reference/reactions#reaction-types). Omit this parameter to list all reactions to a pull request review comment.
  'perPage': 30, // Number | Results per page (max 100)
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.reactionsListForPullRequestReviewComment(owner, repo, commentId, opts, (error, data, response) => {
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
 **owner** | **String**|  | 
 **repo** | **String**|  | 
 **commentId** | **Number**| comment_id parameter | 
 **content** | **String**| Returns a single [reaction type](https://docs.github.com/enterprise-server@2.18/rest/reference/reactions#reaction-types). Omit this parameter to list all reactions to a pull request review comment. | [optional] 
 **perPage** | **Number**| Results per page (max 100) | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[Reaction]**](Reaction.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reactionsListForTeamDiscussion

> [Reaction] reactionsListForTeamDiscussion(accept, teamId, discussionNumber, opts)

List reactions for a team discussion

List the reactions to a [team discussion](https://docs.github.com/enterprise-server@2.18/rest/reference/teams#discussions). OAuth access tokens require the &#x60;read:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.18/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.ReactionsApi();
let accept = "'application/vnd.github.echo-preview+json,application/vnd.github.squirrel-girl-preview+json'"; // String | This API is under preview and subject to change.
let teamId = 56; // Number | 
let discussionNumber = 56; // Number | 
let opts = {
  'content': "content_example", // String | Returns a single [reaction type](https://docs.github.com/enterprise-server@2.18/rest/reference/reactions#reaction-types). Omit this parameter to list all reactions to a team discussion.
  'perPage': 30, // Number | Results per page (max 100)
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.reactionsListForTeamDiscussion(accept, teamId, discussionNumber, opts, (error, data, response) => {
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
 **accept** | **String**| This API is under preview and subject to change. | [default to &#39;application/vnd.github.echo-preview+json,application/vnd.github.squirrel-girl-preview+json&#39;]
 **teamId** | **Number**|  | 
 **discussionNumber** | **Number**|  | 
 **content** | **String**| Returns a single [reaction type](https://docs.github.com/enterprise-server@2.18/rest/reference/reactions#reaction-types). Omit this parameter to list all reactions to a team discussion. | [optional] 
 **perPage** | **Number**| Results per page (max 100) | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[Reaction]**](Reaction.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reactionsListForTeamDiscussionComment

> [Reaction] reactionsListForTeamDiscussionComment(accept, teamId, discussionNumber, commentNumber, opts)

List reactions for a team discussion comment

List the reactions to a [team discussion comment](https://docs.github.com/enterprise-server@2.18/rest/reference/teams#discussion-comments). OAuth access tokens require the &#x60;read:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.18/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.ReactionsApi();
let accept = "'application/vnd.github.echo-preview+json,application/vnd.github.squirrel-girl-preview+json'"; // String | This API is under preview and subject to change.
let teamId = 56; // Number | 
let discussionNumber = 56; // Number | 
let commentNumber = 56; // Number | 
let opts = {
  'content': "content_example", // String | Returns a single [reaction type](https://docs.github.com/enterprise-server@2.18/rest/reference/reactions#reaction-types). Omit this parameter to list all reactions to a team discussion comment.
  'perPage': 30, // Number | Results per page (max 100)
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.reactionsListForTeamDiscussionComment(accept, teamId, discussionNumber, commentNumber, opts, (error, data, response) => {
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
 **accept** | **String**| This API is under preview and subject to change. | [default to &#39;application/vnd.github.echo-preview+json,application/vnd.github.squirrel-girl-preview+json&#39;]
 **teamId** | **Number**|  | 
 **discussionNumber** | **Number**|  | 
 **commentNumber** | **Number**|  | 
 **content** | **String**| Returns a single [reaction type](https://docs.github.com/enterprise-server@2.18/rest/reference/reactions#reaction-types). Omit this parameter to list all reactions to a team discussion comment. | [optional] 
 **perPage** | **Number**| Results per page (max 100) | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[Reaction]**](Reaction.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

