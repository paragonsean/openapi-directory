# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.async_request_status import AsyncRequestStatus
from openapi_server.models.available_version_info import AvailableVersionInfo
from openapi_server.models.boolean_response import BooleanResponse
from openapi_server.models.cluster_api_version import ClusterApiVersion
from openapi_server.models.cluster_certificate import ClusterCertificate
from openapi_server.models.cluster_info import ClusterInfo
from openapi_server.models.cluster_update import ClusterUpdate
from openapi_server.models.cluster_version import ClusterVersion
from openapi_server.models.community_user_credentials import CommunityUserCredentials
from openapi_server.models.cors_configuration import CorsConfiguration
from openapi_server.models.cors_configuration_patch import CorsConfigurationPatch
from openapi_server.models.encryption_status import EncryptionStatus
from openapi_server.models.event_notification import EventNotification
from openapi_server.models.fips_status import FipsStatus
from openapi_server.models.fips_status_patch import FipsStatusPatch
from openapi_server.models.kmip_client_configuration import KmipClientConfiguration
from openapi_server.models.kmip_client_detail import KmipClientDetail
from openapi_server.models.kmip_server_configuration import KmipServerConfiguration
from openapi_server.models.kmip_server_detail import KmipServerDetail
from openapi_server.models.manual_discovery_node_info import ManualDiscoveryNodeInfo
from openapi_server.models.manual_discovery_node_ipv4_info import ManualDiscoveryNodeIpv4Info
from openapi_server.models.node_hostname_info import NodeHostnameInfo
from openapi_server.models.node_hostname_info_list_response import NodeHostnameInfoListResponse
from openapi_server.models.node_id import NodeId
from openapi_server.models.password_requirements_patch_request import PasswordRequirementsPatchRequest
from openapi_server.models.password_requirements_summary import PasswordRequirementsSummary
from openapi_server.models.precheck_status_response import PrecheckStatusResponse
from openapi_server.models.rubrik_mib_file_download_link import RubrikMibFileDownloadLink
from openapi_server.models.stage_cdm_software_info import StageCdmSoftwareInfo
from openapi_server.models.syslog_export_rule_full import SyslogExportRuleFull
from openapi_server.models.syslog_export_rule_partial import SyslogExportRulePartial
from openapi_server.models.syslog_export_rule_summary import SyslogExportRuleSummary
from openapi_server.models.syslog_export_rule_summary_list_response import SyslogExportRuleSummaryListResponse
from openapi_server.models.syslog_msg_mib_file_download_link import SyslogMsgMibFileDownloadLink
from openapi_server.models.syslog_server_test_result import SyslogServerTestResult
from openapi_server.models.syslog_tc_mib_file_download_link import SyslogTcMibFileDownloadLink
from openapi_server.models.totp_global_setting import TotpGlobalSetting
from openapi_server.models.totp_global_setting_update import TotpGlobalSettingUpdate
from openapi_server.models.truststore_payload import TruststorePayload
from openapi_server.models.truststore_summary_list_response import TruststoreSummaryListResponse
from openapi_server.models.web_server_certificate_payload import WebServerCertificatePayload
from openapi_server.models.web_server_certificate_summary import WebServerCertificateSummary


pytestmark = pytest.mark.asyncio

