# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.database import Database
from openapi_server.models.database_list_result import DatabaseListResult
from openapi_server.models.database_update import DatabaseUpdate


pytestmark = pytest.mark.asyncio

async def test_databases_create_or_update(client):
    """Test case for databases_create_or_update

    
    """
    parameters = {"kind":"kind","properties":{"elasticPoolName":"elasticPoolName","sourceDatabaseDeletionDate":"2000-01-23T04:56:07.000+00:00","edition":"Web","failoverGroupId":"failoverGroupId","currentServiceObjectiveId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","recommendedIndex":[{"properties":{"reportedImpact":[{"unit":"unit","changeValueRelative":1.4658129805029452,"name":"name","changeValueAbsolute":6.027456183070403},{"unit":"unit","changeValueRelative":1.4658129805029452,"name":"name","changeValueAbsolute":6.027456183070403}],"schema":"schema","estimatedImpact":[{"unit":"unit","changeValueRelative":1.4658129805029452,"name":"name","changeValueAbsolute":6.027456183070403},{"unit":"unit","changeValueRelative":1.4658129805029452,"name":"name","changeValueAbsolute":6.027456183070403}],"indexType":"CLUSTERED","columns":["columns","columns"],"created":"2000-01-23T04:56:07.000+00:00","includedColumns":["includedColumns","includedColumns"],"action":"Create","indexScript":"indexScript","lastModified":"2000-01-23T04:56:07.000+00:00","state":"Active","table":"table"}},{"properties":{"reportedImpact":[{"unit":"unit","changeValueRelative":1.4658129805029452,"name":"name","changeValueAbsolute":6.027456183070403},{"unit":"unit","changeValueRelative":1.4658129805029452,"name":"name","changeValueAbsolute":6.027456183070403}],"schema":"schema","estimatedImpact":[{"unit":"unit","changeValueRelative":1.4658129805029452,"name":"name","changeValueAbsolute":6.027456183070403},{"unit":"unit","changeValueRelative":1.4658129805029452,"name":"name","changeValueAbsolute":6.027456183070403}],"indexType":"CLUSTERED","columns":["columns","columns"],"created":"2000-01-23T04:56:07.000+00:00","includedColumns":["includedColumns","includedColumns"],"action":"Create","indexScript":"indexScript","lastModified":"2000-01-23T04:56:07.000+00:00","state":"Active","table":"table"}}],"restorePointInTime":"2000-01-23T04:56:07.000+00:00","sampleName":"AdventureWorksLT","maxSizeBytes":"maxSizeBytes","defaultSecondaryLocation":"defaultSecondaryLocation","collation":"collation","databaseId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","earliestRestoreDate":"2000-01-23T04:56:07.000+00:00","requestedServiceObjectiveName":"System","transparentDataEncryption":[{"location":"location","properties":{"status":"Enabled"}},{"location":"location","properties":{"status":"Enabled"}}],"serviceTierAdvisors":[{"properties":{"currentServiceLevelObjective":"currentServiceLevelObjective","databaseSizeBasedRecommendationServiceLevelObjective":"databaseSizeBasedRecommendationServiceLevelObjective","overallRecommendationServiceLevelObjective":"overallRecommendationServiceLevelObjective","avgDtu":5.637376656633329,"confidence":2.3021358869347655,"overallRecommendationServiceLevelObjectiveId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","minDtu":3.616076749251911,"disasterPlanBasedRecommendationServiceLevelObjectiveId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","usageBasedRecommendationServiceLevelObjectiveId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","maxDtu":7.061401241503109,"serviceLevelObjectiveUsageMetrics":[{"serviceLevelObjectiveId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","serviceLevelObjective":"System","inRangeTimeRatio":2.027123023002322},{"serviceLevelObjectiveId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","serviceLevelObjective":"System","inRangeTimeRatio":2.027123023002322}],"observationPeriodEnd":"2000-01-23T04:56:07.000+00:00","activeTimeRatio":5.962133916683182,"databaseSizeBasedRecommendationServiceLevelObjectiveId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","currentServiceLevelObjectiveId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","disasterPlanBasedRecommendationServiceLevelObjective":"disasterPlanBasedRecommendationServiceLevelObjective","observationPeriodStart":"2000-01-23T04:56:07.000+00:00","maxSizeInGB":9.301444243932576,"usageBasedRecommendationServiceLevelObjective":"usageBasedRecommendationServiceLevelObjective"}},{"properties":{"currentServiceLevelObjective":"currentServiceLevelObjective","databaseSizeBasedRecommendationServiceLevelObjective":"databaseSizeBasedRecommendationServiceLevelObjective","overallRecommendationServiceLevelObjective":"overallRecommendationServiceLevelObjective","avgDtu":5.637376656633329,"confidence":2.3021358869347655,"overallRecommendationServiceLevelObjectiveId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","minDtu":3.616076749251911,"disasterPlanBasedRecommendationServiceLevelObjectiveId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","usageBasedRecommendationServiceLevelObjectiveId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","maxDtu":7.061401241503109,"serviceLevelObjectiveUsageMetrics":[{"serviceLevelObjectiveId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","serviceLevelObjective":"System","inRangeTimeRatio":2.027123023002322},{"serviceLevelObjectiveId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","serviceLevelObjective":"System","inRangeTimeRatio":2.027123023002322}],"observationPeriodEnd":"2000-01-23T04:56:07.000+00:00","activeTimeRatio":5.962133916683182,"databaseSizeBasedRecommendationServiceLevelObjectiveId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","currentServiceLevelObjectiveId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","disasterPlanBasedRecommendationServiceLevelObjective":"disasterPlanBasedRecommendationServiceLevelObjective","observationPeriodStart":"2000-01-23T04:56:07.000+00:00","maxSizeInGB":9.301444243932576,"usageBasedRecommendationServiceLevelObjective":"usageBasedRecommendationServiceLevelObjective"}}],"readScale":"Enabled","createMode":"Copy","zoneRedundant":True,"creationDate":"2000-01-23T04:56:07.000+00:00","serviceLevelObjective":"System","sourceDatabaseId":"sourceDatabaseId","recoveryServicesRecoveryPointResourceId":"recoveryServicesRecoveryPointResourceId","containmentState":0,"requestedServiceObjectiveId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","status":"status"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/databases/{database_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', server_name='server_name_example', database_name='database_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_databases_delete(client):
    """Test case for databases_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/databases/{database_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', server_name='server_name_example', database_name='database_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_databases_get(client):
    """Test case for databases_get

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/databases/{database_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', server_name='server_name_example', database_name='database_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_databases_get_by_recommended_elastic_pool(client):
    """Test case for databases_get_by_recommended_elastic_pool

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/recommendedElasticPools/{recommended_elastic_pool_name}/databases/{database_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', server_name='server_name_example', recommended_elastic_pool_name='recommended_elastic_pool_name_example', database_name='database_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_databases_list_by_elastic_pool(client):
    """Test case for databases_list_by_elastic_pool

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/elasticPools/{elastic_pool_name}/databases'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', server_name='server_name_example', elastic_pool_name='elastic_pool_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_databases_list_by_recommended_elastic_pool(client):
    """Test case for databases_list_by_recommended_elastic_pool

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/recommendedElasticPools/{recommended_elastic_pool_name}/databases'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', server_name='server_name_example', recommended_elastic_pool_name='recommended_elastic_pool_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_databases_list_by_server(client):
    """Test case for databases_list_by_server

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$expand', 'expand_example'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/databases'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', server_name='server_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_databases_update(client):
    """Test case for databases_update

    
    """
    parameters = {"properties":{"elasticPoolName":"elasticPoolName","sourceDatabaseDeletionDate":"2000-01-23T04:56:07.000+00:00","edition":"Web","failoverGroupId":"failoverGroupId","currentServiceObjectiveId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","recommendedIndex":[{"properties":{"reportedImpact":[{"unit":"unit","changeValueRelative":1.4658129805029452,"name":"name","changeValueAbsolute":6.027456183070403},{"unit":"unit","changeValueRelative":1.4658129805029452,"name":"name","changeValueAbsolute":6.027456183070403}],"schema":"schema","estimatedImpact":[{"unit":"unit","changeValueRelative":1.4658129805029452,"name":"name","changeValueAbsolute":6.027456183070403},{"unit":"unit","changeValueRelative":1.4658129805029452,"name":"name","changeValueAbsolute":6.027456183070403}],"indexType":"CLUSTERED","columns":["columns","columns"],"created":"2000-01-23T04:56:07.000+00:00","includedColumns":["includedColumns","includedColumns"],"action":"Create","indexScript":"indexScript","lastModified":"2000-01-23T04:56:07.000+00:00","state":"Active","table":"table"}},{"properties":{"reportedImpact":[{"unit":"unit","changeValueRelative":1.4658129805029452,"name":"name","changeValueAbsolute":6.027456183070403},{"unit":"unit","changeValueRelative":1.4658129805029452,"name":"name","changeValueAbsolute":6.027456183070403}],"schema":"schema","estimatedImpact":[{"unit":"unit","changeValueRelative":1.4658129805029452,"name":"name","changeValueAbsolute":6.027456183070403},{"unit":"unit","changeValueRelative":1.4658129805029452,"name":"name","changeValueAbsolute":6.027456183070403}],"indexType":"CLUSTERED","columns":["columns","columns"],"created":"2000-01-23T04:56:07.000+00:00","includedColumns":["includedColumns","includedColumns"],"action":"Create","indexScript":"indexScript","lastModified":"2000-01-23T04:56:07.000+00:00","state":"Active","table":"table"}}],"restorePointInTime":"2000-01-23T04:56:07.000+00:00","sampleName":"AdventureWorksLT","maxSizeBytes":"maxSizeBytes","defaultSecondaryLocation":"defaultSecondaryLocation","collation":"collation","databaseId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","earliestRestoreDate":"2000-01-23T04:56:07.000+00:00","requestedServiceObjectiveName":"System","transparentDataEncryption":[{"location":"location","properties":{"status":"Enabled"}},{"location":"location","properties":{"status":"Enabled"}}],"serviceTierAdvisors":[{"properties":{"currentServiceLevelObjective":"currentServiceLevelObjective","databaseSizeBasedRecommendationServiceLevelObjective":"databaseSizeBasedRecommendationServiceLevelObjective","overallRecommendationServiceLevelObjective":"overallRecommendationServiceLevelObjective","avgDtu":5.637376656633329,"confidence":2.3021358869347655,"overallRecommendationServiceLevelObjectiveId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","minDtu":3.616076749251911,"disasterPlanBasedRecommendationServiceLevelObjectiveId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","usageBasedRecommendationServiceLevelObjectiveId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","maxDtu":7.061401241503109,"serviceLevelObjectiveUsageMetrics":[{"serviceLevelObjectiveId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","serviceLevelObjective":"System","inRangeTimeRatio":2.027123023002322},{"serviceLevelObjectiveId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","serviceLevelObjective":"System","inRangeTimeRatio":2.027123023002322}],"observationPeriodEnd":"2000-01-23T04:56:07.000+00:00","activeTimeRatio":5.962133916683182,"databaseSizeBasedRecommendationServiceLevelObjectiveId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","currentServiceLevelObjectiveId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","disasterPlanBasedRecommendationServiceLevelObjective":"disasterPlanBasedRecommendationServiceLevelObjective","observationPeriodStart":"2000-01-23T04:56:07.000+00:00","maxSizeInGB":9.301444243932576,"usageBasedRecommendationServiceLevelObjective":"usageBasedRecommendationServiceLevelObjective"}},{"properties":{"currentServiceLevelObjective":"currentServiceLevelObjective","databaseSizeBasedRecommendationServiceLevelObjective":"databaseSizeBasedRecommendationServiceLevelObjective","overallRecommendationServiceLevelObjective":"overallRecommendationServiceLevelObjective","avgDtu":5.637376656633329,"confidence":2.3021358869347655,"overallRecommendationServiceLevelObjectiveId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","minDtu":3.616076749251911,"disasterPlanBasedRecommendationServiceLevelObjectiveId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","usageBasedRecommendationServiceLevelObjectiveId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","maxDtu":7.061401241503109,"serviceLevelObjectiveUsageMetrics":[{"serviceLevelObjectiveId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","serviceLevelObjective":"System","inRangeTimeRatio":2.027123023002322},{"serviceLevelObjectiveId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","serviceLevelObjective":"System","inRangeTimeRatio":2.027123023002322}],"observationPeriodEnd":"2000-01-23T04:56:07.000+00:00","activeTimeRatio":5.962133916683182,"databaseSizeBasedRecommendationServiceLevelObjectiveId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","currentServiceLevelObjectiveId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","disasterPlanBasedRecommendationServiceLevelObjective":"disasterPlanBasedRecommendationServiceLevelObjective","observationPeriodStart":"2000-01-23T04:56:07.000+00:00","maxSizeInGB":9.301444243932576,"usageBasedRecommendationServiceLevelObjective":"usageBasedRecommendationServiceLevelObjective"}}],"readScale":"Enabled","createMode":"Copy","zoneRedundant":True,"creationDate":"2000-01-23T04:56:07.000+00:00","serviceLevelObjective":"System","sourceDatabaseId":"sourceDatabaseId","recoveryServicesRecoveryPointResourceId":"recoveryServicesRecoveryPointResourceId","containmentState":0,"requestedServiceObjectiveId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","status":"status"},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/databases/{database_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', server_name='server_name_example', database_name='database_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

