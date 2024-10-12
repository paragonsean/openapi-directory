

# FaceDetail

<p>Structure containing attributes of the face that the algorithm detected.</p> <p>A <code>FaceDetail</code> object contains either the default facial attributes or all facial attributes. The default attributes are <code>BoundingBox</code>, <code>Confidence</code>, <code>Landmarks</code>, <code>Pose</code>, and <code>Quality</code>.</p> <p> <a>GetFaceDetection</a> is the only Amazon Rekognition Video stored video operation that can return a <code>FaceDetail</code> object with all attributes. To specify which attributes to return, use the <code>FaceAttributes</code> input parameter for <a>StartFaceDetection</a>. The following Amazon Rekognition Video operations return only the default attributes. The corresponding Start operations don't have a <code>FaceAttributes</code> input parameter:</p> <ul> <li> <p>GetCelebrityRecognition</p> </li> <li> <p>GetPersonTracking</p> </li> <li> <p>GetFaceSearch</p> </li> </ul> <p>The Amazon Rekognition Image <a>DetectFaces</a> and <a>IndexFaces</a> operations can return all facial attributes. To specify which attributes to return, use the <code>Attributes</code> input parameter for <code>DetectFaces</code>. For <code>IndexFaces</code>, use the <code>DetectAttributes</code> input parameter.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**boundingBox** | [**FaceDetailBoundingBox**](FaceDetailBoundingBox.md) |  |  [optional] |
|**ageRange** | [**FaceDetailAgeRange**](FaceDetailAgeRange.md) |  |  [optional] |
|**smile** | [**FaceDetailSmile**](FaceDetailSmile.md) |  |  [optional] |
|**eyeglasses** | [**FaceDetailEyeglasses**](FaceDetailEyeglasses.md) |  |  [optional] |
|**sunglasses** | [**FaceDetailSunglasses**](FaceDetailSunglasses.md) |  |  [optional] |
|**gender** | [**FaceDetailGender**](FaceDetailGender.md) |  |  [optional] |
|**beard** | [**FaceDetailBeard**](FaceDetailBeard.md) |  |  [optional] |
|**mustache** | [**FaceDetailMustache**](FaceDetailMustache.md) |  |  [optional] |
|**eyesOpen** | [**FaceDetailEyesOpen**](FaceDetailEyesOpen.md) |  |  [optional] |
|**mouthOpen** | [**FaceDetailMouthOpen**](FaceDetailMouthOpen.md) |  |  [optional] |
|**emotions** | [**List**](List.md) |  |  [optional] |
|**landmarks** | [**List**](List.md) |  |  [optional] |
|**pose** | [**FaceDetailPose**](FaceDetailPose.md) |  |  [optional] |
|**quality** | [**FaceDetailQuality**](FaceDetailQuality.md) |  |  [optional] |
|**confidence** | [**Float**](Float.md) |  |  [optional] |
|**faceOccluded** | [**FaceDetailFaceOccluded**](FaceDetailFaceOccluded.md) |  |  [optional] |
|**eyeDirection** | [**FaceDetailEyeDirection**](FaceDetailEyeDirection.md) |  |  [optional] |



