

# Stream


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backfillAll** | [**BackfillAllStrategy**](BackfillAllStrategy.md) |  |  [optional] |
|**backfillNone** | **Object** | Backfill strategy to disable automatic backfill for the Stream&#39;s objects. |  [optional] |
|**createTime** | **String** | Output only. The creation time of the stream. |  [optional] [readonly] |
|**customerManagedEncryptionKey** | **String** | Immutable. A reference to a KMS encryption key. If provided, it will be used to encrypt the data. If left blank, data will be encrypted using an internal Stream-specific encryption key provisioned through KMS. |  [optional] |
|**destinationConfig** | [**DestinationConfig**](DestinationConfig.md) |  |  [optional] |
|**displayName** | **String** | Required. Display name. |  [optional] |
|**errors** | [**List&lt;Error&gt;**](Error.md) | Output only. Errors on the Stream. |  [optional] [readonly] |
|**labels** | **Map&lt;String, String&gt;** | Labels. |  [optional] |
|**name** | **String** | Output only. The stream&#39;s name. |  [optional] [readonly] |
|**sourceConfig** | [**SourceConfig**](SourceConfig.md) |  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The state of the stream. |  [optional] |
|**updateTime** | **String** | Output only. The last update time of the stream. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| CREATED | &quot;CREATED&quot; |
| RUNNING | &quot;RUNNING&quot; |
| PAUSED | &quot;PAUSED&quot; |
| MAINTENANCE | &quot;MAINTENANCE&quot; |
| FAILED | &quot;FAILED&quot; |
| FAILED_PERMANENTLY | &quot;FAILED_PERMANENTLY&quot; |
| STARTING | &quot;STARTING&quot; |
| DRAINING | &quot;DRAINING&quot; |



