# GitHubV3RestApi.PullsApi

All URIs are relative to *http://HOSTNAME/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pullsCheckIfMerged**](PullsApi.md#pullsCheckIfMerged) | **GET** /repos/{owner}/{repo}/pulls/{pull_number}/merge | Check if a pull request has been merged
[**pullsCreate**](PullsApi.md#pullsCreate) | **POST** /repos/{owner}/{repo}/pulls | Create a pull request
[**pullsCreateReplyForReviewComment**](PullsApi.md#pullsCreateReplyForReviewComment) | **POST** /repos/{owner}/{repo}/pulls/{pull_number}/comments/{comment_id}/replies | Create a reply for a review comment
[**pullsCreateReview**](PullsApi.md#pullsCreateReview) | **POST** /repos/{owner}/{repo}/pulls/{pull_number}/reviews | Create a review for a pull request
[**pullsCreateReviewComment**](PullsApi.md#pullsCreateReviewComment) | **POST** /repos/{owner}/{repo}/pulls/{pull_number}/comments | Create a review comment for a pull request
[**pullsDeletePendingReview**](PullsApi.md#pullsDeletePendingReview) | **DELETE** /repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id} | Delete a pending review for a pull request
[**pullsDeleteReviewComment**](PullsApi.md#pullsDeleteReviewComment) | **DELETE** /repos/{owner}/{repo}/pulls/comments/{comment_id} | Delete a review comment for a pull request
[**pullsDismissReview**](PullsApi.md#pullsDismissReview) | **PUT** /repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}/dismissals | Dismiss a review for a pull request
[**pullsGet**](PullsApi.md#pullsGet) | **GET** /repos/{owner}/{repo}/pulls/{pull_number} | Get a pull request
[**pullsGetReview**](PullsApi.md#pullsGetReview) | **GET** /repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id} | Get a review for a pull request
[**pullsGetReviewComment**](PullsApi.md#pullsGetReviewComment) | **GET** /repos/{owner}/{repo}/pulls/comments/{comment_id} | Get a review comment for a pull request
[**pullsList**](PullsApi.md#pullsList) | **GET** /repos/{owner}/{repo}/pulls | List pull requests
[**pullsListCommentsForReview**](PullsApi.md#pullsListCommentsForReview) | **GET** /repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}/comments | List comments for a pull request review
[**pullsListCommits**](PullsApi.md#pullsListCommits) | **GET** /repos/{owner}/{repo}/pulls/{pull_number}/commits | List commits on a pull request
[**pullsListFiles**](PullsApi.md#pullsListFiles) | **GET** /repos/{owner}/{repo}/pulls/{pull_number}/files | List pull requests files
[**pullsListRequestedReviewers**](PullsApi.md#pullsListRequestedReviewers) | **GET** /repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers | List requested reviewers for a pull request
[**pullsListReviewComments**](PullsApi.md#pullsListReviewComments) | **GET** /repos/{owner}/{repo}/pulls/{pull_number}/comments | List review comments on a pull request
[**pullsListReviewCommentsForRepo**](PullsApi.md#pullsListReviewCommentsForRepo) | **GET** /repos/{owner}/{repo}/pulls/comments | List review comments in a repository
[**pullsListReviews**](PullsApi.md#pullsListReviews) | **GET** /repos/{owner}/{repo}/pulls/{pull_number}/reviews | List reviews for a pull request
[**pullsMerge**](PullsApi.md#pullsMerge) | **PUT** /repos/{owner}/{repo}/pulls/{pull_number}/merge | Merge a pull request
[**pullsRemoveRequestedReviewers**](PullsApi.md#pullsRemoveRequestedReviewers) | **DELETE** /repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers | Remove requested reviewers from a pull request
[**pullsRequestReviewers**](PullsApi.md#pullsRequestReviewers) | **POST** /repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers | Request reviewers for a pull request
[**pullsSubmitReview**](PullsApi.md#pullsSubmitReview) | **POST** /repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}/events | Submit a review for a pull request
[**pullsUpdate**](PullsApi.md#pullsUpdate) | **PATCH** /repos/{owner}/{repo}/pulls/{pull_number} | Update a pull request
[**pullsUpdateBranch**](PullsApi.md#pullsUpdateBranch) | **PUT** /repos/{owner}/{repo}/pulls/{pull_number}/update-branch | Update a pull request branch
[**pullsUpdateReview**](PullsApi.md#pullsUpdateReview) | **PUT** /repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id} | Update a review for a pull request
[**pullsUpdateReviewComment**](PullsApi.md#pullsUpdateReviewComment) | **PATCH** /repos/{owner}/{repo}/pulls/comments/{comment_id} | Update a review comment for a pull request



## pullsCheckIfMerged

> pullsCheckIfMerged(owner, repo, pullNumber)

Check if a pull request has been merged



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.PullsApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let pullNumber = 56; // Number | 
apiInstance.pullsCheckIfMerged(owner, repo, pullNumber, (error, data, response) => {
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
 **owner** | **String**|  | 
 **repo** | **String**|  | 
 **pullNumber** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## pullsCreate

> PullRequest pullsCreate(owner, repo, pullsCreateRequest)

Create a pull request

Draft pull requests are available in public repositories with GitHub Free and GitHub Free for organizations, GitHub Pro, and legacy per-repository billing plans, and in public and private repositories with GitHub Team, GitHub Enterprise Server 2.17+, and GitHub Enterprise Cloud. You can create a new pull request. This endpoint triggers [notifications](https://docs.github.com/articles/about-notifications/). Creating content too quickly using this endpoint may result in secondary rate limiting. See \&quot;[Secondary rate limits](https://docs.github.com/enterprise-server@2.20/rest/overview/resources-in-the-rest-api#secondary-rate-limits)\&quot; for details.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.PullsApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let pullsCreateRequest = {"base":"master","body":"Please pull these awesome changes in!","head":"octocat:new-feature","title":"Amazing new feature"}; // PullsCreateRequest | 
apiInstance.pullsCreate(owner, repo, pullsCreateRequest, (error, data, response) => {
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
 **pullsCreateRequest** | [**PullsCreateRequest**](PullsCreateRequest.md)|  | 

### Return type

[**PullRequest**](PullRequest.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## pullsCreateReplyForReviewComment

> PullRequestReviewComment pullsCreateReplyForReviewComment(owner, repo, pullNumber, commentId, pullsCreateReplyForReviewCommentRequest)

Create a reply for a review comment

Creates a reply to a review comment for a pull request. For the &#x60;comment_id&#x60;, provide the ID of the review comment you are replying to. This must be the ID of a _top-level review comment_, not a reply to that comment. Replies to replies are not supported.  This endpoint triggers [notifications](https://docs.github.com/en/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See \&quot;[Secondary rate limits](https://docs.github.com/enterprise-server@2.20/rest/overview/resources-in-the-rest-api#secondary-rate-limits)\&quot; and \&quot;[Dealing with secondary rate limits](https://docs.github.com/enterprise-server@2.20/rest/guides/best-practices-for-integrators#dealing-with-secondary-rate-limits)\&quot; for details.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.PullsApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let pullNumber = 56; // Number | 
let commentId = 56; // Number | comment_id parameter
let pullsCreateReplyForReviewCommentRequest = {"body":"Great stuff!"}; // PullsCreateReplyForReviewCommentRequest | 
apiInstance.pullsCreateReplyForReviewComment(owner, repo, pullNumber, commentId, pullsCreateReplyForReviewCommentRequest, (error, data, response) => {
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
 **pullNumber** | **Number**|  | 
 **commentId** | **Number**| comment_id parameter | 
 **pullsCreateReplyForReviewCommentRequest** | [**PullsCreateReplyForReviewCommentRequest**](PullsCreateReplyForReviewCommentRequest.md)|  | 

### Return type

[**PullRequestReviewComment**](PullRequestReviewComment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## pullsCreateReview

> PullRequestReview pullsCreateReview(owner, repo, pullNumber, opts)

Create a review for a pull request

This endpoint triggers [notifications](https://docs.github.com/en/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See \&quot;[Secondary rate limits](https://docs.github.com/enterprise-server@2.20/rest/overview/resources-in-the-rest-api#secondary-rate-limits)\&quot; and \&quot;[Dealing with secondary rate limits](https://docs.github.com/enterprise-server@2.20/rest/guides/best-practices-for-integrators#dealing-with-secondary-rate-limits)\&quot; for details.  Pull request reviews created in the &#x60;PENDING&#x60; state do not include the &#x60;submitted_at&#x60; property in the response.  **Note:** To comment on a specific line in a file, you need to first determine the _position_ of that line in the diff. The GitHub REST API v3 offers the &#x60;application/vnd.github.v3.diff&#x60; [media type](https://docs.github.com/enterprise-server@2.20/rest/overview/media-types#commits-commit-comparison-and-pull-requests). To see a pull request diff, add this media type to the &#x60;Accept&#x60; header of a call to the [single pull request](https://docs.github.com/enterprise-server@2.20/rest/reference/pulls#get-a-pull-request) endpoint.  The &#x60;position&#x60; value equals the number of lines down from the first \&quot;@@\&quot; hunk header in the file you want to add a comment. The line just below the \&quot;@@\&quot; line is position 1, the next line is position 2, and so on. The position in the diff continues to increase through lines of whitespace and additional hunks until the beginning of a new file.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.PullsApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let pullNumber = 56; // Number | 
let opts = {
  'pullsCreateReviewRequest': {"body":"This is close to perfect! Please address the suggested inline change.","comments":[{"body":"Please add more information here, and fix this typo.","path":"file.md","position":6}],"commit_id":"ecdd80bb57125d7ba9641ffaa4d7d2c19d3f3091","event":"REQUEST_CHANGES"} // PullsCreateReviewRequest | 
};
apiInstance.pullsCreateReview(owner, repo, pullNumber, opts, (error, data, response) => {
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
 **pullNumber** | **Number**|  | 
 **pullsCreateReviewRequest** | [**PullsCreateReviewRequest**](PullsCreateReviewRequest.md)|  | [optional] 

### Return type

[**PullRequestReview**](PullRequestReview.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## pullsCreateReviewComment

> PullRequestReviewComment pullsCreateReviewComment(owner, repo, pullNumber, pullsCreateReviewCommentRequest)

Create a review comment for a pull request

 Creates a review comment in the pull request diff. To add a regular comment to a pull request timeline, see \&quot;[Create an issue comment](https://docs.github.com/enterprise-server@2.20/rest/reference/issues#create-an-issue-comment).\&quot; We recommend creating a review comment using &#x60;line&#x60;, &#x60;side&#x60;, and optionally &#x60;start_line&#x60; and &#x60;start_side&#x60; if your comment applies to more than one line in the pull request diff.  You can still create a review comment using the &#x60;position&#x60; parameter. When you use &#x60;position&#x60;, the &#x60;line&#x60;, &#x60;side&#x60;, &#x60;start_line&#x60;, and &#x60;start_side&#x60; parameters are not required. For more information, see the [&#x60;comfort-fade&#x60; preview notice](https://docs.github.com/enterprise-server@2.20/rest/reference/pulls#create-a-review-comment-for-a-pull-request-preview-notices).  **Note:** The position value equals the number of lines down from the first \&quot;@@\&quot; hunk header in the file you want to add a comment. The line just below the \&quot;@@\&quot; line is position 1, the next line is position 2, and so on. The position in the diff continues to increase through lines of whitespace and additional hunks until the beginning of a new file.  This endpoint triggers [notifications](https://docs.github.com/en/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See \&quot;[Secondary rate limits](https://docs.github.com/enterprise-server@2.20/rest/overview/resources-in-the-rest-api#secondary-rate-limits)\&quot; and \&quot;[Dealing with secondary rate limits](https://docs.github.com/enterprise-server@2.20/rest/guides/best-practices-for-integrators#dealing-with-secondary-rate-limits)\&quot; for details.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.PullsApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let pullNumber = 56; // Number | 
let pullsCreateReviewCommentRequest = {"body":"Great stuff!","commit_id":"6dcb09b5b57875f334f61aebed695e2e4193db5e","line":2,"path":"file1.txt","side":"RIGHT","start_line":1,"start_side":"RIGHT"}; // PullsCreateReviewCommentRequest | 
apiInstance.pullsCreateReviewComment(owner, repo, pullNumber, pullsCreateReviewCommentRequest, (error, data, response) => {
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
 **pullNumber** | **Number**|  | 
 **pullsCreateReviewCommentRequest** | [**PullsCreateReviewCommentRequest**](PullsCreateReviewCommentRequest.md)|  | 

### Return type

[**PullRequestReviewComment**](PullRequestReviewComment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## pullsDeletePendingReview

> PullRequestReview pullsDeletePendingReview(owner, repo, pullNumber, reviewId)

Delete a pending review for a pull request



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.PullsApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let pullNumber = 56; // Number | 
let reviewId = 56; // Number | review_id parameter
apiInstance.pullsDeletePendingReview(owner, repo, pullNumber, reviewId, (error, data, response) => {
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
 **pullNumber** | **Number**|  | 
 **reviewId** | **Number**| review_id parameter | 

### Return type

[**PullRequestReview**](PullRequestReview.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## pullsDeleteReviewComment

> pullsDeleteReviewComment(owner, repo, commentId)

Delete a review comment for a pull request

Deletes a review comment.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.PullsApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let commentId = 56; // Number | comment_id parameter
apiInstance.pullsDeleteReviewComment(owner, repo, commentId, (error, data, response) => {
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
 **owner** | **String**|  | 
 **repo** | **String**|  | 
 **commentId** | **Number**| comment_id parameter | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## pullsDismissReview

> PullRequestReview pullsDismissReview(owner, repo, pullNumber, reviewId, pullsDismissReviewRequest)

Dismiss a review for a pull request

**Note:** To dismiss a pull request review on a [protected branch](https://docs.github.com/enterprise-server@2.20/rest/reference/repos#branches), you must be a repository administrator or be included in the list of people or teams who can dismiss pull request reviews.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.PullsApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let pullNumber = 56; // Number | 
let reviewId = 56; // Number | review_id parameter
let pullsDismissReviewRequest = new GitHubV3RestApi.PullsDismissReviewRequest(); // PullsDismissReviewRequest | 
apiInstance.pullsDismissReview(owner, repo, pullNumber, reviewId, pullsDismissReviewRequest, (error, data, response) => {
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
 **pullNumber** | **Number**|  | 
 **reviewId** | **Number**| review_id parameter | 
 **pullsDismissReviewRequest** | [**PullsDismissReviewRequest**](PullsDismissReviewRequest.md)|  | 

### Return type

[**PullRequestReview**](PullRequestReview.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## pullsGet

> PullRequest pullsGet(owner, repo, pullNumber)

Get a pull request

Draft pull requests are available in public repositories with GitHub Free and GitHub Free for organizations, GitHub Pro, and legacy per-repository billing plans, and in public and private repositories with GitHub Team and GitHub Enterprise Cloud. For more information, see [GitHub&#39;s products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Lists details of a pull request by providing its number.  When you get, [create](https://docs.github.com/enterprise-server@2.20/rest/reference/pulls/#create-a-pull-request), or [edit](https://docs.github.com/enterprise-server@2.20/rest/reference/pulls#update-a-pull-request) a pull request, GitHub Enterprise Server creates a merge commit to test whether the pull request can be automatically merged into the base branch. This test commit is not added to the base branch or the head branch. You can review the status of the test commit using the &#x60;mergeable&#x60; key. For more information, see \&quot;[Checking mergeability of pull requests](https://docs.github.com/enterprise-server@2.20/rest/guides/getting-started-with-the-git-database-api#checking-mergeability-of-pull-requests)\&quot;.  The value of the &#x60;mergeable&#x60; attribute can be &#x60;true&#x60;, &#x60;false&#x60;, or &#x60;null&#x60;. If the value is &#x60;null&#x60;, then GitHub Enterprise Server has started a background job to compute the mergeability. After giving the job time to complete, resubmit the request. When the job finishes, you will see a non-&#x60;null&#x60; value for the &#x60;mergeable&#x60; attribute in the response. If &#x60;mergeable&#x60; is &#x60;true&#x60;, then &#x60;merge_commit_sha&#x60; will be the SHA of the _test_ merge commit.  The value of the &#x60;merge_commit_sha&#x60; attribute changes depending on the state of the pull request. Before merging a pull request, the &#x60;merge_commit_sha&#x60; attribute holds the SHA of the _test_ merge commit. After merging a pull request, the &#x60;merge_commit_sha&#x60; attribute changes depending on how you merged the pull request:  *   If merged as a [merge commit](https://help.github.com/articles/about-merge-methods-on-github/), &#x60;merge_commit_sha&#x60; represents the SHA of the merge commit. *   If merged via a [squash](https://help.github.com/articles/about-merge-methods-on-github/#squashing-your-merge-commits), &#x60;merge_commit_sha&#x60; represents the SHA of the squashed commit on the base branch. *   If [rebased](https://help.github.com/articles/about-merge-methods-on-github/#rebasing-and-merging-your-commits), &#x60;merge_commit_sha&#x60; represents the commit that the base branch was updated to.  Pass the appropriate [media type](https://docs.github.com/enterprise-server@2.20/rest/overview/media-types/#commits-commit-comparison-and-pull-requests) to fetch diff and patch formats.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.PullsApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let pullNumber = 56; // Number | 
apiInstance.pullsGet(owner, repo, pullNumber, (error, data, response) => {
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
 **pullNumber** | **Number**|  | 

### Return type

[**PullRequest**](PullRequest.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## pullsGetReview

> PullRequestReview pullsGetReview(owner, repo, pullNumber, reviewId)

Get a review for a pull request



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.PullsApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let pullNumber = 56; // Number | 
let reviewId = 56; // Number | review_id parameter
apiInstance.pullsGetReview(owner, repo, pullNumber, reviewId, (error, data, response) => {
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
 **pullNumber** | **Number**|  | 
 **reviewId** | **Number**| review_id parameter | 

### Return type

[**PullRequestReview**](PullRequestReview.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## pullsGetReviewComment

> PullRequestReviewComment pullsGetReviewComment(owner, repo, commentId)

Get a review comment for a pull request

Provides details for a review comment.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.PullsApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let commentId = 56; // Number | comment_id parameter
apiInstance.pullsGetReviewComment(owner, repo, commentId, (error, data, response) => {
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

### Return type

[**PullRequestReviewComment**](PullRequestReviewComment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## pullsList

> [PullRequestSimple] pullsList(owner, repo, opts)

List pull requests

Draft pull requests are available in public repositories with GitHub Free and GitHub Free for organizations, GitHub Pro, and legacy per-repository billing plans, and in public and private repositories with GitHub Team, GitHub Enterprise Server 2.17+, and GitHub Enterprise Cloud.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.PullsApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let opts = {
  'state': "'open'", // String | Either `open`, `closed`, or `all` to filter by state.
  'head': "head_example", // String | Filter pulls by head user or head organization and branch name in the format of `user:ref-name` or `organization:ref-name`. For example: `github:new-script-format` or `octocat:test-branch`.
  'base': "base_example", // String | Filter pulls by base branch name. Example: `gh-pages`.
  'sort': "'created'", // String | What to sort results by. Can be either `created`, `updated`, `popularity` (comment count) or `long-running` (age, filtering by pulls updated in the last month).
  'direction': "direction_example", // String | The direction of the sort. Can be either `asc` or `desc`. Default: `desc` when sort is `created` or sort is not specified, otherwise `asc`.
  'perPage': 30, // Number | Results per page (max 100)
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.pullsList(owner, repo, opts, (error, data, response) => {
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
 **state** | **String**| Either &#x60;open&#x60;, &#x60;closed&#x60;, or &#x60;all&#x60; to filter by state. | [optional] [default to &#39;open&#39;]
 **head** | **String**| Filter pulls by head user or head organization and branch name in the format of &#x60;user:ref-name&#x60; or &#x60;organization:ref-name&#x60;. For example: &#x60;github:new-script-format&#x60; or &#x60;octocat:test-branch&#x60;. | [optional] 
 **base** | **String**| Filter pulls by base branch name. Example: &#x60;gh-pages&#x60;. | [optional] 
 **sort** | **String**| What to sort results by. Can be either &#x60;created&#x60;, &#x60;updated&#x60;, &#x60;popularity&#x60; (comment count) or &#x60;long-running&#x60; (age, filtering by pulls updated in the last month). | [optional] [default to &#39;created&#39;]
 **direction** | **String**| The direction of the sort. Can be either &#x60;asc&#x60; or &#x60;desc&#x60;. Default: &#x60;desc&#x60; when sort is &#x60;created&#x60; or sort is not specified, otherwise &#x60;asc&#x60;. | [optional] 
 **perPage** | **Number**| Results per page (max 100) | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[PullRequestSimple]**](PullRequestSimple.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## pullsListCommentsForReview

> [ReviewComment] pullsListCommentsForReview(owner, repo, pullNumber, reviewId, opts)

List comments for a pull request review

List comments for a specific pull request review.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.PullsApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let pullNumber = 56; // Number | 
let reviewId = 56; // Number | review_id parameter
let opts = {
  'perPage': 30, // Number | Results per page (max 100)
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.pullsListCommentsForReview(owner, repo, pullNumber, reviewId, opts, (error, data, response) => {
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
 **pullNumber** | **Number**|  | 
 **reviewId** | **Number**| review_id parameter | 
 **perPage** | **Number**| Results per page (max 100) | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[ReviewComment]**](ReviewComment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## pullsListCommits

> [Commit] pullsListCommits(owner, repo, pullNumber, opts)

List commits on a pull request

Lists a maximum of 250 commits for a pull request. To receive a complete commit list for pull requests with more than 250 commits, use the [List commits](https://docs.github.com/enterprise-server@2.20/rest/reference/repos#list-commits) endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.PullsApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let pullNumber = 56; // Number | 
let opts = {
  'perPage': 30, // Number | Results per page (max 100)
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.pullsListCommits(owner, repo, pullNumber, opts, (error, data, response) => {
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
 **pullNumber** | **Number**|  | 
 **perPage** | **Number**| Results per page (max 100) | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[Commit]**](Commit.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## pullsListFiles

> [DiffEntry] pullsListFiles(owner, repo, pullNumber, opts)

List pull requests files

**Note:** Responses include a maximum of 3000 files. The paginated response returns 30 files per page by default.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.PullsApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let pullNumber = 56; // Number | 
let opts = {
  'perPage': 30, // Number | Results per page (max 100)
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.pullsListFiles(owner, repo, pullNumber, opts, (error, data, response) => {
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
 **pullNumber** | **Number**|  | 
 **perPage** | **Number**| Results per page (max 100) | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[DiffEntry]**](DiffEntry.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## pullsListRequestedReviewers

> PullRequestReviewRequest pullsListRequestedReviewers(owner, repo, pullNumber, opts)

List requested reviewers for a pull request



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.PullsApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let pullNumber = 56; // Number | 
let opts = {
  'perPage': 30, // Number | Results per page (max 100)
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.pullsListRequestedReviewers(owner, repo, pullNumber, opts, (error, data, response) => {
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
 **pullNumber** | **Number**|  | 
 **perPage** | **Number**| Results per page (max 100) | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**PullRequestReviewRequest**](PullRequestReviewRequest.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## pullsListReviewComments

> [PullRequestReviewComment] pullsListReviewComments(owner, repo, pullNumber, opts)

List review comments on a pull request

Lists all review comments for a pull request. By default, review comments are in ascending order by ID.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.PullsApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let pullNumber = 56; // Number | 
let opts = {
  'sort': "'created'", // String | One of `created` (when the repository was starred) or `updated` (when it was last pushed to).
  'direction': "direction_example", // String | Can be either `asc` or `desc`. Ignored without `sort` parameter.
  'since': new Date("2013-10-20T19:20:30+01:00"), // Date | Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
  'perPage': 30, // Number | Results per page (max 100)
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.pullsListReviewComments(owner, repo, pullNumber, opts, (error, data, response) => {
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
 **pullNumber** | **Number**|  | 
 **sort** | **String**| One of &#x60;created&#x60; (when the repository was starred) or &#x60;updated&#x60; (when it was last pushed to). | [optional] [default to &#39;created&#39;]
 **direction** | **String**| Can be either &#x60;asc&#x60; or &#x60;desc&#x60;. Ignored without &#x60;sort&#x60; parameter. | [optional] 
 **since** | **Date**| Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] 
 **perPage** | **Number**| Results per page (max 100) | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[PullRequestReviewComment]**](PullRequestReviewComment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## pullsListReviewCommentsForRepo

> [PullRequestReviewComment] pullsListReviewCommentsForRepo(owner, repo, opts)

List review comments in a repository

Lists review comments for all pull requests in a repository. By default, review comments are in ascending order by ID.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.PullsApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let opts = {
  'sort': "sort_example", // String | 
  'direction': "direction_example", // String | Can be either `asc` or `desc`. Ignored without `sort` parameter.
  'since': new Date("2013-10-20T19:20:30+01:00"), // Date | Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
  'perPage': 30, // Number | Results per page (max 100)
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.pullsListReviewCommentsForRepo(owner, repo, opts, (error, data, response) => {
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
 **sort** | **String**|  | [optional] 
 **direction** | **String**| Can be either &#x60;asc&#x60; or &#x60;desc&#x60;. Ignored without &#x60;sort&#x60; parameter. | [optional] 
 **since** | **Date**| Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] 
 **perPage** | **Number**| Results per page (max 100) | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[PullRequestReviewComment]**](PullRequestReviewComment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## pullsListReviews

> [PullRequestReview] pullsListReviews(owner, repo, pullNumber, opts)

List reviews for a pull request

The list of reviews returns in chronological order.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.PullsApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let pullNumber = 56; // Number | 
let opts = {
  'perPage': 30, // Number | Results per page (max 100)
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.pullsListReviews(owner, repo, pullNumber, opts, (error, data, response) => {
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
 **pullNumber** | **Number**|  | 
 **perPage** | **Number**| Results per page (max 100) | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[PullRequestReview]**](PullRequestReview.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## pullsMerge

> PullRequestMergeResult pullsMerge(owner, repo, pullNumber, opts)

Merge a pull request

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.PullsApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let pullNumber = 56; // Number | 
let opts = {
  'pullsMergeRequest': new GitHubV3RestApi.PullsMergeRequest() // PullsMergeRequest | 
};
apiInstance.pullsMerge(owner, repo, pullNumber, opts, (error, data, response) => {
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
 **pullNumber** | **Number**|  | 
 **pullsMergeRequest** | [**PullsMergeRequest**](PullsMergeRequest.md)|  | [optional] 

### Return type

[**PullRequestMergeResult**](PullRequestMergeResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## pullsRemoveRequestedReviewers

> PullRequestSimple pullsRemoveRequestedReviewers(owner, repo, pullNumber, pullsRemoveRequestedReviewersRequest)

Remove requested reviewers from a pull request



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.PullsApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let pullNumber = 56; // Number | 
let pullsRemoveRequestedReviewersRequest = {"reviewers":["octocat","hubot","other_user"],"team_reviewers":["justice-league"]}; // PullsRemoveRequestedReviewersRequest | 
apiInstance.pullsRemoveRequestedReviewers(owner, repo, pullNumber, pullsRemoveRequestedReviewersRequest, (error, data, response) => {
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
 **pullNumber** | **Number**|  | 
 **pullsRemoveRequestedReviewersRequest** | [**PullsRemoveRequestedReviewersRequest**](PullsRemoveRequestedReviewersRequest.md)|  | 

### Return type

[**PullRequestSimple**](PullRequestSimple.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## pullsRequestReviewers

> PullRequestSimple pullsRequestReviewers(owner, repo, pullNumber, opts)

Request reviewers for a pull request

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.PullsApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let pullNumber = 56; // Number | 
let opts = {
  'pullsRequestReviewersRequest': {"reviewers":["octocat","hubot","other_user"],"team_reviewers":["justice-league"]} // PullsRequestReviewersRequest | 
};
apiInstance.pullsRequestReviewers(owner, repo, pullNumber, opts, (error, data, response) => {
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
 **pullNumber** | **Number**|  | 
 **pullsRequestReviewersRequest** | [**PullsRequestReviewersRequest**](PullsRequestReviewersRequest.md)|  | [optional] 

### Return type

[**PullRequestSimple**](PullRequestSimple.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## pullsSubmitReview

> PullRequestReview pullsSubmitReview(owner, repo, pullNumber, reviewId, pullsSubmitReviewRequest)

Submit a review for a pull request



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.PullsApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let pullNumber = 56; // Number | 
let reviewId = 56; // Number | review_id parameter
let pullsSubmitReviewRequest = new GitHubV3RestApi.PullsSubmitReviewRequest(); // PullsSubmitReviewRequest | 
apiInstance.pullsSubmitReview(owner, repo, pullNumber, reviewId, pullsSubmitReviewRequest, (error, data, response) => {
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
 **pullNumber** | **Number**|  | 
 **reviewId** | **Number**| review_id parameter | 
 **pullsSubmitReviewRequest** | [**PullsSubmitReviewRequest**](PullsSubmitReviewRequest.md)|  | 

### Return type

[**PullRequestReview**](PullRequestReview.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## pullsUpdate

> PullRequest pullsUpdate(owner, repo, pullNumber, opts)

Update a pull request

Draft pull requests are available in public repositories with GitHub Free and GitHub Free for organizations, GitHub Pro, and legacy per-repository billing plans, and in public and private repositories with GitHub Team, GitHub Enterprise Server 2.17+, and GitHub Enterprise Cloud.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.PullsApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let pullNumber = 56; // Number | 
let opts = {
  'pullsUpdateRequest': {"base":"master","body":"updated body","state":"open","title":"new title"} // PullsUpdateRequest | 
};
apiInstance.pullsUpdate(owner, repo, pullNumber, opts, (error, data, response) => {
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
 **pullNumber** | **Number**|  | 
 **pullsUpdateRequest** | [**PullsUpdateRequest**](PullsUpdateRequest.md)|  | [optional] 

### Return type

[**PullRequest**](PullRequest.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## pullsUpdateBranch

> EnterpriseAdminUpdateOrgName202Response pullsUpdateBranch(owner, repo, pullNumber, opts)

Update a pull request branch

Updates the pull request branch with the latest upstream changes by merging HEAD from the base branch into the pull request branch.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.PullsApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let pullNumber = 56; // Number | 
let opts = {
  'pullsUpdateBranchRequest': {"expected_head_sha":"6dcb09b5b57875f334f61aebed695e2e4193db5e"} // PullsUpdateBranchRequest | 
};
apiInstance.pullsUpdateBranch(owner, repo, pullNumber, opts, (error, data, response) => {
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
 **pullNumber** | **Number**|  | 
 **pullsUpdateBranchRequest** | [**PullsUpdateBranchRequest**](PullsUpdateBranchRequest.md)|  | [optional] 

### Return type

[**EnterpriseAdminUpdateOrgName202Response**](EnterpriseAdminUpdateOrgName202Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## pullsUpdateReview

> PullRequestReview pullsUpdateReview(owner, repo, pullNumber, reviewId, pullsUpdateReviewRequest)

Update a review for a pull request

Update the review summary comment with new text.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.PullsApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let pullNumber = 56; // Number | 
let reviewId = 56; // Number | review_id parameter
let pullsUpdateReviewRequest = {"body":"This is close to perfect! Please address the suggested inline change. And add more about this."}; // PullsUpdateReviewRequest | 
apiInstance.pullsUpdateReview(owner, repo, pullNumber, reviewId, pullsUpdateReviewRequest, (error, data, response) => {
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
 **pullNumber** | **Number**|  | 
 **reviewId** | **Number**| review_id parameter | 
 **pullsUpdateReviewRequest** | [**PullsUpdateReviewRequest**](PullsUpdateReviewRequest.md)|  | 

### Return type

[**PullRequestReview**](PullRequestReview.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## pullsUpdateReviewComment

> PullRequestReviewComment pullsUpdateReviewComment(owner, repo, commentId, pullsUpdateReviewCommentRequest)

Update a review comment for a pull request

Enables you to edit a review comment.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.PullsApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let commentId = 56; // Number | comment_id parameter
let pullsUpdateReviewCommentRequest = {"body":"I like this too!"}; // PullsUpdateReviewCommentRequest | 
apiInstance.pullsUpdateReviewComment(owner, repo, commentId, pullsUpdateReviewCommentRequest, (error, data, response) => {
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
 **pullsUpdateReviewCommentRequest** | [**PullsUpdateReviewCommentRequest**](PullsUpdateReviewCommentRequest.md)|  | 

### Return type

[**PullRequestReviewComment**](PullRequestReviewComment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

