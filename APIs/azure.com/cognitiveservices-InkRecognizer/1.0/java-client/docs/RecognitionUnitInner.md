

# RecognitionUnitInner

This identifies the recognized entity

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alternates** | [**List&lt;AlternatePatternInner&gt;**](AlternatePatternInner.md) | The list of alternates for the core recognition result. In case of handwriting related recognition units, this list includes other words that are close possibilities to the results provided as &#39;recognizedText&#39;. |  [optional] |
|**boundingRectangle** | [**RecognitionUnitInnerBoundingRectangle**](RecognitionUnitInnerBoundingRectangle.md) |  |  [optional] |
|**category** | **CategoryPattern** |  |  |
|**center** | [**PointDetailsPattern**](PointDetailsPattern.md) |  |  [optional] |
|**childIds** | **List&lt;Integer&gt;** | An array of integers representing the identifier of each child of the current recognition unit. |  [optional] |
|**propertyClass** | **ClassPattern** |  |  |
|**confidence** | **BigDecimal** | A number between 0 and 1 which indicates the confidence level in the result. |  [optional] |
|**id** | **Integer** | The identifier of the recognition unit. This id is used to indicate parent/child relationship between different recognition units. |  |
|**parentId** | **Integer** | The id of the parent node in the tree structure of the recognition results. parent &#x3D; 0 indicates that there is no dedicated parent node for this unit. |  |
|**points** | [**List&lt;PointDetailsPattern&gt;**](PointDetailsPattern.md) | Array of point objects that represent points that are relevant to the type of recognition unit. For example, for a leaf node of inkDrawing category that represents a triangle, points would include the x, y coordinates of the vertices of the recognized triangle. The points represent the coordinates used to create the perfectly drawn shape that is closest to the original input. They may not exactly match. |  [optional] |
|**recognizedObject** | **ShapePattern** |  |  [optional] |
|**recognizedText** | **String** | The string contains the text that was recognized. It can be an empty string if the recognizer cannot determine the text. |  [optional] |
|**rotatedBoundingRectangle** | [**List&lt;PointDetailsPattern&gt;**](PointDetailsPattern.md) | This is the rotated bounding rectangle that covers the entire recognized object along the angle of rotation of the object. Note that this is NOT the same as rotating the boundingRectangle by the rotation angle. |  [optional] |
|**rotationAngle** | **BigDecimal** | This is the angle at which the unit is rotated in degrees with respect to the positive X axis. |  [optional] |
|**strokeIds** | **List&lt;Integer&gt;** | This is an array of integers representing the list of stroke Identifiers from the input request body that belong to this recognition unit. |  |



