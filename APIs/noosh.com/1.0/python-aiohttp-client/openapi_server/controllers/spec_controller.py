from typing import List, Dict
from aiohttp import web

from openapi_server.models.http_status_vo import HTTPStatusVO
from openapi_server.models.property_param_list_vo import PropertyParamListVO
from openapi_server.models.spec_http_status_vo import SpecHTTPStatusVO
from openapi_server.models.spec_list_vo import SpecListVO
from openapi_server.models.spec_persist_vo import SpecPersistVO
from openapi_server.models.spec_type_fields_list_vo import SpecTypeFieldsListVO
from openapi_server.models.spec_update_persist_vo import SpecUpdatePersistVO
from openapi_server.models.spec_vo import SpecVO
from openapi_server.models.v1_x1_spec_updating_po import V1X1SpecUpdatingPO
from openapi_server.models.v1x1_spec_expand_vo import V1x1SpecExpandVO
from openapi_server.models.wg_spec_prd_type_reg_persist_vo import WgSpecPrdTypeRegPersistVO
from openapi_server.models.workgroup_attribute_list_vo import WorkgroupAttributeListVO
from openapi_server import util


async def get_product_type_list_of_workgroup(request: web.Request, workgroup_id) -> web.Response:
    """Get product type of workgroup level

    Get product type of workgroup level

    :param workgroup_id: 
    :type workgroup_id: str

    """
    return web.Response(status=200)


async def get_spec(request: web.Request, workgroup_id, project_id, spec_id) -> web.Response:
    """List a specific spec of project Level

    List a specific spec of project Level

    :param workgroup_id: 
    :type workgroup_id: str
    :param project_id: 
    :type project_id: str
    :param spec_id: 
    :type spec_id: str

    """
    return web.Response(status=200)


async def get_spec_list(request: web.Request, workgroup_id, project_id) -> web.Response:
    """List specs of project Level

    List specs of project Level

    :param workgroup_id: 
    :type workgroup_id: str
    :param project_id: 
    :type project_id: str

    """
    return web.Response(status=200)


async def get_spec_product_type_list_of_workgroup(request: web.Request, workgroup_id) -> web.Response:
    """Get product type of spec level by workgroupId

    Get product type of spec level by workgroupId

    :param workgroup_id: 
    :type workgroup_id: str

    """
    return web.Response(status=200)


async def get_spec_type_fields(request: web.Request, workgroup_id, spec_type_id) -> web.Response:
    """Get Spec Type Fields

    Get Spec Type Fields

    :param workgroup_id: 
    :type workgroup_id: str
    :param spec_type_id: 
    :type spec_type_id: str

    """
    return web.Response(status=200)


async def post_spec(request: web.Request, workgroup_id, project_id, body=None) -> web.Response:
    """Create a Spec

    Create a Spec

    :param workgroup_id: 
    :type workgroup_id: str
    :param project_id: 
    :type project_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = SpecPersistVO.from_dict(body)
    return web.Response(status=200)


async def post_spec_product_type_list_of_workgroup(request: web.Request, workgroup_id, body=None) -> web.Response:
    """Register product types for spec types

    Register product types for spec types

    :param workgroup_id: 
    :type workgroup_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = WgSpecPrdTypeRegPersistVO.from_dict(body)
    return web.Response(status=200)


async def put_spec(request: web.Request, workgroup_id, project_id, spec_id, body=None) -> web.Response:
    """Update a specific Spec

    Update a specific Spec

    :param workgroup_id: 
    :type workgroup_id: str
    :param project_id: 
    :type project_id: str
    :param spec_id: 
    :type spec_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = V1X1SpecUpdatingPO.from_dict(body)
    return web.Response(status=200)


async def v1_workgroups_workgroup_id_projects_project_id_specs_spec_id_get(request: web.Request, workgroup_id, project_id, spec_id) -> web.Response:
    """List a specific spec of project Level

    List a specific spec of project Level

    :param workgroup_id: 
    :type workgroup_id: str
    :param project_id: 
    :type project_id: str
    :param spec_id: 
    :type spec_id: str

    """
    return web.Response(status=200)


async def v1_workgroups_workgroup_id_projects_project_id_specs_spec_id_put(request: web.Request, workgroup_id, project_id, spec_id, body=None) -> web.Response:
    """Update a specific Spec

    Update a specific Spec

    :param workgroup_id: 
    :type workgroup_id: str
    :param project_id: 
    :type project_id: str
    :param spec_id: 
    :type spec_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = SpecUpdatePersistVO.from_dict(body)
    return web.Response(status=200)


async def v1_workgroups_workgroup_id_spec_types_spec_type_id_spec_type_fields_get(request: web.Request, workgroup_id, spec_type_id) -> web.Response:
    """Get Spec Type Fields

    Get Spec Type Fields

    :param workgroup_id: 
    :type workgroup_id: str
    :param spec_type_id: 
    :type spec_type_id: str

    """
    return web.Response(status=200)
