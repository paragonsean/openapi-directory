

# MaterializedViewStatus

Status of a materialized view. The last refresh timestamp status is omitted here, but is present in the MaterializedViewDefinition message.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**lastRefreshStatus** | [**ErrorProto**](ErrorProto.md) |  |  [optional] |
|**refreshWatermark** | **String** | Output only. Refresh watermark of materialized view. The base tables&#39; data were collected into the materialized view cache until this time. |  [optional] [readonly] |



