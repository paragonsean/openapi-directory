# GooglePlayAndroidDeveloperApi.TrackRelease

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**countryTargeting** | [**CountryTargeting**](CountryTargeting.md) |  | [optional] 
**inAppUpdatePriority** | **Number** | In-app update priority of the release. All newly added APKs in the release will be considered at this priority. Can take values in the range [0, 5], with 5 the highest priority. Defaults to 0. in_app_update_priority can not be updated once the release is rolled out. See https://developer.android.com/guide/playcore/in-app-updates. | [optional] 
**name** | **String** | The release name. Not required to be unique. If not set, the name is generated from the APK&#39;s version_name. If the release contains multiple APKs, the name is generated from the date. | [optional] 
**releaseNotes** | [**[LocalizedText]**](LocalizedText.md) | A description of what is new in this release. | [optional] 
**status** | **String** | The status of the release. | [optional] 
**userFraction** | **Number** | Fraction of users who are eligible for a staged release. 0 &lt; fraction &lt; 1. Can only be set when status is \&quot;inProgress\&quot; or \&quot;halted\&quot;. | [optional] 
**versionCodes** | **[String]** | Version codes of all APKs in the release. Must include version codes to retain from previous releases. | [optional] 



## Enum: StatusEnum


* `statusUnspecified` (value: `"statusUnspecified"`)

* `draft` (value: `"draft"`)

* `inProgress` (value: `"inProgress"`)

* `halted` (value: `"halted"`)

* `completed` (value: `"completed"`)




