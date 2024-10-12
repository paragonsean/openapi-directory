

# StoresBasicReleaseDetails

Basic information on a release

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**destinationType** | [**DestinationTypeEnum**](#DestinationTypeEnum) | Destination for this release. |  [optional] |
|**distributionStores** | [**List&lt;StoreReleasesList200ResponseInnerDistributionStoresInner&gt;**](StoreReleasesList200ResponseInnerDistributionStoresInner.md) | a list of distribution stores that are associated with this release. |  [optional] |
|**id** | **BigDecimal** | ID identifying this unique release. |  [optional] |
|**shortVersion** | **String** | The release&#39;s short version. For iOS: CFBundleShortVersionString from info.plist. For Android: android:versionName from AppManifest.xml.  |  [optional] |
|**uploadedAt** | **String** | UTC time in ISO 8601 format of the uploaded time. |  [optional] |
|**version** | **String** | The release&#39;s version. For iOS: CFBundleVersion from info.plist. For Android: android:versionCode from AppManifest.xml.  |  [optional] |



## Enum: DestinationTypeEnum

| Name | Value |
|---- | -----|
| GROUP | &quot;group&quot; |
| STORE | &quot;store&quot; |
| TESTER | &quot;tester&quot; |



