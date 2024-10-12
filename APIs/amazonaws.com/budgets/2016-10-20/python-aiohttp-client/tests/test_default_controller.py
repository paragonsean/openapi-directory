# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_budget_action_request import CreateBudgetActionRequest
from openapi_server.models.create_budget_action_response import CreateBudgetActionResponse
from openapi_server.models.create_budget_request import CreateBudgetRequest
from openapi_server.models.create_notification_request import CreateNotificationRequest
from openapi_server.models.create_subscriber_request import CreateSubscriberRequest
from openapi_server.models.delete_budget_action_request import DeleteBudgetActionRequest
from openapi_server.models.delete_budget_action_response import DeleteBudgetActionResponse
from openapi_server.models.delete_budget_request import DeleteBudgetRequest
from openapi_server.models.delete_notification_request import DeleteNotificationRequest
from openapi_server.models.delete_subscriber_request import DeleteSubscriberRequest
from openapi_server.models.describe_budget_action_histories_request import DescribeBudgetActionHistoriesRequest
from openapi_server.models.describe_budget_action_histories_response import DescribeBudgetActionHistoriesResponse
from openapi_server.models.describe_budget_action_request import DescribeBudgetActionRequest
from openapi_server.models.describe_budget_action_response import DescribeBudgetActionResponse
from openapi_server.models.describe_budget_actions_for_account_request import DescribeBudgetActionsForAccountRequest
from openapi_server.models.describe_budget_actions_for_account_response import DescribeBudgetActionsForAccountResponse
from openapi_server.models.describe_budget_actions_for_budget_request import DescribeBudgetActionsForBudgetRequest
from openapi_server.models.describe_budget_actions_for_budget_response import DescribeBudgetActionsForBudgetResponse
from openapi_server.models.describe_budget_notifications_for_account_request import DescribeBudgetNotificationsForAccountRequest
from openapi_server.models.describe_budget_notifications_for_account_response import DescribeBudgetNotificationsForAccountResponse
from openapi_server.models.describe_budget_performance_history_request import DescribeBudgetPerformanceHistoryRequest
from openapi_server.models.describe_budget_performance_history_response import DescribeBudgetPerformanceHistoryResponse
from openapi_server.models.describe_budget_request import DescribeBudgetRequest
from openapi_server.models.describe_budget_response import DescribeBudgetResponse
from openapi_server.models.describe_budgets_request import DescribeBudgetsRequest
from openapi_server.models.describe_budgets_response import DescribeBudgetsResponse
from openapi_server.models.describe_notifications_for_budget_request import DescribeNotificationsForBudgetRequest
from openapi_server.models.describe_notifications_for_budget_response import DescribeNotificationsForBudgetResponse
from openapi_server.models.describe_subscribers_for_notification_request import DescribeSubscribersForNotificationRequest
from openapi_server.models.describe_subscribers_for_notification_response import DescribeSubscribersForNotificationResponse
from openapi_server.models.execute_budget_action_request import ExecuteBudgetActionRequest
from openapi_server.models.execute_budget_action_response import ExecuteBudgetActionResponse
from openapi_server.models.update_budget_action_request import UpdateBudgetActionRequest
from openapi_server.models.update_budget_action_response import UpdateBudgetActionResponse
from openapi_server.models.update_budget_request import UpdateBudgetRequest
from openapi_server.models.update_notification_request import UpdateNotificationRequest
from openapi_server.models.update_subscriber_request import UpdateSubscriberRequest


pytestmark = pytest.mark.asyncio

