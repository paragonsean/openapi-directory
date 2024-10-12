

# SourceControlSyncJobStreamProperties

Definition of source control sync job stream properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**sourceControlSyncJobStreamId** | **String** | The sync job stream id. |  [optional] |
|**streamType** | [**StreamTypeEnum**](#StreamTypeEnum) | The type of the sync job stream. |  [optional] |
|**summary** | **String** | The summary of the sync job stream. |  [optional] |
|**time** | **OffsetDateTime** | The time of the sync job stream. |  [optional] [readonly] |



## Enum: StreamTypeEnum

| Name | Value |
|---- | -----|
| ERROR | &quot;Error&quot; |
| OUTPUT | &quot;Output&quot; |



