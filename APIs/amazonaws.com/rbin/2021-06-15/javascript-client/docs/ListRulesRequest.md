# AmazonRecycleBin.ListRulesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maxResults** | **Number** | The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned &lt;code&gt;NextToken&lt;/code&gt; value. | [optional] 
**nextToken** | **String** | The token for the next page of results. | [optional] 
**resourceType** | **String** | The resource type retained by the retention rule. Only retention rules that retain the specified resource type are listed. Currently, only Amazon EBS snapshots and EBS-backed AMIs are supported. To list retention rules that retain snapshots, specify &lt;code&gt;EBS_SNAPSHOT&lt;/code&gt;. To list retention rules that retain EBS-backed AMIs, specify &lt;code&gt;EC2_IMAGE&lt;/code&gt;. | 
**resourceTags** | [**[ResourceTag]**](ResourceTag.md) | Information about the resource tags used to identify resources that are retained by the retention rule. | [optional] 
**lockState** | **String** | The lock state of the retention rules to list. Only retention rules with the specified lock state are returned. | [optional] 



## Enum: ResourceTypeEnum


* `EBS_SNAPSHOT` (value: `"EBS_SNAPSHOT"`)

* `EC2_IMAGE` (value: `"EC2_IMAGE"`)





## Enum: LockStateEnum


* `locked` (value: `"locked"`)

* `pending_unlock` (value: `"pending_unlock"`)

* `unlocked` (value: `"unlocked"`)




