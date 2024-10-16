# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.header_dto import HeaderDTO
from openapi_server.models.secret_ref import SecretRef
from openapi_server.models.test_case_result import TestCaseResult
from openapi_server.models.test_runner_type import TestRunnerType
from openapi_server import util


class TestResult(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, elapsed_time: float=None, id: str=None, in_progress: bool=None, operation_headers: Dict[str, List[HeaderDTO]]=None, runner_type: TestRunnerType=None, secret_ref: SecretRef=None, service_id: str=None, success: bool=None, test_case_results: List[TestCaseResult]=None, test_date: int=None, test_number: float=None, tested_endpoint: str=None, timeout: int=None, version: float=None):
        """TestResult - a model defined in OpenAPI

        :param elapsed_time: The elapsed_time of this TestResult.
        :param id: The id of this TestResult.
        :param in_progress: The in_progress of this TestResult.
        :param operation_headers: The operation_headers of this TestResult.
        :param runner_type: The runner_type of this TestResult.
        :param secret_ref: The secret_ref of this TestResult.
        :param service_id: The service_id of this TestResult.
        :param success: The success of this TestResult.
        :param test_case_results: The test_case_results of this TestResult.
        :param test_date: The test_date of this TestResult.
        :param test_number: The test_number of this TestResult.
        :param tested_endpoint: The tested_endpoint of this TestResult.
        :param timeout: The timeout of this TestResult.
        :param version: The version of this TestResult.
        """
        self.openapi_types = {
            'elapsed_time': float,
            'id': str,
            'in_progress': bool,
            'operation_headers': Dict[str, List[HeaderDTO]],
            'runner_type': TestRunnerType,
            'secret_ref': SecretRef,
            'service_id': str,
            'success': bool,
            'test_case_results': List[TestCaseResult],
            'test_date': int,
            'test_number': float,
            'tested_endpoint': str,
            'timeout': int,
            'version': float
        }

        self.attribute_map = {
            'elapsed_time': 'elapsedTime',
            'id': 'id',
            'in_progress': 'inProgress',
            'operation_headers': 'operationHeaders',
            'runner_type': 'runnerType',
            'secret_ref': 'secretRef',
            'service_id': 'serviceId',
            'success': 'success',
            'test_case_results': 'testCaseResults',
            'test_date': 'testDate',
            'test_number': 'testNumber',
            'tested_endpoint': 'testedEndpoint',
            'timeout': 'timeout',
            'version': 'version'
        }

        self._elapsed_time = elapsed_time
        self._id = id
        self._in_progress = in_progress
        self._operation_headers = operation_headers
        self._runner_type = runner_type
        self._secret_ref = secret_ref
        self._service_id = service_id
        self._success = success
        self._test_case_results = test_case_results
        self._test_date = test_date
        self._test_number = test_number
        self._tested_endpoint = tested_endpoint
        self._timeout = timeout
        self._version = version

    @classmethod
    def from_dict(cls, dikt: dict) -> 'TestResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The TestResult of this TestResult.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def elapsed_time(self):
        """Gets the elapsed_time of this TestResult.

        Elapsed time in milliseconds since test beginning

        :return: The elapsed_time of this TestResult.
        :rtype: float
        """
        return self._elapsed_time

    @elapsed_time.setter
    def elapsed_time(self, elapsed_time):
        """Sets the elapsed_time of this TestResult.

        Elapsed time in milliseconds since test beginning

        :param elapsed_time: The elapsed_time of this TestResult.
        :type elapsed_time: float
        """

        self._elapsed_time = elapsed_time

    @property
    def id(self):
        """Gets the id of this TestResult.

        Unique identifier of TestResult

        :return: The id of this TestResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TestResult.

        Unique identifier of TestResult

        :param id: The id of this TestResult.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def in_progress(self):
        """Gets the in_progress of this TestResult.

        Flag telling is test is still in progress

        :return: The in_progress of this TestResult.
        :rtype: bool
        """
        return self._in_progress

    @in_progress.setter
    def in_progress(self, in_progress):
        """Sets the in_progress of this TestResult.

        Flag telling is test is still in progress

        :param in_progress: The in_progress of this TestResult.
        :type in_progress: bool
        """
        if in_progress is None:
            raise ValueError("Invalid value for `in_progress`, must not be `None`")

        self._in_progress = in_progress

    @property
    def operation_headers(self):
        """Gets the operation_headers of this TestResult.

        Specification of additional headers for a Service/API operations. Keys are operation name or \"globals\" (if header applies to all), values are Header objects DTO.

        :return: The operation_headers of this TestResult.
        :rtype: Dict[str, List[HeaderDTO]]
        """
        return self._operation_headers

    @operation_headers.setter
    def operation_headers(self, operation_headers):
        """Sets the operation_headers of this TestResult.

        Specification of additional headers for a Service/API operations. Keys are operation name or \"globals\" (if header applies to all), values are Header objects DTO.

        :param operation_headers: The operation_headers of this TestResult.
        :type operation_headers: Dict[str, List[HeaderDTO]]
        """

        self._operation_headers = operation_headers

    @property
    def runner_type(self):
        """Gets the runner_type of this TestResult.


        :return: The runner_type of this TestResult.
        :rtype: TestRunnerType
        """
        return self._runner_type

    @runner_type.setter
    def runner_type(self, runner_type):
        """Sets the runner_type of this TestResult.


        :param runner_type: The runner_type of this TestResult.
        :type runner_type: TestRunnerType
        """
        if runner_type is None:
            raise ValueError("Invalid value for `runner_type`, must not be `None`")

        self._runner_type = runner_type

    @property
    def secret_ref(self):
        """Gets the secret_ref of this TestResult.


        :return: The secret_ref of this TestResult.
        :rtype: SecretRef
        """
        return self._secret_ref

    @secret_ref.setter
    def secret_ref(self, secret_ref):
        """Sets the secret_ref of this TestResult.


        :param secret_ref: The secret_ref of this TestResult.
        :type secret_ref: SecretRef
        """

        self._secret_ref = secret_ref

    @property
    def service_id(self):
        """Gets the service_id of this TestResult.

        Unique identifier of service tested

        :return: The service_id of this TestResult.
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        """Sets the service_id of this TestResult.

        Unique identifier of service tested

        :param service_id: The service_id of this TestResult.
        :type service_id: str
        """
        if service_id is None:
            raise ValueError("Invalid value for `service_id`, must not be `None`")

        self._service_id = service_id

    @property
    def success(self):
        """Gets the success of this TestResult.

        Flag telling if test is a success

        :return: The success of this TestResult.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this TestResult.

        Flag telling if test is a success

        :param success: The success of this TestResult.
        :type success: bool
        """
        if success is None:
            raise ValueError("Invalid value for `success`, must not be `None`")

        self._success = success

    @property
    def test_case_results(self):
        """Gets the test_case_results of this TestResult.

        TestCase results associated to this test

        :return: The test_case_results of this TestResult.
        :rtype: List[TestCaseResult]
        """
        return self._test_case_results

    @test_case_results.setter
    def test_case_results(self, test_case_results):
        """Sets the test_case_results of this TestResult.

        TestCase results associated to this test

        :param test_case_results: The test_case_results of this TestResult.
        :type test_case_results: List[TestCaseResult]
        """

        self._test_case_results = test_case_results

    @property
    def test_date(self):
        """Gets the test_date of this TestResult.

        Timestamp of creation date of this service

        :return: The test_date of this TestResult.
        :rtype: int
        """
        return self._test_date

    @test_date.setter
    def test_date(self, test_date):
        """Sets the test_date of this TestResult.

        Timestamp of creation date of this service

        :param test_date: The test_date of this TestResult.
        :type test_date: int
        """
        if test_date is None:
            raise ValueError("Invalid value for `test_date`, must not be `None`")

        self._test_date = test_date

    @property
    def test_number(self):
        """Gets the test_number of this TestResult.

        Incremental number for tracking number of tests of a service

        :return: The test_number of this TestResult.
        :rtype: float
        """
        return self._test_number

    @test_number.setter
    def test_number(self, test_number):
        """Sets the test_number of this TestResult.

        Incremental number for tracking number of tests of a service

        :param test_number: The test_number of this TestResult.
        :type test_number: float
        """
        if test_number is None:
            raise ValueError("Invalid value for `test_number`, must not be `None`")

        self._test_number = test_number

    @property
    def tested_endpoint(self):
        """Gets the tested_endpoint of this TestResult.

        Endpoint used during test

        :return: The tested_endpoint of this TestResult.
        :rtype: str
        """
        return self._tested_endpoint

    @tested_endpoint.setter
    def tested_endpoint(self, tested_endpoint):
        """Sets the tested_endpoint of this TestResult.

        Endpoint used during test

        :param tested_endpoint: The tested_endpoint of this TestResult.
        :type tested_endpoint: str
        """
        if tested_endpoint is None:
            raise ValueError("Invalid value for `tested_endpoint`, must not be `None`")

        self._tested_endpoint = tested_endpoint

    @property
    def timeout(self):
        """Gets the timeout of this TestResult.

        The maximum time (in milliseconds) to wait for this test ends

        :return: The timeout of this TestResult.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this TestResult.

        The maximum time (in milliseconds) to wait for this test ends

        :param timeout: The timeout of this TestResult.
        :type timeout: int
        """

        self._timeout = timeout

    @property
    def version(self):
        """Gets the version of this TestResult.

        Revision number of this test

        :return: The version of this TestResult.
        :rtype: float
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this TestResult.

        Revision number of this test

        :param version: The version of this TestResult.
        :type version: float
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")

        self._version = version
