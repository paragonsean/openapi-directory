

# GoogleCloudAiplatformV1beta1SchemaPredictPredictionImageObjectDetectionPredictionResult

Prediction output format for Image Object Detection.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bboxes** | **List&lt;List&lt;Object&gt;&gt;** | Bounding boxes, i.e. the rectangles over the image, that pinpoint the found AnnotationSpecs. Given in order that matches the IDs. Each bounding box is an array of 4 numbers &#x60;xMin&#x60;, &#x60;xMax&#x60;, &#x60;yMin&#x60;, and &#x60;yMax&#x60;, which represent the extremal coordinates of the box. They are relative to the image size, and the point 0,0 is in the top left of the image. |  [optional] |
|**confidences** | **List&lt;Float&gt;** | The Model&#39;s confidences in correctness of the predicted IDs, higher value means higher confidence. Order matches the Ids. |  [optional] |
|**displayNames** | **List&lt;String&gt;** | The display names of the AnnotationSpecs that had been identified, order matches the IDs. |  [optional] |
|**ids** | **List&lt;String&gt;** | The resource IDs of the AnnotationSpecs that had been identified, ordered by the confidence score descendingly. |  [optional] |



