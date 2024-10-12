from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import APIError
from openapi_server.models.apply_snapshot_request import ApplySnapshotRequest
from openapi_server.models.detected_face import DetectedFace
from openapi_server.models.face_detect_with_url_request import FaceDetectWithUrlRequest
from openapi_server.models.face_list import FaceList
from openapi_server.models.find_similar_request import FindSimilarRequest
from openapi_server.models.group_request import GroupRequest
from openapi_server.models.group_result import GroupResult
from openapi_server.models.identify_request import IdentifyRequest
from openapi_server.models.identify_result import IdentifyResult
from openapi_server.models.large_face_list import LargeFaceList
from openapi_server.models.large_person_group import LargePersonGroup
from openapi_server.models.meta_data_contract import MetaDataContract
from openapi_server.models.name_and_user_data_contract import NameAndUserDataContract
from openapi_server.models.operation_status import OperationStatus
from openapi_server.models.persisted_face import PersistedFace
from openapi_server.models.person import Person
from openapi_server.models.person_group import PersonGroup
from openapi_server.models.similar_face import SimilarFace
from openapi_server.models.snapshot import Snapshot
from openapi_server.models.take_snapshot_request import TakeSnapshotRequest
from openapi_server.models.training_status import TrainingStatus
from openapi_server.models.update_face_request import UpdateFaceRequest
from openapi_server.models.update_snapshot_request import UpdateSnapshotRequest
from openapi_server.models.verify_face_to_face_request import VerifyFaceToFaceRequest
from openapi_server.models.verify_result import VerifyResult
from openapi_server import util


async def face_detect_with_url(request: web.Request, image_url, return_face_id=None, return_face_landmarks=None, return_face_attributes=None, recognition_model=None, return_recognition_model=None, detection_model=None) -> web.Response:
    """face_detect_with_url

    Detect human faces in an image, return face rectangles, and optionally with faceIds, landmarks, and attributes.&lt;br /&gt; * No image will be stored. Only the extracted face feature will be stored on server. The faceId is an identifier of the face feature and will be used in [Face - Identify](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395239), [Face - Verify](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f3039523a), and [Face - Find Similar](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395237). The stored face feature(s) will expire and be deleted 24 hours after the original detection call. * Optional parameters include faceId, landmarks, and attributes. Attributes include age, gender, headPose, smile, facialHair, glasses, emotion, hair, makeup, occlusion, accessories, blur, exposure and noise. Some of the results returned for specific attributes may not be highly accurate. * JPEG, PNG, GIF (the first frame), and BMP format are supported. The allowed image file size is from 1KB to 6MB. * Up to 100 faces can be returned for an image. Faces are ranked by face rectangle size from large to small. * For optimal results when querying [Face - Identify](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395239), [Face - Verify](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f3039523a), and [Face - Find Similar](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395237) (&#39;returnFaceId&#39; is true), please use faces that are: frontal, clear, and with a minimum size of 200x200 pixels (100 pixels between eyes). * The minimum detectable face size is 36x36 pixels in an image no larger than 1920x1080 pixels. Images with dimensions higher than 1920x1080 pixels will need a proportionally larger minimum face size. * Different &#39;detectionModel&#39; values can be provided. To use and compare different detection models, please refer to [How to specify a detection model](https://docs.microsoft.com/en-us/azure/cognitive-services/face/face-api-how-to-topics/specify-detection-model)   | Model | Recommended use-case(s) |   | ---------- | -------- |   | &#39;detection_01&#39;: | The default detection model for [Face - Detect](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395236). Recommend for near frontal face detection. For scenarios with exceptionally large angle (head-pose) faces, occluded faces or wrong image orientation, the faces in such cases may not be detected. |   | &#39;detection_02&#39;: | Detection model released in 2019 May with improved accuracy especially on small, side and blurry faces. |  * Different &#39;recognitionModel&#39; values are provided. If follow-up operations like Verify, Identify, Find Similar are needed, please specify the recognition model with &#39;recognitionModel&#39; parameter. The default value for &#39;recognitionModel&#39; is &#39;recognition_01&#39;, if latest model needed, please explicitly specify the model you need in this parameter. Once specified, the detected faceIds will be associated with the specified recognition model. More details, please refer to [How to specify a recognition model](https://docs.microsoft.com/en-us/azure/cognitive-services/face/face-api-how-to-topics/specify-recognition-model)   | Model | Recommended use-case(s) |   | ---------- | -------- |   | &#39;recognition_01&#39;: | The default recognition model for [Face - Detect](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395236). All those faceIds created before 2019 March are bonded with this recognition model. |   | &#39;recognition_02&#39;: | Recognition model released in 2019 March. &#39;recognition_02&#39; is recommended since its overall accuracy is improved compared with &#39;recognition_01&#39;. |

    :param image_url: A JSON document with a URL pointing to the image that is to be analyzed.
    :type image_url: dict | bytes
    :param return_face_id: A value indicating whether the operation should return faceIds of detected faces.
    :type return_face_id: bool
    :param return_face_landmarks: A value indicating whether the operation should return landmarks of the detected faces.
    :type return_face_landmarks: bool
    :param return_face_attributes: Analyze and return the one or more specified face attributes in the comma-separated string like \&quot;returnFaceAttributes&#x3D;age,gender\&quot;. Supported face attributes include age, gender, headPose, smile, facialHair, glasses and emotion. Note that each face attribute analysis has additional computational and time cost.
    :type return_face_attributes: List[str]
    :param recognition_model: Name of recognition model. Recognition model is used when the face features are extracted and associated with detected faceIds, (Large)FaceList or (Large)PersonGroup. A recognition model name can be provided when performing Face - Detect or (Large)FaceList - Create or (Large)PersonGroup - Create. The default value is &#39;recognition_01&#39;, if latest model needed, please explicitly specify the model you need.
    :type recognition_model: str
    :param return_recognition_model: A value indicating whether the operation should return &#39;recognitionModel&#39; in response.
    :type return_recognition_model: bool
    :param detection_model: Name of detection model. Detection model is used to detect faces in the submitted image. A detection model name can be provided when performing Face - Detect or (Large)FaceList - Add Face or (Large)PersonGroup - Add Face. The default value is &#39;detection_01&#39;, if another model is needed, please explicitly specify it.
    :type detection_model: str

    """
    image_url = FaceDetectWithUrlRequest.from_dict(image_url)
    return web.Response(status=200)


async def face_find_similar(request: web.Request, body) -> web.Response:
    """face_find_similar

    Given query face&#39;s faceId, to search the similar-looking faces from a faceId array, a face list or a large face list. faceId array contains the faces created by [Face - Detect](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395236), which will expire 24 hours after creation. A \&quot;faceListId\&quot; is created by [FaceList - Create](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f3039524b) containing persistedFaceIds that will not expire. And a \&quot;largeFaceListId\&quot; is created by [LargeFaceList - Create](/docs/services/563879b61984550e40cbbe8d/operations/5a157b68d2de3616c086f2cc) containing persistedFaceIds that will also not expire. Depending on the input the returned similar faces list contains faceIds or persistedFaceIds ranked by similarity. &lt;br/&gt;Find similar has two working modes, \&quot;matchPerson\&quot; and \&quot;matchFace\&quot;. \&quot;matchPerson\&quot; is the default mode that it tries to find faces of the same person as possible by using internal same-person thresholds. It is useful to find a known person&#39;s other photos. Note that an empty list will be returned if no faces pass the internal thresholds. \&quot;matchFace\&quot; mode ignores same-person thresholds and returns ranked similar faces anyway, even the similarity is low. It can be used in the cases like searching celebrity-looking faces. &lt;br/&gt;The &#39;recognitionModel&#39; associated with the query face&#39;s faceId should be the same as the &#39;recognitionModel&#39; used by the target faceId array, face list or large face list. 

    :param body: Request body for Find Similar.
    :type body: dict | bytes

    """
    body = FindSimilarRequest.from_dict(body)
    return web.Response(status=200)


