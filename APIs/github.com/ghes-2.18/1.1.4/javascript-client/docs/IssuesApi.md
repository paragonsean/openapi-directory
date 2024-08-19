# GitHubV3RestApi.IssuesApi

All URIs are relative to *http://HOSTNAME/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**issuesAddAssignees**](IssuesApi.md#issuesAddAssignees) | **POST** /repos/{owner}/{repo}/issues/{issue_number}/assignees | Add assignees to an issue
[**issuesAddLabels**](IssuesApi.md#issuesAddLabels) | **POST** /repos/{owner}/{repo}/issues/{issue_number}/labels | Add labels to an issue
[**issuesCheckUserCanBeAssigned**](IssuesApi.md#issuesCheckUserCanBeAssigned) | **GET** /repos/{owner}/{repo}/assignees/{assignee} | Check if a user can be assigned
[**issuesCreate**](IssuesApi.md#issuesCreate) | **POST** /repos/{owner}/{repo}/issues | Create an issue
[**issuesCreateComment**](IssuesApi.md#issuesCreateComment) | **POST** /repos/{owner}/{repo}/issues/{issue_number}/comments | Create an issue comment
[**issuesCreateLabel**](IssuesApi.md#issuesCreateLabel) | **POST** /repos/{owner}/{repo}/labels | Create a label
[**issuesCreateMilestone**](IssuesApi.md#issuesCreateMilestone) | **POST** /repos/{owner}/{repo}/milestones | Create a milestone
[**issuesDeleteComment**](IssuesApi.md#issuesDeleteComment) | **DELETE** /repos/{owner}/{repo}/issues/comments/{comment_id} | Delete an issue comment
[**issuesDeleteLabel**](IssuesApi.md#issuesDeleteLabel) | **DELETE** /repos/{owner}/{repo}/labels/{name} | Delete a label
[**issuesDeleteMilestone**](IssuesApi.md#issuesDeleteMilestone) | **DELETE** /repos/{owner}/{repo}/milestones/{milestone_number} | Delete a milestone
[**issuesGet**](IssuesApi.md#issuesGet) | **GET** /repos/{owner}/{repo}/issues/{issue_number} | Get an issue
[**issuesGetComment**](IssuesApi.md#issuesGetComment) | **GET** /repos/{owner}/{repo}/issues/comments/{comment_id} | Get an issue comment
[**issuesGetEvent**](IssuesApi.md#issuesGetEvent) | **GET** /repos/{owner}/{repo}/issues/events/{event_id} | Get an issue event
[**issuesGetLabel**](IssuesApi.md#issuesGetLabel) | **GET** /repos/{owner}/{repo}/labels/{name} | Get a label
[**issuesGetMilestone**](IssuesApi.md#issuesGetMilestone) | **GET** /repos/{owner}/{repo}/milestones/{milestone_number} | Get a milestone
[**issuesList**](IssuesApi.md#issuesList) | **GET** /issues | List issues assigned to the authenticated user
[**issuesListAssignees**](IssuesApi.md#issuesListAssignees) | **GET** /repos/{owner}/{repo}/assignees | List assignees
[**issuesListComments**](IssuesApi.md#issuesListComments) | **GET** /repos/{owner}/{repo}/issues/{issue_number}/comments | List issue comments
[**issuesListCommentsForRepo**](IssuesApi.md#issuesListCommentsForRepo) | **GET** /repos/{owner}/{repo}/issues/comments | List issue comments for a repository
[**issuesListEvents**](IssuesApi.md#issuesListEvents) | **GET** /repos/{owner}/{repo}/issues/{issue_number}/events | List issue events
[**issuesListEventsForRepo**](IssuesApi.md#issuesListEventsForRepo) | **GET** /repos/{owner}/{repo}/issues/events | List issue events for a repository
[**issuesListEventsForTimeline**](IssuesApi.md#issuesListEventsForTimeline) | **GET** /repos/{owner}/{repo}/issues/{issue_number}/timeline | List timeline events for an issue
[**issuesListForAuthenticatedUser**](IssuesApi.md#issuesListForAuthenticatedUser) | **GET** /user/issues | List user account issues assigned to the authenticated user
[**issuesListForOrg**](IssuesApi.md#issuesListForOrg) | **GET** /orgs/{org}/issues | List organization issues assigned to the authenticated user
[**issuesListForRepo**](IssuesApi.md#issuesListForRepo) | **GET** /repos/{owner}/{repo}/issues | List repository issues
[**issuesListLabelsForMilestone**](IssuesApi.md#issuesListLabelsForMilestone) | **GET** /repos/{owner}/{repo}/milestones/{milestone_number}/labels | List labels for issues in a milestone
[**issuesListLabelsForRepo**](IssuesApi.md#issuesListLabelsForRepo) | **GET** /repos/{owner}/{repo}/labels | List labels for a repository
[**issuesListLabelsOnIssue**](IssuesApi.md#issuesListLabelsOnIssue) | **GET** /repos/{owner}/{repo}/issues/{issue_number}/labels | List labels for an issue
[**issuesListMilestones**](IssuesApi.md#issuesListMilestones) | **GET** /repos/{owner}/{repo}/milestones | List milestones
[**issuesLock**](IssuesApi.md#issuesLock) | **PUT** /repos/{owner}/{repo}/issues/{issue_number}/lock | Lock an issue
[**issuesRemoveAllLabels**](IssuesApi.md#issuesRemoveAllLabels) | **DELETE** /repos/{owner}/{repo}/issues/{issue_number}/labels | Remove all labels from an issue
[**issuesRemoveAssignees**](IssuesApi.md#issuesRemoveAssignees) | **DELETE** /repos/{owner}/{repo}/issues/{issue_number}/assignees | Remove assignees from an issue
[**issuesRemoveLabel**](IssuesApi.md#issuesRemoveLabel) | **DELETE** /repos/{owner}/{repo}/issues/{issue_number}/labels/{name} | Remove a label from an issue
[**issuesSetLabels**](IssuesApi.md#issuesSetLabels) | **PUT** /repos/{owner}/{repo}/issues/{issue_number}/labels | Set labels for an issue
[**issuesUnlock**](IssuesApi.md#issuesUnlock) | **DELETE** /repos/{owner}/{repo}/issues/{issue_number}/lock | Unlock an issue
[**issuesUpdate**](IssuesApi.md#issuesUpdate) | **PATCH** /repos/{owner}/{repo}/issues/{issue_number} | Update an issue
[**issuesUpdateComment**](IssuesApi.md#issuesUpdateComment) | **PATCH** /repos/{owner}/{repo}/issues/comments/{comment_id} | Update an issue comment
[**issuesUpdateMilestone**](IssuesApi.md#issuesUpdateMilestone) | **PATCH** /repos/{owner}/{repo}/milestones/{milestone_number} | Update a milestone



## issuesAddAssignees

> IssueSimple issuesAddAssignees(owner, repo, issueNumber, opts)

Add assignees to an issue

Adds up to 10 assignees to an issue. Users already assigned to an issue are not replaced.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.IssuesApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let issueNumber = 56; // Number | issue_number parameter
let opts = {
  'issuesAddAssigneesRequest': {"assignees":["hubot","other_user"]} // IssuesAddAssigneesRequest | 
};
apiInstance.issuesAddAssignees(owner, repo, issueNumber, opts, (error, data, response) => {
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
 **issuesAddAssigneesRequest** | [**IssuesAddAssigneesRequest**](IssuesAddAssigneesRequest.md)|  | [optional] 

### Return type

[**IssueSimple**](IssueSimple.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## issuesAddLabels

> [Label] issuesAddLabels(owner, repo, issueNumber, opts)

Add labels to an issue



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.IssuesApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let issueNumber = 56; // Number | issue_number parameter
let opts = {
  'issuesSetLabelsRequest': {"labels":["bug","enhancement"]} // IssuesSetLabelsRequest | 
};
apiInstance.issuesAddLabels(owner, repo, issueNumber, opts, (error, data, response) => {
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
 **issuesSetLabelsRequest** | [**IssuesSetLabelsRequest**](IssuesSetLabelsRequest.md)|  | [optional] 

### Return type

[**[Label]**](Label.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## issuesCheckUserCanBeAssigned

> issuesCheckUserCanBeAssigned(owner, repo, assignee)

Check if a user can be assigned

Checks if a user has permission to be assigned to an issue in this repository.  If the &#x60;assignee&#x60; can be assigned to issues in the repository, a &#x60;204&#x60; header with no content is returned.  Otherwise a &#x60;404&#x60; status code is returned.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.IssuesApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let assignee = "assignee_example"; // String | 
apiInstance.issuesCheckUserCanBeAssigned(owner, repo, assignee, (error, data, response) => {
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
 **assignee** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## issuesCreate

> Issue issuesCreate(owner, repo, issuesCreateRequest)

Create an issue

Any user with pull access to a repository can create an issue. If [issues are disabled in the repository](https://help.github.com/articles/disabling-issues/), the API returns a &#x60;410 Gone&#x60; status.  This endpoint triggers [notifications](https://docs.github.com/en/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See \&quot;[Secondary rate limits](https://docs.github.com/enterprise-server@2.18/rest/overview/resources-in-the-rest-api#secondary-rate-limits)\&quot; and \&quot;[Dealing with secondary rate limits](https://docs.github.com/enterprise-server@2.18/rest/guides/best-practices-for-integrators#dealing-with-secondary-rate-limits)\&quot; for details.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.IssuesApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let issuesCreateRequest = {"assignees":["octocat"],"body":"I'm having a problem with this.","labels":["bug"],"milestone":1,"title":"Found a bug"}; // IssuesCreateRequest | 
apiInstance.issuesCreate(owner, repo, issuesCreateRequest, (error, data, response) => {
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
 **issuesCreateRequest** | [**IssuesCreateRequest**](IssuesCreateRequest.md)|  | 

### Return type

[**Issue**](Issue.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## issuesCreateComment

> IssueComment issuesCreateComment(owner, repo, issueNumber, issuesUpdateCommentRequest)

Create an issue comment

This endpoint triggers [notifications](https://docs.github.com/en/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See \&quot;[Secondary rate limits](https://docs.github.com/enterprise-server@2.18/rest/overview/resources-in-the-rest-api#secondary-rate-limits)\&quot; and \&quot;[Dealing with secondary rate limits](https://docs.github.com/enterprise-server@2.18/rest/guides/best-practices-for-integrators#dealing-with-secondary-rate-limits)\&quot; for details.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.IssuesApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let issueNumber = 56; // Number | issue_number parameter
let issuesUpdateCommentRequest = {"body":"Me too"}; // IssuesUpdateCommentRequest | 
apiInstance.issuesCreateComment(owner, repo, issueNumber, issuesUpdateCommentRequest, (error, data, response) => {
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
 **issuesUpdateCommentRequest** | [**IssuesUpdateCommentRequest**](IssuesUpdateCommentRequest.md)|  | 

### Return type

[**IssueComment**](IssueComment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## issuesCreateLabel

> Label issuesCreateLabel(owner, repo, issuesCreateLabelRequest)

Create a label



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.IssuesApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let issuesCreateLabelRequest = {"color":"f29513","description":"Something isn't working","name":"bug"}; // IssuesCreateLabelRequest | 
apiInstance.issuesCreateLabel(owner, repo, issuesCreateLabelRequest, (error, data, response) => {
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
 **issuesCreateLabelRequest** | [**IssuesCreateLabelRequest**](IssuesCreateLabelRequest.md)|  | 

### Return type

[**Label**](Label.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## issuesCreateMilestone

> Milestone issuesCreateMilestone(owner, repo, issuesCreateMilestoneRequest)

Create a milestone



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.IssuesApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let issuesCreateMilestoneRequest = {"description":"Tracking milestone for version 1.0","due_on":"2012-10-09T23:39:01Z","state":"open","title":"v1.0"}; // IssuesCreateMilestoneRequest | 
apiInstance.issuesCreateMilestone(owner, repo, issuesCreateMilestoneRequest, (error, data, response) => {
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
 **issuesCreateMilestoneRequest** | [**IssuesCreateMilestoneRequest**](IssuesCreateMilestoneRequest.md)|  | 

### Return type

[**Milestone**](Milestone.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## issuesDeleteComment

> issuesDeleteComment(owner, repo, commentId)

Delete an issue comment



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.IssuesApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let commentId = 56; // Number | comment_id parameter
apiInstance.issuesDeleteComment(owner, repo, commentId, (error, data, response) => {
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
- **Accept**: Not defined


## issuesDeleteLabel

> issuesDeleteLabel(owner, repo, name)

Delete a label



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.IssuesApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let name = "name_example"; // String | 
apiInstance.issuesDeleteLabel(owner, repo, name, (error, data, response) => {
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
 **name** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## issuesDeleteMilestone

> issuesDeleteMilestone(owner, repo, milestoneNumber)

Delete a milestone



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.IssuesApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let milestoneNumber = 56; // Number | milestone_number parameter
apiInstance.issuesDeleteMilestone(owner, repo, milestoneNumber, (error, data, response) => {
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
 **milestoneNumber** | **Number**| milestone_number parameter | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## issuesGet

> Issue issuesGet(owner, repo, issueNumber)

Get an issue

The API returns a [&#x60;301 Moved Permanently&#x60; status](https://docs.github.com/enterprise-server@2.18/rest/overview/resources-in-the-rest-api#http-redirects-redirects) if the issue was [transferred](https://help.github.com/articles/transferring-an-issue-to-another-repository/) to another repository. If the issue was transferred to or deleted from a repository where the authenticated user lacks read access, the API returns a &#x60;404 Not Found&#x60; status. If the issue was deleted from a repository where the authenticated user has read access, the API returns a &#x60;410 Gone&#x60; status. To receive webhook events for transferred and deleted issues, subscribe to the [&#x60;issues&#x60;](https://docs.github.com/enterprise-server@2.18/webhooks/event-payloads/#issues) webhook.  **Note**: GitHub&#39;s REST API v3 considers every pull request an issue, but not every issue is a pull request. For this reason, \&quot;Issues\&quot; endpoints may return both issues and pull requests in the response. You can identify pull requests by the &#x60;pull_request&#x60; key. Be aware that the &#x60;id&#x60; of a pull request returned from \&quot;Issues\&quot; endpoints will be an _issue id_. To find out the pull request id, use the \&quot;[List pull requests](https://docs.github.com/enterprise-server@2.18/rest/reference/pulls#list-pull-requests)\&quot; endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.IssuesApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let issueNumber = 56; // Number | issue_number parameter
apiInstance.issuesGet(owner, repo, issueNumber, (error, data, response) => {
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

### Return type

[**Issue**](Issue.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## issuesGetComment

> IssueComment issuesGetComment(owner, repo, commentId)

Get an issue comment



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.IssuesApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let commentId = 56; // Number | comment_id parameter
apiInstance.issuesGetComment(owner, repo, commentId, (error, data, response) => {
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

[**IssueComment**](IssueComment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## issuesGetEvent

> IssueEvent issuesGetEvent(owner, repo, eventId)

Get an issue event



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.IssuesApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let eventId = 56; // Number | 
apiInstance.issuesGetEvent(owner, repo, eventId, (error, data, response) => {
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
 **eventId** | **Number**|  | 

### Return type

[**IssueEvent**](IssueEvent.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## issuesGetLabel

> Label issuesGetLabel(owner, repo, name)

Get a label



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.IssuesApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let name = "name_example"; // String | 
apiInstance.issuesGetLabel(owner, repo, name, (error, data, response) => {
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
 **name** | **String**|  | 

### Return type

[**Label**](Label.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## issuesGetMilestone

> Milestone issuesGetMilestone(owner, repo, milestoneNumber)

Get a milestone



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.IssuesApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let milestoneNumber = 56; // Number | milestone_number parameter
apiInstance.issuesGetMilestone(owner, repo, milestoneNumber, (error, data, response) => {
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
 **milestoneNumber** | **Number**| milestone_number parameter | 

### Return type

[**Milestone**](Milestone.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## issuesList

> [Issue] issuesList(opts)

List issues assigned to the authenticated user

List issues assigned to the authenticated user across all visible repositories including owned repositories, member repositories, and organization repositories. You can use the &#x60;filter&#x60; query parameter to fetch issues that are not necessarily assigned to you.   **Note**: GitHub&#39;s REST API v3 considers every pull request an issue, but not every issue is a pull request. For this reason, \&quot;Issues\&quot; endpoints may return both issues and pull requests in the response. You can identify pull requests by the &#x60;pull_request&#x60; key. Be aware that the &#x60;id&#x60; of a pull request returned from \&quot;Issues\&quot; endpoints will be an _issue id_. To find out the pull request id, use the \&quot;[List pull requests](https://docs.github.com/enterprise-server@2.18/rest/reference/pulls#list-pull-requests)\&quot; endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.IssuesApi();
let opts = {
  'filter': "'assigned'", // String | Indicates which sorts of issues to return. Can be one of:   \\* `assigned`: Issues assigned to you   \\* `created`: Issues created by you   \\* `mentioned`: Issues mentioning you   \\* `subscribed`: Issues you're subscribed to updates for   \\* `all` or `repos`: All issues the authenticated user can see, regardless of participation or creation
  'state': "'open'", // String | Indicates the state of the issues to return. Can be either `open`, `closed`, or `all`.
  'labels': "labels_example", // String | A list of comma separated label names. Example: `bug,ui,@high`
  'sort': "'created'", // String | What to sort results by. Can be either `created`, `updated`, `comments`.
  'direction': "'desc'", // String | One of `asc` (ascending) or `desc` (descending).
  'since': new Date("2013-10-20T19:20:30+01:00"), // Date | Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
  'collab': true, // Boolean | 
  'orgs': true, // Boolean | 
  'owned': true, // Boolean | 
  'pulls': true, // Boolean | 
  'perPage': 30, // Number | Results per page (max 100)
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.issuesList(opts, (error, data, response) => {
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
 **filter** | **String**| Indicates which sorts of issues to return. Can be one of:   \\* &#x60;assigned&#x60;: Issues assigned to you   \\* &#x60;created&#x60;: Issues created by you   \\* &#x60;mentioned&#x60;: Issues mentioning you   \\* &#x60;subscribed&#x60;: Issues you&#39;re subscribed to updates for   \\* &#x60;all&#x60; or &#x60;repos&#x60;: All issues the authenticated user can see, regardless of participation or creation | [optional] [default to &#39;assigned&#39;]
 **state** | **String**| Indicates the state of the issues to return. Can be either &#x60;open&#x60;, &#x60;closed&#x60;, or &#x60;all&#x60;. | [optional] [default to &#39;open&#39;]
 **labels** | **String**| A list of comma separated label names. Example: &#x60;bug,ui,@high&#x60; | [optional] 
 **sort** | **String**| What to sort results by. Can be either &#x60;created&#x60;, &#x60;updated&#x60;, &#x60;comments&#x60;. | [optional] [default to &#39;created&#39;]
 **direction** | **String**| One of &#x60;asc&#x60; (ascending) or &#x60;desc&#x60; (descending). | [optional] [default to &#39;desc&#39;]
 **since** | **Date**| Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] 
 **collab** | **Boolean**|  | [optional] 
 **orgs** | **Boolean**|  | [optional] 
 **owned** | **Boolean**|  | [optional] 
 **pulls** | **Boolean**|  | [optional] 
 **perPage** | **Number**| Results per page (max 100) | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[Issue]**](Issue.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## issuesListAssignees

> [SimpleUser] issuesListAssignees(owner, repo, opts)

List assignees

Lists the [available assignees](https://help.github.com/articles/assigning-issues-and-pull-requests-to-other-github-users/) for issues in a repository.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.IssuesApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let opts = {
  'perPage': 30, // Number | Results per page (max 100)
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.issuesListAssignees(owner, repo, opts, (error, data, response) => {
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
 **perPage** | **Number**| Results per page (max 100) | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[SimpleUser]**](SimpleUser.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## issuesListComments

> [IssueComment] issuesListComments(owner, repo, issueNumber, opts)

List issue comments

Issue Comments are ordered by ascending ID.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.IssuesApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let issueNumber = 56; // Number | issue_number parameter
let opts = {
  'since': new Date("2013-10-20T19:20:30+01:00"), // Date | Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
  'perPage': 30, // Number | Results per page (max 100)
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.issuesListComments(owner, repo, issueNumber, opts, (error, data, response) => {
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
 **since** | **Date**| Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] 
 **perPage** | **Number**| Results per page (max 100) | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[IssueComment]**](IssueComment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## issuesListCommentsForRepo

> [IssueComment] issuesListCommentsForRepo(owner, repo, opts)

List issue comments for a repository

By default, Issue Comments are ordered by ascending ID.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.IssuesApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let opts = {
  'sort': "'created'", // String | One of `created` (when the repository was starred) or `updated` (when it was last pushed to).
  'direction': "direction_example", // String | Either `asc` or `desc`. Ignored without the `sort` parameter.
  'since': new Date("2013-10-20T19:20:30+01:00"), // Date | Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
  'perPage': 30, // Number | Results per page (max 100)
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.issuesListCommentsForRepo(owner, repo, opts, (error, data, response) => {
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
 **sort** | **String**| One of &#x60;created&#x60; (when the repository was starred) or &#x60;updated&#x60; (when it was last pushed to). | [optional] [default to &#39;created&#39;]
 **direction** | **String**| Either &#x60;asc&#x60; or &#x60;desc&#x60;. Ignored without the &#x60;sort&#x60; parameter. | [optional] 
 **since** | **Date**| Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] 
 **perPage** | **Number**| Results per page (max 100) | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[IssueComment]**](IssueComment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## issuesListEvents

> [IssueEventForIssue] issuesListEvents(owner, repo, issueNumber, opts)

List issue events



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.IssuesApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let issueNumber = 56; // Number | issue_number parameter
let opts = {
  'perPage': 30, // Number | Results per page (max 100)
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.issuesListEvents(owner, repo, issueNumber, opts, (error, data, response) => {
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
 **perPage** | **Number**| Results per page (max 100) | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[IssueEventForIssue]**](IssueEventForIssue.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## issuesListEventsForRepo

> [IssueEvent] issuesListEventsForRepo(owner, repo, opts)

List issue events for a repository



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.IssuesApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let opts = {
  'perPage': 30, // Number | Results per page (max 100)
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.issuesListEventsForRepo(owner, repo, opts, (error, data, response) => {
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
 **perPage** | **Number**| Results per page (max 100) | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[IssueEvent]**](IssueEvent.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## issuesListEventsForTimeline

> [TimelineIssueEvents] issuesListEventsForTimeline(owner, repo, issueNumber, opts)

List timeline events for an issue



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.IssuesApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let issueNumber = 56; // Number | issue_number parameter
let opts = {
  'perPage': 30, // Number | Results per page (max 100)
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.issuesListEventsForTimeline(owner, repo, issueNumber, opts, (error, data, response) => {
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
 **perPage** | **Number**| Results per page (max 100) | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[TimelineIssueEvents]**](TimelineIssueEvents.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## issuesListForAuthenticatedUser

> [Issue] issuesListForAuthenticatedUser(opts)

List user account issues assigned to the authenticated user

List issues across owned and member repositories assigned to the authenticated user.  **Note**: GitHub&#39;s REST API v3 considers every pull request an issue, but not every issue is a pull request. For this reason, \&quot;Issues\&quot; endpoints may return both issues and pull requests in the response. You can identify pull requests by the &#x60;pull_request&#x60; key. Be aware that the &#x60;id&#x60; of a pull request returned from \&quot;Issues\&quot; endpoints will be an _issue id_. To find out the pull request id, use the \&quot;[List pull requests](https://docs.github.com/enterprise-server@2.18/rest/reference/pulls#list-pull-requests)\&quot; endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.IssuesApi();
let opts = {
  'filter': "'assigned'", // String | Indicates which sorts of issues to return. Can be one of:   \\* `assigned`: Issues assigned to you   \\* `created`: Issues created by you   \\* `mentioned`: Issues mentioning you   \\* `subscribed`: Issues you're subscribed to updates for   \\* `all` or `repos`: All issues the authenticated user can see, regardless of participation or creation
  'state': "'open'", // String | Indicates the state of the issues to return. Can be either `open`, `closed`, or `all`.
  'labels': "labels_example", // String | A list of comma separated label names. Example: `bug,ui,@high`
  'sort': "'created'", // String | What to sort results by. Can be either `created`, `updated`, `comments`.
  'direction': "'desc'", // String | One of `asc` (ascending) or `desc` (descending).
  'since': new Date("2013-10-20T19:20:30+01:00"), // Date | Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
  'perPage': 30, // Number | Results per page (max 100)
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.issuesListForAuthenticatedUser(opts, (error, data, response) => {
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
 **filter** | **String**| Indicates which sorts of issues to return. Can be one of:   \\* &#x60;assigned&#x60;: Issues assigned to you   \\* &#x60;created&#x60;: Issues created by you   \\* &#x60;mentioned&#x60;: Issues mentioning you   \\* &#x60;subscribed&#x60;: Issues you&#39;re subscribed to updates for   \\* &#x60;all&#x60; or &#x60;repos&#x60;: All issues the authenticated user can see, regardless of participation or creation | [optional] [default to &#39;assigned&#39;]
 **state** | **String**| Indicates the state of the issues to return. Can be either &#x60;open&#x60;, &#x60;closed&#x60;, or &#x60;all&#x60;. | [optional] [default to &#39;open&#39;]
 **labels** | **String**| A list of comma separated label names. Example: &#x60;bug,ui,@high&#x60; | [optional] 
 **sort** | **String**| What to sort results by. Can be either &#x60;created&#x60;, &#x60;updated&#x60;, &#x60;comments&#x60;. | [optional] [default to &#39;created&#39;]
 **direction** | **String**| One of &#x60;asc&#x60; (ascending) or &#x60;desc&#x60; (descending). | [optional] [default to &#39;desc&#39;]
 **since** | **Date**| Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] 
 **perPage** | **Number**| Results per page (max 100) | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[Issue]**](Issue.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## issuesListForOrg

> [Issue] issuesListForOrg(org, opts)

List organization issues assigned to the authenticated user

List issues in an organization assigned to the authenticated user.  **Note**: GitHub&#39;s REST API v3 considers every pull request an issue, but not every issue is a pull request. For this reason, \&quot;Issues\&quot; endpoints may return both issues and pull requests in the response. You can identify pull requests by the &#x60;pull_request&#x60; key. Be aware that the &#x60;id&#x60; of a pull request returned from \&quot;Issues\&quot; endpoints will be an _issue id_. To find out the pull request id, use the \&quot;[List pull requests](https://docs.github.com/enterprise-server@2.18/rest/reference/pulls#list-pull-requests)\&quot; endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.IssuesApi();
let org = "org_example"; // String | 
let opts = {
  'filter': "'assigned'", // String | Indicates which sorts of issues to return. Can be one of:   \\* `assigned`: Issues assigned to you   \\* `created`: Issues created by you   \\* `mentioned`: Issues mentioning you   \\* `subscribed`: Issues you're subscribed to updates for   \\* `all` or `repos`: All issues the authenticated user can see, regardless of participation or creation
  'state': "'open'", // String | Indicates the state of the issues to return. Can be either `open`, `closed`, or `all`.
  'labels': "labels_example", // String | A list of comma separated label names. Example: `bug,ui,@high`
  'sort': "'created'", // String | What to sort results by. Can be either `created`, `updated`, `comments`.
  'direction': "'desc'", // String | One of `asc` (ascending) or `desc` (descending).
  'since': new Date("2013-10-20T19:20:30+01:00"), // Date | Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
  'perPage': 30, // Number | Results per page (max 100)
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.issuesListForOrg(org, opts, (error, data, response) => {
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
 **org** | **String**|  | 
 **filter** | **String**| Indicates which sorts of issues to return. Can be one of:   \\* &#x60;assigned&#x60;: Issues assigned to you   \\* &#x60;created&#x60;: Issues created by you   \\* &#x60;mentioned&#x60;: Issues mentioning you   \\* &#x60;subscribed&#x60;: Issues you&#39;re subscribed to updates for   \\* &#x60;all&#x60; or &#x60;repos&#x60;: All issues the authenticated user can see, regardless of participation or creation | [optional] [default to &#39;assigned&#39;]
 **state** | **String**| Indicates the state of the issues to return. Can be either &#x60;open&#x60;, &#x60;closed&#x60;, or &#x60;all&#x60;. | [optional] [default to &#39;open&#39;]
 **labels** | **String**| A list of comma separated label names. Example: &#x60;bug,ui,@high&#x60; | [optional] 
 **sort** | **String**| What to sort results by. Can be either &#x60;created&#x60;, &#x60;updated&#x60;, &#x60;comments&#x60;. | [optional] [default to &#39;created&#39;]
 **direction** | **String**| One of &#x60;asc&#x60; (ascending) or &#x60;desc&#x60; (descending). | [optional] [default to &#39;desc&#39;]
 **since** | **Date**| Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] 
 **perPage** | **Number**| Results per page (max 100) | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[Issue]**](Issue.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## issuesListForRepo

> [IssueSimple] issuesListForRepo(owner, repo, opts)

List repository issues

List issues in a repository.  **Note**: GitHub&#39;s REST API v3 considers every pull request an issue, but not every issue is a pull request. For this reason, \&quot;Issues\&quot; endpoints may return both issues and pull requests in the response. You can identify pull requests by the &#x60;pull_request&#x60; key. Be aware that the &#x60;id&#x60; of a pull request returned from \&quot;Issues\&quot; endpoints will be an _issue id_. To find out the pull request id, use the \&quot;[List pull requests](https://docs.github.com/enterprise-server@2.18/rest/reference/pulls#list-pull-requests)\&quot; endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.IssuesApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let opts = {
  'milestone': "milestone_example", // String | If an `integer` is passed, it should refer to a milestone by its `number` field. If the string `*` is passed, issues with any milestone are accepted. If the string `none` is passed, issues without milestones are returned.
  'state': "'open'", // String | Indicates the state of the issues to return. Can be either `open`, `closed`, or `all`.
  'assignee': "assignee_example", // String | Can be the name of a user. Pass in `none` for issues with no assigned user, and `*` for issues assigned to any user.
  'creator': "creator_example", // String | The user that created the issue.
  'mentioned': "mentioned_example", // String | A user that's mentioned in the issue.
  'labels': "labels_example", // String | A list of comma separated label names. Example: `bug,ui,@high`
  'sort': "'created'", // String | What to sort results by. Can be either `created`, `updated`, `comments`.
  'direction': "'desc'", // String | One of `asc` (ascending) or `desc` (descending).
  'since': new Date("2013-10-20T19:20:30+01:00"), // Date | Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
  'perPage': 30, // Number | Results per page (max 100)
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.issuesListForRepo(owner, repo, opts, (error, data, response) => {
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
 **milestone** | **String**| If an &#x60;integer&#x60; is passed, it should refer to a milestone by its &#x60;number&#x60; field. If the string &#x60;*&#x60; is passed, issues with any milestone are accepted. If the string &#x60;none&#x60; is passed, issues without milestones are returned. | [optional] 
 **state** | **String**| Indicates the state of the issues to return. Can be either &#x60;open&#x60;, &#x60;closed&#x60;, or &#x60;all&#x60;. | [optional] [default to &#39;open&#39;]
 **assignee** | **String**| Can be the name of a user. Pass in &#x60;none&#x60; for issues with no assigned user, and &#x60;*&#x60; for issues assigned to any user. | [optional] 
 **creator** | **String**| The user that created the issue. | [optional] 
 **mentioned** | **String**| A user that&#39;s mentioned in the issue. | [optional] 
 **labels** | **String**| A list of comma separated label names. Example: &#x60;bug,ui,@high&#x60; | [optional] 
 **sort** | **String**| What to sort results by. Can be either &#x60;created&#x60;, &#x60;updated&#x60;, &#x60;comments&#x60;. | [optional] [default to &#39;created&#39;]
 **direction** | **String**| One of &#x60;asc&#x60; (ascending) or &#x60;desc&#x60; (descending). | [optional] [default to &#39;desc&#39;]
 **since** | **Date**| Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] 
 **perPage** | **Number**| Results per page (max 100) | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[IssueSimple]**](IssueSimple.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## issuesListLabelsForMilestone

> [Label] issuesListLabelsForMilestone(owner, repo, milestoneNumber, opts)

List labels for issues in a milestone



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.IssuesApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let milestoneNumber = 56; // Number | milestone_number parameter
let opts = {
  'perPage': 30, // Number | Results per page (max 100)
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.issuesListLabelsForMilestone(owner, repo, milestoneNumber, opts, (error, data, response) => {
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
 **milestoneNumber** | **Number**| milestone_number parameter | 
 **perPage** | **Number**| Results per page (max 100) | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[Label]**](Label.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## issuesListLabelsForRepo

> [Label] issuesListLabelsForRepo(owner, repo, opts)

List labels for a repository



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.IssuesApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let opts = {
  'perPage': 30, // Number | Results per page (max 100)
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.issuesListLabelsForRepo(owner, repo, opts, (error, data, response) => {
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
 **perPage** | **Number**| Results per page (max 100) | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[Label]**](Label.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## issuesListLabelsOnIssue

> [Label] issuesListLabelsOnIssue(owner, repo, issueNumber, opts)

List labels for an issue



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.IssuesApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let issueNumber = 56; // Number | issue_number parameter
let opts = {
  'perPage': 30, // Number | Results per page (max 100)
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.issuesListLabelsOnIssue(owner, repo, issueNumber, opts, (error, data, response) => {
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
 **perPage** | **Number**| Results per page (max 100) | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[Label]**](Label.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## issuesListMilestones

> [Milestone] issuesListMilestones(owner, repo, opts)

List milestones



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.IssuesApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let opts = {
  'state': "'open'", // String | The state of the milestone. Either `open`, `closed`, or `all`.
  'sort': "'due_on'", // String | What to sort results by. Either `due_on` or `completeness`.
  'direction': "'asc'", // String | The direction of the sort. Either `asc` or `desc`.
  'perPage': 30, // Number | Results per page (max 100)
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.issuesListMilestones(owner, repo, opts, (error, data, response) => {
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
 **state** | **String**| The state of the milestone. Either &#x60;open&#x60;, &#x60;closed&#x60;, or &#x60;all&#x60;. | [optional] [default to &#39;open&#39;]
 **sort** | **String**| What to sort results by. Either &#x60;due_on&#x60; or &#x60;completeness&#x60;. | [optional] [default to &#39;due_on&#39;]
 **direction** | **String**| The direction of the sort. Either &#x60;asc&#x60; or &#x60;desc&#x60;. | [optional] [default to &#39;asc&#39;]
 **perPage** | **Number**| Results per page (max 100) | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[Milestone]**](Milestone.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## issuesLock

> issuesLock(owner, repo, issueNumber, opts)

Lock an issue

Users with push access can lock an issue or pull request&#39;s conversation.  Note that, if you choose not to pass any parameters, you&#39;ll need to set &#x60;Content-Length&#x60; to zero when calling out to this endpoint. For more information, see \&quot;[HTTP verbs](https://docs.github.com/enterprise-server@2.18/rest/overview/resources-in-the-rest-api#http-verbs).\&quot;

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.IssuesApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let issueNumber = 56; // Number | issue_number parameter
let opts = {
  'issuesLockRequest': new GitHubV3RestApi.IssuesLockRequest() // IssuesLockRequest | 
};
apiInstance.issuesLock(owner, repo, issueNumber, opts, (error, data, response) => {
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
 **issueNumber** | **Number**| issue_number parameter | 
 **issuesLockRequest** | [**IssuesLockRequest**](IssuesLockRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## issuesRemoveAllLabels

> issuesRemoveAllLabels(owner, repo, issueNumber)

Remove all labels from an issue



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.IssuesApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let issueNumber = 56; // Number | issue_number parameter
apiInstance.issuesRemoveAllLabels(owner, repo, issueNumber, (error, data, response) => {
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
 **issueNumber** | **Number**| issue_number parameter | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## issuesRemoveAssignees

> IssueSimple issuesRemoveAssignees(owner, repo, issueNumber, opts)

Remove assignees from an issue

Removes one or more assignees from an issue.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.IssuesApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let issueNumber = 56; // Number | issue_number parameter
let opts = {
  'issuesRemoveAssigneesRequest': {"assignees":["hubot","other_user"]} // IssuesRemoveAssigneesRequest | 
};
apiInstance.issuesRemoveAssignees(owner, repo, issueNumber, opts, (error, data, response) => {
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
 **issuesRemoveAssigneesRequest** | [**IssuesRemoveAssigneesRequest**](IssuesRemoveAssigneesRequest.md)|  | [optional] 

### Return type

[**IssueSimple**](IssueSimple.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## issuesRemoveLabel

> [Label] issuesRemoveLabel(owner, repo, issueNumber, name)

Remove a label from an issue

Removes the specified label from the issue, and returns the remaining labels on the issue. This endpoint returns a &#x60;404 Not Found&#x60; status if the label does not exist.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.IssuesApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let issueNumber = 56; // Number | issue_number parameter
let name = "name_example"; // String | 
apiInstance.issuesRemoveLabel(owner, repo, issueNumber, name, (error, data, response) => {
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
 **name** | **String**|  | 

### Return type

[**[Label]**](Label.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## issuesSetLabels

> [Label] issuesSetLabels(owner, repo, issueNumber, opts)

Set labels for an issue

Removes any previous labels and sets the new labels for an issue.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.IssuesApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let issueNumber = 56; // Number | issue_number parameter
let opts = {
  'issuesSetLabelsRequest': {"labels":["bug","enhancement"]} // IssuesSetLabelsRequest | 
};
apiInstance.issuesSetLabels(owner, repo, issueNumber, opts, (error, data, response) => {
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
 **issuesSetLabelsRequest** | [**IssuesSetLabelsRequest**](IssuesSetLabelsRequest.md)|  | [optional] 

### Return type

[**[Label]**](Label.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## issuesUnlock

> issuesUnlock(owner, repo, issueNumber)

Unlock an issue

Users with push access can unlock an issue&#39;s conversation.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.IssuesApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let issueNumber = 56; // Number | issue_number parameter
apiInstance.issuesUnlock(owner, repo, issueNumber, (error, data, response) => {
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
 **issueNumber** | **Number**| issue_number parameter | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## issuesUpdate

> Issue issuesUpdate(owner, repo, issueNumber, opts)

Update an issue

Issue owners and users with push access can edit an issue.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.IssuesApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let issueNumber = 56; // Number | issue_number parameter
let opts = {
  'issuesUpdateRequest': {"assignees":["octocat"],"body":"I'm having a problem with this.","labels":["bug"],"milestone":1,"state":"open","title":"Found a bug"} // IssuesUpdateRequest | 
};
apiInstance.issuesUpdate(owner, repo, issueNumber, opts, (error, data, response) => {
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
 **issuesUpdateRequest** | [**IssuesUpdateRequest**](IssuesUpdateRequest.md)|  | [optional] 

### Return type

[**Issue**](Issue.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## issuesUpdateComment

> IssueComment issuesUpdateComment(owner, repo, commentId, issuesUpdateCommentRequest)

Update an issue comment



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.IssuesApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let commentId = 56; // Number | comment_id parameter
let issuesUpdateCommentRequest = {"body":"Me too"}; // IssuesUpdateCommentRequest | 
apiInstance.issuesUpdateComment(owner, repo, commentId, issuesUpdateCommentRequest, (error, data, response) => {
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
 **issuesUpdateCommentRequest** | [**IssuesUpdateCommentRequest**](IssuesUpdateCommentRequest.md)|  | 

### Return type

[**IssueComment**](IssueComment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## issuesUpdateMilestone

> Milestone issuesUpdateMilestone(owner, repo, milestoneNumber, opts)

Update a milestone



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.IssuesApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let milestoneNumber = 56; // Number | milestone_number parameter
let opts = {
  'issuesUpdateMilestoneRequest': {"description":"Tracking milestone for version 1.0","due_on":"2012-10-09T23:39:01Z","state":"open","title":"v1.0"} // IssuesUpdateMilestoneRequest | 
};
apiInstance.issuesUpdateMilestone(owner, repo, milestoneNumber, opts, (error, data, response) => {
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
 **milestoneNumber** | **Number**| milestone_number parameter | 
 **issuesUpdateMilestoneRequest** | [**IssuesUpdateMilestoneRequest**](IssuesUpdateMilestoneRequest.md)|  | [optional] 

### Return type

[**Milestone**](Milestone.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

