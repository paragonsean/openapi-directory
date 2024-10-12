

# GoogleCloudDataplexV1DataScanJob

A DataScanJob represents an instance of DataScan execution.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataProfileResult** | [**GoogleCloudDataplexV1DataProfileResult**](GoogleCloudDataplexV1DataProfileResult.md) |  |  [optional] |
|**dataProfileSpec** | [**GoogleCloudDataplexV1DataProfileSpec**](GoogleCloudDataplexV1DataProfileSpec.md) |  |  [optional] |
|**dataQualityResult** | [**GoogleCloudDataplexV1DataQualityResult**](GoogleCloudDataplexV1DataQualityResult.md) |  |  [optional] |
|**dataQualitySpec** | [**GoogleCloudDataplexV1DataQualitySpec**](GoogleCloudDataplexV1DataQualitySpec.md) |  |  [optional] |
|**endTime** | **String** | Output only. The time when the DataScanJob ended. |  [optional] [readonly] |
|**message** | **String** | Output only. Additional information about the current state. |  [optional] [readonly] |
|**name** | **String** | Output only. The relative resource name of the DataScanJob, of the form: projects/{project}/locations/{location_id}/dataScans/{datascan_id}/jobs/{job_id}, where project refers to a project_id or project_number and location_id refers to a GCP region. |  [optional] [readonly] |
|**startTime** | **String** | Output only. The time when the DataScanJob was started. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. Execution state for the DataScanJob. |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | Output only. The type of the parent DataScan. |  [optional] [readonly] |
|**uid** | **String** | Output only. System generated globally unique ID for the DataScanJob. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| RUNNING | &quot;RUNNING&quot; |
| CANCELING | &quot;CANCELING&quot; |
| CANCELLED | &quot;CANCELLED&quot; |
| SUCCEEDED | &quot;SUCCEEDED&quot; |
| FAILED | &quot;FAILED&quot; |
| PENDING | &quot;PENDING&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| SCAN_TYPE_UNSPECIFIED | &quot;DATA_SCAN_TYPE_UNSPECIFIED&quot; |
| QUALITY | &quot;DATA_QUALITY&quot; |
| PROFILE | &quot;DATA_PROFILE&quot; |



