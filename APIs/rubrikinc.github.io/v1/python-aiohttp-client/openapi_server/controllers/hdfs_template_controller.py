from typing import List, Dict
from aiohttp import web

from openapi_server.models.hdfs_template_create import HdfsTemplateCreate
from openapi_server.models.hdfs_template_detail import HdfsTemplateDetail
from openapi_server.models.hdfs_template_detail_list_response import HdfsTemplateDetailListResponse
from openapi_server.models.hdfs_template_patch import HdfsTemplatePatch
from openapi_server import util


async def create_hdfs_template(request: web.Request, body) -> web.Response:
    """Create a HDFS directory template

    Create a HDFS directory template. The template is applied to the host.  Each template is a set of paths on the host. A template uses full paths and wildcards to define the objects to include, exclude, and exempt from exclusion. The **_exceptions_** value specifies paths that should not be excluded from the HDFS directory by the **_exclude_** value. Specify an array of full path descriptions for each property **_include_**, **_exclude_**, and **_exceptions_**. Acceptable wildcard characters are. + **_\\*_** Single asterisk matches zero or more characters up to a path deliminator. + **_\\*\\*_** Double asterisk matches zero or more characters. The following rules apply to path descriptions. + Accepts UTF-8 characters. + Case sensitive. + Forward slash character **_/_** is the path deliminator. + Symbolic links must point to a subset of a non symbolic link path. + Paths that do not start with **_/_** are modified to start with **_\\*\\*/_**. + Paths that do not end with **_\\*_** are modified to end with **_/\\*\\*_**.

    :param body: Provide an object with the HDFS directory template definition.
    :type body: dict | bytes

    """
    body = HdfsTemplateCreate.from_dict(body)
    return web.Response(status=200)


async def delete_hdfs_template(request: web.Request, id, preserve_snapshots=None) -> web.Response:
    """Delete a HDFS directory template

    Deletes the specfied HDFS directory template. All associated HDFS directories are deleted.

    :param id: ID of the HDFS directory template to remove.
    :type id: str
    :param preserve_snapshots: A flag that indicates whether the snapshots of the HDFS directories of this template are converted to relics or deleted. By default, snapshots are converted. Set this flag to &#39;false&#39; to delete the snapshots.
    :type preserve_snapshots: bool

    """
    return web.Response(status=200)


async def get_hdfs_template(request: web.Request, id) -> web.Response:
    """Get information for a HDFS directory template

    Retrieve summary information for a specified HDFS directory template.

    :param id: The ID of the HDFS directory template.
    :type id: str

    """
    return web.Response(status=200)


async def query_hdfs_template(request: web.Request, primary_cluster_id=None, name=None, sort_by=None, sort_order=None) -> web.Response:
    """Get summary information for all HDFS directory templates

    Retrieve summary information for all HDFS directory templates, including: ID and name of the HDFS directory template, HDFS directory template creation timestamp, array of the included filepaths, array of the excluded filepaths.

    :param primary_cluster_id: Filter the summary information based on the primary_cluster_id of the primary Rubrik cluster. Use **_local_** as the primary_cluster_id of the Rubrik cluster that is hosting the current REST API session.
    :type primary_cluster_id: str
    :param name: Retrieve HDFS directory templates with a name matching the provided name. The search is performed as a case-insensitive infix search.
    :type name: str
    :param sort_by: Specifies a comma-separated list of HDFS directory attributes to use in sorting the HDFS directory summary information. Performs an ASCII sort of the summary information using each specified attribute, in the order specified. Valid attributes are: **_name_**, **_includes_**, **_excludes_**, **_exceptions_**, **_hostCount_**. Default sort_order is ascending.
    :type sort_by: str
    :param sort_order: Sort order, either ascending or descending.
    :type sort_order: str

    """
    return web.Response(status=200)


async def update_hdfs_template(request: web.Request, id, body) -> web.Response:
    """Modify a HDFS directory template

    Modify the values of specified HDFS directory template.

    :param id: ID of the HDFS directory template to update.
    :type id: str
    :param body: Provide an object with the HDFS directory template definition.
    :type body: dict | bytes

    """
    body = HdfsTemplatePatch.from_dict(body)
    return web.Response(status=200)
