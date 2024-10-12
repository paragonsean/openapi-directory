

# Pullrequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**author** | [**Account**](Account.md) |  |  [optional] |
|**closeSourceBranch** | **Boolean** | A boolean flag indicating if merging the pull request closes the source branch. |  [optional] |
|**closedBy** | [**Account**](Account.md) |  |  [optional] |
|**commentCount** | **Integer** | The number of comments for a specific pull request. |  [optional] |
|**createdOn** | **OffsetDateTime** | The ISO8601 timestamp the request was created. |  [optional] |
|**destination** | [**PullrequestEndpoint**](PullrequestEndpoint.md) |  |  [optional] |
|**id** | **Integer** | The pull request&#39;s unique ID. Note that pull request IDs are only unique within their associated repository. |  [optional] |
|**links** | [**PullRequestLinks**](PullRequestLinks.md) |  |  [optional] |
|**mergeCommit** | [**PullRequestCommit**](PullRequestCommit.md) |  |  [optional] |
|**participants** | [**List&lt;Participant&gt;**](Participant.md) |         The list of users that are collaborating on this pull request.         Collaborators are user that:          * are added to the pull request as a reviewer (part of the reviewers           list)         * are not explicit reviewers, but have commented on the pull request         * are not explicit reviewers, but have approved the pull request          Each user is wrapped in an object that indicates the user&#39;s role and         whether they have approved the pull request. For performance reasons,         the API only returns this list when an API requests a pull request by         id.          |  [optional] |
|**reason** | **String** | Explains why a pull request was declined. This field is only applicable to pull requests in rejected state. |  [optional] |
|**rendered** | [**RenderedPullRequestMarkup**](RenderedPullRequestMarkup.md) |  |  [optional] |
|**reviewers** | [**List&lt;Account&gt;**](Account.md) | The list of users that were added as reviewers on this pull request when it was created. For performance reasons, the API only includes this list on a pull request&#39;s &#x60;self&#x60; URL. |  [optional] |
|**source** | [**PullrequestEndpoint**](PullrequestEndpoint.md) |  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The pull request&#39;s current status. |  [optional] |
|**summary** | [**BaseCommitSummary**](BaseCommitSummary.md) |  |  [optional] |
|**taskCount** | **Integer** | The number of open tasks for a specific pull request. |  [optional] |
|**title** | **String** | Title of the pull request. |  [optional] |
|**updatedOn** | **OffsetDateTime** | The ISO8601 timestamp the request was last updated. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| OPEN | &quot;OPEN&quot; |
| MERGED | &quot;MERGED&quot; |
| DECLINED | &quot;DECLINED&quot; |
| SUPERSEDED | &quot;SUPERSEDED&quot; |



