# ChromeUxReportApi.Metric

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fractions** | **{String: Number}** | For enum metrics, provides fractions which add up to approximately 1.0. | [optional] 
**histogram** | [**[Bin]**](Bin.md) | The histogram of user experiences for a metric. The histogram will have at least one bin and the densities of all bins will add up to ~1. | [optional] 
**percentiles** | [**Percentiles**](Percentiles.md) |  | [optional] 


