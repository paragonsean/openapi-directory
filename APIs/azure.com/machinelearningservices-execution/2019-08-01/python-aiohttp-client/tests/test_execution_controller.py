# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.run_definition import RunDefinition
from openapi_server.models.start_run_result import StartRunResult


pytestmark = pytest.mark.asyncio

async def test_execution_cancel_run_with_uri(client):
    """Test case for execution_cancel_run_with_uri

    Cancel a run.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/execution/v1.0/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MachineLearningServices/workspaces/{workspace_name}/experiments/{experiment_name}/runId/{run_id}/cancel'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workspace_name='workspace_name_example', experiment_name='experiment_name_example', run_id='run_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_execution_start_local_run(client):
    """Test case for execution_start_local_run

    Start a run on a local machine.
    """
    definition = {"parentRunId":"myexperiment_155000000001_0","snapshotId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","configuration":{"jobName":"FindSquaresJob","mpi":{"processCountPerNode":2},"history":{"directoriesToWatch":"[\"logs\", \"outputs\"]","outputCollection":True},"hdi":{"yarnDeployMode":"None"},"script":"findsquare.py","target":"amlcompute","environment":{"python":{"baseCondaEnvironment":"baseCondaEnvironment","userManagedDependencies":True,"condaDependencies":"{}","interpreterPath":"interpreterPath"},"spark":{"repositories":["repositories","repositories"],"precachePackages":True,"packages":[{"artifact":"artifact","version":"version","group":"group"},{"artifact":"artifact","version":"version","group":"group"}]},"environmentVariables":{"key":"environmentVariables"},"inferencingStackVersion":"latest","name":"mydevenvironment","version":"1","docker":{"sharedVolumes":True,"baseImage":"ubuntu:latest","arguments":["arguments","arguments"],"baseDockerfile":"FROM ubuntu:latest\r\nRUN echo \"Hello world!\"","enabled":True,"baseImageRegistry":{"password":"password","address":"address","username":"username"}}},"tensorflow":{"workerCount":2,"parameterServerCount":1},"framework":"Python","spark":{"configuration":{"key":"configuration"}},"maxRunDurationSeconds":84000,"arguments":"[\"234\"]","nodeCount":1,"communicator":"None","dataReferences":{"key":{"mode":"Mount","pathOnDataStore":"/images/validation","dataStoreName":"myblobstore","pathOnCompute":"pathOnCompute","overwrite":True}}},"runType":"experiment"}
    params = [('runId', 'run_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/execution/v1.0/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MachineLearningServices/workspaces/{workspace_name}/experiments/{experiment_name}/startlocalrun'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workspace_name='workspace_name_example', experiment_name='experiment_name_example'),
        headers=headers,
        json=definition,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_execution_start_run(client):
    """Test case for execution_start_run

    Start a run on a remote compute target.
    """
    params = [('runId', 'run_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('run_definition_file', '/path/to/file')
    data.add_field('project_zip_file', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/execution/v1.0/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MachineLearningServices/workspaces/{workspace_name}/experiments/{experiment_name}/startrun'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workspace_name='workspace_name_example', experiment_name='experiment_name_example'),
        headers=headers,
        data=data,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_execution_start_snapshot_run(client):
    """Test case for execution_start_snapshot_run

    Start a run from a snapshot on a remote compute target.
    """
    definition = {"parentRunId":"myexperiment_155000000001_0","snapshotId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","configuration":{"jobName":"FindSquaresJob","mpi":{"processCountPerNode":2},"history":{"directoriesToWatch":"[\"logs\", \"outputs\"]","outputCollection":True},"hdi":{"yarnDeployMode":"None"},"script":"findsquare.py","target":"amlcompute","environment":{"python":{"baseCondaEnvironment":"baseCondaEnvironment","userManagedDependencies":True,"condaDependencies":"{}","interpreterPath":"interpreterPath"},"spark":{"repositories":["repositories","repositories"],"precachePackages":True,"packages":[{"artifact":"artifact","version":"version","group":"group"},{"artifact":"artifact","version":"version","group":"group"}]},"environmentVariables":{"key":"environmentVariables"},"inferencingStackVersion":"latest","name":"mydevenvironment","version":"1","docker":{"sharedVolumes":True,"baseImage":"ubuntu:latest","arguments":["arguments","arguments"],"baseDockerfile":"FROM ubuntu:latest\r\nRUN echo \"Hello world!\"","enabled":True,"baseImageRegistry":{"password":"password","address":"address","username":"username"}}},"tensorflow":{"workerCount":2,"parameterServerCount":1},"framework":"Python","spark":{"configuration":{"key":"configuration"}},"maxRunDurationSeconds":84000,"arguments":"[\"234\"]","nodeCount":1,"communicator":"None","dataReferences":{"key":{"mode":"Mount","pathOnDataStore":"/images/validation","dataStoreName":"myblobstore","pathOnCompute":"pathOnCompute","overwrite":True}}},"runType":"experiment"}
    params = [('runId', 'run_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/execution/v1.0/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MachineLearningServices/workspaces/{workspace_name}/experiments/{experiment_name}/snapshotrun'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workspace_name='workspace_name_example', experiment_name='experiment_name_example'),
        headers=headers,
        json=definition,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

