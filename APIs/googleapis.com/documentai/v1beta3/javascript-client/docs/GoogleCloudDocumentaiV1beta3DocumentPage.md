# CloudDocumentAiApi.GoogleCloudDocumentaiV1beta3DocumentPage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blocks** | [**[GoogleCloudDocumentaiV1beta3DocumentPageBlock]**](GoogleCloudDocumentaiV1beta3DocumentPageBlock.md) | A list of visually detected text blocks on the page. A block has a set of lines (collected into paragraphs) that have a common line-spacing and orientation. | [optional] 
**detectedBarcodes** | [**[GoogleCloudDocumentaiV1beta3DocumentPageDetectedBarcode]**](GoogleCloudDocumentaiV1beta3DocumentPageDetectedBarcode.md) | A list of detected barcodes. | [optional] 
**detectedLanguages** | [**[GoogleCloudDocumentaiV1beta3DocumentPageDetectedLanguage]**](GoogleCloudDocumentaiV1beta3DocumentPageDetectedLanguage.md) | A list of detected languages together with confidence. | [optional] 
**dimension** | [**GoogleCloudDocumentaiV1beta3DocumentPageDimension**](GoogleCloudDocumentaiV1beta3DocumentPageDimension.md) |  | [optional] 
**formFields** | [**[GoogleCloudDocumentaiV1beta3DocumentPageFormField]**](GoogleCloudDocumentaiV1beta3DocumentPageFormField.md) | A list of visually detected form fields on the page. | [optional] 
**image** | [**GoogleCloudDocumentaiV1beta3DocumentPageImage**](GoogleCloudDocumentaiV1beta3DocumentPageImage.md) |  | [optional] 
**imageQualityScores** | [**GoogleCloudDocumentaiV1beta3DocumentPageImageQualityScores**](GoogleCloudDocumentaiV1beta3DocumentPageImageQualityScores.md) |  | [optional] 
**layout** | [**GoogleCloudDocumentaiV1beta3DocumentPageLayout**](GoogleCloudDocumentaiV1beta3DocumentPageLayout.md) |  | [optional] 
**lines** | [**[GoogleCloudDocumentaiV1beta3DocumentPageLine]**](GoogleCloudDocumentaiV1beta3DocumentPageLine.md) | A list of visually detected text lines on the page. A collection of tokens that a human would perceive as a line. | [optional] 
**pageNumber** | **Number** | 1-based index for current Page in a parent Document. Useful when a page is taken out of a Document for individual processing. | [optional] 
**paragraphs** | [**[GoogleCloudDocumentaiV1beta3DocumentPageParagraph]**](GoogleCloudDocumentaiV1beta3DocumentPageParagraph.md) | A list of visually detected text paragraphs on the page. A collection of lines that a human would perceive as a paragraph. | [optional] 
**provenance** | [**GoogleCloudDocumentaiV1beta3DocumentProvenance**](GoogleCloudDocumentaiV1beta3DocumentProvenance.md) |  | [optional] 
**symbols** | [**[GoogleCloudDocumentaiV1beta3DocumentPageSymbol]**](GoogleCloudDocumentaiV1beta3DocumentPageSymbol.md) | A list of visually detected symbols on the page. | [optional] 
**tables** | [**[GoogleCloudDocumentaiV1beta3DocumentPageTable]**](GoogleCloudDocumentaiV1beta3DocumentPageTable.md) | A list of visually detected tables on the page. | [optional] 
**tokens** | [**[GoogleCloudDocumentaiV1beta3DocumentPageToken]**](GoogleCloudDocumentaiV1beta3DocumentPageToken.md) | A list of visually detected tokens on the page. | [optional] 
**transforms** | [**[GoogleCloudDocumentaiV1beta3DocumentPageMatrix]**](GoogleCloudDocumentaiV1beta3DocumentPageMatrix.md) | Transformation matrices that were applied to the original document image to produce Page.image. | [optional] 
**visualElements** | [**[GoogleCloudDocumentaiV1beta3DocumentPageVisualElement]**](GoogleCloudDocumentaiV1beta3DocumentPageVisualElement.md) | A list of detected non-text visual elements e.g. checkbox, signature etc. on the page. | [optional] 


