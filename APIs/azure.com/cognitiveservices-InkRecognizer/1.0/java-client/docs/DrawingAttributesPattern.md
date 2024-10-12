

# DrawingAttributesPattern

The properties to use when rendering ink

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**color** | [**DrawingAttributesPatternColor**](DrawingAttributesPatternColor.md) |  |  [optional] |
|**fitToCurve** | **Boolean** |  This indicates whether Bezier smoothing is used to render the stroke |  [optional] |
|**height** | **BigDecimal** | The height of the stylus used to draw the stroke |  [optional] |
|**ignorePressure** | **Boolean** |  This indicates whether the thickness of a rendered Stroke changes according the amount of pressure applied. |  [optional] |
|**rasterOp** | [**RasterOpEnum**](#RasterOpEnum) |  |  [optional] |
|**tip** | [**TipEnum**](#TipEnum) | This specifies the tip to be used to draw a stroke |  [optional] |
|**width** | **BigDecimal** | The width of the stylus used to draw the stroke |  [optional] |



## Enum: RasterOpEnum

| Name | Value |
|---- | -----|
| NO_OPERATION | &quot;noOperation&quot; |
| COPY_PEN | &quot;copyPen&quot; |
| MASK_PEN | &quot;maskPen&quot; |



## Enum: TipEnum

| Name | Value |
|---- | -----|
| ELLIPSE | &quot;ellipse&quot; |
| RECTANGLE | &quot;rectangle&quot; |



