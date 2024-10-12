

# WebhookSubscription


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**active** | **Boolean** |  |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] |
|**description** | **String** | A user-defined description of the webhook. |  [optional] |
|**events** | [**Set&lt;EventsEnum&gt;**](#Set&lt;EventsEnum&gt;) | The events this webhook is subscribed to. |  [optional] |
|**subject** | **Object** |  |  [optional] |
|**subjectType** | [**SubjectTypeEnum**](#SubjectTypeEnum) | The type of entity. Set to either &#x60;repository&#x60; or &#x60;workspace&#x60; based on where the subscription is defined. |  [optional] |
|**url** | **URI** | The URL events get delivered to. |  [optional] |
|**uuid** | **String** | The webhook&#39;s id |  [optional] |



## Enum: Set&lt;EventsEnum&gt;

| Name | Value |
|---- | -----|
| PULLREQUEST_CHANGES_REQUEST_REMOVED | &quot;pullrequest:changes_request_removed&quot; |
| ISSUE_COMMENT_CREATED | &quot;issue:comment_created&quot; |
| REPO_PUSH | &quot;repo:push&quot; |
| REPO_COMMIT_STATUS_UPDATED | &quot;repo:commit_status_updated&quot; |
| REPO_IMPORTED | &quot;repo:imported&quot; |
| PULLREQUEST_UNAPPROVED | &quot;pullrequest:unapproved&quot; |
| REPO_UPDATED | &quot;repo:updated&quot; |
| PULLREQUEST_REJECTED | &quot;pullrequest:rejected&quot; |
| PULLREQUEST_FULFILLED | &quot;pullrequest:fulfilled&quot; |
| PULLREQUEST_CREATED | &quot;pullrequest:created&quot; |
| PULLREQUEST_APPROVED | &quot;pullrequest:approved&quot; |
| REPO_TRANSFER | &quot;repo:transfer&quot; |
| REPO_COMMIT_STATUS_CREATED | &quot;repo:commit_status_created&quot; |
| REPO_FORK | &quot;repo:fork&quot; |
| ISSUE_UPDATED | &quot;issue:updated&quot; |
| PROJECT_UPDATED | &quot;project:updated&quot; |
| REPO_CREATED | &quot;repo:created&quot; |
| ISSUE_CREATED | &quot;issue:created&quot; |
| REPO_COMMIT_COMMENT_CREATED | &quot;repo:commit_comment_created&quot; |
| PULLREQUEST_UPDATED | &quot;pullrequest:updated&quot; |
| REPO_DELETED | &quot;repo:deleted&quot; |
| PULLREQUEST_COMMENT_UPDATED | &quot;pullrequest:comment_updated&quot; |
| PULLREQUEST_CHANGES_REQUEST_CREATED | &quot;pullrequest:changes_request_created&quot; |
| PULLREQUEST_COMMENT_DELETED | &quot;pullrequest:comment_deleted&quot; |
| PULLREQUEST_COMMENT_CREATED | &quot;pullrequest:comment_created&quot; |



## Enum: SubjectTypeEnum

| Name | Value |
|---- | -----|
| REPOSITORY | &quot;repository&quot; |
| WORKSPACE | &quot;workspace&quot; |



