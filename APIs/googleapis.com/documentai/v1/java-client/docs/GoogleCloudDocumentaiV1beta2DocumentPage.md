

# GoogleCloudDocumentaiV1beta2DocumentPage

A page in a Document.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**blocks** | [**List&lt;GoogleCloudDocumentaiV1beta2DocumentPageBlock&gt;**](GoogleCloudDocumentaiV1beta2DocumentPageBlock.md) | A list of visually detected text blocks on the page. A block has a set of lines (collected into paragraphs) that have a common line-spacing and orientation. |  [optional] |
|**detectedBarcodes** | [**List&lt;GoogleCloudDocumentaiV1beta2DocumentPageDetectedBarcode&gt;**](GoogleCloudDocumentaiV1beta2DocumentPageDetectedBarcode.md) | A list of detected barcodes. |  [optional] |
|**detectedLanguages** | [**List&lt;GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguage&gt;**](GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguage.md) | A list of detected languages together with confidence. |  [optional] |
|**dimension** | [**GoogleCloudDocumentaiV1beta2DocumentPageDimension**](GoogleCloudDocumentaiV1beta2DocumentPageDimension.md) |  |  [optional] |
|**formFields** | [**List&lt;GoogleCloudDocumentaiV1beta2DocumentPageFormField&gt;**](GoogleCloudDocumentaiV1beta2DocumentPageFormField.md) | A list of visually detected form fields on the page. |  [optional] |
|**image** | [**GoogleCloudDocumentaiV1beta2DocumentPageImage**](GoogleCloudDocumentaiV1beta2DocumentPageImage.md) |  |  [optional] |
|**imageQualityScores** | [**GoogleCloudDocumentaiV1beta2DocumentPageImageQualityScores**](GoogleCloudDocumentaiV1beta2DocumentPageImageQualityScores.md) |  |  [optional] |
|**layout** | [**GoogleCloudDocumentaiV1beta2DocumentPageLayout**](GoogleCloudDocumentaiV1beta2DocumentPageLayout.md) |  |  [optional] |
|**lines** | [**List&lt;GoogleCloudDocumentaiV1beta2DocumentPageLine&gt;**](GoogleCloudDocumentaiV1beta2DocumentPageLine.md) | A list of visually detected text lines on the page. A collection of tokens that a human would perceive as a line. |  [optional] |
|**pageNumber** | **Integer** | 1-based index for current Page in a parent Document. Useful when a page is taken out of a Document for individual processing. |  [optional] |
|**paragraphs** | [**List&lt;GoogleCloudDocumentaiV1beta2DocumentPageParagraph&gt;**](GoogleCloudDocumentaiV1beta2DocumentPageParagraph.md) | A list of visually detected text paragraphs on the page. A collection of lines that a human would perceive as a paragraph. |  [optional] |
|**provenance** | [**GoogleCloudDocumentaiV1beta2DocumentProvenance**](GoogleCloudDocumentaiV1beta2DocumentProvenance.md) |  |  [optional] |
|**symbols** | [**List&lt;GoogleCloudDocumentaiV1beta2DocumentPageSymbol&gt;**](GoogleCloudDocumentaiV1beta2DocumentPageSymbol.md) | A list of visually detected symbols on the page. |  [optional] |
|**tables** | [**List&lt;GoogleCloudDocumentaiV1beta2DocumentPageTable&gt;**](GoogleCloudDocumentaiV1beta2DocumentPageTable.md) | A list of visually detected tables on the page. |  [optional] |
|**tokens** | [**List&lt;GoogleCloudDocumentaiV1beta2DocumentPageToken&gt;**](GoogleCloudDocumentaiV1beta2DocumentPageToken.md) | A list of visually detected tokens on the page. |  [optional] |
|**transforms** | [**List&lt;GoogleCloudDocumentaiV1beta2DocumentPageMatrix&gt;**](GoogleCloudDocumentaiV1beta2DocumentPageMatrix.md) | Transformation matrices that were applied to the original document image to produce Page.image. |  [optional] |
|**visualElements** | [**List&lt;GoogleCloudDocumentaiV1beta2DocumentPageVisualElement&gt;**](GoogleCloudDocumentaiV1beta2DocumentPageVisualElement.md) | A list of detected non-text visual elements e.g. checkbox, signature etc. on the page. |  [optional] |



