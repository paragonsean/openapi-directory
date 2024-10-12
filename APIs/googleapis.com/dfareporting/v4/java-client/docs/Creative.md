

# Creative

Contains properties of a Creative.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | Account ID of this creative. This field, if left unset, will be auto-generated for both insert and update operations. Applicable to all creative types. |  [optional] |
|**active** | **Boolean** | Whether the creative is active. Applicable to all creative types. |  [optional] |
|**adParameters** | **String** | Ad parameters user for VPAID creative. This is a read-only field. Applicable to the following creative types: all VPAID. |  [optional] |
|**adTagKeys** | **List&lt;String&gt;** | Keywords for a Rich Media creative. Keywords let you customize the creative settings of a Rich Media ad running on your site without having to contact the advertiser. You can use keywords to dynamically change the look or functionality of a creative. Applicable to the following creative types: all RICH_MEDIA, and all VPAID. |  [optional] |
|**additionalSizes** | [**List&lt;Size&gt;**](Size.md) | Additional sizes associated with a responsive creative. When inserting or updating a creative either the size ID field or size width and height fields can be used. Applicable to DISPLAY creatives when the primary asset type is HTML_IMAGE. |  [optional] |
|**advertiserId** | **String** | Required. Advertiser ID of this creative. This is a required field. Applicable to all creative types. |  [optional] |
|**allowScriptAccess** | **Boolean** | Whether script access is allowed for this creative. This is a read-only and deprecated field which will automatically be set to true on update. Applicable to the following creative types: FLASH_INPAGE. |  [optional] |
|**archived** | **Boolean** | Whether the creative is archived. Applicable to all creative types. |  [optional] |
|**artworkType** | [**ArtworkTypeEnum**](#ArtworkTypeEnum) | Type of artwork used for the creative. This is a read-only field. Applicable to the following creative types: all RICH_MEDIA, and all VPAID. |  [optional] |
|**authoringSource** | [**AuthoringSourceEnum**](#AuthoringSourceEnum) | Source application where creative was authored. Presently, only DBM authored creatives will have this field set. Applicable to all creative types. |  [optional] |
|**authoringTool** | [**AuthoringToolEnum**](#AuthoringToolEnum) | Authoring tool for HTML5 banner creatives. This is a read-only field. Applicable to the following creative types: HTML5_BANNER. |  [optional] |
|**autoAdvanceImages** | **Boolean** | Whether images are automatically advanced for image gallery creatives. Applicable to the following creative types: DISPLAY_IMAGE_GALLERY. |  [optional] |
|**backgroundColor** | **String** | The 6-character HTML color code, beginning with #, for the background of the window area where the Flash file is displayed. Default is white. Applicable to the following creative types: FLASH_INPAGE. |  [optional] |
|**backupImageClickThroughUrl** | [**CreativeClickThroughUrl**](CreativeClickThroughUrl.md) |  |  [optional] |
|**backupImageFeatures** | [**List&lt;BackupImageFeaturesEnum&gt;**](#List&lt;BackupImageFeaturesEnum&gt;) | List of feature dependencies that will cause a backup image to be served if the browser that serves the ad does not support them. Feature dependencies are features that a browser must be able to support in order to render your HTML5 creative asset correctly. This field is initially auto-generated to contain all features detected by Campaign Manager for all the assets of this creative and can then be modified by the client. To reset this field, copy over all the creativeAssets&#39; detected features. Applicable to the following creative types: HTML5_BANNER. Applicable to DISPLAY when the primary asset type is not HTML_IMAGE. |  [optional] |
|**backupImageReportingLabel** | **String** | Reporting label used for HTML5 banner backup image. Applicable to the following creative types: DISPLAY when the primary asset type is not HTML_IMAGE. |  [optional] |
|**backupImageTargetWindow** | [**TargetWindow**](TargetWindow.md) |  |  [optional] |
|**clickTags** | [**List&lt;ClickTag&gt;**](ClickTag.md) | Click tags of the creative. For DISPLAY, FLASH_INPAGE, and HTML5_BANNER creatives, this is a subset of detected click tags for the assets associated with this creative. After creating a flash asset, detected click tags will be returned in the creativeAssetMetadata. When inserting the creative, populate the creative clickTags field using the creativeAssetMetadata.clickTags field. For DISPLAY_IMAGE_GALLERY creatives, there should be exactly one entry in this list for each image creative asset. A click tag is matched with a corresponding creative asset by matching the clickTag.name field with the creativeAsset.assetIdentifier.name field. Applicable to the following creative types: DISPLAY_IMAGE_GALLERY, FLASH_INPAGE, HTML5_BANNER. Applicable to DISPLAY when the primary asset type is not HTML_IMAGE. |  [optional] |
|**commercialId** | **String** | Industry standard ID assigned to creative for reach and frequency. Applicable to INSTREAM_VIDEO_REDIRECT creatives. |  [optional] |
|**companionCreatives** | **List&lt;String&gt;** | List of companion creatives assigned to an in-Stream video creative. Acceptable values include IDs of existing flash and image creatives. Applicable to the following creative types: all VPAID, all INSTREAM_AUDIO and all INSTREAM_VIDEO with dynamicAssetSelection set to false. |  [optional] |
|**compatibility** | [**List&lt;CompatibilityEnum&gt;**](#List&lt;CompatibilityEnum&gt;) | Compatibilities associated with this creative. This is a read-only field. DISPLAY and DISPLAY_INTERSTITIAL refer to rendering either on desktop or on mobile devices or in mobile apps for regular or interstitial ads, respectively. APP and APP_INTERSTITIAL are for rendering in mobile apps. Only pre-existing creatives may have these compatibilities since new creatives will either be assigned DISPLAY or DISPLAY_INTERSTITIAL instead. IN_STREAM_VIDEO refers to rendering in in-stream video ads developed with the VAST standard. IN_STREAM_AUDIO refers to rendering in in-stream audio ads developed with the VAST standard. Applicable to all creative types. Acceptable values are: - \&quot;APP\&quot; - \&quot;APP_INTERSTITIAL\&quot; - \&quot;IN_STREAM_VIDEO\&quot; - \&quot;IN_STREAM_AUDIO\&quot; - \&quot;DISPLAY\&quot; - \&quot;DISPLAY_INTERSTITIAL\&quot;  |  [optional] |
|**convertFlashToHtml5** | **Boolean** | Whether Flash assets associated with the creative need to be automatically converted to HTML5. This flag is enabled by default and users can choose to disable it if they don&#39;t want the system to generate and use HTML5 asset for this creative. Applicable to the following creative type: FLASH_INPAGE. Applicable to DISPLAY when the primary asset type is not HTML_IMAGE. |  [optional] |
|**counterCustomEvents** | [**List&lt;CreativeCustomEvent&gt;**](CreativeCustomEvent.md) | List of counter events configured for the creative. For DISPLAY_IMAGE_GALLERY creatives, these are read-only and auto-generated from clickTags. Applicable to the following creative types: DISPLAY_IMAGE_GALLERY, all RICH_MEDIA, and all VPAID. |  [optional] |
|**creativeAssetSelection** | [**CreativeAssetSelection**](CreativeAssetSelection.md) |  |  [optional] |
|**creativeAssets** | [**List&lt;CreativeAsset&gt;**](CreativeAsset.md) | Assets associated with a creative. Applicable to all but the following creative types: INTERNAL_REDIRECT, INTERSTITIAL_INTERNAL_REDIRECT, and REDIRECT |  [optional] |
|**creativeFieldAssignments** | [**List&lt;CreativeFieldAssignment&gt;**](CreativeFieldAssignment.md) | Creative field assignments for this creative. Applicable to all creative types. |  [optional] |
|**customKeyValues** | **List&lt;String&gt;** | Custom key-values for a Rich Media creative. Key-values let you customize the creative settings of a Rich Media ad running on your site without having to contact the advertiser. You can use key-values to dynamically change the look or functionality of a creative. Applicable to the following creative types: all RICH_MEDIA, and all VPAID. |  [optional] |
|**dynamicAssetSelection** | **Boolean** | Set this to true to enable the use of rules to target individual assets in this creative. When set to true creativeAssetSelection must be set. This also controls asset-level companions. When this is true, companion creatives should be assigned to creative assets. Learn more. Applicable to INSTREAM_VIDEO creatives. |  [optional] |
|**exitCustomEvents** | [**List&lt;CreativeCustomEvent&gt;**](CreativeCustomEvent.md) | List of exit events configured for the creative. For DISPLAY and DISPLAY_IMAGE_GALLERY creatives, these are read-only and auto-generated from clickTags, For DISPLAY, an event is also created from the backupImageReportingLabel. Applicable to the following creative types: DISPLAY_IMAGE_GALLERY, all RICH_MEDIA, and all VPAID. Applicable to DISPLAY when the primary asset type is not HTML_IMAGE. |  [optional] |
|**fsCommand** | [**FsCommand**](FsCommand.md) |  |  [optional] |
|**htmlCode** | **String** | HTML code for the creative. This is a required field when applicable. This field is ignored if htmlCodeLocked is true. Applicable to the following creative types: all CUSTOM, FLASH_INPAGE, and HTML5_BANNER, and all RICH_MEDIA. |  [optional] |
|**htmlCodeLocked** | **Boolean** | Whether HTML code is generated by Campaign Manager or manually entered. Set to true to ignore changes to htmlCode. Applicable to the following creative types: FLASH_INPAGE and HTML5_BANNER. |  [optional] |
|**id** | **String** | ID of this creative. This is a read-only, auto-generated field. Applicable to all creative types. |  [optional] |
|**idDimensionValue** | [**DimensionValue**](DimensionValue.md) |  |  [optional] |
|**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;dfareporting#creative\&quot;. |  [optional] |
|**lastModifiedInfo** | [**LastModifiedInfo**](LastModifiedInfo.md) |  |  [optional] |
|**latestTraffickedCreativeId** | **String** | Latest Studio trafficked creative ID associated with rich media and VPAID creatives. This is a read-only field. Applicable to the following creative types: all RICH_MEDIA, and all VPAID. |  [optional] |
|**mediaDescription** | **String** | Description of the audio or video ad. Applicable to the following creative types: all INSTREAM_VIDEO, INSTREAM_AUDIO, and all VPAID. |  [optional] |
|**mediaDuration** | **Float** | Creative audio or video duration in seconds. This is a read-only field. Applicable to the following creative types: INSTREAM_VIDEO, INSTREAM_AUDIO, all RICH_MEDIA, and all VPAID. |  [optional] |
|**name** | **String** | Required. Name of the creative. This must be less than 256 characters long. Applicable to all creative types. |  [optional] |
|**obaIcon** | [**ObaIcon**](ObaIcon.md) |  |  [optional] |
|**overrideCss** | **String** | Override CSS value for rich media creatives. Applicable to the following creative types: all RICH_MEDIA. |  [optional] |
|**progressOffset** | [**VideoOffset**](VideoOffset.md) |  |  [optional] |
|**redirectUrl** | **String** | URL of hosted image or hosted video or another ad tag. For INSTREAM_VIDEO_REDIRECT creatives this is the in-stream video redirect URL. The standard for a VAST (Video Ad Serving Template) ad response allows for a redirect link to another VAST 2.0 or 3.0 call. This is a required field when applicable. Applicable to the following creative types: DISPLAY_REDIRECT, INTERNAL_REDIRECT, INTERSTITIAL_INTERNAL_REDIRECT, and INSTREAM_VIDEO_REDIRECT |  [optional] |
|**renderingId** | **String** | ID of current rendering version. This is a read-only field. Applicable to all creative types. |  [optional] |
|**renderingIdDimensionValue** | [**DimensionValue**](DimensionValue.md) |  |  [optional] |
|**requiredFlashPluginVersion** | **String** | The minimum required Flash plugin version for this creative. For example, 11.2.202.235. This is a read-only field. Applicable to the following creative types: all RICH_MEDIA, and all VPAID. |  [optional] |
|**requiredFlashVersion** | **Integer** | The internal Flash version for this creative as calculated by Studio. This is a read-only field. Applicable to the following creative types: FLASH_INPAGE all RICH_MEDIA, and all VPAID. Applicable to DISPLAY when the primary asset type is not HTML_IMAGE. |  [optional] |
|**size** | [**Size**](Size.md) |  |  [optional] |
|**skipOffset** | [**VideoOffset**](VideoOffset.md) |  |  [optional] |
|**skippable** | **Boolean** | Whether the user can choose to skip the creative. Applicable to the following creative types: all INSTREAM_VIDEO and all VPAID. |  [optional] |
|**sslCompliant** | **Boolean** | Whether the creative is SSL-compliant. This is a read-only field. Applicable to all creative types. |  [optional] |
|**sslOverride** | **Boolean** | Whether creative should be treated as SSL compliant even if the system scan shows it&#39;s not. Applicable to all creative types. |  [optional] |
|**studioAdvertiserId** | **String** | Studio advertiser ID associated with rich media and VPAID creatives. This is a read-only field. Applicable to the following creative types: all RICH_MEDIA, and all VPAID. |  [optional] |
|**studioCreativeId** | **String** | Studio creative ID associated with rich media and VPAID creatives. This is a read-only field. Applicable to the following creative types: all RICH_MEDIA, and all VPAID. |  [optional] |
|**studioTraffickedCreativeId** | **String** | Studio trafficked creative ID associated with rich media and VPAID creatives. This is a read-only field. Applicable to the following creative types: all RICH_MEDIA, and all VPAID. |  [optional] |
|**subaccountId** | **String** | Subaccount ID of this creative. This field, if left unset, will be auto-generated for both insert and update operations. Applicable to all creative types. |  [optional] |
|**thirdPartyBackupImageImpressionsUrl** | **String** | Third-party URL used to record backup image impressions. Applicable to the following creative types: all RICH_MEDIA. |  [optional] |
|**thirdPartyRichMediaImpressionsUrl** | **String** | Third-party URL used to record rich media impressions. Applicable to the following creative types: all RICH_MEDIA. |  [optional] |
|**thirdPartyUrls** | [**List&lt;ThirdPartyTrackingUrl&gt;**](ThirdPartyTrackingUrl.md) | Third-party URLs for tracking in-stream creative events. Applicable to the following creative types: all INSTREAM_VIDEO, all INSTREAM_AUDIO, and all VPAID. |  [optional] |
|**timerCustomEvents** | [**List&lt;CreativeCustomEvent&gt;**](CreativeCustomEvent.md) | List of timer events configured for the creative. For DISPLAY_IMAGE_GALLERY creatives, these are read-only and auto-generated from clickTags. Applicable to the following creative types: DISPLAY_IMAGE_GALLERY, all RICH_MEDIA, and all VPAID. Applicable to DISPLAY when the primary asset is not HTML_IMAGE. |  [optional] |
|**totalFileSize** | **String** | Combined size of all creative assets. This is a read-only field. Applicable to the following creative types: all RICH_MEDIA, and all VPAID. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Required. Type of this creative. Applicable to all creative types. *Note:* FLASH_INPAGE, HTML5_BANNER, and IMAGE are only used for existing creatives. New creatives should use DISPLAY as a replacement for these types. |  [optional] |
|**universalAdId** | [**UniversalAdId**](UniversalAdId.md) |  |  [optional] |
|**version** | **Integer** | The version number helps you keep track of multiple versions of your creative in your reports. The version number will always be auto-generated during insert operations to start at 1. For tracking creatives the version cannot be incremented and will always remain at 1. For all other creative types the version can be incremented only by 1 during update operations. In addition, the version will be automatically incremented by 1 when undergoing Rich Media creative merging. Applicable to all creative types. |  [optional] |



## Enum: ArtworkTypeEnum

| Name | Value |
|---- | -----|
| FLASH | &quot;ARTWORK_TYPE_FLASH&quot; |
| HTML5 | &quot;ARTWORK_TYPE_HTML5&quot; |
| MIXED | &quot;ARTWORK_TYPE_MIXED&quot; |
| IMAGE | &quot;ARTWORK_TYPE_IMAGE&quot; |



## Enum: AuthoringSourceEnum

| Name | Value |
|---- | -----|
| DCM | &quot;CREATIVE_AUTHORING_SOURCE_DCM&quot; |
| DBM | &quot;CREATIVE_AUTHORING_SOURCE_DBM&quot; |
| STUDIO | &quot;CREATIVE_AUTHORING_SOURCE_STUDIO&quot; |
| GWD | &quot;CREATIVE_AUTHORING_SOURCE_GWD&quot; |
| ACS | &quot;CREATIVE_AUTHORING_SOURCE_ACS&quot; |



## Enum: AuthoringToolEnum

| Name | Value |
|---- | -----|
| NINJA | &quot;NINJA&quot; |
| SWIFFY | &quot;SWIFFY&quot; |



## Enum: List&lt;BackupImageFeaturesEnum&gt;

| Name | Value |
|---- | -----|
| CSS_FONT_FACE | &quot;CSS_FONT_FACE&quot; |
| CSS_BACKGROUND_SIZE | &quot;CSS_BACKGROUND_SIZE&quot; |
| CSS_BORDER_IMAGE | &quot;CSS_BORDER_IMAGE&quot; |
| CSS_BORDER_RADIUS | &quot;CSS_BORDER_RADIUS&quot; |
| CSS_BOX_SHADOW | &quot;CSS_BOX_SHADOW&quot; |
| CSS_FLEX_BOX | &quot;CSS_FLEX_BOX&quot; |
| CSS_HSLA | &quot;CSS_HSLA&quot; |
| CSS_MULTIPLE_BGS | &quot;CSS_MULTIPLE_BGS&quot; |
| CSS_OPACITY | &quot;CSS_OPACITY&quot; |
| CSS_RGBA | &quot;CSS_RGBA&quot; |
| CSS_TEXT_SHADOW | &quot;CSS_TEXT_SHADOW&quot; |
| CSS_ANIMATIONS | &quot;CSS_ANIMATIONS&quot; |
| CSS_COLUMNS | &quot;CSS_COLUMNS&quot; |
| CSS_GENERATED_CONTENT | &quot;CSS_GENERATED_CONTENT&quot; |
| CSS_GRADIENTS | &quot;CSS_GRADIENTS&quot; |
| CSS_REFLECTIONS | &quot;CSS_REFLECTIONS&quot; |
| CSS_TRANSFORMS | &quot;CSS_TRANSFORMS&quot; |
| CSS_TRANSFORMS3_D | &quot;CSS_TRANSFORMS3D&quot; |
| CSS_TRANSITIONS | &quot;CSS_TRANSITIONS&quot; |
| APPLICATION_CACHE | &quot;APPLICATION_CACHE&quot; |
| CANVAS | &quot;CANVAS&quot; |
| CANVAS_TEXT | &quot;CANVAS_TEXT&quot; |
| DRAG_AND_DROP | &quot;DRAG_AND_DROP&quot; |
| HASH_CHANGE | &quot;HASH_CHANGE&quot; |
| HISTORY | &quot;HISTORY&quot; |
| AUDIO | &quot;AUDIO&quot; |
| VIDEO | &quot;VIDEO&quot; |
| INDEXED_DB | &quot;INDEXED_DB&quot; |
| INPUT_ATTR_AUTOCOMPLETE | &quot;INPUT_ATTR_AUTOCOMPLETE&quot; |
| INPUT_ATTR_AUTOFOCUS | &quot;INPUT_ATTR_AUTOFOCUS&quot; |
| INPUT_ATTR_LIST | &quot;INPUT_ATTR_LIST&quot; |
| INPUT_ATTR_PLACEHOLDER | &quot;INPUT_ATTR_PLACEHOLDER&quot; |
| INPUT_ATTR_MAX | &quot;INPUT_ATTR_MAX&quot; |
| INPUT_ATTR_MIN | &quot;INPUT_ATTR_MIN&quot; |
| INPUT_ATTR_MULTIPLE | &quot;INPUT_ATTR_MULTIPLE&quot; |
| INPUT_ATTR_PATTERN | &quot;INPUT_ATTR_PATTERN&quot; |
| INPUT_ATTR_REQUIRED | &quot;INPUT_ATTR_REQUIRED&quot; |
| INPUT_ATTR_STEP | &quot;INPUT_ATTR_STEP&quot; |
| INPUT_TYPE_SEARCH | &quot;INPUT_TYPE_SEARCH&quot; |
| INPUT_TYPE_TEL | &quot;INPUT_TYPE_TEL&quot; |
| INPUT_TYPE_URL | &quot;INPUT_TYPE_URL&quot; |
| INPUT_TYPE_EMAIL | &quot;INPUT_TYPE_EMAIL&quot; |
| INPUT_TYPE_DATETIME | &quot;INPUT_TYPE_DATETIME&quot; |
| INPUT_TYPE_DATE | &quot;INPUT_TYPE_DATE&quot; |
| INPUT_TYPE_MONTH | &quot;INPUT_TYPE_MONTH&quot; |
| INPUT_TYPE_WEEK | &quot;INPUT_TYPE_WEEK&quot; |
| INPUT_TYPE_TIME | &quot;INPUT_TYPE_TIME&quot; |
| INPUT_TYPE_DATETIME_LOCAL | &quot;INPUT_TYPE_DATETIME_LOCAL&quot; |
| INPUT_TYPE_NUMBER | &quot;INPUT_TYPE_NUMBER&quot; |
| INPUT_TYPE_RANGE | &quot;INPUT_TYPE_RANGE&quot; |
| INPUT_TYPE_COLOR | &quot;INPUT_TYPE_COLOR&quot; |
| LOCAL_STORAGE | &quot;LOCAL_STORAGE&quot; |
| POST_MESSAGE | &quot;POST_MESSAGE&quot; |
| SESSION_STORAGE | &quot;SESSION_STORAGE&quot; |
| WEB_SOCKETS | &quot;WEB_SOCKETS&quot; |
| WEB_SQL_DATABASE | &quot;WEB_SQL_DATABASE&quot; |
| WEB_WORKERS | &quot;WEB_WORKERS&quot; |
| GEO_LOCATION | &quot;GEO_LOCATION&quot; |
| INLINE_SVG | &quot;INLINE_SVG&quot; |
| SMIL | &quot;SMIL&quot; |
| SVG_HREF | &quot;SVG_HREF&quot; |
| SVG_CLIP_PATHS | &quot;SVG_CLIP_PATHS&quot; |
| TOUCH | &quot;TOUCH&quot; |
| WEBGL | &quot;WEBGL&quot; |
| SVG_FILTERS | &quot;SVG_FILTERS&quot; |
| SVG_FE_IMAGE | &quot;SVG_FE_IMAGE&quot; |



## Enum: List&lt;CompatibilityEnum&gt;

| Name | Value |
|---- | -----|
| DISPLAY | &quot;DISPLAY&quot; |
| DISPLAY_INTERSTITIAL | &quot;DISPLAY_INTERSTITIAL&quot; |
| APP | &quot;APP&quot; |
| APP_INTERSTITIAL | &quot;APP_INTERSTITIAL&quot; |
| IN_STREAM_VIDEO | &quot;IN_STREAM_VIDEO&quot; |
| IN_STREAM_AUDIO | &quot;IN_STREAM_AUDIO&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| IMAGE | &quot;IMAGE&quot; |
| DISPLAY_REDIRECT | &quot;DISPLAY_REDIRECT&quot; |
| CUSTOM_DISPLAY | &quot;CUSTOM_DISPLAY&quot; |
| INTERNAL_REDIRECT | &quot;INTERNAL_REDIRECT&quot; |
| CUSTOM_DISPLAY_INTERSTITIAL | &quot;CUSTOM_DISPLAY_INTERSTITIAL&quot; |
| INTERSTITIAL_INTERNAL_REDIRECT | &quot;INTERSTITIAL_INTERNAL_REDIRECT&quot; |
| TRACKING_TEXT | &quot;TRACKING_TEXT&quot; |
| RICH_MEDIA_DISPLAY_BANNER | &quot;RICH_MEDIA_DISPLAY_BANNER&quot; |
| RICH_MEDIA_INPAGE_FLOATING | &quot;RICH_MEDIA_INPAGE_FLOATING&quot; |
| RICH_MEDIA_IM_EXPAND | &quot;RICH_MEDIA_IM_EXPAND&quot; |
| RICH_MEDIA_DISPLAY_EXPANDING | &quot;RICH_MEDIA_DISPLAY_EXPANDING&quot; |
| RICH_MEDIA_DISPLAY_INTERSTITIAL | &quot;RICH_MEDIA_DISPLAY_INTERSTITIAL&quot; |
| RICH_MEDIA_DISPLAY_MULTI_FLOATING_INTERSTITIAL | &quot;RICH_MEDIA_DISPLAY_MULTI_FLOATING_INTERSTITIAL&quot; |
| RICH_MEDIA_MOBILE_IN_APP | &quot;RICH_MEDIA_MOBILE_IN_APP&quot; |
| FLASH_INPAGE | &quot;FLASH_INPAGE&quot; |
| INSTREAM_VIDEO | &quot;INSTREAM_VIDEO&quot; |
| VPAID_LINEAR_VIDEO | &quot;VPAID_LINEAR_VIDEO&quot; |
| VPAID_NON_LINEAR_VIDEO | &quot;VPAID_NON_LINEAR_VIDEO&quot; |
| INSTREAM_VIDEO_REDIRECT | &quot;INSTREAM_VIDEO_REDIRECT&quot; |
| RICH_MEDIA_PEEL_DOWN | &quot;RICH_MEDIA_PEEL_DOWN&quot; |
| HTML5_BANNER | &quot;HTML5_BANNER&quot; |
| DISPLAY | &quot;DISPLAY&quot; |
| DISPLAY_IMAGE_GALLERY | &quot;DISPLAY_IMAGE_GALLERY&quot; |
| BRAND_SAFE_DEFAULT_INSTREAM_VIDEO | &quot;BRAND_SAFE_DEFAULT_INSTREAM_VIDEO&quot; |
| INSTREAM_AUDIO | &quot;INSTREAM_AUDIO&quot; |



