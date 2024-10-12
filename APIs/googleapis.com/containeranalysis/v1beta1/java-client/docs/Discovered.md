

# Discovered

Provides information about the analysis status of a discovered resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**analysisCompleted** | [**AnalysisCompleted**](AnalysisCompleted.md) |  |  [optional] |
|**analysisError** | [**List&lt;Status&gt;**](Status.md) | Indicates any errors encountered during analysis of a resource. There could be 0 or more of these errors. |  [optional] |
|**analysisStatus** | [**AnalysisStatusEnum**](#AnalysisStatusEnum) | The status of discovery for the resource. |  [optional] |
|**analysisStatusError** | [**Status**](Status.md) |  |  [optional] |
|**continuousAnalysis** | [**ContinuousAnalysisEnum**](#ContinuousAnalysisEnum) | Whether the resource is continuously analyzed. |  [optional] |
|**lastAnalysisTime** | **String** | The last time continuous analysis was done for this resource. Deprecated, do not use. |  [optional] |
|**lastScanTime** | **String** | The last time this resource was scanned. |  [optional] |
|**sbomStatus** | [**SBOMStatus**](SBOMStatus.md) |  |  [optional] |



## Enum: AnalysisStatusEnum

| Name | Value |
|---- | -----|
| ANALYSIS_STATUS_UNSPECIFIED | &quot;ANALYSIS_STATUS_UNSPECIFIED&quot; |
| PENDING | &quot;PENDING&quot; |
| SCANNING | &quot;SCANNING&quot; |
| FINISHED_SUCCESS | &quot;FINISHED_SUCCESS&quot; |
| COMPLETE | &quot;COMPLETE&quot; |
| FINISHED_FAILED | &quot;FINISHED_FAILED&quot; |
| FINISHED_UNSUPPORTED | &quot;FINISHED_UNSUPPORTED&quot; |



## Enum: ContinuousAnalysisEnum

| Name | Value |
|---- | -----|
| CONTINUOUS_ANALYSIS_UNSPECIFIED | &quot;CONTINUOUS_ANALYSIS_UNSPECIFIED&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| INACTIVE | &quot;INACTIVE&quot; |



