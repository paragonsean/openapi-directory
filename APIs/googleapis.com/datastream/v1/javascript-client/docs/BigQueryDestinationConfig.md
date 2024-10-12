# DatastreamApi.BigQueryDestinationConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataFreshness** | **String** | The guaranteed data freshness (in seconds) when querying tables created by the stream. Editing this field will only affect new tables created in the future, but existing tables will not be impacted. Lower values mean that queries will return fresher data, but may result in higher cost. | [optional] 
**singleTargetDataset** | [**SingleTargetDataset**](SingleTargetDataset.md) |  | [optional] 
**sourceHierarchyDatasets** | [**SourceHierarchyDatasets**](SourceHierarchyDatasets.md) |  | [optional] 


