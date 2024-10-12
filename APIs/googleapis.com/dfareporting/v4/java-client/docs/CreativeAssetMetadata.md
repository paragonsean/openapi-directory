

# CreativeAssetMetadata

CreativeAssets contains properties of a creative asset file which will be uploaded or has already been uploaded. Refer to the creative sample code for how to upload assets and insert a creative.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**assetIdentifier** | [**CreativeAssetId**](CreativeAssetId.md) |  |  [optional] |
|**clickTags** | [**List&lt;ClickTag&gt;**](ClickTag.md) | List of detected click tags for assets. This is a read-only, auto-generated field. This field is empty for a rich media asset. |  [optional] |
|**counterCustomEvents** | [**List&lt;CreativeCustomEvent&gt;**](CreativeCustomEvent.md) | List of counter events configured for the asset. This is a read-only, auto-generated field and only applicable to a rich media asset. |  [optional] |
|**detectedFeatures** | [**List&lt;DetectedFeaturesEnum&gt;**](#List&lt;DetectedFeaturesEnum&gt;) | List of feature dependencies for the creative asset that are detected by Campaign Manager. Feature dependencies are features that a browser must be able to support in order to render your HTML5 creative correctly. This is a read-only, auto-generated field. |  [optional] |
|**exitCustomEvents** | [**List&lt;CreativeCustomEvent&gt;**](CreativeCustomEvent.md) | List of exit events configured for the asset. This is a read-only, auto-generated field and only applicable to a rich media asset. |  [optional] |
|**id** | **String** | Numeric ID of the asset. This is a read-only, auto-generated field. |  [optional] |
|**idDimensionValue** | [**DimensionValue**](DimensionValue.md) |  |  [optional] |
|**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;dfareporting#creativeAssetMetadata\&quot;. |  [optional] |
|**richMedia** | **Boolean** | True if the uploaded asset is a rich media asset. This is a read-only, auto-generated field. |  [optional] |
|**timerCustomEvents** | [**List&lt;CreativeCustomEvent&gt;**](CreativeCustomEvent.md) | List of timer events configured for the asset. This is a read-only, auto-generated field and only applicable to a rich media asset. |  [optional] |
|**warnedValidationRules** | [**List&lt;WarnedValidationRulesEnum&gt;**](#List&lt;WarnedValidationRulesEnum&gt;) | Rules validated during code generation that generated a warning. This is a read-only, auto-generated field. Possible values are: - \&quot;ADMOB_REFERENCED\&quot; - \&quot;ASSET_FORMAT_UNSUPPORTED_DCM\&quot; - \&quot;ASSET_INVALID\&quot; - \&quot;CLICK_TAG_HARD_CODED\&quot; - \&quot;CLICK_TAG_INVALID\&quot; - \&quot;CLICK_TAG_IN_GWD\&quot; - \&quot;CLICK_TAG_MISSING\&quot; - \&quot;CLICK_TAG_MORE_THAN_ONE\&quot; - \&quot;CLICK_TAG_NON_TOP_LEVEL\&quot; - \&quot;COMPONENT_UNSUPPORTED_DCM\&quot; - \&quot;ENABLER_UNSUPPORTED_METHOD_DCM\&quot; - \&quot;EXTERNAL_FILE_REFERENCED\&quot; - \&quot;FILE_DETAIL_EMPTY\&quot; - \&quot;FILE_TYPE_INVALID\&quot; - \&quot;GWD_PROPERTIES_INVALID\&quot; - \&quot;HTML5_FEATURE_UNSUPPORTED\&quot; - \&quot;LINKED_FILE_NOT_FOUND\&quot; - \&quot;MAX_FLASH_VERSION_11\&quot; - \&quot;MRAID_REFERENCED\&quot; - \&quot;NOT_SSL_COMPLIANT\&quot; - \&quot;ORPHANED_ASSET\&quot; - \&quot;PRIMARY_HTML_MISSING\&quot; - \&quot;SVG_INVALID\&quot; - \&quot;ZIP_INVALID\&quot;  |  [optional] |



## Enum: List&lt;DetectedFeaturesEnum&gt;

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



## Enum: List&lt;WarnedValidationRulesEnum&gt;

| Name | Value |
|---- | -----|
| CLICK_TAG_NON_TOP_LEVEL | &quot;CLICK_TAG_NON_TOP_LEVEL&quot; |
| CLICK_TAG_MISSING | &quot;CLICK_TAG_MISSING&quot; |
| CLICK_TAG_MORE_THAN_ONE | &quot;CLICK_TAG_MORE_THAN_ONE&quot; |
| CLICK_TAG_INVALID | &quot;CLICK_TAG_INVALID&quot; |
| ORPHANED_ASSET | &quot;ORPHANED_ASSET&quot; |
| PRIMARY_HTML_MISSING | &quot;PRIMARY_HTML_MISSING&quot; |
| EXTERNAL_FILE_REFERENCED | &quot;EXTERNAL_FILE_REFERENCED&quot; |
| MRAID_REFERENCED | &quot;MRAID_REFERENCED&quot; |
| ADMOB_REFERENCED | &quot;ADMOB_REFERENCED&quot; |
| FILE_TYPE_INVALID | &quot;FILE_TYPE_INVALID&quot; |
| ZIP_INVALID | &quot;ZIP_INVALID&quot; |
| LINKED_FILE_NOT_FOUND | &quot;LINKED_FILE_NOT_FOUND&quot; |
| MAX_FLASH_VERSION_11 | &quot;MAX_FLASH_VERSION_11&quot; |
| NOT_SSL_COMPLIANT | &quot;NOT_SSL_COMPLIANT&quot; |
| FILE_DETAIL_EMPTY | &quot;FILE_DETAIL_EMPTY&quot; |
| ASSET_INVALID | &quot;ASSET_INVALID&quot; |
| GWD_PROPERTIES_INVALID | &quot;GWD_PROPERTIES_INVALID&quot; |
| ENABLER_UNSUPPORTED_METHOD_DCM | &quot;ENABLER_UNSUPPORTED_METHOD_DCM&quot; |
| ASSET_FORMAT_UNSUPPORTED_DCM | &quot;ASSET_FORMAT_UNSUPPORTED_DCM&quot; |
| COMPONENT_UNSUPPORTED_DCM | &quot;COMPONENT_UNSUPPORTED_DCM&quot; |
| HTML5_FEATURE_UNSUPPORTED | &quot;HTML5_FEATURE_UNSUPPORTED&quot; |
| CLICK_TAG_IN_GWD | &quot;CLICK_TAG_IN_GWD&quot; |
| CLICK_TAG_HARD_CODED | &quot;CLICK_TAG_HARD_CODED&quot; |
| SVG_INVALID | &quot;SVG_INVALID&quot; |
| CLICK_TAG_IN_RICH_MEDIA | &quot;CLICK_TAG_IN_RICH_MEDIA&quot; |
| MISSING_ENABLER_REFERENCE | &quot;MISSING_ENABLER_REFERENCE&quot; |



