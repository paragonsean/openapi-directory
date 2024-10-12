# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
import re
from openapi_server import util


class FindSimilarRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, face_id: str=None, face_ids: List[str]=None, face_list_id: str=None, large_face_list_id: str=None, max_num_of_candidates_returned: int=None, mode: str='matchPerson'):
        """FindSimilarRequest - a model defined in OpenAPI

        :param face_id: The face_id of this FindSimilarRequest.
        :param face_ids: The face_ids of this FindSimilarRequest.
        :param face_list_id: The face_list_id of this FindSimilarRequest.
        :param large_face_list_id: The large_face_list_id of this FindSimilarRequest.
        :param max_num_of_candidates_returned: The max_num_of_candidates_returned of this FindSimilarRequest.
        :param mode: The mode of this FindSimilarRequest.
        """
        self.openapi_types = {
            'face_id': str,
            'face_ids': List[str],
            'face_list_id': str,
            'large_face_list_id': str,
            'max_num_of_candidates_returned': int,
            'mode': str
        }

        self.attribute_map = {
            'face_id': 'faceId',
            'face_ids': 'faceIds',
            'face_list_id': 'faceListId',
            'large_face_list_id': 'largeFaceListId',
            'max_num_of_candidates_returned': 'maxNumOfCandidatesReturned',
            'mode': 'mode'
        }

        self._face_id = face_id
        self._face_ids = face_ids
        self._face_list_id = face_list_id
        self._large_face_list_id = large_face_list_id
        self._max_num_of_candidates_returned = max_num_of_candidates_returned
        self._mode = mode

    @classmethod
    def from_dict(cls, dikt: dict) -> 'FindSimilarRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The FindSimilarRequest of this FindSimilarRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def face_id(self):
        """Gets the face_id of this FindSimilarRequest.

        FaceId of the query face. User needs to call Face - Detect first to get a valid faceId. Note that this faceId is not persisted and will expire 24 hours after the detection call

        :return: The face_id of this FindSimilarRequest.
        :rtype: str
        """
        return self._face_id

    @face_id.setter
    def face_id(self, face_id):
        """Sets the face_id of this FindSimilarRequest.

        FaceId of the query face. User needs to call Face - Detect first to get a valid faceId. Note that this faceId is not persisted and will expire 24 hours after the detection call

        :param face_id: The face_id of this FindSimilarRequest.
        :type face_id: str
        """
        if face_id is None:
            raise ValueError("Invalid value for `face_id`, must not be `None`")

        self._face_id = face_id

    @property
    def face_ids(self):
        """Gets the face_ids of this FindSimilarRequest.

        An array of candidate faceIds. All of them are created by Face - Detect and the faceIds will expire 24 hours after the detection call. The number of faceIds is limited to 1000. Parameter faceListId, largeFaceListId and faceIds should not be provided at the same time.

        :return: The face_ids of this FindSimilarRequest.
        :rtype: List[str]
        """
        return self._face_ids

    @face_ids.setter
    def face_ids(self, face_ids):
        """Sets the face_ids of this FindSimilarRequest.

        An array of candidate faceIds. All of them are created by Face - Detect and the faceIds will expire 24 hours after the detection call. The number of faceIds is limited to 1000. Parameter faceListId, largeFaceListId and faceIds should not be provided at the same time.

        :param face_ids: The face_ids of this FindSimilarRequest.
        :type face_ids: List[str]
        """
        if face_ids is not None and len(face_ids) > 1000:
            raise ValueError("Invalid value for `face_ids`, number of items must be less than or equal to `1000`")

        self._face_ids = face_ids

    @property
    def face_list_id(self):
        """Gets the face_list_id of this FindSimilarRequest.

        An existing user-specified unique candidate face list, created in Face List - Create a Face List. Face list contains a set of persistedFaceIds which are persisted and will never expire. Parameter faceListId, largeFaceListId and faceIds should not be provided at the same time.

        :return: The face_list_id of this FindSimilarRequest.
        :rtype: str
        """
        return self._face_list_id

    @face_list_id.setter
    def face_list_id(self, face_list_id):
        """Sets the face_list_id of this FindSimilarRequest.

        An existing user-specified unique candidate face list, created in Face List - Create a Face List. Face list contains a set of persistedFaceIds which are persisted and will never expire. Parameter faceListId, largeFaceListId and faceIds should not be provided at the same time.

        :param face_list_id: The face_list_id of this FindSimilarRequest.
        :type face_list_id: str
        """
        if face_list_id is not None and len(face_list_id) > 64:
            raise ValueError("Invalid value for `face_list_id`, length must be less than or equal to `64`")
        if face_list_id is not None and not re.search(r'^[a-z0-9-_]+$', face_list_id):
            raise ValueError("Invalid value for `face_list_id`, must be a follow pattern or equal to `/^[a-z0-9-_]+$/`")

        self._face_list_id = face_list_id

    @property
    def large_face_list_id(self):
        """Gets the large_face_list_id of this FindSimilarRequest.

        An existing user-specified unique candidate large face list, created in LargeFaceList - Create. Large face list contains a set of persistedFaceIds which are persisted and will never expire. Parameter faceListId, largeFaceListId and faceIds should not be provided at the same time.

        :return: The large_face_list_id of this FindSimilarRequest.
        :rtype: str
        """
        return self._large_face_list_id

    @large_face_list_id.setter
    def large_face_list_id(self, large_face_list_id):
        """Sets the large_face_list_id of this FindSimilarRequest.

        An existing user-specified unique candidate large face list, created in LargeFaceList - Create. Large face list contains a set of persistedFaceIds which are persisted and will never expire. Parameter faceListId, largeFaceListId and faceIds should not be provided at the same time.

        :param large_face_list_id: The large_face_list_id of this FindSimilarRequest.
        :type large_face_list_id: str
        """
        if large_face_list_id is not None and len(large_face_list_id) > 64:
            raise ValueError("Invalid value for `large_face_list_id`, length must be less than or equal to `64`")
        if large_face_list_id is not None and not re.search(r'^[a-z0-9-_]+$', large_face_list_id):
            raise ValueError("Invalid value for `large_face_list_id`, must be a follow pattern or equal to `/^[a-z0-9-_]+$/`")

        self._large_face_list_id = large_face_list_id

    @property
    def max_num_of_candidates_returned(self):
        """Gets the max_num_of_candidates_returned of this FindSimilarRequest.

        The number of top similar faces returned. The valid range is [1, 1000].

        :return: The max_num_of_candidates_returned of this FindSimilarRequest.
        :rtype: int
        """
        return self._max_num_of_candidates_returned

    @max_num_of_candidates_returned.setter
    def max_num_of_candidates_returned(self, max_num_of_candidates_returned):
        """Sets the max_num_of_candidates_returned of this FindSimilarRequest.

        The number of top similar faces returned. The valid range is [1, 1000].

        :param max_num_of_candidates_returned: The max_num_of_candidates_returned of this FindSimilarRequest.
        :type max_num_of_candidates_returned: int
        """
        if max_num_of_candidates_returned is not None and max_num_of_candidates_returned > 1000:
            raise ValueError("Invalid value for `max_num_of_candidates_returned`, must be a value less than or equal to `1000`")
        if max_num_of_candidates_returned is not None and max_num_of_candidates_returned < 1:
            raise ValueError("Invalid value for `max_num_of_candidates_returned`, must be a value greater than or equal to `1`")

        self._max_num_of_candidates_returned = max_num_of_candidates_returned

    @property
    def mode(self):
        """Gets the mode of this FindSimilarRequest.

        Similar face searching mode. It can be \"matchPerson\" or \"matchFace\".

        :return: The mode of this FindSimilarRequest.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this FindSimilarRequest.

        Similar face searching mode. It can be \"matchPerson\" or \"matchFace\".

        :param mode: The mode of this FindSimilarRequest.
        :type mode: str
        """
        allowed_values = ["matchPerson", "matchFace"]  # noqa: E501
        if mode not in allowed_values:
            raise ValueError(
                "Invalid value for `mode` ({0}), must be one of {1}"
                .format(mode, allowed_values)
            )

        self._mode = mode
