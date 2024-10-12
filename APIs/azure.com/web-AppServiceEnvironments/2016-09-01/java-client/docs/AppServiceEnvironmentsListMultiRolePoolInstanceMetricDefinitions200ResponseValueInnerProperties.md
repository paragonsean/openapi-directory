

# AppServiceEnvironmentsListMultiRolePoolInstanceMetricDefinitions200ResponseValueInnerProperties

ResourceMetricDefinition resource specific properties

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Resource ID. |  [optional] [readonly] |
|**metricAvailabilities** | [**List&lt;AppServiceEnvironmentsListMultiRolePoolInstanceMetricDefinitions200ResponseValueInnerPropertiesMetricAvailabilitiesInner&gt;**](AppServiceEnvironmentsListMultiRolePoolInstanceMetricDefinitions200ResponseValueInnerPropertiesMetricAvailabilitiesInner.md) | List of time grains supported for the metric together with retention period. |  [optional] [readonly] |
|**name** | [**AppServiceEnvironmentsListMetrics200ResponseValueInnerName**](AppServiceEnvironmentsListMetrics200ResponseValueInnerName.md) |  |  [optional] |
|**primaryAggregationType** | **String** | Primary aggregation type. |  [optional] [readonly] |
|**properties** | **Map&lt;String, String&gt;** | Resource metric definition properties. |  [optional] [readonly] |
|**resourceUri** | **String** | Resource URI. |  [optional] [readonly] |
|**unit** | **String** | Unit of the metric. |  [optional] [readonly] |



