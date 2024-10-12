

# Range

Specifies a contiguous range of an indexed collection, such as characters in text.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endIndex** | **Integer** | The optional zero-based index of the end of the collection. Required for &#x60;FIXED_RANGE&#x60; ranges. |  [optional] |
|**startIndex** | **Integer** | The optional zero-based index of the beginning of the collection. Required for &#x60;FIXED_RANGE&#x60; and &#x60;FROM_START_INDEX&#x60; ranges. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of range. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| RANGE_TYPE_UNSPECIFIED | &quot;RANGE_TYPE_UNSPECIFIED&quot; |
| FIXED_RANGE | &quot;FIXED_RANGE&quot; |
| FROM_START_INDEX | &quot;FROM_START_INDEX&quot; |
| ALL | &quot;ALL&quot; |



