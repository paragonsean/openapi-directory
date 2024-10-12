

# VideoSpatial

360 spatial data.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**directorTimeline** | [**List&lt;VideoSpatialDirectorTimelineInner&gt;**](VideoSpatialDirectorTimelineInner.md) | 360 director timeline. |  |
|**fieldOfView** | **BigDecimal** | The 360 field of view, from 30 (minimum) to 90 (maximum). The default is 50. |  |
|**projection** | [**ProjectionEnum**](#ProjectionEnum) | The 360 spatial projection:  Option descriptions:  * &#x60;cubical&#x60; - The spatial projection is cubical.  * &#x60;cylindrical&#x60; - The spatial projection is cylindrical.  * &#x60;dome&#x60; - The spatial projection is dome-shaped.  * &#x60;equirectangular&#x60; - The spatial projection is equirectangular.  * &#x60;pyramid&#x60; - The spatial projection is pyramid-shaped.  |  |
|**stereoFormat** | [**StereoFormatEnum**](#StereoFormatEnum) | The 360 stereo format:  Option descriptions:  * &#x60;left-right&#x60; - The stereo format is left-right.  * &#x60;mono&#x60; - The audio is monaural.  * &#x60;top-bottom&#x60; - The stereo format is top-bottom.  |  |



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



