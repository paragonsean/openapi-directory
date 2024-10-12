# BitbucketApi.WebhookSubscription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **Boolean** |  | [optional] 
**createdAt** | **Date** |  | [optional] 
**description** | **String** | A user-defined description of the webhook. | [optional] 
**events** | **[String]** | The events this webhook is subscribed to. | [optional] 
**subject** | **Object** |  | [optional] 
**subjectType** | **String** | The type of entity. Set to either &#x60;repository&#x60; or &#x60;workspace&#x60; based on where the subscription is defined. | [optional] 
**url** | **String** | The URL events get delivered to. | [optional] 
**uuid** | **String** | The webhook&#39;s id | [optional] 



## Enum: [EventsEnum]


* `pullrequest:changes_request_removed` (value: `"pullrequest:changes_request_removed"`)

* `issue:comment_created` (value: `"issue:comment_created"`)

* `repo:push` (value: `"repo:push"`)

* `repo:commit_status_updated` (value: `"repo:commit_status_updated"`)

* `repo:imported` (value: `"repo:imported"`)

* `pullrequest:unapproved` (value: `"pullrequest:unapproved"`)

* `repo:updated` (value: `"repo:updated"`)

* `pullrequest:rejected` (value: `"pullrequest:rejected"`)

* `pullrequest:fulfilled` (value: `"pullrequest:fulfilled"`)

* `pullrequest:created` (value: `"pullrequest:created"`)

* `pullrequest:approved` (value: `"pullrequest:approved"`)

* `repo:transfer` (value: `"repo:transfer"`)

* `repo:commit_status_created` (value: `"repo:commit_status_created"`)

* `repo:fork` (value: `"repo:fork"`)

* `issue:updated` (value: `"issue:updated"`)

* `project:updated` (value: `"project:updated"`)

* `repo:created` (value: `"repo:created"`)

* `issue:created` (value: `"issue:created"`)

* `repo:commit_comment_created` (value: `"repo:commit_comment_created"`)

* `pullrequest:updated` (value: `"pullrequest:updated"`)

* `repo:deleted` (value: `"repo:deleted"`)

* `pullrequest:comment_updated` (value: `"pullrequest:comment_updated"`)

* `pullrequest:changes_request_created` (value: `"pullrequest:changes_request_created"`)

* `pullrequest:comment_deleted` (value: `"pullrequest:comment_deleted"`)

* `pullrequest:comment_created` (value: `"pullrequest:comment_created"`)





## Enum: SubjectTypeEnum


* `repository` (value: `"repository"`)

* `workspace` (value: `"workspace"`)




