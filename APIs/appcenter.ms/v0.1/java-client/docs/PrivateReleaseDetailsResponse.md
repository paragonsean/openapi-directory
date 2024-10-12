

# PrivateReleaseDetailsResponse

Details of an uploaded release

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**androidMinApiLevel** | **String** | The release&#39;s minimum required Android API level. |  [optional] |
|**appDisplayName** | **String** | The app&#39;s display name. |  [optional] |
|**appIconUrl** | **String** | A URL to the app&#39;s icon. |  [optional] |
|**appName** | **String** | The app&#39;s name (extracted from the uploaded release). |  [optional] |
|**bundleIdentifier** | **String** | The identifier of the apps bundle. |  [optional] |
|**destinationType** | [**DestinationTypeEnum**](#DestinationTypeEnum) | The destination type.&lt;br&gt; &lt;b&gt;group&lt;/b&gt;: The release distributed to internal groups and distribution_groups details will be returned.&lt;br&gt; &lt;b&gt;store&lt;/b&gt;: The release distributed to external stores and distribution_stores details will be returned. &lt;br&gt;  |  [optional] |
|**deviceFamily** | **String** | The release&#39;s device family. |  [optional] |
|**distributionGroupId** | **String** | the destination where release is distributed |  [optional] |
|**downloadUrl** | **String** | The URL that hosts the binary for this release. |  [optional] |
|**fingerprint** | **String** | MD5 checksum of the release binary. |  [optional] |
|**id** | **Integer** | ID identifying this unique release. |  [optional] |
|**installUrl** | **String** | The href required to install a release on a mobile device. On iOS devices will be prefixed with &#x60;itms-services://?action&#x3D;download-manifest&amp;url&#x3D;&#x60; |  [optional] |
|**isExternalBuild** | **Boolean** | This value determines if a release is external or not. |  [optional] |
|**isProvisioningProfileSyncing** | **Boolean** | A flag that determines whether the release&#39;s provisioning profile is still extracted or not. |  [optional] |
|**minOs** | **String** | The release&#39;s minimum required operating system. |  [optional] |
|**origin** | [**OriginEnum**](#OriginEnum) | The release&#39;s origin |  [optional] |
|**provisioningProfileName** | **String** | The release&#39;s provisioning profile name. |  [optional] |
|**provisioningProfileType** | [**ProvisioningProfileTypeEnum**](#ProvisioningProfileTypeEnum) | The type of the provisioning profile for the requested app version. |  [optional] |
|**publishingStatus** | **String** | the publishing status of the distributed release |  [optional] |
|**releaseNotes** | **String** | The release&#39;s release notes. |  [optional] |
|**secondaryDownloadUrl** | **String** | The URL that hosts the secondary binary for this release, such as the apk file for aab releases. |  [optional] |
|**shortVersion** | **String** | The release&#39;s short version.&lt;br&gt; For iOS: CFBundleShortVersionString from info.plist. For Android: android:versionName from AppManifest.xml.  |  [optional] |
|**size** | **Integer** | The release&#39;s size in bytes. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | OBSOLETE. Will be removed in next version. The availability concept is now replaced with distributed. Any &#39;available&#39; release will be associated with the default distribution group of an app.&lt;/br&gt; The release state.&lt;br&gt; &lt;b&gt;available&lt;/b&gt;: The uploaded release has been distributed.&lt;br&gt; &lt;b&gt;unavailable&lt;/b&gt;: The uploaded release is not visible to the user. &lt;br&gt;  |  [optional] |
|**uploadedAt** | **String** | UTC time in ISO 8601 format of the uploaded time. |  [optional] |
|**version** | **String** | The release&#39;s version.&lt;br&gt; For iOS: CFBundleVersion from info.plist. For Android: android:versionCode from AppManifest.xml.  |  [optional] |



## Enum: DestinationTypeEnum

| Name | Value |
|---- | -----|
| GROUP | &quot;group&quot; |
| STORE | &quot;store&quot; |
| TESTER | &quot;tester&quot; |



## Enum: OriginEnum

| Name | Value |
|---- | -----|
| HOCKEYAPP | &quot;hockeyapp&quot; |
| APPCENTER | &quot;appcenter&quot; |



## Enum: ProvisioningProfileTypeEnum

| Name | Value |
|---- | -----|
| ADHOC | &quot;adhoc&quot; |
| ENTERPRISE | &quot;enterprise&quot; |
| OTHER | &quot;other&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| AVAILABLE | &quot;available&quot; |
| UNAVAILABLE | &quot;unavailable&quot; |



