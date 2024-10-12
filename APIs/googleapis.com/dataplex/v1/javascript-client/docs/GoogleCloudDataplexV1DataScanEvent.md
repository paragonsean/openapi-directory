# CloudDataplexApi.GoogleCloudDataplexV1DataScanEvent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | The time when the data scan job was created. | [optional] 
**dataProfile** | [**GoogleCloudDataplexV1DataScanEventDataProfileResult**](GoogleCloudDataplexV1DataScanEventDataProfileResult.md) |  | [optional] 
**dataProfileConfigs** | [**GoogleCloudDataplexV1DataScanEventDataProfileAppliedConfigs**](GoogleCloudDataplexV1DataScanEventDataProfileAppliedConfigs.md) |  | [optional] 
**dataQuality** | [**GoogleCloudDataplexV1DataScanEventDataQualityResult**](GoogleCloudDataplexV1DataScanEventDataQualityResult.md) |  | [optional] 
**dataQualityConfigs** | [**GoogleCloudDataplexV1DataScanEventDataQualityAppliedConfigs**](GoogleCloudDataplexV1DataScanEventDataQualityAppliedConfigs.md) |  | [optional] 
**dataSource** | **String** | The data source of the data scan | [optional] 
**endTime** | **String** | The time when the data scan job finished. | [optional] 
**jobId** | **String** | The identifier of the specific data scan job this log entry is for. | [optional] 
**message** | **String** | The message describing the data scan job event. | [optional] 
**postScanActionsResult** | [**GoogleCloudDataplexV1DataScanEventPostScanActionsResult**](GoogleCloudDataplexV1DataScanEventPostScanActionsResult.md) |  | [optional] 
**scope** | **String** | The scope of the data scan (e.g. full, incremental). | [optional] 
**specVersion** | **String** | A version identifier of the spec which was used to execute this job. | [optional] 
**startTime** | **String** | The time when the data scan job started to run. | [optional] 
**state** | **String** | The status of the data scan job. | [optional] 
**trigger** | **String** | The trigger type of the data scan job. | [optional] 
**type** | **String** | The type of the data scan. | [optional] 



## Enum: ScopeEnum


* `SCOPE_UNSPECIFIED` (value: `"SCOPE_UNSPECIFIED"`)

* `FULL` (value: `"FULL"`)

* `INCREMENTAL` (value: `"INCREMENTAL"`)





## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `STARTED` (value: `"STARTED"`)

* `SUCCEEDED` (value: `"SUCCEEDED"`)

* `FAILED` (value: `"FAILED"`)

* `CANCELLED` (value: `"CANCELLED"`)

* `CREATED` (value: `"CREATED"`)





## Enum: TriggerEnum


* `TRIGGER_UNSPECIFIED` (value: `"TRIGGER_UNSPECIFIED"`)

* `ON_DEMAND` (value: `"ON_DEMAND"`)

* `SCHEDULE` (value: `"SCHEDULE"`)





## Enum: TypeEnum


* `SCAN_TYPE_UNSPECIFIED` (value: `"SCAN_TYPE_UNSPECIFIED"`)

* `DATA_PROFILE` (value: `"DATA_PROFILE"`)

* `DATA_QUALITY` (value: `"DATA_QUALITY"`)




