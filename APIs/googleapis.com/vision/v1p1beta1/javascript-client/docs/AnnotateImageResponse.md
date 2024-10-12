# CloudVisionApi.AnnotateImageResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**ImageAnnotationContext**](ImageAnnotationContext.md) |  | [optional] 
**cropHintsAnnotation** | [**CropHintsAnnotation**](CropHintsAnnotation.md) |  | [optional] 
**error** | [**Status**](Status.md) |  | [optional] 
**faceAnnotations** | [**[FaceAnnotation]**](FaceAnnotation.md) | If present, face detection has completed successfully. | [optional] 
**fullTextAnnotation** | [**TextAnnotation**](TextAnnotation.md) |  | [optional] 
**imagePropertiesAnnotation** | [**ImageProperties**](ImageProperties.md) |  | [optional] 
**labelAnnotations** | [**[EntityAnnotation]**](EntityAnnotation.md) | If present, label detection has completed successfully. | [optional] 
**landmarkAnnotations** | [**[EntityAnnotation]**](EntityAnnotation.md) | If present, landmark detection has completed successfully. | [optional] 
**localizedObjectAnnotations** | [**[LocalizedObjectAnnotation]**](LocalizedObjectAnnotation.md) | If present, localized object detection has completed successfully. This will be sorted descending by confidence score. | [optional] 
**logoAnnotations** | [**[EntityAnnotation]**](EntityAnnotation.md) | If present, logo detection has completed successfully. | [optional] 
**productSearchResults** | [**ProductSearchResults**](ProductSearchResults.md) |  | [optional] 
**safeSearchAnnotation** | [**SafeSearchAnnotation**](SafeSearchAnnotation.md) |  | [optional] 
**textAnnotations** | [**[EntityAnnotation]**](EntityAnnotation.md) | If present, text (OCR) detection has completed successfully. | [optional] 
**webDetection** | [**WebDetection**](WebDetection.md) |  | [optional] 


