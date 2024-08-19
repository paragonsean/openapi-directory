

# GoogleCloudAiplatformV1beta1SchemaPredictPredictionTextExtractionPredictionResult

Prediction output format for Text Extraction.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**confidences** | **List&lt;Float&gt;** | The Model&#39;s confidences in correctness of the predicted IDs, higher value means higher confidence. Order matches the Ids. |  [optional] |
|**displayNames** | **List&lt;String&gt;** | The display names of the AnnotationSpecs that had been identified, order matches the IDs. |  [optional] |
|**ids** | **List&lt;String&gt;** | The resource IDs of the AnnotationSpecs that had been identified, ordered by the confidence score descendingly. |  [optional] |
|**textSegmentEndOffsets** | **List&lt;String&gt;** | The end offsets, inclusive, of the text segment in which the AnnotationSpec has been identified. Expressed as a zero-based number of characters as measured from the start of the text snippet. |  [optional] |
|**textSegmentStartOffsets** | **List&lt;String&gt;** | The start offsets, inclusive, of the text segment in which the AnnotationSpec has been identified. Expressed as a zero-based number of characters as measured from the start of the text snippet. |  [optional] |



