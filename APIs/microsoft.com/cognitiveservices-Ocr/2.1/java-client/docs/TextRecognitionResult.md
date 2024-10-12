

# TextRecognitionResult

An object representing a recognized text region

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clockwiseOrientation** | **BigDecimal** | The orientation of the image in degrees in the clockwise direction. Range between [0, 360). |  [optional] |
|**height** | **BigDecimal** | The height of the image in pixels or the PDF in inches. |  [optional] |
|**lines** | [**List&lt;Line&gt;**](Line.md) | A list of recognized text lines. |  |
|**page** | **Integer** | The 1-based page number of the recognition result. |  [optional] |
|**unit** | [**UnitEnum**](#UnitEnum) | The unit used in the Width, Height and BoundingBox. For images, the unit is &#39;pixel&#39;. For PDF, the unit is &#39;inch&#39;. |  [optional] |
|**width** | **BigDecimal** | The width of the image in pixels or the PDF in inches. |  [optional] |



## Enum: UnitEnum

| Name | Value |
|---- | -----|
| PIXEL | &quot;pixel&quot; |
| INCH | &quot;inch&quot; |



