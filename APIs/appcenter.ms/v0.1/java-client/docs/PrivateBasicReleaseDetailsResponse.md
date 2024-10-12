

# PrivateBasicReleaseDetailsResponse

Basic information on a release for private apis

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**destinationType** | [**DestinationTypeEnum**](#DestinationTypeEnum) | The destination type.&lt;br&gt; &lt;b&gt;group&lt;/b&gt;: The release distributed to internal groups and distribution_groups details will be returned.&lt;br&gt; &lt;b&gt;store&lt;/b&gt;: The release distributed to external stores and distribution_stores details will be returned. &lt;br&gt;  |  [optional] |
|**distributionGroupId** | **String** | the destination id of release where it is distributed. |  [optional] |
|**id** | **Integer** | ID identifying this unique release. |  [optional] |
|**isExternalBuild** | **Boolean** | This value determines if a release is external or not. |  [optional] |
|**isLatest** | **Boolean** | Indicates if this is the latest release in the group. |  [optional] |
|**mandatoryUpdate** | **Boolean** | A boolean which determines whether the release is a mandatory update or not. |  [optional] |
|**origin** | [**OriginEnum**](#OriginEnum) | The release&#39;s origin |  [optional] |
|**publishingStatus** | **String** | the publishing status of the distributed release |  [optional] |
|**shortVersion** | **String** | The release&#39;s short version.&lt;br&gt; For iOS: CFBundleShortVersionString from info.plist.&lt;br&gt; For Android: android:versionName from AppManifest.xml.  |  [optional] |
|**uploadedAt** | **String** | UTC time in ISO 8601 format of the uploaded time. |  [optional] |
|**version** | **String** | The release&#39;s version.&lt;br&gt; For iOS: CFBundleVersion from info.plist.&lt;br&gt; For Android: android:versionCode from AppManifest.xml.  |  [optional] |



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



