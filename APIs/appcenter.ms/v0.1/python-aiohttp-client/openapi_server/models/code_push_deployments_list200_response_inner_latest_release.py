# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.code_push_deployments_list200_response_inner_latest_release_all_of_diff_package_map_value import CodePushDeploymentsList200ResponseInnerLatestReleaseAllOfDiffPackageMapValue
from openapi_server import util


class CodePushDeploymentsList200ResponseInnerLatestRelease(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, description: str=None, is_disabled: bool=None, is_mandatory: bool=None, rollout: int=None, target_binary_range: str=None, blob_url: str=None, diff_package_map: Dict[str, CodePushDeploymentsList200ResponseInnerLatestReleaseAllOfDiffPackageMapValue]=None, label: str=None, original_deployment: str=None, original_label: str=None, package_hash: str=None, release_method: str=None, released_by: str=None, size: float=None, upload_time: int=None):
        """CodePushDeploymentsList200ResponseInnerLatestRelease - a model defined in OpenAPI

        :param description: The description of this CodePushDeploymentsList200ResponseInnerLatestRelease.
        :param is_disabled: The is_disabled of this CodePushDeploymentsList200ResponseInnerLatestRelease.
        :param is_mandatory: The is_mandatory of this CodePushDeploymentsList200ResponseInnerLatestRelease.
        :param rollout: The rollout of this CodePushDeploymentsList200ResponseInnerLatestRelease.
        :param target_binary_range: The target_binary_range of this CodePushDeploymentsList200ResponseInnerLatestRelease.
        :param blob_url: The blob_url of this CodePushDeploymentsList200ResponseInnerLatestRelease.
        :param diff_package_map: The diff_package_map of this CodePushDeploymentsList200ResponseInnerLatestRelease.
        :param label: The label of this CodePushDeploymentsList200ResponseInnerLatestRelease.
        :param original_deployment: The original_deployment of this CodePushDeploymentsList200ResponseInnerLatestRelease.
        :param original_label: The original_label of this CodePushDeploymentsList200ResponseInnerLatestRelease.
        :param package_hash: The package_hash of this CodePushDeploymentsList200ResponseInnerLatestRelease.
        :param release_method: The release_method of this CodePushDeploymentsList200ResponseInnerLatestRelease.
        :param released_by: The released_by of this CodePushDeploymentsList200ResponseInnerLatestRelease.
        :param size: The size of this CodePushDeploymentsList200ResponseInnerLatestRelease.
        :param upload_time: The upload_time of this CodePushDeploymentsList200ResponseInnerLatestRelease.
        """
        self.openapi_types = {
            'description': str,
            'is_disabled': bool,
            'is_mandatory': bool,
            'rollout': int,
            'target_binary_range': str,
            'blob_url': str,
            'diff_package_map': Dict[str, CodePushDeploymentsList200ResponseInnerLatestReleaseAllOfDiffPackageMapValue],
            'label': str,
            'original_deployment': str,
            'original_label': str,
            'package_hash': str,
            'release_method': str,
            'released_by': str,
            'size': float,
            'upload_time': int
        }

        self.attribute_map = {
            'description': 'description',
            'is_disabled': 'is_disabled',
            'is_mandatory': 'is_mandatory',
            'rollout': 'rollout',
            'target_binary_range': 'target_binary_range',
            'blob_url': 'blob_url',
            'diff_package_map': 'diff_package_map',
            'label': 'label',
            'original_deployment': 'original_deployment',
            'original_label': 'original_label',
            'package_hash': 'package_hash',
            'release_method': 'release_method',
            'released_by': 'released_by',
            'size': 'size',
            'upload_time': 'upload_time'
        }

        self._description = description
        self._is_disabled = is_disabled
        self._is_mandatory = is_mandatory
        self._rollout = rollout
        self._target_binary_range = target_binary_range
        self._blob_url = blob_url
        self._diff_package_map = diff_package_map
        self._label = label
        self._original_deployment = original_deployment
        self._original_label = original_label
        self._package_hash = package_hash
        self._release_method = release_method
        self._released_by = released_by
        self._size = size
        self._upload_time = upload_time

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CodePushDeploymentsList200ResponseInnerLatestRelease':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The codePushDeployments_list_200_response_inner_latest_release of this CodePushDeploymentsList200ResponseInnerLatestRelease.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def description(self):
        """Gets the description of this CodePushDeploymentsList200ResponseInnerLatestRelease.


        :return: The description of this CodePushDeploymentsList200ResponseInnerLatestRelease.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CodePushDeploymentsList200ResponseInnerLatestRelease.


        :param description: The description of this CodePushDeploymentsList200ResponseInnerLatestRelease.
        :type description: str
        """

        self._description = description

    @property
    def is_disabled(self):
        """Gets the is_disabled of this CodePushDeploymentsList200ResponseInnerLatestRelease.


        :return: The is_disabled of this CodePushDeploymentsList200ResponseInnerLatestRelease.
        :rtype: bool
        """
        return self._is_disabled

    @is_disabled.setter
    def is_disabled(self, is_disabled):
        """Sets the is_disabled of this CodePushDeploymentsList200ResponseInnerLatestRelease.


        :param is_disabled: The is_disabled of this CodePushDeploymentsList200ResponseInnerLatestRelease.
        :type is_disabled: bool
        """

        self._is_disabled = is_disabled

    @property
    def is_mandatory(self):
        """Gets the is_mandatory of this CodePushDeploymentsList200ResponseInnerLatestRelease.


        :return: The is_mandatory of this CodePushDeploymentsList200ResponseInnerLatestRelease.
        :rtype: bool
        """
        return self._is_mandatory

    @is_mandatory.setter
    def is_mandatory(self, is_mandatory):
        """Sets the is_mandatory of this CodePushDeploymentsList200ResponseInnerLatestRelease.


        :param is_mandatory: The is_mandatory of this CodePushDeploymentsList200ResponseInnerLatestRelease.
        :type is_mandatory: bool
        """

        self._is_mandatory = is_mandatory

    @property
    def rollout(self):
        """Gets the rollout of this CodePushDeploymentsList200ResponseInnerLatestRelease.


        :return: The rollout of this CodePushDeploymentsList200ResponseInnerLatestRelease.
        :rtype: int
        """
        return self._rollout

    @rollout.setter
    def rollout(self, rollout):
        """Sets the rollout of this CodePushDeploymentsList200ResponseInnerLatestRelease.


        :param rollout: The rollout of this CodePushDeploymentsList200ResponseInnerLatestRelease.
        :type rollout: int
        """
        if rollout is not None and rollout > 100:
            raise ValueError("Invalid value for `rollout`, must be a value less than or equal to `100`")
        if rollout is not None and rollout < 1:
            raise ValueError("Invalid value for `rollout`, must be a value greater than or equal to `1`")

        self._rollout = rollout

    @property
    def target_binary_range(self):
        """Gets the target_binary_range of this CodePushDeploymentsList200ResponseInnerLatestRelease.


        :return: The target_binary_range of this CodePushDeploymentsList200ResponseInnerLatestRelease.
        :rtype: str
        """
        return self._target_binary_range

    @target_binary_range.setter
    def target_binary_range(self, target_binary_range):
        """Sets the target_binary_range of this CodePushDeploymentsList200ResponseInnerLatestRelease.


        :param target_binary_range: The target_binary_range of this CodePushDeploymentsList200ResponseInnerLatestRelease.
        :type target_binary_range: str
        """

        self._target_binary_range = target_binary_range

    @property
    def blob_url(self):
        """Gets the blob_url of this CodePushDeploymentsList200ResponseInnerLatestRelease.


        :return: The blob_url of this CodePushDeploymentsList200ResponseInnerLatestRelease.
        :rtype: str
        """
        return self._blob_url

    @blob_url.setter
    def blob_url(self, blob_url):
        """Sets the blob_url of this CodePushDeploymentsList200ResponseInnerLatestRelease.


        :param blob_url: The blob_url of this CodePushDeploymentsList200ResponseInnerLatestRelease.
        :type blob_url: str
        """

        self._blob_url = blob_url

    @property
    def diff_package_map(self):
        """Gets the diff_package_map of this CodePushDeploymentsList200ResponseInnerLatestRelease.


        :return: The diff_package_map of this CodePushDeploymentsList200ResponseInnerLatestRelease.
        :rtype: Dict[str, CodePushDeploymentsList200ResponseInnerLatestReleaseAllOfDiffPackageMapValue]
        """
        return self._diff_package_map

    @diff_package_map.setter
    def diff_package_map(self, diff_package_map):
        """Sets the diff_package_map of this CodePushDeploymentsList200ResponseInnerLatestRelease.


        :param diff_package_map: The diff_package_map of this CodePushDeploymentsList200ResponseInnerLatestRelease.
        :type diff_package_map: Dict[str, CodePushDeploymentsList200ResponseInnerLatestReleaseAllOfDiffPackageMapValue]
        """

        self._diff_package_map = diff_package_map

    @property
    def label(self):
        """Gets the label of this CodePushDeploymentsList200ResponseInnerLatestRelease.


        :return: The label of this CodePushDeploymentsList200ResponseInnerLatestRelease.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this CodePushDeploymentsList200ResponseInnerLatestRelease.


        :param label: The label of this CodePushDeploymentsList200ResponseInnerLatestRelease.
        :type label: str
        """

        self._label = label

    @property
    def original_deployment(self):
        """Gets the original_deployment of this CodePushDeploymentsList200ResponseInnerLatestRelease.

        Set on 'Promote'

        :return: The original_deployment of this CodePushDeploymentsList200ResponseInnerLatestRelease.
        :rtype: str
        """
        return self._original_deployment

    @original_deployment.setter
    def original_deployment(self, original_deployment):
        """Sets the original_deployment of this CodePushDeploymentsList200ResponseInnerLatestRelease.

        Set on 'Promote'

        :param original_deployment: The original_deployment of this CodePushDeploymentsList200ResponseInnerLatestRelease.
        :type original_deployment: str
        """

        self._original_deployment = original_deployment

    @property
    def original_label(self):
        """Gets the original_label of this CodePushDeploymentsList200ResponseInnerLatestRelease.

        Set on 'Promote' and 'Rollback'

        :return: The original_label of this CodePushDeploymentsList200ResponseInnerLatestRelease.
        :rtype: str
        """
        return self._original_label

    @original_label.setter
    def original_label(self, original_label):
        """Sets the original_label of this CodePushDeploymentsList200ResponseInnerLatestRelease.

        Set on 'Promote' and 'Rollback'

        :param original_label: The original_label of this CodePushDeploymentsList200ResponseInnerLatestRelease.
        :type original_label: str
        """

        self._original_label = original_label

    @property
    def package_hash(self):
        """Gets the package_hash of this CodePushDeploymentsList200ResponseInnerLatestRelease.


        :return: The package_hash of this CodePushDeploymentsList200ResponseInnerLatestRelease.
        :rtype: str
        """
        return self._package_hash

    @package_hash.setter
    def package_hash(self, package_hash):
        """Sets the package_hash of this CodePushDeploymentsList200ResponseInnerLatestRelease.


        :param package_hash: The package_hash of this CodePushDeploymentsList200ResponseInnerLatestRelease.
        :type package_hash: str
        """

        self._package_hash = package_hash

    @property
    def release_method(self):
        """Gets the release_method of this CodePushDeploymentsList200ResponseInnerLatestRelease.

        The release method is unknown if unspecified

        :return: The release_method of this CodePushDeploymentsList200ResponseInnerLatestRelease.
        :rtype: str
        """
        return self._release_method

    @release_method.setter
    def release_method(self, release_method):
        """Sets the release_method of this CodePushDeploymentsList200ResponseInnerLatestRelease.

        The release method is unknown if unspecified

        :param release_method: The release_method of this CodePushDeploymentsList200ResponseInnerLatestRelease.
        :type release_method: str
        """
        allowed_values = ["Upload", "Promote", "Rollback"]  # noqa: E501
        if release_method not in allowed_values:
            raise ValueError(
                "Invalid value for `release_method` ({0}), must be one of {1}"
                .format(release_method, allowed_values)
            )

        self._release_method = release_method

    @property
    def released_by(self):
        """Gets the released_by of this CodePushDeploymentsList200ResponseInnerLatestRelease.


        :return: The released_by of this CodePushDeploymentsList200ResponseInnerLatestRelease.
        :rtype: str
        """
        return self._released_by

    @released_by.setter
    def released_by(self, released_by):
        """Sets the released_by of this CodePushDeploymentsList200ResponseInnerLatestRelease.


        :param released_by: The released_by of this CodePushDeploymentsList200ResponseInnerLatestRelease.
        :type released_by: str
        """

        self._released_by = released_by

    @property
    def size(self):
        """Gets the size of this CodePushDeploymentsList200ResponseInnerLatestRelease.


        :return: The size of this CodePushDeploymentsList200ResponseInnerLatestRelease.
        :rtype: float
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this CodePushDeploymentsList200ResponseInnerLatestRelease.


        :param size: The size of this CodePushDeploymentsList200ResponseInnerLatestRelease.
        :type size: float
        """

        self._size = size

    @property
    def upload_time(self):
        """Gets the upload_time of this CodePushDeploymentsList200ResponseInnerLatestRelease.


        :return: The upload_time of this CodePushDeploymentsList200ResponseInnerLatestRelease.
        :rtype: int
        """
        return self._upload_time

    @upload_time.setter
    def upload_time(self, upload_time):
        """Sets the upload_time of this CodePushDeploymentsList200ResponseInnerLatestRelease.


        :param upload_time: The upload_time of this CodePushDeploymentsList200ResponseInnerLatestRelease.
        :type upload_time: int
        """

        self._upload_time = upload_time
