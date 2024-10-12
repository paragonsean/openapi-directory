# InkRecognizerClient.RecognitionUnitInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alternates** | [**[AlternatePatternInner]**](AlternatePatternInner.md) | The list of alternates for the core recognition result. In case of handwriting related recognition units, this list includes other words that are close possibilities to the results provided as &#39;recognizedText&#39;. | [optional] 
**boundingRectangle** | [**RecognitionUnitInnerBoundingRectangle**](RecognitionUnitInnerBoundingRectangle.md) |  | [optional] 
**category** | [**CategoryPattern**](CategoryPattern.md) |  | 
**center** | [**PointDetailsPattern**](PointDetailsPattern.md) |  | [optional] 
**childIds** | **[Number]** | An array of integers representing the identifier of each child of the current recognition unit. | [optional] 
**_class** | [**ClassPattern**](ClassPattern.md) |  | 
**confidence** | **Number** | A number between 0 and 1 which indicates the confidence level in the result. | [optional] 
**id** | **Number** | The identifier of the recognition unit. This id is used to indicate parent/child relationship between different recognition units. | 
**parentId** | **Number** | The id of the parent node in the tree structure of the recognition results. parent &#x3D; 0 indicates that there is no dedicated parent node for this unit. | 
**points** | [**[PointDetailsPattern]**](PointDetailsPattern.md) | Array of point objects that represent points that are relevant to the type of recognition unit. For example, for a leaf node of inkDrawing category that represents a triangle, points would include the x, y coordinates of the vertices of the recognized triangle. The points represent the coordinates used to create the perfectly drawn shape that is closest to the original input. They may not exactly match. | [optional] 
**recognizedObject** | [**ShapePattern**](ShapePattern.md) |  | [optional] 
**recognizedText** | **String** | The string contains the text that was recognized. It can be an empty string if the recognizer cannot determine the text. | [optional] 
**rotatedBoundingRectangle** | [**[PointDetailsPattern]**](PointDetailsPattern.md) | This is the rotated bounding rectangle that covers the entire recognized object along the angle of rotation of the object. Note that this is NOT the same as rotating the boundingRectangle by the rotation angle. | [optional] 
**rotationAngle** | **Number** | This is the angle at which the unit is rotated in degrees with respect to the positive X axis. | [optional] 
**strokeIds** | **[Number]** | This is an array of integers representing the list of stroke Identifiers from the input request body that belong to this recognition unit. | 


