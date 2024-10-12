# PolyApi.Asset

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorName** | **String** | The author&#39;s publicly visible name. Use this name when giving credit to the author. For more information, see [Licensing](/poly/discover/licensing). | [optional] 
**createTime** | **String** | For published assets, the time when the asset was published. For unpublished assets, the time when the asset was created. | [optional] 
**description** | **String** | The human-readable description, set by the asset&#39;s author. | [optional] 
**displayName** | **String** | The human-readable name, set by the asset&#39;s author. | [optional] 
**formats** | [**[Format]**](Format.md) | A list of Formats where each format describes one representation of the asset. | [optional] 
**isCurated** | **Boolean** | Whether this asset has been curated by the Poly team. | [optional] 
**license** | **String** | The license under which the author has made the asset available for use, if any. | [optional] 
**metadata** | **String** | Application-defined opaque metadata for this asset. This field is only returned when querying for the signed-in user&#39;s own assets, not for public assets. This string is limited to 1K chars. It is up to the creator of the asset to define the format for this string (for example, JSON). | [optional] 
**name** | **String** | The unique identifier for the asset in the form: &#x60;assets/{ASSET_ID}&#x60;. | [optional] 
**presentationParams** | [**PresentationParams**](PresentationParams.md) |  | [optional] 
**remixInfo** | [**RemixInfo**](RemixInfo.md) |  | [optional] 
**thumbnail** | **File** |  | [optional] 
**updateTime** | **String** | The time when the asset was last modified. For published assets, whose contents are immutable, the update time changes only when metadata properties, such as visibility, are updated. | [optional] 
**visibility** | **String** | The visibility of the asset and who can access it. | [optional] 



## Enum: LicenseEnum


* `UNKNOWN` (value: `"UNKNOWN"`)

* `CREATIVE_COMMONS_BY` (value: `"CREATIVE_COMMONS_BY"`)

* `ALL_RIGHTS_RESERVED` (value: `"ALL_RIGHTS_RESERVED"`)





## Enum: VisibilityEnum


* `VISIBILITY_UNSPECIFIED` (value: `"VISIBILITY_UNSPECIFIED"`)

* `PRIVATE` (value: `"PRIVATE"`)

* `UNLISTED` (value: `"UNLISTED"`)

* `PUBLIC` (value: `"PUBLIC"`)




