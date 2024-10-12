from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def standard_data(request: web.Request, format=None, _date=None, cohort=None, data_type=None, tool=None, platform=None, center=None, level=None, protocol=None, page=None, page_size=None, sort_by=None) -> web.Response:
    """Retrieve standard data archives.

    This service returns the archive URLs for our Firehose standard data runs, providing a RESTful interface similar in spirit to the command line &lt;a href&#x3D;\&quot;https://confluence.broadinstitute.org/display/GDAC/Download\&quot;&gt;firehose_get&lt;/a&gt; tool. The archives can be filtered based on date, cohort, data type, platform, center, data level, and protocol.

    :param format: Format of result.
    :type format: str
    :param _date: Select one or more date stamps.
    :type _date: List[str]
    :param cohort: Narrow search to one or more TCGA disease cohorts from the scrollable list.
    :type cohort: List[str]
    :param data_type: Narrow search to one or more TCGA data types from the scrollable list.
    :type data_type: List[str]
    :param tool: Narrow search to include only data/results produced by the selected Firehose tool.
    :type tool: List[str]
    :param platform: Narrow search to one or more TCGA data generation platforms from the scrollable list.
    :type platform: List[str]
    :param center: Narrow search to one or more TCGA centers from the scrollable list.
    :type center: List[str]
    :param level: Narrow search to one or more TCGA data levels.
    :type level: List[int]
    :param protocol: Narrow search to one or more sample characterization protocols from the scrollable list.
    :type protocol: List[str]
    :param page: Which page (slice) of entire results set should be returned. 
    :type page: List[int]
    :param page_size: Number of records per page of results.  Max is 2000.
    :type page_size: List[int]
    :param sort_by: Which column in the results should be used for sorting paginated results?
    :type sort_by: str

    """
    _date = [util.deserialize_date(s) for s in _date]
    return web.Response(status=200)
