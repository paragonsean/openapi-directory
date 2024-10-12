from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.run_definition import RunDefinition
from openapi_server.models.start_run_result import StartRunResult
from openapi_server import util


async def runs_cancel_run_with_uri(request: web.Request, subscription_id, resource_group_name, workspace_name, experiment_name, run_id) -> web.Response:
    """Cancel a run.

    Cancels a run within an experiment.

    :param subscription_id: The Azure Subscription ID.
    :type subscription_id: str
    :type subscription_id: str
    :param resource_group_name: The Name of the resource group in which the workspace is located.
    :type resource_group_name: str
    :param workspace_name: The name of the workspace.
    :type workspace_name: str
    :param experiment_name: The experiment name.
    :type experiment_name: str
    :param run_id: The id of the run to cancel.
    :type run_id: str

    """
    return web.Response(status=200)


async def runs_start_local_run(request: web.Request, subscription_id, resource_group_name, workspace_name, experiment_name, definition, run_id=None) -> web.Response:
    """Start a run on a local machine.

    Starts an experiment run using the provided definition.json file to define the run.              The source code and configuration is defined in a zip archive in project.zip.

    :param subscription_id: The Azure Subscription ID.
    :type subscription_id: str
    :type subscription_id: str
    :param resource_group_name: The Name of the resource group in which the workspace is located.
    :type resource_group_name: str
    :param workspace_name: The name of the workspace.
    :type workspace_name: str
    :param experiment_name: The experiment name.
    :type experiment_name: str
    :param definition: A JSON run definition structure.
    :type definition: dict | bytes
    :param run_id: A run id. If not supplied a run id will be created automatically.
    :type run_id: str

    """
    definition = RunDefinition.from_dict(definition)
    return web.Response(status=200)


async def runs_start_run(request: web.Request, subscription_id, resource_group_name, workspace_name, experiment_name, run_definition_file, project_zip_file, run_id=None) -> web.Response:
    """Start a run on a remote compute target.

    Starts an experiment run using the provided definition.json file to define the run.              The source code and configuration is defined in a zip archive in project.zip.

    :param subscription_id: The Azure Subscription ID.
    :type subscription_id: str
    :type subscription_id: str
    :param resource_group_name: The Name of the resource group in which the workspace is located.
    :type resource_group_name: str
    :param workspace_name: The name of the workspace.
    :type workspace_name: str
    :param experiment_name: The experiment name.
    :type experiment_name: str
    :param run_definition_file: The JSON file containing the RunDefinition
    :type run_definition_file: str
    :param project_zip_file: The zip archive of the project folder containing the source code to use for the run.
    :type project_zip_file: str
    :param run_id: A run id. If not supplied a run id will be created automatically.
    :type run_id: str

    """
    return web.Response(status=200)


async def runs_start_snapshot_run(request: web.Request, subscription_id, resource_group_name, workspace_name, experiment_name, definition, run_id=None) -> web.Response:
    """Start a run from a snapshot on a remote compute target.

    Starts an experiment run on the remote compute target using the provided definition.json file to define the run.              The code for the run is retrieved using the snapshotId in definition.json.

    :param subscription_id: The Azure Subscription ID.
    :type subscription_id: str
    :type subscription_id: str
    :param resource_group_name: The Name of the resource group in which the workspace is located.
    :type resource_group_name: str
    :param workspace_name: The name of the workspace.
    :type workspace_name: str
    :param experiment_name: The experiment name.
    :type experiment_name: str
    :param definition: A JSON run definition structure.
    :type definition: dict | bytes
    :param run_id: A run id. If not supplied a run id will be created automatically.
    :type run_id: str

    """
    definition = RunDefinition.from_dict(definition)
    return web.Response(status=200)
