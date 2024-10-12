

# GoogleCloudBillingBillingaccountpricesV1betaAggregationInfo

Encapsulates the aggregation information such as aggregation level and interval for a billing account price.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**interval** | [**IntervalEnum**](#IntervalEnum) | Interval at which usage is aggregated to compute cost. Example: \&quot;MONTHLY\&quot; interval indicates that usage is aggregated every month. |  [optional] |
|**level** | [**LevelEnum**](#LevelEnum) | Level at which usage is aggregated to compute cost. Example: \&quot;ACCOUNT\&quot; level indicates that usage is aggregated across all projects in a single account. |  [optional] |



## Enum: IntervalEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;INTERVAL_UNSPECIFIED&quot; |
| MONTHLY | &quot;INTERVAL_MONTHLY&quot; |
| DAILY | &quot;INTERVAL_DAILY&quot; |



## Enum: LevelEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;LEVEL_UNSPECIFIED&quot; |
| ACCOUNT | &quot;LEVEL_ACCOUNT&quot; |
| PROJECT | &quot;LEVEL_PROJECT&quot; |



