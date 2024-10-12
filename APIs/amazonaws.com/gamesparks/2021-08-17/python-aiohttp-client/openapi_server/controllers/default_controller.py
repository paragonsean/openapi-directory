from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_game_request import CreateGameRequest
from openapi_server.models.create_game_result import CreateGameResult
from openapi_server.models.create_snapshot_request import CreateSnapshotRequest
from openapi_server.models.create_snapshot_result import CreateSnapshotResult
from openapi_server.models.create_stage_request import CreateStageRequest
from openapi_server.models.create_stage_result import CreateStageResult
from openapi_server.models.disconnect_player_result import DisconnectPlayerResult
from openapi_server.models.export_snapshot_result import ExportSnapshotResult
from openapi_server.models.get_extension_result import GetExtensionResult
from openapi_server.models.get_extension_version_result import GetExtensionVersionResult
from openapi_server.models.get_game_configuration_result import GetGameConfigurationResult
from openapi_server.models.get_game_result import GetGameResult
from openapi_server.models.get_generated_code_job_result import GetGeneratedCodeJobResult
from openapi_server.models.get_player_connection_status_result import GetPlayerConnectionStatusResult
from openapi_server.models.get_snapshot_result import GetSnapshotResult
from openapi_server.models.get_stage_deployment_result import GetStageDeploymentResult
from openapi_server.models.get_stage_result import GetStageResult
from openapi_server.models.import_game_configuration_request import ImportGameConfigurationRequest
from openapi_server.models.import_game_configuration_result import ImportGameConfigurationResult
from openapi_server.models.list_extension_versions_result import ListExtensionVersionsResult
from openapi_server.models.list_extensions_result import ListExtensionsResult
from openapi_server.models.list_games_result import ListGamesResult
from openapi_server.models.list_generated_code_jobs_result import ListGeneratedCodeJobsResult
from openapi_server.models.list_snapshots_result import ListSnapshotsResult
from openapi_server.models.list_stage_deployments_result import ListStageDeploymentsResult
from openapi_server.models.list_stages_result import ListStagesResult
from openapi_server.models.list_tags_for_resource_result import ListTagsForResourceResult
from openapi_server.models.start_generated_code_job_request import StartGeneratedCodeJobRequest
from openapi_server.models.start_generated_code_job_result import StartGeneratedCodeJobResult
from openapi_server.models.start_stage_deployment_request import StartStageDeploymentRequest
from openapi_server.models.start_stage_deployment_result import StartStageDeploymentResult
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.update_game_configuration_request import UpdateGameConfigurationRequest
from openapi_server.models.update_game_configuration_result import UpdateGameConfigurationResult
from openapi_server.models.update_game_request import UpdateGameRequest
from openapi_server.models.update_game_result import UpdateGameResult
from openapi_server.models.update_snapshot_result import UpdateSnapshotResult
from openapi_server.models.update_stage_request import UpdateStageRequest
from openapi_server.models.update_stage_result import UpdateStageResult
from openapi_server import util


