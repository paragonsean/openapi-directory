# CampaignManager360Api.Creative

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** | Account ID of this creative. This field, if left unset, will be auto-generated for both insert and update operations. Applicable to all creative types. | [optional] 
**active** | **Boolean** | Whether the creative is active. Applicable to all creative types. | [optional] 
**adParameters** | **String** | Ad parameters user for VPAID creative. This is a read-only field. Applicable to the following creative types: all VPAID. | [optional] 
**adTagKeys** | **[String]** | Keywords for a Rich Media creative. Keywords let you customize the creative settings of a Rich Media ad running on your site without having to contact the advertiser. You can use keywords to dynamically change the look or functionality of a creative. Applicable to the following creative types: all RICH_MEDIA, and all VPAID. | [optional] 
**additionalSizes** | [**[Size]**](Size.md) | Additional sizes associated with a responsive creative. When inserting or updating a creative either the size ID field or size width and height fields can be used. Applicable to DISPLAY creatives when the primary asset type is HTML_IMAGE. | [optional] 
**advertiserId** | **String** | Advertiser ID of this creative. This is a required field. Applicable to all creative types. | [optional] 
**allowScriptAccess** | **Boolean** | Whether script access is allowed for this creative. This is a read-only and deprecated field which will automatically be set to true on update. Applicable to the following creative types: FLASH_INPAGE. | [optional] 
**archived** | **Boolean** | Whether the creative is archived. Applicable to all creative types. | [optional] 
**artworkType** | **String** | Type of artwork used for the creative. This is a read-only field. Applicable to the following creative types: all RICH_MEDIA, and all VPAID. | [optional] 
**authoringSource** | **String** | Source application where creative was authored. Presently, only DBM authored creatives will have this field set. Applicable to all creative types. | [optional] 
**authoringTool** | **String** | Authoring tool for HTML5 banner creatives. This is a read-only field. Applicable to the following creative types: HTML5_BANNER. | [optional] 
**autoAdvanceImages** | **Boolean** | Whether images are automatically advanced for image gallery creatives. Applicable to the following creative types: DISPLAY_IMAGE_GALLERY. | [optional] 
**backgroundColor** | **String** | The 6-character HTML color code, beginning with #, for the background of the window area where the Flash file is displayed. Default is white. Applicable to the following creative types: FLASH_INPAGE. | [optional] 
**backupImageClickThroughUrl** | [**CreativeClickThroughUrl**](CreativeClickThroughUrl.md) |  | [optional] 
**backupImageFeatures** | **[String]** | List of feature dependencies that will cause a backup image to be served if the browser that serves the ad does not support them. Feature dependencies are features that a browser must be able to support in order to render your HTML5 creative asset correctly. This field is initially auto-generated to contain all features detected by Campaign Manager for all the assets of this creative and can then be modified by the client. To reset this field, copy over all the creativeAssets&#39; detected features. Applicable to the following creative types: HTML5_BANNER. Applicable to DISPLAY when the primary asset type is not HTML_IMAGE. | [optional] 
**backupImageReportingLabel** | **String** | Reporting label used for HTML5 banner backup image. Applicable to the following creative types: DISPLAY when the primary asset type is not HTML_IMAGE. | [optional] 
**backupImageTargetWindow** | [**TargetWindow**](TargetWindow.md) |  | [optional] 
**clickTags** | [**[ClickTag]**](ClickTag.md) | Click tags of the creative. For DISPLAY, FLASH_INPAGE, and HTML5_BANNER creatives, this is a subset of detected click tags for the assets associated with this creative. After creating a flash asset, detected click tags will be returned in the creativeAssetMetadata. When inserting the creative, populate the creative clickTags field using the creativeAssetMetadata.clickTags field. For DISPLAY_IMAGE_GALLERY creatives, there should be exactly one entry in this list for each image creative asset. A click tag is matched with a corresponding creative asset by matching the clickTag.name field with the creativeAsset.assetIdentifier.name field. Applicable to the following creative types: DISPLAY_IMAGE_GALLERY, FLASH_INPAGE, HTML5_BANNER. Applicable to DISPLAY when the primary asset type is not HTML_IMAGE. | [optional] 
**commercialId** | **String** | Industry standard ID assigned to creative for reach and frequency. Applicable to INSTREAM_VIDEO_REDIRECT creatives. | [optional] 
**companionCreatives** | **[String]** | List of companion creatives assigned to an in-Stream video creative. Acceptable values include IDs of existing flash and image creatives. Applicable to the following creative types: all VPAID, all INSTREAM_AUDIO and all INSTREAM_VIDEO with dynamicAssetSelection set to false. | [optional] 
**compatibility** | **[String]** | Compatibilities associated with this creative. This is a read-only field. DISPLAY and DISPLAY_INTERSTITIAL refer to rendering either on desktop or on mobile devices or in mobile apps for regular or interstitial ads, respectively. APP and APP_INTERSTITIAL are for rendering in mobile apps. Only pre-existing creatives may have these compatibilities since new creatives will either be assigned DISPLAY or DISPLAY_INTERSTITIAL instead. IN_STREAM_VIDEO refers to rendering in in-stream video ads developed with the VAST standard. IN_STREAM_AUDIO refers to rendering in in-stream audio ads developed with the VAST standard. Applicable to all creative types. Acceptable values are: - \&quot;APP\&quot; - \&quot;APP_INTERSTITIAL\&quot; - \&quot;IN_STREAM_VIDEO\&quot; - \&quot;IN_STREAM_AUDIO\&quot; - \&quot;DISPLAY\&quot; - \&quot;DISPLAY_INTERSTITIAL\&quot;  | [optional] 
**convertFlashToHtml5** | **Boolean** | Whether Flash assets associated with the creative need to be automatically converted to HTML5. This flag is enabled by default and users can choose to disable it if they don&#39;t want the system to generate and use HTML5 asset for this creative. Applicable to the following creative type: FLASH_INPAGE. Applicable to DISPLAY when the primary asset type is not HTML_IMAGE. | [optional] 
**counterCustomEvents** | [**[CreativeCustomEvent]**](CreativeCustomEvent.md) | List of counter events configured for the creative. For DISPLAY_IMAGE_GALLERY creatives, these are read-only and auto-generated from clickTags. Applicable to the following creative types: DISPLAY_IMAGE_GALLERY, all RICH_MEDIA, and all VPAID. | [optional] 
**creativeAssetSelection** | [**CreativeAssetSelection**](CreativeAssetSelection.md) |  | [optional] 
**creativeAssets** | [**[CreativeAsset]**](CreativeAsset.md) | Assets associated with a creative. Applicable to all but the following creative types: INTERNAL_REDIRECT, INTERSTITIAL_INTERNAL_REDIRECT, and REDIRECT | [optional] 
**creativeFieldAssignments** | [**[CreativeFieldAssignment]**](CreativeFieldAssignment.md) | Creative field assignments for this creative. Applicable to all creative types. | [optional] 
**customKeyValues** | **[String]** | Custom key-values for a Rich Media creative. Key-values let you customize the creative settings of a Rich Media ad running on your site without having to contact the advertiser. You can use key-values to dynamically change the look or functionality of a creative. Applicable to the following creative types: all RICH_MEDIA, and all VPAID. | [optional] 
**dynamicAssetSelection** | **Boolean** | Set this to true to enable the use of rules to target individual assets in this creative. When set to true creativeAssetSelection must be set. This also controls asset-level companions. When this is true, companion creatives should be assigned to creative assets. Learn more. Applicable to INSTREAM_VIDEO creatives. | [optional] 
**exitCustomEvents** | [**[CreativeCustomEvent]**](CreativeCustomEvent.md) | List of exit events configured for the creative. For DISPLAY and DISPLAY_IMAGE_GALLERY creatives, these are read-only and auto-generated from clickTags, For DISPLAY, an event is also created from the backupImageReportingLabel. Applicable to the following creative types: DISPLAY_IMAGE_GALLERY, all RICH_MEDIA, and all VPAID. Applicable to DISPLAY when the primary asset type is not HTML_IMAGE. | [optional] 
**fsCommand** | [**FsCommand**](FsCommand.md) |  | [optional] 
**htmlCode** | **String** | HTML code for the creative. This is a required field when applicable. This field is ignored if htmlCodeLocked is true. Applicable to the following creative types: all CUSTOM, FLASH_INPAGE, and HTML5_BANNER, and all RICH_MEDIA. | [optional] 
**htmlCodeLocked** | **Boolean** | Whether HTML code is generated by Campaign Manager or manually entered. Set to true to ignore changes to htmlCode. Applicable to the following creative types: FLASH_INPAGE and HTML5_BANNER. | [optional] 
**id** | **String** | ID of this creative. This is a read-only, auto-generated field. Applicable to all creative types. | [optional] 
**idDimensionValue** | [**DimensionValue**](DimensionValue.md) |  | [optional] 
**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;dfareporting#creative\&quot;. | [optional] 
**lastModifiedInfo** | [**LastModifiedInfo**](LastModifiedInfo.md) |  | [optional] 
**latestTraffickedCreativeId** | **String** | Latest Studio trafficked creative ID associated with rich media and VPAID creatives. This is a read-only field. Applicable to the following creative types: all RICH_MEDIA, and all VPAID. | [optional] 
**mediaDescription** | **String** | Description of the audio or video ad. Applicable to the following creative types: all INSTREAM_VIDEO, INSTREAM_AUDIO, and all VPAID. | [optional] 
**mediaDuration** | **Number** | Creative audio or video duration in seconds. This is a read-only field. Applicable to the following creative types: INSTREAM_VIDEO, INSTREAM_AUDIO, all RICH_MEDIA, and all VPAID. | [optional] 
**name** | **String** | Name of the creative. This is a required field and must be less than 256 characters long. Applicable to all creative types. | [optional] 
**overrideCss** | **String** | Override CSS value for rich media creatives. Applicable to the following creative types: all RICH_MEDIA. | [optional] 
**progressOffset** | [**VideoOffset**](VideoOffset.md) |  | [optional] 
**redirectUrl** | **String** | URL of hosted image or hosted video or another ad tag. For INSTREAM_VIDEO_REDIRECT creatives this is the in-stream video redirect URL. The standard for a VAST (Video Ad Serving Template) ad response allows for a redirect link to another VAST 2.0 or 3.0 call. This is a required field when applicable. Applicable to the following creative types: DISPLAY_REDIRECT, INTERNAL_REDIRECT, INTERSTITIAL_INTERNAL_REDIRECT, and INSTREAM_VIDEO_REDIRECT | [optional] 
**renderingId** | **String** | ID of current rendering version. This is a read-only field. Applicable to all creative types. | [optional] 
**renderingIdDimensionValue** | [**DimensionValue**](DimensionValue.md) |  | [optional] 
**requiredFlashPluginVersion** | **String** | The minimum required Flash plugin version for this creative. For example, 11.2.202.235. This is a read-only field. Applicable to the following creative types: all RICH_MEDIA, and all VPAID. | [optional] 
**requiredFlashVersion** | **Number** | The internal Flash version for this creative as calculated by Studio. This is a read-only field. Applicable to the following creative types: FLASH_INPAGE all RICH_MEDIA, and all VPAID. Applicable to DISPLAY when the primary asset type is not HTML_IMAGE. | [optional] 
**size** | [**Size**](Size.md) |  | [optional] 
**skipOffset** | [**VideoOffset**](VideoOffset.md) |  | [optional] 
**skippable** | **Boolean** | Whether the user can choose to skip the creative. Applicable to the following creative types: all INSTREAM_VIDEO and all VPAID. | [optional] 
**sslCompliant** | **Boolean** | Whether the creative is SSL-compliant. This is a read-only field. Applicable to all creative types. | [optional] 
**sslOverride** | **Boolean** | Whether creative should be treated as SSL compliant even if the system scan shows it&#39;s not. Applicable to all creative types. | [optional] 
**studioAdvertiserId** | **String** | Studio advertiser ID associated with rich media and VPAID creatives. This is a read-only field. Applicable to the following creative types: all RICH_MEDIA, and all VPAID. | [optional] 
**studioCreativeId** | **String** | Studio creative ID associated with rich media and VPAID creatives. This is a read-only field. Applicable to the following creative types: all RICH_MEDIA, and all VPAID. | [optional] 
**studioTraffickedCreativeId** | **String** | Studio trafficked creative ID associated with rich media and VPAID creatives. This is a read-only field. Applicable to the following creative types: all RICH_MEDIA, and all VPAID. | [optional] 
**subaccountId** | **String** | Subaccount ID of this creative. This field, if left unset, will be auto-generated for both insert and update operations. Applicable to all creative types. | [optional] 
**thirdPartyBackupImageImpressionsUrl** | **String** | Third-party URL used to record backup image impressions. Applicable to the following creative types: all RICH_MEDIA. | [optional] 
**thirdPartyRichMediaImpressionsUrl** | **String** | Third-party URL used to record rich media impressions. Applicable to the following creative types: all RICH_MEDIA. | [optional] 
**thirdPartyUrls** | [**[ThirdPartyTrackingUrl]**](ThirdPartyTrackingUrl.md) | Third-party URLs for tracking in-stream creative events. Applicable to the following creative types: all INSTREAM_VIDEO, all INSTREAM_AUDIO, and all VPAID. | [optional] 
**timerCustomEvents** | [**[CreativeCustomEvent]**](CreativeCustomEvent.md) | List of timer events configured for the creative. For DISPLAY_IMAGE_GALLERY creatives, these are read-only and auto-generated from clickTags. Applicable to the following creative types: DISPLAY_IMAGE_GALLERY, all RICH_MEDIA, and all VPAID. Applicable to DISPLAY when the primary asset is not HTML_IMAGE. | [optional] 
**totalFileSize** | **String** | Combined size of all creative assets. This is a read-only field. Applicable to the following creative types: all RICH_MEDIA, and all VPAID. | [optional] 
**type** | **String** | Type of this creative. This is a required field. Applicable to all creative types. *Note:* FLASH_INPAGE, HTML5_BANNER, and IMAGE are only used for existing creatives. New creatives should use DISPLAY as a replacement for these types. | [optional] 
**universalAdId** | [**UniversalAdId**](UniversalAdId.md) |  | [optional] 
**version** | **Number** | The version number helps you keep track of multiple versions of your creative in your reports. The version number will always be auto-generated during insert operations to start at 1. For tracking creatives the version cannot be incremented and will always remain at 1. For all other creative types the version can be incremented only by 1 during update operations. In addition, the version will be automatically incremented by 1 when undergoing Rich Media creative merging. Applicable to all creative types. | [optional] 



