# RudderApi.NodeFullSoftwareUpdateInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arch** | **String** | CPU architecture of the update | [optional] 
**description** | **String** | details about the content of the update, if available | [optional] 
**from** | **String** | tool that discovered that update | [optional] 
**ids** | **[String]** |  | [optional] 
**kind** | **String** | if available, kind of patch provided by that update, else none | [optional] 
**name** | **String** | name of software that can be updated | [optional] 
**severity** | **String** | if available, the severity of the update | [optional] 
**source** | **String** | information about the source providing that update | [optional] 
**version** | **String** | available version for software | [optional] 



## Enum: KindEnum


* `none` (value: `"none"`)

* `security` (value: `"security"`)

* `defect` (value: `"defect"`)

* `enhancement` (value: `"enhancement"`)

* `other` (value: `"other"`)





## Enum: SeverityEnum


* `critical` (value: `"critical"`)

* `high` (value: `"high"`)

* `moderate` (value: `"moderate"`)

* `low` (value: `"low"`)

* `other` (value: `"other"`)




