

# GoogleCloudVisionV1p4beta1ReferenceImage

A `ReferenceImage` represents a product image and its associated metadata, such as bounding boxes.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**boundingPolys** | [**List&lt;GoogleCloudVisionV1p4beta1BoundingPoly&gt;**](GoogleCloudVisionV1p4beta1BoundingPoly.md) | Optional. Bounding polygons around the areas of interest in the reference image. If this field is empty, the system will try to detect regions of interest. At most 10 bounding polygons will be used. The provided shape is converted into a non-rotated rectangle. Once converted, the small edge of the rectangle must be greater than or equal to 300 pixels. The aspect ratio must be 1:4 or less (i.e. 1:3 is ok; 1:5 is not). |  [optional] |
|**name** | **String** | The resource name of the reference image. Format is: &#x60;projects/PROJECT_ID/locations/LOC_ID/products/PRODUCT_ID/referenceImages/IMAGE_ID&#x60;. This field is ignored when creating a reference image. |  [optional] |
|**uri** | **String** | Required. The Google Cloud Storage URI of the reference image. The URI must start with &#x60;gs://&#x60;. |  [optional] |



