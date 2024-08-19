from typing import List, Dict
from aiohttp import web

from openapi_server.models.operation import Operation
from openapi_server.models.upload_session import UploadSession
from openapi_server import util


async def abort_upload(request: web.Request, session_id) -> web.Response:
    """Abort database upload process

    Aborts the specified upload session and deletes any uploaded parts. After the session is aborted it cannot be restarted. If any part uploads are in progress when the session is aborted, their data may not be deleted. To ensure that uploaded parts are deleted correctly, you should only abort an upload session after all part uploads have completed. 

    :param session_id: The id of the upload session.
    :type session_id: str

    """
    return web.Response(status=200)


async def complete_upload(request: web.Request, session_id) -> web.Response:
    """Complete snapshot upload session

    Completes the database upload by closing the upload session, upgrading the database if appropriate, and scheduling analysis of that snapshot of the codebase.  You can view the analysis progress and access the results using the &#x60;task-result-url&#x60;. 

    :param session_id: The id of the upload session.
    :type session_id: str

    """
    return web.Response(status=200)


async def get_snapshot(request: web.Request, project_id, language) -> web.Response:
    """Download a snapshot

    Download a CodeQL database from LGTM, representing a snapshot of the codebase, to run queries in your IDE.  This endpoint works for projects that have been successfully analyzed for the language specified in the request.  A successful request redirects you to a URL for downloading a database that represents the code snapshot, as specified in the &#x60;Location:&#x60; header in the response. Therefore, your HTTP client should be configured to follow redirects. For example, if you are using &#x60;curl&#x60;, you can add the&#x60;-L&#x60; flag to the command.  The database is downloaded as a zip file that can be imported into an IDE equipped with a  CodeQL extension. The extension must be up to date to analyze databases downloaded from LGTM. For more information on running queries locally in your IDE, see [Runnning queries in your IDE](https://lgtm.com/help/lgtm/running-queries-ide).  

    :param project_id: The numeric project identifier.
    :type project_id: int
    :param language: The language of the database to download.
    :type language: str

    """
    return web.Response(status=200)


async def init_snapshot_upload(request: web.Request, project_id, language, commit, _date=None) -> web.Response:
    """Start snapshot upload session

    Start a session to upload an externally-built database (which represents a snapshot of a codebase) to a project on LGTM.   This endpoint works for projects that are already on LGTM, and the selected language of  the database must already be configured. The project must be configured with &#39;upload&#39; analysis mode. You can upload a \&quot;bundled\&quot; CodeQL database or a database exported by  the QL command-line tools (&#x60;odasa&#x60;).  If your database was generated using a version of the  command line that is older than LGTM,  LGTM will try to upgrade and analyze it when the upload is complete. You can include cached predicates in the upload, but they are ignored as the cache is  repopulated after the database has been upgraded and analyzed. However, if you want to include results with your database, make sure the database is  compatible before you start the upload session.  Incompatible databases with results won&#39;t be upgraded and therefore cannot be uploaded.  For further information on externally-built databases,  see [Preparing snapshots to upload to LGTM using the QL command-line tools](https://help.semmle.com/wiki/display/SD/Preparing+snapshots+to+upload+to+LGTM).       When the upload session has been successfully started, upload the database to the  upload URL returned in the response. The database can be uploaded to the upload URL in parts using  the [&#x60;PUT /snapshots/uploads/{session-id}&#x60;](https://lgtm.com/help/lgtm/api/api-v1#opIduploadPart) endpoint. After uploading all the parts you must call  the [&#x60;POST /snapshots/uploads/{session-id}&#x60;](https://lgtm.com/help/lgtm/api/api-v1#opIdcompleteUpload) endpoint to complete the upload session. 

    :param project_id: The numeric project identifier.
    :type project_id: int
    :param language: The language of the database to upload.
    :type language: str
    :param commit: The identifier of the analyzed commit.
    :type commit: str
    :param _date: The date and time of the analyzed commit (default the current time).
    :type _date: str

    """
    _date = util.deserialize_datetime(_date)
    return web.Response(status=200)


async def upload_part(request: web.Request, session_id, body) -> web.Response:
    """Upload snapshot

    Upload a database representing a snapshot of a codebase.  The database is sent in one or more parts. Each part is sent in the request body.  Use the [&#x60;POST /snapshots/{project-id}/{language}&#x60;](https://lgtm.com/help/lgtm/api/api-v1#opIdinitSnapshotUpload) endpoint  to start an upload session before uploading a database part. Database parts must have been generated and prepared for upload using the CodeQL CLI or the QL command-line tools. For further information on exporting externally-built databases,  see [Preparing snapshots to upload to LGTM](https://help.semmle.com/wiki/display/SD/Preparing+snapshots+to+upload+to+LGTM).  Split large databases into multiple parts. Upload the parts by making a separate request for each part.  Don&#39;t upload the next part until you&#39;ve successfully uploaded the previous part.  If the upload fails you should retry it with the same data. 

    :param session_id: The id of the upload session.
    :type session_id: str
    :param body: The database or database part to upload.
    :type body: str

    """
    return web.Response(status=200)
