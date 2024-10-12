# GooglePlayDeveloper.UserComment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**androidOsVersion** | **Number** | Integer Android SDK version of the user&#39;s device at the time the review was written, e.g. 23 is Marshmallow. May be absent. | [optional] 
**appVersionCode** | **Number** | Integer version code of the app as installed at the time the review was written. May be absent. | [optional] 
**appVersionName** | **String** | String version name of the app as installed at the time the review was written. May be absent. | [optional] 
**device** | **String** | Codename for the reviewer&#39;s device, e.g. klte, flounder. May be absent. | [optional] 
**deviceMetadata** | [**DeviceMetadata**](DeviceMetadata.md) |  | [optional] 
**lastModified** | [**Timestamp**](Timestamp.md) |  | [optional] 
**originalText** | **String** | Untranslated text of the review, in the case where the review has been translated. If the review has not been translated this is left blank. | [optional] 
**reviewerLanguage** | **String** | Language code for the reviewer. This is taken from the device settings so is not guaranteed to match the language the review is written in. May be absent. | [optional] 
**starRating** | **Number** | The star rating associated with the review, from 1 to 5. | [optional] 
**text** | **String** | The content of the comment, i.e. review body. In some cases users have been able to write a review with separate title and body; in those cases the title and body are concatenated and separated by a tab character. | [optional] 
**thumbsDownCount** | **Number** | Number of users who have given this review a thumbs down | [optional] 
**thumbsUpCount** | **Number** | Number of users who have given this review a thumbs up | [optional] 


