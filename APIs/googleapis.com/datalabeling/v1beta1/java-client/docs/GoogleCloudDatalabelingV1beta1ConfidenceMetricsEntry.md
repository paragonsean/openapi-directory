

# GoogleCloudDatalabelingV1beta1ConfidenceMetricsEntry


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**confidenceThreshold** | **Float** | Threshold used for this entry. For classification tasks, this is a classification threshold: a predicted label is categorized as positive or negative (in the context of this point on the PR curve) based on whether the label&#39;s score meets this threshold. For image object detection (bounding box) tasks, this is the [intersection-over-union (IOU)](/vision/automl/object-detection/docs/evaluate#intersection-over-union) threshold for the context of this point on the PR curve. |  [optional] |
|**f1Score** | **Float** | Harmonic mean of recall and precision. |  [optional] |
|**f1ScoreAt1** | **Float** | The harmonic mean of recall_at1 and precision_at1. |  [optional] |
|**f1ScoreAt5** | **Float** | The harmonic mean of recall_at5 and precision_at5. |  [optional] |
|**precision** | **Float** | Precision value. |  [optional] |
|**precisionAt1** | **Float** | Precision value for entries with label that has highest score. |  [optional] |
|**precisionAt5** | **Float** | Precision value for entries with label that has highest 5 scores. |  [optional] |
|**recall** | **Float** | Recall value. |  [optional] |
|**recallAt1** | **Float** | Recall value for entries with label that has highest score. |  [optional] |
|**recallAt5** | **Float** | Recall value for entries with label that has highest 5 scores. |  [optional] |



