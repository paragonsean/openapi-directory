# SensitiveDataProtectionDlp.GooglePrivacyDlpV2DataProfilePubSubMessage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | **String** | The event that caused the Pub/Sub message to be sent. | [optional] 
**profile** | [**GooglePrivacyDlpV2TableDataProfile**](GooglePrivacyDlpV2TableDataProfile.md) |  | [optional] 



## Enum: EventEnum


* `EVENT_TYPE_UNSPECIFIED` (value: `"EVENT_TYPE_UNSPECIFIED"`)

* `NEW_PROFILE` (value: `"NEW_PROFILE"`)

* `CHANGED_PROFILE` (value: `"CHANGED_PROFILE"`)

* `SCORE_INCREASED` (value: `"SCORE_INCREASED"`)

* `ERROR_CHANGED` (value: `"ERROR_CHANGED"`)




