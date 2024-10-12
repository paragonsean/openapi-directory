

# Metric

A `metric` is a set of user experience data for a single web performance metric, like \"first contentful paint\". It contains a summary histogram of real world Chrome usage as a series of `bins`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fractions** | **Map&lt;String, Double&gt;** | For enum metrics, provides fractions which add up to approximately 1.0. |  [optional] |
|**histogram** | [**List&lt;Bin&gt;**](Bin.md) | The histogram of user experiences for a metric. The histogram will have at least one bin and the densities of all bins will add up to ~1. |  [optional] |
|**percentiles** | [**Percentiles**](Percentiles.md) |  |  [optional] |



