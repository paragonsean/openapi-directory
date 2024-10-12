# CampaignManager360Api.CreativeAssetMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assetIdentifier** | [**CreativeAssetId**](CreativeAssetId.md) |  | [optional] 
**clickTags** | [**[ClickTag]**](ClickTag.md) | List of detected click tags for assets. This is a read-only, auto-generated field. This field is empty for a rich media asset. | [optional] 
**detectedFeatures** | **[String]** | List of feature dependencies for the creative asset that are detected by Campaign Manager. Feature dependencies are features that a browser must be able to support in order to render your HTML5 creative correctly. This is a read-only, auto-generated field. | [optional] 
**id** | **String** | Numeric ID of the asset. This is a read-only, auto-generated field. | [optional] 
**idDimensionValue** | [**DimensionValue**](DimensionValue.md) |  | [optional] 
**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;dfareporting#creativeAssetMetadata\&quot;. | [optional] 
**warnedValidationRules** | **[String]** | Rules validated during code generation that generated a warning. This is a read-only, auto-generated field. Possible values are: - \&quot;ADMOB_REFERENCED\&quot; - \&quot;ASSET_FORMAT_UNSUPPORTED_DCM\&quot; - \&quot;ASSET_INVALID\&quot; - \&quot;CLICK_TAG_HARD_CODED\&quot; - \&quot;CLICK_TAG_INVALID\&quot; - \&quot;CLICK_TAG_IN_GWD\&quot; - \&quot;CLICK_TAG_MISSING\&quot; - \&quot;CLICK_TAG_MORE_THAN_ONE\&quot; - \&quot;CLICK_TAG_NON_TOP_LEVEL\&quot; - \&quot;COMPONENT_UNSUPPORTED_DCM\&quot; - \&quot;ENABLER_UNSUPPORTED_METHOD_DCM\&quot; - \&quot;EXTERNAL_FILE_REFERENCED\&quot; - \&quot;FILE_DETAIL_EMPTY\&quot; - \&quot;FILE_TYPE_INVALID\&quot; - \&quot;GWD_PROPERTIES_INVALID\&quot; - \&quot;HTML5_FEATURE_UNSUPPORTED\&quot; - \&quot;LINKED_FILE_NOT_FOUND\&quot; - \&quot;MAX_FLASH_VERSION_11\&quot; - \&quot;MRAID_REFERENCED\&quot; - \&quot;NOT_SSL_COMPLIANT\&quot; - \&quot;ORPHANED_ASSET\&quot; - \&quot;PRIMARY_HTML_MISSING\&quot; - \&quot;SVG_INVALID\&quot; - \&quot;ZIP_INVALID\&quot;  | [optional] 



## Enum: [DetectedFeaturesEnum]


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





## Enum: [WarnedValidationRulesEnum]


* `CLICK_TAG_NON_TOP_LEVEL` (value: `"CLICK_TAG_NON_TOP_LEVEL"`)

* `CLICK_TAG_MISSING` (value: `"CLICK_TAG_MISSING"`)

* `CLICK_TAG_MORE_THAN_ONE` (value: `"CLICK_TAG_MORE_THAN_ONE"`)

* `CLICK_TAG_INVALID` (value: `"CLICK_TAG_INVALID"`)

* `ORPHANED_ASSET` (value: `"ORPHANED_ASSET"`)

* `PRIMARY_HTML_MISSING` (value: `"PRIMARY_HTML_MISSING"`)

* `EXTERNAL_FILE_REFERENCED` (value: `"EXTERNAL_FILE_REFERENCED"`)

* `MRAID_REFERENCED` (value: `"MRAID_REFERENCED"`)

* `ADMOB_REFERENCED` (value: `"ADMOB_REFERENCED"`)

* `FILE_TYPE_INVALID` (value: `"FILE_TYPE_INVALID"`)

* `ZIP_INVALID` (value: `"ZIP_INVALID"`)

* `LINKED_FILE_NOT_FOUND` (value: `"LINKED_FILE_NOT_FOUND"`)

* `MAX_FLASH_VERSION_11` (value: `"MAX_FLASH_VERSION_11"`)

* `NOT_SSL_COMPLIANT` (value: `"NOT_SSL_COMPLIANT"`)

* `FILE_DETAIL_EMPTY` (value: `"FILE_DETAIL_EMPTY"`)

* `ASSET_INVALID` (value: `"ASSET_INVALID"`)

* `GWD_PROPERTIES_INVALID` (value: `"GWD_PROPERTIES_INVALID"`)

* `ENABLER_UNSUPPORTED_METHOD_DCM` (value: `"ENABLER_UNSUPPORTED_METHOD_DCM"`)

* `ASSET_FORMAT_UNSUPPORTED_DCM` (value: `"ASSET_FORMAT_UNSUPPORTED_DCM"`)

* `COMPONENT_UNSUPPORTED_DCM` (value: `"COMPONENT_UNSUPPORTED_DCM"`)

* `HTML5_FEATURE_UNSUPPORTED` (value: `"HTML5_FEATURE_UNSUPPORTED"`)

* `CLICK_TAG_IN_GWD` (value: `"CLICK_TAG_IN_GWD"`)

* `CLICK_TAG_HARD_CODED` (value: `"CLICK_TAG_HARD_CODED"`)

* `SVG_INVALID` (value: `"SVG_INVALID"`)

* `CLICK_TAG_IN_RICH_MEDIA` (value: `"CLICK_TAG_IN_RICH_MEDIA"`)




