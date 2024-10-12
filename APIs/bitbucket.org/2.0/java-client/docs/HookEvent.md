

# HookEvent

An event, associated with a resource or subject type.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**category** | **String** | The category this event belongs to. |  [optional] |
|**description** | **String** | More detailed description of the webhook event type. |  [optional] |
|**event** | [**EventEnum**](#EventEnum) | The event identifier. |  [optional] |
|**label** | **String** | Summary of the webhook event type. |  [optional] |



## Enum: EventEnum

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