async def face_group(request: web.Request, body) -> web.Response:
    """face_group

    Divide candidate faces into groups based on face similarity.&lt;br /&gt; * The output is one or more disjointed face groups and a messyGroup. A face group contains faces that have similar looking, often of the same person. Face groups are ranked by group size, i.e. number of faces. Notice that faces belonging to a same person might be split into several groups in the result. * MessyGroup is a special face group containing faces that cannot find any similar counterpart face from original faces. The messyGroup will not appear in the result if all faces found their counterparts. * Group API needs at least 2 candidate faces and 1000 at most. We suggest to try [Face - Verify](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f3039523a) when you only have 2 candidate faces. * The &#39;recognitionModel&#39; associated with the query faces&#39; faceIds should be the same. 

    :param body: Request body for grouping.
    :type body: dict | bytes

    """
    body = GroupRequest.from_dict(body)
    return web.Response(status=200)


async def face_identify(request: web.Request, body) -> web.Response:
    """face_identify

    1-to-many identification to find the closest matches of the specific query person face from a person group or large person group. &lt;br/&gt; For each face in the faceIds array, Face Identify will compute similarities between the query face and all the faces in the person group (given by personGroupId) or large person group (given by largePersonGroupId), and return candidate person(s) for that face ranked by similarity confidence. The person group/large person group should be trained to make it ready for identification. See more in [PersonGroup - Train](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395249) and [LargePersonGroup - Train](/docs/services/563879b61984550e40cbbe8d/operations/599ae2d16ac60f11b48b5aa4). &lt;br/&gt;   Remarks:&lt;br /&gt; * The algorithm allows more than one face to be identified independently at the same request, but no more than 10 faces. * Each person in the person group/large person group could have more than one face, but no more than 248 faces. * Higher face image quality means better identification precision. Please consider high-quality faces: frontal, clear, and face size is 200x200 pixels (100 pixels between eyes) or bigger. * Number of candidates returned is restricted by maxNumOfCandidatesReturned and confidenceThreshold. If no person is identified, the returned candidates will be an empty array. * Try [Face - Find Similar](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395237) when you need to find similar faces from a face list/large face list instead of a person group/large person group. * The &#39;recognitionModel&#39; associated with the query faces&#39; faceIds should be the same as the &#39;recognitionModel&#39; used by the target person group or large person group. 

    :param body: Request body for identify operation.
    :type body: dict | bytes

    """
    body = IdentifyRequest.from_dict(body)
    return web.Response(status=200)


async def face_list_add_face_from_url(request: web.Request, face_list_id, image_url, user_data=None, target_face=None, detection_model=None) -> web.Response:
    """face_list_add_face_from_url

    Add a face to a specified face list, up to 1,000 faces. &lt;br /&gt; To deal with an image contains multiple faces, input face can be specified as an image with a targetFace rectangle. It returns a persistedFaceId representing the added face. No image will be stored. Only the extracted face feature will be stored on server until [FaceList - Delete Face](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395251) or [FaceList - Delete](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f3039524f) is called. &lt;br /&gt; Note persistedFaceId is different from faceId generated by [Face - Detect](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395236). * Higher face image quality means better detection and recognition precision. Please consider high-quality faces: frontal, clear, and face size is 200x200 pixels (100 pixels between eyes) or bigger. * JPEG, PNG, GIF (the first frame), and BMP format are supported. The allowed image file size is from 1KB to 6MB. * \&quot;targetFace\&quot; rectangle should contain one face. Zero or multiple faces will be regarded as an error. If the provided \&quot;targetFace\&quot; rectangle is not returned from [Face - Detect](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395236), there’s no guarantee to detect and add the face successfully. * Out of detectable face size (36x36 - 4096x4096 pixels), large head-pose, or large occlusions will cause failures. * Adding/deleting faces to/from a same face list are processed sequentially and to/from different face lists are in parallel. * The minimum detectable face size is 36x36 pixels in an image no larger than 1920x1080 pixels. Images with dimensions higher than 1920x1080 pixels will need a proportionally larger minimum face size. * Different &#39;detectionModel&#39; values can be provided. To use and compare different detection models, please refer to [How to specify a detection model](https://docs.microsoft.com/en-us/azure/cognitive-services/face/face-api-how-to-topics/specify-detection-model)   | Model | Recommended use-case(s) |   | ---------- | -------- |   | &#39;detection_01&#39;: | The default detection model for [FaceList - Add Face](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395250). Recommend for near frontal face detection. For scenarios with exceptionally large angle (head-pose) faces, occluded faces or wrong image orientation, the faces in such cases may not be detected. |   | &#39;detection_02&#39;: | Detection model released in 2019 May with improved accuracy especially on small, side and blurry faces. |

    :param face_list_id: Id referencing a particular face list.
    :type face_list_id: str
    :param image_url: A JSON document with a URL pointing to the image that is to be analyzed.
    :type image_url: dict | bytes
    :param user_data: User-specified data about the face for any purpose. The maximum length is 1KB.
    :type user_data: str
    :param target_face: A face rectangle to specify the target face to be added to a person in the format of \&quot;targetFace&#x3D;left,top,width,height\&quot;. E.g. \&quot;targetFace&#x3D;10,10,100,100\&quot;. If there is more than one face in the image, targetFace is required to specify which face to add. No targetFace means there is only one face detected in the entire image.
    :type target_face: List[int]
    :param detection_model: Name of detection model. Detection model is used to detect faces in the submitted image. A detection model name can be provided when performing Face - Detect or (Large)FaceList - Add Face or (Large)PersonGroup - Add Face. The default value is &#39;detection_01&#39;, if another model is needed, please explicitly specify it.
    :type detection_model: str

    """
    image_url = FaceDetectWithUrlRequest.from_dict(image_url)
    return web.Response(status=200)


async def face_list_create(request: web.Request, face_list_id, body) -> web.Response:
    """face_list_create

    Create an empty face list with user-specified faceListId, name, an optional userData and recognitionModel. Up to 64 face lists are allowed in one subscription. &lt;br /&gt; Face list is a list of faces, up to 1,000 faces, and used by [Face - Find Similar](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395237). &lt;br /&gt; After creation, user should use [FaceList - Add Face](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395250) to import the faces. No image will be stored. Only the extracted face features are stored on server until [FaceList - Delete](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f3039524f) is called. &lt;br /&gt; Find Similar is used for scenario like finding celebrity-like faces, similar face filtering, or as a light way face identification. But if the actual use is to identify person, please use [PersonGroup](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395244) / [LargePersonGroup](/docs/services/563879b61984550e40cbbe8d/operations/599acdee6ac60f11b48b5a9d) and [Face - Identify](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395239). &lt;br /&gt; Please consider [LargeFaceList](/docs/services/563879b61984550e40cbbe8d/operations/5a157b68d2de3616c086f2cc) when the face number is large. It can support up to 1,000,000 faces. &lt;br /&gt;&#39;recognitionModel&#39; should be specified to associate with this face list. The default value for &#39;recognitionModel&#39; is &#39;recognition_01&#39;, if the latest model needed, please explicitly specify the model you need in this parameter. New faces that are added to an existing face list will use the recognition model that&#39;s already associated with the collection. Existing face features in a face list can&#39;t be updated to features extracted by another version of recognition model. * &#39;recognition_01&#39;: The default recognition model for [FaceList- Create](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f3039524b). All those face lists created before 2019 March are bonded with this recognition model. * &#39;recognition_02&#39;: Recognition model released in 2019 March. &#39;recognition_02&#39; is recommended since its overall accuracy is improved compared with &#39;recognition_01&#39;.

    :param face_list_id: Id referencing a particular face list.
    :type face_list_id: str
    :param body: Request body for creating a face list.
    :type body: dict | bytes

    """
    body = MetaDataContract.from_dict(body)
    return web.Response(status=200)


async def face_list_delete(request: web.Request, face_list_id) -> web.Response:
    """face_list_delete

    Delete a specified face list.

    :param face_list_id: Id referencing a particular face list.
    :type face_list_id: str

    """
    return web.Response(status=200)


async def face_list_delete_face(request: web.Request, face_list_id, persisted_face_id) -> web.Response:
    """face_list_delete_face

    Delete a face from a face list by specified faceListId and persistedFaceId. &lt;br /&gt; Adding/deleting faces to/from a same face list are processed sequentially and to/from different face lists are in parallel.

    :param face_list_id: Id referencing a particular face list.
    :type face_list_id: str
    :param persisted_face_id: Id referencing a particular persistedFaceId of an existing face.
    :type persisted_face_id: str
    :type persisted_face_id: str

    """
    return web.Response(status=200)


