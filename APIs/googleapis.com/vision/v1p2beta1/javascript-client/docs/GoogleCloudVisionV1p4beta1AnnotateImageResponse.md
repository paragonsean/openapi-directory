# CloudVisionApi.GoogleCloudVisionV1p4beta1AnnotateImageResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**GoogleCloudVisionV1p4beta1ImageAnnotationContext**](GoogleCloudVisionV1p4beta1ImageAnnotationContext.md) |  | [optional] 
**cropHintsAnnotation** | [**GoogleCloudVisionV1p4beta1CropHintsAnnotation**](GoogleCloudVisionV1p4beta1CropHintsAnnotation.md) |  | [optional] 
**error** | [**Status**](Status.md) |  | [optional] 
**faceAnnotations** | [**[GoogleCloudVisionV1p4beta1FaceAnnotation]**](GoogleCloudVisionV1p4beta1FaceAnnotation.md) | If present, face detection has completed successfully. | [optional] 
**fullTextAnnotation** | [**GoogleCloudVisionV1p4beta1TextAnnotation**](GoogleCloudVisionV1p4beta1TextAnnotation.md) |  | [optional] 
**imagePropertiesAnnotation** | [**GoogleCloudVisionV1p4beta1ImageProperties**](GoogleCloudVisionV1p4beta1ImageProperties.md) |  | [optional] 
**labelAnnotations** | [**[GoogleCloudVisionV1p4beta1EntityAnnotation]**](GoogleCloudVisionV1p4beta1EntityAnnotation.md) | If present, label detection has completed successfully. | [optional] 
**landmarkAnnotations** | [**[GoogleCloudVisionV1p4beta1EntityAnnotation]**](GoogleCloudVisionV1p4beta1EntityAnnotation.md) | If present, landmark detection has completed successfully. | [optional] 
**localizedObjectAnnotations** | [**[GoogleCloudVisionV1p4beta1LocalizedObjectAnnotation]**](GoogleCloudVisionV1p4beta1LocalizedObjectAnnotation.md) | If present, localized object detection has completed successfully. This will be sorted descending by confidence score. | [optional] 
**logoAnnotations** | [**[GoogleCloudVisionV1p4beta1EntityAnnotation]**](GoogleCloudVisionV1p4beta1EntityAnnotation.md) | If present, logo detection has completed successfully. | [optional] 
**productSearchResults** | [**GoogleCloudVisionV1p4beta1ProductSearchResults**](GoogleCloudVisionV1p4beta1ProductSearchResults.md) |  | [optional] 
**safeSearchAnnotation** | [**GoogleCloudVisionV1p4beta1SafeSearchAnnotation**](GoogleCloudVisionV1p4beta1SafeSearchAnnotation.md) |  | [optional] 
**textAnnotations** | [**[GoogleCloudVisionV1p4beta1EntityAnnotation]**](GoogleCloudVisionV1p4beta1EntityAnnotation.md) | If present, text (OCR) detection has completed successfully. | [optional] 
**webDetection** | [**GoogleCloudVisionV1p4beta1WebDetection**](GoogleCloudVisionV1p4beta1WebDetection.md) |  | [optional] 


