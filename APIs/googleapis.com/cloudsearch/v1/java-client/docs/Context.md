

# Context


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**app** | [**List&lt;AppEnum&gt;**](#List&lt;AppEnum&gt;) | [Optional] App where the card should be shown. If missing, the card will be shown in TOPAZ. |  [optional] |
|**dayOfWeek** | **List&lt;Integer&gt;** | [Optional] Day of week when the card should be shown, where 0 is Monday. |  [optional] |
|**endDateSec** | **String** | [Optional] Date (in seconds since epoch) when the card should stop being shown. If missing, end_date_sec will be set to Jan 1st, 2100. |  [optional] |
|**endDayOffsetSec** | **String** | [Optional] End time in seconds, within a day, when the card should stop being shown if it&#39;s within [start_date_sec, end_date_sec]. If missing, this is set to 86400 (24 hours x 3600 sec/hour), i.e., midnight next day. |  [optional] |
|**locale** | **List&lt;String&gt;** | [Optional] The locales for which the card should be triggered (e.g., en_US and en_CA). If missing, the card is going to show to clients regardless of their locale. |  [optional] |
|**location** | **List&lt;String&gt;** | [Optional] Text-free locations where the card should be shown. This is expected to match the user&#39;s location in focus. If no location is specified, the card will be shown for any location. |  [optional] |
|**query** | **List&lt;String&gt;** | [Required only for Answer and RHS cards - will be ignored for Homepage] cards. It&#39;s the exact case-insensitive queries that will trigger the Answer or RHS card. |  [optional] |
|**startDateSec** | **String** | [Optional] Date (in seconds since epoch) when the card should start being shown. If missing, start_date_sec will be Jan 1st, 1970 UTC. |  [optional] |
|**startDayOffsetSec** | **String** | [Optional] Start time in seconds, within a day, when the card should be shown if it&#39;s within [start_date_sec, end_date_sec]. If 0, the card will be shown from 12:00am on. |  [optional] |
|**surface** | [**List&lt;SurfaceEnum&gt;**](#List&lt;SurfaceEnum&gt;) | [Optional] Surface where the card should be shown in. If missing, the card will be shown in any surface. |  [optional] |
|**type** | [**List&lt;TypeEnum&gt;**](#List&lt;TypeEnum&gt;) | [Required] Type of the card (homepage, Answer or RHS). |  [optional] |



## Enum: List&lt;AppEnum&gt;

| Name | Value |
|---- | -----|
| UNKNOWN_APP | &quot;UNKNOWN_APP&quot; |
| TOPAZ | &quot;TOPAZ&quot; |
| MOMA | &quot;MOMA&quot; |



## Enum: List&lt;SurfaceEnum&gt;

| Name | Value |
|---- | -----|
| UNKNOWN_SURFACE | &quot;UNKNOWN_SURFACE&quot; |
| DESKTOP | &quot;DESKTOP&quot; |
| ANDROID | &quot;ANDROID&quot; |
| IOS | &quot;IOS&quot; |
| MOBILE | &quot;MOBILE&quot; |
| ANY | &quot;ANY&quot; |



## Enum: List&lt;TypeEnum&gt;

| Name | Value |
|---- | -----|
| UNKNOWN_CARD_TYPE | &quot;UNKNOWN_CARD_TYPE&quot; |
| HOMEPAGE_CARD | &quot;HOMEPAGE_CARD&quot; |
| ANSWER_CARD | &quot;ANSWER_CARD&quot; |
| RHS_CARD | &quot;RHS_CARD&quot; |