async def test_add_kmip_server(client):
    """Test case for add_kmip_server

    Add a KMIP server
    """
    body = {"serverAddress":"serverAddress","serverPort":0,"serverCertificateId":"serverCertificateId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/cluster/{id}/security/kmip/server'.format(id='me'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_syslog_export_rule(client):
    """Test case for add_syslog_export_rule

    Add a new syslog export rule
    """
    body = {"severity":"Emergency","enableTls":True,"hostname":"hostname","protocol":"TCP","port":0,"certificateId":"certificateId","facility":"Kernel"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/syslog/export',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_available_version(client):
    """Test case for available_version

    Retrieve CDM versions available for upgrade
    """
    params = [('filter_version', 'filter_version_example'),
                    ('fetch_links', False),
                    ('source_version', 'source_version_example'),
                    ('ignore_local', False),
                    ('ignore_remote', False),
                    ('ignore_downloading', True),
                    ('download_job_instance_id', 'download_job_instance_id_example'),
                    ('filter_upgradable', True),
                    ('show_all', False)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/cluster/{id}/upgrade/available_version'.format(id='me'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_change_cluster_node_hostnames(client):
    """Test case for change_cluster_node_hostnames

    Change hostname for nodes in a Rubrik cluster
    """
    body = {"hostname":"hostname","id":"id"}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/cluster/{id}/node_hostname'.format(id='me'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_kmip_server(client):
    """Test case for delete_kmip_server

    Remove the specified KMIP server
    """
    params = [('server_address', 'server_address_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/cluster/{id}/security/kmip/server'.format(id='me'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_syslog_export_rule(client):
    """Test case for delete_syslog_export_rule

    Delete the specified syslog export rule
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/syslog/export/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_async_request_status_for_upgrade(client):
    """Test case for get_async_request_status_for_upgrade

    Get asynchronous request details
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/cluster/{id}/upgrade/request/{request_id}'.format(id='me', request_id='request_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_cluster_api_version(client):
    """Test case for get_cluster_api_version

    Get cluster REST API version
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/cluster/{id}/api_version'.format(id='me'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_cluster_certificate(client):
    """Test case for get_cluster_certificate

    Get the cluster certificate
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/cluster/{id}/certificate'.format(id='me'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_cluster_node_hostnames(client):
    """Test case for get_cluster_node_hostnames

    Get the node ID to hostname mapping for all the nodes in a Rubrik cluster 
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/cluster/{id}/node_hostname'.format(id='me'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_cluster_node_ids(client):
    """Test case for get_cluster_node_ids

    Get the name of the nodes in the cluster
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/cluster/{id}/node_id'.format(id='me'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_cluster_version(client):
    """Test case for get_cluster_version

    Get cluster software version
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/cluster/{id}/version'.format(id='me'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_cors_configuration(client):
    """Test case for get_cors_configuration

    Get CORS configuration
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/cluster/{id}/security/cors'.format(id='me'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_encryption_status(client):
    """Test case for get_encryption_status

    Get encryption at rest status
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/cluster/{id}/security/encryption'.format(id='me'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_fips(client):
    """Test case for get_fips

    Get FIPS enablement status
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/cluster/{id}/security/fips'.format(id='me'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_kmip_client(client):
    """Test case for get_kmip_client

    Get the KMIP client configuration
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/cluster/{id}/security/kmip/client'.format(id='me'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_kmip_server(client):
    """Test case for get_kmip_server

    Get KMIP server information
    """
    params = [('server_address', 'server_address_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/cluster/{id}/security/kmip/server'.format(id='me'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_periodic_upgrade_prechecks_status(client):
    """Test case for get_periodic_upgrade_prechecks_status

    Get the result of the latest run of the upgrade prechecks
    """
    params = [('fetch_next_run_info', False)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/cluster/{id}/upgrade/precheck_status'.format(id='me'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_public_cluster_info(client):
    """Test case for get_public_cluster_info

    Get cluster details
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/cluster/{id}'.format(id='me'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_rubrik_snmp_mib_download_link(client):
    """Test case for get_rubrik_snmp_mib_download_link

    Get the link for Rubrik SNMP MIB file
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/cluster/{id}/snmp_mib_link'.format(id='me'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_syslog_export_rule(client):
    """Test case for get_syslog_export_rule

    Get the specified syslog export rule
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/syslog/export/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_syslog_export_rules(client):
    """Test case for get_syslog_export_rules

    Get the configured syslog export rules
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/syslog/export',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_syslog_msg_snmp_mib_download_link(client):
    """Test case for get_syslog_msg_snmp_mib_download_link

    Get the link for SYSLOG-MSG-MIB file
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/cluster/{id}/syslog_msg_mib_link'.format(id='me'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_syslog_tc_snmp_mib_download_link(client):
    """Test case for get_syslog_tc_snmp_mib_download_link

    Get the link for SYSLOG-TC-MIB file
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/cluster/{id}/syslog_tc_mib_link'.format(id='me'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_totp_global_setting(client):
    """Test case for get_totp_global_setting

    Get global TOTP setting
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/cluster/{id}/security/totp/setting'.format(id='me'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_truststores(client):
    """Test case for get_truststores

    Get summary of all truststores
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/cluster/{id}/security/truststore'.format(id='me'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_web_signed_certificate(client):
    """Test case for get_web_signed_certificate

    Get the signed certificate for Web server
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/cluster/{id}/security/web_signed_cert'.format(id='me'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_has_rubrik_support_portal_credentials(client):
    """Test case for has_rubrik_support_portal_credentials

    Check credentials to the Rubrik support portal
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/cluster/{id}/rubrik_support_portal_credentials'.format(id='me'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_manual_discover(client):
    """Test case for manual_discover

    Manually discover nodes
    """
    body = {"nodeInfo":[{"hostname":"hostname","ipv6":"ipv6"},{"hostname":"hostname","ipv6":"ipv6"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/cluster/{id}/manual_discover'.format(id='me'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_manual_discover_ipv4(client):
    """Test case for manual_discover_ipv4

    Manually discover nodes over IPv4 address
    """
    body = {"nodeInfo":[{"hostname":"hostname","ipv4":"ipv4"},{"hostname":"hostname","ipv4":"ipv4"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/cluster/{id}/manual_discover_ipv4'.format(id='me'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_monitor_events(client):
    """Test case for monitor_events

    Get event notifications
    """
    params = [('event_notification_query', ['event_notification_query_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/cluster/me/upgrade/monitor_events',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_password_requirements(client):
    """Test case for patch_password_requirements

    Set password requirements
    """
    body = {"clearApiTokens":True,"minUpperCase":5,"useZxcvbn":True,"minLength":0,"minLowerCase":6,"minNumerics":1,"blockPreviousPasswords":True,"clearWebSessions":True,"minSpecial":5}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/cluster/{id}/security/password_requirements'.format(id='me'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_password_requirements(client):
    """Test case for query_password_requirements

    Get password requirements
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/cluster/{id}/security/password_requirements'.format(id='me'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reset_web_signed_certificate(client):
    """Test case for reset_web_signed_certificate

    Reset the signed certificate for Web server
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/cluster/{id}/security/web_signed_cert'.format(id='me'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_run_periodic_upgrade_prechecks(client):
    """Test case for run_periodic_upgrade_prechecks

    Start an on demand run of the prechecks
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/cluster/{id}/upgrade/precheck_status'.format(id='me'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_kmip_client(client):
    """Test case for set_kmip_client

    Specify KMIP client credentials for nodes
    """
    body = {"password":"password","clientCertificateId":"clientCertificateId","username":"username"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/cluster/{id}/security/kmip/client'.format(id='me'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_truststore_certificate(client):
    """Test case for set_truststore_certificate

    Set certificates for one or more truststores
    """
    body = {"truststoreType":"System","certIds":["certIds","certIds"]}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/cluster/{id}/security/truststore'.format(id='me'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_web_signed_certificate(client):
    """Test case for set_web_signed_certificate

    Set a signed certificate for Web server
    """
    body = {"certificateId":"certificateId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/cluster/{id}/security/web_signed_cert'.format(id='me'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stage_cdm_software(client):
    """Test case for stage_cdm_software

    Stage software on CDM for upgrade
    """
    body = {"size":0,"md5sum":"md5sum","packageUrl":"packageUrl","version":"version","skipDownload":False}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/cluster/{id}/upgrade/stage_cdm_software'.format(id='me'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_syslog_export_rule(client):
    """Test case for test_syslog_export_rule

    Test the specified syslog export rule
    """
    body = {"severity":"Emergency","enableTls":True,"hostname":"hostname","protocol":"TCP","port":0,"certificateId":"certificateId","facility":"Kernel"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/syslog/export/test',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unset_truststore_certificate(client):
    """Test case for unset_truststore_certificate

    Remove certificate associated with specified truststore
    """
    params = [('truststores', ['truststores_example'])]
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/cluster/{id}/security/truststore'.format(id='me'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_cluster(client):
    """Test case for update_cluster

    Change Rubrik cluster properties
    """
    body = {"acceptedEulaVersion":"acceptedEulaVersion","timezone":{"timezone":"Africa/Johannesburg"},"name":"name","geolocation":{"address":"address"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/cluster/{id}'.format(id='me'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_cors_configuration(client):
    """Test case for update_cors_configuration

    Update CORS configuration
    """
    body = {"allowedOrigins":"allowedOrigins","isEnabled":True,"allowedHeaders":"allowedHeaders"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/cluster/{id}/security/cors'.format(id='me'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_fips(client):
    """Test case for update_fips

    Update FIPS enablement status
    """
    body = {"isEnabledInFlight":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/cluster/{id}/security/fips'.format(id='me'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_rubrik_support_portal_credentials(client):
    """Test case for update_rubrik_support_portal_credentials

    Update credentials to the Rubrik support portal
    """
    body = {"password":"password","username":"username"}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/cluster/{id}/rubrik_support_portal_credentials'.format(id='me'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_syslog_export_rule(client):
    """Test case for update_syslog_export_rule

    Update the specified syslog export rule
    """
    body = {"severity":"Emergency","enableTls":True,"hostname":"hostname","protocol":"TCP","port":0,"certificateId":"certificateId","facility":"Kernel"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/syslog/export/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_totp_global_setting(client):
    """Test case for update_totp_global_setting

    Update TOTP global setting
    """
    body = {"isEnforced":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/cluster/{id}/security/totp/setting'.format(id='me'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

