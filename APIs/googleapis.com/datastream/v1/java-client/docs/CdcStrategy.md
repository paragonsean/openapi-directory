

# CdcStrategy

The strategy that the stream uses for CDC replication.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**mostRecentStartPosition** | **Object** | CDC strategy to start replicating from the most recent position in the source. |  [optional] |
|**nextAvailableStartPosition** | **Object** | CDC strategy to resume replication from the next available position in the source. |  [optional] |
|**specificStartPosition** | [**SpecificStartPosition**](SpecificStartPosition.md) |  |  [optional] |



