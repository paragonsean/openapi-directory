# CloudVisionApi.GoogleCloudVisionV1p2beta1FaceAnnotation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**angerLikelihood** | **String** | Anger likelihood. | [optional] 
**blurredLikelihood** | **String** | Blurred likelihood. | [optional] 
**boundingPoly** | [**GoogleCloudVisionV1p2beta1BoundingPoly**](GoogleCloudVisionV1p2beta1BoundingPoly.md) |  | [optional] 
**detectionConfidence** | **Number** | Detection confidence. Range [0, 1]. | [optional] 
**fdBoundingPoly** | [**GoogleCloudVisionV1p2beta1BoundingPoly**](GoogleCloudVisionV1p2beta1BoundingPoly.md) |  | [optional] 
**headwearLikelihood** | **String** | Headwear likelihood. | [optional] 
**joyLikelihood** | **String** | Joy likelihood. | [optional] 
**landmarkingConfidence** | **Number** | Face landmarking confidence. Range [0, 1]. | [optional] 
**landmarks** | [**[GoogleCloudVisionV1p2beta1FaceAnnotationLandmark]**](GoogleCloudVisionV1p2beta1FaceAnnotationLandmark.md) | Detected face landmarks. | [optional] 
**panAngle** | **Number** | Yaw angle, which indicates the leftward/rightward angle that the face is pointing relative to the vertical plane perpendicular to the image. Range [-180,180]. | [optional] 
**rollAngle** | **Number** | Roll angle, which indicates the amount of clockwise/anti-clockwise rotation of the face relative to the image vertical about the axis perpendicular to the face. Range [-180,180]. | [optional] 
**sorrowLikelihood** | **String** | Sorrow likelihood. | [optional] 
**surpriseLikelihood** | **String** | Surprise likelihood. | [optional] 
**tiltAngle** | **Number** | Pitch angle, which indicates the upwards/downwards angle that the face is pointing relative to the image&#39;s horizontal plane. Range [-180,180]. | [optional] 
**underExposedLikelihood** | **String** | Under-exposed likelihood. | [optional] 



## Enum: AngerLikelihoodEnum


* `UNKNOWN` (value: `"UNKNOWN"`)

* `VERY_UNLIKELY` (value: `"VERY_UNLIKELY"`)

* `UNLIKELY` (value: `"UNLIKELY"`)

* `POSSIBLE` (value: `"POSSIBLE"`)

* `LIKELY` (value: `"LIKELY"`)

* `VERY_LIKELY` (value: `"VERY_LIKELY"`)





## Enum: BlurredLikelihoodEnum


* `UNKNOWN` (value: `"UNKNOWN"`)

* `VERY_UNLIKELY` (value: `"VERY_UNLIKELY"`)

* `UNLIKELY` (value: `"UNLIKELY"`)

* `POSSIBLE` (value: `"POSSIBLE"`)

* `LIKELY` (value: `"LIKELY"`)

* `VERY_LIKELY` (value: `"VERY_LIKELY"`)





## Enum: HeadwearLikelihoodEnum


* `UNKNOWN` (value: `"UNKNOWN"`)

* `VERY_UNLIKELY` (value: `"VERY_UNLIKELY"`)

* `UNLIKELY` (value: `"UNLIKELY"`)

* `POSSIBLE` (value: `"POSSIBLE"`)

* `LIKELY` (value: `"LIKELY"`)

* `VERY_LIKELY` (value: `"VERY_LIKELY"`)





## Enum: JoyLikelihoodEnum


* `UNKNOWN` (value: `"UNKNOWN"`)

* `VERY_UNLIKELY` (value: `"VERY_UNLIKELY"`)

* `UNLIKELY` (value: `"UNLIKELY"`)

* `POSSIBLE` (value: `"POSSIBLE"`)

* `LIKELY` (value: `"LIKELY"`)

* `VERY_LIKELY` (value: `"VERY_LIKELY"`)





## Enum: SorrowLikelihoodEnum


* `UNKNOWN` (value: `"UNKNOWN"`)

* `VERY_UNLIKELY` (value: `"VERY_UNLIKELY"`)

* `UNLIKELY` (value: `"UNLIKELY"`)

* `POSSIBLE` (value: `"POSSIBLE"`)

* `LIKELY` (value: `"LIKELY"`)

* `VERY_LIKELY` (value: `"VERY_LIKELY"`)





## Enum: SurpriseLikelihoodEnum


* `UNKNOWN` (value: `"UNKNOWN"`)

* `VERY_UNLIKELY` (value: `"VERY_UNLIKELY"`)

* `UNLIKELY` (value: `"UNLIKELY"`)

* `POSSIBLE` (value: `"POSSIBLE"`)

* `LIKELY` (value: `"LIKELY"`)

* `VERY_LIKELY` (value: `"VERY_LIKELY"`)





## Enum: UnderExposedLikelihoodEnum


* `UNKNOWN` (value: `"UNKNOWN"`)

* `VERY_UNLIKELY` (value: `"VERY_UNLIKELY"`)

* `UNLIKELY` (value: `"UNLIKELY"`)

* `POSSIBLE` (value: `"POSSIBLE"`)

* `LIKELY` (value: `"LIKELY"`)

* `VERY_LIKELY` (value: `"VERY_LIKELY"`)




