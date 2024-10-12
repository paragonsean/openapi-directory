# TheJiraCloudPlatformRestApi.Webhook

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | **[String]** | The Jira events that trigger the webhook. | 
**expirationDate** | **Number** | The date after which the webhook is no longer sent. Use [Extend webhook life](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-webhooks/#api-rest-api-3-webhook-refresh-put) to extend the date. | [optional] [readonly] 
**fieldIdsFilter** | **[String]** | A list of field IDs. When the issue changelog contains any of the fields, the webhook &#x60;jira:issue_updated&#x60; is sent. If this parameter is not present, the app is notified about all field updates. | [optional] 
**id** | **Number** | The ID of the webhook. | 
**issuePropertyKeysFilter** | **[String]** | A list of issue property keys. A change of those issue properties triggers the &#x60;issue_property_set&#x60; or &#x60;issue_property_deleted&#x60; webhooks. If this parameter is not present, the app is notified about all issue property updates. | [optional] 
**jqlFilter** | **String** | The JQL filter that specifies which issues the webhook is sent for. | 



## Enum: [EventsEnum]


* `jira:issue_created` (value: `"jira:issue_created"`)

* `jira:issue_updated` (value: `"jira:issue_updated"`)

* `jira:issue_deleted` (value: `"jira:issue_deleted"`)

* `comment_created` (value: `"comment_created"`)

* `comment_updated` (value: `"comment_updated"`)

* `comment_deleted` (value: `"comment_deleted"`)

* `issue_property_set` (value: `"issue_property_set"`)

* `issue_property_deleted` (value: `"issue_property_deleted"`)




