# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_availability_zones_input import AddAvailabilityZonesInput
from openapi_server.models.add_availability_zones_output import AddAvailabilityZonesOutput
from openapi_server.models.add_tags_input import AddTagsInput
from openapi_server.models.apply_security_groups_to_load_balancer_input import ApplySecurityGroupsToLoadBalancerInput
from openapi_server.models.apply_security_groups_to_load_balancer_output import ApplySecurityGroupsToLoadBalancerOutput
from openapi_server.models.attach_load_balancer_to_subnets_input import AttachLoadBalancerToSubnetsInput
from openapi_server.models.attach_load_balancer_to_subnets_output import AttachLoadBalancerToSubnetsOutput
from openapi_server.models.configure_health_check_input import ConfigureHealthCheckInput
from openapi_server.models.configure_health_check_output import ConfigureHealthCheckOutput
from openapi_server.models.create_access_point_input import CreateAccessPointInput
from openapi_server.models.create_access_point_output import CreateAccessPointOutput
from openapi_server.models.create_app_cookie_stickiness_policy_input import CreateAppCookieStickinessPolicyInput
from openapi_server.models.create_lb_cookie_stickiness_policy_input import CreateLBCookieStickinessPolicyInput
from openapi_server.models.create_load_balancer_listener_input import CreateLoadBalancerListenerInput
from openapi_server.models.create_load_balancer_policy_input import CreateLoadBalancerPolicyInput
from openapi_server.models.delete_access_point_input import DeleteAccessPointInput
from openapi_server.models.delete_load_balancer_listener_input import DeleteLoadBalancerListenerInput
from openapi_server.models.delete_load_balancer_policy_input import DeleteLoadBalancerPolicyInput
from openapi_server.models.deregister_end_points_input import DeregisterEndPointsInput
from openapi_server.models.deregister_end_points_output import DeregisterEndPointsOutput
from openapi_server.models.describe_access_points_input import DescribeAccessPointsInput
from openapi_server.models.describe_access_points_output import DescribeAccessPointsOutput
from openapi_server.models.describe_account_limits_input import DescribeAccountLimitsInput
from openapi_server.models.describe_account_limits_output import DescribeAccountLimitsOutput
from openapi_server.models.describe_end_point_state_input import DescribeEndPointStateInput
from openapi_server.models.describe_end_point_state_output import DescribeEndPointStateOutput
from openapi_server.models.describe_load_balancer_attributes_input import DescribeLoadBalancerAttributesInput
from openapi_server.models.describe_load_balancer_attributes_output import DescribeLoadBalancerAttributesOutput
from openapi_server.models.describe_load_balancer_policies_input import DescribeLoadBalancerPoliciesInput
from openapi_server.models.describe_load_balancer_policies_output import DescribeLoadBalancerPoliciesOutput
from openapi_server.models.describe_load_balancer_policy_types_input import DescribeLoadBalancerPolicyTypesInput
from openapi_server.models.describe_load_balancer_policy_types_output import DescribeLoadBalancerPolicyTypesOutput
from openapi_server.models.describe_tags_input import DescribeTagsInput
from openapi_server.models.describe_tags_output import DescribeTagsOutput
from openapi_server.models.detach_load_balancer_from_subnets_input import DetachLoadBalancerFromSubnetsInput
from openapi_server.models.detach_load_balancer_from_subnets_output import DetachLoadBalancerFromSubnetsOutput
from openapi_server.models.get_configure_health_check_health_check_parameter import GETConfigureHealthCheckHealthCheckParameter
from openapi_server.models.get_modify_load_balancer_attributes_load_balancer_attributes_parameter import GETModifyLoadBalancerAttributesLoadBalancerAttributesParameter
from openapi_server.models.instance import Instance
from openapi_server.models.listener import Listener
from openapi_server.models.modify_load_balancer_attributes_input import ModifyLoadBalancerAttributesInput
from openapi_server.models.modify_load_balancer_attributes_output import ModifyLoadBalancerAttributesOutput
from openapi_server.models.policy_attribute import PolicyAttribute
from openapi_server.models.register_end_points_input import RegisterEndPointsInput
from openapi_server.models.register_end_points_output import RegisterEndPointsOutput
from openapi_server.models.remove_availability_zones_input import RemoveAvailabilityZonesInput
from openapi_server.models.remove_availability_zones_output import RemoveAvailabilityZonesOutput
from openapi_server.models.remove_tags_input import RemoveTagsInput
from openapi_server.models.set_load_balancer_listener_ssl_certificate_input import SetLoadBalancerListenerSSLCertificateInput
from openapi_server.models.set_load_balancer_policies_for_backend_server_input import SetLoadBalancerPoliciesForBackendServerInput
from openapi_server.models.set_load_balancer_policies_of_listener_input import SetLoadBalancerPoliciesOfListenerInput
from openapi_server.models.tag import Tag
from openapi_server.models.tag_key_only import TagKeyOnly


