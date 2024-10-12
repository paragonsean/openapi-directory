

# GoogleCloudDocumentaiV1beta3OcrConfig

Config for Document OCR.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**advancedOcrOptions** | **List&lt;String&gt;** | A list of advanced OCR options to further fine-tune OCR behavior. Current valid values are: - &#x60;legacy_layout&#x60;: a heuristics layout detection algorithm, which serves as an alternative to the current ML-based layout detection algorithm. Customers can choose the best suitable layout algorithm based on their situation. |  [optional] |
|**computeStyleInfo** | **Boolean** | Turn on font identification model and return font style information. Deprecated, use PremiumFeatures.compute_style_info instead. |  [optional] |
|**disableCharacterBoxesDetection** | **Boolean** | Turn off character box detector in OCR engine. Character box detection is enabled by default in OCR 2.0 (and later) processors. |  [optional] |
|**enableImageQualityScores** | **Boolean** | Enables intelligent document quality scores after OCR. Can help with diagnosing why OCR responses are of poor quality for a given input. Adds additional latency comparable to regular OCR to the process call. |  [optional] |
|**enableNativePdfParsing** | **Boolean** | Enables special handling for PDFs with existing text information. Results in better text extraction quality in such PDF inputs. |  [optional] |
|**enableSymbol** | **Boolean** | Includes symbol level OCR information if set to true. |  [optional] |
|**hints** | [**GoogleCloudDocumentaiV1beta3OcrConfigHints**](GoogleCloudDocumentaiV1beta3OcrConfigHints.md) |  |  [optional] |
|**premiumFeatures** | [**GoogleCloudDocumentaiV1beta3OcrConfigPremiumFeatures**](GoogleCloudDocumentaiV1beta3OcrConfigPremiumFeatures.md) |  |  [optional] |



