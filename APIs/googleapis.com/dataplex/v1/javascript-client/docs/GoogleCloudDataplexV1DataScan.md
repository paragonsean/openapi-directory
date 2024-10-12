# CloudDataplexApi.GoogleCloudDataplexV1DataScan

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. The time when the scan was created. | [optional] [readonly] 
**data** | [**GoogleCloudDataplexV1DataSource**](GoogleCloudDataplexV1DataSource.md) |  | [optional] 
**dataProfileResult** | [**GoogleCloudDataplexV1DataProfileResult**](GoogleCloudDataplexV1DataProfileResult.md) |  | [optional] 
**dataProfileSpec** | [**GoogleCloudDataplexV1DataProfileSpec**](GoogleCloudDataplexV1DataProfileSpec.md) |  | [optional] 
**dataQualityResult** | [**GoogleCloudDataplexV1DataQualityResult**](GoogleCloudDataplexV1DataQualityResult.md) |  | [optional] 
**dataQualitySpec** | [**GoogleCloudDataplexV1DataQualitySpec**](GoogleCloudDataplexV1DataQualitySpec.md) |  | [optional] 
**description** | **String** | Optional. Description of the scan. Must be between 1-1024 characters. | [optional] 
**displayName** | **String** | Optional. User friendly display name. Must be between 1-256 characters. | [optional] 
**executionSpec** | [**GoogleCloudDataplexV1DataScanExecutionSpec**](GoogleCloudDataplexV1DataScanExecutionSpec.md) |  | [optional] 
**executionStatus** | [**GoogleCloudDataplexV1DataScanExecutionStatus**](GoogleCloudDataplexV1DataScanExecutionStatus.md) |  | [optional] 
**labels** | **{String: String}** | Optional. User-defined labels for the scan. | [optional] 
**name** | **String** | Output only. The relative resource name of the scan, of the form: projects/{project}/locations/{location_id}/dataScans/{datascan_id}, where project refers to a project_id or project_number and location_id refers to a GCP region. | [optional] [readonly] 
**state** | **String** | Output only. Current state of the DataScan. | [optional] [readonly] 
**type** | **String** | Output only. The type of DataScan. | [optional] [readonly] 
**uid** | **String** | Output only. System generated globally unique ID for the scan. This ID will be different if the scan is deleted and re-created with the same name. | [optional] [readonly] 
**updateTime** | **String** | Output only. The time when the scan was last updated. | [optional] [readonly] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `CREATING` (value: `"CREATING"`)

* `DELETING` (value: `"DELETING"`)

* `ACTION_REQUIRED` (value: `"ACTION_REQUIRED"`)





## Enum: TypeEnum


* `SCAN_TYPE_UNSPECIFIED` (value: `"DATA_SCAN_TYPE_UNSPECIFIED"`)

* `QUALITY` (value: `"DATA_QUALITY"`)

* `PROFILE` (value: `"DATA_PROFILE"`)




