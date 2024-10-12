

# UpdateAlarmModelRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alarmModelDescription** | **String** | The description of the alarm model. |  [optional] |
|**roleArn** | **String** | The ARN of the IAM role that allows the alarm to perform actions and access AWS resources. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;Amazon Resource Names (ARNs)&lt;/a&gt; in the &lt;i&gt;AWS General Reference&lt;/i&gt;. |  |
|**severity** | **Integer** | A non-negative integer that reflects the severity level of the alarm. |  [optional] |
|**alarmRule** | [**CreateAlarmModelRequestAlarmRule**](CreateAlarmModelRequestAlarmRule.md) |  |  |
|**alarmNotification** | [**CreateAlarmModelRequestAlarmNotification**](CreateAlarmModelRequestAlarmNotification.md) |  |  [optional] |
|**alarmEventActions** | [**CreateAlarmModelRequestAlarmEventActions**](CreateAlarmModelRequestAlarmEventActions.md) |  |  [optional] |
|**alarmCapabilities** | [**CreateAlarmModelRequestAlarmCapabilities**](CreateAlarmModelRequestAlarmCapabilities.md) |  |  [optional] |



