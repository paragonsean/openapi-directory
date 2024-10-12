

# AnnotationPayload

Contains annotation information that is relevant to AutoML.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**annotationSpecId** | **String** | Output only . The resource ID of the annotation spec that this annotation pertains to. The annotation spec comes from either an ancestor dataset, or the dataset that was used to train the model in use. |  [optional] |
|**classification** | [**ClassificationAnnotation**](ClassificationAnnotation.md) |  |  [optional] |
|**displayName** | **String** | Output only. The value of display_name when the model was trained. Because this field returns a value at model training time, for different models trained using the same dataset, the returned value could be different as model owner could update the &#x60;display_name&#x60; between any two model training. |  [optional] |
|**imageObjectDetection** | [**ImageObjectDetectionAnnotation**](ImageObjectDetectionAnnotation.md) |  |  [optional] |
|**tables** | [**TablesAnnotation**](TablesAnnotation.md) |  |  [optional] |
|**textExtraction** | [**TextExtractionAnnotation**](TextExtractionAnnotation.md) |  |  [optional] |
|**textSentiment** | [**TextSentimentAnnotation**](TextSentimentAnnotation.md) |  |  [optional] |
|**translation** | [**TranslationAnnotation**](TranslationAnnotation.md) |  |  [optional] |
|**videoClassification** | [**VideoClassificationAnnotation**](VideoClassificationAnnotation.md) |  |  [optional] |
|**videoObjectTracking** | [**VideoObjectTrackingAnnotation**](VideoObjectTrackingAnnotation.md) |  |  [optional] |



