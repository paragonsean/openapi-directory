

# Process


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**crop** | **String** | Crops the image according to the specified mechanism. If you specify the size \&quot;WidthexHeight\&quot;, the image will be cropped centered. If coordinates \&quot;x1,y1,x2,y2\&quot; are given, the image is cropped according to the coordinates. The image will be cropped to the size of the stories if \&quot;faces\&quot; are specified as. Example Centered: \&quot;crop\&quot;: \&quot;200x300\&quot;. Example Region: \&quot;crop\&quot;: \&quot;200,300,150,300\&quot;. Example Faces: \&quot;crop\&quot;: \&quot;faces\&quot;. |  [optional] |
|**flip** | **Boolean** | Flips the image around the horizontal axis, from top to bottom. Example: \&quot;flip\&quot;: true |  [optional] |
|**mirror** | **Boolean** | Mirrors the image around the vertical axis, i.e. from right to left. Example: \&quot;mirror\&quot;: true |  [optional] |
|**processingAlgorithm** | **String** | Schlüssel welcher Verarbeitungs-Algorithmus angewendet wird. Zur Auswahl stehen \&quot;logo-to-vector\&quot;, \&quot;logo-super-resolution\&quot;, \&quot;logo-segmentation\&quot; und \&quot;image-processing\&quot;. |  |
|**resize** | **String** | Changes the size of the image according to the specified size. Example: \&quot;resize\&quot;: \&quot;200x300\&quot;. |  [optional] |
|**rotate** | **Integer** | Rotates the image around the center according to the specified degree. Example: \&quot;rotate\&quot;: 90 |  [optional] |



