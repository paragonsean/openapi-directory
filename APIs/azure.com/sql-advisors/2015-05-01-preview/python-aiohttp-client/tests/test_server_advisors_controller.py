# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.advisor import Advisor


pytestmark = pytest.mark.asyncio

async def test_server_advisors_get(client):
    """Test case for server_advisors_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/advisors/{advisor_name}'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', advisor_name='advisor_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_server_advisors_list_by_server(client):
    """Test case for server_advisors_list_by_server

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/advisors'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_server_advisors_update(client):
    """Test case for server_advisors_update

    
    """
    parameters = {"kind":"kind","location":"location","properties":{"autoExecuteStatus":"Enabled","autoExecuteStatusInheritedFrom":"Default","recommendedActions":[{"kind":"kind","location":"location","properties":{"validSince":"2000-01-23T04:56:07.000+00:00","revertActionInitiatedTime":"2000-01-23T04:56:07.000+00:00","lastRefresh":"2000-01-23T04:56:07.000+00:00","linkedObjects":["linkedObjects","linkedObjects"],"observedImpact":[{"unit":"unit","absoluteValue":0.8008281904610115,"changeValueRelative":1.4658129805029452,"changeValueAbsolute":6.027456183070403,"dimensionName":"dimensionName"},{"unit":"unit","absoluteValue":0.8008281904610115,"changeValueRelative":1.4658129805029452,"changeValueAbsolute":6.027456183070403,"dimensionName":"dimensionName"}],"isArchivedAction":True,"recommendationReason":"recommendationReason","executeActionInitiatedBy":"User","revertActionInitiatedBy":"User","executeActionInitiatedTime":"2000-01-23T04:56:07.000+00:00","isExecutableAction":True,"score":5,"timeSeries":[{"timeGrain":"timeGrain","unit":"unit","metricName":"metricName","startTime":"2000-01-23T04:56:07.000+00:00","value":5.637376656633329},{"timeGrain":"timeGrain","unit":"unit","metricName":"metricName","startTime":"2000-01-23T04:56:07.000+00:00","value":5.637376656633329}],"estimatedImpact":[{"unit":"unit","absoluteValue":0.8008281904610115,"changeValueRelative":1.4658129805029452,"changeValueAbsolute":6.027456183070403,"dimensionName":"dimensionName"},{"unit":"unit","absoluteValue":0.8008281904610115,"changeValueRelative":1.4658129805029452,"changeValueAbsolute":6.027456183070403,"dimensionName":"dimensionName"}],"executeActionDuration":"executeActionDuration","implementationDetails":{"method":"TSql","script":"script"},"revertActionStartTime":"2000-01-23T04:56:07.000+00:00","isRevertableAction":True,"details":{"key":"{}"},"revertActionDuration":"revertActionDuration","state":{"actionInitiatedBy":"User","lastModified":"2000-01-23T04:56:07.000+00:00","currentValue":"Active"},"errorDetails":{"isRetryable":"Yes","errorCode":"errorCode"},"executeActionStartTime":"2000-01-23T04:56:07.000+00:00"}},{"kind":"kind","location":"location","properties":{"validSince":"2000-01-23T04:56:07.000+00:00","revertActionInitiatedTime":"2000-01-23T04:56:07.000+00:00","lastRefresh":"2000-01-23T04:56:07.000+00:00","linkedObjects":["linkedObjects","linkedObjects"],"observedImpact":[{"unit":"unit","absoluteValue":0.8008281904610115,"changeValueRelative":1.4658129805029452,"changeValueAbsolute":6.027456183070403,"dimensionName":"dimensionName"},{"unit":"unit","absoluteValue":0.8008281904610115,"changeValueRelative":1.4658129805029452,"changeValueAbsolute":6.027456183070403,"dimensionName":"dimensionName"}],"isArchivedAction":True,"recommendationReason":"recommendationReason","executeActionInitiatedBy":"User","revertActionInitiatedBy":"User","executeActionInitiatedTime":"2000-01-23T04:56:07.000+00:00","isExecutableAction":True,"score":5,"timeSeries":[{"timeGrain":"timeGrain","unit":"unit","metricName":"metricName","startTime":"2000-01-23T04:56:07.000+00:00","value":5.637376656633329},{"timeGrain":"timeGrain","unit":"unit","metricName":"metricName","startTime":"2000-01-23T04:56:07.000+00:00","value":5.637376656633329}],"estimatedImpact":[{"unit":"unit","absoluteValue":0.8008281904610115,"changeValueRelative":1.4658129805029452,"changeValueAbsolute":6.027456183070403,"dimensionName":"dimensionName"},{"unit":"unit","absoluteValue":0.8008281904610115,"changeValueRelative":1.4658129805029452,"changeValueAbsolute":6.027456183070403,"dimensionName":"dimensionName"}],"executeActionDuration":"executeActionDuration","implementationDetails":{"method":"TSql","script":"script"},"revertActionStartTime":"2000-01-23T04:56:07.000+00:00","isRevertableAction":True,"details":{"key":"{}"},"revertActionDuration":"revertActionDuration","state":{"actionInitiatedBy":"User","lastModified":"2000-01-23T04:56:07.000+00:00","currentValue":"Active"},"errorDetails":{"isRetryable":"Yes","errorCode":"errorCode"},"executeActionStartTime":"2000-01-23T04:56:07.000+00:00"}}],"lastChecked":"2000-01-23T04:56:07.000+00:00","advisorStatus":"GA","recommendationsStatus":"recommendationsStatus"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/advisors/{advisor_name}'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', advisor_name='advisor_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

