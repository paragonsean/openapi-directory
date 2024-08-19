from typing import List, Dict
from aiohttp import web

from openapi_server.models.analysis import Analysis
from openapi_server.models.operation import Operation
from openapi_server import util


async def get_alerts(request: web.Request, analysis_id, sarif_version=None, excluded_files=None) -> web.Response:
    """Get detailed alert information

    Download all the alerts found by an analysis. Use the &#x60;Accept:&#x60; request header to specify the output media type as either CSV or [SARIF](https://lgtm.com/help/lgtm/sarif-results-file):   - &#x60;application/sarif+json&#x60;: Alerts in SARIF format. If no version is specified the latest supported SARIF version is used. - &#x60;application/json&#x60;: Alerts in SARIF format (*deprecated*).    If no version is specified, [SARIF 2.0.0](http://docs.oasis-open.org/sarif/sarif/v2.0/sarif-v2.0.html)    is used for backwards compatibility.  - &#x60;text/csv&#x60;: Alerts in CSV format. The &#x60;text/csv&#x60; media type has two optional parameters:    - &#x60;charset&#x60;: determines the character encoding of the text, by default UTF-8.    - &#x60;header&#x60;: determines whether a header row with column names is &#x60;present&#x60; or &#x60;absent&#x60;.       The default value for this parameter is &#x60;present&#x60;.       For example, an Accept header with value &#x60;text/csv; header&#x3D;absent&#x60;        would result in CSV output without a header row.         To find the analysis identifier for a commit, use the &#x60;/analyses/{project-id}/commits/{commit-id}&#x60;  endpoint. For more information, see [Get analysis summary for a specific commit](https://lgtm.com/help/lgtm/api/api-v1#opIdgetAnalysisForCommit).  

    :param analysis_id: The analysis identifier.
    :type analysis_id: str
    :param sarif_version: The desired version of the SARIF format. Currently supported versions are &#x60;1.0.0&#x60;, &#x60;2.0.0&#x60;, and &#x60;2.1.0&#x60;.
    :type sarif_version: str
    :param excluded_files: Set &#x60;true&#x60; to include results in files that are excluded from the output by default. This includes results in test code and generated files. For more information, see [File classification](https://lgtm.com/help/lgtm/file-classification).
    :type excluded_files: bool

    """
    return web.Response(status=200)


async def get_analysis(request: web.Request, analysis_id) -> web.Response:
    """Get analysis summary

    Get a summary of the analysis results for a specific analysis identifier.  To find the analysis identifier for a commit, use the &#x60;/analyses/{project-id}/commits/{commit-id}&#x60; endpoint. For more information, see [Get analysis summary for a specific commit](https://lgtm.com/help/lgtm/api/api-v1#opIdgetAnalysisForCommit).  This endpoint reports the commit analyzed and a summary of the results for each language. Alternatively, you can use this identifier to download full details  of all the alerts found by the analysis. For more information, see [Get detailed alert information](https://lgtm.com/help/lgtm/api/api-v1#opIdgetAlerts). 

    :param analysis_id: The analysis identifier.
    :type analysis_id: str

    """
    return web.Response(status=200)


async def get_analysis_for_commit(request: web.Request, project_id, commit_id) -> web.Response:
    """Get analysis summary for a specific commit

    Get a summary of the analysis results for a specific commit, or the latest commit, to a project. (For projects configured for sparse or upload analysis, only &#x60;latest&#x60; is supported.)   This endpoint reports a summary of results for each language, and also the analysis identifier. You can use the analysis identifier to download full details of all the alerts  found by the analysis. For more information, see [Get detailed alert information](https://lgtm.com/help/lgtm/api/api-v1#opIdgetAlerts). 

    :param project_id: The numeric project identifier.
    :type project_id: int
    :param commit_id: The identifier of a specific commit. Alternatively, use &#x60;latest&#x60; for the most recent analyzed commit.
    :type commit_id: str

    """
    return web.Response(status=200)


async def request_analysis(request: web.Request, project_id, commit, language=None) -> web.Response:
    """Run analysis of a specific commit

    Trigger the analysis of a specific commit to a project. If a previous attempt to analyze that commit failed, this triggers a fresh analysis.  This is supported for all LGTM projects, regardless of repository type or host. The commit must be available in the main repository, but can be on a branch that isn&#39;t tracked by LGTM. For both LGTM.com and LGTM Enterprise, you must include an access token with the &#x60;analyses:write&#x60; scope.  When you request the analysis of a commit, the API returns: - &#x60;operation-id&#x60;: used to track the status of the task using the &#x60;/operations&#x60; endpoint. For more information, see [Get operation status](https://lgtm.com/help/lgtm/api/api-v1#opIdgetOperation). - &#x60;status&#x60;: initially pending. - &#x60;task-result&#x60;: containing information about the progress and results of the analysis. 

    :param project_id: The numeric project identifier.
    :type project_id: int
    :param commit: The identifier of the commit to analyze.
    :type commit: str
    :param language: The language codes of the languages to analyze. For a list of available languages, see [Supported languages](https://lgtm.com/help/lgtm/analysis-faqs#which-languages-are-supported). To specify more than one language, this parameter can be repeated. If no language is specified, all the project&#39;s languages will be analyzed. 
    :type language: List[str]

    """
    return web.Response(status=200)
