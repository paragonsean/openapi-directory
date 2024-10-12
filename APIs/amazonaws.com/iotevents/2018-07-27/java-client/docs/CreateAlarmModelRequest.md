

# CreateAlarmModelRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alarmModelName** | **String** | A unique name that helps you identify the alarm model. You can&#39;t change this name after you create the alarm model. |  |
|**alarmModelDescription** | **String** | A description that tells you what the alarm model detects. |  [optional] |
|**roleArn** | **String** | The ARN of the IAM role that allows the alarm to perform actions and access AWS resources. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;Amazon Resource Names (ARNs)&lt;/a&gt; in the &lt;i&gt;AWS General Reference&lt;/i&gt;. |  |
|**tags** | [**List&lt;Tag&gt;**](Tag.md) | &lt;p&gt;A list of key-value pairs that contain metadata for the alarm model. The tags help you manage the alarm model. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iotevents/latest/developerguide/tagging-iotevents.html\&quot;&gt;Tagging your AWS IoT Events resources&lt;/a&gt; in the &lt;i&gt;AWS IoT Events Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;You can create up to 50 tags for one alarm model.&lt;/p&gt; |  [optional] |
|**key** | **String** | An input attribute used as a key to create an alarm. AWS IoT Events routes &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iotevents/latest/apireference/API_Input.html\&quot;&gt;inputs&lt;/a&gt; associated with this key to the alarm. |  [optional] |
|**severity** | **Integer** | A non-negative integer that reflects the severity level of the alarm. |  [optional] |
|**alarmRule** | [**CreateAlarmModelRequestAlarmRule**](CreateAlarmModelRequestAlarmRule.md) |  |  |
|**alarmNotification** | [**CreateAlarmModelRequestAlarmNotification**](CreateAlarmModelRequestAlarmNotification.md) |  |  [optional] |
|**alarmEventActions** | [**CreateAlarmModelRequestAlarmEventActions**](CreateAlarmModelRequestAlarmEventActions.md) |  |  [optional] |
|**alarmCapabilities** | [**CreateAlarmModelRequestAlarmCapabilities**](CreateAlarmModelRequestAlarmCapabilities.md) |  |  [optional] |



