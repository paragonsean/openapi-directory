# AnalyticsReportingApi.Activity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activityTime** | **String** | Timestamp of the activity. If activities for a visit cross midnight and occur in two separate dates, then two sessions (one per date) share the session identifier. For example, say session ID 113472 has activity within 2019-08-20, and session ID 243742 has activity within 2019-08-25 and 2019-08-26. Session ID 113472 is one session, and session ID 243742 is two sessions. | [optional] 
**activityType** | **String** | Type of this activity. | [optional] 
**appview** | [**ScreenviewData**](ScreenviewData.md) |  | [optional] 
**campaign** | **String** | For manual campaign tracking, it is the value of the utm_campaign campaign tracking parameter. For AdWords autotagging, it is the name(s) of the online ad campaign(s) you use for the property. If you use neither, its value is (not set). | [optional] 
**channelGrouping** | **String** | The Channel Group associated with an end user&#39;s session for this View (defined by the View&#39;s Channel Groupings). | [optional] 
**customDimension** | [**[CustomDimension]**](CustomDimension.md) | A list of all custom dimensions associated with this activity. | [optional] 
**ecommerce** | [**EcommerceData**](EcommerceData.md) |  | [optional] 
**event** | [**EventData**](EventData.md) |  | [optional] 
**goals** | [**GoalSetData**](GoalSetData.md) |  | [optional] 
**hostname** | **String** | The hostname from which the tracking request was made. | [optional] 
**keyword** | **String** | For manual campaign tracking, it is the value of the utm_term campaign tracking parameter. For AdWords traffic, it contains the best matching targeting criteria. For the display network, where multiple targeting criteria could have caused the ad to show up, it returns the best matching targeting criteria as selected by Ads. This could be display_keyword, site placement, boomuserlist, user_interest, age, or gender. Otherwise its value is (not set). | [optional] 
**landingPagePath** | **String** | The first page in users&#39; sessions, or the landing page. | [optional] 
**medium** | **String** | The type of referrals. For manual campaign tracking, it is the value of the utm_medium campaign tracking parameter. For AdWords autotagging, it is cpc. If users came from a search engine detected by Google Analytics, it is organic. If the referrer is not a search engine, it is referral. If users came directly to the property and document.referrer is empty, its value is (none). | [optional] 
**pageview** | [**PageviewData**](PageviewData.md) |  | [optional] 
**source** | **String** | The source of referrals. For manual campaign tracking, it is the value of the utm_source campaign tracking parameter. For AdWords autotagging, it is google. If you use neither, it is the domain of the source (e.g., document.referrer) referring the users. It may also contain a port address. If users arrived without a referrer, its value is (direct). | [optional] 



## Enum: ActivityTypeEnum


* `ACTIVITY_TYPE_UNSPECIFIED` (value: `"ACTIVITY_TYPE_UNSPECIFIED"`)

* `PAGEVIEW` (value: `"PAGEVIEW"`)

* `SCREENVIEW` (value: `"SCREENVIEW"`)

* `GOAL` (value: `"GOAL"`)

* `ECOMMERCE` (value: `"ECOMMERCE"`)

* `EVENT` (value: `"EVENT"`)




