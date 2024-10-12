

# CreativeSize

Specifies the size of the creative.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowedFormats** | [**List&lt;AllowedFormatsEnum&gt;**](#List&lt;AllowedFormatsEnum&gt;) | What formats are allowed by the publisher. If this repeated field is empty then all formats are allowed. For example, if this field contains AllowedFormatType.AUDIO then the publisher only allows an audio ad (without any video). |  [optional] |
|**companionSizes** | [**List&lt;Size&gt;**](Size.md) | For video creatives specifies the sizes of companion ads (if present). Companion sizes may be filled in only when creative_size_type &#x3D; VIDEO |  [optional] |
|**creativeSizeType** | [**CreativeSizeTypeEnum**](#CreativeSizeTypeEnum) | The creative size type. |  [optional] |
|**nativeTemplate** | [**NativeTemplateEnum**](#NativeTemplateEnum) | Output only. The native template for this creative. It will have a value only if creative_size_type &#x3D; CreativeSizeType.NATIVE. |  [optional] |
|**size** | [**Size**](Size.md) |  |  [optional] |
|**skippableAdType** | [**SkippableAdTypeEnum**](#SkippableAdTypeEnum) | The type of skippable ad for this creative. It will have a value only if creative_size_type &#x3D; CreativeSizeType.VIDEO. |  [optional] |



## Enum: List&lt;AllowedFormatsEnum&gt;

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;UNKNOWN&quot; |
| AUDIO | &quot;AUDIO&quot; |



## Enum: CreativeSizeTypeEnum

| Name | Value |
|---- | -----|
| CREATIVE_SIZE_TYPE_UNSPECIFIED | &quot;CREATIVE_SIZE_TYPE_UNSPECIFIED&quot; |
| REGULAR | &quot;REGULAR&quot; |
| INTERSTITIAL | &quot;INTERSTITIAL&quot; |
| VIDEO | &quot;VIDEO&quot; |
| NATIVE | &quot;NATIVE&quot; |



## Enum: NativeTemplateEnum

| Name | Value |
|---- | -----|
| UNKNOWN_NATIVE_TEMPLATE | &quot;UNKNOWN_NATIVE_TEMPLATE&quot; |
| NATIVE_CONTENT_AD | &quot;NATIVE_CONTENT_AD&quot; |
| NATIVE_APP_INSTALL_AD | &quot;NATIVE_APP_INSTALL_AD&quot; |
| NATIVE_VIDEO_CONTENT_AD | &quot;NATIVE_VIDEO_CONTENT_AD&quot; |
| NATIVE_VIDEO_APP_INSTALL_AD | &quot;NATIVE_VIDEO_APP_INSTALL_AD&quot; |



## Enum: SkippableAdTypeEnum

| Name | Value |
|---- | -----|
| SKIPPABLE_AD_TYPE_UNSPECIFIED | &quot;SKIPPABLE_AD_TYPE_UNSPECIFIED&quot; |
| GENERIC | &quot;GENERIC&quot; |
| INSTREAM_SELECT | &quot;INSTREAM_SELECT&quot; |
| NOT_SKIPPABLE | &quot;NOT_SKIPPABLE&quot; |



