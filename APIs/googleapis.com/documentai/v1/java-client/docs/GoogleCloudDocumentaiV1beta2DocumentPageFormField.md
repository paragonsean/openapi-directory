

# GoogleCloudDocumentaiV1beta2DocumentPageFormField

A form field detected on the page.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**correctedKeyText** | **String** | Created for Labeling UI to export key text. If corrections were made to the text identified by the &#x60;field_name.text_anchor&#x60;, this field will contain the correction. |  [optional] |
|**correctedValueText** | **String** | Created for Labeling UI to export value text. If corrections were made to the text identified by the &#x60;field_value.text_anchor&#x60;, this field will contain the correction. |  [optional] |
|**fieldName** | [**GoogleCloudDocumentaiV1beta2DocumentPageLayout**](GoogleCloudDocumentaiV1beta2DocumentPageLayout.md) |  |  [optional] |
|**fieldValue** | [**GoogleCloudDocumentaiV1beta2DocumentPageLayout**](GoogleCloudDocumentaiV1beta2DocumentPageLayout.md) |  |  [optional] |
|**nameDetectedLanguages** | [**List&lt;GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguage&gt;**](GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguage.md) | A list of detected languages for name together with confidence. |  [optional] |
|**provenance** | [**GoogleCloudDocumentaiV1beta2DocumentProvenance**](GoogleCloudDocumentaiV1beta2DocumentProvenance.md) |  |  [optional] |
|**valueDetectedLanguages** | [**List&lt;GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguage&gt;**](GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguage.md) | A list of detected languages for value together with confidence. |  [optional] |
|**valueType** | **String** | If the value is non-textual, this field represents the type. Current valid values are: - blank (this indicates the &#x60;field_value&#x60; is normal text) - &#x60;unfilled_checkbox&#x60; - &#x60;filled_checkbox&#x60; |  [optional] |



