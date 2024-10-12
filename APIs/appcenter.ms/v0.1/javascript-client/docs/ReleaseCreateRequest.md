# AppCenterClient.ReleaseCreateRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appexProvisioningProfiles** | [**[ReleaseCreateRequestAppexProvisioningProfilesInner]**](ReleaseCreateRequestAppexProvisioningProfilesInner.md) | iOS app extension provisioning profiles included in the release. | [optional] 
**buildVersion** | **String** | The release&#39;s short version.&lt;br&gt; For iOS: CFBundleShortVersionString from info.plist.&lt;br&gt; For Android: android:versionName from AppManifest.xml.  | [optional] 
**deviceFamily** | **String** | The release&#39;s device family. | [optional] 
**fileExtension** | **String** | The file extension of the asset. Does not include the initial period. | [optional] 
**fingerprint** | **String** | MD5 checksum of the release binary. | 
**iconAssetId** | **String** | The assetId associated with the icon uploaded to app center file upload service. | [optional] 
**ipaUuids** | [**[ReleaseCreateRequestIpaUuidsInner]**](ReleaseCreateRequestIpaUuidsInner.md) | A list of UUIDs for architectures for an iOS app. | [optional] 
**languages** | **[String]** | The languages supported by the release. Limited to 510 characters in a serialized array. | [optional] 
**minimumOsVersion** | **String** | The release&#39;s minimum required operating system. | [optional] 
**packageUrl** | **String** | The URL to the release&#39;s binary. | [optional] 
**provision** | [**ReleaseCreateRequestAppexProvisioningProfilesInner**](ReleaseCreateRequestAppexProvisioningProfilesInner.md) |  | [optional] 
**proxyFlow** | **Boolean** | If true this release was uploaded to the AKS upload proxy | [optional] 
**size** | **Number** | The release&#39;s size in bytes. | 
**uniqueIdentifier** | **String** | The identifier of the app&#39;s bundle. | [optional] 
**uploadId** | **String** | The upload id associated with the release, to map to the releases upload table. | 
**version** | **String** | The release&#39;s version.&lt;br&gt; For iOS: CFBundleVersion from info.plist.&lt;br&gt; For Android: android:versionCode from AppManifest.xml.  | [optional] 


