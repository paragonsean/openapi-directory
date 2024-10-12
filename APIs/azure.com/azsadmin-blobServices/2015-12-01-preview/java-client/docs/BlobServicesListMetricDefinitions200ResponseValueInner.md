

# BlobServicesListMetricDefinitions200ResponseValueInner

Metric definition.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**metricAvailabilities** | [**List&lt;BlobServicesListMetricDefinitions200ResponseValueInnerMetricAvailabilitiesInner&gt;**](BlobServicesListMetricDefinitions200ResponseValueInnerMetricAvailabilitiesInner.md) | Metric availabilities. |  [optional] [readonly] |
|**name** | [**BlobServicesListMetricDefinitions200ResponseValueInnerName**](BlobServicesListMetricDefinitions200ResponseValueInnerName.md) |  |  [optional] |
|**primaryAggregationType** | [**PrimaryAggregationTypeEnum**](#PrimaryAggregationTypeEnum) | Aggregate type. |  [optional] [readonly] |
|**unit** | [**UnitEnum**](#UnitEnum) | Metric unit. |  [optional] |



## Enum: PrimaryAggregationTypeEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| AVERAGE | &quot;Average&quot; |
| TOTAL | &quot;Total&quot; |
| MINIMUM | &quot;Minimum&quot; |
| MAXIMUM | &quot;Maximum&quot; |
| LAST | &quot;Last&quot; |



## Enum: UnitEnum

| Name | Value |
|---- | -----|
| COUNT | &quot;Count&quot; |
| BYTES | &quot;Bytes&quot; |
| SECONDS | &quot;Seconds&quot; |
| COUNT_PER_SECOND | &quot;CountPerSecond&quot; |
| BYTES_PER_SECOND | &quot;BytesPerSecond&quot; |



