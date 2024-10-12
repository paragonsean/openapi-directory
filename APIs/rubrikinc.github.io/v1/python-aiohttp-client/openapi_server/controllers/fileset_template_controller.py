from typing import List, Dict
from aiohttp import web

from openapi_server.models.fileset_template_create import FilesetTemplateCreate
from openapi_server.models.fileset_template_detail import FilesetTemplateDetail
from openapi_server.models.fileset_template_detail_list_response import FilesetTemplateDetailListResponse
from openapi_server.models.fileset_template_patch import FilesetTemplatePatch
from openapi_server import util


async def create_fileset_template(request: web.Request, body) -> web.Response:
    """Create a fileset template

    Create a fileset template. The template is applied to the host.  Each template is a set of paths on the host.  A template uses full paths and wildcards to define the objects to include, exclude, and exempt from exclusion.  The **_exceptions_** value specifies paths that should not be excluded from the fileset by the **_exclude_** value.  Specify an array of full path descriptions for each property **_include_**, **_exclude_**, and **_exceptions_**.  Acceptable wildcard characters are. + **_\\*_** Single asterisk matches zero or more characters up to a path deliminator. + **_\\*\\*_** Double asterisk matches zero or more characters.  The following rules apply to path descriptions. + Accepts UTF-8 characters. + Case sensitive. + Forward slash character **_/_** is the path deliminator. + Symbolic links must point to a subset of a non symbolic link path. + Paths that do not start with **_/_** are modified to start with **_\\*\\*/_**. + Paths that do not end with **_\\*_** are modified to end with **_/\\*\\*_**.

    :param body: Provide an object with the fileset template definition.
    :type body: dict | bytes

    """
    body = FilesetTemplateCreate.from_dict(body)
    return web.Response(status=200)


async def delete_fileset_template(request: web.Request, id, preserve_snapshots=None) -> web.Response:
    """Delete a fileset template

    Deletes the specfied fileset template. All associated filesets are deleted.

    :param id: ID of the fileset template to remove.
    :type id: str
    :param preserve_snapshots: Flag to indicate whether to convert snapshots of all filesets of this template to relics or to delete them.  Default is true.
    :type preserve_snapshots: bool

    """
    return web.Response(status=200)


async def get_fileset_template(request: web.Request, id) -> web.Response:
    """Get information for a fileset template

    Retrieve summary information for a specified fileset template.

    :param id: The ID of the fileset template.
    :type id: str

    """
    return web.Response(status=200)


async def query_fileset_template(request: web.Request, primary_cluster_id=None, operating_system_type=None, share_type=None, name=None, sort_by=None, sort_order=None) -> web.Response:
    """Get summary information for all fileset templates

    Retrieve summary information for all fileset templates, including: ID and name of the fileset template, fileset template creation timestamp, array of the included filepaths, array of the excluded filepaths.

    :param primary_cluster_id: Filter the summary information based on the primary_cluster_id of the primary Rubrik cluster. Use **_local_** as the primary_cluster_id of the Rubrik cluster that is hosting the current REST API session.
    :type primary_cluster_id: str
    :param operating_system_type: Filter the summary information based on the operating system type of the fileset. Accepted values: &#39;Windows&#39;, &#39;UnixLike&#39;, &#39;ANY&#39;, &#39;NONE&#39;. Use **_NONE_** to only return information for fileset templates that do not have operating system type set. Use **_ANY_** to only return information for fileset templates that have operating system type set.
    :type operating_system_type: str
    :param share_type: Filter the summary information based on the share type where the fileset is assigned to. Accepted values: &#39;NFS&#39;, &#39;SMB&#39;, &#39;ANY&#39;, &#39;NONE&#39;. Use **_NONE_** to only return information for fileset templates that do not have share type set. Use **_ANY_** to only return information for fileset templates that have share type set.
    :type share_type: str
    :param name: Retrieve fileset templates with a name matching the provided name. The search is performed as a case-insensitive infix search.
    :type name: str
    :param sort_by: Specifies a comma-separated list of fileset attributes to use in sorting the fileset summary information. Performs an ASCII sort of the summary information using each specified attribute, in the order specified.  Valid attributes are: **_name_**, **_includes_**, **_excludes_**, **_exceptions_**, **_hostCount_**, **_shareType_**. Default sort_order is ascending.
    :type sort_by: str
    :param sort_order: Sort order, either ascending or descending.
    :type sort_order: str

    """
    return web.Response(status=200)


async def update_fileset_template(request: web.Request, id, body) -> web.Response:
    """Modify a fileset template

    Modify the values of specified fileset template.

    :param id: ID of the fileset template to update.
    :type id: str
    :param body: Provide an object with the fileset template definition.
    :type body: dict | bytes

    """
    body = FilesetTemplatePatch.from_dict(body)
    return web.Response(status=200)
