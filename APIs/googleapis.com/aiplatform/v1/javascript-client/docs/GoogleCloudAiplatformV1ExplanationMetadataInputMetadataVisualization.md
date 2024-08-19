# VertexAiApi.GoogleCloudAiplatformV1ExplanationMetadataInputMetadataVisualization

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clipPercentLowerbound** | **Number** | Excludes attributions below the specified percentile, from the highlighted areas. Defaults to 62. | [optional] 
**clipPercentUpperbound** | **Number** | Excludes attributions above the specified percentile from the highlighted areas. Using the clip_percent_upperbound and clip_percent_lowerbound together can be useful for filtering out noise and making it easier to see areas of strong attribution. Defaults to 99.9. | [optional] 
**colorMap** | **String** | The color scheme used for the highlighted areas. Defaults to PINK_GREEN for Integrated Gradients attribution, which shows positive attributions in green and negative in pink. Defaults to VIRIDIS for XRAI attribution, which highlights the most influential regions in yellow and the least influential in blue. | [optional] 
**overlayType** | **String** | How the original image is displayed in the visualization. Adjusting the overlay can help increase visual clarity if the original image makes it difficult to view the visualization. Defaults to NONE. | [optional] 
**polarity** | **String** | Whether to only highlight pixels with positive contributions, negative or both. Defaults to POSITIVE. | [optional] 
**type** | **String** | Type of the image visualization. Only applicable to Integrated Gradients attribution. OUTLINES shows regions of attribution, while PIXELS shows per-pixel attribution. Defaults to OUTLINES. | [optional] 



## Enum: ColorMapEnum


* `COLOR_MAP_UNSPECIFIED` (value: `"COLOR_MAP_UNSPECIFIED"`)

* `PINK_GREEN` (value: `"PINK_GREEN"`)

* `VIRIDIS` (value: `"VIRIDIS"`)

* `RED` (value: `"RED"`)

* `GREEN` (value: `"GREEN"`)

* `RED_GREEN` (value: `"RED_GREEN"`)

* `PINK_WHITE_GREEN` (value: `"PINK_WHITE_GREEN"`)





## Enum: OverlayTypeEnum


* `OVERLAY_TYPE_UNSPECIFIED` (value: `"OVERLAY_TYPE_UNSPECIFIED"`)

* `NONE` (value: `"NONE"`)

* `ORIGINAL` (value: `"ORIGINAL"`)

* `GRAYSCALE` (value: `"GRAYSCALE"`)

* `MASK_BLACK` (value: `"MASK_BLACK"`)





## Enum: PolarityEnum


* `POLARITY_UNSPECIFIED` (value: `"POLARITY_UNSPECIFIED"`)

* `POSITIVE` (value: `"POSITIVE"`)

* `NEGATIVE` (value: `"NEGATIVE"`)

* `BOTH` (value: `"BOTH"`)





## Enum: TypeEnum


* `TYPE_UNSPECIFIED` (value: `"TYPE_UNSPECIFIED"`)

* `PIXELS` (value: `"PIXELS"`)

* `OUTLINES` (value: `"OUTLINES"`)