async def face_list_get(request: web.Request, face_list_id, return_recognition_model=None) -> web.Response:
    """face_list_get

    Retrieve a face list’s faceListId, name, userData, recognitionModel and faces in the face list. 

    :param face_list_id: Id referencing a particular face list.
    :type face_list_id: str
    :param return_recognition_model: A value indicating whether the operation should return &#39;recognitionModel&#39; in response.
    :type return_recognition_model: bool

    """
    return web.Response(status=200)


async def face_list_list(request: web.Request, return_recognition_model=None) -> web.Response:
    """face_list_list

    List face lists’ faceListId, name, userData and recognitionModel. &lt;br /&gt;  To get face information inside faceList use [FaceList - Get](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f3039524c) 

    :param return_recognition_model: A value indicating whether the operation should return &#39;recognitionModel&#39; in response.
    :type return_recognition_model: bool

    """
    return web.Response(status=200)


async def face_list_update(request: web.Request, face_list_id, body) -> web.Response:
    """face_list_update

    Update information of a face list.

    :param face_list_id: Id referencing a particular face list.
    :type face_list_id: str
    :param body: Request body for updating a face list.
    :type body: dict | bytes

    """
    body = NameAndUserDataContract.from_dict(body)
    return web.Response(status=200)


async def face_verify_face_to_face(request: web.Request, body) -> web.Response:
    """face_verify_face_to_face

    Verify whether two faces belong to a same person or whether one face belongs to a person. &lt;br/&gt; Remarks:&lt;br /&gt; * Higher face image quality means better identification precision. Please consider high-quality faces: frontal, clear, and face size is 200x200 pixels (100 pixels between eyes) or bigger. * For the scenarios that are sensitive to accuracy please make your own judgment. * The &#39;recognitionModel&#39; associated with the query faces&#39; faceIds should be the same as the &#39;recognitionModel&#39; used by the target face, person group or large person group. 

    :param body: Request body for face to face verification.
    :type body: dict | bytes

    """
    body = VerifyFaceToFaceRequest.from_dict(body)
    return web.Response(status=200)


async def large_face_list_add_face_from_url(request: web.Request, large_face_list_id, image_url, user_data=None, target_face=None, detection_model=None) -> web.Response:
    """large_face_list_add_face_from_url

    Add a face to a specified large face list, up to 1,000,000 faces. &lt;br /&gt; To deal with an image contains multiple faces, input face can be specified as an image with a targetFace rectangle. It returns a persistedFaceId representing the added face. No image will be stored. Only the extracted face feature will be stored on server until [LargeFaceList Face - Delete](/docs/services/563879b61984550e40cbbe8d/operations/5a158c8ad2de3616c086f2d4) or [LargeFaceList - Delete](/docs/services/563879b61984550e40cbbe8d/operations/5a1580d5d2de3616c086f2cd) is called. &lt;br /&gt; Note persistedFaceId is different from faceId generated by [Face - Detect](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395236). * Higher face image quality means better recognition precision. Please consider high-quality faces: frontal, clear, and face size is 200x200 pixels (100 pixels between eyes) or bigger. * JPEG, PNG, GIF (the first frame), and BMP format are supported. The allowed image file size is from 1KB to 6MB. * \&quot;targetFace\&quot; rectangle should contain one face. Zero or multiple faces will be regarded as an error. If the provided \&quot;targetFace\&quot; rectangle is not returned from [Face - Detect](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395236), there’s no guarantee to detect and add the face successfully. * Out of detectable face size (36x36 - 4096x4096 pixels), large head-pose, or large occlusions will cause failures. * Adding/deleting faces to/from a same face list are processed sequentially and to/from different face lists are in parallel. * The minimum detectable face size is 36x36 pixels in an image no larger than 1920x1080 pixels. Images with dimensions higher than 1920x1080 pixels will need a proportionally larger minimum face size. * Different &#39;detectionModel&#39; values can be provided. To use and compare different detection models, please refer to [How to specify a detection model](https://docs.microsoft.com/en-us/azure/cognitive-services/face/face-api-how-to-topics/specify-detection-model)   | Model | Recommended use-case(s) |   | ---------- | -------- |   | &#39;detection_01&#39;: | The default detection model for [LargeFaceList - Add Face](/docs/services/563879b61984550e40cbbe8d/operations/5a158c10d2de3616c086f2d3). Recommend for near frontal face detection. For scenarios with exceptionally large angle (head-pose) faces, occluded faces or wrong image orientation, the faces in such cases may not be detected. |   | &#39;detection_02&#39;: | Detection model released in 2019 May with improved accuracy especially on small, side and blurry faces. |  Quota: * Free-tier subscription quota: 1,000 faces per large face list. * S0-tier subscription quota: 1,000,000 faces per large face list.

    :param large_face_list_id: Id referencing a particular large face list.
    :type large_face_list_id: str
    :param image_url: A JSON document with a URL pointing to the image that is to be analyzed.
    :type image_url: dict | bytes
    :param user_data: User-specified data about the face for any purpose. The maximum length is 1KB.
    :type user_data: str
    :param target_face: A face rectangle to specify the target face to be added to a person in the format of \&quot;targetFace&#x3D;left,top,width,height\&quot;. E.g. \&quot;targetFace&#x3D;10,10,100,100\&quot;. If there is more than one face in the image, targetFace is required to specify which face to add. No targetFace means there is only one face detected in the entire image.
    :type target_face: List[int]
    :param detection_model: Name of detection model. Detection model is used to detect faces in the submitted image. A detection model name can be provided when performing Face - Detect or (Large)FaceList - Add Face or (Large)PersonGroup - Add Face. The default value is &#39;detection_01&#39;, if another model is needed, please explicitly specify it.
    :type detection_model: str

    """
    image_url = FaceDetectWithUrlRequest.from_dict(image_url)
    return web.Response(status=200)


async def large_face_list_create(request: web.Request, large_face_list_id, body) -> web.Response:
    """large_face_list_create

    Create an empty large face list with user-specified largeFaceListId, name, an optional userData and recognitionModel. &lt;br /&gt; Large face list is a list of faces, up to 1,000,000 faces, and used by [Face - Find Similar](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395237). &lt;br /&gt; After creation, user should use [LargeFaceList Face - Add](/docs/services/563879b61984550e40cbbe8d/operations/5a158c10d2de3616c086f2d3) to import the faces and [LargeFaceList - Train](/docs/services/563879b61984550e40cbbe8d/operations/5a158422d2de3616c086f2d1) to make it ready for [Face - Find Similar](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395237). No image will be stored. Only the extracted face features are stored on server until [LargeFaceList - Delete](/docs/services/563879b61984550e40cbbe8d/operations/5a1580d5d2de3616c086f2cd) is called. &lt;br /&gt; Find Similar is used for scenario like finding celebrity-like faces, similar face filtering, or as a light way face identification. But if the actual use is to identify person, please use [PersonGroup](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395244) / [LargePersonGroup](/docs/services/563879b61984550e40cbbe8d/operations/599acdee6ac60f11b48b5a9d) and [Face - Identify](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395239). &lt;br/&gt;&#39;recognitionModel&#39; should be specified to associate with this large face list. The default value for &#39;recognitionModel&#39; is &#39;recognition_01&#39;, if the latest model needed, please explicitly specify the model you need in this parameter. New faces that are added to an existing large face list will use the recognition model that&#39;s already associated with the collection. Existing face features in a large face list can&#39;t be updated to features extracted by another version of recognition model. * &#39;recognition_01&#39;: The default recognition model for [LargeFaceList- Create](/docs/services/563879b61984550e40cbbe8d/operations/5a157b68d2de3616c086f2cc). All those large face lists created before 2019 March are bonded with this recognition model. * &#39;recognition_02&#39;: Recognition model released in 2019 March. &#39;recognition_02&#39; is recommended since its overall accuracy is improved compared with &#39;recognition_01&#39;.  Large face list quota: * Free-tier subscription quota: 64 large face lists. * S0-tier subscription quota: 1,000,000 large face lists.

    :param large_face_list_id: Id referencing a particular large face list.
    :type large_face_list_id: str
    :param body: Request body for creating a large face list.
    :type body: dict | bytes

    """
    body = MetaDataContract.from_dict(body)
    return web.Response(status=200)


