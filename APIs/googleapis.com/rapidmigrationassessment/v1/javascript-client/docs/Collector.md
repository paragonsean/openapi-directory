# RapidMigrationAssessmentApi.Collector

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket** | **String** | Output only. Store cloud storage bucket name (which is a guid) created with this Collector. | [optional] [readonly] 
**clientVersion** | **String** | Output only. Client version. | [optional] [readonly] 
**collectionDays** | **Number** | How many days to collect data. | [optional] 
**createTime** | **String** | Output only. Create time stamp. | [optional] [readonly] 
**description** | **String** | User specified description of the Collector. | [optional] 
**displayName** | **String** | User specified name of the Collector. | [optional] 
**eulaUri** | **String** | Uri for EULA (End User License Agreement) from customer. | [optional] 
**expectedAssetCount** | **String** | User specified expected asset count. | [optional] 
**guestOsScan** | [**GuestOsScan**](GuestOsScan.md) |  | [optional] 
**labels** | **{String: String}** | Labels as key value pairs. | [optional] 
**name** | **String** | name of resource. | [optional] 
**serviceAccount** | **String** | Service Account email used to ingest data to this Collector. | [optional] 
**state** | **String** | Output only. State of the Collector. | [optional] [readonly] 
**updateTime** | **String** | Output only. Update time stamp. | [optional] [readonly] 
**vsphereScan** | [**VSphereScan**](VSphereScan.md) |  | [optional] 



## Enum: StateEnum


* `UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `INITIALIZING` (value: `"STATE_INITIALIZING"`)

* `READY_TO_USE` (value: `"STATE_READY_TO_USE"`)

* `REGISTERED` (value: `"STATE_REGISTERED"`)

* `ACTIVE` (value: `"STATE_ACTIVE"`)

* `PAUSED` (value: `"STATE_PAUSED"`)

* `DELETING` (value: `"STATE_DELETING"`)

* `DECOMMISSIONED` (value: `"STATE_DECOMMISSIONED"`)

* `ERROR` (value: `"STATE_ERROR"`)




