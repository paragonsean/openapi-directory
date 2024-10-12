# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_pipe_request import CreatePipeRequest
from openapi_server.models.create_pipe_response import CreatePipeResponse
from openapi_server.models.delete_pipe_response import DeletePipeResponse
from openapi_server.models.describe_pipe_response import DescribePipeResponse
from openapi_server.models.list_pipes_response import ListPipesResponse
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.start_pipe_response import StartPipeResponse
from openapi_server.models.stop_pipe_response import StopPipeResponse
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.update_pipe_request import UpdatePipeRequest
from openapi_server.models.update_pipe_response import UpdatePipeResponse


pytestmark = pytest.mark.asyncio

async def test_create_pipe(client):
    """Test case for create_pipe

    
    """
    body = {"Enrichment":"","Target":"","Description":"","DesiredState":"","TargetParameters":{"HttpParameters":{"PathParameterValues":"","HeaderParameters":"","QueryStringParameters":""},"StepFunctionStateMachineParameters":{"InvocationType":""},"SqsQueueParameters":{"MessageGroupId":"","MessageDeduplicationId":""},"CloudWatchLogsParameters":{"LogStreamName":"","Timestamp":""},"KinesisStreamParameters":{"PartitionKey":""},"InputTemplate":"","SageMakerPipelineParameters":{"PipelineParameterList":""},"EventBridgeEventBusParameters":{"DetailType":"","EndpointId":"","Time":"","Resources":"","Source":""},"BatchJobParameters":{"DependsOn":"","Parameters":"","ArrayProperties":{"Size":""},"JobName":"","RetryStrategy":{"Attempts":""},"ContainerOverrides":{"Command":"","Environment":"","InstanceType":"","ResourceRequirements":""},"JobDefinition":""},"EcsTaskParameters":{"PlatformVersion":"","Group":"","EnableECSManagedTags":"","EnableExecuteCommand":"","PlacementConstraints":"","PropagateTags":"","TaskCount":"","PlacementStrategy":"","CapacityProviderStrategy":"","LaunchType":"","ReferenceId":"","Overrides":{"ExecutionRoleArn":"","TaskRoleArn":"","Memory":"","Cpu":"","InferenceAcceleratorOverrides":"","EphemeralStorage":{"sizeInGiB":""},"ContainerOverrides":""},"NetworkConfiguration":{"awsvpcConfiguration":{"SecurityGroups":"","Subnets":"","AssignPublicIp":""}},"Tags":"","TaskDefinitionArn":""},"LambdaFunctionParameters":{"InvocationType":""},"RedshiftDataParameters":{"StatementName":"","Sqls":"","Database":"","SecretManagerArn":"","DbUser":"","WithEvent":""}},"EnrichmentParameters":{"HttpParameters":{"PathParameterValues":"","HeaderParameters":"","QueryStringParameters":""},"InputTemplate":""},"RoleArn":"","Source":"","SourceParameters":{"ManagedStreamingKafkaParameters":{"StartingPosition":"","BatchSize":"","ConsumerGroupID":"","Credentials":{"ClientCertificateTlsAuth":"","SaslScram512Auth":""},"MaximumBatchingWindowInSeconds":"","TopicName":""},"DynamoDBStreamParameters":{"StartingPosition":"","BatchSize":"","MaximumRetryAttempts":"","OnPartialBatchItemFailure":"","DeadLetterConfig":{"Arn":""},"ParallelizationFactor":"","MaximumRecordAgeInSeconds":"","MaximumBatchingWindowInSeconds":""},"SelfManagedKafkaParameters":{"StartingPosition":"","BatchSize":"","ConsumerGroupID":"","AdditionalBootstrapServers":"","Vpc":{"Subnets":"","SecurityGroup":""},"Credentials":{"BasicAuth":"","SaslScram256Auth":"","ClientCertificateTlsAuth":"","SaslScram512Auth":""},"ServerRootCaCertificate":"","MaximumBatchingWindowInSeconds":"","TopicName":""},"RabbitMQBrokerParameters":{"BatchSize":"","VirtualHost":"","QueueName":"","Credentials":{"BasicAuth":""},"MaximumBatchingWindowInSeconds":""},"SqsQueueParameters":{"BatchSize":"","MaximumBatchingWindowInSeconds":""},"KinesisStreamParameters":{"StartingPosition":"","BatchSize":"","MaximumRetryAttempts":"","OnPartialBatchItemFailure":"","DeadLetterConfig":{"Arn":""},"ParallelizationFactor":"","MaximumRecordAgeInSeconds":"","StartingPositionTimestamp":"","MaximumBatchingWindowInSeconds":""},"FilterCriteria":{"Filters":""},"ActiveMQBrokerParameters":{"BatchSize":"","QueueName":"","Credentials":{"BasicAuth":""},"MaximumBatchingWindowInSeconds":""}},"Tags":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/pipes/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_pipe(client):
    """Test case for delete_pipe

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/pipes/{name}'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_pipe(client):
    """Test case for describe_pipe

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/pipes/{name}'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_pipes(client):
    """Test case for list_pipes

    
    """
    params = [('CurrentState', 'current_state_example'),
                    ('DesiredState', 'desired_state_example'),
                    ('Limit', 56),
                    ('NamePrefix', 'name_prefix_example'),
                    ('NextToken', 'next_token_example'),
                    ('SourcePrefix', 'source_prefix_example'),
                    ('TargetPrefix', 'target_prefix_example')]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/pipes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_tags_for_resource(client):
    """Test case for list_tags_for_resource

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/tags/{resource_arn}'.format(resource_arn='resource_arn_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_start_pipe(client):
    """Test case for start_pipe

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/pipes/{name}/start'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stop_pipe(client):
    """Test case for stop_pipe

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/pipes/{name}/stop'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tag_resource(client):
    """Test case for tag_resource

    
    """
    body = {"tags":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/tags/{resource_arn}'.format(resource_arn='resource_arn_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_untag_resource(client):
    """Test case for untag_resource

    
    """
    params = [('tagKeys', ['tag_keys_example'])]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/tags/{resource_arntag_key}'.format(resource_arn='resource_arn_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_pipe(client):
    """Test case for update_pipe

    
    """
    body = {"Enrichment":"","Target":"","Description":"","DesiredState":"","TargetParameters":{"HttpParameters":{"PathParameterValues":"","HeaderParameters":"","QueryStringParameters":""},"StepFunctionStateMachineParameters":{"InvocationType":""},"SqsQueueParameters":{"MessageGroupId":"","MessageDeduplicationId":""},"CloudWatchLogsParameters":{"LogStreamName":"","Timestamp":""},"KinesisStreamParameters":{"PartitionKey":""},"InputTemplate":"","SageMakerPipelineParameters":{"PipelineParameterList":""},"EventBridgeEventBusParameters":{"DetailType":"","EndpointId":"","Time":"","Resources":"","Source":""},"BatchJobParameters":{"DependsOn":"","Parameters":"","ArrayProperties":{"Size":""},"JobName":"","RetryStrategy":{"Attempts":""},"ContainerOverrides":{"Command":"","Environment":"","InstanceType":"","ResourceRequirements":""},"JobDefinition":""},"EcsTaskParameters":{"PlatformVersion":"","Group":"","EnableECSManagedTags":"","EnableExecuteCommand":"","PlacementConstraints":"","PropagateTags":"","TaskCount":"","PlacementStrategy":"","CapacityProviderStrategy":"","LaunchType":"","ReferenceId":"","Overrides":{"ExecutionRoleArn":"","TaskRoleArn":"","Memory":"","Cpu":"","InferenceAcceleratorOverrides":"","EphemeralStorage":{"sizeInGiB":""},"ContainerOverrides":""},"NetworkConfiguration":{"awsvpcConfiguration":{"SecurityGroups":"","Subnets":"","AssignPublicIp":""}},"Tags":"","TaskDefinitionArn":""},"LambdaFunctionParameters":{"InvocationType":""},"RedshiftDataParameters":{"StatementName":"","Sqls":"","Database":"","SecretManagerArn":"","DbUser":"","WithEvent":""}},"EnrichmentParameters":{"HttpParameters":{"PathParameterValues":"","HeaderParameters":"","QueryStringParameters":""},"InputTemplate":""},"RoleArn":"","SourceParameters":{"ManagedStreamingKafkaParameters":{"BatchSize":"","Credentials":{"ClientCertificateTlsAuth":"","SaslScram512Auth":""},"MaximumBatchingWindowInSeconds":""},"DynamoDBStreamParameters":{"BatchSize":"","MaximumRetryAttempts":"","OnPartialBatchItemFailure":"","DeadLetterConfig":{"Arn":""},"ParallelizationFactor":"","MaximumRecordAgeInSeconds":"","MaximumBatchingWindowInSeconds":""},"SelfManagedKafkaParameters":{"BatchSize":"","Vpc":{"Subnets":"","SecurityGroup":""},"Credentials":{"BasicAuth":"","SaslScram256Auth":"","ClientCertificateTlsAuth":"","SaslScram512Auth":""},"ServerRootCaCertificate":"","MaximumBatchingWindowInSeconds":""},"RabbitMQBrokerParameters":{"BatchSize":"","Credentials":{"BasicAuth":""},"MaximumBatchingWindowInSeconds":""},"SqsQueueParameters":{"BatchSize":"","MaximumBatchingWindowInSeconds":""},"KinesisStreamParameters":{"BatchSize":"","MaximumRetryAttempts":"","OnPartialBatchItemFailure":"","DeadLetterConfig":{"Arn":""},"ParallelizationFactor":"","MaximumRecordAgeInSeconds":"","MaximumBatchingWindowInSeconds":""},"FilterCriteria":{"Filters":""},"ActiveMQBrokerParameters":{"BatchSize":"","Credentials":{"BasicAuth":""},"MaximumBatchingWindowInSeconds":""}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/pipes/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

