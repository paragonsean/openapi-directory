

# Photo

Photo is used to store 360 photos along with photo metadata.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**captureTime** | **String** | Optional. Absolute time when the photo was captured. When the photo has no exif timestamp, this is used to set a timestamp in the photo metadata. |  [optional] |
|**connections** | [**List&lt;Connection&gt;**](Connection.md) | Optional. Connections to other photos. A connection represents the link from this photo to another photo. |  [optional] |
|**downloadUrl** | **String** | Output only. The download URL for the photo bytes. This field is set only when GetPhotoRequest.view is set to PhotoView.INCLUDE_DOWNLOAD_URL. |  [optional] [readonly] |
|**mapsPublishStatus** | [**MapsPublishStatusEnum**](#MapsPublishStatusEnum) | Output only. Status in Google Maps, whether this photo was published or rejected. |  [optional] [readonly] |
|**photoId** | [**PhotoId**](PhotoId.md) |  |  [optional] |
|**places** | [**List&lt;Place&gt;**](Place.md) | Optional. Places where this photo belongs. |  [optional] |
|**pose** | [**Pose**](Pose.md) |  |  [optional] |
|**shareLink** | **String** | Output only. The share link for the photo. |  [optional] [readonly] |
|**thumbnailUrl** | **String** | Output only. The thumbnail URL for showing a preview of the given photo. |  [optional] [readonly] |
|**transferStatus** | [**TransferStatusEnum**](#TransferStatusEnum) | Output only. Status of rights transfer on this photo. |  [optional] [readonly] |
|**uploadReference** | [**UploadRef**](UploadRef.md) |  |  [optional] |
|**uploadTime** | **String** | Output only. Time when the image was uploaded. |  [optional] [readonly] |
|**viewCount** | **String** | Output only. View count of the photo. |  [optional] [readonly] |



## Enum: MapsPublishStatusEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED_MAPS_PUBLISH_STATUS | &quot;UNSPECIFIED_MAPS_PUBLISH_STATUS&quot; |
| PUBLISHED | &quot;PUBLISHED&quot; |
| REJECTED_UNKNOWN | &quot;REJECTED_UNKNOWN&quot; |



## Enum: TransferStatusEnum

| Name | Value |
|---- | -----|
| TRANSFER_STATUS_UNKNOWN | &quot;TRANSFER_STATUS_UNKNOWN&quot; |
| NEVER_TRANSFERRED | &quot;NEVER_TRANSFERRED&quot; |
| PENDING | &quot;PENDING&quot; |
| COMPLETED | &quot;COMPLETED&quot; |
| REJECTED | &quot;REJECTED&quot; |
| EXPIRED | &quot;EXPIRED&quot; |
| CANCELLED | &quot;CANCELLED&quot; |
| RECEIVED_VIA_TRANSFER | &quot;RECEIVED_VIA_TRANSFER&quot; |