async def large_face_list_delete(request: web.Request, large_face_list_id) -> web.Response:
    """large_face_list_delete

    Delete a specified large face list.

    :param large_face_list_id: Id referencing a particular large face list.
    :type large_face_list_id: str

    """
    return web.Response(status=200)


async def large_face_list_delete_face(request: web.Request, large_face_list_id, persisted_face_id) -> web.Response:
    """large_face_list_delete_face

    Delete a face from a large face list by specified largeFaceListId and persistedFaceId. &lt;br /&gt; Adding/deleting faces to/from a same large face list are processed sequentially and to/from different large face lists are in parallel.

    :param large_face_list_id: Id referencing a particular large face list.
    :type large_face_list_id: str
    :param persisted_face_id: Id referencing a particular persistedFaceId of an existing face.
    :type persisted_face_id: str
    :type persisted_face_id: str

    """
    return web.Response(status=200)


async def large_face_list_get(request: web.Request, large_face_list_id, return_recognition_model=None) -> web.Response:
    """large_face_list_get

    Retrieve a large face list’s largeFaceListId, name, userData and recognitionModel.

    :param large_face_list_id: Id referencing a particular large face list.
    :type large_face_list_id: str
    :param return_recognition_model: A value indicating whether the operation should return &#39;recognitionModel&#39; in response.
    :type return_recognition_model: bool

    """
    return web.Response(status=200)


async def large_face_list_get_face(request: web.Request, large_face_list_id, persisted_face_id) -> web.Response:
    """large_face_list_get_face

    Retrieve information about a persisted face (specified by persistedFaceId and its belonging largeFaceListId).

    :param large_face_list_id: Id referencing a particular large face list.
    :type large_face_list_id: str
    :param persisted_face_id: Id referencing a particular persistedFaceId of an existing face.
    :type persisted_face_id: str
    :type persisted_face_id: str

    """
    return web.Response(status=200)


async def large_face_list_get_training_status(request: web.Request, large_face_list_id) -> web.Response:
    """large_face_list_get_training_status

    Retrieve the training status of a large face list (completed or ongoing).

    :param large_face_list_id: Id referencing a particular large face list.
    :type large_face_list_id: str

    """
    return web.Response(status=200)


async def large_face_list_list(request: web.Request, return_recognition_model=None) -> web.Response:
    """large_face_list_list

    List large face lists’ information of largeFaceListId, name, userData and recognitionModel. &lt;br /&gt;  To get face information inside largeFaceList use [LargeFaceList Face - Get](/docs/services/563879b61984550e40cbbe8d/operations/5a158cf2d2de3616c086f2d5)&lt;br /&gt; * Large face lists are stored in alphabetical order of largeFaceListId. * \&quot;start\&quot; parameter (string, optional) is a user-provided largeFaceListId value that returned entries have larger ids by string comparison. \&quot;start\&quot; set to empty to indicate return from the first item. * \&quot;top\&quot; parameter (int, optional) specifies the number of entries to return. A maximal of 1000 entries can be returned in one call. To fetch more, you can specify \&quot;start\&quot; with the last returned entry’s Id of the current call. &lt;br /&gt; For example, total 5 large person lists: \&quot;list1\&quot;, ..., \&quot;list5\&quot;. &lt;br /&gt; \&quot;start&#x3D;&amp;top&#x3D;\&quot; will return all 5 lists. &lt;br /&gt; \&quot;start&#x3D;&amp;top&#x3D;2\&quot; will return \&quot;list1\&quot;, \&quot;list2\&quot;. &lt;br /&gt; \&quot;start&#x3D;list2&amp;top&#x3D;3\&quot; will return \&quot;list3\&quot;, \&quot;list4\&quot;, \&quot;list5\&quot;. 

    :param return_recognition_model: A value indicating whether the operation should return &#39;recognitionModel&#39; in response.
    :type return_recognition_model: bool

    """
    return web.Response(status=200)


async def large_face_list_list_faces(request: web.Request, large_face_list_id, start=None, top=None) -> web.Response:
    """large_face_list_list_faces

    List all faces in a large face list, and retrieve face information (including userData and persistedFaceIds of registered faces of the face).

    :param large_face_list_id: Id referencing a particular large face list.
    :type large_face_list_id: str
    :param start: Starting face id to return (used to list a range of faces).
    :type start: str
    :param top: Number of faces to return starting with the face id indicated by the &#39;start&#39; parameter.
    :type top: int

    """
    return web.Response(status=200)


async def large_face_list_train(request: web.Request, large_face_list_id) -> web.Response:
    """large_face_list_train

    Queue a large face list training task, the training task may not be started immediately.

    :param large_face_list_id: Id referencing a particular large face list.
    :type large_face_list_id: str

    """
    return web.Response(status=200)


async def large_face_list_update(request: web.Request, large_face_list_id, body) -> web.Response:
    """large_face_list_update

    Update information of a large face list.

    :param large_face_list_id: Id referencing a particular large face list.
    :type large_face_list_id: str
    :param body: Request body for updating a large face list.
    :type body: dict | bytes

    """
    body = NameAndUserDataContract.from_dict(body)
    return web.Response(status=200)


async def large_face_list_update_face(request: web.Request, large_face_list_id, persisted_face_id, body) -> web.Response:
    """large_face_list_update_face

    Update a persisted face&#39;s userData field.

    :param large_face_list_id: Id referencing a particular large face list.
    :type large_face_list_id: str
    :param persisted_face_id: Id referencing a particular persistedFaceId of an existing face.
    :type persisted_face_id: str
    :type persisted_face_id: str
    :param body: Request body for updating persisted face.
    :type body: dict | bytes

    """
    body = UpdateFaceRequest.from_dict(body)
    return web.Response(status=200)


async def large_person_group_create(request: web.Request, large_person_group_id, body) -> web.Response:
    """large_person_group_create

    Create a new large person group with user-specified largePersonGroupId, name, an optional userData and recognitionModel. &lt;br /&gt; A large person group is the container of the uploaded person data, including face recognition feature, and up to 1,000,000 people. &lt;br /&gt; After creation, use [LargePersonGroup Person - Create](/docs/services/563879b61984550e40cbbe8d/operations/599adcba3a7b9412a4d53f40) to add person into the group, and call [LargePersonGroup - Train](/docs/services/563879b61984550e40cbbe8d/operations/599ae2d16ac60f11b48b5aa4) to get this group ready for [Face - Identify](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395239). &lt;br /&gt; No image will be stored. Only the person&#39;s extracted face features and userData will be stored on server until [LargePersonGroup Person - Delete](/docs/services/563879b61984550e40cbbe8d/operations/599ade5c6ac60f11b48b5aa2) or [LargePersonGroup - Delete](/docs/services/563879b61984550e40cbbe8d/operations/599adc216ac60f11b48b5a9f) is called. &lt;br/&gt;&#39;recognitionModel&#39; should be specified to associate with this large person group. The default value for &#39;recognitionModel&#39; is &#39;recognition_01&#39;, if the latest model needed, please explicitly specify the model you need in this parameter. New faces that are added to an existing large person group will use the recognition model that&#39;s already associated with the collection. Existing face features in a large person group can&#39;t be updated to features extracted by another version of recognition model. * &#39;recognition_01&#39;: The default recognition model for [LargePersonGroup - Create](/docs/services/563879b61984550e40cbbe8d/operations/599acdee6ac60f11b48b5a9d). All those large person groups created before 2019 March are bonded with this recognition model. * &#39;recognition_02&#39;: Recognition model released in 2019 March. &#39;recognition_02&#39; is recommended since its overall accuracy is improved compared with &#39;recognition_01&#39;.  Large person group quota: * Free-tier subscription quota: 1,000 large person groups. * S0-tier subscription quota: 1,000,000 large person groups.

    :param large_person_group_id: Id referencing a particular large person group.
    :type large_person_group_id: str
    :param body: Request body for creating new large person group.
    :type body: dict | bytes

    """
    body = MetaDataContract.from_dict(body)
    return web.Response(status=200)


async def large_person_group_delete(request: web.Request, large_person_group_id) -> web.Response:
    """large_person_group_delete

    Delete an existing large person group. Persisted face features of all people in the large person group will also be deleted.

    :param large_person_group_id: Id referencing a particular large person group.
    :type large_person_group_id: str

    """
    return web.Response(status=200)


