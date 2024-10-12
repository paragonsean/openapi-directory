

# StreamSession

Object that captures the Amazon IVS configuration that the customer provisioned, the ingest configurations that the broadcaster used, and the most recent Amazon IVS stream events it encountered.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**channel** | [**StreamSessionChannel**](StreamSessionChannel.md) |  |  [optional] |
|**endTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**ingestConfiguration** | [**StreamSessionIngestConfiguration**](StreamSessionIngestConfiguration.md) |  |  [optional] |
|**recordingConfiguration** | [**StreamSessionRecordingConfiguration**](StreamSessionRecordingConfiguration.md) |  |  [optional] |
|**startTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**streamId** | [**String**](String.md) |  |  [optional] |
|**truncatedEvents** | [**List**](List.md) |  |  [optional] |



