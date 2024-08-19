# AdExchangeBuyerApiIi.CreativeSize

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowedFormats** | **[String]** | What formats are allowed by the publisher. If this repeated field is empty then all formats are allowed. For example, if this field contains AllowedFormatType.AUDIO then the publisher only allows an audio ad (without any video). | [optional] 
**companionSizes** | [**[Size]**](Size.md) | For video creatives specifies the sizes of companion ads (if present). Companion sizes may be filled in only when creative_size_type &#x3D; VIDEO | [optional] 
**creativeSizeType** | **String** | The creative size type. | [optional] 
**nativeTemplate** | **String** | Output only. The native template for this creative. It will have a value only if creative_size_type &#x3D; CreativeSizeType.NATIVE. | [optional] 
**size** | [**Size**](Size.md) |  | [optional] 
**skippableAdType** | **String** | The type of skippable ad for this creative. It will have a value only if creative_size_type &#x3D; CreativeSizeType.VIDEO. | [optional] 



## Enum: [AllowedFormatsEnum]


* `UNKNOWN` (value: `"UNKNOWN"`)

* `AUDIO` (value: `"AUDIO"`)





## Enum: CreativeSizeTypeEnum


* `CREATIVE_SIZE_TYPE_UNSPECIFIED` (value: `"CREATIVE_SIZE_TYPE_UNSPECIFIED"`)

* `REGULAR` (value: `"REGULAR"`)

* `INTERSTITIAL` (value: `"INTERSTITIAL"`)

* `VIDEO` (value: `"VIDEO"`)

* `NATIVE` (value: `"NATIVE"`)





## Enum: NativeTemplateEnum


* `UNKNOWN_NATIVE_TEMPLATE` (value: `"UNKNOWN_NATIVE_TEMPLATE"`)

* `NATIVE_CONTENT_AD` (value: `"NATIVE_CONTENT_AD"`)

* `NATIVE_APP_INSTALL_AD` (value: `"NATIVE_APP_INSTALL_AD"`)

* `NATIVE_VIDEO_CONTENT_AD` (value: `"NATIVE_VIDEO_CONTENT_AD"`)

* `NATIVE_VIDEO_APP_INSTALL_AD` (value: `"NATIVE_VIDEO_APP_INSTALL_AD"`)





## Enum: SkippableAdTypeEnum


* `SKIPPABLE_AD_TYPE_UNSPECIFIED` (value: `"SKIPPABLE_AD_TYPE_UNSPECIFIED"`)

* `GENERIC` (value: `"GENERIC"`)

* `INSTREAM_SELECT` (value: `"INSTREAM_SELECT"`)

* `NOT_SKIPPABLE` (value: `"NOT_SKIPPABLE"`)