async def large_person_group_get(request: web.Request, large_person_group_id, return_recognition_model=None) -> web.Response:
    """large_person_group_get

    Retrieve the information of a large person group, including its name, userData and recognitionModel. This API returns large person group information only, use [LargePersonGroup Person - List](/docs/services/563879b61984550e40cbbe8d/operations/599adda06ac60f11b48b5aa1) instead to retrieve person information under the large person group. 

    :param large_person_group_id: Id referencing a particular large person group.
    :type large_person_group_id: str
    :param return_recognition_model: A value indicating whether the operation should return &#39;recognitionModel&#39; in response.
    :type return_recognition_model: bool

    """
    return web.Response(status=200)


async def large_person_group_get_training_status(request: web.Request, large_person_group_id) -> web.Response:
    """large_person_group_get_training_status

    Retrieve the training status of a large person group (completed or ongoing).

    :param large_person_group_id: Id referencing a particular large person group.
    :type large_person_group_id: str

    """
    return web.Response(status=200)


async def large_person_group_list(request: web.Request, start=None, top=None, return_recognition_model=None) -> web.Response:
    """large_person_group_list

    List all existing large person groups’ largePersonGroupId, name, userData and recognitionModel.&lt;br /&gt; * Large person groups are stored in alphabetical order of largePersonGroupId. * \&quot;start\&quot; parameter (string, optional) is a user-provided largePersonGroupId value that returned entries have larger ids by string comparison. \&quot;start\&quot; set to empty to indicate return from the first item. * \&quot;top\&quot; parameter (int, optional) specifies the number of entries to return. A maximal of 1000 entries can be returned in one call. To fetch more, you can specify \&quot;start\&quot; with the last returned entry’s Id of the current call. &lt;br /&gt; For example, total 5 large person groups: \&quot;group1\&quot;, ..., \&quot;group5\&quot;. &lt;br /&gt; \&quot;start&#x3D;&amp;top&#x3D;\&quot; will return all 5 groups. &lt;br /&gt; \&quot;start&#x3D;&amp;top&#x3D;2\&quot; will return \&quot;group1\&quot;, \&quot;group2\&quot;. &lt;br /&gt; \&quot;start&#x3D;group2&amp;top&#x3D;3\&quot; will return \&quot;group3\&quot;, \&quot;group4\&quot;, \&quot;group5\&quot;. 

    :param start: List large person groups from the least largePersonGroupId greater than the \&quot;start\&quot;.
    :type start: str
    :param top: The number of large person groups to list.
    :type top: int
    :param return_recognition_model: A value indicating whether the operation should return &#39;recognitionModel&#39; in response.
    :type return_recognition_model: bool

    """
    return web.Response(status=200)


async def large_person_group_person_add_face_from_url(request: web.Request, large_person_group_id, person_id, image_url, user_data=None, target_face=None, detection_model=None) -> web.Response:
    """large_person_group_person_add_face_from_url

    Add a face to a person into a large person group for face identification or verification. To deal with an image contains multiple faces, input face can be specified as an image with a targetFace rectangle. It returns a persistedFaceId representing the added face. No image will be stored. Only the extracted face feature will be stored on server until [LargePersonGroup PersonFace - Delete](/docs/services/563879b61984550e40cbbe8d/operations/599ae2966ac60f11b48b5aa3), [LargePersonGroup Person - Delete](/docs/services/563879b61984550e40cbbe8d/operations/599ade5c6ac60f11b48b5aa2) or [LargePersonGroup - Delete](/docs/services/563879b61984550e40cbbe8d/operations/599adc216ac60f11b48b5a9f) is called. &lt;br /&gt; Note persistedFaceId is different from faceId generated by [Face - Detect](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395236). * Higher face image quality means better recognition precision. Please consider high-quality faces: frontal, clear, and face size is 200x200 pixels (100 pixels between eyes) or bigger. * Each person entry can hold up to 248 faces. * JPEG, PNG, GIF (the first frame), and BMP format are supported. The allowed image file size is from 1KB to 6MB. * \&quot;targetFace\&quot; rectangle should contain one face. Zero or multiple faces will be regarded as an error. If the provided \&quot;targetFace\&quot; rectangle is not returned from [Face - Detect](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395236), there’s no guarantee to detect and add the face successfully. * Out of detectable face size (36x36 - 4096x4096 pixels), large head-pose, or large occlusions will cause failures. * Adding/deleting faces to/from a same person will be processed sequentially. Adding/deleting faces to/from different persons are processed in parallel. * The minimum detectable face size is 36x36 pixels in an image no larger than 1920x1080 pixels. Images with dimensions higher than 1920x1080 pixels will need a proportionally larger minimum face size. * Different &#39;detectionModel&#39; values can be provided. To use and compare different detection models, please refer to [How to specify a detection model](https://docs.microsoft.com/en-us/azure/cognitive-services/face/face-api-how-to-topics/specify-detection-model)   | Model | Recommended use-case(s) |   | ---------- | -------- |   | &#39;detection_01&#39;: | The default detection model for [LargePersonGroup Person - Add Face](/docs/services/563879b61984550e40cbbe8d/operations/599adf2a3a7b9412a4d53f42). Recommend for near frontal face detection. For scenarios with exceptionally large angle (head-pose) faces, occluded faces or wrong image orientation, the faces in such cases may not be detected. |   | &#39;detection_02&#39;: | Detection model released in 2019 May with improved accuracy especially on small, side and blurry faces. |

    :param large_person_group_id: Id referencing a particular large person group.
    :type large_person_group_id: str
    :param person_id: Id referencing a particular person.
    :type person_id: str
    :type person_id: str
    :param image_url: A JSON document with a URL pointing to the image that is to be analyzed.
    :type image_url: dict | bytes
    :param user_data: User-specified data about the face for any purpose. The maximum length is 1KB.
    :type user_data: str
    :param target_face: A face rectangle to specify the target face to be added to a person in the format of \&quot;targetFace&#x3D;left,top,width,height\&quot;. E.g. \&quot;targetFace&#x3D;10,10,100,100\&quot;. If there is more than one face in the image, targetFace is required to specify which face to add. No targetFace means there is only one face detected in the entire image.
    :type target_face: List[int]
    :param detection_model: Name of detection model. Detection model is used to detect faces in the submitted image. A detection model name can be provided when performing Face - Detect or (Large)FaceList - Add Face or (Large)PersonGroup - Add Face. The default value is &#39;detection_01&#39;, if another model is needed, please explicitly specify it.
    :type detection_model: str

    """
    image_url = FaceDetectWithUrlRequest.from_dict(image_url)
    return web.Response(status=200)


async def large_person_group_person_create(request: web.Request, large_person_group_id, body) -> web.Response:
    """large_person_group_person_create

    Create a new person in a specified large person group.

    :param large_person_group_id: Id referencing a particular large person group.
    :type large_person_group_id: str
    :param body: Request body for creating new person.
    :type body: dict | bytes

    """
    body = NameAndUserDataContract.from_dict(body)
    return web.Response(status=200)


async def large_person_group_person_delete(request: web.Request, large_person_group_id, person_id) -> web.Response:
    """large_person_group_person_delete

    Delete an existing person from a large person group. The persistedFaceId, userData, person name and face feature in the person entry will all be deleted.

    :param large_person_group_id: Id referencing a particular large person group.
    :type large_person_group_id: str
    :param person_id: Id referencing a particular person.
    :type person_id: str
    :type person_id: str

    """
    return web.Response(status=200)


async def large_person_group_person_delete_face(request: web.Request, large_person_group_id, person_id, persisted_face_id) -> web.Response:
    """large_person_group_person_delete_face

    Delete a face from a person in a large person group by specified largePersonGroupId, personId and persistedFaceId. &lt;br /&gt; Adding/deleting faces to/from a same person will be processed sequentially. Adding/deleting faces to/from different persons are processed in parallel.

    :param large_person_group_id: Id referencing a particular large person group.
    :type large_person_group_id: str
    :param person_id: Id referencing a particular person.
    :type person_id: str
    :type person_id: str
    :param persisted_face_id: Id referencing a particular persistedFaceId of an existing face.
    :type persisted_face_id: str
    :type persisted_face_id: str

    """
    return web.Response(status=200)


