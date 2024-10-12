

# GoogleCloudDataplexV1DataScan

Represents a user-visible job which provides the insights for the related data source.For example: Data Quality: generates queries based on the rules and runs against the data to get data quality check results. Data Profile: analyzes the data in table(s) and generates insights about the structure, content and relationships (such as null percent, cardinality, min/max/mean, etc).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. The time when the scan was created. |  [optional] [readonly] |
|**data** | [**GoogleCloudDataplexV1DataSource**](GoogleCloudDataplexV1DataSource.md) |  |  [optional] |
|**dataProfileResult** | [**GoogleCloudDataplexV1DataProfileResult**](GoogleCloudDataplexV1DataProfileResult.md) |  |  [optional] |
|**dataProfileSpec** | [**GoogleCloudDataplexV1DataProfileSpec**](GoogleCloudDataplexV1DataProfileSpec.md) |  |  [optional] |
|**dataQualityResult** | [**GoogleCloudDataplexV1DataQualityResult**](GoogleCloudDataplexV1DataQualityResult.md) |  |  [optional] |
|**dataQualitySpec** | [**GoogleCloudDataplexV1DataQualitySpec**](GoogleCloudDataplexV1DataQualitySpec.md) |  |  [optional] |
|**description** | **String** | Optional. Description of the scan. Must be between 1-1024 characters. |  [optional] |
|**displayName** | **String** | Optional. User friendly display name. Must be between 1-256 characters. |  [optional] |
|**executionSpec** | [**GoogleCloudDataplexV1DataScanExecutionSpec**](GoogleCloudDataplexV1DataScanExecutionSpec.md) |  |  [optional] |
|**executionStatus** | [**GoogleCloudDataplexV1DataScanExecutionStatus**](GoogleCloudDataplexV1DataScanExecutionStatus.md) |  |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Optional. User-defined labels for the scan. |  [optional] |
|**name** | **String** | Output only. The relative resource name of the scan, of the form: projects/{project}/locations/{location_id}/dataScans/{datascan_id}, where project refers to a project_id or project_number and location_id refers to a GCP region. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. Current state of the DataScan. |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | Output only. The type of DataScan. |  [optional] [readonly] |
|**uid** | **String** | Output only. System generated globally unique ID for the scan. This ID will be different if the scan is deleted and re-created with the same name. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. The time when the scan was last updated. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| CREATING | &quot;CREATING&quot; |
| DELETING | &quot;DELETING&quot; |
| ACTION_REQUIRED | &quot;ACTION_REQUIRED&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| SCAN_TYPE_UNSPECIFIED | &quot;DATA_SCAN_TYPE_UNSPECIFIED&quot; |
| QUALITY | &quot;DATA_QUALITY&quot; |
| PROFILE | &quot;DATA_PROFILE&quot; |



