

# KeyRangeInfo

A message representing information for a key range (possibly one key).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**contextValues** | [**List&lt;ContextValue&gt;**](ContextValue.md) | The list of context values for this key range. |  [optional] |
|**endKeyIndex** | **Integer** | The index of the end key in indexed_keys. |  [optional] |
|**info** | [**LocalizedString**](LocalizedString.md) |  |  [optional] |
|**keysCount** | **String** | The number of keys this range covers. |  [optional] |
|**metric** | [**LocalizedString**](LocalizedString.md) |  |  [optional] |
|**startKeyIndex** | **Integer** | The index of the start key in indexed_keys. |  [optional] |
|**timeOffset** | **String** | The time offset. This is the time since the start of the time interval. |  [optional] |
|**unit** | [**LocalizedString**](LocalizedString.md) |  |  [optional] |
|**value** | **Float** | The value of the metric. |  [optional] |