async def large_person_group_person_get(request: web.Request, large_person_group_id, person_id) -> web.Response:
    """large_person_group_person_get

    Retrieve a person&#39;s name and userData, and the persisted faceIds representing the registered person face feature.

    :param large_person_group_id: Id referencing a particular large person group.
    :type large_person_group_id: str
    :param person_id: Id referencing a particular person.
    :type person_id: str
    :type person_id: str

    """
    return web.Response(status=200)


async def large_person_group_person_get_face(request: web.Request, large_person_group_id, person_id, persisted_face_id) -> web.Response:
    """large_person_group_person_get_face

    Retrieve information about a persisted face (specified by persistedFaceId, personId and its belonging largePersonGroupId).

    :param large_person_group_id: Id referencing a particular large person group.
    :type large_person_group_id: str
    :param person_id: Id referencing a particular person.
    :type person_id: str
    :type person_id: str
    :param persisted_face_id: Id referencing a particular persistedFaceId of an existing face.
    :type persisted_face_id: str
    :type persisted_face_id: str

    """
    return web.Response(status=200)


async def large_person_group_person_list(request: web.Request, large_person_group_id, start=None, top=None) -> web.Response:
    """large_person_group_person_list

    List all persons in a large person group, and retrieve person information (including personId, name, userData and persistedFaceIds of registered faces of the person).

    :param large_person_group_id: Id referencing a particular large person group.
    :type large_person_group_id: str
    :param start: Starting person id to return (used to list a range of persons).
    :type start: str
    :param top: Number of persons to return starting with the person id indicated by the &#39;start&#39; parameter.
    :type top: int

    """
    return web.Response(status=200)


async def large_person_group_person_update(request: web.Request, large_person_group_id, person_id, body) -> web.Response:
    """large_person_group_person_update

    Update name or userData of a person.

    :param large_person_group_id: Id referencing a particular large person group.
    :type large_person_group_id: str
    :param person_id: Id referencing a particular person.
    :type person_id: str
    :type person_id: str
    :param body: Request body for person update operation.
    :type body: dict | bytes

    """
    body = NameAndUserDataContract.from_dict(body)
    return web.Response(status=200)


async def large_person_group_person_update_face(request: web.Request, large_person_group_id, person_id, persisted_face_id, body) -> web.Response:
    """large_person_group_person_update_face

    Update a person persisted face&#39;s userData field.

    :param large_person_group_id: Id referencing a particular large person group.
    :type large_person_group_id: str
    :param person_id: Id referencing a particular person.
    :type person_id: str
    :type person_id: str
    :param persisted_face_id: Id referencing a particular persistedFaceId of an existing face.
    :type persisted_face_id: str
    :type persisted_face_id: str
    :param body: Request body for updating persisted face.
    :type body: dict | bytes

    """
    body = UpdateFaceRequest.from_dict(body)
    return web.Response(status=200)


async def large_person_group_train(request: web.Request, large_person_group_id) -> web.Response:
    """large_person_group_train

    Queue a large person group training task, the training task may not be started immediately.

    :param large_person_group_id: Id referencing a particular large person group.
    :type large_person_group_id: str

    """
    return web.Response(status=200)


async def large_person_group_update(request: web.Request, large_person_group_id, body) -> web.Response:
    """large_person_group_update

    Update an existing large person group&#39;s display name and userData. The properties which does not appear in request body will not be updated.

    :param large_person_group_id: Id referencing a particular large person group.
    :type large_person_group_id: str
    :param body: Request body for updating large person group.
    :type body: dict | bytes

    """
    body = NameAndUserDataContract.from_dict(body)
    return web.Response(status=200)


async def person_group_create(request: web.Request, person_group_id, body) -> web.Response:
    """person_group_create

    Create a new person group with specified personGroupId, name, user-provided userData and recognitionModel. &lt;br /&gt; A person group is the container of the uploaded person data, including face recognition features. &lt;br /&gt; After creation, use [PersonGroup Person - Create](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f3039523c) to add persons into the group, and then call [PersonGroup - Train](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395249) to get this group ready for [Face - Identify](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395239). &lt;br /&gt; No image will be stored. Only the person&#39;s extracted face features and userData will be stored on server until [PersonGroup Person - Delete](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f3039523d) or [PersonGroup - Delete](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395245) is called. &lt;br/&gt;&#39;recognitionModel&#39; should be specified to associate with this person group. The default value for &#39;recognitionModel&#39; is &#39;recognition_01&#39;, if the latest model needed, please explicitly specify the model you need in this parameter. New faces that are added to an existing person group will use the recognition model that&#39;s already associated with the collection. Existing face features in a person group can&#39;t be updated to features extracted by another version of recognition model. * &#39;recognition_01&#39;: The default recognition model for [PersonGroup - Create](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395244). All those person groups created before 2019 March are bonded with this recognition model. * &#39;recognition_02&#39;: Recognition model released in 2019 March. &#39;recognition_02&#39; is recommended since its overall accuracy is improved compared with &#39;recognition_01&#39;.  Person group quota: * Free-tier subscription quota: 1,000 person groups. Each holds up to 1,000 persons. * S0-tier subscription quota: 1,000,000 person groups. Each holds up to 10,000 persons. * to handle larger scale face identification problem, please consider using [LargePersonGroup](/docs/services/563879b61984550e40cbbe8d/operations/599acdee6ac60f11b48b5a9d).

    :param person_group_id: Id referencing a particular person group.
    :type person_group_id: str
    :param body: Request body for creating new person group.
    :type body: dict | bytes

    """
    body = MetaDataContract.from_dict(body)
    return web.Response(status=200)


async def person_group_delete(request: web.Request, person_group_id) -> web.Response:
    """person_group_delete

    Delete an existing person group. Persisted face features of all people in the person group will also be deleted.

    :param person_group_id: Id referencing a particular person group.
    :type person_group_id: str

    """
    return web.Response(status=200)


async def person_group_get(request: web.Request, person_group_id, return_recognition_model=None) -> web.Response:
    """person_group_get

    Retrieve person group name, userData and recognitionModel. To get person information under this personGroup, use [PersonGroup Person - List](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395241).

    :param person_group_id: Id referencing a particular person group.
    :type person_group_id: str
    :param return_recognition_model: A value indicating whether the operation should return &#39;recognitionModel&#39; in response.
    :type return_recognition_model: bool

    """
    return web.Response(status=200)


async def person_group_get_training_status(request: web.Request, person_group_id) -> web.Response:
    """person_group_get_training_status

    Retrieve the training status of a person group (completed or ongoing).

    :param person_group_id: Id referencing a particular person group.
    :type person_group_id: str

    """
    return web.Response(status=200)


async def person_group_list(request: web.Request, start=None, top=None, return_recognition_model=None) -> web.Response:
    """person_group_list

    List person groups’ personGroupId, name, userData and recognitionModel.&lt;br /&gt; * Person groups are stored in alphabetical order of personGroupId. * \&quot;start\&quot; parameter (string, optional) is a user-provided personGroupId value that returned entries have larger ids by string comparison. \&quot;start\&quot; set to empty to indicate return from the first item. * \&quot;top\&quot; parameter (int, optional) specifies the number of entries to return. A maximal of 1000 entries can be returned in one call. To fetch more, you can specify \&quot;start\&quot; with the last returned entry’s Id of the current call. &lt;br /&gt; For example, total 5 person groups: \&quot;group1\&quot;, ..., \&quot;group5\&quot;. &lt;br /&gt; \&quot;start&#x3D;&amp;top&#x3D;\&quot; will return all 5 groups. &lt;br /&gt; \&quot;start&#x3D;&amp;top&#x3D;2\&quot; will return \&quot;group1\&quot;, \&quot;group2\&quot;. &lt;br /&gt; \&quot;start&#x3D;group2&amp;top&#x3D;3\&quot; will return \&quot;group3\&quot;, \&quot;group4\&quot;, \&quot;group5\&quot;. 

    :param start: List person groups from the least personGroupId greater than the \&quot;start\&quot;.
    :type start: str
    :param top: The number of person groups to list.
    :type top: int
    :param return_recognition_model: A value indicating whether the operation should return &#39;recognitionModel&#39; in response.
    :type return_recognition_model: bool

    """
    return web.Response(status=200)


