# StreetViewPublishApi.PhotoSequence

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**captureTimeOverride** | **String** | Optional. Absolute time when the photo sequence starts to be captured. If the photo sequence is a video, this is the start time of the video. If this field is populated in input, it overrides the capture time in the video or XDM file. | [optional] 
**distanceMeters** | **Number** | Output only. The computed distance of the photo sequence in meters. | [optional] [readonly] 
**failureDetails** | [**ProcessingFailureDetails**](ProcessingFailureDetails.md) |  | [optional] 
**failureReason** | **String** | Output only. If this sequence has processing_state &#x3D; FAILED, this will contain the reason why it failed. If the processing_state is any other value, this field will be unset. | [optional] [readonly] 
**filename** | **String** | Output only. The filename of the upload. Does not include the directory path. Only available if the sequence was uploaded on a platform that provides the filename. | [optional] [readonly] 
**gpsSource** | **String** | Input only. If both raw_gps_timeline and the Camera Motion Metadata Track (CAMM) contain GPS measurements, indicate which takes precedence. | [optional] 
**id** | **String** | Output only. Unique identifier for the photo sequence. This also acts as a long running operation ID if uploading is performed asynchronously. | [optional] [readonly] 
**imu** | [**Imu**](Imu.md) |  | [optional] 
**photos** | [**[Photo]**](Photo.md) | Output only. Photos with increasing timestamps. | [optional] [readonly] 
**processingState** | **String** | Output only. The processing state of this sequence. | [optional] [readonly] 
**rawGpsTimeline** | [**[Pose]**](Pose.md) | Input only. Raw GPS measurements with increasing timestamps from the device that aren&#39;t time synced with each photo. These raw measurements will be used to infer the pose of each frame. Required in input when InputType is VIDEO and raw GPS measurements are not in Camera Motion Metadata Track (CAMM). User can indicate which takes precedence using gps_source if raw GPS measurements are provided in both raw_gps_timeline and Camera Motion Metadata Track (CAMM). | [optional] 
**sequenceBounds** | [**LatLngBounds**](LatLngBounds.md) |  | [optional] 
**uploadReference** | [**UploadRef**](UploadRef.md) |  | [optional] 
**uploadTime** | **String** | Output only. The time this photo sequence was created in uSV Store service. | [optional] [readonly] 
**viewCount** | **String** | Output only. The total number of views that all the published images in this PhotoSequence have received. | [optional] [readonly] 



## Enum: FailureReasonEnum


* `PROCESSING_FAILURE_REASON_UNSPECIFIED` (value: `"PROCESSING_FAILURE_REASON_UNSPECIFIED"`)

* `LOW_RESOLUTION` (value: `"LOW_RESOLUTION"`)

* `DUPLICATE` (value: `"DUPLICATE"`)

* `INSUFFICIENT_GPS` (value: `"INSUFFICIENT_GPS"`)

* `NO_OVERLAP_GPS` (value: `"NO_OVERLAP_GPS"`)

* `INVALID_GPS` (value: `"INVALID_GPS"`)

* `FAILED_TO_REFINE_POSITIONS` (value: `"FAILED_TO_REFINE_POSITIONS"`)

* `TAKEDOWN` (value: `"TAKEDOWN"`)

* `CORRUPT_VIDEO` (value: `"CORRUPT_VIDEO"`)

* `INTERNAL` (value: `"INTERNAL"`)

* `INVALID_VIDEO_FORMAT` (value: `"INVALID_VIDEO_FORMAT"`)

* `INVALID_VIDEO_DIMENSIONS` (value: `"INVALID_VIDEO_DIMENSIONS"`)

* `INVALID_CAPTURE_TIME` (value: `"INVALID_CAPTURE_TIME"`)

* `GPS_DATA_GAP` (value: `"GPS_DATA_GAP"`)

* `JUMPY_GPS` (value: `"JUMPY_GPS"`)

* `INVALID_IMU` (value: `"INVALID_IMU"`)

* `INSUFFICIENT_IMU` (value: `"INSUFFICIENT_IMU"`)

* `INSUFFICIENT_OVERLAP_TIME_SERIES` (value: `"INSUFFICIENT_OVERLAP_TIME_SERIES"`)

* `IMU_DATA_GAP` (value: `"IMU_DATA_GAP"`)

* `UNSUPPORTED_CAMERA` (value: `"UNSUPPORTED_CAMERA"`)

* `NOT_OUTDOORS` (value: `"NOT_OUTDOORS"`)

* `INSUFFICIENT_VIDEO_FRAMES` (value: `"INSUFFICIENT_VIDEO_FRAMES"`)

* `INSUFFICIENT_MOVEMENT` (value: `"INSUFFICIENT_MOVEMENT"`)

* `MAST_DOWN` (value: `"MAST_DOWN"`)

* `CAMERA_COVERED` (value: `"CAMERA_COVERED"`)





## Enum: GpsSourceEnum


* `PHOTO_SEQUENCE` (value: `"PHOTO_SEQUENCE"`)

* `CAMERA_MOTION_METADATA_TRACK` (value: `"CAMERA_MOTION_METADATA_TRACK"`)





## Enum: ProcessingStateEnum


* `PROCESSING_STATE_UNSPECIFIED` (value: `"PROCESSING_STATE_UNSPECIFIED"`)

* `PENDING` (value: `"PENDING"`)

* `PROCESSING` (value: `"PROCESSING"`)

* `PROCESSED` (value: `"PROCESSED"`)

* `FAILED` (value: `"FAILED"`)




