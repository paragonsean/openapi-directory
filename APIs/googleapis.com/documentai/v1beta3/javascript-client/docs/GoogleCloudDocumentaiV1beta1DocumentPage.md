# CloudDocumentAiApi.GoogleCloudDocumentaiV1beta1DocumentPage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blocks** | [**[GoogleCloudDocumentaiV1beta1DocumentPageBlock]**](GoogleCloudDocumentaiV1beta1DocumentPageBlock.md) | A list of visually detected text blocks on the page. A block has a set of lines (collected into paragraphs) that have a common line-spacing and orientation. | [optional] 
**detectedBarcodes** | [**[GoogleCloudDocumentaiV1beta1DocumentPageDetectedBarcode]**](GoogleCloudDocumentaiV1beta1DocumentPageDetectedBarcode.md) | A list of detected barcodes. | [optional] 
**detectedLanguages** | [**[GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguage]**](GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguage.md) | A list of detected languages together with confidence. | [optional] 
**dimension** | [**GoogleCloudDocumentaiV1beta1DocumentPageDimension**](GoogleCloudDocumentaiV1beta1DocumentPageDimension.md) |  | [optional] 
**formFields** | [**[GoogleCloudDocumentaiV1beta1DocumentPageFormField]**](GoogleCloudDocumentaiV1beta1DocumentPageFormField.md) | A list of visually detected form fields on the page. | [optional] 
**image** | [**GoogleCloudDocumentaiV1beta1DocumentPageImage**](GoogleCloudDocumentaiV1beta1DocumentPageImage.md) |  | [optional] 
**imageQualityScores** | [**GoogleCloudDocumentaiV1beta1DocumentPageImageQualityScores**](GoogleCloudDocumentaiV1beta1DocumentPageImageQualityScores.md) |  | [optional] 
**layout** | [**GoogleCloudDocumentaiV1beta1DocumentPageLayout**](GoogleCloudDocumentaiV1beta1DocumentPageLayout.md) |  | [optional] 
**lines** | [**[GoogleCloudDocumentaiV1beta1DocumentPageLine]**](GoogleCloudDocumentaiV1beta1DocumentPageLine.md) | A list of visually detected text lines on the page. A collection of tokens that a human would perceive as a line. | [optional] 
**pageNumber** | **Number** | 1-based index for current Page in a parent Document. Useful when a page is taken out of a Document for individual processing. | [optional] 
**paragraphs** | [**[GoogleCloudDocumentaiV1beta1DocumentPageParagraph]**](GoogleCloudDocumentaiV1beta1DocumentPageParagraph.md) | A list of visually detected text paragraphs on the page. A collection of lines that a human would perceive as a paragraph. | [optional] 
**provenance** | [**GoogleCloudDocumentaiV1beta1DocumentProvenance**](GoogleCloudDocumentaiV1beta1DocumentProvenance.md) |  | [optional] 
**symbols** | [**[GoogleCloudDocumentaiV1beta1DocumentPageSymbol]**](GoogleCloudDocumentaiV1beta1DocumentPageSymbol.md) | A list of visually detected symbols on the page. | [optional] 
**tables** | [**[GoogleCloudDocumentaiV1beta1DocumentPageTable]**](GoogleCloudDocumentaiV1beta1DocumentPageTable.md) | A list of visually detected tables on the page. | [optional] 
**tokens** | [**[GoogleCloudDocumentaiV1beta1DocumentPageToken]**](GoogleCloudDocumentaiV1beta1DocumentPageToken.md) | A list of visually detected tokens on the page. | [optional] 
**transforms** | [**[GoogleCloudDocumentaiV1beta1DocumentPageMatrix]**](GoogleCloudDocumentaiV1beta1DocumentPageMatrix.md) | Transformation matrices that were applied to the original document image to produce Page.image. | [optional] 
**visualElements** | [**[GoogleCloudDocumentaiV1beta1DocumentPageVisualElement]**](GoogleCloudDocumentaiV1beta1DocumentPageVisualElement.md) | A list of detected non-text visual elements e.g. checkbox, signature etc. on the page. | [optional] 


