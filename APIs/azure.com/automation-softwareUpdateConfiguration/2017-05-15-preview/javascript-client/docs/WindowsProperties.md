# UpdateManagement.WindowsProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**excludedKbNumbers** | **[String]** | KB numbers excluded from the software update configuration. | [optional] 
**includedKbNumbers** | **[String]** | KB numbers included from the software update configuration. | [optional] 
**includedUpdateClassifications** | **String** | Update classification included in the software update configuration. A comma separated string with required values | [optional] 
**rebootSetting** | **String** | Reboot setting for the software update configuration. | [optional] 



## Enum: IncludedUpdateClassificationsEnum


* `Unclassified` (value: `"Unclassified"`)

* `Critical` (value: `"Critical"`)

* `Security` (value: `"Security"`)

* `UpdateRollup` (value: `"UpdateRollup"`)

* `FeaturePack` (value: `"FeaturePack"`)

* `ServicePack` (value: `"ServicePack"`)

* `Definition` (value: `"Definition"`)

* `Tools` (value: `"Tools"`)

* `Updates` (value: `"Updates"`)




