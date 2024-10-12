

# GoogleCloudApigeeV1DataCollectorConfig

Data collector and its configuration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | Name of the data collector in the following format: &#x60;organizations/{org}/datacollectors/{datacollector}&#x60; |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Data type accepted by the data collector. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| INTEGER | &quot;INTEGER&quot; |
| FLOAT | &quot;FLOAT&quot; |
| STRING | &quot;STRING&quot; |
| BOOLEAN | &quot;BOOLEAN&quot; |
| DATETIME | &quot;DATETIME&quot; |



