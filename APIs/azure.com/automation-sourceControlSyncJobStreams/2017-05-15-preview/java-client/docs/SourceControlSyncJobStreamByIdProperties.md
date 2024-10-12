

# SourceControlSyncJobStreamByIdProperties

Definition of source control sync job stream by id properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**sourceControlSyncJobStreamId** | **String** | The sync job stream id. |  [optional] |
|**streamText** | **String** | The text of the sync job stream. |  [optional] |
|**streamType** | [**StreamTypeEnum**](#StreamTypeEnum) | The type of the sync job stream. |  [optional] |
|**summary** | **String** | The summary of the sync job stream. |  [optional] |
|**time** | **OffsetDateTime** | The time of the sync job stream. |  [optional] [readonly] |
|**value** | **Map&lt;String, Object&gt;** | The values of the job stream. |  [optional] |



## Enum: StreamTypeEnum

| Name | Value |
|---- | -----|
| ERROR | &quot;Error&quot; |
| OUTPUT | &quot;Output&quot; |



