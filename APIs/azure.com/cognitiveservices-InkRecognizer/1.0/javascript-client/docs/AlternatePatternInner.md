# InkRecognizerClient.AlternatePatternInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | [**LeafCategoryPattern**](LeafCategoryPattern.md) |  | 
**confidence** | **Number** | A number between 0 and 1 which indicates the confidence level in the result | [optional] 
**points** | [**[PointDetailsPattern]**](PointDetailsPattern.md) | Array of point objects that represent points that are relevant to the type of recognition unit. For example, for leaf node of inkDrawing category that represents a triangle, points would include the x,y coordinates of the vertices of the recognized triangle. The points represent the coordinates of points used to create the perfectly drawn shape that is closest to the original input. They may not exactly match. | [optional] 
**recognizedString** | **String** | The recognized string from an inkWord or the name of a recognized shape in an inkDrawing object | 
**rotationAngle** | **Number** | The angular orientation of an object relative to the horizontal axis | [optional] 


