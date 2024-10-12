

# ReleaseDetailsResponse

Details of an uploaded release

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**androidMinApiLevel** | **String** | The release&#39;s minimum required Android API level. |  [optional] |
|**appDisplayName** | **String** | The app&#39;s display name. |  |
|**appIconUrl** | **String** | A URL to the app&#39;s icon. |  |
|**appName** | **String** | The app&#39;s name (extracted from the uploaded release). |  |
|**appOs** | **String** | The app&#39;s OS. |  [optional] |
|**build** | [**ReleasesGetLatestByDistributionGroup200ResponseBuild**](ReleasesGetLatestByDistributionGroup200ResponseBuild.md) |  |  [optional] |
|**bundleIdentifier** | **String** | The identifier of the apps bundle. |  [optional] |
|**canResign** | **Boolean** | In calls that allow passing &#x60;udid&#x60; in the query string, this value determines if a release can be re-signed. When true, after a re-sign, the tester will be able to install the release from his registered devices. Will not be returned for non-iOS platforms. |  [optional] |
|**destinationType** | [**DestinationTypeEnum**](#DestinationTypeEnum) | OBSOLETE. Will be removed in next version. The destination type.&lt;br&gt; &lt;b&gt;group&lt;/b&gt;: The release distributed to internal groups and distribution_groups details will be returned.&lt;br&gt; &lt;b&gt;store&lt;/b&gt;: The release distributed to external stores and distribution_stores details will be returned.&lt;br&gt; &lt;b&gt;tester&lt;/b&gt;: The release distributed testers details will be returned.&lt;br&gt;  |  [optional] |
|**destinations** | [**List&lt;ReleasesGetLatestByDistributionGroup200ResponseDestinationsInner&gt;**](ReleasesGetLatestByDistributionGroup200ResponseDestinationsInner.md) | A list of distribution groups or stores. |  [optional] |
|**deviceFamily** | **String** | The release&#39;s device family. |  [optional] |
|**distributionGroups** | [**List&lt;ReleasesGetLatestByDistributionGroup200ResponseDistributionGroupsInner&gt;**](ReleasesGetLatestByDistributionGroup200ResponseDistributionGroupsInner.md) | OBSOLETE. Will be removed in next version. A list of distribution groups that are associated with this release. |  [optional] |
|**distributionStores** | [**List&lt;ReleasesGetLatestByDistributionGroup200ResponseDistributionStoresInner&gt;**](ReleasesGetLatestByDistributionGroup200ResponseDistributionStoresInner.md) | OBSOLETE. Will be removed in next version. A list of distribution stores that are associated with this release. |  [optional] |
|**downloadUrl** | **String** | The URL that hosts the binary for this release. |  [optional] |
|**enabled** | **Boolean** | This value determines the whether a release currently is enabled or disabled. |  |
|**fingerprint** | **String** | MD5 checksum of the release binary. |  [optional] |
|**id** | **Integer** | ID identifying this unique release. |  |
|**installUrl** | **String** | The href required to install a release on a mobile device. On iOS devices will be prefixed with &#x60;itms-services://?action&#x3D;download-manifest&amp;url&#x3D;&#x60; |  [optional] |
|**isExternalBuild** | **Boolean** | This value determines if a release is external or not. |  [optional] |
|**isProvisioningProfileSyncing** | **Boolean** | A flag that determines whether the release&#39;s provisioning profile is still extracted or not. |  [optional] |
|**isUdidProvisioned** | **Boolean** | In calls that allow passing &#x60;udid&#x60; in the query string, this value will hold the provisioning status of that UDID in this release. Will be ignored for non-iOS platforms. |  [optional] |
|**minOs** | **String** | The release&#39;s minimum required operating system. |  [optional] |
|**origin** | [**OriginEnum**](#OriginEnum) | The release&#39;s origin |  [optional] |
|**packageHashes** | **List&lt;String&gt;** | Hashes for the packages. |  [optional] |
|**provisioningProfileExpiryDate** | **String** | expiration date of provisioning profile in UTC format. |  [optional] |
|**provisioningProfileName** | **String** | The release&#39;s provisioning profile name. |  [optional] |
|**provisioningProfileType** | [**ProvisioningProfileTypeEnum**](#ProvisioningProfileTypeEnum) | The type of the provisioning profile for the requested app version. |  [optional] |
|**releaseNotes** | **String** | The release&#39;s release notes. |  [optional] |
|**secondaryDownloadUrl** | **String** | The URL that hosts the secondary binary for this release, such as the apk file for aab releases. |  [optional] |
|**shortVersion** | **String** | The release&#39;s short version.&lt;br&gt; For iOS: CFBundleShortVersionString from info.plist. For Android: android:versionName from AppManifest.xml.  |  |
|**size** | **Integer** | The release&#39;s size in bytes. |  [optional] |
|**status** | **String** | Status of the release. |  [optional] |
|**uploadedAt** | **String** | UTC time in ISO 8601 format of the uploaded time. |  |
|**version** | **String** | The release&#39;s version.&lt;br&gt; For iOS: CFBundleVersion from info.plist. For Android: android:versionCode from AppManifest.xml.  |  |



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



