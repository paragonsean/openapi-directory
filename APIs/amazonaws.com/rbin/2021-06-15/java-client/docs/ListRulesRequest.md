

# ListRulesRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**maxResults** | **Integer** | The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned &lt;code&gt;NextToken&lt;/code&gt; value. |  [optional] |
|**nextToken** | **String** | The token for the next page of results. |  [optional] |
|**resourceType** | [**ResourceTypeEnum**](#ResourceTypeEnum) | The resource type retained by the retention rule. Only retention rules that retain the specified resource type are listed. Currently, only Amazon EBS snapshots and EBS-backed AMIs are supported. To list retention rules that retain snapshots, specify &lt;code&gt;EBS_SNAPSHOT&lt;/code&gt;. To list retention rules that retain EBS-backed AMIs, specify &lt;code&gt;EC2_IMAGE&lt;/code&gt;. |  |
|**resourceTags** | [**List&lt;ResourceTag&gt;**](ResourceTag.md) | Information about the resource tags used to identify resources that are retained by the retention rule. |  [optional] |
|**lockState** | [**LockStateEnum**](#LockStateEnum) | The lock state of the retention rules to list. Only retention rules with the specified lock state are returned. |  [optional] |



## Enum: ResourceTypeEnum

| Name | Value |
|---- | -----|
| EBS_SNAPSHOT | &quot;EBS_SNAPSHOT&quot; |
| EC2_IMAGE | &quot;EC2_IMAGE&quot; |



## Enum: LockStateEnum

| Name | Value |
|---- | -----|
| LOCKED | &quot;locked&quot; |
| PENDING_UNLOCK | &quot;pending_unlock&quot; |
| UNLOCKED | &quot;unlocked&quot; |



