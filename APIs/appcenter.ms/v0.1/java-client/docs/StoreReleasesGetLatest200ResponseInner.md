

# StoreReleasesGetLatest200ResponseInner

Details of an uploaded release

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**androidMinApiLevel** | **String** | The release&#39;s minimum required Android API level. |  [optional] |
|**appDisplayName** | **String** | The app&#39;s display name. |  [optional] |
|**appName** | **String** | The app&#39;s name (extracted from the uploaded release). |  [optional] |
|**bundleIdentifier** | **String** | The identifier of the apps bundle. |  [optional] |
|**distributionStores** | [**List&lt;StoreReleasesGetLatest200ResponseInnerDistributionStoresInner&gt;**](StoreReleasesGetLatest200ResponseInnerDistributionStoresInner.md) | a list of distribution stores that are associated with this release. |  [optional] |
|**downloadUrl** | **String** | The URL that hosts the binary for this release. |  [optional] |
|**fingerprint** | **String** | MD5 checksum of the release binary. |  [optional] |
|**id** | **BigDecimal** | ID identifying this unique release. |  [optional] |
|**installUrl** | [**InstallUrlEnum**](#InstallUrlEnum) | The href required to install a release on a mobile device. On iOS devices will be prefixed with &#x60;itms-services://?action&#x3D;download-manifest&amp;url&#x3D;&#x60; |  [optional] |
|**minOs** | **String** | The release&#39;s minimum required operating system. |  [optional] |
|**releaseNotes** | **String** | The release&#39;s release notes. |  [optional] |
|**shortVersion** | **String** | The release&#39;s short version.&lt;br&gt; For iOS: CFBundleShortVersionString from info.plist. For Android: android:versionName from AppManifest.xml.  |  [optional] |
|**size** | **BigDecimal** | The release&#39;s size in bytes. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | OBSOLETE. Will be removed in next version. The availability concept is now replaced with distributed. Any &#39;available&#39; release will be associated with the default distribution group of an app.&lt;/br&gt; The release state.&lt;br&gt; &lt;b&gt;available&lt;/b&gt;: The uploaded release has been distributed.&lt;br&gt; &lt;b&gt;unavailable&lt;/b&gt;: The uploaded release is not visible to the user. &lt;br&gt;  |  [optional] |
|**uploadedAt** | **String** | UTC time in ISO 8601 format of the uploaded time. |  [optional] |
|**version** | **String** | The release&#39;s version.&lt;br&gt; For iOS: CFBundleVersion from info.plist. For Android: android:versionCode from AppManifest.xml.  |  [optional] |



## Enum: InstallUrlEnum

| Name | Value |
|---- | -----|
| GROUP | &quot;group&quot; |
| STORE | &quot;store&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| AVAILABLE | &quot;available&quot; |
| UNAVAILABLE | &quot;unavailable&quot; |



