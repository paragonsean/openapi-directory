

# Value

A message that can hold any of the supported value types and associated metadata.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**arrayValue** | [**ArrayValue**](ArrayValue.md) |  |  [optional] |
|**blobValue** | **byte[]** | A blob value. May have at most 1,000,000 bytes. When &#x60;exclude_from_indexes&#x60; is false, may have at most 1500 bytes. In JSON requests, must be base64-encoded. |  [optional] |
|**booleanValue** | **Boolean** | A boolean value. |  [optional] |
|**doubleValue** | **Double** | A double value. |  [optional] |
|**entityValue** | [**Entity**](Entity.md) |  |  [optional] |
|**excludeFromIndexes** | **Boolean** | If the value should be excluded from all indexes including those defined explicitly. |  [optional] |
|**geoPointValue** | [**LatLng**](LatLng.md) |  |  [optional] |
|**integerValue** | **String** | An integer value. |  [optional] |
|**keyValue** | [**Key**](Key.md) |  |  [optional] |
|**meaning** | **Integer** | The &#x60;meaning&#x60; field should only be populated for backwards compatibility. |  [optional] |
|**nullValue** | [**NullValueEnum**](#NullValueEnum) | A null value. |  [optional] |
|**stringValue** | **String** | A UTF-8 encoded string value. When &#x60;exclude_from_indexes&#x60; is false (it is indexed) , may have at most 1500 bytes. Otherwise, may be set to at most 1,000,000 bytes. |  [optional] |
|**timestampValue** | **String** | A timestamp value. When stored in the Datastore, precise only to microseconds; any additional precision is rounded down. |  [optional] |



## Enum: NullValueEnum

| Name | Value |
|---- | -----|
| NULL_VALUE | &quot;NULL_VALUE&quot; |



