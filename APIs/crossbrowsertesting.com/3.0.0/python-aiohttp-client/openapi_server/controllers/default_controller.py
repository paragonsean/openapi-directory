from typing import List, Dict
from aiohttp import web

from openapi_server.models.full_comparison_test import FullComparisonTest
from openapi_server.models.single_comparison_test import SingleComparisonTest
from openapi_server import util


async def screenshots_target_screenshot_test_id_target_version_id_comparison_base_result_id_get(request: web.Request, target_screenshot_test_id, target_version_id, base_result_id, format=None, param_callback=None, tolerance=None) -> web.Response:
    """Compare Full Screenshot Test

    Get comparison results for all browsers in target screenshot test against a base screenshot result. The base result can be from the same test or from another test run at an earlier time. This is a one-to-many comparison.

    :param target_screenshot_test_id: test id of the target Screenshot Test
    :type target_screenshot_test_id: int
    :param target_version_id: version id of the target Screenshot Test
    :type target_version_id: int
    :param base_result_id: result id of the base Screenshot Test
    :type base_result_id: int
    :param format: The format of the returned data. Possible values are \&quot;json\&quot; or \&quot;jsonp\&quot;.
    :type format: str
    :param param_callback: Name of callback method for JSONP requests.
    :type param_callback: str
    :param tolerance: Used as the basis for detecting box model differences in element positioning and dimensions that should be flagged and reported back to the comparison results. The default is 30px which is a good basis for finding notable layout differences.
    :type tolerance: 

    """
    return web.Response(status=200)


async def screenshots_target_screenshot_test_id_target_version_id_comparison_parallel_base_version_id_get(request: web.Request, target_screenshot_test_id, target_version_id, base_version_id, format=None, param_callback=None, tolerance=None) -> web.Response:
    """Compare Screenshot Test Versions

    Get comparison results for all browsers in target screenshot test against the same browser in the base screenshot test. This is a good method for regression testing. For example, you&#39;ve run a screenshot test against a set of browsers that is \&quot;good\&quot;. Then, after some changes, you run a new screenshot test against the same set of browsers. This method will compare each of the same browsers against each other. For example, IE9 will be compared to IE9 from an earlier test. This is a many-to-many comparison where the OS/Browser/Resolution must match between the two test versions in order for the comparison to return results. The two versions can be from the same screenshot_test_id or not.

    :param target_screenshot_test_id: test id of the target Screenshot Test
    :type target_screenshot_test_id: int
    :param target_version_id: version id of the target Screenshot Test
    :type target_version_id: int
    :param base_version_id: version id of the base Screenshot Test
    :type base_version_id: int
    :param format: The format of the returned data. Possible values are \&quot;json\&quot; or \&quot;jsonp\&quot;.
    :type format: str
    :param param_callback: Name of callback method for JSONP requests.
    :type param_callback: str
    :param tolerance: Used as the basis for detecting box model differences in element positioning and dimensions that should be flagged and reported back to the comparison results. The default is 30px which is a good basis for finding notable layout differences.
    :type tolerance: 

    """
    return web.Response(status=200)


async def screenshots_target_screenshot_test_id_target_version_id_target_result_id_comparison_base_result_id_get(request: web.Request, target_screenshot_test_id, target_version_id, target_result_id, base_result_id, format=None, param_callback=None, tolerance=None) -> web.Response:
    """Compare Single Screenshot

    Get comparison results for a single target screenshot result against a base screenshot result. This is a one-to-one comparison.

    :param target_screenshot_test_id: test id of the target Screenshot Test
    :type target_screenshot_test_id: int
    :param target_version_id: version id of the target Screenshot Test
    :type target_version_id: int
    :param target_result_id: result id of the target Screenshot Test
    :type target_result_id: int
    :param base_result_id: result id of the base Screenshot Test
    :type base_result_id: int
    :param format: The format of the returned data. Possible values are \&quot;json\&quot; or \&quot;jsonp\&quot;.
    :type format: str
    :param param_callback: Name of callback method for JSONP requests.
    :type param_callback: str
    :param tolerance: Used as the basis for detecting box model differences in element positioning and dimensions that should be flagged and reported back to the comparison results. The default is 30px which is a good basis for finding notable layout differences.
    :type tolerance: 

    """
    return web.Response(status=200)
