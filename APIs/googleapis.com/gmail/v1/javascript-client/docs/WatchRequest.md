# GmailApi.WatchRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**labelFilterAction** | **String** | Filtering behavior of &#x60;labelIds list&#x60; specified. This field is deprecated because it caused incorrect behavior in some cases; use &#x60;label_filter_behavior&#x60; instead. | [optional] 
**labelFilterBehavior** | **String** | Filtering behavior of &#x60;labelIds list&#x60; specified. This field replaces &#x60;label_filter_action&#x60;; if set, &#x60;label_filter_action&#x60; is ignored. | [optional] 
**labelIds** | **[String]** | List of label_ids to restrict notifications about. By default, if unspecified, all changes are pushed out. If specified then dictates which labels are required for a push notification to be generated. | [optional] 
**topicName** | **String** | A fully qualified Google Cloud Pub/Sub API topic name to publish the events to. This topic name **must** already exist in Cloud Pub/Sub and you **must** have already granted gmail \&quot;publish\&quot; permission on it. For example, \&quot;projects/my-project-identifier/topics/my-topic-name\&quot; (using the Cloud Pub/Sub \&quot;v1\&quot; topic naming format). Note that the \&quot;my-project-identifier\&quot; portion must exactly match your Google developer project id (the one executing this watch request). | [optional] 



## Enum: LabelFilterActionEnum


* `include` (value: `"include"`)

* `exclude` (value: `"exclude"`)





## Enum: LabelFilterBehaviorEnum


* `include` (value: `"include"`)

* `exclude` (value: `"exclude"`)




