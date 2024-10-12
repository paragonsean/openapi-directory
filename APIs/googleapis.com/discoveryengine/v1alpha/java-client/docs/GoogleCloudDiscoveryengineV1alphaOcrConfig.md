

# GoogleCloudDiscoveryengineV1alphaOcrConfig

The OCR options for parsing documents.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enabled** | **Boolean** | Required. If OCR is enabled or not. OCR must be enabled for other OcrConfig options to apply. We will only perform OCR on the first 80 pages of the PDF files. |  [optional] |
|**enhancedDocumentElements** | **List&lt;String&gt;** | Apply additional enhanced OCR processing to a list of document elements. Supported values: * &#x60;table&#x60;: advanced table parsing model. |  [optional] |
|**useNativeText** | **Boolean** | If true, will use native text instead of OCR text on pages containing native text. |  [optional] |