async def person_group_person_add_face_from_url(request: web.Request, person_group_id, person_id, image_url, user_data=None, target_face=None, detection_model=None) -> web.Response:
    """person_group_person_add_face_from_url

    Add a face to a person into a person group for face identification or verification. To deal with an image contains multiple faces, input face can be specified as an image with a targetFace rectangle. It returns a persistedFaceId representing the added face. No image will be stored. Only the extracted face feature will be stored on server until [PersonGroup PersonFace - Delete](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f3039523e), [PersonGroup Person - Delete](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f3039523d) or [PersonGroup - Delete](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395245) is called. &lt;br /&gt; Note persistedFaceId is different from faceId generated by [Face - Detect](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395236). *   Higher face image quality means better recognition precision. Please consider high-quality faces: frontal, clear, and face size is 200x200 pixels (100 pixels between eyes) or bigger. *   Each person entry can hold up to 248 faces. *   JPEG, PNG, GIF (the first frame), and BMP format are supported. The allowed image file size is from 1KB to 6MB. *   \&quot;targetFace\&quot; rectangle should contain one face. Zero or multiple faces will be regarded as an error. If the provided \&quot;targetFace\&quot; rectangle is not returned from [Face - Detect](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395236), there’s no guarantee to detect and add the face successfully. *   Out of detectable face size (36x36 - 4096x4096 pixels), large head-pose, or large occlusions will cause failures. *   Adding/deleting faces to/from a same person will be processed sequentially. Adding/deleting faces to/from different persons are processed in parallel. * The minimum detectable face size is 36x36 pixels in an image no larger than 1920x1080 pixels. Images with dimensions higher than 1920x1080 pixels will need a proportionally larger minimum face size. * Different &#39;detectionModel&#39; values can be provided. To use and compare different detection models, please refer to [How to specify a detection model](https://docs.microsoft.com/en-us/azure/cognitive-services/face/face-api-how-to-topics/specify-detection-model)   | Model | Recommended use-case(s) |   | ---------- | -------- |   | &#39;detection_01&#39;: | The default detection model for [PersonGroup Person - Add Face](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f3039523b). Recommend for near frontal face detection. For scenarios with exceptionally large angle (head-pose) faces, occluded faces or wrong image orientation, the faces in such cases may not be detected. |   | &#39;detection_02&#39;: | Detection model released in 2019 May with improved accuracy especially on small, side and blurry faces. |

    :param person_group_id: Id referencing a particular person group.
    :type person_group_id: str
    :param person_id: Id referencing a particular person.
    :type person_id: str
    :type person_id: str
    :param image_url: A JSON document with a URL pointing to the image that is to be analyzed.
    :type image_url: dict | bytes
    :param user_data: User-specified data about the face for any purpose. The maximum length is 1KB.
    :type user_data: str
    :param target_face: A face rectangle to specify the target face to be added to a person in the format of \&quot;targetFace&#x3D;left,top,width,height\&quot;. E.g. \&quot;targetFace&#x3D;10,10,100,100\&quot;. If there is more than one face in the image, targetFace is required to specify which face to add. No targetFace means there is only one face detected in the entire image.
    :type target_face: List[int]
    :param detection_model: Name of detection model. Detection model is used to detect faces in the submitted image. A detection model name can be provided when performing Face - Detect or (Large)FaceList - Add Face or (Large)PersonGroup - Add Face. The default value is &#39;detection_01&#39;, if another model is needed, please explicitly specify it.
    :type detection_model: str

    """
    image_url = FaceDetectWithUrlRequest.from_dict(image_url)
    return web.Response(status=200)


async def person_group_person_create(request: web.Request, person_group_id, body) -> web.Response:
    """person_group_person_create

    Create a new person in a specified person group.

    :param person_group_id: Id referencing a particular person group.
    :type person_group_id: str
    :param body: Request body for creating new person.
    :type body: dict | bytes

    """
    body = NameAndUserDataContract.from_dict(body)
    return web.Response(status=200)


async def person_group_person_delete(request: web.Request, person_group_id, person_id) -> web.Response:
    """person_group_person_delete

    Delete an existing person from a person group. The persistedFaceId, userData, person name and face feature in the person entry will all be deleted.

    :param person_group_id: Id referencing a particular person group.
    :type person_group_id: str
    :param person_id: Id referencing a particular person.
    :type person_id: str
    :type person_id: str

    """
    return web.Response(status=200)


async def person_group_person_delete_face(request: web.Request, person_group_id, person_id, persisted_face_id) -> web.Response:
    """person_group_person_delete_face

    Delete a face from a person in a person group by specified personGroupId, personId and persistedFaceId. &lt;br /&gt; Adding/deleting faces to/from a same person will be processed sequentially. Adding/deleting faces to/from different persons are processed in parallel.

    :param person_group_id: Id referencing a particular person group.
    :type person_group_id: str
    :param person_id: Id referencing a particular person.
    :type person_id: str
    :type person_id: str
    :param persisted_face_id: Id referencing a particular persistedFaceId of an existing face.
    :type persisted_face_id: str
    :type persisted_face_id: str

    """
    return web.Response(status=200)


async def person_group_person_get(request: web.Request, person_group_id, person_id) -> web.Response:
    """person_group_person_get

    Retrieve a person&#39;s information, including registered persisted faces, name and userData.

    :param person_group_id: Id referencing a particular person group.
    :type person_group_id: str
    :param person_id: Id referencing a particular person.
    :type person_id: str
    :type person_id: str

    """
    return web.Response(status=200)


async def person_group_person_get_face(request: web.Request, person_group_id, person_id, persisted_face_id) -> web.Response:
    """person_group_person_get_face

    Retrieve information about a persisted face (specified by persistedFaceId, personId and its belonging personGroupId).

    :param person_group_id: Id referencing a particular person group.
    :type person_group_id: str
    :param person_id: Id referencing a particular person.
    :type person_id: str
    :type person_id: str
    :param persisted_face_id: Id referencing a particular persistedFaceId of an existing face.
    :type persisted_face_id: str
    :type persisted_face_id: str

    """
    return web.Response(status=200)


async def person_group_person_list(request: web.Request, person_group_id, start=None, top=None) -> web.Response:
    """person_group_person_list

    List all persons in a person group, and retrieve person information (including personId, name, userData and persistedFaceIds of registered faces of the person).

    :param person_group_id: Id referencing a particular person group.
    :type person_group_id: str
    :param start: Starting person id to return (used to list a range of persons).
    :type start: str
    :param top: Number of persons to return starting with the person id indicated by the &#39;start&#39; parameter.
    :type top: int

    """
    return web.Response(status=200)


async def person_group_person_update(request: web.Request, person_group_id, person_id, body) -> web.Response:
    """person_group_person_update

    Update name or userData of a person.

    :param person_group_id: Id referencing a particular person group.
    :type person_group_id: str
    :param person_id: Id referencing a particular person.
    :type person_id: str
    :type person_id: str
    :param body: Request body for person update operation.
    :type body: dict | bytes

    """
    body = NameAndUserDataContract.from_dict(body)
    return web.Response(status=200)


async def person_group_person_update_face(request: web.Request, person_group_id, person_id, persisted_face_id, body) -> web.Response:
    """person_group_person_update_face

    Add a face to a person into a person group for face identification or verification. To deal with an image contains multiple faces, input face can be specified as an image with a targetFace rectangle. It returns a persistedFaceId representing the added face. No image will be stored. Only the extracted face feature will be stored on server until [PersonGroup PersonFace - Delete](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f3039523e), [PersonGroup Person - Delete](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f3039523d) or [PersonGroup - Delete](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395245) is called. &lt;br /&gt; Note persistedFaceId is different from faceId generated by [Face - Detect](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395236). * Higher face image quality means better recognition precision. Please consider high-quality faces: frontal, clear, and face size is 200x200 pixels (100 pixels between eyes) or bigger. * Each person entry can hold up to 248 faces. * JPEG, PNG, GIF (the first frame), and BMP format are supported. The allowed image file size is from 1KB to 6MB. * \&quot;targetFace\&quot; rectangle should contain one face. Zero or multiple faces will be regarded as an error. If the provided \&quot;targetFace\&quot; rectangle is not returned from [Face - Detect](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395236), there’s no guarantee to detect and add the face successfully. * Out of detectable face size (36x36 - 4096x4096 pixels), large head-pose, or large occlusions will cause failures. * Adding/deleting faces to/from a same person will be processed sequentially. Adding/deleting faces to/from different persons are processed in parallel.

    :param person_group_id: Id referencing a particular person group.
    :type person_group_id: str
    :param person_id: Id referencing a particular person.
    :type person_id: str
    :type person_id: str
    :param persisted_face_id: Id referencing a particular persistedFaceId of an existing face.
    :type persisted_face_id: str
    :type persisted_face_id: str
    :param body: Request body for updating persisted face.
    :type body: dict | bytes

    """
    body = UpdateFaceRequest.from_dict(body)
    return web.Response(status=200)


