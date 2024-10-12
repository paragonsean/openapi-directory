

# Asset

Represents and describes an asset in the Poly library. An asset is a 3D model or scene created using [Tilt Brush](//www.tiltbrush.com), [Blocks](//vr.google.com/blocks/), or any 3D program that produces a file that can be upload to Poly.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authorName** | **String** | The author&#39;s publicly visible name. Use this name when giving credit to the author. For more information, see [Licensing](/poly/discover/licensing). |  [optional] |
|**createTime** | **String** | For published assets, the time when the asset was published. For unpublished assets, the time when the asset was created. |  [optional] |
|**description** | **String** | The human-readable description, set by the asset&#39;s author. |  [optional] |
|**displayName** | **String** | The human-readable name, set by the asset&#39;s author. |  [optional] |
|**formats** | [**List&lt;Format&gt;**](Format.md) | A list of Formats where each format describes one representation of the asset. |  [optional] |
|**isCurated** | **Boolean** | Whether this asset has been curated by the Poly team. |  [optional] |
|**license** | [**LicenseEnum**](#LicenseEnum) | The license under which the author has made the asset available for use, if any. |  [optional] |
|**metadata** | **String** | Application-defined opaque metadata for this asset. This field is only returned when querying for the signed-in user&#39;s own assets, not for public assets. This string is limited to 1K chars. It is up to the creator of the asset to define the format for this string (for example, JSON). |  [optional] |
|**name** | **String** | The unique identifier for the asset in the form: &#x60;assets/{ASSET_ID}&#x60;. |  [optional] |
|**presentationParams** | [**PresentationParams**](PresentationParams.md) |  |  [optional] |
|**remixInfo** | [**RemixInfo**](RemixInfo.md) |  |  [optional] |
|**thumbnail** | [**ModelFile**](ModelFile.md) |  |  [optional] |
|**updateTime** | **String** | The time when the asset was last modified. For published assets, whose contents are immutable, the update time changes only when metadata properties, such as visibility, are updated. |  [optional] |
|**visibility** | [**VisibilityEnum**](#VisibilityEnum) | The visibility of the asset and who can access it. |  [optional] |



## Enum: LicenseEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;UNKNOWN&quot; |
| CREATIVE_COMMONS_BY | &quot;CREATIVE_COMMONS_BY&quot; |
| ALL_RIGHTS_RESERVED | &quot;ALL_RIGHTS_RESERVED&quot; |



## Enum: VisibilityEnum

| Name | Value |
|---- | -----|
| VISIBILITY_UNSPECIFIED | &quot;VISIBILITY_UNSPECIFIED&quot; |
| PRIVATE | &quot;PRIVATE&quot; |
| UNLISTED | &quot;UNLISTED&quot; |
| PUBLIC | &quot;PUBLIC&quot; |



