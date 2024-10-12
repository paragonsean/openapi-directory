# AnalyticsReportingApi.SearchUserActivityResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nextPageToken** | **String** | This token should be passed to [SearchUserActivityRequest](#SearchUserActivityRequest) to retrieve the next page. | [optional] 
**sampleRate** | **Number** | This field represents the [sampling rate](https://support.google.com/analytics/answer/2637192) for the given request and is a number between 0.0 to 1.0. See [developer guide](/analytics/devguides/reporting/core/v4/basics#sampling) for details. | [optional] 
**sessions** | [**[UserActivitySession]**](UserActivitySession.md) | Each record represents a session (device details, duration, etc). | [optional] 
**totalRows** | **Number** | Total rows returned by this query (across different pages). | [optional] 