async def person_group_train(request: web.Request, person_group_id) -> web.Response:
    """person_group_train

    Queue a person group training task, the training task may not be started immediately.

    :param person_group_id: Id referencing a particular person group.
    :type person_group_id: str

    """
    return web.Response(status=200)


async def person_group_update(request: web.Request, person_group_id, body) -> web.Response:
    """person_group_update

    Update an existing person group&#39;s display name and userData. The properties which does not appear in request body will not be updated.

    :param person_group_id: Id referencing a particular person group.
    :type person_group_id: str
    :param body: Request body for updating person group.
    :type body: dict | bytes

    """
    body = NameAndUserDataContract.from_dict(body)
    return web.Response(status=200)


async def snapshot_apply(request: web.Request, snapshot_id, body) -> web.Response:
    """snapshot_apply

    Submit an operation to apply a snapshot to current subscription. For each snapshot, only subscriptions included in the applyScope of Snapshot - Take can apply it.&lt;br /&gt; The snapshot interfaces are for users to backup and restore their face data from one face subscription to another, inside same region or across regions. The workflow contains two phases, user first calls Snapshot - Take to create a copy of the source object and store it as a snapshot, then calls Snapshot - Apply to paste the snapshot to target subscription. The snapshots are stored in a centralized location (per Azure instance), so that they can be applied cross accounts and regions.&lt;br /&gt; Applying snapshot is an asynchronous operation. An operation id can be obtained from the \&quot;Operation-Location\&quot; field in response header, to be used in OperationStatus - Get for tracking the progress of applying the snapshot. The target object id will be included in the \&quot;resourceLocation\&quot; field in OperationStatus - Get response when the operation status is \&quot;succeeded\&quot;.&lt;br /&gt; Snapshot applying time depends on the number of person and face entries in the snapshot object. It could be in seconds, or up to 1 hour for 1,000,000 persons with multiple faces.&lt;br /&gt; Snapshots will be automatically expired and cleaned in 48 hours after it is created by Snapshot - Take. So the target subscription is required to apply the snapshot in 48 hours since its creation.&lt;br /&gt; Applying a snapshot will not block any other operations against the target object, however it is not recommended because the correctness cannot be guaranteed during snapshot applying. After snapshot applying is completed, all operations towards the target object can work as normal. Snapshot also includes the training results of the source object, which means target subscription the snapshot applied to does not need re-train the target object before calling Identify/FindSimilar.&lt;br /&gt; One snapshot can be applied multiple times in parallel, while currently only CreateNew apply mode is supported, which means the apply operation will fail if target subscription already contains an object of same type and using the same objectId. Users can specify the \&quot;objectId\&quot; in request body to avoid such conflicts.&lt;br /&gt; * Free-tier subscription quota: 100 apply operations per month. * S0-tier subscription quota: 100 apply operations per day.

    :param snapshot_id: Id referencing a particular snapshot.
    :type snapshot_id: str
    :type snapshot_id: str
    :param body: Request body for applying a snapshot.
    :type body: dict | bytes

    """
    body = ApplySnapshotRequest.from_dict(body)
    return web.Response(status=200)


async def snapshot_delete(request: web.Request, snapshot_id) -> web.Response:
    """snapshot_delete

    Delete an existing snapshot according to the snapshotId. All object data and information in the snapshot will also be deleted. Only the source subscription who took the snapshot can delete the snapshot. If the user does not delete a snapshot with this API, the snapshot will still be automatically deleted in 48 hours after creation.

    :param snapshot_id: Id referencing a particular snapshot.
    :type snapshot_id: str
    :type snapshot_id: str

    """
    return web.Response(status=200)


async def snapshot_get(request: web.Request, snapshot_id) -> web.Response:
    """snapshot_get

    Retrieve information about a snapshot. Snapshot is only accessible to the source subscription who took it, and target subscriptions included in the applyScope in Snapshot - Take.

    :param snapshot_id: Id referencing a particular snapshot.
    :type snapshot_id: str
    :type snapshot_id: str

    """
    return web.Response(status=200)


async def snapshot_get_operation_status(request: web.Request, operation_id) -> web.Response:
    """snapshot_get_operation_status

    Retrieve the status of a take/apply snapshot operation.

    :param operation_id: Id referencing a particular take/apply snapshot operation.
    :type operation_id: str
    :type operation_id: str

    """
    return web.Response(status=200)


async def snapshot_list(request: web.Request, type=None, apply_scope=None) -> web.Response:
    """snapshot_list

    List all accessible snapshots with related information, including snapshots that were taken by the user, or snapshots to be applied to the user (subscription id was included in the applyScope in Snapshot - Take).

    :param type: User specified object type as a search filter.
    :type type: str
    :param apply_scope: User specified snapshot apply scopes as a search filter. ApplyScope is an array of the target Azure subscription ids for the snapshot, specified by the user who created the snapshot by Snapshot - Take.
    :type apply_scope: List[str]

    """
    return web.Response(status=200)


async def snapshot_take(request: web.Request, body) -> web.Response:
    """snapshot_take

    Submit an operation to take a snapshot of face list, large face list, person group or large person group, with user-specified snapshot type, source object id, apply scope and an optional user data.&lt;br /&gt; The snapshot interfaces are for users to backup and restore their face data from one face subscription to another, inside same region or across regions. The workflow contains two phases, user first calls Snapshot - Take to create a copy of the source object and store it as a snapshot, then calls Snapshot - Apply to paste the snapshot to target subscription. The snapshots are stored in a centralized location (per Azure instance), so that they can be applied cross accounts and regions.&lt;br /&gt; Taking snapshot is an asynchronous operation. An operation id can be obtained from the \&quot;Operation-Location\&quot; field in response header, to be used in OperationStatus - Get for tracking the progress of creating the snapshot. The snapshot id will be included in the \&quot;resourceLocation\&quot; field in OperationStatus - Get response when the operation status is \&quot;succeeded\&quot;.&lt;br /&gt; Snapshot taking time depends on the number of person and face entries in the source object. It could be in seconds, or up to several hours for 1,000,000 persons with multiple faces.&lt;br /&gt; Snapshots will be automatically expired and cleaned in 48 hours after it is created by Snapshot - Take. User can delete the snapshot using Snapshot - Delete by themselves any time before expiration.&lt;br /&gt; Taking snapshot for a certain object will not block any other operations against the object. All read-only operations (Get/List and Identify/FindSimilar/Verify) can be conducted as usual. For all writable operations, including Add/Update/Delete the source object or its persons/faces and Train, they are not blocked but not recommended because writable updates may not be reflected on the snapshot during its taking. After snapshot taking is completed, all readable and writable operations can work as normal. Snapshot will also include the training results of the source object, which means target subscription the snapshot applied to does not need re-train the target object before calling Identify/FindSimilar.&lt;br /&gt; * Free-tier subscription quota: 100 take operations per month. * S0-tier subscription quota: 100 take operations per day.

    :param body: Request body for taking a snapshot.
    :type body: dict | bytes

    """
    body = TakeSnapshotRequest.from_dict(body)
    return web.Response(status=200)


async def snapshot_update(request: web.Request, snapshot_id, body) -> web.Response:
    """snapshot_update

    Update the information of a snapshot. Only the source subscription who took the snapshot can update the snapshot.

    :param snapshot_id: Id referencing a particular snapshot.
    :type snapshot_id: str
    :type snapshot_id: str
    :param body: Request body for updating a snapshot.
    :type body: dict | bytes

    """
    body = UpdateSnapshotRequest.from_dict(body)
    return web.Response(status=200)
