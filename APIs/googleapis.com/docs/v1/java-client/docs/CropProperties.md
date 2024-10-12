

# CropProperties

The crop properties of an image. The crop rectangle is represented using fractional offsets from the original content's 4 edges. - If the offset is in the interval (0, 1), the corresponding edge of crop rectangle is positioned inside of the image's original bounding rectangle. - If the offset is negative or greater than 1, the corresponding edge of crop rectangle is positioned outside of the image's original bounding rectangle. - If all offsets and rotation angle are 0, the image is not cropped.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**angle** | **Float** | The clockwise rotation angle of the crop rectangle around its center, in radians. Rotation is applied after the offsets. |  [optional] |
|**offsetBottom** | **Float** | The offset specifies how far inwards the bottom edge of the crop rectangle is from the bottom edge of the original content as a fraction of the original content&#39;s height. |  [optional] |
|**offsetLeft** | **Float** | The offset specifies how far inwards the left edge of the crop rectangle is from the left edge of the original content as a fraction of the original content&#39;s width. |  [optional] |
|**offsetRight** | **Float** | The offset specifies how far inwards the right edge of the crop rectangle is from the right edge of the original content as a fraction of the original content&#39;s width. |  [optional] |
|**offsetTop** | **Float** | The offset specifies how far inwards the top edge of the crop rectangle is from the top edge of the original content as a fraction of the original content&#39;s height. |  [optional] |



