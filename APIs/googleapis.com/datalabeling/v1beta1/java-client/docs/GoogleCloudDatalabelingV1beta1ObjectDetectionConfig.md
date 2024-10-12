

# GoogleCloudDatalabelingV1beta1ObjectDetectionConfig

Config for video object detection human labeling task. Object detection will be conducted on the images extracted from the video, and those objects will be labeled with bounding boxes. User need to specify the number of images to be extracted per second as the extraction frame rate.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**annotationSpecSet** | **String** | Required. Annotation spec set resource name. |  [optional] |
|**extractionFrameRate** | **Double** | Required. Number of frames per second to be extracted from the video. |  [optional] |



