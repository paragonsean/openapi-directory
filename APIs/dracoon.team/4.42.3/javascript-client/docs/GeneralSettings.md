# DracoonApi.GeneralSettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authTokenRestrictions** | [**AuthTokenRestrictions**](AuthTokenRestrictions.md) |  | [optional] 
**cryptoEnabled** | **Boolean** | Activation status of client-side encryption.  Can only be enabled once; disabling is not possible. | [optional] 
**emailNotificationButtonEnabled** | **Boolean** | Enable email notification button | [optional] 
**eulaEnabled** | **Boolean** | Each user has to confirm the EULA at first login. | [optional] 
**hideLoginInputFields** | **Boolean** | &amp;#128679; Deprecated since v4.42.0  Defines if login fields should be hidden | [optional] 
**mediaServerEnabled** | **Boolean** | &amp;#128679; Deprecated since v4.12.0  Determines if the media server is enabled | [optional] 
**s3TagsEnabled** | **Boolean** | &amp;#128640; Since v4.9.0  Defines if S3 tags are enabled | [optional] 
**sharePasswordSmsEnabled** | **Boolean** | Allow sending of share passwords via SMS | [optional] 
**useS3Storage** | **Boolean** | Defines if S3 is used as storage backend | [optional] 
**weakPasswordEnabled** | **Boolean** | &amp;#128679; Deprecated since v4.14.0  Allow weak password  * A weak password has to fulfill the following criteria:     * is at least 8 characters long     * contains letters and numbers  * A strong password has to fulfill the following criteria in addition:     * contains at least one special character     * contains upper and lower case characters  Please use &#x60;GET /system/config/policies/passwords&#x60; API to get configured password policies. | [optional] 