## Enum: ArtworkTypeEnum


* `FLASH` (value: `"ARTWORK_TYPE_FLASH"`)

* `HTML5` (value: `"ARTWORK_TYPE_HTML5"`)

* `MIXED` (value: `"ARTWORK_TYPE_MIXED"`)

* `IMAGE` (value: `"ARTWORK_TYPE_IMAGE"`)





## Enum: AuthoringSourceEnum


* `DCM` (value: `"CREATIVE_AUTHORING_SOURCE_DCM"`)

* `DBM` (value: `"CREATIVE_AUTHORING_SOURCE_DBM"`)

* `STUDIO` (value: `"CREATIVE_AUTHORING_SOURCE_STUDIO"`)

* `GWD` (value: `"CREATIVE_AUTHORING_SOURCE_GWD"`)





## Enum: AuthoringToolEnum


* `NINJA` (value: `"NINJA"`)

* `SWIFFY` (value: `"SWIFFY"`)





## Enum: [BackupImageFeaturesEnum]


* `CSS_FONT_FACE` (value: `"CSS_FONT_FACE"`)

* `CSS_BACKGROUND_SIZE` (value: `"CSS_BACKGROUND_SIZE"`)

* `CSS_BORDER_IMAGE` (value: `"CSS_BORDER_IMAGE"`)

