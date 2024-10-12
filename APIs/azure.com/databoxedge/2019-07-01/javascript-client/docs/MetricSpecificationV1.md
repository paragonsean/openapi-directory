# DataBoxEdgeManagementClient.MetricSpecificationV1

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregationType** | **String** | Metric aggregation type. | [optional] 
**category** | **String** | Metric category. | [optional] 
**dimensions** | [**[MetricDimensionV1]**](MetricDimensionV1.md) | Metric dimensions, other than default dimension which is resource. | [optional] 
**displayDescription** | **String** | Description of the metric to be displayed. | [optional] 
**displayName** | **String** | Display name of the metric. | [optional] 
**fillGapWithZero** | **Boolean** | Set true to fill the gaps with zero. | [optional] 
**name** | **String** | Name of the metric. | [optional] 
**resourceIdDimensionNameOverride** | **String** | Resource name override. | [optional] 
**supportedAggregationTypes** | **[String]** | Support metric aggregation type. | [optional] 
**supportedTimeGrainTypes** | **[String]** | Support granularity of metrics. | [optional] 
**unit** | **String** | Metric units. | [optional] 



## Enum: AggregationTypeEnum


* `NotSpecified` (value: `"NotSpecified"`)

* `None` (value: `"None"`)

* `Average` (value: `"Average"`)

* `Minimum` (value: `"Minimum"`)

* `Maximum` (value: `"Maximum"`)

* `Total` (value: `"Total"`)

* `Count` (value: `"Count"`)





## Enum: CategoryEnum


* `Capacity` (value: `"Capacity"`)

* `Transaction` (value: `"Transaction"`)





## Enum: [SupportedAggregationTypesEnum]


* `NotSpecified` (value: `"NotSpecified"`)

* `None` (value: `"None"`)

* `Average` (value: `"Average"`)

* `Minimum` (value: `"Minimum"`)

* `Maximum` (value: `"Maximum"`)

* `Total` (value: `"Total"`)

* `Count` (value: `"Count"`)





## Enum: [SupportedTimeGrainTypesEnum]


* `PT1M` (value: `"PT1M"`)

* `PT5M` (value: `"PT5M"`)

* `PT15M` (value: `"PT15M"`)

* `PT30M` (value: `"PT30M"`)

* `PT1H` (value: `"PT1H"`)

* `PT6H` (value: `"PT6H"`)

* `PT12H` (value: `"PT12H"`)

* `PT1D` (value: `"PT1D"`)





## Enum: UnitEnum


* `NotSpecified` (value: `"NotSpecified"`)

* `Percent` (value: `"Percent"`)

* `Count` (value: `"Count"`)

* `Seconds` (value: `"Seconds"`)

* `Milliseconds` (value: `"Milliseconds"`)

* `Bytes` (value: `"Bytes"`)

* `BytesPerSecond` (value: `"BytesPerSecond"`)

* `CountPerSecond` (value: `"CountPerSecond"`)




