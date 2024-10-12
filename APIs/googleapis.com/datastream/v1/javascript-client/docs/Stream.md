# DatastreamApi.Stream

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backfillAll** | [**BackfillAllStrategy**](BackfillAllStrategy.md) |  | [optional] 
**backfillNone** | **Object** | Backfill strategy to disable automatic backfill for the Stream&#39;s objects. | [optional] 
**createTime** | **String** | Output only. The creation time of the stream. | [optional] [readonly] 
**customerManagedEncryptionKey** | **String** | Immutable. A reference to a KMS encryption key. If provided, it will be used to encrypt the data. If left blank, data will be encrypted using an internal Stream-specific encryption key provisioned through KMS. | [optional] 
**destinationConfig** | [**DestinationConfig**](DestinationConfig.md) |  | [optional] 
**displayName** | **String** | Required. Display name. | [optional] 
**errors** | [**[Error]**](Error.md) | Output only. Errors on the Stream. | [optional] [readonly] 
**labels** | **{String: String}** | Labels. | [optional] 
**lastRecoveryTime** | **String** | Output only. If the stream was recovered, the time of the last recovery. Note: This field is currently experimental. | [optional] [readonly] 
**name** | **String** | Output only. The stream&#39;s name. | [optional] [readonly] 
**sourceConfig** | [**SourceConfig**](SourceConfig.md) |  | [optional] 
**state** | **String** | The state of the stream. | [optional] 
**updateTime** | **String** | Output only. The last update time of the stream. | [optional] [readonly] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `NOT_STARTED` (value: `"NOT_STARTED"`)

* `RUNNING` (value: `"RUNNING"`)

* `PAUSED` (value: `"PAUSED"`)

* `MAINTENANCE` (value: `"MAINTENANCE"`)

* `FAILED` (value: `"FAILED"`)

* `FAILED_PERMANENTLY` (value: `"FAILED_PERMANENTLY"`)

* `STARTING` (value: `"STARTING"`)

* `DRAINING` (value: `"DRAINING"`)




