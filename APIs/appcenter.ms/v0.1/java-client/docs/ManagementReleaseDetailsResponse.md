

# ManagementReleaseDetailsResponse

Details of an uploaded release

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**buildVersion** | **String** | The release&#39;s buildVersion.&lt;br&gt; For iOS: CFBundleVersion from info.plist.&lt;br&gt; For Android: android:versionCode from AppManifest.xml.  |  [optional] |
|**createdAt** | **String** | UTC time the release was created in ISO 8601 format. |  [optional] |
|**deletedAt** | **String** | UTC time the release was created in ISO 8601 format. |  [optional] |
|**distinctId** | **Integer** | ID identifying this unique release. |  [optional] |
|**enabled** | **Boolean** | This value determines the whether a release currently is enabled or disabled. |  [optional] |
|**origin** | [**OriginEnum**](#OriginEnum) | The release&#39;s origin |  [optional] |
|**sortVersion** | **String** | The release&#39;s sortVersion. |  [optional] |
|**version** | **String** | The release&#39;s short version.&lt;br&gt; For iOS: CFBundleShortVersionString from info.plist.&lt;br&gt; For Android: android:versionName from AppManifest.xml.  |  [optional] |



## Enum: OriginEnum

| Name | Value |
|---- | -----|
| HOCKEYAPP | &quot;hockeyapp&quot; |
| APPCENTER | &quot;appcenter&quot; |



