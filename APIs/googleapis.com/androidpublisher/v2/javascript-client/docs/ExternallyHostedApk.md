# GooglePlayDeveloper.ExternallyHostedApk

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicationLabel** | **String** | The application label. | [optional] 
**certificateBase64s** | **[String]** | A certificate (or array of certificates if a certificate-chain is used) used to signed this APK, represented as a base64 encoded byte array. | [optional] 
**externallyHostedUrl** | **String** | The URL at which the APK is hosted. This must be an https URL. | [optional] 
**fileSha1Base64** | **String** | The SHA1 checksum of this APK, represented as a base64 encoded byte array. | [optional] 
**fileSha256Base64** | **String** | The SHA256 checksum of this APK, represented as a base64 encoded byte array. | [optional] 
**fileSize** | **String** | The file size in bytes of this APK. | [optional] 
**iconBase64** | **String** | The icon image from the APK, as a base64 encoded byte array. | [optional] 
**maximumSdk** | **Number** | The maximum SDK supported by this APK (optional). | [optional] 
**minimumSdk** | **Number** | The minimum SDK targeted by this APK. | [optional] 
**nativeCodes** | **[String]** | The native code environments supported by this APK (optional). | [optional] 
**packageName** | **String** | The package name. | [optional] 
**usesFeatures** | **[String]** | The features required by this APK (optional). | [optional] 
**usesPermissions** | [**[ExternallyHostedApkUsesPermission]**](ExternallyHostedApkUsesPermission.md) | The permissions requested by this APK. | [optional] 
**versionCode** | **Number** | The version code of this APK. | [optional] 
**versionName** | **String** | The version name of this APK. | [optional] 


