

# GoogleCloudAiplatformV1ExplanationMetadataInputMetadataVisualization

Visualization configurations for image explanation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clipPercentLowerbound** | **Float** | Excludes attributions below the specified percentile, from the highlighted areas. Defaults to 62. |  [optional] |
|**clipPercentUpperbound** | **Float** | Excludes attributions above the specified percentile from the highlighted areas. Using the clip_percent_upperbound and clip_percent_lowerbound together can be useful for filtering out noise and making it easier to see areas of strong attribution. Defaults to 99.9. |  [optional] |
|**colorMap** | [**ColorMapEnum**](#ColorMapEnum) | The color scheme used for the highlighted areas. Defaults to PINK_GREEN for Integrated Gradients attribution, which shows positive attributions in green and negative in pink. Defaults to VIRIDIS for XRAI attribution, which highlights the most influential regions in yellow and the least influential in blue. |  [optional] |
|**overlayType** | [**OverlayTypeEnum**](#OverlayTypeEnum) | How the original image is displayed in the visualization. Adjusting the overlay can help increase visual clarity if the original image makes it difficult to view the visualization. Defaults to NONE. |  [optional] |
|**polarity** | [**PolarityEnum**](#PolarityEnum) | Whether to only highlight pixels with positive contributions, negative or both. Defaults to POSITIVE. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of the image visualization. Only applicable to Integrated Gradients attribution. OUTLINES shows regions of attribution, while PIXELS shows per-pixel attribution. Defaults to OUTLINES. |  [optional] |



## Enum: ColorMapEnum

| Name | Value |
|---- | -----|
| COLOR_MAP_UNSPECIFIED | &quot;COLOR_MAP_UNSPECIFIED&quot; |
| PINK_GREEN | &quot;PINK_GREEN&quot; |
| VIRIDIS | &quot;VIRIDIS&quot; |
| RED | &quot;RED&quot; |
| GREEN | &quot;GREEN&quot; |
| RED_GREEN | &quot;RED_GREEN&quot; |
| PINK_WHITE_GREEN | &quot;PINK_WHITE_GREEN&quot; |



## Enum: OverlayTypeEnum

| Name | Value |
|---- | -----|
| OVERLAY_TYPE_UNSPECIFIED | &quot;OVERLAY_TYPE_UNSPECIFIED&quot; |
| NONE | &quot;NONE&quot; |
| ORIGINAL | &quot;ORIGINAL&quot; |
| GRAYSCALE | &quot;GRAYSCALE&quot; |
| MASK_BLACK | &quot;MASK_BLACK&quot; |



## Enum: PolarityEnum

| Name | Value |
|---- | -----|
| POLARITY_UNSPECIFIED | &quot;POLARITY_UNSPECIFIED&quot; |
| POSITIVE | &quot;POSITIVE&quot; |
| NEGATIVE | &quot;NEGATIVE&quot; |
| BOTH | &quot;BOTH&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| PIXELS | &quot;PIXELS&quot; |
| OUTLINES | &quot;OUTLINES&quot; |



