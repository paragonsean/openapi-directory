

# GoogleCloudDatalabelingV1beta1PrCurve


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**annotationSpec** | [**GoogleCloudDatalabelingV1beta1AnnotationSpec**](GoogleCloudDatalabelingV1beta1AnnotationSpec.md) |  |  [optional] |
|**areaUnderCurve** | **Float** | Area under the precision-recall curve. Not to be confused with area under a receiver operating characteristic (ROC) curve. |  [optional] |
|**confidenceMetricsEntries** | [**List&lt;GoogleCloudDatalabelingV1beta1ConfidenceMetricsEntry&gt;**](GoogleCloudDatalabelingV1beta1ConfidenceMetricsEntry.md) | Entries that make up the precision-recall graph. Each entry is a \&quot;point\&quot; on the graph drawn for a different &#x60;confidence_threshold&#x60;. |  [optional] |
|**meanAveragePrecision** | **Float** | Mean average prcision of this curve. |  [optional] |



