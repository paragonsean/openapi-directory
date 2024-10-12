# CloudVisionApi.Feature

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maxResults** | **Number** | Maximum number of results of this type. Does not apply to &#x60;TEXT_DETECTION&#x60;, &#x60;DOCUMENT_TEXT_DETECTION&#x60;, or &#x60;CROP_HINTS&#x60;. | [optional] 
**model** | **String** | Model to use for the feature. Supported values: \&quot;builtin/stable\&quot; (the default if unset) and \&quot;builtin/latest\&quot;. &#x60;DOCUMENT_TEXT_DETECTION&#x60; and &#x60;TEXT_DETECTION&#x60; also support \&quot;builtin/weekly\&quot; for the bleeding edge release updated weekly. | [optional] 
**type** | **String** | The feature type. | [optional] 



## Enum: TypeEnum


* `TYPE_UNSPECIFIED` (value: `"TYPE_UNSPECIFIED"`)

* `FACE_DETECTION` (value: `"FACE_DETECTION"`)

* `LANDMARK_DETECTION` (value: `"LANDMARK_DETECTION"`)

* `LOGO_DETECTION` (value: `"LOGO_DETECTION"`)

* `LABEL_DETECTION` (value: `"LABEL_DETECTION"`)

* `TEXT_DETECTION` (value: `"TEXT_DETECTION"`)

* `DOCUMENT_TEXT_DETECTION` (value: `"DOCUMENT_TEXT_DETECTION"`)

* `SAFE_SEARCH_DETECTION` (value: `"SAFE_SEARCH_DETECTION"`)

* `IMAGE_PROPERTIES` (value: `"IMAGE_PROPERTIES"`)

* `CROP_HINTS` (value: `"CROP_HINTS"`)

* `WEB_DETECTION` (value: `"WEB_DETECTION"`)

* `PRODUCT_SEARCH` (value: `"PRODUCT_SEARCH"`)

* `OBJECT_LOCALIZATION` (value: `"OBJECT_LOCALIZATION"`)




