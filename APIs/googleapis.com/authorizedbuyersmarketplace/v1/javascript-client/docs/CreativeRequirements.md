# AuthorizedBuyersMarketplaceApi.CreativeRequirements

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creativeFormat** | **String** | Output only. The format of the creative, only applicable for programmatic guaranteed and preferred deals. | [optional] [readonly] 
**creativePreApprovalPolicy** | **String** | Output only. Specifies the creative pre-approval policy. | [optional] [readonly] 
**creativeSafeFrameCompatibility** | **String** | Output only. Specifies whether the creative is safeFrame compatible. | [optional] [readonly] 
**maxAdDurationMs** | **String** | Output only. The max duration of the video creative in milliseconds. only applicable for deals with video creatives. | [optional] [readonly] 
**programmaticCreativeSource** | **String** | Output only. Specifies the creative source for programmatic deals. PUBLISHER means creative is provided by seller and ADVERTISER means creative is provided by the buyer. | [optional] [readonly] 
**skippableAdType** | **String** | Output only. Skippable video ads allow viewers to skip ads after 5 seconds. Only applicable for deals with video creatives. | [optional] [readonly] 



## Enum: CreativeFormatEnum


* `CREATIVE_FORMAT_UNSPECIFIED` (value: `"CREATIVE_FORMAT_UNSPECIFIED"`)

* `DISPLAY` (value: `"DISPLAY"`)

* `VIDEO` (value: `"VIDEO"`)

* `AUDIO` (value: `"AUDIO"`)





## Enum: CreativePreApprovalPolicyEnum


* `CREATIVE_PRE_APPROVAL_POLICY_UNSPECIFIED` (value: `"CREATIVE_PRE_APPROVAL_POLICY_UNSPECIFIED"`)

* `SELLER_PRE_APPROVAL_REQUIRED` (value: `"SELLER_PRE_APPROVAL_REQUIRED"`)

* `SELLER_PRE_APPROVAL_NOT_REQUIRED` (value: `"SELLER_PRE_APPROVAL_NOT_REQUIRED"`)





## Enum: CreativeSafeFrameCompatibilityEnum


* `CREATIVE_SAFE_FRAME_COMPATIBILITY_UNSPECIFIED` (value: `"CREATIVE_SAFE_FRAME_COMPATIBILITY_UNSPECIFIED"`)

* `COMPATIBLE` (value: `"COMPATIBLE"`)

* `INCOMPATIBLE` (value: `"INCOMPATIBLE"`)





## Enum: ProgrammaticCreativeSourceEnum


* `PROGRAMMATIC_CREATIVE_SOURCE_UNSPECIFIED` (value: `"PROGRAMMATIC_CREATIVE_SOURCE_UNSPECIFIED"`)

* `ADVERTISER` (value: `"ADVERTISER"`)

* `PUBLISHER` (value: `"PUBLISHER"`)





## Enum: SkippableAdTypeEnum


* `SKIPPABLE_AD_TYPE_UNSPECIFIED` (value: `"SKIPPABLE_AD_TYPE_UNSPECIFIED"`)

* `SKIPPABLE` (value: `"SKIPPABLE"`)

* `INSTREAM_SELECT` (value: `"INSTREAM_SELECT"`)

* `NOT_SKIPPABLE` (value: `"NOT_SKIPPABLE"`)

* `ANY` (value: `"ANY"`)




