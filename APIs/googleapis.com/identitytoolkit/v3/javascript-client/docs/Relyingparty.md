# GoogleIdentityToolkitApi.Relyingparty

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**androidInstallApp** | **Boolean** | whether or not to install the android app on the device where the link is opened | [optional] 
**androidMinimumVersion** | **String** | minimum version of the app. if the version on the device is lower than this version then the user is taken to the play store to upgrade the app | [optional] 
**androidPackageName** | **String** | android package name of the android app to handle the action code | [optional] 
**canHandleCodeInApp** | **Boolean** | whether or not the app can handle the oob code without first going to web | [optional] 
**captchaResp** | **String** | The recaptcha response from the user. | [optional] 
**challenge** | **String** | The recaptcha challenge presented to the user. | [optional] 
**continueUrl** | **String** | The url to continue to the Gitkit app | [optional] 
**email** | **String** | The email of the user. | [optional] 
**iOSAppStoreId** | **String** | iOS app store id to download the app if it&#39;s not already installed | [optional] 
**iOSBundleId** | **String** | the iOS bundle id of iOS app to handle the action code | [optional] 
**idToken** | **String** | The user&#39;s Gitkit login token for email change. | [optional] 
**kind** | **String** | The fixed string \&quot;identitytoolkit#relyingparty\&quot;. | [optional] [default to &#39;identitytoolkit#relyingparty&#39;]
**newEmail** | **String** | The new email if the code is for email change. | [optional] 
**requestType** | **String** | The request type. | [optional] 
**userIp** | **String** | The IP address of the user. | [optional] 


