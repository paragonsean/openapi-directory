

# GoogleCloudDocumentaiV1DocumentPage

A page in a Document.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**blocks** | [**List&lt;GoogleCloudDocumentaiV1DocumentPageBlock&gt;**](GoogleCloudDocumentaiV1DocumentPageBlock.md) | A list of visually detected text blocks on the page. A block has a set of lines (collected into paragraphs) that have a common line-spacing and orientation. |  [optional] |
|**detectedBarcodes** | [**List&lt;GoogleCloudDocumentaiV1DocumentPageDetectedBarcode&gt;**](GoogleCloudDocumentaiV1DocumentPageDetectedBarcode.md) | A list of detected barcodes. |  [optional] |
|**detectedLanguages** | [**List&lt;GoogleCloudDocumentaiV1DocumentPageDetectedLanguage&gt;**](GoogleCloudDocumentaiV1DocumentPageDetectedLanguage.md) | A list of detected languages together with confidence. |  [optional] |
|**dimension** | [**GoogleCloudDocumentaiV1DocumentPageDimension**](GoogleCloudDocumentaiV1DocumentPageDimension.md) |  |  [optional] |
|**formFields** | [**List&lt;GoogleCloudDocumentaiV1DocumentPageFormField&gt;**](GoogleCloudDocumentaiV1DocumentPageFormField.md) | A list of visually detected form fields on the page. |  [optional] |
|**image** | [**GoogleCloudDocumentaiV1DocumentPageImage**](GoogleCloudDocumentaiV1DocumentPageImage.md) |  |  [optional] |
|**imageQualityScores** | [**GoogleCloudDocumentaiV1DocumentPageImageQualityScores**](GoogleCloudDocumentaiV1DocumentPageImageQualityScores.md) |  |  [optional] |
|**layout** | [**GoogleCloudDocumentaiV1DocumentPageLayout**](GoogleCloudDocumentaiV1DocumentPageLayout.md) |  |  [optional] |
|**lines** | [**List&lt;GoogleCloudDocumentaiV1DocumentPageLine&gt;**](GoogleCloudDocumentaiV1DocumentPageLine.md) | A list of visually detected text lines on the page. A collection of tokens that a human would perceive as a line. |  [optional] |
|**pageNumber** | **Integer** | 1-based index for current Page in a parent Document. Useful when a page is taken out of a Document for individual processing. |  [optional] |
|**paragraphs** | [**List&lt;GoogleCloudDocumentaiV1DocumentPageParagraph&gt;**](GoogleCloudDocumentaiV1DocumentPageParagraph.md) | A list of visually detected text paragraphs on the page. A collection of lines that a human would perceive as a paragraph. |  [optional] |
|**provenance** | [**GoogleCloudDocumentaiV1DocumentProvenance**](GoogleCloudDocumentaiV1DocumentProvenance.md) |  |  [optional] |
|**symbols** | [**List&lt;GoogleCloudDocumentaiV1DocumentPageSymbol&gt;**](GoogleCloudDocumentaiV1DocumentPageSymbol.md) | A list of visually detected symbols on the page. |  [optional] |
|**tables** | [**List&lt;GoogleCloudDocumentaiV1DocumentPageTable&gt;**](GoogleCloudDocumentaiV1DocumentPageTable.md) | A list of visually detected tables on the page. |  [optional] |
|**tokens** | [**List&lt;GoogleCloudDocumentaiV1DocumentPageToken&gt;**](GoogleCloudDocumentaiV1DocumentPageToken.md) | A list of visually detected tokens on the page. |  [optional] |
|**transforms** | [**List&lt;GoogleCloudDocumentaiV1DocumentPageMatrix&gt;**](GoogleCloudDocumentaiV1DocumentPageMatrix.md) | Transformation matrices that were applied to the original document image to produce Page.image. |  [optional] |
|**visualElements** | [**List&lt;GoogleCloudDocumentaiV1DocumentPageVisualElement&gt;**](GoogleCloudDocumentaiV1DocumentPageVisualElement.md) | A list of detected non-text visual elements e.g. checkbox, signature etc. on the page. |  [optional] |



