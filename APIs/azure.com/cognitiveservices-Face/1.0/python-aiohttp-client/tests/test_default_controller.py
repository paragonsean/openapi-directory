# coding: utf-8

import pytest
import json
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


pytestmark = pytest.mark.asyncio

async def test_face_detect_with_url(client):
    """Test case for face_detect_with_url

    
    """
    image_url = openapi_server.FaceDetectWithUrlRequest()
    params = [('returnFaceId', True),
                    ('returnFaceLandmarks', False),
                    ('returnFaceAttributes', ['return_face_attributes_example']),
                    ('recognitionModel', recognition_01),
                    ('returnRecognitionModel', False),
                    ('detectionModel', detection_01)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/detect',
        headers=headers,
        json=image_url,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_face_find_similar(client):
    """Test case for face_find_similar

    
    """
    body = {"largeFaceListId":"largeFaceListId","mode":"matchPerson","maxNumOfCandidatesReturned":81,"faceIds":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"faceId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","faceListId":"faceListId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/findsimilars',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_face_group(client):
    """Test case for face_group

    
    """
    body = {"faceIds":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/group',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_face_identify(client):
    """Test case for face_identify

    
    """
    body = {"maxNumOfCandidatesReturned":3,"personGroupId":"personGroupId","confidenceThreshold":0.08008281904610115,"faceIds":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"largePersonGroupId":"largePersonGroupId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/identify',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_face_list_add_face_from_url(client):
    """Test case for face_list_add_face_from_url

    
    """
    image_url = openapi_server.FaceDetectWithUrlRequest()
    params = [('userData', 'user_data_example'),
                    ('targetFace', [56]),
                    ('detectionModel', detection_01)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/facelists/{face_list_id}/persistedfaces'.format(face_list_id='face_list_id_example'),
        headers=headers,
        json=image_url,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_face_list_create(client):
    """Test case for face_list_create

    
    """
    body = {"recognitionModel":"recognition_01"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/facelists/{face_list_id}'.format(face_list_id='face_list_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_face_list_delete(client):
    """Test case for face_list_delete

    
    """
    headers = { 
        'Accept': '*/*',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/facelists/{face_list_id}'.format(face_list_id='face_list_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_face_list_delete_face(client):
    """Test case for face_list_delete_face

    
    """
    headers = { 
        'Accept': '*/*',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/facelists/{face_list_id}/persistedfaces/{persisted_face_id}'.format(face_list_id='face_list_id_example', persisted_face_id='persisted_face_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_face_list_get(client):
    """Test case for face_list_get

    
    """
    params = [('returnRecognitionModel', False)]
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/facelists/{face_list_id}'.format(face_list_id='face_list_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_face_list_list(client):
    """Test case for face_list_list

    
    """
    params = [('returnRecognitionModel', False)]
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/facelists',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_face_list_update(client):
    """Test case for face_list_update

    
    """
    body = {"userData":"userData","name":"name"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/facelists/{face_list_id}'.format(face_list_id='face_list_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_face_verify_face_to_face(client):
    """Test case for face_verify_face_to_face

    
    """
    body = {"faceId2":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","faceId1":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/verify',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_large_face_list_add_face_from_url(client):
    """Test case for large_face_list_add_face_from_url

    
    """
    image_url = openapi_server.FaceDetectWithUrlRequest()
    params = [('userData', 'user_data_example'),
                    ('targetFace', [56]),
                    ('detectionModel', detection_01)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/largefacelists/{large_face_list_id}/persistedfaces'.format(large_face_list_id='large_face_list_id_example'),
        headers=headers,
        json=image_url,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_large_face_list_create(client):
    """Test case for large_face_list_create

    
    """
    body = {"recognitionModel":"recognition_01"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/largefacelists/{large_face_list_id}'.format(large_face_list_id='large_face_list_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_large_face_list_delete(client):
    """Test case for large_face_list_delete

    
    """
    headers = { 
        'Accept': '*/*',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/largefacelists/{large_face_list_id}'.format(large_face_list_id='large_face_list_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_large_face_list_delete_face(client):
    """Test case for large_face_list_delete_face

    
    """
    headers = { 
        'Accept': '*/*',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/largefacelists/{large_face_list_id}/persistedfaces/{persisted_face_id}'.format(large_face_list_id='large_face_list_id_example', persisted_face_id='persisted_face_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_large_face_list_get(client):
    """Test case for large_face_list_get

    
    """
    params = [('returnRecognitionModel', False)]
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/largefacelists/{large_face_list_id}'.format(large_face_list_id='large_face_list_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_large_face_list_get_face(client):
    """Test case for large_face_list_get_face

    
    """
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/largefacelists/{large_face_list_id}/persistedfaces/{persisted_face_id}'.format(large_face_list_id='large_face_list_id_example', persisted_face_id='persisted_face_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_large_face_list_get_training_status(client):
    """Test case for large_face_list_get_training_status

    
    """
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/largefacelists/{large_face_list_id}/training'.format(large_face_list_id='large_face_list_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_large_face_list_list(client):
    """Test case for large_face_list_list

    
    """
    params = [('returnRecognitionModel', False)]
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/largefacelists',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_large_face_list_list_faces(client):
    """Test case for large_face_list_list_faces

    
    """
    params = [('start', 'start_example'),
                    ('top', 56)]
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/largefacelists/{large_face_list_id}/persistedfaces'.format(large_face_list_id='large_face_list_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_large_face_list_train(client):
    """Test case for large_face_list_train

    
    """
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/largefacelists/{large_face_list_id}/train'.format(large_face_list_id='large_face_list_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_large_face_list_update(client):
    """Test case for large_face_list_update

    
    """
    body = {"userData":"userData","name":"name"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/largefacelists/{large_face_list_id}'.format(large_face_list_id='large_face_list_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_large_face_list_update_face(client):
    """Test case for large_face_list_update_face

    
    """
    body = {"userData":"userData"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/largefacelists/{large_face_list_id}/persistedfaces/{persisted_face_id}'.format(large_face_list_id='large_face_list_id_example', persisted_face_id='persisted_face_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_large_person_group_create(client):
    """Test case for large_person_group_create

    
    """
    body = {"recognitionModel":"recognition_01"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/largepersongroups/{large_person_group_id}'.format(large_person_group_id='large_person_group_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_large_person_group_delete(client):
    """Test case for large_person_group_delete

    
    """
    headers = { 
        'Accept': '*/*',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/largepersongroups/{large_person_group_id}'.format(large_person_group_id='large_person_group_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_large_person_group_get(client):
    """Test case for large_person_group_get

    
    """
    params = [('returnRecognitionModel', False)]
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/largepersongroups/{large_person_group_id}'.format(large_person_group_id='large_person_group_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_large_person_group_get_training_status(client):
    """Test case for large_person_group_get_training_status

    
    """
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/largepersongroups/{large_person_group_id}/training'.format(large_person_group_id='large_person_group_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_large_person_group_list(client):
    """Test case for large_person_group_list

    
    """
    params = [('start', 'start_example'),
                    ('top', 1000),
                    ('returnRecognitionModel', False)]
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/largepersongroups',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_large_person_group_person_add_face_from_url(client):
    """Test case for large_person_group_person_add_face_from_url

    
    """
    image_url = openapi_server.FaceDetectWithUrlRequest()
    params = [('userData', 'user_data_example'),
                    ('targetFace', [56]),
                    ('detectionModel', detection_01)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/largepersongroups/{large_person_group_id}/persons/{person_id}/persistedfaces'.format(large_person_group_id='large_person_group_id_example', person_id='person_id_example'),
        headers=headers,
        json=image_url,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_large_person_group_person_create(client):
    """Test case for large_person_group_person_create

    
    """
    body = {"userData":"userData","name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/largepersongroups/{large_person_group_id}/persons'.format(large_person_group_id='large_person_group_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_large_person_group_person_delete(client):
    """Test case for large_person_group_person_delete

    
    """
    headers = { 
        'Accept': '*/*',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/largepersongroups/{large_person_group_id}/persons/{person_id}'.format(large_person_group_id='large_person_group_id_example', person_id='person_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_large_person_group_person_delete_face(client):
    """Test case for large_person_group_person_delete_face

    
    """
    headers = { 
        'Accept': '*/*',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/largepersongroups/{large_person_group_id}/persons/{person_id}/persistedfaces/{persisted_face_id}'.format(large_person_group_id='large_person_group_id_example', person_id='person_id_example', persisted_face_id='persisted_face_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_large_person_group_person_get(client):
    """Test case for large_person_group_person_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/largepersongroups/{large_person_group_id}/persons/{person_id}'.format(large_person_group_id='large_person_group_id_example', person_id='person_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_large_person_group_person_get_face(client):
    """Test case for large_person_group_person_get_face

    
    """
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/largepersongroups/{large_person_group_id}/persons/{person_id}/persistedfaces/{persisted_face_id}'.format(large_person_group_id='large_person_group_id_example', person_id='person_id_example', persisted_face_id='persisted_face_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_large_person_group_person_list(client):
    """Test case for large_person_group_person_list

    
    """
    params = [('start', 'start_example'),
                    ('top', 56)]
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/largepersongroups/{large_person_group_id}/persons'.format(large_person_group_id='large_person_group_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_large_person_group_person_update(client):
    """Test case for large_person_group_person_update

    
    """
    body = {"userData":"userData","name":"name"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/largepersongroups/{large_person_group_id}/persons/{person_id}'.format(large_person_group_id='large_person_group_id_example', person_id='person_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_large_person_group_person_update_face(client):
    """Test case for large_person_group_person_update_face

    
    """
    body = {"userData":"userData"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/largepersongroups/{large_person_group_id}/persons/{person_id}/persistedfaces/{persisted_face_id}'.format(large_person_group_id='large_person_group_id_example', person_id='person_id_example', persisted_face_id='persisted_face_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_large_person_group_train(client):
    """Test case for large_person_group_train

    
    """
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/largepersongroups/{large_person_group_id}/train'.format(large_person_group_id='large_person_group_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_large_person_group_update(client):
    """Test case for large_person_group_update

    
    """
    body = {"userData":"userData","name":"name"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/largepersongroups/{large_person_group_id}'.format(large_person_group_id='large_person_group_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_person_group_create(client):
    """Test case for person_group_create

    
    """
    body = {"recognitionModel":"recognition_01"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/persongroups/{person_group_id}'.format(person_group_id='person_group_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_person_group_delete(client):
    """Test case for person_group_delete

    
    """
    headers = { 
        'Accept': '*/*',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/persongroups/{person_group_id}'.format(person_group_id='person_group_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_person_group_get(client):
    """Test case for person_group_get

    
    """
    params = [('returnRecognitionModel', False)]
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/persongroups/{person_group_id}'.format(person_group_id='person_group_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_person_group_get_training_status(client):
    """Test case for person_group_get_training_status

    
    """
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/persongroups/{person_group_id}/training'.format(person_group_id='person_group_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_person_group_list(client):
    """Test case for person_group_list

    
    """
    params = [('start', 'start_example'),
                    ('top', 1000),
                    ('returnRecognitionModel', False)]
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/persongroups',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_person_group_person_add_face_from_url(client):
    """Test case for person_group_person_add_face_from_url

    
    """
    image_url = openapi_server.FaceDetectWithUrlRequest()
    params = [('userData', 'user_data_example'),
                    ('targetFace', [56]),
                    ('detectionModel', detection_01)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/persongroups/{person_group_id}/persons/{person_id}/persistedfaces'.format(person_group_id='person_group_id_example', person_id='person_id_example'),
        headers=headers,
        json=image_url,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_person_group_person_create(client):
    """Test case for person_group_person_create

    
    """
    body = {"userData":"userData","name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/persongroups/{person_group_id}/persons'.format(person_group_id='person_group_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_person_group_person_delete(client):
    """Test case for person_group_person_delete

    
    """
    headers = { 
        'Accept': '*/*',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/persongroups/{person_group_id}/persons/{person_id}'.format(person_group_id='person_group_id_example', person_id='person_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_person_group_person_delete_face(client):
    """Test case for person_group_person_delete_face

    
    """
    headers = { 
        'Accept': '*/*',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/persongroups/{person_group_id}/persons/{person_id}/persistedfaces/{persisted_face_id}'.format(person_group_id='person_group_id_example', person_id='person_id_example', persisted_face_id='persisted_face_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_person_group_person_get(client):
    """Test case for person_group_person_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/persongroups/{person_group_id}/persons/{person_id}'.format(person_group_id='person_group_id_example', person_id='person_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_person_group_person_get_face(client):
    """Test case for person_group_person_get_face

    
    """
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/persongroups/{person_group_id}/persons/{person_id}/persistedfaces/{persisted_face_id}'.format(person_group_id='person_group_id_example', person_id='person_id_example', persisted_face_id='persisted_face_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_person_group_person_list(client):
    """Test case for person_group_person_list

    
    """
    params = [('start', 'start_example'),
                    ('top', 56)]
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/persongroups/{person_group_id}/persons'.format(person_group_id='person_group_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_person_group_person_update(client):
    """Test case for person_group_person_update

    
    """
    body = {"userData":"userData","name":"name"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/persongroups/{person_group_id}/persons/{person_id}'.format(person_group_id='person_group_id_example', person_id='person_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_person_group_person_update_face(client):
    """Test case for person_group_person_update_face

    
    """
    body = {"userData":"userData"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/persongroups/{person_group_id}/persons/{person_id}/persistedfaces/{persisted_face_id}'.format(person_group_id='person_group_id_example', person_id='person_id_example', persisted_face_id='persisted_face_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_person_group_train(client):
    """Test case for person_group_train

    
    """
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/persongroups/{person_group_id}/train'.format(person_group_id='person_group_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_person_group_update(client):
    """Test case for person_group_update

    
    """
    body = {"userData":"userData","name":"name"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/persongroups/{person_group_id}'.format(person_group_id='person_group_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_snapshot_apply(client):
    """Test case for snapshot_apply

    
    """
    body = {"mode":"CreateNew","objectId":"objectId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/snapshots/{snapshot_id}/apply'.format(snapshot_id='snapshot_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_snapshot_delete(client):
    """Test case for snapshot_delete

    
    """
    headers = { 
        'Accept': '*/*',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/snapshots/{snapshot_id}'.format(snapshot_id='snapshot_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_snapshot_get(client):
    """Test case for snapshot_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/snapshots/{snapshot_id}'.format(snapshot_id='snapshot_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_snapshot_get_operation_status(client):
    """Test case for snapshot_get_operation_status

    
    """
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/operations/{operation_id}'.format(operation_id='operation_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_snapshot_list(client):
    """Test case for snapshot_list

    
    """
    params = [('type', 'type_example'),
                    ('applyScope', ['apply_scope_example'])]
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/snapshots',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_snapshot_take(client):
    """Test case for snapshot_take

    
    """
    body = {"userData":"userData","applyScope":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"type":"FaceList","objectId":"objectId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/snapshots',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_snapshot_update(client):
    """Test case for snapshot_update

    
    """
    body = {"userData":"userData","applyScope":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"]}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/snapshots/{snapshot_id}'.format(snapshot_id='snapshot_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

