# FaceClient.DefaultApi

All URIs are relative to *https://azure.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**faceDetectWithUrl**](DefaultApi.md#faceDetectWithUrl) | **POST** /detect | 
[**faceFindSimilar**](DefaultApi.md#faceFindSimilar) | **POST** /findsimilars | 
[**faceGroup**](DefaultApi.md#faceGroup) | **POST** /group | 
[**faceIdentify**](DefaultApi.md#faceIdentify) | **POST** /identify | 
[**faceListAddFaceFromUrl**](DefaultApi.md#faceListAddFaceFromUrl) | **POST** /facelists/{faceListId}/persistedfaces | 
[**faceListCreate**](DefaultApi.md#faceListCreate) | **PUT** /facelists/{faceListId} | 
[**faceListDelete**](DefaultApi.md#faceListDelete) | **DELETE** /facelists/{faceListId} | 
[**faceListDeleteFace**](DefaultApi.md#faceListDeleteFace) | **DELETE** /facelists/{faceListId}/persistedfaces/{persistedFaceId} | 
[**faceListGet**](DefaultApi.md#faceListGet) | **GET** /facelists/{faceListId} | 
[**faceListList**](DefaultApi.md#faceListList) | **GET** /facelists | 
[**faceListUpdate**](DefaultApi.md#faceListUpdate) | **PATCH** /facelists/{faceListId} | 
[**faceVerifyFaceToFace**](DefaultApi.md#faceVerifyFaceToFace) | **POST** /verify | 
[**largeFaceListAddFaceFromUrl**](DefaultApi.md#largeFaceListAddFaceFromUrl) | **POST** /largefacelists/{largeFaceListId}/persistedfaces | 
[**largeFaceListCreate**](DefaultApi.md#largeFaceListCreate) | **PUT** /largefacelists/{largeFaceListId} | 
[**largeFaceListDelete**](DefaultApi.md#largeFaceListDelete) | **DELETE** /largefacelists/{largeFaceListId} | 
[**largeFaceListDeleteFace**](DefaultApi.md#largeFaceListDeleteFace) | **DELETE** /largefacelists/{largeFaceListId}/persistedfaces/{persistedFaceId} | 
[**largeFaceListGet**](DefaultApi.md#largeFaceListGet) | **GET** /largefacelists/{largeFaceListId} | 
[**largeFaceListGetFace**](DefaultApi.md#largeFaceListGetFace) | **GET** /largefacelists/{largeFaceListId}/persistedfaces/{persistedFaceId} | 
[**largeFaceListGetTrainingStatus**](DefaultApi.md#largeFaceListGetTrainingStatus) | **GET** /largefacelists/{largeFaceListId}/training | 
[**largeFaceListList**](DefaultApi.md#largeFaceListList) | **GET** /largefacelists | 
[**largeFaceListListFaces**](DefaultApi.md#largeFaceListListFaces) | **GET** /largefacelists/{largeFaceListId}/persistedfaces | 
[**largeFaceListTrain**](DefaultApi.md#largeFaceListTrain) | **POST** /largefacelists/{largeFaceListId}/train | 
[**largeFaceListUpdate**](DefaultApi.md#largeFaceListUpdate) | **PATCH** /largefacelists/{largeFaceListId} | 
[**largeFaceListUpdateFace**](DefaultApi.md#largeFaceListUpdateFace) | **PATCH** /largefacelists/{largeFaceListId}/persistedfaces/{persistedFaceId} | 
[**largePersonGroupCreate**](DefaultApi.md#largePersonGroupCreate) | **PUT** /largepersongroups/{largePersonGroupId} | 
[**largePersonGroupDelete**](DefaultApi.md#largePersonGroupDelete) | **DELETE** /largepersongroups/{largePersonGroupId} | 
[**largePersonGroupGet**](DefaultApi.md#largePersonGroupGet) | **GET** /largepersongroups/{largePersonGroupId} | 
[**largePersonGroupGetTrainingStatus**](DefaultApi.md#largePersonGroupGetTrainingStatus) | **GET** /largepersongroups/{largePersonGroupId}/training | 
[**largePersonGroupList**](DefaultApi.md#largePersonGroupList) | **GET** /largepersongroups | 
[**largePersonGroupPersonAddFaceFromUrl**](DefaultApi.md#largePersonGroupPersonAddFaceFromUrl) | **POST** /largepersongroups/{largePersonGroupId}/persons/{personId}/persistedfaces | 
[**largePersonGroupPersonCreate**](DefaultApi.md#largePersonGroupPersonCreate) | **POST** /largepersongroups/{largePersonGroupId}/persons | 
[**largePersonGroupPersonDelete**](DefaultApi.md#largePersonGroupPersonDelete) | **DELETE** /largepersongroups/{largePersonGroupId}/persons/{personId} | 
[**largePersonGroupPersonDeleteFace**](DefaultApi.md#largePersonGroupPersonDeleteFace) | **DELETE** /largepersongroups/{largePersonGroupId}/persons/{personId}/persistedfaces/{persistedFaceId} | 
[**largePersonGroupPersonGet**](DefaultApi.md#largePersonGroupPersonGet) | **GET** /largepersongroups/{largePersonGroupId}/persons/{personId} | 
[**largePersonGroupPersonGetFace**](DefaultApi.md#largePersonGroupPersonGetFace) | **GET** /largepersongroups/{largePersonGroupId}/persons/{personId}/persistedfaces/{persistedFaceId} | 
[**largePersonGroupPersonList**](DefaultApi.md#largePersonGroupPersonList) | **GET** /largepersongroups/{largePersonGroupId}/persons | 
[**largePersonGroupPersonUpdate**](DefaultApi.md#largePersonGroupPersonUpdate) | **PATCH** /largepersongroups/{largePersonGroupId}/persons/{personId} | 
[**largePersonGroupPersonUpdateFace**](DefaultApi.md#largePersonGroupPersonUpdateFace) | **PATCH** /largepersongroups/{largePersonGroupId}/persons/{personId}/persistedfaces/{persistedFaceId} | 
[**largePersonGroupTrain**](DefaultApi.md#largePersonGroupTrain) | **POST** /largepersongroups/{largePersonGroupId}/train | 
[**largePersonGroupUpdate**](DefaultApi.md#largePersonGroupUpdate) | **PATCH** /largepersongroups/{largePersonGroupId} | 
[**personGroupCreate**](DefaultApi.md#personGroupCreate) | **PUT** /persongroups/{personGroupId} | 
[**personGroupDelete**](DefaultApi.md#personGroupDelete) | **DELETE** /persongroups/{personGroupId} | 
[**personGroupGet**](DefaultApi.md#personGroupGet) | **GET** /persongroups/{personGroupId} | 
[**personGroupGetTrainingStatus**](DefaultApi.md#personGroupGetTrainingStatus) | **GET** /persongroups/{personGroupId}/training | 
[**personGroupList**](DefaultApi.md#personGroupList) | **GET** /persongroups | 
[**personGroupPersonAddFaceFromUrl**](DefaultApi.md#personGroupPersonAddFaceFromUrl) | **POST** /persongroups/{personGroupId}/persons/{personId}/persistedfaces | 
[**personGroupPersonCreate**](DefaultApi.md#personGroupPersonCreate) | **POST** /persongroups/{personGroupId}/persons | 
[**personGroupPersonDelete**](DefaultApi.md#personGroupPersonDelete) | **DELETE** /persongroups/{personGroupId}/persons/{personId} | 
[**personGroupPersonDeleteFace**](DefaultApi.md#personGroupPersonDeleteFace) | **DELETE** /persongroups/{personGroupId}/persons/{personId}/persistedfaces/{persistedFaceId} | 
[**personGroupPersonGet**](DefaultApi.md#personGroupPersonGet) | **GET** /persongroups/{personGroupId}/persons/{personId} | 
[**personGroupPersonGetFace**](DefaultApi.md#personGroupPersonGetFace) | **GET** /persongroups/{personGroupId}/persons/{personId}/persistedfaces/{persistedFaceId} | 
[**personGroupPersonList**](DefaultApi.md#personGroupPersonList) | **GET** /persongroups/{personGroupId}/persons | 
[**personGroupPersonUpdate**](DefaultApi.md#personGroupPersonUpdate) | **PATCH** /persongroups/{personGroupId}/persons/{personId} | 
[**personGroupPersonUpdateFace**](DefaultApi.md#personGroupPersonUpdateFace) | **PATCH** /persongroups/{personGroupId}/persons/{personId}/persistedfaces/{persistedFaceId} | 
[**personGroupTrain**](DefaultApi.md#personGroupTrain) | **POST** /persongroups/{personGroupId}/train | 
[**personGroupUpdate**](DefaultApi.md#personGroupUpdate) | **PATCH** /persongroups/{personGroupId} | 
[**snapshotApply**](DefaultApi.md#snapshotApply) | **POST** /snapshots/{snapshotId}/apply | 
[**snapshotDelete**](DefaultApi.md#snapshotDelete) | **DELETE** /snapshots/{snapshotId} | 
[**snapshotGet**](DefaultApi.md#snapshotGet) | **GET** /snapshots/{snapshotId} | 
[**snapshotGetOperationStatus**](DefaultApi.md#snapshotGetOperationStatus) | **GET** /operations/{operationId} | 
[**snapshotList**](DefaultApi.md#snapshotList) | **GET** /snapshots | 
[**snapshotTake**](DefaultApi.md#snapshotTake) | **POST** /snapshots | 
[**snapshotUpdate**](DefaultApi.md#snapshotUpdate) | **PATCH** /snapshots/{snapshotId} | 



## faceDetectWithUrl

> [DetectedFace] faceDetectWithUrl(imageUrl, opts)



Detect human faces in an image, return face rectangles, and optionally with faceIds, landmarks, and attributes.&lt;br /&gt; * No image will be stored. Only the extracted face feature will be stored on server. The faceId is an identifier of the face feature and will be used in [Face - Identify](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395239), [Face - Verify](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f3039523a), and [Face - Find Similar](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395237). The stored face feature(s) will expire and be deleted 24 hours after the original detection call. * Optional parameters include faceId, landmarks, and attributes. Attributes include age, gender, headPose, smile, facialHair, glasses, emotion, hair, makeup, occlusion, accessories, blur, exposure and noise. Some of the results returned for specific attributes may not be highly accurate. * JPEG, PNG, GIF (the first frame), and BMP format are supported. The allowed image file size is from 1KB to 6MB. * Up to 100 faces can be returned for an image. Faces are ranked by face rectangle size from large to small. * For optimal results when querying [Face - Identify](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395239), [Face - Verify](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f3039523a), and [Face - Find Similar](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395237) (&#39;returnFaceId&#39; is true), please use faces that are: frontal, clear, and with a minimum size of 200x200 pixels (100 pixels between eyes). * The minimum detectable face size is 36x36 pixels in an image no larger than 1920x1080 pixels. Images with dimensions higher than 1920x1080 pixels will need a proportionally larger minimum face size. * Different &#39;detectionModel&#39; values can be provided. To use and compare different detection models, please refer to [How to specify a detection model](https://docs.microsoft.com/en-us/azure/cognitive-services/face/face-api-how-to-topics/specify-detection-model)   | Model | Recommended use-case(s) |   | ---------- | -------- |   | &#39;detection_01&#39;: | The default detection model for [Face - Detect](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395236). Recommend for near frontal face detection. For scenarios with exceptionally large angle (head-pose) faces, occluded faces or wrong image orientation, the faces in such cases may not be detected. |   | &#39;detection_02&#39;: | Detection model released in 2019 May with improved accuracy especially on small, side and blurry faces. |  * Different &#39;recognitionModel&#39; values are provided. If follow-up operations like Verify, Identify, Find Similar are needed, please specify the recognition model with &#39;recognitionModel&#39; parameter. The default value for &#39;recognitionModel&#39; is &#39;recognition_01&#39;, if latest model needed, please explicitly specify the model you need in this parameter. Once specified, the detected faceIds will be associated with the specified recognition model. More details, please refer to [How to specify a recognition model](https://docs.microsoft.com/en-us/azure/cognitive-services/face/face-api-how-to-topics/specify-recognition-model)   | Model | Recommended use-case(s) |   | ---------- | -------- |   | &#39;recognition_01&#39;: | The default recognition model for [Face - Detect](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395236). All those faceIds created before 2019 March are bonded with this recognition model. |   | &#39;recognition_02&#39;: | Recognition model released in 2019 March. &#39;recognition_02&#39; is recommended since its overall accuracy is improved compared with &#39;recognition_01&#39;. |

### Example

```javascript
import FaceClient from 'face_client';
let defaultClient = FaceClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FaceClient.DefaultApi();
let imageUrl = new FaceClient.FaceDetectWithUrlRequest(); // FaceDetectWithUrlRequest | A JSON document with a URL pointing to the image that is to be analyzed.
let opts = {
  'returnFaceId': true, // Boolean | A value indicating whether the operation should return faceIds of detected faces.
  'returnFaceLandmarks': false, // Boolean | A value indicating whether the operation should return landmarks of the detected faces.
  'returnFaceAttributes': ["null"], // [String] | Analyze and return the one or more specified face attributes in the comma-separated string like \"returnFaceAttributes=age,gender\". Supported face attributes include age, gender, headPose, smile, facialHair, glasses and emotion. Note that each face attribute analysis has additional computational and time cost.
  'recognitionModel': "'recognition_01'", // String | Name of recognition model. Recognition model is used when the face features are extracted and associated with detected faceIds, (Large)FaceList or (Large)PersonGroup. A recognition model name can be provided when performing Face - Detect or (Large)FaceList - Create or (Large)PersonGroup - Create. The default value is 'recognition_01', if latest model needed, please explicitly specify the model you need.
  'returnRecognitionModel': false, // Boolean | A value indicating whether the operation should return 'recognitionModel' in response.
  'detectionModel': "'detection_01'" // String | Name of detection model. Detection model is used to detect faces in the submitted image. A detection model name can be provided when performing Face - Detect or (Large)FaceList - Add Face or (Large)PersonGroup - Add Face. The default value is 'detection_01', if another model is needed, please explicitly specify it.
};
apiInstance.faceDetectWithUrl(imageUrl, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imageUrl** | [**FaceDetectWithUrlRequest**](FaceDetectWithUrlRequest.md)| A JSON document with a URL pointing to the image that is to be analyzed. | 
 **returnFaceId** | **Boolean**| A value indicating whether the operation should return faceIds of detected faces. | [optional] [default to true]
 **returnFaceLandmarks** | **Boolean**| A value indicating whether the operation should return landmarks of the detected faces. | [optional] [default to false]
 **returnFaceAttributes** | [**[String]**](String.md)| Analyze and return the one or more specified face attributes in the comma-separated string like \&quot;returnFaceAttributes&#x3D;age,gender\&quot;. Supported face attributes include age, gender, headPose, smile, facialHair, glasses and emotion. Note that each face attribute analysis has additional computational and time cost. | [optional] 
 **recognitionModel** | **String**| Name of recognition model. Recognition model is used when the face features are extracted and associated with detected faceIds, (Large)FaceList or (Large)PersonGroup. A recognition model name can be provided when performing Face - Detect or (Large)FaceList - Create or (Large)PersonGroup - Create. The default value is &#39;recognition_01&#39;, if latest model needed, please explicitly specify the model you need. | [optional] [default to &#39;recognition_01&#39;]
 **returnRecognitionModel** | **Boolean**| A value indicating whether the operation should return &#39;recognitionModel&#39; in response. | [optional] [default to false]
 **detectionModel** | **String**| Name of detection model. Detection model is used to detect faces in the submitted image. A detection model name can be provided when performing Face - Detect or (Large)FaceList - Add Face or (Large)PersonGroup - Add Face. The default value is &#39;detection_01&#39;, if another model is needed, please explicitly specify it. | [optional] [default to &#39;detection_01&#39;]

### Return type

[**[DetectedFace]**](DetectedFace.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## faceFindSimilar

> [SimilarFace] faceFindSimilar(body)



Given query face&#39;s faceId, to search the similar-looking faces from a faceId array, a face list or a large face list. faceId array contains the faces created by [Face - Detect](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395236), which will expire 24 hours after creation. A \&quot;faceListId\&quot; is created by [FaceList - Create](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f3039524b) containing persistedFaceIds that will not expire. And a \&quot;largeFaceListId\&quot; is created by [LargeFaceList - Create](/docs/services/563879b61984550e40cbbe8d/operations/5a157b68d2de3616c086f2cc) containing persistedFaceIds that will also not expire. Depending on the input the returned similar faces list contains faceIds or persistedFaceIds ranked by similarity. &lt;br/&gt;Find similar has two working modes, \&quot;matchPerson\&quot; and \&quot;matchFace\&quot;. \&quot;matchPerson\&quot; is the default mode that it tries to find faces of the same person as possible by using internal same-person thresholds. It is useful to find a known person&#39;s other photos. Note that an empty list will be returned if no faces pass the internal thresholds. \&quot;matchFace\&quot; mode ignores same-person thresholds and returns ranked similar faces anyway, even the similarity is low. It can be used in the cases like searching celebrity-looking faces. &lt;br/&gt;The &#39;recognitionModel&#39; associated with the query face&#39;s faceId should be the same as the &#39;recognitionModel&#39; used by the target faceId array, face list or large face list. 

### Example

```javascript
import FaceClient from 'face_client';
let defaultClient = FaceClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FaceClient.DefaultApi();
let body = new FaceClient.FindSimilarRequest(); // FindSimilarRequest | Request body for Find Similar.
apiInstance.faceFindSimilar(body, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FindSimilarRequest**](FindSimilarRequest.md)| Request body for Find Similar. | 

### Return type

[**[SimilarFace]**](SimilarFace.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## faceGroup

> GroupResult faceGroup(body)



Divide candidate faces into groups based on face similarity.&lt;br /&gt; * The output is one or more disjointed face groups and a messyGroup. A face group contains faces that have similar looking, often of the same person. Face groups are ranked by group size, i.e. number of faces. Notice that faces belonging to a same person might be split into several groups in the result. * MessyGroup is a special face group containing faces that cannot find any similar counterpart face from original faces. The messyGroup will not appear in the result if all faces found their counterparts. * Group API needs at least 2 candidate faces and 1000 at most. We suggest to try [Face - Verify](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f3039523a) when you only have 2 candidate faces. * The &#39;recognitionModel&#39; associated with the query faces&#39; faceIds should be the same. 

### Example

```javascript
import FaceClient from 'face_client';
let defaultClient = FaceClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FaceClient.DefaultApi();
let body = new FaceClient.GroupRequest(); // GroupRequest | Request body for grouping.
apiInstance.faceGroup(body, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GroupRequest**](GroupRequest.md)| Request body for grouping. | 

### Return type

[**GroupResult**](GroupResult.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## faceIdentify

> [IdentifyResult] faceIdentify(body)



1-to-many identification to find the closest matches of the specific query person face from a person group or large person group. &lt;br/&gt; For each face in the faceIds array, Face Identify will compute similarities between the query face and all the faces in the person group (given by personGroupId) or large person group (given by largePersonGroupId), and return candidate person(s) for that face ranked by similarity confidence. The person group/large person group should be trained to make it ready for identification. See more in [PersonGroup - Train](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395249) and [LargePersonGroup - Train](/docs/services/563879b61984550e40cbbe8d/operations/599ae2d16ac60f11b48b5aa4). &lt;br/&gt;   Remarks:&lt;br /&gt; * The algorithm allows more than one face to be identified independently at the same request, but no more than 10 faces. * Each person in the person group/large person group could have more than one face, but no more than 248 faces. * Higher face image quality means better identification precision. Please consider high-quality faces: frontal, clear, and face size is 200x200 pixels (100 pixels between eyes) or bigger. * Number of candidates returned is restricted by maxNumOfCandidatesReturned and confidenceThreshold. If no person is identified, the returned candidates will be an empty array. * Try [Face - Find Similar](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395237) when you need to find similar faces from a face list/large face list instead of a person group/large person group. * The &#39;recognitionModel&#39; associated with the query faces&#39; faceIds should be the same as the &#39;recognitionModel&#39; used by the target person group or large person group. 

### Example

```javascript
import FaceClient from 'face_client';
let defaultClient = FaceClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FaceClient.DefaultApi();
let body = new FaceClient.IdentifyRequest(); // IdentifyRequest | Request body for identify operation.
apiInstance.faceIdentify(body, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IdentifyRequest**](IdentifyRequest.md)| Request body for identify operation. | 

### Return type

[**[IdentifyResult]**](IdentifyResult.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## faceListAddFaceFromUrl

> PersistedFace faceListAddFaceFromUrl(faceListId, imageUrl, opts)



Add a face to a specified face list, up to 1,000 faces. &lt;br /&gt; To deal with an image contains multiple faces, input face can be specified as an image with a targetFace rectangle. It returns a persistedFaceId representing the added face. No image will be stored. Only the extracted face feature will be stored on server until [FaceList - Delete Face](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395251) or [FaceList - Delete](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f3039524f) is called. &lt;br /&gt; Note persistedFaceId is different from faceId generated by [Face - Detect](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395236). * Higher face image quality means better detection and recognition precision. Please consider high-quality faces: frontal, clear, and face size is 200x200 pixels (100 pixels between eyes) or bigger. * JPEG, PNG, GIF (the first frame), and BMP format are supported. The allowed image file size is from 1KB to 6MB. * \&quot;targetFace\&quot; rectangle should contain one face. Zero or multiple faces will be regarded as an error. If the provided \&quot;targetFace\&quot; rectangle is not returned from [Face - Detect](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395236), there’s no guarantee to detect and add the face successfully. * Out of detectable face size (36x36 - 4096x4096 pixels), large head-pose, or large occlusions will cause failures. * Adding/deleting faces to/from a same face list are processed sequentially and to/from different face lists are in parallel. * The minimum detectable face size is 36x36 pixels in an image no larger than 1920x1080 pixels. Images with dimensions higher than 1920x1080 pixels will need a proportionally larger minimum face size. * Different &#39;detectionModel&#39; values can be provided. To use and compare different detection models, please refer to [How to specify a detection model](https://docs.microsoft.com/en-us/azure/cognitive-services/face/face-api-how-to-topics/specify-detection-model)   | Model | Recommended use-case(s) |   | ---------- | -------- |   | &#39;detection_01&#39;: | The default detection model for [FaceList - Add Face](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395250). Recommend for near frontal face detection. For scenarios with exceptionally large angle (head-pose) faces, occluded faces or wrong image orientation, the faces in such cases may not be detected. |   | &#39;detection_02&#39;: | Detection model released in 2019 May with improved accuracy especially on small, side and blurry faces. |

### Example

```javascript
import FaceClient from 'face_client';
let defaultClient = FaceClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FaceClient.DefaultApi();
let faceListId = "faceListId_example"; // String | Id referencing a particular face list.
let imageUrl = new FaceClient.FaceDetectWithUrlRequest(); // FaceDetectWithUrlRequest | A JSON document with a URL pointing to the image that is to be analyzed.
let opts = {
  'userData': "userData_example", // String | User-specified data about the face for any purpose. The maximum length is 1KB.
  'targetFace': [null], // [Number] | A face rectangle to specify the target face to be added to a person in the format of \"targetFace=left,top,width,height\". E.g. \"targetFace=10,10,100,100\". If there is more than one face in the image, targetFace is required to specify which face to add. No targetFace means there is only one face detected in the entire image.
  'detectionModel': "'detection_01'" // String | Name of detection model. Detection model is used to detect faces in the submitted image. A detection model name can be provided when performing Face - Detect or (Large)FaceList - Add Face or (Large)PersonGroup - Add Face. The default value is 'detection_01', if another model is needed, please explicitly specify it.
};
apiInstance.faceListAddFaceFromUrl(faceListId, imageUrl, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **faceListId** | **String**| Id referencing a particular face list. | 
 **imageUrl** | [**FaceDetectWithUrlRequest**](FaceDetectWithUrlRequest.md)| A JSON document with a URL pointing to the image that is to be analyzed. | 
 **userData** | **String**| User-specified data about the face for any purpose. The maximum length is 1KB. | [optional] 
 **targetFace** | [**[Number]**](Number.md)| A face rectangle to specify the target face to be added to a person in the format of \&quot;targetFace&#x3D;left,top,width,height\&quot;. E.g. \&quot;targetFace&#x3D;10,10,100,100\&quot;. If there is more than one face in the image, targetFace is required to specify which face to add. No targetFace means there is only one face detected in the entire image. | [optional] 
 **detectionModel** | **String**| Name of detection model. Detection model is used to detect faces in the submitted image. A detection model name can be provided when performing Face - Detect or (Large)FaceList - Add Face or (Large)PersonGroup - Add Face. The default value is &#39;detection_01&#39;, if another model is needed, please explicitly specify it. | [optional] [default to &#39;detection_01&#39;]

### Return type

[**PersistedFace**](PersistedFace.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## faceListCreate

> faceListCreate(faceListId, body)



Create an empty face list with user-specified faceListId, name, an optional userData and recognitionModel. Up to 64 face lists are allowed in one subscription. &lt;br /&gt; Face list is a list of faces, up to 1,000 faces, and used by [Face - Find Similar](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395237). &lt;br /&gt; After creation, user should use [FaceList - Add Face](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395250) to import the faces. No image will be stored. Only the extracted face features are stored on server until [FaceList - Delete](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f3039524f) is called. &lt;br /&gt; Find Similar is used for scenario like finding celebrity-like faces, similar face filtering, or as a light way face identification. But if the actual use is to identify person, please use [PersonGroup](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395244) / [LargePersonGroup](/docs/services/563879b61984550e40cbbe8d/operations/599acdee6ac60f11b48b5a9d) and [Face - Identify](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395239). &lt;br /&gt; Please consider [LargeFaceList](/docs/services/563879b61984550e40cbbe8d/operations/5a157b68d2de3616c086f2cc) when the face number is large. It can support up to 1,000,000 faces. &lt;br /&gt;&#39;recognitionModel&#39; should be specified to associate with this face list. The default value for &#39;recognitionModel&#39; is &#39;recognition_01&#39;, if the latest model needed, please explicitly specify the model you need in this parameter. New faces that are added to an existing face list will use the recognition model that&#39;s already associated with the collection. Existing face features in a face list can&#39;t be updated to features extracted by another version of recognition model. * &#39;recognition_01&#39;: The default recognition model for [FaceList- Create](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f3039524b). All those face lists created before 2019 March are bonded with this recognition model. * &#39;recognition_02&#39;: Recognition model released in 2019 March. &#39;recognition_02&#39; is recommended since its overall accuracy is improved compared with &#39;recognition_01&#39;.

### Example

```javascript
import FaceClient from 'face_client';
let defaultClient = FaceClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FaceClient.DefaultApi();
let faceListId = "faceListId_example"; // String | Id referencing a particular face list.
let body = new FaceClient.MetaDataContract(); // MetaDataContract | Request body for creating a face list.
apiInstance.faceListCreate(faceListId, body, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **faceListId** | **String**| Id referencing a particular face list. | 
 **body** | [**MetaDataContract**](MetaDataContract.md)| Request body for creating a face list. | 

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## faceListDelete

> faceListDelete(faceListId)



Delete a specified face list.

### Example

```javascript
import FaceClient from 'face_client';
let defaultClient = FaceClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FaceClient.DefaultApi();
let faceListId = "faceListId_example"; // String | Id referencing a particular face list.
apiInstance.faceListDelete(faceListId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **faceListId** | **String**| Id referencing a particular face list. | 

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## faceListDeleteFace

> faceListDeleteFace(faceListId, persistedFaceId)



Delete a face from a face list by specified faceListId and persistedFaceId. &lt;br /&gt; Adding/deleting faces to/from a same face list are processed sequentially and to/from different face lists are in parallel.

### Example

```javascript
import FaceClient from 'face_client';
let defaultClient = FaceClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FaceClient.DefaultApi();
let faceListId = "faceListId_example"; // String | Id referencing a particular face list.
let persistedFaceId = "persistedFaceId_example"; // String | Id referencing a particular persistedFaceId of an existing face.
apiInstance.faceListDeleteFace(faceListId, persistedFaceId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **faceListId** | **String**| Id referencing a particular face list. | 
 **persistedFaceId** | **String**| Id referencing a particular persistedFaceId of an existing face. | 

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## faceListGet

> FaceList faceListGet(faceListId, opts)



Retrieve a face list’s faceListId, name, userData, recognitionModel and faces in the face list. 

### Example

```javascript
import FaceClient from 'face_client';
let defaultClient = FaceClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FaceClient.DefaultApi();
let faceListId = "faceListId_example"; // String | Id referencing a particular face list.
let opts = {
  'returnRecognitionModel': false // Boolean | A value indicating whether the operation should return 'recognitionModel' in response.
};
apiInstance.faceListGet(faceListId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **faceListId** | **String**| Id referencing a particular face list. | 
 **returnRecognitionModel** | **Boolean**| A value indicating whether the operation should return &#39;recognitionModel&#39; in response. | [optional] [default to false]

### Return type

[**FaceList**](FaceList.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## faceListList

> [FaceList] faceListList(opts)



List face lists’ faceListId, name, userData and recognitionModel. &lt;br /&gt;  To get face information inside faceList use [FaceList - Get](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f3039524c) 

### Example

```javascript
import FaceClient from 'face_client';
let defaultClient = FaceClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FaceClient.DefaultApi();
let opts = {
  'returnRecognitionModel': false // Boolean | A value indicating whether the operation should return 'recognitionModel' in response.
};
apiInstance.faceListList(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **returnRecognitionModel** | **Boolean**| A value indicating whether the operation should return &#39;recognitionModel&#39; in response. | [optional] [default to false]

### Return type

[**[FaceList]**](FaceList.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## faceListUpdate

> faceListUpdate(faceListId, body)



Update information of a face list.

### Example

```javascript
import FaceClient from 'face_client';
let defaultClient = FaceClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FaceClient.DefaultApi();
let faceListId = "faceListId_example"; // String | Id referencing a particular face list.
let body = new FaceClient.NameAndUserDataContract(); // NameAndUserDataContract | Request body for updating a face list.
apiInstance.faceListUpdate(faceListId, body, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **faceListId** | **String**| Id referencing a particular face list. | 
 **body** | [**NameAndUserDataContract**](NameAndUserDataContract.md)| Request body for updating a face list. | 

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## faceVerifyFaceToFace

> VerifyResult faceVerifyFaceToFace(body)



Verify whether two faces belong to a same person or whether one face belongs to a person. &lt;br/&gt; Remarks:&lt;br /&gt; * Higher face image quality means better identification precision. Please consider high-quality faces: frontal, clear, and face size is 200x200 pixels (100 pixels between eyes) or bigger. * For the scenarios that are sensitive to accuracy please make your own judgment. * The &#39;recognitionModel&#39; associated with the query faces&#39; faceIds should be the same as the &#39;recognitionModel&#39; used by the target face, person group or large person group. 

### Example

```javascript
import FaceClient from 'face_client';
let defaultClient = FaceClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FaceClient.DefaultApi();
let body = new FaceClient.VerifyFaceToFaceRequest(); // VerifyFaceToFaceRequest | Request body for face to face verification.
apiInstance.faceVerifyFaceToFace(body, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VerifyFaceToFaceRequest**](VerifyFaceToFaceRequest.md)| Request body for face to face verification. | 

### Return type

[**VerifyResult**](VerifyResult.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## largeFaceListAddFaceFromUrl

> PersistedFace largeFaceListAddFaceFromUrl(largeFaceListId, imageUrl, opts)



Add a face to a specified large face list, up to 1,000,000 faces. &lt;br /&gt; To deal with an image contains multiple faces, input face can be specified as an image with a targetFace rectangle. It returns a persistedFaceId representing the added face. No image will be stored. Only the extracted face feature will be stored on server until [LargeFaceList Face - Delete](/docs/services/563879b61984550e40cbbe8d/operations/5a158c8ad2de3616c086f2d4) or [LargeFaceList - Delete](/docs/services/563879b61984550e40cbbe8d/operations/5a1580d5d2de3616c086f2cd) is called. &lt;br /&gt; Note persistedFaceId is different from faceId generated by [Face - Detect](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395236). * Higher face image quality means better recognition precision. Please consider high-quality faces: frontal, clear, and face size is 200x200 pixels (100 pixels between eyes) or bigger. * JPEG, PNG, GIF (the first frame), and BMP format are supported. The allowed image file size is from 1KB to 6MB. * \&quot;targetFace\&quot; rectangle should contain one face. Zero or multiple faces will be regarded as an error. If the provided \&quot;targetFace\&quot; rectangle is not returned from [Face - Detect](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395236), there’s no guarantee to detect and add the face successfully. * Out of detectable face size (36x36 - 4096x4096 pixels), large head-pose, or large occlusions will cause failures. * Adding/deleting faces to/from a same face list are processed sequentially and to/from different face lists are in parallel. * The minimum detectable face size is 36x36 pixels in an image no larger than 1920x1080 pixels. Images with dimensions higher than 1920x1080 pixels will need a proportionally larger minimum face size. * Different &#39;detectionModel&#39; values can be provided. To use and compare different detection models, please refer to [How to specify a detection model](https://docs.microsoft.com/en-us/azure/cognitive-services/face/face-api-how-to-topics/specify-detection-model)   | Model | Recommended use-case(s) |   | ---------- | -------- |   | &#39;detection_01&#39;: | The default detection model for [LargeFaceList - Add Face](/docs/services/563879b61984550e40cbbe8d/operations/5a158c10d2de3616c086f2d3). Recommend for near frontal face detection. For scenarios with exceptionally large angle (head-pose) faces, occluded faces or wrong image orientation, the faces in such cases may not be detected. |   | &#39;detection_02&#39;: | Detection model released in 2019 May with improved accuracy especially on small, side and blurry faces. |  Quota: * Free-tier subscription quota: 1,000 faces per large face list. * S0-tier subscription quota: 1,000,000 faces per large face list.

### Example

```javascript
import FaceClient from 'face_client';
let defaultClient = FaceClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FaceClient.DefaultApi();
let largeFaceListId = "largeFaceListId_example"; // String | Id referencing a particular large face list.
let imageUrl = new FaceClient.FaceDetectWithUrlRequest(); // FaceDetectWithUrlRequest | A JSON document with a URL pointing to the image that is to be analyzed.
let opts = {
  'userData': "userData_example", // String | User-specified data about the face for any purpose. The maximum length is 1KB.
  'targetFace': [null], // [Number] | A face rectangle to specify the target face to be added to a person in the format of \"targetFace=left,top,width,height\". E.g. \"targetFace=10,10,100,100\". If there is more than one face in the image, targetFace is required to specify which face to add. No targetFace means there is only one face detected in the entire image.
  'detectionModel': "'detection_01'" // String | Name of detection model. Detection model is used to detect faces in the submitted image. A detection model name can be provided when performing Face - Detect or (Large)FaceList - Add Face or (Large)PersonGroup - Add Face. The default value is 'detection_01', if another model is needed, please explicitly specify it.
};
apiInstance.largeFaceListAddFaceFromUrl(largeFaceListId, imageUrl, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **largeFaceListId** | **String**| Id referencing a particular large face list. | 
 **imageUrl** | [**FaceDetectWithUrlRequest**](FaceDetectWithUrlRequest.md)| A JSON document with a URL pointing to the image that is to be analyzed. | 
 **userData** | **String**| User-specified data about the face for any purpose. The maximum length is 1KB. | [optional] 
 **targetFace** | [**[Number]**](Number.md)| A face rectangle to specify the target face to be added to a person in the format of \&quot;targetFace&#x3D;left,top,width,height\&quot;. E.g. \&quot;targetFace&#x3D;10,10,100,100\&quot;. If there is more than one face in the image, targetFace is required to specify which face to add. No targetFace means there is only one face detected in the entire image. | [optional] 
 **detectionModel** | **String**| Name of detection model. Detection model is used to detect faces in the submitted image. A detection model name can be provided when performing Face - Detect or (Large)FaceList - Add Face or (Large)PersonGroup - Add Face. The default value is &#39;detection_01&#39;, if another model is needed, please explicitly specify it. | [optional] [default to &#39;detection_01&#39;]

### Return type

[**PersistedFace**](PersistedFace.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## largeFaceListCreate

> largeFaceListCreate(largeFaceListId, body)



Create an empty large face list with user-specified largeFaceListId, name, an optional userData and recognitionModel. &lt;br /&gt; Large face list is a list of faces, up to 1,000,000 faces, and used by [Face - Find Similar](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395237). &lt;br /&gt; After creation, user should use [LargeFaceList Face - Add](/docs/services/563879b61984550e40cbbe8d/operations/5a158c10d2de3616c086f2d3) to import the faces and [LargeFaceList - Train](/docs/services/563879b61984550e40cbbe8d/operations/5a158422d2de3616c086f2d1) to make it ready for [Face - Find Similar](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395237). No image will be stored. Only the extracted face features are stored on server until [LargeFaceList - Delete](/docs/services/563879b61984550e40cbbe8d/operations/5a1580d5d2de3616c086f2cd) is called. &lt;br /&gt; Find Similar is used for scenario like finding celebrity-like faces, similar face filtering, or as a light way face identification. But if the actual use is to identify person, please use [PersonGroup](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395244) / [LargePersonGroup](/docs/services/563879b61984550e40cbbe8d/operations/599acdee6ac60f11b48b5a9d) and [Face - Identify](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395239). &lt;br/&gt;&#39;recognitionModel&#39; should be specified to associate with this large face list. The default value for &#39;recognitionModel&#39; is &#39;recognition_01&#39;, if the latest model needed, please explicitly specify the model you need in this parameter. New faces that are added to an existing large face list will use the recognition model that&#39;s already associated with the collection. Existing face features in a large face list can&#39;t be updated to features extracted by another version of recognition model. * &#39;recognition_01&#39;: The default recognition model for [LargeFaceList- Create](/docs/services/563879b61984550e40cbbe8d/operations/5a157b68d2de3616c086f2cc). All those large face lists created before 2019 March are bonded with this recognition model. * &#39;recognition_02&#39;: Recognition model released in 2019 March. &#39;recognition_02&#39; is recommended since its overall accuracy is improved compared with &#39;recognition_01&#39;.  Large face list quota: * Free-tier subscription quota: 64 large face lists. * S0-tier subscription quota: 1,000,000 large face lists.

### Example

```javascript
import FaceClient from 'face_client';
let defaultClient = FaceClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FaceClient.DefaultApi();
let largeFaceListId = "largeFaceListId_example"; // String | Id referencing a particular large face list.
let body = new FaceClient.MetaDataContract(); // MetaDataContract | Request body for creating a large face list.
apiInstance.largeFaceListCreate(largeFaceListId, body, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **largeFaceListId** | **String**| Id referencing a particular large face list. | 
 **body** | [**MetaDataContract**](MetaDataContract.md)| Request body for creating a large face list. | 

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## largeFaceListDelete

> largeFaceListDelete(largeFaceListId)



Delete a specified large face list.

### Example

```javascript
import FaceClient from 'face_client';
let defaultClient = FaceClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FaceClient.DefaultApi();
let largeFaceListId = "largeFaceListId_example"; // String | Id referencing a particular large face list.
apiInstance.largeFaceListDelete(largeFaceListId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **largeFaceListId** | **String**| Id referencing a particular large face list. | 

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## largeFaceListDeleteFace

> largeFaceListDeleteFace(largeFaceListId, persistedFaceId)



Delete a face from a large face list by specified largeFaceListId and persistedFaceId. &lt;br /&gt; Adding/deleting faces to/from a same large face list are processed sequentially and to/from different large face lists are in parallel.

### Example

```javascript
import FaceClient from 'face_client';
let defaultClient = FaceClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FaceClient.DefaultApi();
let largeFaceListId = "largeFaceListId_example"; // String | Id referencing a particular large face list.
let persistedFaceId = "persistedFaceId_example"; // String | Id referencing a particular persistedFaceId of an existing face.
apiInstance.largeFaceListDeleteFace(largeFaceListId, persistedFaceId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **largeFaceListId** | **String**| Id referencing a particular large face list. | 
 **persistedFaceId** | **String**| Id referencing a particular persistedFaceId of an existing face. | 

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## largeFaceListGet

> LargeFaceList largeFaceListGet(largeFaceListId, opts)



Retrieve a large face list’s largeFaceListId, name, userData and recognitionModel.

### Example

```javascript
import FaceClient from 'face_client';
let defaultClient = FaceClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FaceClient.DefaultApi();
let largeFaceListId = "largeFaceListId_example"; // String | Id referencing a particular large face list.
let opts = {
  'returnRecognitionModel': false // Boolean | A value indicating whether the operation should return 'recognitionModel' in response.
};
apiInstance.largeFaceListGet(largeFaceListId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **largeFaceListId** | **String**| Id referencing a particular large face list. | 
 **returnRecognitionModel** | **Boolean**| A value indicating whether the operation should return &#39;recognitionModel&#39; in response. | [optional] [default to false]

### Return type

[**LargeFaceList**](LargeFaceList.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## largeFaceListGetFace

> PersistedFace largeFaceListGetFace(largeFaceListId, persistedFaceId)



Retrieve information about a persisted face (specified by persistedFaceId and its belonging largeFaceListId).

### Example

```javascript
import FaceClient from 'face_client';
let defaultClient = FaceClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FaceClient.DefaultApi();
let largeFaceListId = "largeFaceListId_example"; // String | Id referencing a particular large face list.
let persistedFaceId = "persistedFaceId_example"; // String | Id referencing a particular persistedFaceId of an existing face.
apiInstance.largeFaceListGetFace(largeFaceListId, persistedFaceId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **largeFaceListId** | **String**| Id referencing a particular large face list. | 
 **persistedFaceId** | **String**| Id referencing a particular persistedFaceId of an existing face. | 

### Return type

[**PersistedFace**](PersistedFace.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## largeFaceListGetTrainingStatus

> TrainingStatus largeFaceListGetTrainingStatus(largeFaceListId)



Retrieve the training status of a large face list (completed or ongoing).

### Example

```javascript
import FaceClient from 'face_client';
let defaultClient = FaceClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FaceClient.DefaultApi();
let largeFaceListId = "largeFaceListId_example"; // String | Id referencing a particular large face list.
apiInstance.largeFaceListGetTrainingStatus(largeFaceListId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **largeFaceListId** | **String**| Id referencing a particular large face list. | 

### Return type

[**TrainingStatus**](TrainingStatus.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## largeFaceListList

> [LargeFaceList] largeFaceListList(opts)



List large face lists’ information of largeFaceListId, name, userData and recognitionModel. &lt;br /&gt;  To get face information inside largeFaceList use [LargeFaceList Face - Get](/docs/services/563879b61984550e40cbbe8d/operations/5a158cf2d2de3616c086f2d5)&lt;br /&gt; * Large face lists are stored in alphabetical order of largeFaceListId. * \&quot;start\&quot; parameter (string, optional) is a user-provided largeFaceListId value that returned entries have larger ids by string comparison. \&quot;start\&quot; set to empty to indicate return from the first item. * \&quot;top\&quot; parameter (int, optional) specifies the number of entries to return. A maximal of 1000 entries can be returned in one call. To fetch more, you can specify \&quot;start\&quot; with the last returned entry’s Id of the current call. &lt;br /&gt; For example, total 5 large person lists: \&quot;list1\&quot;, ..., \&quot;list5\&quot;. &lt;br /&gt; \&quot;start&#x3D;&amp;top&#x3D;\&quot; will return all 5 lists. &lt;br /&gt; \&quot;start&#x3D;&amp;top&#x3D;2\&quot; will return \&quot;list1\&quot;, \&quot;list2\&quot;. &lt;br /&gt; \&quot;start&#x3D;list2&amp;top&#x3D;3\&quot; will return \&quot;list3\&quot;, \&quot;list4\&quot;, \&quot;list5\&quot;. 

### Example

```javascript
import FaceClient from 'face_client';
let defaultClient = FaceClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FaceClient.DefaultApi();
let opts = {
  'returnRecognitionModel': false // Boolean | A value indicating whether the operation should return 'recognitionModel' in response.
};
apiInstance.largeFaceListList(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **returnRecognitionModel** | **Boolean**| A value indicating whether the operation should return &#39;recognitionModel&#39; in response. | [optional] [default to false]

### Return type

[**[LargeFaceList]**](LargeFaceList.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## largeFaceListListFaces

> [PersistedFace] largeFaceListListFaces(largeFaceListId, opts)



List all faces in a large face list, and retrieve face information (including userData and persistedFaceIds of registered faces of the face).

### Example

```javascript
import FaceClient from 'face_client';
let defaultClient = FaceClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FaceClient.DefaultApi();
let largeFaceListId = "largeFaceListId_example"; // String | Id referencing a particular large face list.
let opts = {
  'start': "start_example", // String | Starting face id to return (used to list a range of faces).
  'top': 56 // Number | Number of faces to return starting with the face id indicated by the 'start' parameter.
};
apiInstance.largeFaceListListFaces(largeFaceListId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **largeFaceListId** | **String**| Id referencing a particular large face list. | 
 **start** | **String**| Starting face id to return (used to list a range of faces). | [optional] 
 **top** | **Number**| Number of faces to return starting with the face id indicated by the &#39;start&#39; parameter. | [optional] 

### Return type

[**[PersistedFace]**](PersistedFace.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## largeFaceListTrain

> largeFaceListTrain(largeFaceListId)



Queue a large face list training task, the training task may not be started immediately.

### Example

```javascript
import FaceClient from 'face_client';
let defaultClient = FaceClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FaceClient.DefaultApi();
let largeFaceListId = "largeFaceListId_example"; // String | Id referencing a particular large face list.
apiInstance.largeFaceListTrain(largeFaceListId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **largeFaceListId** | **String**| Id referencing a particular large face list. | 

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## largeFaceListUpdate

> largeFaceListUpdate(largeFaceListId, body)



Update information of a large face list.

### Example

```javascript
import FaceClient from 'face_client';
let defaultClient = FaceClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FaceClient.DefaultApi();
let largeFaceListId = "largeFaceListId_example"; // String | Id referencing a particular large face list.
let body = new FaceClient.NameAndUserDataContract(); // NameAndUserDataContract | Request body for updating a large face list.
apiInstance.largeFaceListUpdate(largeFaceListId, body, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **largeFaceListId** | **String**| Id referencing a particular large face list. | 
 **body** | [**NameAndUserDataContract**](NameAndUserDataContract.md)| Request body for updating a large face list. | 

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## largeFaceListUpdateFace

> largeFaceListUpdateFace(largeFaceListId, persistedFaceId, body)



Update a persisted face&#39;s userData field.

### Example

```javascript
import FaceClient from 'face_client';
let defaultClient = FaceClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FaceClient.DefaultApi();
let largeFaceListId = "largeFaceListId_example"; // String | Id referencing a particular large face list.
let persistedFaceId = "persistedFaceId_example"; // String | Id referencing a particular persistedFaceId of an existing face.
let body = new FaceClient.UpdateFaceRequest(); // UpdateFaceRequest | Request body for updating persisted face.
apiInstance.largeFaceListUpdateFace(largeFaceListId, persistedFaceId, body, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **largeFaceListId** | **String**| Id referencing a particular large face list. | 
 **persistedFaceId** | **String**| Id referencing a particular persistedFaceId of an existing face. | 
 **body** | [**UpdateFaceRequest**](UpdateFaceRequest.md)| Request body for updating persisted face. | 

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## largePersonGroupCreate

> largePersonGroupCreate(largePersonGroupId, body)



Create a new large person group with user-specified largePersonGroupId, name, an optional userData and recognitionModel. &lt;br /&gt; A large person group is the container of the uploaded person data, including face recognition feature, and up to 1,000,000 people. &lt;br /&gt; After creation, use [LargePersonGroup Person - Create](/docs/services/563879b61984550e40cbbe8d/operations/599adcba3a7b9412a4d53f40) to add person into the group, and call [LargePersonGroup - Train](/docs/services/563879b61984550e40cbbe8d/operations/599ae2d16ac60f11b48b5aa4) to get this group ready for [Face - Identify](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395239). &lt;br /&gt; No image will be stored. Only the person&#39;s extracted face features and userData will be stored on server until [LargePersonGroup Person - Delete](/docs/services/563879b61984550e40cbbe8d/operations/599ade5c6ac60f11b48b5aa2) or [LargePersonGroup - Delete](/docs/services/563879b61984550e40cbbe8d/operations/599adc216ac60f11b48b5a9f) is called. &lt;br/&gt;&#39;recognitionModel&#39; should be specified to associate with this large person group. The default value for &#39;recognitionModel&#39; is &#39;recognition_01&#39;, if the latest model needed, please explicitly specify the model you need in this parameter. New faces that are added to an existing large person group will use the recognition model that&#39;s already associated with the collection. Existing face features in a large person group can&#39;t be updated to features extracted by another version of recognition model. * &#39;recognition_01&#39;: The default recognition model for [LargePersonGroup - Create](/docs/services/563879b61984550e40cbbe8d/operations/599acdee6ac60f11b48b5a9d). All those large person groups created before 2019 March are bonded with this recognition model. * &#39;recognition_02&#39;: Recognition model released in 2019 March. &#39;recognition_02&#39; is recommended since its overall accuracy is improved compared with &#39;recognition_01&#39;.  Large person group quota: * Free-tier subscription quota: 1,000 large person groups. * S0-tier subscription quota: 1,000,000 large person groups.

### Example

```javascript
import FaceClient from 'face_client';
let defaultClient = FaceClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FaceClient.DefaultApi();
let largePersonGroupId = "largePersonGroupId_example"; // String | Id referencing a particular large person group.
let body = new FaceClient.MetaDataContract(); // MetaDataContract | Request body for creating new large person group.
apiInstance.largePersonGroupCreate(largePersonGroupId, body, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **largePersonGroupId** | **String**| Id referencing a particular large person group. | 
 **body** | [**MetaDataContract**](MetaDataContract.md)| Request body for creating new large person group. | 

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## largePersonGroupDelete

> largePersonGroupDelete(largePersonGroupId)



Delete an existing large person group. Persisted face features of all people in the large person group will also be deleted.

### Example

```javascript
import FaceClient from 'face_client';
let defaultClient = FaceClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FaceClient.DefaultApi();
let largePersonGroupId = "largePersonGroupId_example"; // String | Id referencing a particular large person group.
apiInstance.largePersonGroupDelete(largePersonGroupId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **largePersonGroupId** | **String**| Id referencing a particular large person group. | 

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## largePersonGroupGet

> LargePersonGroup largePersonGroupGet(largePersonGroupId, opts)



Retrieve the information of a large person group, including its name, userData and recognitionModel. This API returns large person group information only, use [LargePersonGroup Person - List](/docs/services/563879b61984550e40cbbe8d/operations/599adda06ac60f11b48b5aa1) instead to retrieve person information under the large person group. 

### Example

```javascript
import FaceClient from 'face_client';
let defaultClient = FaceClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FaceClient.DefaultApi();
let largePersonGroupId = "largePersonGroupId_example"; // String | Id referencing a particular large person group.
let opts = {
  'returnRecognitionModel': false // Boolean | A value indicating whether the operation should return 'recognitionModel' in response.
};
apiInstance.largePersonGroupGet(largePersonGroupId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **largePersonGroupId** | **String**| Id referencing a particular large person group. | 
 **returnRecognitionModel** | **Boolean**| A value indicating whether the operation should return &#39;recognitionModel&#39; in response. | [optional] [default to false]

### Return type

[**LargePersonGroup**](LargePersonGroup.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## largePersonGroupGetTrainingStatus

> TrainingStatus largePersonGroupGetTrainingStatus(largePersonGroupId)



Retrieve the training status of a large person group (completed or ongoing).

### Example

```javascript
import FaceClient from 'face_client';
let defaultClient = FaceClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FaceClient.DefaultApi();
let largePersonGroupId = "largePersonGroupId_example"; // String | Id referencing a particular large person group.
apiInstance.largePersonGroupGetTrainingStatus(largePersonGroupId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **largePersonGroupId** | **String**| Id referencing a particular large person group. | 

### Return type

[**TrainingStatus**](TrainingStatus.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## largePersonGroupList

> [LargePersonGroup] largePersonGroupList(opts)



List all existing large person groups’ largePersonGroupId, name, userData and recognitionModel.&lt;br /&gt; * Large person groups are stored in alphabetical order of largePersonGroupId. * \&quot;start\&quot; parameter (string, optional) is a user-provided largePersonGroupId value that returned entries have larger ids by string comparison. \&quot;start\&quot; set to empty to indicate return from the first item. * \&quot;top\&quot; parameter (int, optional) specifies the number of entries to return. A maximal of 1000 entries can be returned in one call. To fetch more, you can specify \&quot;start\&quot; with the last returned entry’s Id of the current call. &lt;br /&gt; For example, total 5 large person groups: \&quot;group1\&quot;, ..., \&quot;group5\&quot;. &lt;br /&gt; \&quot;start&#x3D;&amp;top&#x3D;\&quot; will return all 5 groups. &lt;br /&gt; \&quot;start&#x3D;&amp;top&#x3D;2\&quot; will return \&quot;group1\&quot;, \&quot;group2\&quot;. &lt;br /&gt; \&quot;start&#x3D;group2&amp;top&#x3D;3\&quot; will return \&quot;group3\&quot;, \&quot;group4\&quot;, \&quot;group5\&quot;. 

### Example

```javascript
import FaceClient from 'face_client';
let defaultClient = FaceClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FaceClient.DefaultApi();
let opts = {
  'start': "start_example", // String | List large person groups from the least largePersonGroupId greater than the \"start\".
  'top': 1000, // Number | The number of large person groups to list.
  'returnRecognitionModel': false // Boolean | A value indicating whether the operation should return 'recognitionModel' in response.
};
apiInstance.largePersonGroupList(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **String**| List large person groups from the least largePersonGroupId greater than the \&quot;start\&quot;. | [optional] 
 **top** | **Number**| The number of large person groups to list. | [optional] [default to 1000]
 **returnRecognitionModel** | **Boolean**| A value indicating whether the operation should return &#39;recognitionModel&#39; in response. | [optional] [default to false]

### Return type

[**[LargePersonGroup]**](LargePersonGroup.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## largePersonGroupPersonAddFaceFromUrl

> PersistedFace largePersonGroupPersonAddFaceFromUrl(largePersonGroupId, personId, imageUrl, opts)



Add a face to a person into a large person group for face identification or verification. To deal with an image contains multiple faces, input face can be specified as an image with a targetFace rectangle. It returns a persistedFaceId representing the added face. No image will be stored. Only the extracted face feature will be stored on server until [LargePersonGroup PersonFace - Delete](/docs/services/563879b61984550e40cbbe8d/operations/599ae2966ac60f11b48b5aa3), [LargePersonGroup Person - Delete](/docs/services/563879b61984550e40cbbe8d/operations/599ade5c6ac60f11b48b5aa2) or [LargePersonGroup - Delete](/docs/services/563879b61984550e40cbbe8d/operations/599adc216ac60f11b48b5a9f) is called. &lt;br /&gt; Note persistedFaceId is different from faceId generated by [Face - Detect](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395236). * Higher face image quality means better recognition precision. Please consider high-quality faces: frontal, clear, and face size is 200x200 pixels (100 pixels between eyes) or bigger. * Each person entry can hold up to 248 faces. * JPEG, PNG, GIF (the first frame), and BMP format are supported. The allowed image file size is from 1KB to 6MB. * \&quot;targetFace\&quot; rectangle should contain one face. Zero or multiple faces will be regarded as an error. If the provided \&quot;targetFace\&quot; rectangle is not returned from [Face - Detect](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395236), there’s no guarantee to detect and add the face successfully. * Out of detectable face size (36x36 - 4096x4096 pixels), large head-pose, or large occlusions will cause failures. * Adding/deleting faces to/from a same person will be processed sequentially. Adding/deleting faces to/from different persons are processed in parallel. * The minimum detectable face size is 36x36 pixels in an image no larger than 1920x1080 pixels. Images with dimensions higher than 1920x1080 pixels will need a proportionally larger minimum face size. * Different &#39;detectionModel&#39; values can be provided. To use and compare different detection models, please refer to [How to specify a detection model](https://docs.microsoft.com/en-us/azure/cognitive-services/face/face-api-how-to-topics/specify-detection-model)   | Model | Recommended use-case(s) |   | ---------- | -------- |   | &#39;detection_01&#39;: | The default detection model for [LargePersonGroup Person - Add Face](/docs/services/563879b61984550e40cbbe8d/operations/599adf2a3a7b9412a4d53f42). Recommend for near frontal face detection. For scenarios with exceptionally large angle (head-pose) faces, occluded faces or wrong image orientation, the faces in such cases may not be detected. |   | &#39;detection_02&#39;: | Detection model released in 2019 May with improved accuracy especially on small, side and blurry faces. |

### Example

```javascript
import FaceClient from 'face_client';
let defaultClient = FaceClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FaceClient.DefaultApi();
let largePersonGroupId = "largePersonGroupId_example"; // String | Id referencing a particular large person group.
let personId = "personId_example"; // String | Id referencing a particular person.
let imageUrl = new FaceClient.FaceDetectWithUrlRequest(); // FaceDetectWithUrlRequest | A JSON document with a URL pointing to the image that is to be analyzed.
let opts = {
  'userData': "userData_example", // String | User-specified data about the face for any purpose. The maximum length is 1KB.
  'targetFace': [null], // [Number] | A face rectangle to specify the target face to be added to a person in the format of \"targetFace=left,top,width,height\". E.g. \"targetFace=10,10,100,100\". If there is more than one face in the image, targetFace is required to specify which face to add. No targetFace means there is only one face detected in the entire image.
  'detectionModel': "'detection_01'" // String | Name of detection model. Detection model is used to detect faces in the submitted image. A detection model name can be provided when performing Face - Detect or (Large)FaceList - Add Face or (Large)PersonGroup - Add Face. The default value is 'detection_01', if another model is needed, please explicitly specify it.
};
apiInstance.largePersonGroupPersonAddFaceFromUrl(largePersonGroupId, personId, imageUrl, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **largePersonGroupId** | **String**| Id referencing a particular large person group. | 
 **personId** | **String**| Id referencing a particular person. | 
 **imageUrl** | [**FaceDetectWithUrlRequest**](FaceDetectWithUrlRequest.md)| A JSON document with a URL pointing to the image that is to be analyzed. | 
 **userData** | **String**| User-specified data about the face for any purpose. The maximum length is 1KB. | [optional] 
 **targetFace** | [**[Number]**](Number.md)| A face rectangle to specify the target face to be added to a person in the format of \&quot;targetFace&#x3D;left,top,width,height\&quot;. E.g. \&quot;targetFace&#x3D;10,10,100,100\&quot;. If there is more than one face in the image, targetFace is required to specify which face to add. No targetFace means there is only one face detected in the entire image. | [optional] 
 **detectionModel** | **String**| Name of detection model. Detection model is used to detect faces in the submitted image. A detection model name can be provided when performing Face - Detect or (Large)FaceList - Add Face or (Large)PersonGroup - Add Face. The default value is &#39;detection_01&#39;, if another model is needed, please explicitly specify it. | [optional] [default to &#39;detection_01&#39;]

### Return type

[**PersistedFace**](PersistedFace.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## largePersonGroupPersonCreate

> Person largePersonGroupPersonCreate(largePersonGroupId, body)



Create a new person in a specified large person group.

### Example

```javascript
import FaceClient from 'face_client';
let defaultClient = FaceClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FaceClient.DefaultApi();
let largePersonGroupId = "largePersonGroupId_example"; // String | Id referencing a particular large person group.
let body = new FaceClient.NameAndUserDataContract(); // NameAndUserDataContract | Request body for creating new person.
apiInstance.largePersonGroupPersonCreate(largePersonGroupId, body, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **largePersonGroupId** | **String**| Id referencing a particular large person group. | 
 **body** | [**NameAndUserDataContract**](NameAndUserDataContract.md)| Request body for creating new person. | 

### Return type

[**Person**](Person.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## largePersonGroupPersonDelete

> largePersonGroupPersonDelete(largePersonGroupId, personId)



Delete an existing person from a large person group. The persistedFaceId, userData, person name and face feature in the person entry will all be deleted.

### Example

```javascript
import FaceClient from 'face_client';
let defaultClient = FaceClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FaceClient.DefaultApi();
let largePersonGroupId = "largePersonGroupId_example"; // String | Id referencing a particular large person group.
let personId = "personId_example"; // String | Id referencing a particular person.
apiInstance.largePersonGroupPersonDelete(largePersonGroupId, personId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **largePersonGroupId** | **String**| Id referencing a particular large person group. | 
 **personId** | **String**| Id referencing a particular person. | 

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## largePersonGroupPersonDeleteFace

> largePersonGroupPersonDeleteFace(largePersonGroupId, personId, persistedFaceId)



Delete a face from a person in a large person group by specified largePersonGroupId, personId and persistedFaceId. &lt;br /&gt; Adding/deleting faces to/from a same person will be processed sequentially. Adding/deleting faces to/from different persons are processed in parallel.

### Example

```javascript
import FaceClient from 'face_client';
let defaultClient = FaceClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FaceClient.DefaultApi();
let largePersonGroupId = "largePersonGroupId_example"; // String | Id referencing a particular large person group.
let personId = "personId_example"; // String | Id referencing a particular person.
let persistedFaceId = "persistedFaceId_example"; // String | Id referencing a particular persistedFaceId of an existing face.
apiInstance.largePersonGroupPersonDeleteFace(largePersonGroupId, personId, persistedFaceId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **largePersonGroupId** | **String**| Id referencing a particular large person group. | 
 **personId** | **String**| Id referencing a particular person. | 
 **persistedFaceId** | **String**| Id referencing a particular persistedFaceId of an existing face. | 

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## largePersonGroupPersonGet

> Person largePersonGroupPersonGet(largePersonGroupId, personId)



Retrieve a person&#39;s name and userData, and the persisted faceIds representing the registered person face feature.

### Example

```javascript
import FaceClient from 'face_client';
let defaultClient = FaceClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FaceClient.DefaultApi();
let largePersonGroupId = "largePersonGroupId_example"; // String | Id referencing a particular large person group.
let personId = "personId_example"; // String | Id referencing a particular person.
apiInstance.largePersonGroupPersonGet(largePersonGroupId, personId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **largePersonGroupId** | **String**| Id referencing a particular large person group. | 
 **personId** | **String**| Id referencing a particular person. | 

### Return type

[**Person**](Person.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## largePersonGroupPersonGetFace

> PersistedFace largePersonGroupPersonGetFace(largePersonGroupId, personId, persistedFaceId)



Retrieve information about a persisted face (specified by persistedFaceId, personId and its belonging largePersonGroupId).

### Example

```javascript
import FaceClient from 'face_client';
let defaultClient = FaceClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FaceClient.DefaultApi();
let largePersonGroupId = "largePersonGroupId_example"; // String | Id referencing a particular large person group.
let personId = "personId_example"; // String | Id referencing a particular person.
let persistedFaceId = "persistedFaceId_example"; // String | Id referencing a particular persistedFaceId of an existing face.
apiInstance.largePersonGroupPersonGetFace(largePersonGroupId, personId, persistedFaceId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **largePersonGroupId** | **String**| Id referencing a particular large person group. | 
 **personId** | **String**| Id referencing a particular person. | 
 **persistedFaceId** | **String**| Id referencing a particular persistedFaceId of an existing face. | 

### Return type

[**PersistedFace**](PersistedFace.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## largePersonGroupPersonList

> [Person] largePersonGroupPersonList(largePersonGroupId, opts)



List all persons in a large person group, and retrieve person information (including personId, name, userData and persistedFaceIds of registered faces of the person).

### Example

```javascript
import FaceClient from 'face_client';
let defaultClient = FaceClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FaceClient.DefaultApi();
let largePersonGroupId = "largePersonGroupId_example"; // String | Id referencing a particular large person group.
let opts = {
  'start': "start_example", // String | Starting person id to return (used to list a range of persons).
  'top': 56 // Number | Number of persons to return starting with the person id indicated by the 'start' parameter.
};
apiInstance.largePersonGroupPersonList(largePersonGroupId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **largePersonGroupId** | **String**| Id referencing a particular large person group. | 
 **start** | **String**| Starting person id to return (used to list a range of persons). | [optional] 
 **top** | **Number**| Number of persons to return starting with the person id indicated by the &#39;start&#39; parameter. | [optional] 

### Return type

[**[Person]**](Person.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## largePersonGroupPersonUpdate

> largePersonGroupPersonUpdate(largePersonGroupId, personId, body)



Update name or userData of a person.

### Example

```javascript
import FaceClient from 'face_client';
let defaultClient = FaceClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FaceClient.DefaultApi();
let largePersonGroupId = "largePersonGroupId_example"; // String | Id referencing a particular large person group.
let personId = "personId_example"; // String | Id referencing a particular person.
let body = new FaceClient.NameAndUserDataContract(); // NameAndUserDataContract | Request body for person update operation.
apiInstance.largePersonGroupPersonUpdate(largePersonGroupId, personId, body, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **largePersonGroupId** | **String**| Id referencing a particular large person group. | 
 **personId** | **String**| Id referencing a particular person. | 
 **body** | [**NameAndUserDataContract**](NameAndUserDataContract.md)| Request body for person update operation. | 

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## largePersonGroupPersonUpdateFace

> largePersonGroupPersonUpdateFace(largePersonGroupId, personId, persistedFaceId, body)



Update a person persisted face&#39;s userData field.

### Example

```javascript
import FaceClient from 'face_client';
let defaultClient = FaceClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FaceClient.DefaultApi();
let largePersonGroupId = "largePersonGroupId_example"; // String | Id referencing a particular large person group.
let personId = "personId_example"; // String | Id referencing a particular person.
let persistedFaceId = "persistedFaceId_example"; // String | Id referencing a particular persistedFaceId of an existing face.
let body = new FaceClient.UpdateFaceRequest(); // UpdateFaceRequest | Request body for updating persisted face.
apiInstance.largePersonGroupPersonUpdateFace(largePersonGroupId, personId, persistedFaceId, body, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **largePersonGroupId** | **String**| Id referencing a particular large person group. | 
 **personId** | **String**| Id referencing a particular person. | 
 **persistedFaceId** | **String**| Id referencing a particular persistedFaceId of an existing face. | 
 **body** | [**UpdateFaceRequest**](UpdateFaceRequest.md)| Request body for updating persisted face. | 

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## largePersonGroupTrain

> largePersonGroupTrain(largePersonGroupId)



Queue a large person group training task, the training task may not be started immediately.

### Example

```javascript
import FaceClient from 'face_client';
let defaultClient = FaceClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FaceClient.DefaultApi();
let largePersonGroupId = "largePersonGroupId_example"; // String | Id referencing a particular large person group.
apiInstance.largePersonGroupTrain(largePersonGroupId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **largePersonGroupId** | **String**| Id referencing a particular large person group. | 

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## largePersonGroupUpdate

> largePersonGroupUpdate(largePersonGroupId, body)



Update an existing large person group&#39;s display name and userData. The properties which does not appear in request body will not be updated.

### Example

```javascript
import FaceClient from 'face_client';
let defaultClient = FaceClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FaceClient.DefaultApi();
let largePersonGroupId = "largePersonGroupId_example"; // String | Id referencing a particular large person group.
let body = new FaceClient.NameAndUserDataContract(); // NameAndUserDataContract | Request body for updating large person group.
apiInstance.largePersonGroupUpdate(largePersonGroupId, body, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **largePersonGroupId** | **String**| Id referencing a particular large person group. | 
 **body** | [**NameAndUserDataContract**](NameAndUserDataContract.md)| Request body for updating large person group. | 

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## personGroupCreate

> personGroupCreate(personGroupId, body)



Create a new person group with specified personGroupId, name, user-provided userData and recognitionModel. &lt;br /&gt; A person group is the container of the uploaded person data, including face recognition features. &lt;br /&gt; After creation, use [PersonGroup Person - Create](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f3039523c) to add persons into the group, and then call [PersonGroup - Train](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395249) to get this group ready for [Face - Identify](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395239). &lt;br /&gt; No image will be stored. Only the person&#39;s extracted face features and userData will be stored on server until [PersonGroup Person - Delete](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f3039523d) or [PersonGroup - Delete](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395245) is called. &lt;br/&gt;&#39;recognitionModel&#39; should be specified to associate with this person group. The default value for &#39;recognitionModel&#39; is &#39;recognition_01&#39;, if the latest model needed, please explicitly specify the model you need in this parameter. New faces that are added to an existing person group will use the recognition model that&#39;s already associated with the collection. Existing face features in a person group can&#39;t be updated to features extracted by another version of recognition model. * &#39;recognition_01&#39;: The default recognition model for [PersonGroup - Create](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395244). All those person groups created before 2019 March are bonded with this recognition model. * &#39;recognition_02&#39;: Recognition model released in 2019 March. &#39;recognition_02&#39; is recommended since its overall accuracy is improved compared with &#39;recognition_01&#39;.  Person group quota: * Free-tier subscription quota: 1,000 person groups. Each holds up to 1,000 persons. * S0-tier subscription quota: 1,000,000 person groups. Each holds up to 10,000 persons. * to handle larger scale face identification problem, please consider using [LargePersonGroup](/docs/services/563879b61984550e40cbbe8d/operations/599acdee6ac60f11b48b5a9d).

### Example

```javascript
import FaceClient from 'face_client';
let defaultClient = FaceClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FaceClient.DefaultApi();
let personGroupId = "personGroupId_example"; // String | Id referencing a particular person group.
let body = new FaceClient.MetaDataContract(); // MetaDataContract | Request body for creating new person group.
apiInstance.personGroupCreate(personGroupId, body, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **personGroupId** | **String**| Id referencing a particular person group. | 
 **body** | [**MetaDataContract**](MetaDataContract.md)| Request body for creating new person group. | 

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## personGroupDelete

> personGroupDelete(personGroupId)



Delete an existing person group. Persisted face features of all people in the person group will also be deleted.

### Example

```javascript
import FaceClient from 'face_client';
let defaultClient = FaceClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FaceClient.DefaultApi();
let personGroupId = "personGroupId_example"; // String | Id referencing a particular person group.
apiInstance.personGroupDelete(personGroupId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **personGroupId** | **String**| Id referencing a particular person group. | 

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## personGroupGet

> PersonGroup personGroupGet(personGroupId, opts)



Retrieve person group name, userData and recognitionModel. To get person information under this personGroup, use [PersonGroup Person - List](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395241).

### Example

```javascript
import FaceClient from 'face_client';
let defaultClient = FaceClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FaceClient.DefaultApi();
let personGroupId = "personGroupId_example"; // String | Id referencing a particular person group.
let opts = {
  'returnRecognitionModel': false // Boolean | A value indicating whether the operation should return 'recognitionModel' in response.
};
apiInstance.personGroupGet(personGroupId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **personGroupId** | **String**| Id referencing a particular person group. | 
 **returnRecognitionModel** | **Boolean**| A value indicating whether the operation should return &#39;recognitionModel&#39; in response. | [optional] [default to false]

### Return type

[**PersonGroup**](PersonGroup.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## personGroupGetTrainingStatus

> TrainingStatus personGroupGetTrainingStatus(personGroupId)



Retrieve the training status of a person group (completed or ongoing).

### Example

```javascript
import FaceClient from 'face_client';
let defaultClient = FaceClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FaceClient.DefaultApi();
let personGroupId = "personGroupId_example"; // String | Id referencing a particular person group.
apiInstance.personGroupGetTrainingStatus(personGroupId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **personGroupId** | **String**| Id referencing a particular person group. | 

### Return type

[**TrainingStatus**](TrainingStatus.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## personGroupList

> [PersonGroup] personGroupList(opts)



List person groups’ personGroupId, name, userData and recognitionModel.&lt;br /&gt; * Person groups are stored in alphabetical order of personGroupId. * \&quot;start\&quot; parameter (string, optional) is a user-provided personGroupId value that returned entries have larger ids by string comparison. \&quot;start\&quot; set to empty to indicate return from the first item. * \&quot;top\&quot; parameter (int, optional) specifies the number of entries to return. A maximal of 1000 entries can be returned in one call. To fetch more, you can specify \&quot;start\&quot; with the last returned entry’s Id of the current call. &lt;br /&gt; For example, total 5 person groups: \&quot;group1\&quot;, ..., \&quot;group5\&quot;. &lt;br /&gt; \&quot;start&#x3D;&amp;top&#x3D;\&quot; will return all 5 groups. &lt;br /&gt; \&quot;start&#x3D;&amp;top&#x3D;2\&quot; will return \&quot;group1\&quot;, \&quot;group2\&quot;. &lt;br /&gt; \&quot;start&#x3D;group2&amp;top&#x3D;3\&quot; will return \&quot;group3\&quot;, \&quot;group4\&quot;, \&quot;group5\&quot;. 

### Example

```javascript
import FaceClient from 'face_client';
let defaultClient = FaceClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FaceClient.DefaultApi();
let opts = {
  'start': "start_example", // String | List person groups from the least personGroupId greater than the \"start\".
  'top': 1000, // Number | The number of person groups to list.
  'returnRecognitionModel': false // Boolean | A value indicating whether the operation should return 'recognitionModel' in response.
};
apiInstance.personGroupList(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **String**| List person groups from the least personGroupId greater than the \&quot;start\&quot;. | [optional] 
 **top** | **Number**| The number of person groups to list. | [optional] [default to 1000]
 **returnRecognitionModel** | **Boolean**| A value indicating whether the operation should return &#39;recognitionModel&#39; in response. | [optional] [default to false]

### Return type

[**[PersonGroup]**](PersonGroup.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## personGroupPersonAddFaceFromUrl

> PersistedFace personGroupPersonAddFaceFromUrl(personGroupId, personId, imageUrl, opts)



Add a face to a person into a person group for face identification or verification. To deal with an image contains multiple faces, input face can be specified as an image with a targetFace rectangle. It returns a persistedFaceId representing the added face. No image will be stored. Only the extracted face feature will be stored on server until [PersonGroup PersonFace - Delete](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f3039523e), [PersonGroup Person - Delete](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f3039523d) or [PersonGroup - Delete](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395245) is called. &lt;br /&gt; Note persistedFaceId is different from faceId generated by [Face - Detect](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395236). *   Higher face image quality means better recognition precision. Please consider high-quality faces: frontal, clear, and face size is 200x200 pixels (100 pixels between eyes) or bigger. *   Each person entry can hold up to 248 faces. *   JPEG, PNG, GIF (the first frame), and BMP format are supported. The allowed image file size is from 1KB to 6MB. *   \&quot;targetFace\&quot; rectangle should contain one face. Zero or multiple faces will be regarded as an error. If the provided \&quot;targetFace\&quot; rectangle is not returned from [Face - Detect](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395236), there’s no guarantee to detect and add the face successfully. *   Out of detectable face size (36x36 - 4096x4096 pixels), large head-pose, or large occlusions will cause failures. *   Adding/deleting faces to/from a same person will be processed sequentially. Adding/deleting faces to/from different persons are processed in parallel. * The minimum detectable face size is 36x36 pixels in an image no larger than 1920x1080 pixels. Images with dimensions higher than 1920x1080 pixels will need a proportionally larger minimum face size. * Different &#39;detectionModel&#39; values can be provided. To use and compare different detection models, please refer to [How to specify a detection model](https://docs.microsoft.com/en-us/azure/cognitive-services/face/face-api-how-to-topics/specify-detection-model)   | Model | Recommended use-case(s) |   | ---------- | -------- |   | &#39;detection_01&#39;: | The default detection model for [PersonGroup Person - Add Face](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f3039523b). Recommend for near frontal face detection. For scenarios with exceptionally large angle (head-pose) faces, occluded faces or wrong image orientation, the faces in such cases may not be detected. |   | &#39;detection_02&#39;: | Detection model released in 2019 May with improved accuracy especially on small, side and blurry faces. |

### Example

```javascript
import FaceClient from 'face_client';
let defaultClient = FaceClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FaceClient.DefaultApi();
let personGroupId = "personGroupId_example"; // String | Id referencing a particular person group.
let personId = "personId_example"; // String | Id referencing a particular person.
let imageUrl = new FaceClient.FaceDetectWithUrlRequest(); // FaceDetectWithUrlRequest | A JSON document with a URL pointing to the image that is to be analyzed.
let opts = {
  'userData': "userData_example", // String | User-specified data about the face for any purpose. The maximum length is 1KB.
  'targetFace': [null], // [Number] | A face rectangle to specify the target face to be added to a person in the format of \"targetFace=left,top,width,height\". E.g. \"targetFace=10,10,100,100\". If there is more than one face in the image, targetFace is required to specify which face to add. No targetFace means there is only one face detected in the entire image.
  'detectionModel': "'detection_01'" // String | Name of detection model. Detection model is used to detect faces in the submitted image. A detection model name can be provided when performing Face - Detect or (Large)FaceList - Add Face or (Large)PersonGroup - Add Face. The default value is 'detection_01', if another model is needed, please explicitly specify it.
};
apiInstance.personGroupPersonAddFaceFromUrl(personGroupId, personId, imageUrl, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **personGroupId** | **String**| Id referencing a particular person group. | 
 **personId** | **String**| Id referencing a particular person. | 
 **imageUrl** | [**FaceDetectWithUrlRequest**](FaceDetectWithUrlRequest.md)| A JSON document with a URL pointing to the image that is to be analyzed. | 
 **userData** | **String**| User-specified data about the face for any purpose. The maximum length is 1KB. | [optional] 
 **targetFace** | [**[Number]**](Number.md)| A face rectangle to specify the target face to be added to a person in the format of \&quot;targetFace&#x3D;left,top,width,height\&quot;. E.g. \&quot;targetFace&#x3D;10,10,100,100\&quot;. If there is more than one face in the image, targetFace is required to specify which face to add. No targetFace means there is only one face detected in the entire image. | [optional] 
 **detectionModel** | **String**| Name of detection model. Detection model is used to detect faces in the submitted image. A detection model name can be provided when performing Face - Detect or (Large)FaceList - Add Face or (Large)PersonGroup - Add Face. The default value is &#39;detection_01&#39;, if another model is needed, please explicitly specify it. | [optional] [default to &#39;detection_01&#39;]

### Return type

[**PersistedFace**](PersistedFace.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## personGroupPersonCreate

> Person personGroupPersonCreate(personGroupId, body)



Create a new person in a specified person group.

### Example

```javascript
import FaceClient from 'face_client';
let defaultClient = FaceClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FaceClient.DefaultApi();
let personGroupId = "personGroupId_example"; // String | Id referencing a particular person group.
let body = new FaceClient.NameAndUserDataContract(); // NameAndUserDataContract | Request body for creating new person.
apiInstance.personGroupPersonCreate(personGroupId, body, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **personGroupId** | **String**| Id referencing a particular person group. | 
 **body** | [**NameAndUserDataContract**](NameAndUserDataContract.md)| Request body for creating new person. | 

### Return type

[**Person**](Person.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## personGroupPersonDelete

> personGroupPersonDelete(personGroupId, personId)



Delete an existing person from a person group. The persistedFaceId, userData, person name and face feature in the person entry will all be deleted.

### Example

```javascript
import FaceClient from 'face_client';
let defaultClient = FaceClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FaceClient.DefaultApi();
let personGroupId = "personGroupId_example"; // String | Id referencing a particular person group.
let personId = "personId_example"; // String | Id referencing a particular person.
apiInstance.personGroupPersonDelete(personGroupId, personId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **personGroupId** | **String**| Id referencing a particular person group. | 
 **personId** | **String**| Id referencing a particular person. | 

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## personGroupPersonDeleteFace

> personGroupPersonDeleteFace(personGroupId, personId, persistedFaceId)



Delete a face from a person in a person group by specified personGroupId, personId and persistedFaceId. &lt;br /&gt; Adding/deleting faces to/from a same person will be processed sequentially. Adding/deleting faces to/from different persons are processed in parallel.

### Example

```javascript
import FaceClient from 'face_client';
let defaultClient = FaceClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FaceClient.DefaultApi();
let personGroupId = "personGroupId_example"; // String | Id referencing a particular person group.
let personId = "personId_example"; // String | Id referencing a particular person.
let persistedFaceId = "persistedFaceId_example"; // String | Id referencing a particular persistedFaceId of an existing face.
apiInstance.personGroupPersonDeleteFace(personGroupId, personId, persistedFaceId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **personGroupId** | **String**| Id referencing a particular person group. | 
 **personId** | **String**| Id referencing a particular person. | 
 **persistedFaceId** | **String**| Id referencing a particular persistedFaceId of an existing face. | 

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## personGroupPersonGet

> Person personGroupPersonGet(personGroupId, personId)



Retrieve a person&#39;s information, including registered persisted faces, name and userData.

### Example

```javascript
import FaceClient from 'face_client';
let defaultClient = FaceClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FaceClient.DefaultApi();
let personGroupId = "personGroupId_example"; // String | Id referencing a particular person group.
let personId = "personId_example"; // String | Id referencing a particular person.
apiInstance.personGroupPersonGet(personGroupId, personId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **personGroupId** | **String**| Id referencing a particular person group. | 
 **personId** | **String**| Id referencing a particular person. | 

### Return type

[**Person**](Person.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## personGroupPersonGetFace

> PersistedFace personGroupPersonGetFace(personGroupId, personId, persistedFaceId)



Retrieve information about a persisted face (specified by persistedFaceId, personId and its belonging personGroupId).

### Example

```javascript
import FaceClient from 'face_client';
let defaultClient = FaceClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FaceClient.DefaultApi();
let personGroupId = "personGroupId_example"; // String | Id referencing a particular person group.
let personId = "personId_example"; // String | Id referencing a particular person.
let persistedFaceId = "persistedFaceId_example"; // String | Id referencing a particular persistedFaceId of an existing face.
apiInstance.personGroupPersonGetFace(personGroupId, personId, persistedFaceId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **personGroupId** | **String**| Id referencing a particular person group. | 
 **personId** | **String**| Id referencing a particular person. | 
 **persistedFaceId** | **String**| Id referencing a particular persistedFaceId of an existing face. | 

### Return type

[**PersistedFace**](PersistedFace.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## personGroupPersonList

> [Person] personGroupPersonList(personGroupId, opts)



List all persons in a person group, and retrieve person information (including personId, name, userData and persistedFaceIds of registered faces of the person).

### Example

```javascript
import FaceClient from 'face_client';
let defaultClient = FaceClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FaceClient.DefaultApi();
let personGroupId = "personGroupId_example"; // String | Id referencing a particular person group.
let opts = {
  'start': "start_example", // String | Starting person id to return (used to list a range of persons).
  'top': 56 // Number | Number of persons to return starting with the person id indicated by the 'start' parameter.
};
apiInstance.personGroupPersonList(personGroupId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **personGroupId** | **String**| Id referencing a particular person group. | 
 **start** | **String**| Starting person id to return (used to list a range of persons). | [optional] 
 **top** | **Number**| Number of persons to return starting with the person id indicated by the &#39;start&#39; parameter. | [optional] 

### Return type

[**[Person]**](Person.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## personGroupPersonUpdate

> personGroupPersonUpdate(personGroupId, personId, body)



Update name or userData of a person.

### Example

```javascript
import FaceClient from 'face_client';
let defaultClient = FaceClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FaceClient.DefaultApi();
let personGroupId = "personGroupId_example"; // String | Id referencing a particular person group.
let personId = "personId_example"; // String | Id referencing a particular person.
let body = new FaceClient.NameAndUserDataContract(); // NameAndUserDataContract | Request body for person update operation.
apiInstance.personGroupPersonUpdate(personGroupId, personId, body, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **personGroupId** | **String**| Id referencing a particular person group. | 
 **personId** | **String**| Id referencing a particular person. | 
 **body** | [**NameAndUserDataContract**](NameAndUserDataContract.md)| Request body for person update operation. | 

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## personGroupPersonUpdateFace

> personGroupPersonUpdateFace(personGroupId, personId, persistedFaceId, body)



Add a face to a person into a person group for face identification or verification. To deal with an image contains multiple faces, input face can be specified as an image with a targetFace rectangle. It returns a persistedFaceId representing the added face. No image will be stored. Only the extracted face feature will be stored on server until [PersonGroup PersonFace - Delete](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f3039523e), [PersonGroup Person - Delete](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f3039523d) or [PersonGroup - Delete](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395245) is called. &lt;br /&gt; Note persistedFaceId is different from faceId generated by [Face - Detect](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395236). * Higher face image quality means better recognition precision. Please consider high-quality faces: frontal, clear, and face size is 200x200 pixels (100 pixels between eyes) or bigger. * Each person entry can hold up to 248 faces. * JPEG, PNG, GIF (the first frame), and BMP format are supported. The allowed image file size is from 1KB to 6MB. * \&quot;targetFace\&quot; rectangle should contain one face. Zero or multiple faces will be regarded as an error. If the provided \&quot;targetFace\&quot; rectangle is not returned from [Face - Detect](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395236), there’s no guarantee to detect and add the face successfully. * Out of detectable face size (36x36 - 4096x4096 pixels), large head-pose, or large occlusions will cause failures. * Adding/deleting faces to/from a same person will be processed sequentially. Adding/deleting faces to/from different persons are processed in parallel.

### Example

```javascript
import FaceClient from 'face_client';
let defaultClient = FaceClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FaceClient.DefaultApi();
let personGroupId = "personGroupId_example"; // String | Id referencing a particular person group.
let personId = "personId_example"; // String | Id referencing a particular person.
let persistedFaceId = "persistedFaceId_example"; // String | Id referencing a particular persistedFaceId of an existing face.
let body = new FaceClient.UpdateFaceRequest(); // UpdateFaceRequest | Request body for updating persisted face.
apiInstance.personGroupPersonUpdateFace(personGroupId, personId, persistedFaceId, body, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **personGroupId** | **String**| Id referencing a particular person group. | 
 **personId** | **String**| Id referencing a particular person. | 
 **persistedFaceId** | **String**| Id referencing a particular persistedFaceId of an existing face. | 
 **body** | [**UpdateFaceRequest**](UpdateFaceRequest.md)| Request body for updating persisted face. | 

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## personGroupTrain

> personGroupTrain(personGroupId)



Queue a person group training task, the training task may not be started immediately.

### Example

```javascript
import FaceClient from 'face_client';
let defaultClient = FaceClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FaceClient.DefaultApi();
let personGroupId = "personGroupId_example"; // String | Id referencing a particular person group.
apiInstance.personGroupTrain(personGroupId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **personGroupId** | **String**| Id referencing a particular person group. | 

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## personGroupUpdate

> personGroupUpdate(personGroupId, body)



Update an existing person group&#39;s display name and userData. The properties which does not appear in request body will not be updated.

### Example

```javascript
import FaceClient from 'face_client';
let defaultClient = FaceClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FaceClient.DefaultApi();
let personGroupId = "personGroupId_example"; // String | Id referencing a particular person group.
let body = new FaceClient.NameAndUserDataContract(); // NameAndUserDataContract | Request body for updating person group.
apiInstance.personGroupUpdate(personGroupId, body, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **personGroupId** | **String**| Id referencing a particular person group. | 
 **body** | [**NameAndUserDataContract**](NameAndUserDataContract.md)| Request body for updating person group. | 

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## snapshotApply

> snapshotApply(snapshotId, body)



Submit an operation to apply a snapshot to current subscription. For each snapshot, only subscriptions included in the applyScope of Snapshot - Take can apply it.&lt;br /&gt; The snapshot interfaces are for users to backup and restore their face data from one face subscription to another, inside same region or across regions. The workflow contains two phases, user first calls Snapshot - Take to create a copy of the source object and store it as a snapshot, then calls Snapshot - Apply to paste the snapshot to target subscription. The snapshots are stored in a centralized location (per Azure instance), so that they can be applied cross accounts and regions.&lt;br /&gt; Applying snapshot is an asynchronous operation. An operation id can be obtained from the \&quot;Operation-Location\&quot; field in response header, to be used in OperationStatus - Get for tracking the progress of applying the snapshot. The target object id will be included in the \&quot;resourceLocation\&quot; field in OperationStatus - Get response when the operation status is \&quot;succeeded\&quot;.&lt;br /&gt; Snapshot applying time depends on the number of person and face entries in the snapshot object. It could be in seconds, or up to 1 hour for 1,000,000 persons with multiple faces.&lt;br /&gt; Snapshots will be automatically expired and cleaned in 48 hours after it is created by Snapshot - Take. So the target subscription is required to apply the snapshot in 48 hours since its creation.&lt;br /&gt; Applying a snapshot will not block any other operations against the target object, however it is not recommended because the correctness cannot be guaranteed during snapshot applying. After snapshot applying is completed, all operations towards the target object can work as normal. Snapshot also includes the training results of the source object, which means target subscription the snapshot applied to does not need re-train the target object before calling Identify/FindSimilar.&lt;br /&gt; One snapshot can be applied multiple times in parallel, while currently only CreateNew apply mode is supported, which means the apply operation will fail if target subscription already contains an object of same type and using the same objectId. Users can specify the \&quot;objectId\&quot; in request body to avoid such conflicts.&lt;br /&gt; * Free-tier subscription quota: 100 apply operations per month. * S0-tier subscription quota: 100 apply operations per day.

### Example

```javascript
import FaceClient from 'face_client';
let defaultClient = FaceClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FaceClient.DefaultApi();
let snapshotId = "snapshotId_example"; // String | Id referencing a particular snapshot.
let body = new FaceClient.ApplySnapshotRequest(); // ApplySnapshotRequest | Request body for applying a snapshot.
apiInstance.snapshotApply(snapshotId, body, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshotId** | **String**| Id referencing a particular snapshot. | 
 **body** | [**ApplySnapshotRequest**](ApplySnapshotRequest.md)| Request body for applying a snapshot. | 

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## snapshotDelete

> snapshotDelete(snapshotId)



Delete an existing snapshot according to the snapshotId. All object data and information in the snapshot will also be deleted. Only the source subscription who took the snapshot can delete the snapshot. If the user does not delete a snapshot with this API, the snapshot will still be automatically deleted in 48 hours after creation.

### Example

```javascript
import FaceClient from 'face_client';
let defaultClient = FaceClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FaceClient.DefaultApi();
let snapshotId = "snapshotId_example"; // String | Id referencing a particular snapshot.
apiInstance.snapshotDelete(snapshotId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshotId** | **String**| Id referencing a particular snapshot. | 

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## snapshotGet

> Snapshot snapshotGet(snapshotId)



Retrieve information about a snapshot. Snapshot is only accessible to the source subscription who took it, and target subscriptions included in the applyScope in Snapshot - Take.

### Example

```javascript
import FaceClient from 'face_client';
let defaultClient = FaceClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FaceClient.DefaultApi();
let snapshotId = "snapshotId_example"; // String | Id referencing a particular snapshot.
apiInstance.snapshotGet(snapshotId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshotId** | **String**| Id referencing a particular snapshot. | 

### Return type

[**Snapshot**](Snapshot.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## snapshotGetOperationStatus

> OperationStatus snapshotGetOperationStatus(operationId)



Retrieve the status of a take/apply snapshot operation.

### Example

```javascript
import FaceClient from 'face_client';
let defaultClient = FaceClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FaceClient.DefaultApi();
let operationId = "operationId_example"; // String | Id referencing a particular take/apply snapshot operation.
apiInstance.snapshotGetOperationStatus(operationId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operationId** | **String**| Id referencing a particular take/apply snapshot operation. | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## snapshotList

> [Snapshot] snapshotList(opts)



List all accessible snapshots with related information, including snapshots that were taken by the user, or snapshots to be applied to the user (subscription id was included in the applyScope in Snapshot - Take).

### Example

```javascript
import FaceClient from 'face_client';
let defaultClient = FaceClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FaceClient.DefaultApi();
let opts = {
  'type': "type_example", // String | User specified object type as a search filter.
  'applyScope': ["null"] // [String] | User specified snapshot apply scopes as a search filter. ApplyScope is an array of the target Azure subscription ids for the snapshot, specified by the user who created the snapshot by Snapshot - Take.
};
apiInstance.snapshotList(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **String**| User specified object type as a search filter. | [optional] 
 **applyScope** | [**[String]**](String.md)| User specified snapshot apply scopes as a search filter. ApplyScope is an array of the target Azure subscription ids for the snapshot, specified by the user who created the snapshot by Snapshot - Take. | [optional] 

### Return type

[**[Snapshot]**](Snapshot.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## snapshotTake

> snapshotTake(body)



Submit an operation to take a snapshot of face list, large face list, person group or large person group, with user-specified snapshot type, source object id, apply scope and an optional user data.&lt;br /&gt; The snapshot interfaces are for users to backup and restore their face data from one face subscription to another, inside same region or across regions. The workflow contains two phases, user first calls Snapshot - Take to create a copy of the source object and store it as a snapshot, then calls Snapshot - Apply to paste the snapshot to target subscription. The snapshots are stored in a centralized location (per Azure instance), so that they can be applied cross accounts and regions.&lt;br /&gt; Taking snapshot is an asynchronous operation. An operation id can be obtained from the \&quot;Operation-Location\&quot; field in response header, to be used in OperationStatus - Get for tracking the progress of creating the snapshot. The snapshot id will be included in the \&quot;resourceLocation\&quot; field in OperationStatus - Get response when the operation status is \&quot;succeeded\&quot;.&lt;br /&gt; Snapshot taking time depends on the number of person and face entries in the source object. It could be in seconds, or up to several hours for 1,000,000 persons with multiple faces.&lt;br /&gt; Snapshots will be automatically expired and cleaned in 48 hours after it is created by Snapshot - Take. User can delete the snapshot using Snapshot - Delete by themselves any time before expiration.&lt;br /&gt; Taking snapshot for a certain object will not block any other operations against the object. All read-only operations (Get/List and Identify/FindSimilar/Verify) can be conducted as usual. For all writable operations, including Add/Update/Delete the source object or its persons/faces and Train, they are not blocked but not recommended because writable updates may not be reflected on the snapshot during its taking. After snapshot taking is completed, all readable and writable operations can work as normal. Snapshot will also include the training results of the source object, which means target subscription the snapshot applied to does not need re-train the target object before calling Identify/FindSimilar.&lt;br /&gt; * Free-tier subscription quota: 100 take operations per month. * S0-tier subscription quota: 100 take operations per day.

### Example

```javascript
import FaceClient from 'face_client';
let defaultClient = FaceClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FaceClient.DefaultApi();
let body = new FaceClient.TakeSnapshotRequest(); // TakeSnapshotRequest | Request body for taking a snapshot.
apiInstance.snapshotTake(body, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TakeSnapshotRequest**](TakeSnapshotRequest.md)| Request body for taking a snapshot. | 

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## snapshotUpdate

> snapshotUpdate(snapshotId, body)



Update the information of a snapshot. Only the source subscription who took the snapshot can update the snapshot.

### Example

```javascript
import FaceClient from 'face_client';
let defaultClient = FaceClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new FaceClient.DefaultApi();
let snapshotId = "snapshotId_example"; // String | Id referencing a particular snapshot.
let body = new FaceClient.UpdateSnapshotRequest(); // UpdateSnapshotRequest | Request body for updating a snapshot.
apiInstance.snapshotUpdate(snapshotId, body, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshotId** | **String**| Id referencing a particular snapshot. | 
 **body** | [**UpdateSnapshotRequest**](UpdateSnapshotRequest.md)| Request body for updating a snapshot. | 

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*