* `CSS_BORDER_RADIUS` (value: `"CSS_BORDER_RADIUS"`)

* `CSS_BOX_SHADOW` (value: `"CSS_BOX_SHADOW"`)

* `CSS_FLEX_BOX` (value: `"CSS_FLEX_BOX"`)

* `CSS_HSLA` (value: `"CSS_HSLA"`)

* `CSS_MULTIPLE_BGS` (value: `"CSS_MULTIPLE_BGS"`)

* `CSS_OPACITY` (value: `"CSS_OPACITY"`)

* `CSS_RGBA` (value: `"CSS_RGBA"`)

* `CSS_TEXT_SHADOW` (value: `"CSS_TEXT_SHADOW"`)

* `CSS_ANIMATIONS` (value: `"CSS_ANIMATIONS"`)

* `CSS_COLUMNS` (value: `"CSS_COLUMNS"`)

* `CSS_GENERATED_CONTENT` (value: `"CSS_GENERATED_CONTENT"`)

* `CSS_GRADIENTS` (value: `"CSS_GRADIENTS"`)

* `CSS_REFLECTIONS` (value: `"CSS_REFLECTIONS"`)

* `CSS_TRANSFORMS` (value: `"CSS_TRANSFORMS"`)

* `CSS_TRANSFORMS3D` (value: `"CSS_TRANSFORMS3D"`)

