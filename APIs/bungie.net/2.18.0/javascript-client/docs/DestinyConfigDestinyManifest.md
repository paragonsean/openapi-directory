# BungieNetApi.DestinyConfigDestinyManifest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iconImagePyramidInfo** | [**[DestinyConfigImagePyramidEntry]**](DestinyConfigImagePyramidEntry.md) | Information about the \&quot;Image Pyramid\&quot; for Destiny icons. Where possible, we create smaller versions of Destiny icons. These are found as subfolders under the location of the \&quot;original/full size\&quot; Destiny images, with the same file name and extension as the original image itself. (this lets us avoid sending largely redundant path info with every entity, at the expense of the smaller versions of the image being less discoverable) | [optional] 
**jsonWorldComponentContentPaths** | **{String: {String: String}}** | This points to the generated JSON that contains all the Definitions. Each key is a locale. The value is a dictionary, where the key is a definition type by name, and the value is the path to the file for that definition. WARNING: This is unsafe and subject to change - do not depend on data in these files staying around long-term. | [optional] 
**jsonWorldContentPaths** | **{String: String}** | This points to the generated JSON that contains all the Definitions. Each key is a locale. The value is a path to the aggregated world definitions (warning: large file!) | [optional] 
**mobileAssetContentPath** | **String** |  | [optional] 
**mobileClanBannerDatabasePath** | **String** |  | [optional] 
**mobileGearAssetDataBases** | [**[DestinyConfigGearAssetDataBaseDefinition]**](DestinyConfigGearAssetDataBaseDefinition.md) |  | [optional] 
**mobileGearCDN** | **{String: String}** |  | [optional] 
**mobileWorldContentPaths** | **{String: String}** |  | [optional] 
**version** | **String** |  | [optional] 


