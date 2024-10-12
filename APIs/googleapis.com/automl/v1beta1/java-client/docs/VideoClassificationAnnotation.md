

# VideoClassificationAnnotation

Contains annotation details specific to video classification.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**classificationAnnotation** | [**ClassificationAnnotation**](ClassificationAnnotation.md) |  |  [optional] |
|**timeSegment** | [**TimeSegment**](TimeSegment.md) |  |  [optional] |
|**type** | **String** | Output only. Expresses the type of video classification. Possible values: * &#x60;segment&#x60; - Classification done on a specified by user time segment of a video. AnnotationSpec is answered to be present in that time segment, if it is present in any part of it. The video ML model evaluations are done only for this type of classification. * &#x60;shot&#x60;- Shot-level classification. AutoML Video Intelligence determines the boundaries for each camera shot in the entire segment of the video that user specified in the request configuration. AutoML Video Intelligence then returns labels and their confidence scores for each detected shot, along with the start and end time of the shot. WARNING: Model evaluation is not done for this classification type, the quality of it depends on training data, but there are no metrics provided to describe that quality. * &#x60;1s_interval&#x60; - AutoML Video Intelligence returns labels and their confidence scores for each second of the entire segment of the video that user specified in the request configuration. WARNING: Model evaluation is not done for this classification type, the quality of it depends on training data, but there are no metrics provided to describe that quality. |  [optional] |