async def test_create_budget(client):
    """Test case for create_budget

    
    """
    body = {"AccountId":"","NotificationsWithSubscribers":"","Budget":{"BudgetLimit":{"Amount":"","Unit":""},"TimePeriod":{"Start":"","End":""},"CalculatedSpend":{"ActualSpend":{"Amount":"","Unit":""},"ForecastedSpend":{"Amount":"","Unit":""}},"TimeUnit":"","LastUpdatedTime":"","AutoAdjustData":{"AutoAdjustType":"","HistoricalOptions":{"BudgetAdjustmentPeriod":"","LookBackAvailablePeriods":""},"LastAutoAdjustTime":""},"PlannedBudgetLimits":"","CostFilters":"","BudgetName":"","CostTypes":{"IncludeSupport":"","IncludeOtherSubscription":"","IncludeTax":"","IncludeSubscription":"","UseBlended":"","IncludeUpfront":"","IncludeDiscount":"","IncludeCredit":"","IncludeRecurring":"","UseAmortized":"","IncludeRefund":""},"BudgetType":""}}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSBudgetServiceGateway.CreateBudget',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_budget_action(client):
    """Test case for create_budget_action

    
    """
    body = {"ExecutionRoleArn":"","AccountId":"AccountId","ActionType":"","NotificationType":"ACTUAL","ActionThreshold":{"ActionThresholdValue":1.2012422856915173E12,"ActionThresholdType":"PERCENTAGE"},"Definition":{"SsmActionDefinition":{"Region":"","ActionSubType":"","InstanceIds":""},"IamActionDefinition":{"PolicyArn":"","Groups":"","Roles":"","Users":""},"ScpActionDefinition":{"TargetIds":"","PolicyId":""}},"ApprovalModel":"","Subscribers":[{"SubscriptionType":"","Address":""},{"SubscriptionType":"","Address":""},{"SubscriptionType":"","Address":""},{"SubscriptionType":"","Address":""},{"SubscriptionType":"","Address":""}],"BudgetName":"BudgetName"}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSBudgetServiceGateway.CreateBudgetAction',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_notification(client):
    """Test case for create_notification

    
    """
    body = {"AccountId":"","Subscribers":"","BudgetName":"","Notification":{"ComparisonOperator":"","NotificationType":"","Threshold":"","ThresholdType":"","NotificationState":""}}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSBudgetServiceGateway.CreateNotification',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_subscriber(client):
    """Test case for create_subscriber

    
    """
    body = {"AccountId":"","Subscriber":{"SubscriptionType":"","Address":""},"BudgetName":"","Notification":{"ComparisonOperator":"","NotificationType":"","Threshold":"","ThresholdType":"","NotificationState":""}}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSBudgetServiceGateway.CreateSubscriber',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_budget(client):
    """Test case for delete_budget

    
    """
    body = {"AccountId":"","BudgetName":""}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSBudgetServiceGateway.DeleteBudget',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_budget_action(client):
    """Test case for delete_budget_action

    
    """
    body = {"ActionId":"","AccountId":"AccountId","BudgetName":"BudgetName"}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSBudgetServiceGateway.DeleteBudgetAction',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_notification(client):
    """Test case for delete_notification

    
    """
    body = {"AccountId":"","BudgetName":"","Notification":{"ComparisonOperator":"","NotificationType":"","Threshold":"","ThresholdType":"","NotificationState":""}}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSBudgetServiceGateway.DeleteNotification',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_subscriber(client):
    """Test case for delete_subscriber

    
    """
    body = {"AccountId":"","Subscriber":{"SubscriptionType":"","Address":""},"BudgetName":"","Notification":{"ComparisonOperator":"","NotificationType":"","Threshold":"","ThresholdType":"","NotificationState":""}}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSBudgetServiceGateway.DeleteSubscriber',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_budget(client):
    """Test case for describe_budget

    
    """
    body = {"AccountId":"","BudgetName":""}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSBudgetServiceGateway.DescribeBudget',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_budget_action(client):
    """Test case for describe_budget_action

    
    """
    body = {"ActionId":"","AccountId":"AccountId","BudgetName":"BudgetName"}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSBudgetServiceGateway.DescribeBudgetAction',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_budget_action_histories(client):
    """Test case for describe_budget_action_histories

    
    """
    body = {"ActionId":"","AccountId":"AccountId","NextToken":"NextToken","TimePeriod":{"Start":"","End":""},"MaxResults":8,"BudgetName":"BudgetName"}
    params = [('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSBudgetServiceGateway.DescribeBudgetActionHistories',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_budget_actions_for_account(client):
    """Test case for describe_budget_actions_for_account

    
    """
    body = {"AccountId":"AccountId","NextToken":"NextToken","MaxResults":8}
    params = [('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSBudgetServiceGateway.DescribeBudgetActionsForAccount',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_budget_actions_for_budget(client):
    """Test case for describe_budget_actions_for_budget

    
    """
    body = {"AccountId":"AccountId","NextToken":"NextToken","MaxResults":8,"BudgetName":"BudgetName"}
    params = [('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSBudgetServiceGateway.DescribeBudgetActionsForBudget',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_budget_notifications_for_account(client):
    """Test case for describe_budget_notifications_for_account

    
    """
    body = {"AccountId":"AccountId","NextToken":"NextToken","MaxResults":""}
    params = [('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSBudgetServiceGateway.DescribeBudgetNotificationsForAccount',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_budget_performance_history(client):
    """Test case for describe_budget_performance_history

    
    """
    body = {"AccountId":"AccountId","NextToken":"NextToken","TimePeriod":{"Start":"","End":""},"MaxResults":8,"BudgetName":"BudgetName"}
    params = [('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSBudgetServiceGateway.DescribeBudgetPerformanceHistory',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_budgets(client):
    """Test case for describe_budgets

    
    """
    body = {"AccountId":"","NextToken":"","MaxResults":""}
    params = [('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSBudgetServiceGateway.DescribeBudgets',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_notifications_for_budget(client):
    """Test case for describe_notifications_for_budget

    
    """
    body = {"AccountId":"","NextToken":"","MaxResults":"","BudgetName":""}
    params = [('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSBudgetServiceGateway.DescribeNotificationsForBudget',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_subscribers_for_notification(client):
    """Test case for describe_subscribers_for_notification

    
    """
    body = {"AccountId":"","NextToken":"","MaxResults":"","BudgetName":"","Notification":{"ComparisonOperator":"","NotificationType":"","Threshold":"","ThresholdType":"","NotificationState":""}}
    params = [('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSBudgetServiceGateway.DescribeSubscribersForNotification',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_execute_budget_action(client):
    """Test case for execute_budget_action

    
    """
    body = {"ActionId":"","AccountId":"AccountId","ExecutionType":"","BudgetName":"BudgetName"}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSBudgetServiceGateway.ExecuteBudgetAction',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_budget(client):
    """Test case for update_budget

    
    """
    body = {"NewBudget":{"BudgetLimit":{"Amount":"","Unit":""},"TimePeriod":{"Start":"","End":""},"CalculatedSpend":{"ActualSpend":{"Amount":"","Unit":""},"ForecastedSpend":{"Amount":"","Unit":""}},"TimeUnit":"","LastUpdatedTime":"","AutoAdjustData":{"AutoAdjustType":"","HistoricalOptions":{"BudgetAdjustmentPeriod":"","LookBackAvailablePeriods":""},"LastAutoAdjustTime":""},"PlannedBudgetLimits":"","CostFilters":"","BudgetName":"","CostTypes":{"IncludeSupport":"","IncludeOtherSubscription":"","IncludeTax":"","IncludeSubscription":"","UseBlended":"","IncludeUpfront":"","IncludeDiscount":"","IncludeCredit":"","IncludeRecurring":"","UseAmortized":"","IncludeRefund":""},"BudgetType":""},"AccountId":""}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSBudgetServiceGateway.UpdateBudget',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_budget_action(client):
    """Test case for update_budget_action

    
    """
    body = {"ExecutionRoleArn":"","ActionId":"","AccountId":"AccountId","NotificationType":"ACTUAL","ActionThreshold":{"ActionThresholdValue":1.2012422856915173E12,"ActionThresholdType":"PERCENTAGE"},"Definition":{"SsmActionDefinition":{"Region":"","ActionSubType":"","InstanceIds":""},"IamActionDefinition":{"PolicyArn":"","Groups":"","Roles":"","Users":""},"ScpActionDefinition":{"TargetIds":"","PolicyId":""}},"ApprovalModel":"","Subscribers":[{"SubscriptionType":"","Address":""},{"SubscriptionType":"","Address":""},{"SubscriptionType":"","Address":""},{"SubscriptionType":"","Address":""},{"SubscriptionType":"","Address":""}],"BudgetName":"BudgetName"}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSBudgetServiceGateway.UpdateBudgetAction',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_notification(client):
    """Test case for update_notification

    
    """
    body = {"AccountId":"","NewNotification":{"ComparisonOperator":"","NotificationType":"","Threshold":"","ThresholdType":"","NotificationState":""},"OldNotification":{"ComparisonOperator":"","NotificationType":"","Threshold":"","ThresholdType":"","NotificationState":""},"BudgetName":""}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSBudgetServiceGateway.UpdateNotification',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_subscriber(client):
    """Test case for update_subscriber

    
    """
    body = {"AccountId":"","NewSubscriber":{"SubscriptionType":"","Address":""},"OldSubscriber":{"SubscriptionType":"","Address":""},"BudgetName":"","Notification":{"ComparisonOperator":"","NotificationType":"","Threshold":"","ThresholdType":"","NotificationState":""}}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSBudgetServiceGateway.UpdateSubscriber',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

