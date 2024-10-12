

# TextDetectionParams

Parameters for text detections. This is used to control TEXT_DETECTION and DOCUMENT_TEXT_DETECTION features.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**advancedOcrOptions** | **List&lt;String&gt;** | A list of advanced OCR options to further fine-tune OCR behavior. Current valid values are: - &#x60;legacy_layout&#x60;: a heuristics layout detection algorithm, which serves as an alternative to the current ML-based layout detection algorithm. Customers can choose the best suitable layout algorithm based on their situation. |  [optional] |
|**enableTextDetectionConfidenceScore** | **Boolean** | By default, Cloud Vision API only includes confidence score for DOCUMENT_TEXT_DETECTION result. Set the flag to true to include confidence score for TEXT_DETECTION as well. |  [optional] |



