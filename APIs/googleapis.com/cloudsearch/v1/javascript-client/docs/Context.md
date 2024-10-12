# CloudSearchApi.Context

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app** | **[String]** | [Optional] App where the card should be shown. If missing, the card will be shown in TOPAZ. | [optional] 
**dayOfWeek** | **[Number]** | [Optional] Day of week when the card should be shown, where 0 is Monday. | [optional] 
**endDateSec** | **String** | [Optional] Date (in seconds since epoch) when the card should stop being shown. If missing, end_date_sec will be set to Jan 1st, 2100. | [optional] 
**endDayOffsetSec** | **String** | [Optional] End time in seconds, within a day, when the card should stop being shown if it&#39;s within [start_date_sec, end_date_sec]. If missing, this is set to 86400 (24 hours x 3600 sec/hour), i.e., midnight next day. | [optional] 
**locale** | **[String]** | [Optional] The locales for which the card should be triggered (e.g., en_US and en_CA). If missing, the card is going to show to clients regardless of their locale. | [optional] 
**location** | **[String]** | [Optional] Text-free locations where the card should be shown. This is expected to match the user&#39;s location in focus. If no location is specified, the card will be shown for any location. | [optional] 
**query** | **[String]** | [Required only for Answer and RHS cards - will be ignored for Homepage] cards. It&#39;s the exact case-insensitive queries that will trigger the Answer or RHS card. | [optional] 
**startDateSec** | **String** | [Optional] Date (in seconds since epoch) when the card should start being shown. If missing, start_date_sec will be Jan 1st, 1970 UTC. | [optional] 
**startDayOffsetSec** | **String** | [Optional] Start time in seconds, within a day, when the card should be shown if it&#39;s within [start_date_sec, end_date_sec]. If 0, the card will be shown from 12:00am on. | [optional] 
**surface** | **[String]** | [Optional] Surface where the card should be shown in. If missing, the card will be shown in any surface. | [optional] 
**type** | **[String]** | [Required] Type of the card (homepage, Answer or RHS). | [optional] 



## Enum: [AppEnum]


* `UNKNOWN_APP` (value: `"UNKNOWN_APP"`)

* `TOPAZ` (value: `"TOPAZ"`)

* `MOMA` (value: `"MOMA"`)





## Enum: [SurfaceEnum]


* `UNKNOWN_SURFACE` (value: `"UNKNOWN_SURFACE"`)

* `DESKTOP` (value: `"DESKTOP"`)

* `ANDROID` (value: `"ANDROID"`)

* `IOS` (value: `"IOS"`)

* `MOBILE` (value: `"MOBILE"`)

* `ANY` (value: `"ANY"`)





## Enum: [TypeEnum]


* `UNKNOWN_CARD_TYPE` (value: `"UNKNOWN_CARD_TYPE"`)

* `HOMEPAGE_CARD` (value: `"HOMEPAGE_CARD"`)

* `ANSWER_CARD` (value: `"ANSWER_CARD"`)

* `RHS_CARD` (value: `"RHS_CARD"`)




