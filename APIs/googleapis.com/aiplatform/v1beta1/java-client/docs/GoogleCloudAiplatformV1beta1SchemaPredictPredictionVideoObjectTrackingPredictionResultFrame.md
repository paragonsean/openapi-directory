

# GoogleCloudAiplatformV1beta1SchemaPredictPredictionVideoObjectTrackingPredictionResultFrame

The fields `xMin`, `xMax`, `yMin`, and `yMax` refer to a bounding box, i.e. the rectangle over the video frame pinpointing the found AnnotationSpec. The coordinates are relative to the frame size, and the point 0,0 is in the top left of the frame.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**timeOffset** | **String** | A time (frame) of a video in which the object has been detected. Expressed as a number of seconds as measured from the start of the video, with fractions up to a microsecond precision, and with \&quot;s\&quot; appended at the end. |  [optional] |
|**xMax** | **Float** | The rightmost coordinate of the bounding box. |  [optional] |
|**xMin** | **Float** | The leftmost coordinate of the bounding box. |  [optional] |
|**yMax** | **Float** | The bottommost coordinate of the bounding box. |  [optional] |
|**yMin** | **Float** | The topmost coordinate of the bounding box. |  [optional] |



