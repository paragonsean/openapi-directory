

# GoogleCloudVisionV1p2beta1Feature

The type of Google Cloud Vision API detection to perform, and the maximum number of results to return for that type. Multiple `Feature` objects can be specified in the `features` list.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**maxResults** | **Integer** | Maximum number of results of this type. Does not apply to &#x60;TEXT_DETECTION&#x60;, &#x60;DOCUMENT_TEXT_DETECTION&#x60;, or &#x60;CROP_HINTS&#x60;. |  [optional] |
|**model** | **String** | Model to use for the feature. Supported values: \&quot;builtin/stable\&quot; (the default if unset) and \&quot;builtin/latest\&quot;. &#x60;DOCUMENT_TEXT_DETECTION&#x60; and &#x60;TEXT_DETECTION&#x60; also support \&quot;builtin/weekly\&quot; for the bleeding edge release updated weekly. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The feature type. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| FACE_DETECTION | &quot;FACE_DETECTION&quot; |
| LANDMARK_DETECTION | &quot;LANDMARK_DETECTION&quot; |
| LOGO_DETECTION | &quot;LOGO_DETECTION&quot; |
| LABEL_DETECTION | &quot;LABEL_DETECTION&quot; |
| TEXT_DETECTION | &quot;TEXT_DETECTION&quot; |
| DOCUMENT_TEXT_DETECTION | &quot;DOCUMENT_TEXT_DETECTION&quot; |
| SAFE_SEARCH_DETECTION | &quot;SAFE_SEARCH_DETECTION&quot; |
| IMAGE_PROPERTIES | &quot;IMAGE_PROPERTIES&quot; |
| CROP_HINTS | &quot;CROP_HINTS&quot; |
| WEB_DETECTION | &quot;WEB_DETECTION&quot; |
| PRODUCT_SEARCH | &quot;PRODUCT_SEARCH&quot; |
| OBJECT_LOCALIZATION | &quot;OBJECT_LOCALIZATION&quot; |



