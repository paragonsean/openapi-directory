# CloudVisionApi.GoogleCloudVisionV1p2beta1AnnotateImageResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**GoogleCloudVisionV1p2beta1ImageAnnotationContext**](GoogleCloudVisionV1p2beta1ImageAnnotationContext.md) |  | [optional] 
**cropHintsAnnotation** | [**GoogleCloudVisionV1p2beta1CropHintsAnnotation**](GoogleCloudVisionV1p2beta1CropHintsAnnotation.md) |  | [optional] 
**error** | [**Status**](Status.md) |  | [optional] 
**faceAnnotations** | [**[GoogleCloudVisionV1p2beta1FaceAnnotation]**](GoogleCloudVisionV1p2beta1FaceAnnotation.md) | If present, face detection has completed successfully. | [optional] 
**fullTextAnnotation** | [**GoogleCloudVisionV1p2beta1TextAnnotation**](GoogleCloudVisionV1p2beta1TextAnnotation.md) |  | [optional] 
**imagePropertiesAnnotation** | [**GoogleCloudVisionV1p2beta1ImageProperties**](GoogleCloudVisionV1p2beta1ImageProperties.md) |  | [optional] 
**labelAnnotations** | [**[GoogleCloudVisionV1p2beta1EntityAnnotation]**](GoogleCloudVisionV1p2beta1EntityAnnotation.md) | If present, label detection has completed successfully. | [optional] 
**landmarkAnnotations** | [**[GoogleCloudVisionV1p2beta1EntityAnnotation]**](GoogleCloudVisionV1p2beta1EntityAnnotation.md) | If present, landmark detection has completed successfully. | [optional] 
**localizedObjectAnnotations** | [**[GoogleCloudVisionV1p2beta1LocalizedObjectAnnotation]**](GoogleCloudVisionV1p2beta1LocalizedObjectAnnotation.md) | If present, localized object detection has completed successfully. This will be sorted descending by confidence score. | [optional] 
**logoAnnotations** | [**[GoogleCloudVisionV1p2beta1EntityAnnotation]**](GoogleCloudVisionV1p2beta1EntityAnnotation.md) | If present, logo detection has completed successfully. | [optional] 
**productSearchResults** | [**GoogleCloudVisionV1p2beta1ProductSearchResults**](GoogleCloudVisionV1p2beta1ProductSearchResults.md) |  | [optional] 
**safeSearchAnnotation** | [**GoogleCloudVisionV1p2beta1SafeSearchAnnotation**](GoogleCloudVisionV1p2beta1SafeSearchAnnotation.md) |  | [optional] 
**textAnnotations** | [**[GoogleCloudVisionV1p2beta1EntityAnnotation]**](GoogleCloudVisionV1p2beta1EntityAnnotation.md) | If present, text (OCR) detection has completed successfully. | [optional] 
**webDetection** | [**GoogleCloudVisionV1p2beta1WebDetection**](GoogleCloudVisionV1p2beta1WebDetection.md) |  | [optional] 