* `CSS_TRANSITIONS` (value: `"CSS_TRANSITIONS"`)

* `APPLICATION_CACHE` (value: `"APPLICATION_CACHE"`)

* `CANVAS` (value: `"CANVAS"`)

* `CANVAS_TEXT` (value: `"CANVAS_TEXT"`)

* `DRAG_AND_DROP` (value: `"DRAG_AND_DROP"`)

* `HASH_CHANGE` (value: `"HASH_CHANGE"`)

* `HISTORY` (value: `"HISTORY"`)

* `AUDIO` (value: `"AUDIO"`)

* `VIDEO` (value: `"VIDEO"`)

* `INDEXED_DB` (value: `"INDEXED_DB"`)

* `INPUT_ATTR_AUTOCOMPLETE` (value: `"INPUT_ATTR_AUTOCOMPLETE"`)

* `INPUT_ATTR_AUTOFOCUS` (value: `"INPUT_ATTR_AUTOFOCUS"`)

* `INPUT_ATTR_LIST` (value: `"INPUT_ATTR_LIST"`)

* `INPUT_ATTR_PLACEHOLDER` (value: `"INPUT_ATTR_PLACEHOLDER"`)

* `INPUT_ATTR_MAX` (value: `"INPUT_ATTR_MAX"`)

