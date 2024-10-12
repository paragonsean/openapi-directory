

# CreativeRequirements

Message captures data about the creatives in the deal.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**creativeFormat** | [**CreativeFormatEnum**](#CreativeFormatEnum) | Output only. The format of the creative, only applicable for programmatic guaranteed and preferred deals. |  [optional] [readonly] |
|**creativePreApprovalPolicy** | [**CreativePreApprovalPolicyEnum**](#CreativePreApprovalPolicyEnum) | Output only. Specifies the creative pre-approval policy. |  [optional] [readonly] |
|**creativeSafeFrameCompatibility** | [**CreativeSafeFrameCompatibilityEnum**](#CreativeSafeFrameCompatibilityEnum) | Output only. Specifies whether the creative is safeFrame compatible. |  [optional] [readonly] |
|**maxAdDurationMs** | **String** | Output only. The max duration of the video creative in milliseconds. only applicable for deals with video creatives. |  [optional] [readonly] |
|**programmaticCreativeSource** | [**ProgrammaticCreativeSourceEnum**](#ProgrammaticCreativeSourceEnum) | Output only. Specifies the creative source for programmatic deals. PUBLISHER means creative is provided by seller and ADVERTISER means creative is provided by the buyer. |  [optional] [readonly] |
|**skippableAdType** | [**SkippableAdTypeEnum**](#SkippableAdTypeEnum) | Output only. Skippable video ads allow viewers to skip ads after 5 seconds. Only applicable for deals with video creatives. |  [optional] [readonly] |



## Enum: CreativeFormatEnum

| Name | Value |
|---- | -----|
| CREATIVE_FORMAT_UNSPECIFIED | &quot;CREATIVE_FORMAT_UNSPECIFIED&quot; |
| DISPLAY | &quot;DISPLAY&quot; |
| VIDEO | &quot;VIDEO&quot; |
| AUDIO | &quot;AUDIO&quot; |



## Enum: CreativePreApprovalPolicyEnum

| Name | Value |
|---- | -----|
| CREATIVE_PRE_APPROVAL_POLICY_UNSPECIFIED | &quot;CREATIVE_PRE_APPROVAL_POLICY_UNSPECIFIED&quot; |
| SELLER_PRE_APPROVAL_REQUIRED | &quot;SELLER_PRE_APPROVAL_REQUIRED&quot; |
| SELLER_PRE_APPROVAL_NOT_REQUIRED | &quot;SELLER_PRE_APPROVAL_NOT_REQUIRED&quot; |



## Enum: CreativeSafeFrameCompatibilityEnum

| Name | Value |
|---- | -----|
| CREATIVE_SAFE_FRAME_COMPATIBILITY_UNSPECIFIED | &quot;CREATIVE_SAFE_FRAME_COMPATIBILITY_UNSPECIFIED&quot; |
| COMPATIBLE | &quot;COMPATIBLE&quot; |
| INCOMPATIBLE | &quot;INCOMPATIBLE&quot; |



## Enum: ProgrammaticCreativeSourceEnum

| Name | Value |
|---- | -----|
| PROGRAMMATIC_CREATIVE_SOURCE_UNSPECIFIED | &quot;PROGRAMMATIC_CREATIVE_SOURCE_UNSPECIFIED&quot; |
| ADVERTISER | &quot;ADVERTISER&quot; |
| PUBLISHER | &quot;PUBLISHER&quot; |



## Enum: SkippableAdTypeEnum

| Name | Value |
|---- | -----|
| SKIPPABLE_AD_TYPE_UNSPECIFIED | &quot;SKIPPABLE_AD_TYPE_UNSPECIFIED&quot; |
| SKIPPABLE | &quot;SKIPPABLE&quot; |
| INSTREAM_SELECT | &quot;INSTREAM_SELECT&quot; |
| NOT_SKIPPABLE | &quot;NOT_SKIPPABLE&quot; |
| ANY | &quot;ANY&quot; |



