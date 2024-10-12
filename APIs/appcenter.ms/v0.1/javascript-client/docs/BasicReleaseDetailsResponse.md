# AppCenterClient.BasicReleaseDetailsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**build** | [**ReleasesListLatest200ResponseInnerBuild**](ReleasesListLatest200ResponseInnerBuild.md) |  | [optional] 
**destinationType** | **String** | OBSOLETE. Will be removed in next version. The destination type.&lt;br&gt; &lt;b&gt;group&lt;/b&gt;: The release distributed to internal groups and distribution_groups details will be returned.&lt;br&gt; &lt;b&gt;store&lt;/b&gt;: The release distributed to external stores and distribution_stores details will be returned. &lt;br&gt;  | [optional] 
**destinations** | [**[ReleasesGetLatestByDistributionGroup200ResponseDestinationsInner]**](ReleasesGetLatestByDistributionGroup200ResponseDestinationsInner.md) | A list of distribution groups or stores. | [optional] 
**distributionGroups** | [**[ReleasesListLatest200ResponseInnerDistributionGroupsInner]**](ReleasesListLatest200ResponseInnerDistributionGroupsInner.md) | OBSOLETE. Will be removed in next version. A list of distribution groups that are associated with this release. | [optional] 
**distributionStores** | [**[ReleasesListLatest200ResponseInnerDistributionStoresInner]**](ReleasesListLatest200ResponseInnerDistributionStoresInner.md) | OBSOLETE. Will be removed in next version. A list of distribution stores that are associated with this release. | [optional] 
**enabled** | **Boolean** | This value determines the whether a release currently is enabled or disabled. | 
**fileExtension** | **String** | The file extension of the main (user-uploaded) package file. | [optional] 
**id** | **Number** | ID identifying this unique release. | 
**isExternalBuild** | **Boolean** | This value determines if a release is external or not. | [optional] 
**origin** | **String** | The release&#39;s origin | [optional] 
**shortVersion** | **String** | The release&#39;s short version.&lt;br&gt; For iOS: CFBundleShortVersionString from info.plist.&lt;br&gt; For Android: android:versionName from AppManifest.xml.  | 
**uploadedAt** | **String** | UTC time in ISO 8601 format of the uploaded time. | 
**version** | **String** | The release&#39;s version.&lt;br&gt; For iOS: CFBundleVersion from info.plist.&lt;br&gt; For Android: android:versionCode from AppManifest.xml.  | 



## Enum: DestinationTypeEnum


* `group` (value: `"group"`)

* `store` (value: `"store"`)

* `tester` (value: `"tester"`)





## Enum: OriginEnum


* `hockeyapp` (value: `"hockeyapp"`)

* `appcenter` (value: `"appcenter"`)




