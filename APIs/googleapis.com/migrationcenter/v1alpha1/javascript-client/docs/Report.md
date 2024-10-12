# MigrationCenterApi.Report

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. Creation timestamp. | [optional] [readonly] 
**description** | **String** | Free-text description. | [optional] 
**displayName** | **String** | User-friendly display name. Maximum length is 63 characters. | [optional] 
**name** | **String** | Output only. Name of resource. | [optional] [readonly] 
**state** | **String** | Report creation state. | [optional] 
**summary** | [**ReportSummary**](ReportSummary.md) |  | [optional] 
**type** | **String** | Report type. | [optional] 
**updateTime** | **String** | Output only. Last update timestamp. | [optional] [readonly] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `PENDING` (value: `"PENDING"`)

* `SUCCEEDED` (value: `"SUCCEEDED"`)

* `FAILED` (value: `"FAILED"`)





## Enum: TypeEnum


* `TYPE_UNSPECIFIED` (value: `"TYPE_UNSPECIFIED"`)

* `TOTAL_COST_OF_OWNERSHIP` (value: `"TOTAL_COST_OF_OWNERSHIP"`)




