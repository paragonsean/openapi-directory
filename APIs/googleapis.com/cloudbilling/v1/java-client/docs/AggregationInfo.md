

# AggregationInfo

Represents the aggregation level and interval for pricing of a single SKU.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aggregationCount** | **Integer** | The number of intervals to aggregate over. Example: If aggregation_level is \&quot;DAILY\&quot; and aggregation_count is 14, aggregation will be over 14 days. |  [optional] |
|**aggregationInterval** | [**AggregationIntervalEnum**](#AggregationIntervalEnum) |  |  [optional] |
|**aggregationLevel** | [**AggregationLevelEnum**](#AggregationLevelEnum) |  |  [optional] |



## Enum: AggregationIntervalEnum

| Name | Value |
|---- | -----|
| AGGREGATION_INTERVAL_UNSPECIFIED | &quot;AGGREGATION_INTERVAL_UNSPECIFIED&quot; |
| DAILY | &quot;DAILY&quot; |
| MONTHLY | &quot;MONTHLY&quot; |



## Enum: AggregationLevelEnum

| Name | Value |
|---- | -----|
| AGGREGATION_LEVEL_UNSPECIFIED | &quot;AGGREGATION_LEVEL_UNSPECIFIED&quot; |
| ACCOUNT | &quot;ACCOUNT&quot; |
| PROJECT | &quot;PROJECT&quot; |



