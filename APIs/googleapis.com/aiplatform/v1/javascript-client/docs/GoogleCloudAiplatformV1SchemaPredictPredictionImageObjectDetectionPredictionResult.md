# VertexAiApi.GoogleCloudAiplatformV1SchemaPredictPredictionImageObjectDetectionPredictionResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bboxes** | **[[Object]]** | Bounding boxes, i.e. the rectangles over the image, that pinpoint the found AnnotationSpecs. Given in order that matches the IDs. Each bounding box is an array of 4 numbers &#x60;xMin&#x60;, &#x60;xMax&#x60;, &#x60;yMin&#x60;, and &#x60;yMax&#x60;, which represent the extremal coordinates of the box. They are relative to the image size, and the point 0,0 is in the top left of the image. | [optional] 
**confidences** | **[Number]** | The Model&#39;s confidences in correctness of the predicted IDs, higher value means higher confidence. Order matches the Ids. | [optional] 
**displayNames** | **[String]** | The display names of the AnnotationSpecs that had been identified, order matches the IDs. | [optional] 
**ids** | **[String]** | The resource IDs of the AnnotationSpecs that had been identified, ordered by the confidence score descendingly. | [optional] 


