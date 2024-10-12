# AwsCodeStarNotifications.UpdateNotificationRuleRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arn** | **String** | The Amazon Resource Name (ARN) of the notification rule. | 
**name** | **String** | The name of the notification rule. | [optional] 
**status** | **String** | The status of the notification rule. Valid statuses include enabled (sending notifications) or disabled (not sending notifications). | [optional] 
**eventTypeIds** | **[String]** | A list of event types associated with this notification rule. For a complete list of event types and IDs, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codestar-notifications/latest/userguide/concepts.html#concepts-api\&quot;&gt;Notification concepts&lt;/a&gt; in the &lt;i&gt;Developer Tools Console User Guide&lt;/i&gt;. | [optional] 
**targets** | [**[Target]**](Target.md) | The address and type of the targets to receive notifications from this notification rule. | [optional] 
**detailType** | **String** | The level of detail to include in the notifications for this resource. BASIC will include only the contents of the event as it would appear in Amazon CloudWatch. FULL will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created. | [optional] 



## Enum: StatusEnum


* `ENABLED` (value: `"ENABLED"`)

* `DISABLED` (value: `"DISABLED"`)





## Enum: DetailTypeEnum


* `BASIC` (value: `"BASIC"`)

* `FULL` (value: `"FULL"`)




