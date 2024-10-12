

# ReferenceDataSetResource

A reference data set provides metadata about the events in an environment. Metadata in the reference data set will be joined with events as they are read from event sources. The metadata that makes up the reference data set is uploaded or modified through the Time Series Insights data plane APIs.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**properties** | [**ReferenceDataSetResourceProperties**](ReferenceDataSetResourceProperties.md) |  |  [optional] |
|**location** | **String** | Resource location |  |
|**tags** | **Map&lt;String, String&gt;** | Resource tags |  [optional] |
|**id** | **String** | Resource Id |  [optional] [readonly] |
|**name** | **String** | Resource name |  [optional] [readonly] |
|**type** | **String** | Resource type |  [optional] [readonly] |



