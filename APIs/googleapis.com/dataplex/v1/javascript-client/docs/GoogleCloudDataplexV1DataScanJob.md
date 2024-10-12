# CloudDataplexApi.GoogleCloudDataplexV1DataScanJob

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataProfileResult** | [**GoogleCloudDataplexV1DataProfileResult**](GoogleCloudDataplexV1DataProfileResult.md) |  | [optional] 
**dataProfileSpec** | [**GoogleCloudDataplexV1DataProfileSpec**](GoogleCloudDataplexV1DataProfileSpec.md) |  | [optional] 
**dataQualityResult** | [**GoogleCloudDataplexV1DataQualityResult**](GoogleCloudDataplexV1DataQualityResult.md) |  | [optional] 
**dataQualitySpec** | [**GoogleCloudDataplexV1DataQualitySpec**](GoogleCloudDataplexV1DataQualitySpec.md) |  | [optional] 
**endTime** | **String** | Output only. The time when the DataScanJob ended. | [optional] [readonly] 
**message** | **String** | Output only. Additional information about the current state. | [optional] [readonly] 
**name** | **String** | Output only. The relative resource name of the DataScanJob, of the form: projects/{project}/locations/{location_id}/dataScans/{datascan_id}/jobs/{job_id}, where project refers to a project_id or project_number and location_id refers to a GCP region. | [optional] [readonly] 
**startTime** | **String** | Output only. The time when the DataScanJob was started. | [optional] [readonly] 
**state** | **String** | Output only. Execution state for the DataScanJob. | [optional] [readonly] 
**type** | **String** | Output only. The type of the parent DataScan. | [optional] [readonly] 
**uid** | **String** | Output only. System generated globally unique ID for the DataScanJob. | [optional] [readonly] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `RUNNING` (value: `"RUNNING"`)

* `CANCELING` (value: `"CANCELING"`)

* `CANCELLED` (value: `"CANCELLED"`)

* `SUCCEEDED` (value: `"SUCCEEDED"`)

* `FAILED` (value: `"FAILED"`)

* `PENDING` (value: `"PENDING"`)





## Enum: TypeEnum


* `SCAN_TYPE_UNSPECIFIED` (value: `"DATA_SCAN_TYPE_UNSPECIFIED"`)

* `QUALITY` (value: `"DATA_QUALITY"`)

* `PROFILE` (value: `"DATA_PROFILE"`)