* `INPUT_ATTR_MIN` (value: `"INPUT_ATTR_MIN"`)

* `INPUT_ATTR_MULTIPLE` (value: `"INPUT_ATTR_MULTIPLE"`)

* `INPUT_ATTR_PATTERN` (value: `"INPUT_ATTR_PATTERN"`)

* `INPUT_ATTR_REQUIRED` (value: `"INPUT_ATTR_REQUIRED"`)

* `INPUT_ATTR_STEP` (value: `"INPUT_ATTR_STEP"`)

* `INPUT_TYPE_SEARCH` (value: `"INPUT_TYPE_SEARCH"`)

* `INPUT_TYPE_TEL` (value: `"INPUT_TYPE_TEL"`)

* `INPUT_TYPE_URL` (value: `"INPUT_TYPE_URL"`)

* `INPUT_TYPE_EMAIL` (value: `"INPUT_TYPE_EMAIL"`)

* `INPUT_TYPE_DATETIME` (value: `"INPUT_TYPE_DATETIME"`)

* `INPUT_TYPE_DATE` (value: `"INPUT_TYPE_DATE"`)

* `INPUT_TYPE_MONTH` (value: `"INPUT_TYPE_MONTH"`)

* `INPUT_TYPE_WEEK` (value: `"INPUT_TYPE_WEEK"`)

* `INPUT_TYPE_TIME` (value: `"INPUT_TYPE_TIME"`)

* `INPUT_TYPE_DATETIME_LOCAL` (value: `"INPUT_TYPE_DATETIME_LOCAL"`)

* `INPUT_TYPE_NUMBER` (value: `"INPUT_TYPE_NUMBER"`)

* `INPUT_TYPE_RANGE` (value: `"INPUT_TYPE_RANGE"`)

* `INPUT_TYPE_COLOR` (value: `"INPUT_TYPE_COLOR"`)

* `LOCAL_STORAGE` (value: `"LOCAL_STORAGE"`)

* `POST_MESSAGE` (value: `"POST_MESSAGE"`)

* `SESSION_STORAGE` (value: `"SESSION_STORAGE"`)

* `WEB_SOCKETS` (value: `"WEB_SOCKETS"`)

* `WEB_SQL_DATABASE` (value: `"WEB_SQL_DATABASE"`)

