

# GoogleCloudDocumentaiV1beta2OcrParams

Parameters to control Optical Character Recognition (OCR) behavior.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**languageHints** | **List&lt;String&gt;** | List of languages to use for OCR. In most cases, an empty value yields the best results since it enables automatic language detection. For languages based on the Latin alphabet, setting &#x60;language_hints&#x60; is not needed. In rare cases, when the language of the text in the image is known, setting a hint will help get better results (although it will be a significant hindrance if the hint is wrong). Document processing returns an error if one or more of the specified languages is not one of the supported languages. |  [optional] |



