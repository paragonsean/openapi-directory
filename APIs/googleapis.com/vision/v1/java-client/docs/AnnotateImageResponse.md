

# AnnotateImageResponse

Response to an image annotation request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**context** | [**ImageAnnotationContext**](ImageAnnotationContext.md) |  |  [optional] |
|**cropHintsAnnotation** | [**CropHintsAnnotation**](CropHintsAnnotation.md) |  |  [optional] |
|**error** | [**Status**](Status.md) |  |  [optional] |
|**faceAnnotations** | [**List&lt;FaceAnnotation&gt;**](FaceAnnotation.md) | If present, face detection has completed successfully. |  [optional] |
|**fullTextAnnotation** | [**TextAnnotation**](TextAnnotation.md) |  |  [optional] |
|**imagePropertiesAnnotation** | [**ImageProperties**](ImageProperties.md) |  |  [optional] |
|**labelAnnotations** | [**List&lt;EntityAnnotation&gt;**](EntityAnnotation.md) | If present, label detection has completed successfully. |  [optional] |
|**landmarkAnnotations** | [**List&lt;EntityAnnotation&gt;**](EntityAnnotation.md) | If present, landmark detection has completed successfully. |  [optional] |
|**localizedObjectAnnotations** | [**List&lt;LocalizedObjectAnnotation&gt;**](LocalizedObjectAnnotation.md) | If present, localized object detection has completed successfully. This will be sorted descending by confidence score. |  [optional] |
|**logoAnnotations** | [**List&lt;EntityAnnotation&gt;**](EntityAnnotation.md) | If present, logo detection has completed successfully. |  [optional] |
|**productSearchResults** | [**ProductSearchResults**](ProductSearchResults.md) |  |  [optional] |
|**safeSearchAnnotation** | [**SafeSearchAnnotation**](SafeSearchAnnotation.md) |  |  [optional] |
|**textAnnotations** | [**List&lt;EntityAnnotation&gt;**](EntityAnnotation.md) | If present, text (OCR) detection has completed successfully. |  [optional] |
|**webDetection** | [**WebDetection**](WebDetection.md) |  |  [optional] |



