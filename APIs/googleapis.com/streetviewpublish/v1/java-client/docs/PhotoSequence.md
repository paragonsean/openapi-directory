

# PhotoSequence

A sequence of 360 photos along with metadata.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**captureTimeOverride** | **String** | Optional. Absolute time when the photo sequence starts to be captured. If the photo sequence is a video, this is the start time of the video. If this field is populated in input, it overrides the capture time in the video or XDM file. |  [optional] |
|**distanceMeters** | **Double** | Output only. The computed distance of the photo sequence in meters. |  [optional] [readonly] |
|**failureDetails** | [**ProcessingFailureDetails**](ProcessingFailureDetails.md) |  |  [optional] |
|**failureReason** | [**FailureReasonEnum**](#FailureReasonEnum) | Output only. If this sequence has processing_state &#x3D; FAILED, this will contain the reason why it failed. If the processing_state is any other value, this field will be unset. |  [optional] [readonly] |
|**filename** | **String** | Output only. The filename of the upload. Does not include the directory path. Only available if the sequence was uploaded on a platform that provides the filename. |  [optional] [readonly] |
|**gpsSource** | [**GpsSourceEnum**](#GpsSourceEnum) | Input only. If both raw_gps_timeline and the Camera Motion Metadata Track (CAMM) contain GPS measurements, indicate which takes precedence. |  [optional] |
|**id** | **String** | Output only. Unique identifier for the photo sequence. This also acts as a long running operation ID if uploading is performed asynchronously. |  [optional] [readonly] |
|**imu** | [**Imu**](Imu.md) |  |  [optional] |
|**photos** | [**List&lt;Photo&gt;**](Photo.md) | Output only. Photos with increasing timestamps. |  [optional] [readonly] |
|**processingState** | [**ProcessingStateEnum**](#ProcessingStateEnum) | Output only. The processing state of this sequence. |  [optional] [readonly] |
|**rawGpsTimeline** | [**List&lt;Pose&gt;**](Pose.md) | Input only. Raw GPS measurements with increasing timestamps from the device that aren&#39;t time synced with each photo. These raw measurements will be used to infer the pose of each frame. Required in input when InputType is VIDEO and raw GPS measurements are not in Camera Motion Metadata Track (CAMM). User can indicate which takes precedence using gps_source if raw GPS measurements are provided in both raw_gps_timeline and Camera Motion Metadata Track (CAMM). |  [optional] |
|**sequenceBounds** | [**LatLngBounds**](LatLngBounds.md) |  |  [optional] |
|**uploadReference** | [**UploadRef**](UploadRef.md) |  |  [optional] |
|**uploadTime** | **String** | Output only. The time this photo sequence was created in uSV Store service. |  [optional] [readonly] |
|**viewCount** | **String** | Output only. The total number of views that all the published images in this PhotoSequence have received. |  [optional] [readonly] |



## Enum: FailureReasonEnum

| Name | Value |
|---- | -----|
| PROCESSING_FAILURE_REASON_UNSPECIFIED | &quot;PROCESSING_FAILURE_REASON_UNSPECIFIED&quot; |
| LOW_RESOLUTION | &quot;LOW_RESOLUTION&quot; |
| DUPLICATE | &quot;DUPLICATE&quot; |
| INSUFFICIENT_GPS | &quot;INSUFFICIENT_GPS&quot; |
| NO_OVERLAP_GPS | &quot;NO_OVERLAP_GPS&quot; |
| INVALID_GPS | &quot;INVALID_GPS&quot; |
| FAILED_TO_REFINE_POSITIONS | &quot;FAILED_TO_REFINE_POSITIONS&quot; |
| TAKEDOWN | &quot;TAKEDOWN&quot; |
| CORRUPT_VIDEO | &quot;CORRUPT_VIDEO&quot; |
| INTERNAL | &quot;INTERNAL&quot; |
| INVALID_VIDEO_FORMAT | &quot;INVALID_VIDEO_FORMAT&quot; |
| INVALID_VIDEO_DIMENSIONS | &quot;INVALID_VIDEO_DIMENSIONS&quot; |
| INVALID_CAPTURE_TIME | &quot;INVALID_CAPTURE_TIME&quot; |
| GPS_DATA_GAP | &quot;GPS_DATA_GAP&quot; |
| JUMPY_GPS | &quot;JUMPY_GPS&quot; |
| INVALID_IMU | &quot;INVALID_IMU&quot; |
| INSUFFICIENT_IMU | &quot;INSUFFICIENT_IMU&quot; |
| INSUFFICIENT_OVERLAP_TIME_SERIES | &quot;INSUFFICIENT_OVERLAP_TIME_SERIES&quot; |
| IMU_DATA_GAP | &quot;IMU_DATA_GAP&quot; |
| UNSUPPORTED_CAMERA | &quot;UNSUPPORTED_CAMERA&quot; |
| NOT_OUTDOORS | &quot;NOT_OUTDOORS&quot; |
| INSUFFICIENT_VIDEO_FRAMES | &quot;INSUFFICIENT_VIDEO_FRAMES&quot; |
| INSUFFICIENT_MOVEMENT | &quot;INSUFFICIENT_MOVEMENT&quot; |
| MAST_DOWN | &quot;MAST_DOWN&quot; |
| CAMERA_COVERED | &quot;CAMERA_COVERED&quot; |



## Enum: GpsSourceEnum

| Name | Value |
|---- | -----|
| PHOTO_SEQUENCE | &quot;PHOTO_SEQUENCE&quot; |
| CAMERA_MOTION_METADATA_TRACK | &quot;CAMERA_MOTION_METADATA_TRACK&quot; |



## Enum: ProcessingStateEnum

| Name | Value |
|---- | -----|
| PROCESSING_STATE_UNSPECIFIED | &quot;PROCESSING_STATE_UNSPECIFIED&quot; |
| PENDING | &quot;PENDING&quot; |
| PROCESSING | &quot;PROCESSING&quot; |
| PROCESSED | &quot;PROCESSED&quot; |
| FAILED | &quot;FAILED&quot; |



