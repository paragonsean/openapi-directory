

# InkPoint

An object containing the properties of an point in the path of an ink stroke. The main properties are the x and y values. Other include tip pressure, x tilt etc. For the coordinate values, it is recommended to have a precision of 8 digits after the decimal to obtain most accurate recognition results. The origin (0,0) of the canvas is assumed to be at the top left corner of the canvas

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**barrelPressure** | **BigDecimal** | The force exerted directly by the user on a transducer sensor, such as a pressure-sensitive button on the barrel of a stylus. This may not be used for recognition. |  [optional] |
|**barrelSwitch** | **Boolean** | A non-tip button located on the barrel of a stylus. Its function is typically mapped to a system secondary button. This may not be used for recognition. |  [optional] |
|**eraser** | **Boolean** | The control is used for erasing objects. It is typically located opposite the writing end of a stylus. This may not be used for recognition. |  [optional] |
|**height** | **BigDecimal** | The height of the tip of the writing instrument. This is used by touch screen devices to report the height of the finger contact on the writing surface. This may not be used for recognition. |  [optional] |
|**inverted** | **Boolean** | A value that indicates that the currently sensed position originates from the end of a stylus opposite the tip switch. This may not be used for recognition. |  [optional] |
|**secondaryTip** | **Boolean** | A secondary switch used in conjunction with the tip switch to indicate pressure above a certain threshold applied with the stylus. This may not be used for recognition. |  [optional] |
|**timestamp** | **BigDecimal** | The time relative to the absolute time the transducer last became active. This may not be used for recognition. |  [optional] |
|**tipPressure** | **BigDecimal** | The force exerted against the tablet surface by the transducer, typically a stylus. This may not be used for recognition. |  [optional] |
|**tipSwitch** | **Boolean** | A switch located on the tip of a stylus indicating contact of the stylus with a surface. This may not be used for recognition. |  [optional] |
|**width** | **BigDecimal** | The width of the tip of the writing instrument. This is used by touch screen devices to report the width of the finger contact on the writing surface. This may not be used for recognition. |  [optional] |
|**x** | **BigDecimal** | The x coordinate of the pen location on the writing surface. |  |
|**xTilt** | **BigDecimal** | The plane angle between the Y-Z plane and the plane containing the transducer axis and the Y axis. This may not be used for recognition. |  [optional] |
|**y** | **BigDecimal** | The y coordinate of the pen location on the writing surface. |  |
|**yTilt** | **BigDecimal** | The angle between the X-Z and transducer-X planes. A positive Y Tilt is toward the user. This may not be used for recognition. |  [optional] |
|**z** | **BigDecimal** | The z coordinate of the pen location on the writing space. This may not be used for recognition. |  [optional] |



