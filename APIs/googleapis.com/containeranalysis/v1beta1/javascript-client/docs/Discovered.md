# ContainerAnalysisApi.Discovered

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysisCompleted** | [**AnalysisCompleted**](AnalysisCompleted.md) |  | [optional] 
**analysisError** | [**[Status]**](Status.md) | Indicates any errors encountered during analysis of a resource. There could be 0 or more of these errors. | [optional] 
**analysisStatus** | **String** | The status of discovery for the resource. | [optional] 
**analysisStatusError** | [**Status**](Status.md) |  | [optional] 
**continuousAnalysis** | **String** | Whether the resource is continuously analyzed. | [optional] 
**lastAnalysisTime** | **String** | The last time continuous analysis was done for this resource. Deprecated, do not use. | [optional] 
**lastScanTime** | **String** | The last time this resource was scanned. | [optional] 
**sbomStatus** | [**SBOMStatus**](SBOMStatus.md) |  | [optional] 



## Enum: AnalysisStatusEnum


* `ANALYSIS_STATUS_UNSPECIFIED` (value: `"ANALYSIS_STATUS_UNSPECIFIED"`)

* `PENDING` (value: `"PENDING"`)

* `SCANNING` (value: `"SCANNING"`)

* `FINISHED_SUCCESS` (value: `"FINISHED_SUCCESS"`)

* `COMPLETE` (value: `"COMPLETE"`)

* `FINISHED_FAILED` (value: `"FINISHED_FAILED"`)

* `FINISHED_UNSUPPORTED` (value: `"FINISHED_UNSUPPORTED"`)





## Enum: ContinuousAnalysisEnum


* `CONTINUOUS_ANALYSIS_UNSPECIFIED` (value: `"CONTINUOUS_ANALYSIS_UNSPECIFIED"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `INACTIVE` (value: `"INACTIVE"`)




