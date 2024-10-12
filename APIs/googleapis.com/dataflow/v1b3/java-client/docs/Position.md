

# Position

Position defines a position within a collection of data. The value can be either the end position, a key (used with ordered collections), a byte offset, or a record index.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**byteOffset** | **String** | Position is a byte offset. |  [optional] |
|**concatPosition** | [**ConcatPosition**](ConcatPosition.md) |  |  [optional] |
|**end** | **Boolean** | Position is past all other positions. Also useful for the end position of an unbounded range. |  [optional] |
|**key** | **String** | Position is a string key, ordered lexicographically. |  [optional] |
|**recordIndex** | **String** | Position is a record index. |  [optional] |
|**shufflePosition** | **String** | CloudPosition is a base64 encoded BatchShufflePosition (with FIXED sharding). |  [optional] |



