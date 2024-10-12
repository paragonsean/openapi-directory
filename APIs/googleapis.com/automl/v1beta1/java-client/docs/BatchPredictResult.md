

# BatchPredictResult

Result of the Batch Predict. This message is returned in response of the operation returned by the PredictionService.BatchPredict.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**metadata** | **Map&lt;String, String&gt;** | Additional domain-specific prediction response metadata. * For Image Object Detection: &#x60;max_bounding_box_count&#x60; - (int64) At most that many bounding boxes per image could have been returned. * For Video Object Tracking: &#x60;max_bounding_box_count&#x60; - (int64) At most that many bounding boxes per frame could have been returned. |  [optional] |



