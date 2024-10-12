

# UploadVideoAlt1RequestSpatial


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**directorTimeline** | [**List&lt;UploadVideoAlt1RequestSpatialDirectorTimelineInner&gt;**](UploadVideoAlt1RequestSpatialDirectorTimelineInner.md) | The 360 director timeline. |  [optional] |
|**fieldOfView** | **BigDecimal** | The 360 field of view: default 50, minimum 30, maximum 90. |  [optional] |
|**projection** | [**ProjectionEnum**](#ProjectionEnum) | The 360 spatial projection. |  [optional] |
|**stereoFormat** | [**StereoFormatEnum**](#StereoFormatEnum) | The 360 spatial stereo format. |  [optional] |



## Enum: ProjectionEnum

| Name | Value |
|---- | -----|
| CUBICAL | &quot;cubical&quot; |
| CYLINDRICAL | &quot;cylindrical&quot; |
| DOME | &quot;dome&quot; |
| EQUIRECTANGULAR | &quot;equirectangular&quot; |
| PYRAMID | &quot;pyramid&quot; |



## Enum: StereoFormatEnum

| Name | Value |
|---- | -----|
| LEFT_RIGHT | &quot;left-right&quot; |
| MONO | &quot;mono&quot; |
| TOP_BOTTOM | &quot;top-bottom&quot; |



