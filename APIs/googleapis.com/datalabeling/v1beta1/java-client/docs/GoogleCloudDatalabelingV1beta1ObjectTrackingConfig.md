

# GoogleCloudDatalabelingV1beta1ObjectTrackingConfig

Config for video object tracking human labeling task.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**annotationSpecSet** | **String** | Required. Annotation spec set resource name. |  [optional] |
|**clipLength** | **Integer** | Videos will be cut to smaller clips to make it easier for labelers to work on. Users can configure is field in seconds, if not set, default value is 20s. |  [optional] |
|**overlapLength** | **Integer** | The overlap length between different video clips. Users can configure is field in seconds, if not set, default value is 0.3s. |  [optional] |