* `WEB_WORKERS` (value: `"WEB_WORKERS"`)

* `GEO_LOCATION` (value: `"GEO_LOCATION"`)

* `INLINE_SVG` (value: `"INLINE_SVG"`)

* `SMIL` (value: `"SMIL"`)

* `SVG_HREF` (value: `"SVG_HREF"`)

* `SVG_CLIP_PATHS` (value: `"SVG_CLIP_PATHS"`)

* `TOUCH` (value: `"TOUCH"`)

* `WEBGL` (value: `"WEBGL"`)

* `SVG_FILTERS` (value: `"SVG_FILTERS"`)

* `SVG_FE_IMAGE` (value: `"SVG_FE_IMAGE"`)





## Enum: [CompatibilityEnum]


* `DISPLAY` (value: `"DISPLAY"`)

* `DISPLAY_INTERSTITIAL` (value: `"DISPLAY_INTERSTITIAL"`)

* `APP` (value: `"APP"`)

* `APP_INTERSTITIAL` (value: `"APP_INTERSTITIAL"`)

* `IN_STREAM_VIDEO` (value: `"IN_STREAM_VIDEO"`)

* `IN_STREAM_AUDIO` (value: `"IN_STREAM_AUDIO"`)





## Enum: TypeEnum


* `IMAGE` (value: `"IMAGE"`)

* `DISPLAY_REDIRECT` (value: `"DISPLAY_REDIRECT"`)

* `CUSTOM_DISPLAY` (value: `"CUSTOM_DISPLAY"`)

* `INTERNAL_REDIRECT` (value: `"INTERNAL_REDIRECT"`)

* `CUSTOM_DISPLAY_INTERSTITIAL` (value: `"CUSTOM_DISPLAY_INTERSTITIAL"`)

* `INTERSTITIAL_INTERNAL_REDIRECT` (value: `"INTERSTITIAL_INTERNAL_REDIRECT"`)

* `TRACKING_TEXT` (value: `"TRACKING_TEXT"`)

* `RICH_MEDIA_DISPLAY_BANNER` (value: `"RICH_MEDIA_DISPLAY_BANNER"`)

* `RICH_MEDIA_INPAGE_FLOATING` (value: `"RICH_MEDIA_INPAGE_FLOATING"`)

* `RICH_MEDIA_IM_EXPAND` (value: `"RICH_MEDIA_IM_EXPAND"`)

* `RICH_MEDIA_DISPLAY_EXPANDING` (value: `"RICH_MEDIA_DISPLAY_EXPANDING"`)

* `RICH_MEDIA_DISPLAY_INTERSTITIAL` (value: `"RICH_MEDIA_DISPLAY_INTERSTITIAL"`)

* `RICH_MEDIA_DISPLAY_MULTI_FLOATING_INTERSTITIAL` (value: `"RICH_MEDIA_DISPLAY_MULTI_FLOATING_INTERSTITIAL"`)

* `RICH_MEDIA_MOBILE_IN_APP` (value: `"RICH_MEDIA_MOBILE_IN_APP"`)

* `FLASH_INPAGE` (value: `"FLASH_INPAGE"`)

* `INSTREAM_VIDEO` (value: `"INSTREAM_VIDEO"`)

* `VPAID_LINEAR_VIDEO` (value: `"VPAID_LINEAR_VIDEO"`)

* `VPAID_NON_LINEAR_VIDEO` (value: `"VPAID_NON_LINEAR_VIDEO"`)

* `INSTREAM_VIDEO_REDIRECT` (value: `"INSTREAM_VIDEO_REDIRECT"`)

* `RICH_MEDIA_PEEL_DOWN` (value: `"RICH_MEDIA_PEEL_DOWN"`)

* `HTML5_BANNER` (value: `"HTML5_BANNER"`)

* `DISPLAY` (value: `"DISPLAY"`)

* `DISPLAY_IMAGE_GALLERY` (value: `"DISPLAY_IMAGE_GALLERY"`)

* `BRAND_SAFE_DEFAULT_INSTREAM_VIDEO` (value: `"BRAND_SAFE_DEFAULT_INSTREAM_VIDEO"`)

* `INSTREAM_AUDIO` (value: `"INSTREAM_AUDIO"`)




