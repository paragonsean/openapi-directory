# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.operation import Operation
from openapi_server.models.run_pipeline_request import RunPipelineRequest


pytestmark = pytest.mark.asyncio

async def test_genomics_pipelines_run(client):
    """Test case for genomics_pipelines_run

    
    """
    body = {"pipeline":{"encryptedEnvironment":{"cipherText":"cipherText","keyName":"keyName"},"environment":{"key":"environment"},"resources":{"virtualMachine":{"disks":[{"sizeGb":1,"name":"name","sourceImage":"sourceImage","type":"type"},{"sizeGb":1,"name":"name","sourceImage":"sourceImage","type":"type"}],"volumes":[{"persistentDisk":{"sizeGb":5,"sourceImage":"sourceImage","type":"type"},"volume":"volume","nfsMount":{"target":"target"},"existingDisk":{"disk":"disk"}},{"persistentDisk":{"sizeGb":5,"sourceImage":"sourceImage","type":"type"},"volume":"volume","nfsMount":{"target":"target"},"existingDisk":{"disk":"disk"}}],"cpuPlatform":"cpuPlatform","serviceAccount":{"scopes":["scopes","scopes"],"email":"email"},"labels":{"key":"labels"},"network":{"subnetwork":"subnetwork","name":"name","usePrivateAddress":True},"nvidiaDriverVersion":"nvidiaDriverVersion","dockerCacheImages":["dockerCacheImages","dockerCacheImages"],"preemptible":True,"accelerators":[{"count":"count","type":"type"},{"count":"count","type":"type"}],"reservation":"reservation","bootImage":"bootImage","bootDiskSizeGb":6,"enableStackdriverMonitoring":True,"machineType":"machineType"},"regions":["regions","regions"],"zones":["zones","zones"],"projectId":"projectId"},"actions":[{"encryptedEnvironment":{"cipherText":"cipherText","keyName":"keyName"},"credentials":{"cipherText":"cipherText","keyName":"keyName"},"flags":["FLAG_UNSPECIFIED","FLAG_UNSPECIFIED"],"mounts":[{"path":"path","disk":"disk","readOnly":True},{"path":"path","disk":"disk","readOnly":True}],"timeout":"timeout","labels":{"key":"labels"},"portMappings":{"key":0},"environment":{"key":"environment"},"imageUri":"imageUri","entrypoint":"entrypoint","name":"name","pidNamespace":"pidNamespace","commands":["commands","commands"]},{"encryptedEnvironment":{"cipherText":"cipherText","keyName":"keyName"},"credentials":{"cipherText":"cipherText","keyName":"keyName"},"flags":["FLAG_UNSPECIFIED","FLAG_UNSPECIFIED"],"mounts":[{"path":"path","disk":"disk","readOnly":True},{"path":"path","disk":"disk","readOnly":True}],"timeout":"timeout","labels":{"key":"labels"},"portMappings":{"key":0},"environment":{"key":"environment"},"imageUri":"imageUri","entrypoint":"entrypoint","name":"name","pidNamespace":"pidNamespace","commands":["commands","commands"]}],"timeout":"timeout"},"pubSubTopic":"pubSubTopic","labels":{"key":"labels"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2alpha1/pipelines:run',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

