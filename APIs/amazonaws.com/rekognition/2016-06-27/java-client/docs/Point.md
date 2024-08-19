

# Point

<p>The X and Y coordinates of a point on an image or video frame. The X and Y values are ratios of the overall image size or video resolution. For example, if an input image is 700x200 and the values are X=0.5 and Y=0.25, then the point is at the (350,50) pixel coordinate on the image.</p> <p>An array of <code>Point</code> objects makes up a <code>Polygon</code>. A <code>Polygon</code> is returned by <a>DetectText</a> and by <a>DetectCustomLabels</a> <code>Polygon</code> represents a fine-grained polygon around a detected item. For more information, see Geometry in the Amazon Rekognition Developer Guide. </p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**X** | [**Float**](Float.md) |  |  [optional] |
|**Y** | [**Float**](Float.md) |  |  [optional] |



