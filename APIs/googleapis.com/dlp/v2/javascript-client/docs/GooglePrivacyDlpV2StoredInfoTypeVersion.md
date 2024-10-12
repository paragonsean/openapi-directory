# SensitiveDataProtectionDlp.GooglePrivacyDlpV2StoredInfoTypeVersion

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**GooglePrivacyDlpV2StoredInfoTypeConfig**](GooglePrivacyDlpV2StoredInfoTypeConfig.md) |  | [optional] 
**createTime** | **String** | Create timestamp of the version. Read-only, determined by the system when the version is created. | [optional] 
**errors** | [**[GooglePrivacyDlpV2Error]**](GooglePrivacyDlpV2Error.md) | Errors that occurred when creating this storedInfoType version, or anomalies detected in the storedInfoType data that render it unusable. Only the five most recent errors will be displayed, with the most recent error appearing first. For example, some of the data for stored custom dictionaries is put in the user&#39;s Cloud Storage bucket, and if this data is modified or deleted by the user or another system, the dictionary becomes invalid. If any errors occur, fix the problem indicated by the error message and use the UpdateStoredInfoType API method to create another version of the storedInfoType to continue using it, reusing the same &#x60;config&#x60; if it was not the source of the error. | [optional] 
**state** | **String** | Stored info type version state. Read-only, updated by the system during dictionary creation. | [optional] 
**stats** | [**GooglePrivacyDlpV2StoredInfoTypeStats**](GooglePrivacyDlpV2StoredInfoTypeStats.md) |  | [optional] 



## Enum: StateEnum


* `STORED_INFO_TYPE_STATE_UNSPECIFIED` (value: `"STORED_INFO_TYPE_STATE_UNSPECIFIED"`)

* `PENDING` (value: `"PENDING"`)

* `READY` (value: `"READY"`)

* `FAILED` (value: `"FAILED"`)

* `INVALID` (value: `"INVALID"`)




