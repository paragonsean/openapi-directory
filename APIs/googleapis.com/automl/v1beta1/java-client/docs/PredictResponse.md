

# PredictResponse

Response message for PredictionService.Predict.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**metadata** | **Map&lt;String, String&gt;** | Additional domain-specific prediction response metadata. * For Image Object Detection: &#x60;max_bounding_box_count&#x60; - (int64) At most that many bounding boxes per image could have been returned. * For Text Sentiment: &#x60;sentiment_score&#x60; - (float, deprecated) A value between -1 and 1, -1 maps to least positive sentiment, while 1 maps to the most positive one and the higher the score, the more positive the sentiment in the document is. Yet these values are relative to the training data, so e.g. if all data was positive then -1 will be also positive (though the least). The sentiment_score shouldn&#39;t be confused with \&quot;score\&quot; or \&quot;magnitude\&quot; from the previous Natural Language Sentiment Analysis API. |  [optional] |
|**payload** | [**List&lt;AnnotationPayload&gt;**](AnnotationPayload.md) | Prediction result. Translation and Text Sentiment will return precisely one payload. |  [optional] |
|**preprocessedInput** | [**ExamplePayload**](ExamplePayload.md) |  |  [optional] |



