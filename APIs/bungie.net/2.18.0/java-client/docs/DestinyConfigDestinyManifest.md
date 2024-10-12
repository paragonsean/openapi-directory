

# DestinyConfigDestinyManifest

DestinyManifest is the external-facing contract for just the properties needed by those calling the Destiny Platform.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**iconImagePyramidInfo** | [**List&lt;DestinyConfigImagePyramidEntry&gt;**](DestinyConfigImagePyramidEntry.md) | Information about the \&quot;Image Pyramid\&quot; for Destiny icons. Where possible, we create smaller versions of Destiny icons. These are found as subfolders under the location of the \&quot;original/full size\&quot; Destiny images, with the same file name and extension as the original image itself. (this lets us avoid sending largely redundant path info with every entity, at the expense of the smaller versions of the image being less discoverable) |  [optional] |
|**jsonWorldComponentContentPaths** | **Map&lt;String, Map&lt;String, String&gt;&gt;** | This points to the generated JSON that contains all the Definitions. Each key is a locale. The value is a dictionary, where the key is a definition type by name, and the value is the path to the file for that definition. WARNING: This is unsafe and subject to change - do not depend on data in these files staying around long-term. |  [optional] |
|**jsonWorldContentPaths** | **Map&lt;String, String&gt;** | This points to the generated JSON that contains all the Definitions. Each key is a locale. The value is a path to the aggregated world definitions (warning: large file!) |  [optional] |
|**mobileAssetContentPath** | **String** |  |  [optional] |
|**mobileClanBannerDatabasePath** | **String** |  |  [optional] |
|**mobileGearAssetDataBases** | [**List&lt;DestinyConfigGearAssetDataBaseDefinition&gt;**](DestinyConfigGearAssetDataBaseDefinition.md) |  |  [optional] |
|**mobileGearCDN** | **Map&lt;String, String&gt;** |  |  [optional] |
|**mobileWorldContentPaths** | **Map&lt;String, String&gt;** |  |  [optional] |
|**version** | **String** |  |  [optional] |



