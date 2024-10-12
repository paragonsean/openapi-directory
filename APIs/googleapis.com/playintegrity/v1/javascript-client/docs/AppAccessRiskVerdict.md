# GooglePlayIntegrityApi.AppAccessRiskVerdict

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**otherApps** | **String** | Required. App access risk verdict related to apps that are not installed by Google Play, and are not preloaded on the system image by the device manufacturer. | [optional] 
**playOrSystemApps** | **String** | Required. App access risk verdict related to apps that are not installed by the Google Play Store, and are not preloaded on the system image by the device manufacturer. | [optional] 



## Enum: OtherAppsEnum


* `UNKNOWN` (value: `"UNKNOWN"`)

* `UNEVALUATED` (value: `"UNEVALUATED"`)

* `NOT_INSTALLED` (value: `"NOT_INSTALLED"`)

* `INSTALLED` (value: `"INSTALLED"`)

* `CAPTURING` (value: `"CAPTURING"`)

* `CONTROLLING` (value: `"CONTROLLING"`)





## Enum: PlayOrSystemAppsEnum


* `UNKNOWN` (value: `"UNKNOWN"`)

* `UNEVALUATED` (value: `"UNEVALUATED"`)

* `NOT_INSTALLED` (value: `"NOT_INSTALLED"`)

* `INSTALLED` (value: `"INSTALLED"`)

* `CAPTURING` (value: `"CAPTURING"`)

* `CONTROLLING` (value: `"CONTROLLING"`)




