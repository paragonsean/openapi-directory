

# TesterAppRelease


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enabled** | **Boolean** | This value determines the whether a release currently is enabled or disabled. |  |
|**id** | **Integer** | ID identifying this unique release. |  |
|**isExternalBuild** | **Boolean** | This value determines if a release is external or not. |  [optional] |
|**mandatoryUpdate** | **Boolean** | A boolean which determines whether the release is a mandatory update or not. |  |
|**origin** | [**OriginEnum**](#OriginEnum) | The release&#39;s origin |  [optional] |
|**shortVersion** | **String** | The release&#39;s short version.&lt;br&gt; For iOS: CFBundleShortVersionString from info.plist.&lt;br&gt; For Android: android:versionName from AppManifest.xml.  |  |
|**uploadedAt** | **String** | UTC time in ISO 8601 format of the uploaded time. |  |
|**version** | **String** | The release&#39;s version.&lt;br&gt; For iOS: CFBundleVersion from info.plist.&lt;br&gt; For Android: android:versionCode from AppManifest.xml.  |  |
|**installUrl** | **String** | The href required to install a release on a mobile device. On iOS devices will be prefixed with &#x60;itms-services://?action&#x3D;download-manifest&amp;url&#x3D;&#x60; |  [optional] |
|**releaseNotes** | **String** | The release&#39;s release notes. |  [optional] |
|**size** | **Integer** | The release&#39;s size in bytes. |  |



## Enum: OriginEnum

| Name | Value |
|---- | -----|
| HOCKEYAPP | &quot;hockeyapp&quot; |
| APPCENTER | &quot;appcenter&quot; |



