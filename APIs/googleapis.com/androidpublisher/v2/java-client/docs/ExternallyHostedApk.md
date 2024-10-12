

# ExternallyHostedApk

Defines an APK available for this application that is hosted externally and not uploaded to Google Play. This function is only available to enterprises who are using Google Play for Work, and whos application is restricted to the enterprise private channel

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applicationLabel** | **String** | The application label. |  [optional] |
|**certificateBase64s** | **List&lt;String&gt;** | A certificate (or array of certificates if a certificate-chain is used) used to signed this APK, represented as a base64 encoded byte array. |  [optional] |
|**externallyHostedUrl** | **String** | The URL at which the APK is hosted. This must be an https URL. |  [optional] |
|**fileSha1Base64** | **String** | The SHA1 checksum of this APK, represented as a base64 encoded byte array. |  [optional] |
|**fileSha256Base64** | **String** | The SHA256 checksum of this APK, represented as a base64 encoded byte array. |  [optional] |
|**fileSize** | **String** | The file size in bytes of this APK. |  [optional] |
|**iconBase64** | **String** | The icon image from the APK, as a base64 encoded byte array. |  [optional] |
|**maximumSdk** | **Integer** | The maximum SDK supported by this APK (optional). |  [optional] |
|**minimumSdk** | **Integer** | The minimum SDK targeted by this APK. |  [optional] |
|**nativeCodes** | **List&lt;String&gt;** | The native code environments supported by this APK (optional). |  [optional] |
|**packageName** | **String** | The package name. |  [optional] |
|**usesFeatures** | **List&lt;String&gt;** | The features required by this APK (optional). |  [optional] |
|**usesPermissions** | [**List&lt;ExternallyHostedApkUsesPermission&gt;**](ExternallyHostedApkUsesPermission.md) | The permissions requested by this APK. |  [optional] |
|**versionCode** | **Integer** | The version code of this APK. |  [optional] |
|**versionName** | **String** | The version name of this APK. |  [optional] |



