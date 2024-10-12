# StreetViewPublishApi.Photo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**captureTime** | **String** | Optional. Absolute time when the photo was captured. When the photo has no exif timestamp, this is used to set a timestamp in the photo metadata. | [optional] 
**connections** | [**[Connection]**](Connection.md) | Optional. Connections to other photos. A connection represents the link from this photo to another photo. | [optional] 
**downloadUrl** | **String** | Output only. The download URL for the photo bytes. This field is set only when GetPhotoRequest.view is set to PhotoView.INCLUDE_DOWNLOAD_URL. | [optional] [readonly] 
**mapsPublishStatus** | **String** | Output only. Status in Google Maps, whether this photo was published or rejected. | [optional] [readonly] 
**photoId** | [**PhotoId**](PhotoId.md) |  | [optional] 
**places** | [**[Place]**](Place.md) | Optional. Places where this photo belongs. | [optional] 
**pose** | [**Pose**](Pose.md) |  | [optional] 
**shareLink** | **String** | Output only. The share link for the photo. | [optional] [readonly] 
**thumbnailUrl** | **String** | Output only. The thumbnail URL for showing a preview of the given photo. | [optional] [readonly] 
**transferStatus** | **String** | Output only. Status of rights transfer on this photo. | [optional] [readonly] 
**uploadReference** | [**UploadRef**](UploadRef.md) |  | [optional] 
**uploadTime** | **String** | Output only. Time when the image was uploaded. | [optional] [readonly] 
**viewCount** | **String** | Output only. View count of the photo. | [optional] [readonly] 



## Enum: MapsPublishStatusEnum


* `UNSPECIFIED_MAPS_PUBLISH_STATUS` (value: `"UNSPECIFIED_MAPS_PUBLISH_STATUS"`)

* `PUBLISHED` (value: `"PUBLISHED"`)

* `REJECTED_UNKNOWN` (value: `"REJECTED_UNKNOWN"`)





## Enum: TransferStatusEnum


* `TRANSFER_STATUS_UNKNOWN` (value: `"TRANSFER_STATUS_UNKNOWN"`)

* `NEVER_TRANSFERRED` (value: `"NEVER_TRANSFERRED"`)

* `PENDING` (value: `"PENDING"`)

* `COMPLETED` (value: `"COMPLETED"`)

* `REJECTED` (value: `"REJECTED"`)

* `EXPIRED` (value: `"EXPIRED"`)

* `CANCELLED` (value: `"CANCELLED"`)

* `RECEIVED_VIA_TRANSFER` (value: `"RECEIVED_VIA_TRANSFER"`)