async def create_game(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_game

     Creates a new game with an empty configuration. After creating your game, you can update the configuration using &lt;code&gt;UpdateGameConfiguration&lt;/code&gt; or &lt;code&gt;ImportGameConfiguration&lt;/code&gt;. 

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateGameRequest.from_dict(body)
    return web.Response(status=200)


async def create_snapshot(request: web.Request, game_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_snapshot

    Creates a snapshot of the game configuration.

    :param game_name: The name of the game.
    :type game_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateSnapshotRequest.from_dict(body)
    return web.Response(status=200)


async def create_stage(request: web.Request, game_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_stage

    Creates a new stage for stage-by-stage game development and deployment.

    :param game_name: The name of the game.
    :type game_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateStageRequest.from_dict(body)
    return web.Response(status=200)


async def delete_game(request: web.Request, game_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_game

    Deletes a game.

    :param game_name: The name of the game to delete.
    :type game_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def delete_stage(request: web.Request, game_name, stage_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_stage

    Deletes a stage from a game, along with the associated game runtime.

    :param game_name: The name of the game.
    :type game_name: str
    :param stage_name: The name of the stage to delete.
    :type stage_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def disconnect_player(request: web.Request, game_name, player_id, stage_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """disconnect_player

    &lt;p&gt;Disconnects a player from the game runtime.&lt;/p&gt; &lt;p&gt; If a player has multiple connections, this operation attempts to close all of them. &lt;/p&gt;

    :param game_name: The name of the game.
    :type game_name: str
    :param player_id: The unique identifier representing a player.
    :type player_id: str
    :param stage_name: The name of the stage.
    :type stage_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def export_snapshot(request: web.Request, game_name, snapshot_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """export_snapshot

    Exports a game configuration snapshot.

    :param game_name: The name of the game.
    :type game_name: str
    :param snapshot_id: The identifier of the snapshot to export.
    :type snapshot_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_extension(request: web.Request, name, namespace, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_extension

    Gets details about a specified extension.

    :param name: The name of the extension.
    :type name: str
    :param namespace: The namespace (qualifier) of the extension.
    :type namespace: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_extension_version(request: web.Request, extension_version, name, namespace, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_extension_version

    Gets details about a specified extension version.

    :param extension_version: The version of the extension.
    :type extension_version: str
    :param name: The name of the extension.
    :type name: str
    :param namespace: The namespace (qualifier) of the extension.
    :type namespace: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_game(request: web.Request, game_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_game

    Gets details about a game.

    :param game_name: The name of the game.
    :type game_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_game_configuration(request: web.Request, game_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, sections=None) -> web.Response:
    """get_game_configuration

    Gets the configuration of the game.

    :param game_name: The name of the game.
    :type game_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param sections: The list of sections to return.
    :type sections: List[str]

    """
    return web.Response(status=200)


async def get_generated_code_job(request: web.Request, game_name, job_id, snapshot_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_generated_code_job

    Gets details about a job that is generating code for a snapshot.

    :param game_name: The name of the game.
    :type game_name: str
    :param job_id: The identifier of the code generation job.
    :type job_id: str
    :param snapshot_id: The identifier of the snapshot for the code generation job.
    :type snapshot_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_player_connection_status(request: web.Request, game_name, player_id, stage_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_player_connection_status

    &lt;p&gt;Gets the status of a player&#39;s connection to the game runtime.&lt;/p&gt; &lt;p&gt; It&#39;s possible for a single player to have multiple connections to the game runtime. If a player is not connected, this operation returns an empty list. &lt;/p&gt;

    :param game_name: The name of the game.
    :type game_name: str
    :param player_id: The unique identifier representing a player.
    :type player_id: str
    :param stage_name: The name of the stage.
    :type stage_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_snapshot(request: web.Request, game_name, snapshot_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, sections=None) -> web.Response:
    """get_snapshot

    Gets a copy of the game configuration in a snapshot.

    :param game_name: The name of the game.
    :type game_name: str
    :param snapshot_id: The identifier of the snapshot.
    :type snapshot_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param sections: The list of game configuration sections to be described.
    :type sections: List[str]

    """
    return web.Response(status=200)


async def get_stage(request: web.Request, game_name, stage_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_stage

    Gets information about a stage.

    :param game_name: The name of the game.
    :type game_name: str
    :param stage_name: The name of the stage.
    :type stage_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_stage_deployment(request: web.Request, game_name, stage_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, deployment_id=None) -> web.Response:
    """get_stage_deployment

    Gets information about a stage deployment.

    :param game_name: The name of the game.
    :type game_name: str
    :param stage_name: The name of the stage.
    :type stage_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param deployment_id:  The identifier of the stage deployment. &lt;code&gt;StartStageDeployment&lt;/code&gt; returns the identifier that you use here. 
    :type deployment_id: str

    """
    return web.Response(status=200)


async def import_game_configuration(request: web.Request, game_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """import_game_configuration

    &lt;p&gt;Imports a game configuration.&lt;/p&gt; &lt;p&gt; This operation replaces the current configuration of the game with the provided input. This is not a reversible operation. If you want to preserve the previous configuration, use &lt;code&gt;CreateSnapshot&lt;/code&gt; to make a new snapshot before importing. &lt;/p&gt;

    :param game_name: The name of the game.
    :type game_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = ImportGameConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def list_extension_versions(request: web.Request, name, namespace, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_extension_versions

    &lt;p&gt;Gets a paginated list of available versions for the extension.&lt;/p&gt; &lt;p&gt; Each time an API change is made to an extension, the version is incremented. The list retrieved by this operation shows the versions that are currently available. &lt;/p&gt;

    :param name: The name of the extension.
    :type name: str
    :param namespace: The namespace (qualifier) of the extension.
    :type namespace: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: &lt;p&gt;The maximum number of results to return.&lt;/p&gt; &lt;p&gt; Use this parameter with NextToken to get results as a set of sequential pages. &lt;/p&gt;
    :type max_results: int
    :param next_token: &lt;p&gt;The token that indicates the start of the next sequential page of results.&lt;/p&gt; &lt;p&gt; Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value. &lt;/p&gt;
    :type next_token: str

    """
    return web.Response(status=200)


async def list_extensions(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_extensions

    &lt;p&gt;Gets a paginated list of available extensions.&lt;/p&gt; &lt;p&gt; Extensions provide features that games can use from scripts. &lt;/p&gt;

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: &lt;p&gt;The maximum number of results to return.&lt;/p&gt; &lt;p&gt; Use this parameter with NextToken to get results as a set of sequential pages. &lt;/p&gt;
    :type max_results: int
    :param next_token: &lt;p&gt;The token that indicates the start of the next sequential page of results.&lt;/p&gt; &lt;p&gt; Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value. &lt;/p&gt;
    :type next_token: str

    """
    return web.Response(status=200)


async def list_games(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_games

    Gets a paginated list of games.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: &lt;p&gt;The maximum number of results to return.&lt;/p&gt; &lt;p&gt; Use this parameter with NextToken to get results as a set of sequential pages. &lt;/p&gt;
    :type max_results: int
    :param next_token: &lt;p&gt;The token that indicates the start of the next sequential page of results.&lt;/p&gt; &lt;p&gt; Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value. &lt;/p&gt;
    :type next_token: str

    """
    return web.Response(status=200)


async def list_generated_code_jobs(request: web.Request, game_name, snapshot_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_generated_code_jobs

    Gets a paginated list of code generation jobs for a snapshot.

    :param game_name: The name of the game.
    :type game_name: str
    :param snapshot_id: The identifier of the snapshot.
    :type snapshot_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: &lt;p&gt;The maximum number of results to return.&lt;/p&gt; &lt;p&gt; Use this parameter with NextToken to get results as a set of sequential pages. &lt;/p&gt;
    :type max_results: int
    :param next_token: &lt;p&gt;The token that indicates the start of the next sequential page of results.&lt;/p&gt; &lt;p&gt; Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value. &lt;/p&gt;
    :type next_token: str

    """
    return web.Response(status=200)


async def list_snapshots(request: web.Request, game_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_snapshots

    Gets a paginated list of snapshot summaries from the game.

    :param game_name: The name of the game.
    :type game_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: &lt;p&gt;The maximum number of results to return.&lt;/p&gt; &lt;p&gt; Use this parameter with NextToken to get results as a set of sequential pages. &lt;/p&gt;
    :type max_results: int
    :param next_token: &lt;p&gt;The token that indicates the start of the next sequential page of results.&lt;/p&gt; &lt;p&gt; Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value. &lt;/p&gt;
    :type next_token: str

    """
    return web.Response(status=200)


async def list_stage_deployments(request: web.Request, game_name, stage_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_stage_deployments

    Gets a paginated list of stage deployment summaries from the game.

    :param game_name: The name of the game.
    :type game_name: str
    :param stage_name: The name of the stage.
    :type stage_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: &lt;p&gt;The maximum number of results to return.&lt;/p&gt; &lt;p&gt; Use this parameter with NextToken to get results as a set of sequential pages. &lt;/p&gt;
    :type max_results: int
    :param next_token: &lt;p&gt;The token that indicates the start of the next sequential page of results.&lt;/p&gt; &lt;p&gt; Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value. &lt;/p&gt;
    :type next_token: str

    """
    return web.Response(status=200)


async def list_stages(request: web.Request, game_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_stages

    Gets a paginated list of stage summaries from the game.

    :param game_name: The name of the game.
    :type game_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: &lt;p&gt;The maximum number of results to return.&lt;/p&gt; &lt;p&gt; Use this parameter with NextToken to get results as a set of sequential pages. &lt;/p&gt;
    :type max_results: int
    :param next_token: &lt;p&gt;The token that indicates the start of the next sequential page of results.&lt;/p&gt; &lt;p&gt; Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value. &lt;/p&gt;
    :type next_token: str

    """
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, resource_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

    Lists the tags associated with a GameSparks resource.

    :param resource_arn: The Amazon Resource Name (ARN) of the GameSparks resource.
    :type resource_arn: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def start_generated_code_job(request: web.Request, game_name, snapshot_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_generated_code_job

     Starts an asynchronous process that generates client code for system-defined and custom messages. The resulting code is collected as a .zip file and uploaded to a pre-signed Amazon S3 URL. 

    :param game_name: The name of the game.
    :type game_name: str
    :param snapshot_id: The identifier of the snapshot for which to generate code.
    :type snapshot_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = StartGeneratedCodeJobRequest.from_dict(body)
    return web.Response(status=200)


async def start_stage_deployment(request: web.Request, game_name, stage_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_stage_deployment

    &lt;p&gt;Deploys a snapshot to the stage and creates a new game runtime.&lt;/p&gt; &lt;p&gt; After you call this operation, you can check the deployment status by using &lt;code&gt;GetStageDeployment&lt;/code&gt;. &lt;/p&gt; &lt;p&gt; If there are any players connected to the previous game runtime, then both runtimes persist. Existing connections to the previous runtime are maintained. When players disconnect and reconnect, they connect to the new runtime. After there are no connections to the previous game runtime, it is deleted. &lt;/p&gt;

    :param game_name: The name of the game.
    :type game_name: str
    :param stage_name: The name of the stage to deploy the snapshot onto.
    :type stage_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = StartStageDeploymentRequest.from_dict(body)
    return web.Response(status=200)


async def tag_resource(request: web.Request, resource_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    Adds tags to a GameSparks resource.

    :param resource_arn: The Amazon Resource Name (ARN) of the resource to add the tags to.
    :type resource_arn: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = TagResourceRequest.from_dict(body)
    return web.Response(status=200)


async def untag_resource(request: web.Request, resource_arn, tag_keys, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """untag_resource

    Removes tags from a GameSparks resource.

    :param resource_arn: The Amazon Resource Name (ARN) of the resource to remove the tags from.
    :type resource_arn: str
    :param tag_keys: The keys of the tags to remove.
    :type tag_keys: List[str]
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def update_game(request: web.Request, game_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_game

    Updates details of the game.

    :param game_name: The name of the game.
    :type game_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateGameRequest.from_dict(body)
    return web.Response(status=200)


async def update_game_configuration(request: web.Request, game_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_game_configuration

    Updates one or more sections of the game configuration.

    :param game_name: The name of the game.
    :type game_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateGameConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def update_snapshot(request: web.Request, game_name, snapshot_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_snapshot

    Updates the metadata of a GameSparks snapshot.

    :param game_name: The name of the game.
    :type game_name: str
    :param snapshot_id: The identifier of the snapshot.
    :type snapshot_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateSnapshotRequest.from_dict(body)
    return web.Response(status=200)


async def update_stage(request: web.Request, game_name, stage_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_stage

    Updates the metadata of a stage.

    :param game_name: The name of the game.
    :type game_name: str
    :param stage_name: The name of the stage.
    :type stage_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateStageRequest.from_dict(body)
    return web.Response(status=200)
