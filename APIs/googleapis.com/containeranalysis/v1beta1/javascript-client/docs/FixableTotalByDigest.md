# ContainerAnalysisApi.FixableTotalByDigest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fixableCount** | **String** | The number of fixable vulnerabilities associated with this resource. | [optional] 
**resource** | [**Resource**](Resource.md) |  | [optional] 
**severity** | **String** | The severity for this count. SEVERITY_UNSPECIFIED indicates total across all severities. | [optional] 
**totalCount** | **String** | The total number of vulnerabilities associated with this resource. | [optional] 



## Enum: SeverityEnum


* `SEVERITY_UNSPECIFIED` (value: `"SEVERITY_UNSPECIFIED"`)

* `MINIMAL` (value: `"MINIMAL"`)

* `LOW` (value: `"LOW"`)

* `MEDIUM` (value: `"MEDIUM"`)

* `HIGH` (value: `"HIGH"`)

* `CRITICAL` (value: `"CRITICAL"`)




