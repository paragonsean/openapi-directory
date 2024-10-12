

# BoundingBoxMetricsEntry

Bounding box matching model metrics for a single intersection-over-union threshold and multiple label match confidence thresholds.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**confidenceMetricsEntries** | [**List&lt;BoundingBoxMetricsEntryConfidenceMetricsEntry&gt;**](BoundingBoxMetricsEntryConfidenceMetricsEntry.md) | Output only. Metrics for each label-match confidence_threshold from 0.05,0.10,...,0.95,0.96,0.97,0.98,0.99. Precision-recall curve is derived from them. |  [optional] |
|**iouThreshold** | **Float** | Output only. The intersection-over-union threshold value used to compute this metrics entry. |  [optional] |
|**meanAveragePrecision** | **Float** | Output only. The mean average precision, most often close to au_prc. |  [optional] |



