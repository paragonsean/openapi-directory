

# CreateRuleRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**retentionPeriod** | [**CreateRuleRequestRetentionPeriod**](CreateRuleRequestRetentionPeriod.md) |  |  |
|**description** | **String** | The retention rule description. |  [optional] |
|**tags** | [**List&lt;Tag&gt;**](Tag.md) | Information about the tags to assign to the retention rule. |  [optional] |
|**resourceType** | [**ResourceTypeEnum**](#ResourceTypeEnum) | The resource type to be retained by the retention rule. Currently, only Amazon EBS snapshots and EBS-backed AMIs are supported. To retain snapshots, specify &lt;code&gt;EBS_SNAPSHOT&lt;/code&gt;. To retain EBS-backed AMIs, specify &lt;code&gt;EC2_IMAGE&lt;/code&gt;. |  |
|**resourceTags** | [**List&lt;ResourceTag&gt;**](ResourceTag.md) | &lt;p&gt;Specifies the resource tags to use to identify resources that are to be retained by a tag-level retention rule. For tag-level retention rules, only deleted resources, of the specified resource type, that have one or more of the specified tag key and value pairs are retained. If a resource is deleted, but it does not have any of the specified tag key and value pairs, it is immediately deleted without being retained by the retention rule.&lt;/p&gt; &lt;p&gt;You can add the same tag key and value pair to a maximum or five retention rules.&lt;/p&gt; &lt;p&gt;To create a Region-level retention rule, omit this parameter. A Region-level retention rule does not have any resource tags specified. It retains all deleted resources of the specified resource type in the Region in which the rule is created, even if the resources are not tagged.&lt;/p&gt; |  [optional] |
|**lockConfiguration** | [**CreateRuleRequestLockConfiguration**](CreateRuleRequestLockConfiguration.md) |  |  [optional] |



## Enum: ResourceTypeEnum

| Name | Value |
|---- | -----|
| EBS_SNAPSHOT | &quot;EBS_SNAPSHOT&quot; |
| EC2_IMAGE | &quot;EC2_IMAGE&quot; |



