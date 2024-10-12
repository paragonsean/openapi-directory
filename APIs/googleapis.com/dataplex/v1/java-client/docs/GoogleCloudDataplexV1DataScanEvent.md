

# GoogleCloudDataplexV1DataScanEvent

These messages contain information about the execution of a datascan. The monitored resource is 'DataScan' Next ID: 13

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | The time when the data scan job was created. |  [optional] |
|**dataProfile** | [**GoogleCloudDataplexV1DataScanEventDataProfileResult**](GoogleCloudDataplexV1DataScanEventDataProfileResult.md) |  |  [optional] |
|**dataProfileConfigs** | [**GoogleCloudDataplexV1DataScanEventDataProfileAppliedConfigs**](GoogleCloudDataplexV1DataScanEventDataProfileAppliedConfigs.md) |  |  [optional] |
|**dataQuality** | [**GoogleCloudDataplexV1DataScanEventDataQualityResult**](GoogleCloudDataplexV1DataScanEventDataQualityResult.md) |  |  [optional] |
|**dataQualityConfigs** | [**GoogleCloudDataplexV1DataScanEventDataQualityAppliedConfigs**](GoogleCloudDataplexV1DataScanEventDataQualityAppliedConfigs.md) |  |  [optional] |
|**dataSource** | **String** | The data source of the data scan |  [optional] |
|**endTime** | **String** | The time when the data scan job finished. |  [optional] |
|**jobId** | **String** | The identifier of the specific data scan job this log entry is for. |  [optional] |
|**message** | **String** | The message describing the data scan job event. |  [optional] |
|**postScanActionsResult** | [**GoogleCloudDataplexV1DataScanEventPostScanActionsResult**](GoogleCloudDataplexV1DataScanEventPostScanActionsResult.md) |  |  [optional] |
|**scope** | [**ScopeEnum**](#ScopeEnum) | The scope of the data scan (e.g. full, incremental). |  [optional] |
|**specVersion** | **String** | A version identifier of the spec which was used to execute this job. |  [optional] |
|**startTime** | **String** | The time when the data scan job started to run. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The status of the data scan job. |  [optional] |
|**trigger** | [**TriggerEnum**](#TriggerEnum) | The trigger type of the data scan job. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of the data scan. |  [optional] |



## Enum: ScopeEnum

| Name | Value |
|---- | -----|
| SCOPE_UNSPECIFIED | &quot;SCOPE_UNSPECIFIED&quot; |
| FULL | &quot;FULL&quot; |
| INCREMENTAL | &quot;INCREMENTAL&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| STARTED | &quot;STARTED&quot; |
| SUCCEEDED | &quot;SUCCEEDED&quot; |
| FAILED | &quot;FAILED&quot; |
| CANCELLED | &quot;CANCELLED&quot; |
| CREATED | &quot;CREATED&quot; |



## Enum: TriggerEnum

| Name | Value |
|---- | -----|
| TRIGGER_UNSPECIFIED | &quot;TRIGGER_UNSPECIFIED&quot; |
| ON_DEMAND | &quot;ON_DEMAND&quot; |
| SCHEDULE | &quot;SCHEDULE&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| SCAN_TYPE_UNSPECIFIED | &quot;SCAN_TYPE_UNSPECIFIED&quot; |
| DATA_PROFILE | &quot;DATA_PROFILE&quot; |
| DATA_QUALITY | &quot;DATA_QUALITY&quot; |



