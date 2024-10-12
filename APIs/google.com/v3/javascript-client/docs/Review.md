# TravelPartnerApi.Review

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | **String** | The author of the review. | [optional] 
**body** | **String** | The body of the review. | [optional] 
**languageCode** | **String** | Language of the review, such as \&quot;en\&quot;, \&quot;de\&quot;, etc. | [optional] 
**link** | **String** | The url of the review. | [optional] 
**rating** | [**[Rating]**](Rating.md) | Any ratings associated with this review. This is repeated because reviews can include ratings on different aspects of a listing, e.g. location, cleanliness, etc. | [optional] 
**reviewTime** | **String** | Unix timestamp (in seconds) of the review, in UTC+0. | [optional] 
**title** | **String** | The title of the review, for example: Great three bedrooms. | [optional] 
**type** | **String** | The type of the review. | [optional] 
**visitTime** | **String** | Unix timestamp (in seconds) of when the stay was, in UTC+0. | [optional] 



## Enum: TypeEnum


* `UNKNOWN` (value: `"UNKNOWN"`)

* `EDITORIAL` (value: `"EDITORIAL"`)

* `USER` (value: `"USER"`)




