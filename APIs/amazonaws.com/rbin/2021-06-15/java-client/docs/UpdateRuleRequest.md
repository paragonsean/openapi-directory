

# UpdateRuleRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**retentionPeriod** | [**CreateRuleRequestRetentionPeriod**](CreateRuleRequestRetentionPeriod.md) |  |  [optional] |
|**description** | **String** | The retention rule description. |  [optional] |
|**resourceType** | [**ResourceTypeEnum**](#ResourceTypeEnum) | &lt;note&gt; &lt;p&gt;This parameter is currently not supported. You can&#39;t update a retention rule&#39;s resource type after creation.&lt;/p&gt; &lt;/note&gt; |  [optional] |
|**resourceTags** | [**List&lt;ResourceTag&gt;**](ResourceTag.md) | &lt;p&gt;Specifies the resource tags to use to identify resources that are to be retained by a tag-level retention rule. For tag-level retention rules, only deleted resources, of the specified resource type, that have one or more of the specified tag key and value pairs are retained. If a resource is deleted, but it does not have any of the specified tag key and value pairs, it is immediately deleted without being retained by the retention rule.&lt;/p&gt; &lt;p&gt;You can add the same tag key and value pair to a maximum or five retention rules.&lt;/p&gt; &lt;p&gt;To create a Region-level retention rule, omit this parameter. A Region-level retention rule does not have any resource tags specified. It retains all deleted resources of the specified resource type in the Region in which the rule is created, even if the resources are not tagged.&lt;/p&gt; |  [optional] |



## Enum: ResourceTypeEnum

| Name | Value |
|---- | -----|
| EBS_SNAPSHOT | &quot;EBS_SNAPSHOT&quot; |
| EC2_IMAGE | &quot;EC2_IMAGE&quot; |



