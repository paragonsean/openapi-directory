

# CreateNotificationRuleRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | The name for the notification rule. Notification rule names must be unique in your Amazon Web Services account. |  |
|**eventTypeIds** | **List&lt;String&gt;** | A list of event types associated with this notification rule. For a list of allowed events, see &lt;a&gt;EventTypeSummary&lt;/a&gt;. |  |
|**resource** | **String** | The Amazon Resource Name (ARN) of the resource to associate with the notification rule. Supported resources include pipelines in CodePipeline, repositories in CodeCommit, and build projects in CodeBuild. |  |
|**targets** | [**List&lt;Target&gt;**](Target.md) | A list of Amazon Resource Names (ARNs) of Amazon Simple Notification Service topics and Chatbot clients to associate with the notification rule. |  |
|**detailType** | [**DetailTypeEnum**](#DetailTypeEnum) | The level of detail to include in the notifications for this resource. &lt;code&gt;BASIC&lt;/code&gt; will include only the contents of the event as it would appear in Amazon CloudWatch. &lt;code&gt;FULL&lt;/code&gt; will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created. |  |
|**clientRequestToken** | **String** | &lt;p&gt;A unique, client-generated idempotency token that, when provided in a request, ensures the request cannot be repeated with a changed parameter. If a request with the same parameters is received and a token is included, the request returns information about the initial request that used that token.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The Amazon Web Services SDKs prepopulate client request tokens. If you are using an Amazon Web Services SDK, an idempotency token is created for you.&lt;/p&gt; &lt;/note&gt; |  [optional] |
|**tags** | **Map&lt;String, String&gt;** | A list of tags to apply to this notification rule. Key names cannot start with \&quot;&lt;code&gt;aws&lt;/code&gt;\&quot;.  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the notification rule. The default value is &lt;code&gt;ENABLED&lt;/code&gt;. If the status is set to &lt;code&gt;DISABLED&lt;/code&gt;, notifications aren&#39;t sent for the notification rule. |  [optional] |



## Enum: DetailTypeEnum

| Name | Value |
|---- | -----|
| BASIC | &quot;BASIC&quot; |
| FULL | &quot;FULL&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;ENABLED&quot; |
| DISABLED | &quot;DISABLED&quot; |



