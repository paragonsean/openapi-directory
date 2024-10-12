

# GoogleCloudAiplatformV1SchemaTrainingjobDefinitionHierarchyConfig

Configuration that defines the hierarchical relationship of time series and parameters for hierarchical forecasting strategies.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**groupColumns** | **List&lt;String&gt;** | A list of time series attribute column names that define the time series hierarchy. Only one level of hierarchy is supported, ex. &#39;region&#39; for a hierarchy of stores or &#39;department&#39; for a hierarchy of products. If multiple columns are specified, time series will be grouped by their combined values, ex. (&#39;blue&#39;, &#39;large&#39;) for &#39;color&#39; and &#39;size&#39;, up to 5 columns are accepted. If no group columns are specified, all time series are considered to be part of the same group. |  [optional] |
|**groupTemporalTotalWeight** | **Double** | The weight of the loss for predictions aggregated over both the horizon and time series in the same hierarchy group. |  [optional] |
|**groupTotalWeight** | **Double** | The weight of the loss for predictions aggregated over time series in the same group. |  [optional] |
|**temporalTotalWeight** | **Double** | The weight of the loss for predictions aggregated over the horizon for a single time series. |  [optional] |



