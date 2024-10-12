

# DistributionGroupRelease

Response for getting a list of releases in a distribution group

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



## Enum: OriginEnum

| Name | Value |
|---- | -----|
| HOCKEYAPP | &quot;hockeyapp&quot; |
| APPCENTER | &quot;appcenter&quot; |



