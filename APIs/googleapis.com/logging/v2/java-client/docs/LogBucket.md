

# LogBucket

Describes a repository in which log entries are stored.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**analyticsEnabled** | **Boolean** | Optional. Whether log analytics is enabled for this bucket.Once enabled, log analytics features cannot be disabled. |  [optional] |
|**cmekSettings** | [**CmekSettings**](CmekSettings.md) |  |  [optional] |
|**createTime** | **String** | Output only. The creation timestamp of the bucket. This is not set for any of the default buckets. |  [optional] [readonly] |
|**description** | **String** | Optional. Describes this bucket. |  [optional] |
|**indexConfigs** | [**List&lt;IndexConfig&gt;**](IndexConfig.md) | Optional. A list of indexed fields and related configuration data. |  [optional] |
|**lifecycleState** | [**LifecycleStateEnum**](#LifecycleStateEnum) | Output only. The bucket lifecycle state. |  [optional] [readonly] |
|**locked** | **Boolean** | Optional. Whether the bucket is locked.The retention period on a locked bucket cannot be changed. Locked buckets may only be deleted if they are empty. |  [optional] |
|**name** | **String** | Output only. The resource name of the bucket.For example:projects/my-project/locations/global/buckets/my-bucketFor a list of supported locations, see Supported Regions (https://cloud.google.com/logging/docs/region-support)For the location of global it is unspecified where log entries are actually stored.After a bucket has been created, the location cannot be changed. |  [optional] [readonly] |
|**restrictedFields** | **List&lt;String&gt;** | Optional. Log entry field paths that are denied access in this bucket.The following fields and their children are eligible: textPayload, jsonPayload, protoPayload, httpRequest, labels, sourceLocation.Restricting a repeated field will restrict all values. Adding a parent will block all child fields. (e.g. foo.bar will block foo.bar.baz) |  [optional] |
|**retentionDays** | **Integer** | Optional. Logs will be retained by default for this amount of time, after which they will automatically be deleted. The minimum retention period is 1 day. If this value is set to zero at bucket creation time, the default time of 30 days will be used. |  [optional] |
|**updateTime** | **String** | Output only. The last update timestamp of the bucket. |  [optional] [readonly] |



## Enum: LifecycleStateEnum

| Name | Value |
|---- | -----|
| LIFECYCLE_STATE_UNSPECIFIED | &quot;LIFECYCLE_STATE_UNSPECIFIED&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| DELETE_REQUESTED | &quot;DELETE_REQUESTED&quot; |
| UPDATING | &quot;UPDATING&quot; |
| CREATING | &quot;CREATING&quot; |
| FAILED | &quot;FAILED&quot; |



