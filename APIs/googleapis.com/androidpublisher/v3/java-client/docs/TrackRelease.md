

# TrackRelease

A release within a track.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**countryTargeting** | [**CountryTargeting**](CountryTargeting.md) |  |  [optional] |
|**inAppUpdatePriority** | **Integer** | In-app update priority of the release. All newly added APKs in the release will be considered at this priority. Can take values in the range [0, 5], with 5 the highest priority. Defaults to 0. in_app_update_priority can not be updated once the release is rolled out. See https://developer.android.com/guide/playcore/in-app-updates. |  [optional] |
|**name** | **String** | The release name. Not required to be unique. If not set, the name is generated from the APK&#39;s version_name. If the release contains multiple APKs, the name is generated from the date. |  [optional] |
|**releaseNotes** | [**List&lt;LocalizedText&gt;**](LocalizedText.md) | A description of what is new in this release. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the release. |  [optional] |
|**userFraction** | **Double** | Fraction of users who are eligible for a staged release. 0 &lt; fraction &lt; 1. Can only be set when status is \&quot;inProgress\&quot; or \&quot;halted\&quot;. |  [optional] |
|**versionCodes** | **List&lt;String&gt;** | Version codes of all APKs in the release. Must include version codes to retain from previous releases. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| STATUS_UNSPECIFIED | &quot;statusUnspecified&quot; |
| DRAFT | &quot;draft&quot; |
| IN_PROGRESS | &quot;inProgress&quot; |
| HALTED | &quot;halted&quot; |
| COMPLETED | &quot;completed&quot; |