pytestmark = pytest.mark.asyncio

async def test_g_et_add_tags(client):
    """Test case for g_et_add_tags

    
    """
    params = [('LoadBalancerNames', ['load_balancer_names_example']),
                    ('Tags', [openapi_server.Tag()]),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
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
        path='/#Action=AddTags',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_apply_security_groups_to_load_balancer(client):
    """Test case for g_et_apply_security_groups_to_load_balancer

    
    """
    params = [('LoadBalancerName', 'load_balancer_name_example'),
                    ('SecurityGroups', ['security_groups_example']),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
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
        path='/#Action=ApplySecurityGroupsToLoadBalancer',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_attach_load_balancer_to_subnets(client):
    """Test case for g_et_attach_load_balancer_to_subnets

    
    """
    params = [('LoadBalancerName', 'load_balancer_name_example'),
                    ('Subnets', ['subnets_example']),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
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
        path='/#Action=AttachLoadBalancerToSubnets',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_configure_health_check(client):
    """Test case for g_et_configure_health_check

    
    """
    params = [('LoadBalancerName', 'load_balancer_name_example'),
                    ('HealthCheck', openapi_server.GETConfigureHealthCheckHealthCheckParameter()),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
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
        path='/#Action=ConfigureHealthCheck',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_create_app_cookie_stickiness_policy(client):
    """Test case for g_et_create_app_cookie_stickiness_policy

    
    """
    params = [('LoadBalancerName', 'load_balancer_name_example'),
                    ('PolicyName', 'policy_name_example'),
                    ('CookieName', 'cookie_name_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
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
        path='/#Action=CreateAppCookieStickinessPolicy',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_create_lb_cookie_stickiness_policy(client):
    """Test case for g_et_create_lb_cookie_stickiness_policy

    
    """
    params = [('LoadBalancerName', 'load_balancer_name_example'),
                    ('PolicyName', 'policy_name_example'),
                    ('CookieExpirationPeriod', 56),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
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
        path='/#Action=CreateLBCookieStickinessPolicy',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_create_load_balancer(client):
    """Test case for g_et_create_load_balancer

    
    """
    params = [('LoadBalancerName', 'load_balancer_name_example'),
                    ('Listeners', [openapi_server.Listener()]),
                    ('AvailabilityZones', ['availability_zones_example']),
                    ('Subnets', ['subnets_example']),
                    ('SecurityGroups', ['security_groups_example']),
                    ('Scheme', 'scheme_example'),
                    ('Tags', [openapi_server.Tag()]),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
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
        path='/#Action=CreateLoadBalancer',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_create_load_balancer_listeners(client):
    """Test case for g_et_create_load_balancer_listeners

    
    """
    params = [('LoadBalancerName', 'load_balancer_name_example'),
                    ('Listeners', [openapi_server.Listener()]),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
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
        path='/#Action=CreateLoadBalancerListeners',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_create_load_balancer_policy(client):
    """Test case for g_et_create_load_balancer_policy

    
    """
    params = [('LoadBalancerName', 'load_balancer_name_example'),
                    ('PolicyName', 'policy_name_example'),
                    ('PolicyTypeName', 'policy_type_name_example'),
                    ('PolicyAttributes', [openapi_server.PolicyAttribute()]),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
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
        path='/#Action=CreateLoadBalancerPolicy',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_delete_load_balancer(client):
    """Test case for g_et_delete_load_balancer

    
    """
    params = [('LoadBalancerName', 'load_balancer_name_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
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
        path='/#Action=DeleteLoadBalancer',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_delete_load_balancer_listeners(client):
    """Test case for g_et_delete_load_balancer_listeners

    
    """
    params = [('LoadBalancerName', 'load_balancer_name_example'),
                    ('LoadBalancerPorts', [56]),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
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
        path='/#Action=DeleteLoadBalancerListeners',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_delete_load_balancer_policy(client):
    """Test case for g_et_delete_load_balancer_policy

    
    """
    params = [('LoadBalancerName', 'load_balancer_name_example'),
                    ('PolicyName', 'policy_name_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
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
        path='/#Action=DeleteLoadBalancerPolicy',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_deregister_instances_from_load_balancer(client):
    """Test case for g_et_deregister_instances_from_load_balancer

    
    """
    params = [('LoadBalancerName', 'load_balancer_name_example'),
                    ('Instances', [openapi_server.Instance()]),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
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
        path='/#Action=DeregisterInstancesFromLoadBalancer',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_describe_account_limits(client):
    """Test case for g_et_describe_account_limits

    
    """
    params = [('Marker', 'marker_example'),
                    ('PageSize', 56),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
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
        path='/#Action=DescribeAccountLimits',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_describe_instance_health(client):
    """Test case for g_et_describe_instance_health

    
    """
    params = [('LoadBalancerName', 'load_balancer_name_example'),
                    ('Instances', [openapi_server.Instance()]),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
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
        path='/#Action=DescribeInstanceHealth',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_describe_load_balancer_attributes(client):
    """Test case for g_et_describe_load_balancer_attributes

    
    """
    params = [('LoadBalancerName', 'load_balancer_name_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
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
        path='/#Action=DescribeLoadBalancerAttributes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_describe_load_balancer_policies(client):
    """Test case for g_et_describe_load_balancer_policies

    
    """
    params = [('LoadBalancerName', 'load_balancer_name_example'),
                    ('PolicyNames', ['policy_names_example']),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
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
        path='/#Action=DescribeLoadBalancerPolicies',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_describe_load_balancer_policy_types(client):
    """Test case for g_et_describe_load_balancer_policy_types

    
    """
    params = [('PolicyTypeNames', ['policy_type_names_example']),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
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
        path='/#Action=DescribeLoadBalancerPolicyTypes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_describe_load_balancers(client):
    """Test case for g_et_describe_load_balancers

    
    """
    params = [('LoadBalancerNames', ['load_balancer_names_example']),
                    ('Marker', 'marker_example'),
                    ('PageSize', 56),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
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
        path='/#Action=DescribeLoadBalancers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_describe_tags(client):
    """Test case for g_et_describe_tags

    
    """
    params = [('LoadBalancerNames', ['load_balancer_names_example']),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
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
        path='/#Action=DescribeTags',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_detach_load_balancer_from_subnets(client):
    """Test case for g_et_detach_load_balancer_from_subnets

    
    """
    params = [('LoadBalancerName', 'load_balancer_name_example'),
                    ('Subnets', ['subnets_example']),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
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
        path='/#Action=DetachLoadBalancerFromSubnets',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_disable_availability_zones_for_load_balancer(client):
    """Test case for g_et_disable_availability_zones_for_load_balancer

    
    """
    params = [('LoadBalancerName', 'load_balancer_name_example'),
                    ('AvailabilityZones', ['availability_zones_example']),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
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
        path='/#Action=DisableAvailabilityZonesForLoadBalancer',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_enable_availability_zones_for_load_balancer(client):
    """Test case for g_et_enable_availability_zones_for_load_balancer

    
    """
    params = [('LoadBalancerName', 'load_balancer_name_example'),
                    ('AvailabilityZones', ['availability_zones_example']),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
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
        path='/#Action=EnableAvailabilityZonesForLoadBalancer',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_modify_load_balancer_attributes(client):
    """Test case for g_et_modify_load_balancer_attributes

    
    """
    params = [('LoadBalancerName', 'load_balancer_name_example'),
                    ('LoadBalancerAttributes', openapi_server.GETModifyLoadBalancerAttributesLoadBalancerAttributesParameter()),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
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
        path='/#Action=ModifyLoadBalancerAttributes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_register_instances_with_load_balancer(client):
    """Test case for g_et_register_instances_with_load_balancer

    
    """
    params = [('LoadBalancerName', 'load_balancer_name_example'),
                    ('Instances', [openapi_server.Instance()]),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
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
        path='/#Action=RegisterInstancesWithLoadBalancer',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_remove_tags(client):
    """Test case for g_et_remove_tags

    
    """
    params = [('LoadBalancerNames', ['load_balancer_names_example']),
                    ('Tags', [openapi_server.TagKeyOnly()]),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
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
        path='/#Action=RemoveTags',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_set_load_balancer_listener_ssl_certificate(client):
    """Test case for g_et_set_load_balancer_listener_ssl_certificate

    
    """
    params = [('LoadBalancerName', 'load_balancer_name_example'),
                    ('LoadBalancerPort', 56),
                    ('SSLCertificateId', 'ssl_certificate_id_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
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
        path='/#Action=SetLoadBalancerListenerSSLCertificate',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_set_load_balancer_policies_for_backend_server(client):
    """Test case for g_et_set_load_balancer_policies_for_backend_server

    
    """
    params = [('LoadBalancerName', 'load_balancer_name_example'),
                    ('InstancePort', 56),
                    ('PolicyNames', ['policy_names_example']),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
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
        path='/#Action=SetLoadBalancerPoliciesForBackendServer',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_set_load_balancer_policies_of_listener(client):
    """Test case for g_et_set_load_balancer_policies_of_listener

    
    """
    params = [('LoadBalancerName', 'load_balancer_name_example'),
                    ('LoadBalancerPort', 56),
                    ('PolicyNames', ['policy_names_example']),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
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
        path='/#Action=SetLoadBalancerPoliciesOfListener',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_add_tags(client):
    """Test case for p_ost_add_tags

    
    """
    body = openapi_server.AddTagsInput()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
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
        path='/#Action=AddTags',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_apply_security_groups_to_load_balancer(client):
    """Test case for p_ost_apply_security_groups_to_load_balancer

    
    """
    body = openapi_server.ApplySecurityGroupsToLoadBalancerInput()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
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
        path='/#Action=ApplySecurityGroupsToLoadBalancer',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_attach_load_balancer_to_subnets(client):
    """Test case for p_ost_attach_load_balancer_to_subnets

    
    """
    body = openapi_server.AttachLoadBalancerToSubnetsInput()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
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
        path='/#Action=AttachLoadBalancerToSubnets',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_configure_health_check(client):
    """Test case for p_ost_configure_health_check

    
    """
    body = openapi_server.ConfigureHealthCheckInput()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
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
        path='/#Action=ConfigureHealthCheck',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_create_app_cookie_stickiness_policy(client):
    """Test case for p_ost_create_app_cookie_stickiness_policy

    
    """
    body = openapi_server.CreateAppCookieStickinessPolicyInput()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
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
        path='/#Action=CreateAppCookieStickinessPolicy',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_create_lb_cookie_stickiness_policy(client):
    """Test case for p_ost_create_lb_cookie_stickiness_policy

    
    """
    body = openapi_server.CreateLBCookieStickinessPolicyInput()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
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
        path='/#Action=CreateLBCookieStickinessPolicy',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_create_load_balancer(client):
    """Test case for p_ost_create_load_balancer

    
    """
    body = openapi_server.CreateAccessPointInput()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
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
        path='/#Action=CreateLoadBalancer',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_create_load_balancer_listeners(client):
    """Test case for p_ost_create_load_balancer_listeners

    
    """
    body = openapi_server.CreateLoadBalancerListenerInput()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
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
        path='/#Action=CreateLoadBalancerListeners',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_create_load_balancer_policy(client):
    """Test case for p_ost_create_load_balancer_policy

    
    """
    body = openapi_server.CreateLoadBalancerPolicyInput()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
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
        path='/#Action=CreateLoadBalancerPolicy',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_delete_load_balancer(client):
    """Test case for p_ost_delete_load_balancer

    
    """
    body = openapi_server.DeleteAccessPointInput()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
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
        path='/#Action=DeleteLoadBalancer',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_delete_load_balancer_listeners(client):
    """Test case for p_ost_delete_load_balancer_listeners

    
    """
    body = openapi_server.DeleteLoadBalancerListenerInput()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
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
        path='/#Action=DeleteLoadBalancerListeners',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_delete_load_balancer_policy(client):
    """Test case for p_ost_delete_load_balancer_policy

    
    """
    body = openapi_server.DeleteLoadBalancerPolicyInput()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
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
        path='/#Action=DeleteLoadBalancerPolicy',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_deregister_instances_from_load_balancer(client):
    """Test case for p_ost_deregister_instances_from_load_balancer

    
    """
    body = openapi_server.DeregisterEndPointsInput()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
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
        path='/#Action=DeregisterInstancesFromLoadBalancer',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_describe_account_limits(client):
    """Test case for p_ost_describe_account_limits

    
    """
    body = openapi_server.DescribeAccountLimitsInput()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
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
        path='/#Action=DescribeAccountLimits',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_describe_instance_health(client):
    """Test case for p_ost_describe_instance_health

    
    """
    body = openapi_server.DescribeEndPointStateInput()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
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
        path='/#Action=DescribeInstanceHealth',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_describe_load_balancer_attributes(client):
    """Test case for p_ost_describe_load_balancer_attributes

    
    """
    body = openapi_server.DescribeLoadBalancerAttributesInput()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
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
        path='/#Action=DescribeLoadBalancerAttributes',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_describe_load_balancer_policies(client):
    """Test case for p_ost_describe_load_balancer_policies

    
    """
    body = openapi_server.DescribeLoadBalancerPoliciesInput()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
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
        path='/#Action=DescribeLoadBalancerPolicies',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_describe_load_balancer_policy_types(client):
    """Test case for p_ost_describe_load_balancer_policy_types

    
    """
    body = openapi_server.DescribeLoadBalancerPolicyTypesInput()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
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
        path='/#Action=DescribeLoadBalancerPolicyTypes',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_describe_load_balancers(client):
    """Test case for p_ost_describe_load_balancers

    
    """
    body = openapi_server.DescribeAccessPointsInput()
    params = [('Marker', 'marker_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
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
        path='/#Action=DescribeLoadBalancers',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_describe_tags(client):
    """Test case for p_ost_describe_tags

    
    """
    body = openapi_server.DescribeTagsInput()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
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
        path='/#Action=DescribeTags',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_detach_load_balancer_from_subnets(client):
    """Test case for p_ost_detach_load_balancer_from_subnets

    
    """
    body = openapi_server.DetachLoadBalancerFromSubnetsInput()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
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
        path='/#Action=DetachLoadBalancerFromSubnets',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_disable_availability_zones_for_load_balancer(client):
    """Test case for p_ost_disable_availability_zones_for_load_balancer

    
    """
    body = openapi_server.RemoveAvailabilityZonesInput()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
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
        path='/#Action=DisableAvailabilityZonesForLoadBalancer',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_enable_availability_zones_for_load_balancer(client):
    """Test case for p_ost_enable_availability_zones_for_load_balancer

    
    """
    body = openapi_server.AddAvailabilityZonesInput()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
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
        path='/#Action=EnableAvailabilityZonesForLoadBalancer',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_modify_load_balancer_attributes(client):
    """Test case for p_ost_modify_load_balancer_attributes

    
    """
    body = openapi_server.ModifyLoadBalancerAttributesInput()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
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
        path='/#Action=ModifyLoadBalancerAttributes',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_register_instances_with_load_balancer(client):
    """Test case for p_ost_register_instances_with_load_balancer

    
    """
    body = openapi_server.RegisterEndPointsInput()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
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
        path='/#Action=RegisterInstancesWithLoadBalancer',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_remove_tags(client):
    """Test case for p_ost_remove_tags

    
    """
    body = openapi_server.RemoveTagsInput()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
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
        path='/#Action=RemoveTags',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_set_load_balancer_listener_ssl_certificate(client):
    """Test case for p_ost_set_load_balancer_listener_ssl_certificate

    
    """
    body = openapi_server.SetLoadBalancerListenerSSLCertificateInput()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
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
        path='/#Action=SetLoadBalancerListenerSSLCertificate',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_set_load_balancer_policies_for_backend_server(client):
    """Test case for p_ost_set_load_balancer_policies_for_backend_server

    
    """
    body = openapi_server.SetLoadBalancerPoliciesForBackendServerInput()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
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
        path='/#Action=SetLoadBalancerPoliciesForBackendServer',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_set_load_balancer_policies_of_listener(client):
    """Test case for p_ost_set_load_balancer_policies_of_listener

    
    """
    body = openapi_server.SetLoadBalancerPoliciesOfListenerInput()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
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
        path='/#Action=SetLoadBalancerPoliciesOfListener',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

