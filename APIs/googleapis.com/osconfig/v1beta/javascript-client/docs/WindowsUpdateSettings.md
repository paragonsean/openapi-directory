# OsConfigApi.WindowsUpdateSettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**classifications** | **[String]** | Only apply updates of these windows update classifications. If empty, all updates are applied. | [optional] 
**excludes** | **[String]** | List of KBs to exclude from update. | [optional] 
**exclusivePatches** | **[String]** | An exclusive list of kbs to be updated. These are the only patches that will be updated. This field must not be used with other patch configurations. | [optional] 



## Enum: [ClassificationsEnum]


* `CLASSIFICATION_UNSPECIFIED` (value: `"CLASSIFICATION_UNSPECIFIED"`)

* `CRITICAL` (value: `"CRITICAL"`)

* `SECURITY` (value: `"SECURITY"`)

* `DEFINITION` (value: `"DEFINITION"`)

* `DRIVER` (value: `"DRIVER"`)

* `FEATURE_PACK` (value: `"FEATURE_PACK"`)

* `SERVICE_PACK` (value: `"SERVICE_PACK"`)

* `TOOL` (value: `"TOOL"`)

* `UPDATE_ROLLUP` (value: `"UPDATE_ROLLUP"`)

* `UPDATE` (value: `"UPDATE"`)




