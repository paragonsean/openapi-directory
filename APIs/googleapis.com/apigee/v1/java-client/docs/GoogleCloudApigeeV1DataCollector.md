

# GoogleCloudApigeeV1DataCollector

Data collector configuration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **String** | Output only. The time at which the data collector was created in milliseconds since the epoch. |  [optional] [readonly] |
|**description** | **String** | A description of the data collector. |  [optional] |
|**lastModifiedAt** | **String** | Output only. The time at which the Data Collector was last updated in milliseconds since the epoch. |  [optional] [readonly] |
|**name** | **String** | ID of the data collector. Must begin with &#x60;dc_&#x60;. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Immutable. The type of data this data collector will collect. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| INTEGER | &quot;INTEGER&quot; |
| FLOAT | &quot;FLOAT&quot; |
| STRING | &quot;STRING&quot; |
| BOOLEAN | &quot;BOOLEAN&quot; |
| DATETIME | &quot;DATETIME&quot; |



