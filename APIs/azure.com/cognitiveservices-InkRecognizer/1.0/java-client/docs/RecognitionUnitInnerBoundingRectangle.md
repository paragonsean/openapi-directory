

# RecognitionUnitInnerBoundingRectangle

The bounding rectangle of the recognition unit represented by the coordinates of the top left corner (topX,topY) along with width and height of the rectangle. Note that this rectangle is not rotated. So for  rotated objects such as slanted handwriting, it will cover the entire object. The unit will be matched to the one specified in the original request (mm by default.) 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**height** | **BigDecimal** | The is the height of the bounding rectangle |  [optional] |
|**topX** | **BigDecimal** | This is the top left x coordinate |  [optional] |
|**topY** | **BigDecimal** | This is the top left y coordinate |  [optional] |
|**width** | **BigDecimal** | This is width of the bounding rectangle |  [optional] |



