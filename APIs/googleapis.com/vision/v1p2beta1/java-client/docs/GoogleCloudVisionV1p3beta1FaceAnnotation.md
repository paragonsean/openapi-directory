

# GoogleCloudVisionV1p3beta1FaceAnnotation

A face annotation object contains the results of face detection.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**angerLikelihood** | [**AngerLikelihoodEnum**](#AngerLikelihoodEnum) | Anger likelihood. |  [optional] |
|**blurredLikelihood** | [**BlurredLikelihoodEnum**](#BlurredLikelihoodEnum) | Blurred likelihood. |  [optional] |
|**boundingPoly** | [**GoogleCloudVisionV1p3beta1BoundingPoly**](GoogleCloudVisionV1p3beta1BoundingPoly.md) |  |  [optional] |
|**detectionConfidence** | **Float** | Detection confidence. Range [0, 1]. |  [optional] |
|**fdBoundingPoly** | [**GoogleCloudVisionV1p3beta1BoundingPoly**](GoogleCloudVisionV1p3beta1BoundingPoly.md) |  |  [optional] |
|**headwearLikelihood** | [**HeadwearLikelihoodEnum**](#HeadwearLikelihoodEnum) | Headwear likelihood. |  [optional] |
|**joyLikelihood** | [**JoyLikelihoodEnum**](#JoyLikelihoodEnum) | Joy likelihood. |  [optional] |
|**landmarkingConfidence** | **Float** | Face landmarking confidence. Range [0, 1]. |  [optional] |
|**landmarks** | [**List&lt;GoogleCloudVisionV1p3beta1FaceAnnotationLandmark&gt;**](GoogleCloudVisionV1p3beta1FaceAnnotationLandmark.md) | Detected face landmarks. |  [optional] |
|**panAngle** | **Float** | Yaw angle, which indicates the leftward/rightward angle that the face is pointing relative to the vertical plane perpendicular to the image. Range [-180,180]. |  [optional] |
|**rollAngle** | **Float** | Roll angle, which indicates the amount of clockwise/anti-clockwise rotation of the face relative to the image vertical about the axis perpendicular to the face. Range [-180,180]. |  [optional] |
|**sorrowLikelihood** | [**SorrowLikelihoodEnum**](#SorrowLikelihoodEnum) | Sorrow likelihood. |  [optional] |
|**surpriseLikelihood** | [**SurpriseLikelihoodEnum**](#SurpriseLikelihoodEnum) | Surprise likelihood. |  [optional] |
|**tiltAngle** | **Float** | Pitch angle, which indicates the upwards/downwards angle that the face is pointing relative to the image&#39;s horizontal plane. Range [-180,180]. |  [optional] |
|**underExposedLikelihood** | [**UnderExposedLikelihoodEnum**](#UnderExposedLikelihoodEnum) | Under-exposed likelihood. |  [optional] |



## Enum: AngerLikelihoodEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;UNKNOWN&quot; |
| VERY_UNLIKELY | &quot;VERY_UNLIKELY&quot; |
| UNLIKELY | &quot;UNLIKELY&quot; |
| POSSIBLE | &quot;POSSIBLE&quot; |
| LIKELY | &quot;LIKELY&quot; |
| VERY_LIKELY | &quot;VERY_LIKELY&quot; |



## Enum: BlurredLikelihoodEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;UNKNOWN&quot; |
| VERY_UNLIKELY | &quot;VERY_UNLIKELY&quot; |
| UNLIKELY | &quot;UNLIKELY&quot; |
| POSSIBLE | &quot;POSSIBLE&quot; |
| LIKELY | &quot;LIKELY&quot; |
| VERY_LIKELY | &quot;VERY_LIKELY&quot; |



## Enum: HeadwearLikelihoodEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;UNKNOWN&quot; |
| VERY_UNLIKELY | &quot;VERY_UNLIKELY&quot; |
| UNLIKELY | &quot;UNLIKELY&quot; |
| POSSIBLE | &quot;POSSIBLE&quot; |
| LIKELY | &quot;LIKELY&quot; |
| VERY_LIKELY | &quot;VERY_LIKELY&quot; |



## Enum: JoyLikelihoodEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;UNKNOWN&quot; |
| VERY_UNLIKELY | &quot;VERY_UNLIKELY&quot; |
| UNLIKELY | &quot;UNLIKELY&quot; |
| POSSIBLE | &quot;POSSIBLE&quot; |
| LIKELY | &quot;LIKELY&quot; |
| VERY_LIKELY | &quot;VERY_LIKELY&quot; |



## Enum: SorrowLikelihoodEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;UNKNOWN&quot; |
| VERY_UNLIKELY | &quot;VERY_UNLIKELY&quot; |
| UNLIKELY | &quot;UNLIKELY&quot; |
| POSSIBLE | &quot;POSSIBLE&quot; |
| LIKELY | &quot;LIKELY&quot; |
| VERY_LIKELY | &quot;VERY_LIKELY&quot; |



## Enum: SurpriseLikelihoodEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;UNKNOWN&quot; |
| VERY_UNLIKELY | &quot;VERY_UNLIKELY&quot; |
| UNLIKELY | &quot;UNLIKELY&quot; |
| POSSIBLE | &quot;POSSIBLE&quot; |
| LIKELY | &quot;LIKELY&quot; |
| VERY_LIKELY | &quot;VERY_LIKELY&quot; |



## Enum: UnderExposedLikelihoodEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;UNKNOWN&quot; |
| VERY_UNLIKELY | &quot;VERY_UNLIKELY&quot; |
| UNLIKELY | &quot;UNLIKELY&quot; |
| POSSIBLE | &quot;POSSIBLE&quot; |
| LIKELY | &quot;LIKELY&quot; |
| VERY_LIKELY | &quot;VERY_LIKELY&quot; |



