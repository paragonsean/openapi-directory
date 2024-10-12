# VertexAiApi.GoogleCloudAiplatformV1SchemaPredictPredictionTextExtractionPredictionResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confidences** | **[Number]** | The Model&#39;s confidences in correctness of the predicted IDs, higher value means higher confidence. Order matches the Ids. | [optional] 
**displayNames** | **[String]** | The display names of the AnnotationSpecs that had been identified, order matches the IDs. | [optional] 
**ids** | **[String]** | The resource IDs of the AnnotationSpecs that had been identified, ordered by the confidence score descendingly. | [optional] 
**textSegmentEndOffsets** | **[String]** | The end offsets, inclusive, of the text segment in which the AnnotationSpec has been identified. Expressed as a zero-based number of characters as measured from the start of the text snippet. | [optional] 
**textSegmentStartOffsets** | **[String]** | The start offsets, inclusive, of the text segment in which the AnnotationSpec has been identified. Expressed as a zero-based number of characters as measured from the start of the text snippet. | [optional] 


