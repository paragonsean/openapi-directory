from typing import List, Dict
from aiohttp import web

from openapi_server.models.container_for_project_features import ContainerForProjectFeatures
from openapi_server.models.project_feature_state import ProjectFeatureState
from openapi_server import util


async def get_features_for_project(request: web.Request, project_id_or_key) -> web.Response:
    """Get project features

    Returns the list of features for a project.

    :param project_id_or_key: The ID or (case-sensitive) key of the project.
    :type project_id_or_key: str

    """
    return web.Response(status=200)


async def toggle_feature_for_project(request: web.Request, project_id_or_key, feature_key, body) -> web.Response:
    """Set project feature state

    Sets the state of a project feature.

    :param project_id_or_key: The ID or (case-sensitive) key of the project.
    :type project_id_or_key: str
    :param feature_key: The key of the feature.
    :type feature_key: str
    :param body: Details of the feature state change.
    :type body: dict | bytes

    """
    body = ProjectFeatureState.from_dict(body)
    return web.Response(status=200)
