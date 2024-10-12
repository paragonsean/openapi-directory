# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.backup_item import BackupItem
from openapi_server.models.backup_item_collection import BackupItemCollection
from openapi_server.models.backup_request import BackupRequest
from openapi_server.models.connection_string_dictionary import ConnectionStringDictionary
from openapi_server.models.continuous_web_job import ContinuousWebJob
from openapi_server.models.continuous_web_job_collection import ContinuousWebJobCollection
from openapi_server.models.csm_publishing_profile_options import CsmPublishingProfileOptions
from openapi_server.models.csm_slot_entity import CsmSlotEntity
from openapi_server.models.custom_hostname_analysis_result import CustomHostnameAnalysisResult
from openapi_server.models.deployment import Deployment
from openapi_server.models.deployment_collection import DeploymentCollection
from openapi_server.models.function_envelope import FunctionEnvelope
from openapi_server.models.function_envelope_collection import FunctionEnvelopeCollection
from openapi_server.models.function_secrets import FunctionSecrets
from openapi_server.models.host_name_binding import HostNameBinding
from openapi_server.models.host_name_binding_collection import HostNameBindingCollection
from openapi_server.models.ms_deploy import MSDeploy
from openapi_server.models.ms_deploy_log import MSDeployLog
from openapi_server.models.ms_deploy_status import MSDeployStatus
from openapi_server.models.migrate_my_sql_request import MigrateMySqlRequest
from openapi_server.models.migrate_my_sql_status import MigrateMySqlStatus
from openapi_server.models.network_features import NetworkFeatures
from openapi_server.models.perf_mon_counter_collection import PerfMonCounterCollection
from openapi_server.models.premier_add_on import PremierAddOn
from openapi_server.models.process_info import ProcessInfo
from openapi_server.models.process_info_collection import ProcessInfoCollection
from openapi_server.models.process_module_info import ProcessModuleInfo
from openapi_server.models.process_module_info_collection import ProcessModuleInfoCollection
from openapi_server.models.process_thread_info import ProcessThreadInfo
from openapi_server.models.process_thread_info_collection import ProcessThreadInfoCollection
from openapi_server.models.public_certificate import PublicCertificate
from openapi_server.models.public_certificate_collection import PublicCertificateCollection
from openapi_server.models.relay_service_connection_entity import RelayServiceConnectionEntity
from openapi_server.models.restore_request import RestoreRequest
from openapi_server.models.restore_response import RestoreResponse
from openapi_server.models.site_auth_settings import SiteAuthSettings
from openapi_server.models.site_cloneability import SiteCloneability
from openapi_server.models.site_config_resource import SiteConfigResource
from openapi_server.models.site_config_resource_collection import SiteConfigResourceCollection
from openapi_server.models.site_configuration_snapshot_info_collection import SiteConfigurationSnapshotInfoCollection
from openapi_server.models.site_extension_info import SiteExtensionInfo
from openapi_server.models.site_extension_info_collection import SiteExtensionInfoCollection
from openapi_server.models.site_logs_config import SiteLogsConfig
from openapi_server.models.site_patch_resource import SitePatchResource
from openapi_server.models.site_php_error_log_flag import SitePhpErrorLogFlag
from openapi_server.models.site_source_control import SiteSourceControl
from openapi_server.models.slot_config_names_resource import SlotConfigNamesResource
from openapi_server.models.slot_difference_collection import SlotDifferenceCollection
from openapi_server.models.snapshot_collection import SnapshotCollection
from openapi_server.models.storage_migration_options import StorageMigrationOptions
from openapi_server.models.storage_migration_response import StorageMigrationResponse
from openapi_server.models.string_dictionary import StringDictionary
from openapi_server.models.triggered_job_history import TriggeredJobHistory
from openapi_server.models.triggered_job_history_collection import TriggeredJobHistoryCollection
from openapi_server.models.triggered_web_job import TriggeredWebJob
from openapi_server.models.triggered_web_job_collection import TriggeredWebJobCollection
from openapi_server.models.web_app_instance_collection import WebAppInstanceCollection
from openapi_server.models.web_apps_get200_response import WebAppsGet200Response
from openapi_server.models.web_apps_get_domain_ownership_identifier200_response import WebAppsGetDomainOwnershipIdentifier200Response
from openapi_server.models.web_apps_get_hybrid_connection200_response import WebAppsGetHybridConnection200Response
from openapi_server.models.web_apps_get_vnet_connection_gateway_slot200_response import WebAppsGetVnetConnectionGatewaySlot200Response
from openapi_server.models.web_apps_get_vnet_connection_slot200_response import WebAppsGetVnetConnectionSlot200Response
from openapi_server.models.web_apps_list200_response import WebAppsList200Response
from openapi_server.models.web_apps_list_domain_ownership_identifiers200_response import WebAppsListDomainOwnershipIdentifiers200Response
from openapi_server.models.web_apps_list_hybrid_connection_keys200_response import WebAppsListHybridConnectionKeys200Response
from openapi_server.models.web_apps_list_metric_definitions200_response import WebAppsListMetricDefinitions200Response
from openapi_server.models.web_apps_list_metrics200_response import WebAppsListMetrics200Response
from openapi_server.models.web_apps_list_publishing_credentials200_response import WebAppsListPublishingCredentials200Response
from openapi_server.models.web_apps_list_usages_slot200_response import WebAppsListUsagesSlot200Response
from openapi_server.models.web_apps_list_vnet_connections_slot200_response_inner import WebAppsListVnetConnectionsSlot200ResponseInner
from openapi_server.models.web_apps_migrate_my_sql200_response import WebAppsMigrateMySql200Response
from openapi_server.models.web_apps_recover_request import WebAppsRecoverRequest
from openapi_server.models.web_apps_update_site_push_settings_request import WebAppsUpdateSitePushSettingsRequest
from openapi_server.models.web_job import WebJob
from openapi_server.models.web_job_collection import WebJobCollection


pytestmark = pytest.mark.asyncio

async def test_web_apps_add_premier_add_on(client):
    """Test case for web_apps_add_premier_add_on

    Updates a named add-on of an app.
    """
    premier_add_on = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/premieraddons/{premier_add_on_name}'.format(resource_group_name='resource_group_name_example', name='name_example', premier_add_on_name='premier_add_on_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=premier_add_on,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_add_premier_add_on_slot(client):
    """Test case for web_apps_add_premier_add_on_slot

    Updates a named add-on of an app.
    """
    premier_add_on = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/premieraddons/{premier_add_on_name}'.format(resource_group_name='resource_group_name_example', name='name_example', premier_add_on_name='premier_add_on_name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=premier_add_on,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_analyze_custom_hostname(client):
    """Test case for web_apps_analyze_custom_hostname

    Analyze a custom hostname.
    """
    params = [('hostName', 'host_name_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/analyzeCustomHostname'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_analyze_custom_hostname_slot(client):
    """Test case for web_apps_analyze_custom_hostname_slot

    Analyze a custom hostname.
    """
    params = [('hostName', 'host_name_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/analyzeCustomHostname'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_apply_slot_config_to_production(client):
    """Test case for web_apps_apply_slot_config_to_production

    Applies the configuration settings from the target slot onto the current slot.
    """
    slot_swap_entity = {"preserveVnet":True,"targetSlot":"targetSlot"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/applySlotConfig'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=slot_swap_entity,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_apply_slot_configuration_slot(client):
    """Test case for web_apps_apply_slot_configuration_slot

    Applies the configuration settings from the target slot onto the current slot.
    """
    slot_swap_entity = {"preserveVnet":True,"targetSlot":"targetSlot"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/applySlotConfig'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=slot_swap_entity,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_backup(client):
    """Test case for web_apps_backup

    Creates a backup of an app.
    """
    request = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/backup'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_backup_slot(client):
    """Test case for web_apps_backup_slot

    Creates a backup of an app.
    """
    request = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/backup'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_create_deployment(client):
    """Test case for web_apps_create_deployment

    Create a deployment for an app, or a deployment slot.
    """
    deployment = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/deployments/{id}'.format(resource_group_name='resource_group_name_example', name='name_example', id='id_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=deployment,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_create_deployment_slot(client):
    """Test case for web_apps_create_deployment_slot

    Create a deployment for an app, or a deployment slot.
    """
    deployment = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/deployments/{id}'.format(resource_group_name='resource_group_name_example', name='name_example', id='id_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=deployment,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_create_function(client):
    """Test case for web_apps_create_function

    Create function for web site, or a deployment slot.
    """
    function_envelope = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/functions/{function_name}'.format(resource_group_name='resource_group_name_example', name='name_example', function_name='function_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=function_envelope,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_create_instance_function_slot(client):
    """Test case for web_apps_create_instance_function_slot

    Create function for web site, or a deployment slot.
    """
    function_envelope = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/functions/{function_name}'.format(resource_group_name='resource_group_name_example', name='name_example', function_name='function_name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=function_envelope,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_create_instance_ms_deploy_operation(client):
    """Test case for web_apps_create_instance_ms_deploy_operation

    Invoke the MSDeploy web app extension.
    """
    ms_deploy = {"properties":{"appOffline":True,"connectionString":"connectionString","setParameters":{"key":"setParameters"},"dbType":"dbType","packageUri":"packageUri","setParametersXmlFileUri":"setParametersXmlFileUri","skipAppData":True}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/instances/{instance_id}/extensions/MSDeploy'.format(resource_group_name='resource_group_name_example', name='name_example', instance_id='instance_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=ms_deploy,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_create_instance_ms_deploy_operation_slot(client):
    """Test case for web_apps_create_instance_ms_deploy_operation_slot

    Invoke the MSDeploy web app extension.
    """
    ms_deploy = {"properties":{"appOffline":True,"connectionString":"connectionString","setParameters":{"key":"setParameters"},"dbType":"dbType","packageUri":"packageUri","setParametersXmlFileUri":"setParametersXmlFileUri","skipAppData":True}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/instances/{instance_id}/extensions/MSDeploy'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', instance_id='instance_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=ms_deploy,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_create_ms_deploy_operation(client):
    """Test case for web_apps_create_ms_deploy_operation

    Invoke the MSDeploy web app extension.
    """
    ms_deploy = {"properties":{"appOffline":True,"connectionString":"connectionString","setParameters":{"key":"setParameters"},"dbType":"dbType","packageUri":"packageUri","setParametersXmlFileUri":"setParametersXmlFileUri","skipAppData":True}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/extensions/MSDeploy'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=ms_deploy,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_create_ms_deploy_operation_slot(client):
    """Test case for web_apps_create_ms_deploy_operation_slot

    Invoke the MSDeploy web app extension.
    """
    ms_deploy = {"properties":{"appOffline":True,"connectionString":"connectionString","setParameters":{"key":"setParameters"},"dbType":"dbType","packageUri":"packageUri","setParametersXmlFileUri":"setParametersXmlFileUri","skipAppData":True}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/extensions/MSDeploy'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=ms_deploy,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_create_or_update(client):
    """Test case for web_apps_create_or_update

    Creates a new web, mobile, or API app in an existing resource group, or updates an existing app.
    """
    site_envelope = openapi_server.WebAppsGet200Response()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=site_envelope,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_create_or_update_configuration(client):
    """Test case for web_apps_create_or_update_configuration

    Updates the configuration of an app.
    """
    site_config = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/config/web'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=site_config,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_create_or_update_configuration_slot(client):
    """Test case for web_apps_create_or_update_configuration_slot

    Updates the configuration of an app.
    """
    site_config = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/web'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=site_config,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_create_or_update_domain_ownership_identifier(client):
    """Test case for web_apps_create_or_update_domain_ownership_identifier

    Creates a domain ownership identifier for web app, or updates an existing ownership identifier.
    """
    domain_ownership_identifier = openapi_server.WebAppsGetDomainOwnershipIdentifier200Response()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/domainOwnershipIdentifiers/{domain_ownership_identifier_name}'.format(resource_group_name='resource_group_name_example', name='name_example', domain_ownership_identifier_name='domain_ownership_identifier_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=domain_ownership_identifier,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_create_or_update_domain_ownership_identifier_slot(client):
    """Test case for web_apps_create_or_update_domain_ownership_identifier_slot

    Creates a domain ownership identifier for web app, or updates an existing ownership identifier.
    """
    domain_ownership_identifier = openapi_server.WebAppsGetDomainOwnershipIdentifier200Response()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/domainOwnershipIdentifiers/{domain_ownership_identifier_name}'.format(resource_group_name='resource_group_name_example', name='name_example', domain_ownership_identifier_name='domain_ownership_identifier_name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=domain_ownership_identifier,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_create_or_update_host_name_binding(client):
    """Test case for web_apps_create_or_update_host_name_binding

    Creates a hostname binding for an app.
    """
    host_name_binding = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/hostNameBindings/{host_name}'.format(resource_group_name='resource_group_name_example', name='name_example', host_name='host_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=host_name_binding,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_create_or_update_host_name_binding_slot(client):
    """Test case for web_apps_create_or_update_host_name_binding_slot

    Creates a hostname binding for an app.
    """
    host_name_binding = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/hostNameBindings/{host_name}'.format(resource_group_name='resource_group_name_example', name='name_example', host_name='host_name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=host_name_binding,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_create_or_update_hybrid_connection(client):
    """Test case for web_apps_create_or_update_hybrid_connection

    Creates a new Hybrid Connection using a Service Bus relay.
    """
    connection_envelope = openapi_server.WebAppsGetHybridConnection200Response()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/hybridConnectionNamespaces/{namespace_name}/relays/{relay_name}'.format(resource_group_name='resource_group_name_example', name='name_example', namespace_name='namespace_name_example', relay_name='relay_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=connection_envelope,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_create_or_update_hybrid_connection_slot(client):
    """Test case for web_apps_create_or_update_hybrid_connection_slot

    Creates a new Hybrid Connection using a Service Bus relay.
    """
    connection_envelope = openapi_server.WebAppsGetHybridConnection200Response()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/hybridConnectionNamespaces/{namespace_name}/relays/{relay_name}'.format(resource_group_name='resource_group_name_example', name='name_example', namespace_name='namespace_name_example', relay_name='relay_name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=connection_envelope,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_create_or_update_public_certificate(client):
    """Test case for web_apps_create_or_update_public_certificate

    Creates a hostname binding for an app.
    """
    public_certificate = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/publicCertificates/{public_certificate_name}'.format(resource_group_name='resource_group_name_example', name='name_example', public_certificate_name='public_certificate_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=public_certificate,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_create_or_update_public_certificate_slot(client):
    """Test case for web_apps_create_or_update_public_certificate_slot

    Creates a hostname binding for an app.
    """
    public_certificate = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/publicCertificates/{public_certificate_name}'.format(resource_group_name='resource_group_name_example', name='name_example', public_certificate_name='public_certificate_name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=public_certificate,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_create_or_update_relay_service_connection(client):
    """Test case for web_apps_create_or_update_relay_service_connection

    Creates a new hybrid connection configuration (PUT), or updates an existing one (PATCH).
    """
    connection_envelope = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/hybridconnection/{entity_name}'.format(resource_group_name='resource_group_name_example', name='name_example', entity_name='entity_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=connection_envelope,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_create_or_update_relay_service_connection_slot(client):
    """Test case for web_apps_create_or_update_relay_service_connection_slot

    Creates a new hybrid connection configuration (PUT), or updates an existing one (PATCH).
    """
    connection_envelope = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/hybridconnection/{entity_name}'.format(resource_group_name='resource_group_name_example', name='name_example', entity_name='entity_name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=connection_envelope,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_create_or_update_slot(client):
    """Test case for web_apps_create_or_update_slot

    Creates a new web, mobile, or API app in an existing resource group, or updates an existing app.
    """
    site_envelope = openapi_server.WebAppsGet200Response()
    params = [('skipDnsRegistration', True),
                    ('skipCustomDomainVerification', True),
                    ('forceDnsRegistration', True),
                    ('ttlInSeconds', 'ttl_in_seconds_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=site_envelope,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_create_or_update_source_control(client):
    """Test case for web_apps_create_or_update_source_control

    Updates the source control configuration of an app.
    """
    site_source_control = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/sourcecontrols/web'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=site_source_control,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_create_or_update_source_control_slot(client):
    """Test case for web_apps_create_or_update_source_control_slot

    Updates the source control configuration of an app.
    """
    site_source_control = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/sourcecontrols/web'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=site_source_control,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_create_or_update_vnet_connection(client):
    """Test case for web_apps_create_or_update_vnet_connection

    Adds a Virtual Network connection to an app or slot (PUT) or updates the connection properties (PATCH).
    """
    connection_envelope = openapi_server.WebAppsGetVnetConnectionSlot200Response()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/virtualNetworkConnections/{vnet_name}'.format(resource_group_name='resource_group_name_example', name='name_example', vnet_name='vnet_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=connection_envelope,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_create_or_update_vnet_connection_gateway(client):
    """Test case for web_apps_create_or_update_vnet_connection_gateway

    Adds a gateway to a connected Virtual Network (PUT) or updates it (PATCH).
    """
    connection_envelope = openapi_server.WebAppsGetVnetConnectionGatewaySlot200Response()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/virtualNetworkConnections/{vnet_name}/gateways/{gateway_name}'.format(resource_group_name='resource_group_name_example', name='name_example', vnet_name='vnet_name_example', gateway_name='gateway_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=connection_envelope,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_create_or_update_vnet_connection_gateway_slot(client):
    """Test case for web_apps_create_or_update_vnet_connection_gateway_slot

    Adds a gateway to a connected Virtual Network (PUT) or updates it (PATCH).
    """
    connection_envelope = openapi_server.WebAppsGetVnetConnectionGatewaySlot200Response()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/virtualNetworkConnections/{vnet_name}/gateways/{gateway_name}'.format(resource_group_name='resource_group_name_example', name='name_example', vnet_name='vnet_name_example', gateway_name='gateway_name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=connection_envelope,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_create_or_update_vnet_connection_slot(client):
    """Test case for web_apps_create_or_update_vnet_connection_slot

    Adds a Virtual Network connection to an app or slot (PUT) or updates the connection properties (PATCH).
    """
    connection_envelope = openapi_server.WebAppsGetVnetConnectionSlot200Response()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/virtualNetworkConnections/{vnet_name}'.format(resource_group_name='resource_group_name_example', name='name_example', vnet_name='vnet_name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=connection_envelope,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_delete(client):
    """Test case for web_apps_delete

    Deletes a web, mobile, or API app, or one of the deployment slots.
    """
    params = [('deleteMetrics', True),
                    ('deleteEmptyServerFarm', True),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_delete_backup(client):
    """Test case for web_apps_delete_backup

    Deletes a backup of an app by its ID.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/backups/{backup_id}'.format(resource_group_name='resource_group_name_example', name='name_example', backup_id='backup_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_delete_backup_configuration(client):
    """Test case for web_apps_delete_backup_configuration

    Deletes the backup configuration of an app.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/config/backup'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_delete_backup_configuration_slot(client):
    """Test case for web_apps_delete_backup_configuration_slot

    Deletes the backup configuration of an app.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/backup'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_delete_backup_slot(client):
    """Test case for web_apps_delete_backup_slot

    Deletes a backup of an app by its ID.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/backups/{backup_id}'.format(resource_group_name='resource_group_name_example', name='name_example', backup_id='backup_id_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_delete_continuous_web_job(client):
    """Test case for web_apps_delete_continuous_web_job

    Delete a continuous web job by its ID for an app, or a deployment slot.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/continuouswebjobs/{web_job_name}'.format(resource_group_name='resource_group_name_example', name='name_example', web_job_name='web_job_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_delete_continuous_web_job_slot(client):
    """Test case for web_apps_delete_continuous_web_job_slot

    Delete a continuous web job by its ID for an app, or a deployment slot.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/continuouswebjobs/{web_job_name}'.format(resource_group_name='resource_group_name_example', name='name_example', web_job_name='web_job_name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_delete_deployment(client):
    """Test case for web_apps_delete_deployment

    Delete a deployment by its ID for an app, or a deployment slot.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/deployments/{id}'.format(resource_group_name='resource_group_name_example', name='name_example', id='id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_delete_deployment_slot(client):
    """Test case for web_apps_delete_deployment_slot

    Delete a deployment by its ID for an app, or a deployment slot.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/deployments/{id}'.format(resource_group_name='resource_group_name_example', name='name_example', id='id_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_delete_domain_ownership_identifier(client):
    """Test case for web_apps_delete_domain_ownership_identifier

    Deletes a domain ownership identifier for a web app.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/domainOwnershipIdentifiers/{domain_ownership_identifier_name}'.format(resource_group_name='resource_group_name_example', name='name_example', domain_ownership_identifier_name='domain_ownership_identifier_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_delete_domain_ownership_identifier_slot(client):
    """Test case for web_apps_delete_domain_ownership_identifier_slot

    Deletes a domain ownership identifier for a web app.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/domainOwnershipIdentifiers/{domain_ownership_identifier_name}'.format(resource_group_name='resource_group_name_example', name='name_example', domain_ownership_identifier_name='domain_ownership_identifier_name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_delete_function(client):
    """Test case for web_apps_delete_function

    Delete a function for web site, or a deployment slot.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/functions/{function_name}'.format(resource_group_name='resource_group_name_example', name='name_example', function_name='function_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_delete_host_name_binding(client):
    """Test case for web_apps_delete_host_name_binding

    Deletes a hostname binding for an app.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/hostNameBindings/{host_name}'.format(resource_group_name='resource_group_name_example', name='name_example', host_name='host_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_delete_host_name_binding_slot(client):
    """Test case for web_apps_delete_host_name_binding_slot

    Deletes a hostname binding for an app.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/hostNameBindings/{host_name}'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', host_name='host_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_delete_hybrid_connection(client):
    """Test case for web_apps_delete_hybrid_connection

    Removes a Hybrid Connection from this site.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/hybridConnectionNamespaces/{namespace_name}/relays/{relay_name}'.format(resource_group_name='resource_group_name_example', name='name_example', namespace_name='namespace_name_example', relay_name='relay_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_delete_hybrid_connection_slot(client):
    """Test case for web_apps_delete_hybrid_connection_slot

    Removes a Hybrid Connection from this site.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/hybridConnectionNamespaces/{namespace_name}/relays/{relay_name}'.format(resource_group_name='resource_group_name_example', name='name_example', namespace_name='namespace_name_example', relay_name='relay_name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_delete_instance_function_slot(client):
    """Test case for web_apps_delete_instance_function_slot

    Delete a function for web site, or a deployment slot.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/functions/{function_name}'.format(resource_group_name='resource_group_name_example', name='name_example', function_name='function_name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_delete_instance_process(client):
    """Test case for web_apps_delete_instance_process

    Terminate a process by its ID for a web site, or a deployment slot, or specific scaled-out instance in a web site.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/instances/{instance_id}/processes/{process_id}'.format(resource_group_name='resource_group_name_example', name='name_example', process_id='process_id_example', instance_id='instance_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_delete_instance_process_slot(client):
    """Test case for web_apps_delete_instance_process_slot

    Terminate a process by its ID for a web site, or a deployment slot, or specific scaled-out instance in a web site.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/instances/{instance_id}/processes/{process_id}'.format(resource_group_name='resource_group_name_example', name='name_example', process_id='process_id_example', slot='slot_example', instance_id='instance_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_delete_premier_add_on(client):
    """Test case for web_apps_delete_premier_add_on

    Delete a premier add-on from an app.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/premieraddons/{premier_add_on_name}'.format(resource_group_name='resource_group_name_example', name='name_example', premier_add_on_name='premier_add_on_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_delete_premier_add_on_slot(client):
    """Test case for web_apps_delete_premier_add_on_slot

    Delete a premier add-on from an app.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/premieraddons/{premier_add_on_name}'.format(resource_group_name='resource_group_name_example', name='name_example', premier_add_on_name='premier_add_on_name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_delete_process(client):
    """Test case for web_apps_delete_process

    Terminate a process by its ID for a web site, or a deployment slot, or specific scaled-out instance in a web site.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/processes/{process_id}'.format(resource_group_name='resource_group_name_example', name='name_example', process_id='process_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_delete_process_slot(client):
    """Test case for web_apps_delete_process_slot

    Terminate a process by its ID for a web site, or a deployment slot, or specific scaled-out instance in a web site.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/processes/{process_id}'.format(resource_group_name='resource_group_name_example', name='name_example', process_id='process_id_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_delete_public_certificate(client):
    """Test case for web_apps_delete_public_certificate

    Deletes a hostname binding for an app.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/publicCertificates/{public_certificate_name}'.format(resource_group_name='resource_group_name_example', name='name_example', public_certificate_name='public_certificate_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_delete_public_certificate_slot(client):
    """Test case for web_apps_delete_public_certificate_slot

    Deletes a hostname binding for an app.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/publicCertificates/{public_certificate_name}'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', public_certificate_name='public_certificate_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_delete_relay_service_connection(client):
    """Test case for web_apps_delete_relay_service_connection

    Deletes a relay service connection by its name.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/hybridconnection/{entity_name}'.format(resource_group_name='resource_group_name_example', name='name_example', entity_name='entity_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_delete_relay_service_connection_slot(client):
    """Test case for web_apps_delete_relay_service_connection_slot

    Deletes a relay service connection by its name.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/hybridconnection/{entity_name}'.format(resource_group_name='resource_group_name_example', name='name_example', entity_name='entity_name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_delete_site_extension(client):
    """Test case for web_apps_delete_site_extension

    Remove a site extension from a web site, or a deployment slot.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/siteextensions/{site_extension_id}'.format(resource_group_name='resource_group_name_example', name='name_example', site_extension_id='site_extension_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_delete_site_extension_slot(client):
    """Test case for web_apps_delete_site_extension_slot

    Remove a site extension from a web site, or a deployment slot.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/siteextensions/{site_extension_id}'.format(resource_group_name='resource_group_name_example', name='name_example', site_extension_id='site_extension_id_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_delete_slot(client):
    """Test case for web_apps_delete_slot

    Deletes a web, mobile, or API app, or one of the deployment slots.
    """
    params = [('deleteMetrics', True),
                    ('deleteEmptyServerFarm', True),
                    ('skipDnsRegistration', True),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_delete_source_control(client):
    """Test case for web_apps_delete_source_control

    Deletes the source control configuration of an app.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/sourcecontrols/web'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_delete_source_control_slot(client):
    """Test case for web_apps_delete_source_control_slot

    Deletes the source control configuration of an app.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/sourcecontrols/web'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_delete_triggered_web_job(client):
    """Test case for web_apps_delete_triggered_web_job

    Delete a triggered web job by its ID for an app, or a deployment slot.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/triggeredwebjobs/{web_job_name}'.format(resource_group_name='resource_group_name_example', name='name_example', web_job_name='web_job_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_delete_triggered_web_job_slot(client):
    """Test case for web_apps_delete_triggered_web_job_slot

    Delete a triggered web job by its ID for an app, or a deployment slot.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/triggeredwebjobs/{web_job_name}'.format(resource_group_name='resource_group_name_example', name='name_example', web_job_name='web_job_name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_delete_vnet_connection(client):
    """Test case for web_apps_delete_vnet_connection

    Deletes a connection from an app (or deployment slot to a named virtual network.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/virtualNetworkConnections/{vnet_name}'.format(resource_group_name='resource_group_name_example', name='name_example', vnet_name='vnet_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_delete_vnet_connection_slot(client):
    """Test case for web_apps_delete_vnet_connection_slot

    Deletes a connection from an app (or deployment slot to a named virtual network.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/virtualNetworkConnections/{vnet_name}'.format(resource_group_name='resource_group_name_example', name='name_example', vnet_name='vnet_name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_discover_restore(client):
    """Test case for web_apps_discover_restore

    Discovers an existing app backup that can be restored from a blob in Azure storage.
    """
    request = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/backups/discover'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_discover_restore_slot(client):
    """Test case for web_apps_discover_restore_slot

    Discovers an existing app backup that can be restored from a blob in Azure storage.
    """
    request = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/backups/discover'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_generate_new_site_publishing_password(client):
    """Test case for web_apps_generate_new_site_publishing_password

    Generates a new publishing password for an app (or deployment slot, if specified).
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/newpassword'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_generate_new_site_publishing_password_slot(client):
    """Test case for web_apps_generate_new_site_publishing_password_slot

    Generates a new publishing password for an app (or deployment slot, if specified).
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/newpassword'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get(client):
    """Test case for web_apps_get

    Gets the details of a web, mobile, or API app.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_auth_settings(client):
    """Test case for web_apps_get_auth_settings

    Gets the Authentication/Authorization settings of an app.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/config/authsettings/list'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_auth_settings_slot(client):
    """Test case for web_apps_get_auth_settings_slot

    Gets the Authentication/Authorization settings of an app.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/authsettings/list'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_backup_configuration(client):
    """Test case for web_apps_get_backup_configuration

    Gets the backup configuration of an app.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/config/backup/list'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_backup_configuration_slot(client):
    """Test case for web_apps_get_backup_configuration_slot

    Gets the backup configuration of an app.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/backup/list'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_backup_status(client):
    """Test case for web_apps_get_backup_status

    Gets a backup of an app by its ID.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/backups/{backup_id}'.format(resource_group_name='resource_group_name_example', name='name_example', backup_id='backup_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_backup_status_slot(client):
    """Test case for web_apps_get_backup_status_slot

    Gets a backup of an app by its ID.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/backups/{backup_id}'.format(resource_group_name='resource_group_name_example', name='name_example', backup_id='backup_id_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_configuration(client):
    """Test case for web_apps_get_configuration

    Gets the configuration of an app, such as platform version and bitness, default documents, virtual applications, Always On, etc.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/config/web'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_configuration_slot(client):
    """Test case for web_apps_get_configuration_slot

    Gets the configuration of an app, such as platform version and bitness, default documents, virtual applications, Always On, etc.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/web'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_configuration_snapshot(client):
    """Test case for web_apps_get_configuration_snapshot

    Gets a snapshot of the configuration of an app at a previous point in time.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/config/web/snapshots/{snapshot_id}'.format(resource_group_name='resource_group_name_example', name='name_example', snapshot_id='snapshot_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_configuration_snapshot_slot(client):
    """Test case for web_apps_get_configuration_snapshot_slot

    Gets a snapshot of the configuration of an app at a previous point in time.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/web/snapshots/{snapshot_id}'.format(resource_group_name='resource_group_name_example', name='name_example', snapshot_id='snapshot_id_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_continuous_web_job(client):
    """Test case for web_apps_get_continuous_web_job

    Gets a continuous web job by its ID for an app, or a deployment slot.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/continuouswebjobs/{web_job_name}'.format(resource_group_name='resource_group_name_example', name='name_example', web_job_name='web_job_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_continuous_web_job_slot(client):
    """Test case for web_apps_get_continuous_web_job_slot

    Gets a continuous web job by its ID for an app, or a deployment slot.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/continuouswebjobs/{web_job_name}'.format(resource_group_name='resource_group_name_example', name='name_example', web_job_name='web_job_name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_deployment(client):
    """Test case for web_apps_get_deployment

    Get a deployment by its ID for an app, or a deployment slot.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/deployments/{id}'.format(resource_group_name='resource_group_name_example', name='name_example', id='id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_deployment_slot(client):
    """Test case for web_apps_get_deployment_slot

    Get a deployment by its ID for an app, or a deployment slot.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/deployments/{id}'.format(resource_group_name='resource_group_name_example', name='name_example', id='id_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_diagnostic_logs_configuration(client):
    """Test case for web_apps_get_diagnostic_logs_configuration

    Gets the logging configuration of an app.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/config/logs'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_diagnostic_logs_configuration_slot(client):
    """Test case for web_apps_get_diagnostic_logs_configuration_slot

    Gets the logging configuration of an app.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/logs'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_domain_ownership_identifier(client):
    """Test case for web_apps_get_domain_ownership_identifier

    Get domain ownership identifier for web app.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/domainOwnershipIdentifiers/{domain_ownership_identifier_name}'.format(resource_group_name='resource_group_name_example', name='name_example', domain_ownership_identifier_name='domain_ownership_identifier_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_domain_ownership_identifier_slot(client):
    """Test case for web_apps_get_domain_ownership_identifier_slot

    Get domain ownership identifier for web app.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/domainOwnershipIdentifiers/{domain_ownership_identifier_name}'.format(resource_group_name='resource_group_name_example', name='name_example', domain_ownership_identifier_name='domain_ownership_identifier_name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_function(client):
    """Test case for web_apps_get_function

    Get function information by its ID for web site, or a deployment slot.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/functions/{function_name}'.format(resource_group_name='resource_group_name_example', name='name_example', function_name='function_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_functions_admin_token(client):
    """Test case for web_apps_get_functions_admin_token

    Fetch a short lived token that can be exchanged for a master key.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/functions/admin/token'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_functions_admin_token_slot(client):
    """Test case for web_apps_get_functions_admin_token_slot

    Fetch a short lived token that can be exchanged for a master key.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/functions/admin/token'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_host_name_binding(client):
    """Test case for web_apps_get_host_name_binding

    Get the named hostname binding for an app (or deployment slot, if specified).
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/hostNameBindings/{host_name}'.format(resource_group_name='resource_group_name_example', name='name_example', host_name='host_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_host_name_binding_slot(client):
    """Test case for web_apps_get_host_name_binding_slot

    Get the named hostname binding for an app (or deployment slot, if specified).
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/hostNameBindings/{host_name}'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', host_name='host_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_hybrid_connection(client):
    """Test case for web_apps_get_hybrid_connection

    Retrieves a specific Service Bus Hybrid Connection used by this Web App.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/hybridConnectionNamespaces/{namespace_name}/relays/{relay_name}'.format(resource_group_name='resource_group_name_example', name='name_example', namespace_name='namespace_name_example', relay_name='relay_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_hybrid_connection_slot(client):
    """Test case for web_apps_get_hybrid_connection_slot

    Retrieves a specific Service Bus Hybrid Connection used by this Web App.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/hybridConnectionNamespaces/{namespace_name}/relays/{relay_name}'.format(resource_group_name='resource_group_name_example', name='name_example', namespace_name='namespace_name_example', relay_name='relay_name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_instance_function_slot(client):
    """Test case for web_apps_get_instance_function_slot

    Get function information by its ID for web site, or a deployment slot.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/functions/{function_name}'.format(resource_group_name='resource_group_name_example', name='name_example', function_name='function_name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_instance_ms_deploy_log(client):
    """Test case for web_apps_get_instance_ms_deploy_log

    Get the MSDeploy Log for the last MSDeploy operation.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/instances/{instance_id}/extensions/MSDeploy/log'.format(resource_group_name='resource_group_name_example', name='name_example', instance_id='instance_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_instance_ms_deploy_log_slot(client):
    """Test case for web_apps_get_instance_ms_deploy_log_slot

    Get the MSDeploy Log for the last MSDeploy operation.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/instances/{instance_id}/extensions/MSDeploy/log'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', instance_id='instance_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_instance_ms_deploy_status(client):
    """Test case for web_apps_get_instance_ms_deploy_status

    Get the status of the last MSDeploy operation.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/instances/{instance_id}/extensions/MSDeploy'.format(resource_group_name='resource_group_name_example', name='name_example', instance_id='instance_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_instance_ms_deploy_status_slot(client):
    """Test case for web_apps_get_instance_ms_deploy_status_slot

    Get the status of the last MSDeploy operation.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/instances/{instance_id}/extensions/MSDeploy'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', instance_id='instance_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_instance_process(client):
    """Test case for web_apps_get_instance_process

    Get process information by its ID for a specific scaled-out instance in a web site.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/instances/{instance_id}/processes/{process_id}'.format(resource_group_name='resource_group_name_example', name='name_example', process_id='process_id_example', instance_id='instance_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_instance_process_dump(client):
    """Test case for web_apps_get_instance_process_dump

    Get a memory dump of a process by its ID for a specific scaled-out instance in a web site.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/instances/{instance_id}/processes/{process_id}/dump'.format(resource_group_name='resource_group_name_example', name='name_example', process_id='process_id_example', instance_id='instance_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_instance_process_dump_slot(client):
    """Test case for web_apps_get_instance_process_dump_slot

    Get a memory dump of a process by its ID for a specific scaled-out instance in a web site.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/instances/{instance_id}/processes/{process_id}/dump'.format(resource_group_name='resource_group_name_example', name='name_example', process_id='process_id_example', slot='slot_example', instance_id='instance_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_instance_process_module(client):
    """Test case for web_apps_get_instance_process_module

    Get process information by its ID for a specific scaled-out instance in a web site.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/instances/{instance_id}/processes/{process_id}/modules/{base_address}'.format(resource_group_name='resource_group_name_example', name='name_example', process_id='process_id_example', base_address='base_address_example', instance_id='instance_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_instance_process_module_slot(client):
    """Test case for web_apps_get_instance_process_module_slot

    Get process information by its ID for a specific scaled-out instance in a web site.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/instances/{instance_id}/processes/{process_id}/modules/{base_address}'.format(resource_group_name='resource_group_name_example', name='name_example', process_id='process_id_example', base_address='base_address_example', slot='slot_example', instance_id='instance_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_instance_process_slot(client):
    """Test case for web_apps_get_instance_process_slot

    Get process information by its ID for a specific scaled-out instance in a web site.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/instances/{instance_id}/processes/{process_id}'.format(resource_group_name='resource_group_name_example', name='name_example', process_id='process_id_example', slot='slot_example', instance_id='instance_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_instance_process_thread(client):
    """Test case for web_apps_get_instance_process_thread

    Get thread information by Thread ID for a specific process, in a specific scaled-out instance in a web site.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/instances/{instance_id}/processes/{process_id}/threads/{thread_id}'.format(resource_group_name='resource_group_name_example', name='name_example', process_id='process_id_example', thread_id='thread_id_example', instance_id='instance_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_instance_process_thread_slot(client):
    """Test case for web_apps_get_instance_process_thread_slot

    Get thread information by Thread ID for a specific process, in a specific scaled-out instance in a web site.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/instances/{instance_id}/processes/{process_id}/threads/{thread_id}'.format(resource_group_name='resource_group_name_example', name='name_example', process_id='process_id_example', thread_id='thread_id_example', slot='slot_example', instance_id='instance_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_migrate_my_sql_status(client):
    """Test case for web_apps_get_migrate_my_sql_status

    Returns the status of MySql in app migration, if one is active, and whether or not MySql in app is enabled
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/migratemysql/status'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_migrate_my_sql_status_slot(client):
    """Test case for web_apps_get_migrate_my_sql_status_slot

    Returns the status of MySql in app migration, if one is active, and whether or not MySql in app is enabled
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/migratemysql/status'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_ms_deploy_log(client):
    """Test case for web_apps_get_ms_deploy_log

    Get the MSDeploy Log for the last MSDeploy operation.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/extensions/MSDeploy/log'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_ms_deploy_log_slot(client):
    """Test case for web_apps_get_ms_deploy_log_slot

    Get the MSDeploy Log for the last MSDeploy operation.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/extensions/MSDeploy/log'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_ms_deploy_status(client):
    """Test case for web_apps_get_ms_deploy_status

    Get the status of the last MSDeploy operation.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/extensions/MSDeploy'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_ms_deploy_status_slot(client):
    """Test case for web_apps_get_ms_deploy_status_slot

    Get the status of the last MSDeploy operation.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/extensions/MSDeploy'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_premier_add_on(client):
    """Test case for web_apps_get_premier_add_on

    Gets a named add-on of an app.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/premieraddons/{premier_add_on_name}'.format(resource_group_name='resource_group_name_example', name='name_example', premier_add_on_name='premier_add_on_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_premier_add_on_slot(client):
    """Test case for web_apps_get_premier_add_on_slot

    Gets a named add-on of an app.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/premieraddons/{premier_add_on_name}'.format(resource_group_name='resource_group_name_example', name='name_example', premier_add_on_name='premier_add_on_name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_process(client):
    """Test case for web_apps_get_process

    Get process information by its ID for a specific scaled-out instance in a web site.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/processes/{process_id}'.format(resource_group_name='resource_group_name_example', name='name_example', process_id='process_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_process_dump(client):
    """Test case for web_apps_get_process_dump

    Get a memory dump of a process by its ID for a specific scaled-out instance in a web site.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/processes/{process_id}/dump'.format(resource_group_name='resource_group_name_example', name='name_example', process_id='process_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_process_dump_slot(client):
    """Test case for web_apps_get_process_dump_slot

    Get a memory dump of a process by its ID for a specific scaled-out instance in a web site.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/processes/{process_id}/dump'.format(resource_group_name='resource_group_name_example', name='name_example', process_id='process_id_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_process_module(client):
    """Test case for web_apps_get_process_module

    Get process information by its ID for a specific scaled-out instance in a web site.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/processes/{process_id}/modules/{base_address}'.format(resource_group_name='resource_group_name_example', name='name_example', process_id='process_id_example', base_address='base_address_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_process_module_slot(client):
    """Test case for web_apps_get_process_module_slot

    Get process information by its ID for a specific scaled-out instance in a web site.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/processes/{process_id}/modules/{base_address}'.format(resource_group_name='resource_group_name_example', name='name_example', process_id='process_id_example', base_address='base_address_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_process_slot(client):
    """Test case for web_apps_get_process_slot

    Get process information by its ID for a specific scaled-out instance in a web site.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/processes/{process_id}'.format(resource_group_name='resource_group_name_example', name='name_example', process_id='process_id_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_process_thread(client):
    """Test case for web_apps_get_process_thread

    Get thread information by Thread ID for a specific process, in a specific scaled-out instance in a web site.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/processes/{process_id}/threads/{thread_id}'.format(resource_group_name='resource_group_name_example', name='name_example', process_id='process_id_example', thread_id='thread_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_process_thread_slot(client):
    """Test case for web_apps_get_process_thread_slot

    Get thread information by Thread ID for a specific process, in a specific scaled-out instance in a web site.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/processes/{process_id}/threads/{thread_id}'.format(resource_group_name='resource_group_name_example', name='name_example', process_id='process_id_example', thread_id='thread_id_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_public_certificate(client):
    """Test case for web_apps_get_public_certificate

    Get the named public certificate for an app (or deployment slot, if specified).
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/publicCertificates/{public_certificate_name}'.format(resource_group_name='resource_group_name_example', name='name_example', public_certificate_name='public_certificate_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_public_certificate_slot(client):
    """Test case for web_apps_get_public_certificate_slot

    Get the named public certificate for an app (or deployment slot, if specified).
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/publicCertificates/{public_certificate_name}'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', public_certificate_name='public_certificate_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_relay_service_connection(client):
    """Test case for web_apps_get_relay_service_connection

    Gets a hybrid connection configuration by its name.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/hybridconnection/{entity_name}'.format(resource_group_name='resource_group_name_example', name='name_example', entity_name='entity_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_relay_service_connection_slot(client):
    """Test case for web_apps_get_relay_service_connection_slot

    Gets a hybrid connection configuration by its name.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/hybridconnection/{entity_name}'.format(resource_group_name='resource_group_name_example', name='name_example', entity_name='entity_name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_site_extension(client):
    """Test case for web_apps_get_site_extension

    Get site extension information by its ID for a web site, or a deployment slot.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/siteextensions/{site_extension_id}'.format(resource_group_name='resource_group_name_example', name='name_example', site_extension_id='site_extension_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_site_extension_slot(client):
    """Test case for web_apps_get_site_extension_slot

    Get site extension information by its ID for a web site, or a deployment slot.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/siteextensions/{site_extension_id}'.format(resource_group_name='resource_group_name_example', name='name_example', site_extension_id='site_extension_id_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_site_php_error_log_flag(client):
    """Test case for web_apps_get_site_php_error_log_flag

    Gets web app's event logs.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/phplogging'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_site_php_error_log_flag_slot(client):
    """Test case for web_apps_get_site_php_error_log_flag_slot

    Gets web app's event logs.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/phplogging'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_slot(client):
    """Test case for web_apps_get_slot

    Gets the details of a web, mobile, or API app.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_source_control(client):
    """Test case for web_apps_get_source_control

    Gets the source control configuration of an app.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/sourcecontrols/web'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_source_control_slot(client):
    """Test case for web_apps_get_source_control_slot

    Gets the source control configuration of an app.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/sourcecontrols/web'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_triggered_web_job(client):
    """Test case for web_apps_get_triggered_web_job

    Gets a triggered web job by its ID for an app, or a deployment slot.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/triggeredwebjobs/{web_job_name}'.format(resource_group_name='resource_group_name_example', name='name_example', web_job_name='web_job_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_triggered_web_job_history(client):
    """Test case for web_apps_get_triggered_web_job_history

    Gets a triggered web job's history by its ID for an app, , or a deployment slot.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/triggeredwebjobs/{web_job_name}/history/{id}'.format(resource_group_name='resource_group_name_example', name='name_example', web_job_name='web_job_name_example', id='id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_triggered_web_job_history_slot(client):
    """Test case for web_apps_get_triggered_web_job_history_slot

    Gets a triggered web job's history by its ID for an app, , or a deployment slot.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/triggeredwebjobs/{web_job_name}/history/{id}'.format(resource_group_name='resource_group_name_example', name='name_example', web_job_name='web_job_name_example', id='id_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_triggered_web_job_slot(client):
    """Test case for web_apps_get_triggered_web_job_slot

    Gets a triggered web job by its ID for an app, or a deployment slot.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/triggeredwebjobs/{web_job_name}'.format(resource_group_name='resource_group_name_example', name='name_example', web_job_name='web_job_name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_vnet_connection(client):
    """Test case for web_apps_get_vnet_connection

    Gets a virtual network the app (or deployment slot) is connected to by name.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/virtualNetworkConnections/{vnet_name}'.format(resource_group_name='resource_group_name_example', name='name_example', vnet_name='vnet_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_vnet_connection_gateway(client):
    """Test case for web_apps_get_vnet_connection_gateway

    Gets an app's Virtual Network gateway.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/virtualNetworkConnections/{vnet_name}/gateways/{gateway_name}'.format(resource_group_name='resource_group_name_example', name='name_example', vnet_name='vnet_name_example', gateway_name='gateway_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_vnet_connection_gateway_slot(client):
    """Test case for web_apps_get_vnet_connection_gateway_slot

    Gets an app's Virtual Network gateway.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/virtualNetworkConnections/{vnet_name}/gateways/{gateway_name}'.format(resource_group_name='resource_group_name_example', name='name_example', vnet_name='vnet_name_example', gateway_name='gateway_name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_vnet_connection_slot(client):
    """Test case for web_apps_get_vnet_connection_slot

    Gets a virtual network the app (or deployment slot) is connected to by name.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/virtualNetworkConnections/{vnet_name}'.format(resource_group_name='resource_group_name_example', name='name_example', vnet_name='vnet_name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_web_job(client):
    """Test case for web_apps_get_web_job

    Get webjob information for an app, or a deployment slot.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/webjobs/{web_job_name}'.format(resource_group_name='resource_group_name_example', name='name_example', web_job_name='web_job_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_web_job_slot(client):
    """Test case for web_apps_get_web_job_slot

    Get webjob information for an app, or a deployment slot.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/webjobs/{web_job_name}'.format(resource_group_name='resource_group_name_example', name='name_example', web_job_name='web_job_name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_web_site_container_logs(client):
    """Test case for web_apps_get_web_site_container_logs

    Gets the last lines of docker logs for the given site
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/octet-stream',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/containerlogs'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_web_site_container_logs_slot(client):
    """Test case for web_apps_get_web_site_container_logs_slot

    Gets the last lines of docker logs for the given site
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/octet-stream',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/containerlogs'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_web_site_container_logs_zip(client):
    """Test case for web_apps_get_web_site_container_logs_zip

    Gets the ZIP archived docker log files for the given site
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/zip',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/containerlogs/zip/download'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_get_web_site_container_logs_zip_slot(client):
    """Test case for web_apps_get_web_site_container_logs_zip_slot

    Gets the ZIP archived docker log files for the given site
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/zip',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/containerlogs/zip/download'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_install_site_extension(client):
    """Test case for web_apps_install_site_extension

    Install site extension on a web site, or a deployment slot.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/siteextensions/{site_extension_id}'.format(resource_group_name='resource_group_name_example', name='name_example', site_extension_id='site_extension_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_install_site_extension_slot(client):
    """Test case for web_apps_install_site_extension_slot

    Install site extension on a web site, or a deployment slot.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/siteextensions/{site_extension_id}'.format(resource_group_name='resource_group_name_example', name='name_example', site_extension_id='site_extension_id_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_is_cloneable(client):
    """Test case for web_apps_is_cloneable

    Shows whether an app can be cloned to another resource group or subscription.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/iscloneable'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_is_cloneable_slot(client):
    """Test case for web_apps_is_cloneable_slot

    Shows whether an app can be cloned to another resource group or subscription.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/iscloneable'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list(client):
    """Test case for web_apps_list

    Get all apps for a subscription.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Web/sites'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_application_settings(client):
    """Test case for web_apps_list_application_settings

    Gets the application settings of an app.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/config/appsettings/list'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_application_settings_slot(client):
    """Test case for web_apps_list_application_settings_slot

    Gets the application settings of an app.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/appsettings/list'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_backup_status_secrets(client):
    """Test case for web_apps_list_backup_status_secrets

    Gets status of a web app backup that may be in progress, including secrets associated with the backup, such as the Azure Storage SAS URL. Also can be used to update the SAS URL for the backup if a new URL is passed in the request body.
    """
    request = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/backups/{backup_id}/list'.format(resource_group_name='resource_group_name_example', name='name_example', backup_id='backup_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_backup_status_secrets_slot(client):
    """Test case for web_apps_list_backup_status_secrets_slot

    Gets status of a web app backup that may be in progress, including secrets associated with the backup, such as the Azure Storage SAS URL. Also can be used to update the SAS URL for the backup if a new URL is passed in the request body.
    """
    request = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/backups/{backup_id}/list'.format(resource_group_name='resource_group_name_example', name='name_example', backup_id='backup_id_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_backups(client):
    """Test case for web_apps_list_backups

    Gets existing backups of an app.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/backups'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_backups_slot(client):
    """Test case for web_apps_list_backups_slot

    Gets existing backups of an app.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/backups'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_by_resource_group(client):
    """Test case for web_apps_list_by_resource_group

    Gets all web, mobile, and API apps in the specified resource group.
    """
    params = [('includeSlots', True),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_configuration_snapshot_info(client):
    """Test case for web_apps_list_configuration_snapshot_info

    Gets a list of web app configuration snapshots identifiers. Each element of the list contains a timestamp and the ID of the snapshot.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/config/web/snapshots'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_configuration_snapshot_info_slot(client):
    """Test case for web_apps_list_configuration_snapshot_info_slot

    Gets a list of web app configuration snapshots identifiers. Each element of the list contains a timestamp and the ID of the snapshot.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/web/snapshots'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_configurations(client):
    """Test case for web_apps_list_configurations

    List the configurations of an app
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/config'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_configurations_slot(client):
    """Test case for web_apps_list_configurations_slot

    List the configurations of an app
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_connection_strings(client):
    """Test case for web_apps_list_connection_strings

    Gets the connection strings of an app.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/config/connectionstrings/list'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_connection_strings_slot(client):
    """Test case for web_apps_list_connection_strings_slot

    Gets the connection strings of an app.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/connectionstrings/list'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_continuous_web_jobs(client):
    """Test case for web_apps_list_continuous_web_jobs

    List continuous web jobs for an app, or a deployment slot.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/continuouswebjobs'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_continuous_web_jobs_slot(client):
    """Test case for web_apps_list_continuous_web_jobs_slot

    List continuous web jobs for an app, or a deployment slot.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/continuouswebjobs'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_deployment_log(client):
    """Test case for web_apps_list_deployment_log

    List deployment log for specific deployment for an app, or a deployment slot.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/deployments/{id}/log'.format(resource_group_name='resource_group_name_example', name='name_example', id='id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_deployment_log_slot(client):
    """Test case for web_apps_list_deployment_log_slot

    List deployment log for specific deployment for an app, or a deployment slot.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/deployments/{id}/log'.format(resource_group_name='resource_group_name_example', name='name_example', id='id_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_deployments(client):
    """Test case for web_apps_list_deployments

    List deployments for an app, or a deployment slot.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/deployments'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_deployments_slot(client):
    """Test case for web_apps_list_deployments_slot

    List deployments for an app, or a deployment slot.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/deployments'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_domain_ownership_identifiers(client):
    """Test case for web_apps_list_domain_ownership_identifiers

    Lists ownership identifiers for domain associated with web app.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/domainOwnershipIdentifiers'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_domain_ownership_identifiers_slot(client):
    """Test case for web_apps_list_domain_ownership_identifiers_slot

    Lists ownership identifiers for domain associated with web app.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/domainOwnershipIdentifiers'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_function_secrets(client):
    """Test case for web_apps_list_function_secrets

    Get function secrets for a function in a web site, or a deployment slot.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/functions/{function_name}/listsecrets'.format(resource_group_name='resource_group_name_example', name='name_example', function_name='function_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_function_secrets_slot(client):
    """Test case for web_apps_list_function_secrets_slot

    Get function secrets for a function in a web site, or a deployment slot.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/functions/{function_name}/listsecrets'.format(resource_group_name='resource_group_name_example', name='name_example', function_name='function_name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_functions(client):
    """Test case for web_apps_list_functions

    List the functions for a web site, or a deployment slot.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/functions'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_host_name_bindings(client):
    """Test case for web_apps_list_host_name_bindings

    Get hostname bindings for an app or a deployment slot.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/hostNameBindings'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_host_name_bindings_slot(client):
    """Test case for web_apps_list_host_name_bindings_slot

    Get hostname bindings for an app or a deployment slot.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/hostNameBindings'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_hybrid_connection_keys(client):
    """Test case for web_apps_list_hybrid_connection_keys

    Gets the send key name and value for a Hybrid Connection.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/hybridConnectionNamespaces/{namespace_name}/relays/{relay_name}/listKeys'.format(resource_group_name='resource_group_name_example', name='name_example', namespace_name='namespace_name_example', relay_name='relay_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_hybrid_connection_keys_slot(client):
    """Test case for web_apps_list_hybrid_connection_keys_slot

    Gets the send key name and value for a Hybrid Connection.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/hybridConnectionNamespaces/{namespace_name}/relays/{relay_name}/listKeys'.format(resource_group_name='resource_group_name_example', name='name_example', namespace_name='namespace_name_example', relay_name='relay_name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_hybrid_connections(client):
    """Test case for web_apps_list_hybrid_connections

    Retrieves all Service Bus Hybrid Connections used by this Web App.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/hybridConnectionRelays'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_hybrid_connections_slot(client):
    """Test case for web_apps_list_hybrid_connections_slot

    Retrieves all Service Bus Hybrid Connections used by this Web App.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/hybridConnectionRelays'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_instance_functions_slot(client):
    """Test case for web_apps_list_instance_functions_slot

    List the functions for a web site, or a deployment slot.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/functions'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_instance_identifiers(client):
    """Test case for web_apps_list_instance_identifiers

    Gets all scale-out instances of an app.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/instances'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_instance_identifiers_slot(client):
    """Test case for web_apps_list_instance_identifiers_slot

    Gets all scale-out instances of an app.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/instances'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_instance_process_modules(client):
    """Test case for web_apps_list_instance_process_modules

    List module information for a process by its ID for a specific scaled-out instance in a web site.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/instances/{instance_id}/processes/{process_id}/modules'.format(resource_group_name='resource_group_name_example', name='name_example', process_id='process_id_example', instance_id='instance_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_instance_process_modules_slot(client):
    """Test case for web_apps_list_instance_process_modules_slot

    List module information for a process by its ID for a specific scaled-out instance in a web site.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/instances/{instance_id}/processes/{process_id}/modules'.format(resource_group_name='resource_group_name_example', name='name_example', process_id='process_id_example', slot='slot_example', instance_id='instance_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_instance_process_threads(client):
    """Test case for web_apps_list_instance_process_threads

    List the threads in a process by its ID for a specific scaled-out instance in a web site.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/instances/{instance_id}/processes/{process_id}/threads'.format(resource_group_name='resource_group_name_example', name='name_example', process_id='process_id_example', instance_id='instance_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_instance_process_threads_slot(client):
    """Test case for web_apps_list_instance_process_threads_slot

    List the threads in a process by its ID for a specific scaled-out instance in a web site.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/instances/{instance_id}/processes/{process_id}/threads'.format(resource_group_name='resource_group_name_example', name='name_example', process_id='process_id_example', slot='slot_example', instance_id='instance_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_instance_processes(client):
    """Test case for web_apps_list_instance_processes

    Get list of processes for a web site, or a deployment slot, or for a specific scaled-out instance in a web site.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/instances/{instance_id}/processes'.format(resource_group_name='resource_group_name_example', name='name_example', instance_id='instance_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_instance_processes_slot(client):
    """Test case for web_apps_list_instance_processes_slot

    Get list of processes for a web site, or a deployment slot, or for a specific scaled-out instance in a web site.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/instances/{instance_id}/processes'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', instance_id='instance_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_metadata(client):
    """Test case for web_apps_list_metadata

    Gets the metadata of an app.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/config/metadata/list'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_metadata_slot(client):
    """Test case for web_apps_list_metadata_slot

    Gets the metadata of an app.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/metadata/list'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_metric_definitions(client):
    """Test case for web_apps_list_metric_definitions

    Gets all metric definitions of an app (or deployment slot, if specified).
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/metricdefinitions'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_metric_definitions_slot(client):
    """Test case for web_apps_list_metric_definitions_slot

    Gets all metric definitions of an app (or deployment slot, if specified).
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/metricdefinitions'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_metrics(client):
    """Test case for web_apps_list_metrics

    Gets performance metrics of an app (or deployment slot, if specified).
    """
    params = [('details', True),
                    ('$filter', 'filter_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/metrics'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_metrics_slot(client):
    """Test case for web_apps_list_metrics_slot

    Gets performance metrics of an app (or deployment slot, if specified).
    """
    params = [('details', True),
                    ('$filter', 'filter_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/metrics'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_network_features(client):
    """Test case for web_apps_list_network_features

    Gets all network features used by the app (or deployment slot, if specified).
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/networkFeatures/{view}'.format(resource_group_name='resource_group_name_example', name='name_example', view='view_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_network_features_slot(client):
    """Test case for web_apps_list_network_features_slot

    Gets all network features used by the app (or deployment slot, if specified).
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/networkFeatures/{view}'.format(resource_group_name='resource_group_name_example', name='name_example', view='view_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_perf_mon_counters(client):
    """Test case for web_apps_list_perf_mon_counters

    Gets perfmon counters for web app.
    """
    params = [('$filter', 'filter_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/perfcounters'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_perf_mon_counters_slot(client):
    """Test case for web_apps_list_perf_mon_counters_slot

    Gets perfmon counters for web app.
    """
    params = [('$filter', 'filter_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/perfcounters'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_premier_add_ons(client):
    """Test case for web_apps_list_premier_add_ons

    Gets the premier add-ons of an app.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/premieraddons'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_premier_add_ons_slot(client):
    """Test case for web_apps_list_premier_add_ons_slot

    Gets the premier add-ons of an app.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/premieraddons'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_process_modules(client):
    """Test case for web_apps_list_process_modules

    List module information for a process by its ID for a specific scaled-out instance in a web site.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/processes/{process_id}/modules'.format(resource_group_name='resource_group_name_example', name='name_example', process_id='process_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_process_modules_slot(client):
    """Test case for web_apps_list_process_modules_slot

    List module information for a process by its ID for a specific scaled-out instance in a web site.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/processes/{process_id}/modules'.format(resource_group_name='resource_group_name_example', name='name_example', process_id='process_id_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_process_threads(client):
    """Test case for web_apps_list_process_threads

    List the threads in a process by its ID for a specific scaled-out instance in a web site.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/processes/{process_id}/threads'.format(resource_group_name='resource_group_name_example', name='name_example', process_id='process_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_process_threads_slot(client):
    """Test case for web_apps_list_process_threads_slot

    List the threads in a process by its ID for a specific scaled-out instance in a web site.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/processes/{process_id}/threads'.format(resource_group_name='resource_group_name_example', name='name_example', process_id='process_id_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_processes(client):
    """Test case for web_apps_list_processes

    Get list of processes for a web site, or a deployment slot, or for a specific scaled-out instance in a web site.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/processes'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_processes_slot(client):
    """Test case for web_apps_list_processes_slot

    Get list of processes for a web site, or a deployment slot, or for a specific scaled-out instance in a web site.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/processes'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_public_certificates(client):
    """Test case for web_apps_list_public_certificates

    Get public certificates for an app or a deployment slot.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/publicCertificates'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_public_certificates_slot(client):
    """Test case for web_apps_list_public_certificates_slot

    Get public certificates for an app or a deployment slot.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/publicCertificates'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_publishing_credentials(client):
    """Test case for web_apps_list_publishing_credentials

    Gets the Git/FTP publishing credentials of an app.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/config/publishingcredentials/list'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_publishing_credentials_slot(client):
    """Test case for web_apps_list_publishing_credentials_slot

    Gets the Git/FTP publishing credentials of an app.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/publishingcredentials/list'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_publishing_profile_xml_with_secrets(client):
    """Test case for web_apps_list_publishing_profile_xml_with_secrets

    Gets the publishing profile for an app (or deployment slot, if specified).
    """
    publishing_profile_options = {"format":"FileZilla3"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/xml',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/publishxml'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=publishing_profile_options,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_publishing_profile_xml_with_secrets_slot(client):
    """Test case for web_apps_list_publishing_profile_xml_with_secrets_slot

    Gets the publishing profile for an app (or deployment slot, if specified).
    """
    publishing_profile_options = {"format":"FileZilla3"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/xml',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/publishxml'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=publishing_profile_options,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_relay_service_connections(client):
    """Test case for web_apps_list_relay_service_connections

    Gets hybrid connections configured for an app (or deployment slot, if specified).
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/hybridconnection'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_relay_service_connections_slot(client):
    """Test case for web_apps_list_relay_service_connections_slot

    Gets hybrid connections configured for an app (or deployment slot, if specified).
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/hybridconnection'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_site_extensions(client):
    """Test case for web_apps_list_site_extensions

    Get list of site extensions for a web site, or a deployment slot.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/siteextensions'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_site_extensions_slot(client):
    """Test case for web_apps_list_site_extensions_slot

    Get list of site extensions for a web site, or a deployment slot.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/siteextensions'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_site_push_settings(client):
    """Test case for web_apps_list_site_push_settings

    Gets the Push settings associated with web app.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/config/pushsettings/list'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_site_push_settings_slot(client):
    """Test case for web_apps_list_site_push_settings_slot

    Gets the Push settings associated with web app.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/pushsettings/list'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_slot_configuration_names(client):
    """Test case for web_apps_list_slot_configuration_names

    Gets the names of app settings and connection strings that stick to the slot (not swapped).
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/config/slotConfigNames'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_slot_differences_from_production(client):
    """Test case for web_apps_list_slot_differences_from_production

    Get the difference in configuration settings between two web app slots.
    """
    slot_swap_entity = {"preserveVnet":True,"targetSlot":"targetSlot"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slotsdiffs'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=slot_swap_entity,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_slot_differences_slot(client):
    """Test case for web_apps_list_slot_differences_slot

    Get the difference in configuration settings between two web app slots.
    """
    slot_swap_entity = {"preserveVnet":True,"targetSlot":"targetSlot"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/slotsdiffs'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=slot_swap_entity,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_slots(client):
    """Test case for web_apps_list_slots

    Gets an app's deployment slots.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_snapshots(client):
    """Test case for web_apps_list_snapshots

    Returns all Snapshots to the user.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/snapshots'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_snapshots_slot(client):
    """Test case for web_apps_list_snapshots_slot

    Returns all Snapshots to the user.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/snapshots'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_sync_function_triggers(client):
    """Test case for web_apps_list_sync_function_triggers

    This is to allow calling via powershell and ARM template.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/listsyncfunctiontriggerstatus'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_sync_function_triggers_slot(client):
    """Test case for web_apps_list_sync_function_triggers_slot

    This is to allow calling via powershell and ARM template.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/listsyncfunctiontriggerstatus'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_triggered_web_job_history(client):
    """Test case for web_apps_list_triggered_web_job_history

    List a triggered web job's history for an app, or a deployment slot.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/triggeredwebjobs/{web_job_name}/history'.format(resource_group_name='resource_group_name_example', name='name_example', web_job_name='web_job_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_triggered_web_job_history_slot(client):
    """Test case for web_apps_list_triggered_web_job_history_slot

    List a triggered web job's history for an app, or a deployment slot.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/triggeredwebjobs/{web_job_name}/history'.format(resource_group_name='resource_group_name_example', name='name_example', web_job_name='web_job_name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_triggered_web_jobs(client):
    """Test case for web_apps_list_triggered_web_jobs

    List triggered web jobs for an app, or a deployment slot.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/triggeredwebjobs'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_triggered_web_jobs_slot(client):
    """Test case for web_apps_list_triggered_web_jobs_slot

    List triggered web jobs for an app, or a deployment slot.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/triggeredwebjobs'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_usages(client):
    """Test case for web_apps_list_usages

    Gets the quota usage information of an app (or deployment slot, if specified).
    """
    params = [('$filter', 'filter_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/usages'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_usages_slot(client):
    """Test case for web_apps_list_usages_slot

    Gets the quota usage information of an app (or deployment slot, if specified).
    """
    params = [('$filter', 'filter_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/usages'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_vnet_connections(client):
    """Test case for web_apps_list_vnet_connections

    Gets the virtual networks the app (or deployment slot) is connected to.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/virtualNetworkConnections'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_vnet_connections_slot(client):
    """Test case for web_apps_list_vnet_connections_slot

    Gets the virtual networks the app (or deployment slot) is connected to.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/virtualNetworkConnections'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_web_jobs(client):
    """Test case for web_apps_list_web_jobs

    List webjobs for an app, or a deployment slot.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/webjobs'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_list_web_jobs_slot(client):
    """Test case for web_apps_list_web_jobs_slot

    List webjobs for an app, or a deployment slot.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/webjobs'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_migrate_my_sql(client):
    """Test case for web_apps_migrate_my_sql

    Migrates a local (in-app) MySql database to a remote MySql database.
    """
    migration_request_envelope = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/migratemysql'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=migration_request_envelope,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_migrate_storage(client):
    """Test case for web_apps_migrate_storage

    Restores a web app.
    """
    migration_options = {"properties":"{}"}
    params = [('subscriptionName', 'subscription_name_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/migrate'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=migration_options,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_recover(client):
    """Test case for web_apps_recover

    Recovers a web app to a previous snapshot.
    """
    recovery_entity = openapi_server.WebAppsRecoverRequest()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/recover'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=recovery_entity,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_recover_site_configuration_snapshot(client):
    """Test case for web_apps_recover_site_configuration_snapshot

    Reverts the configuration of an app to a previous snapshot.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/config/web/snapshots/{snapshot_id}/recover'.format(resource_group_name='resource_group_name_example', name='name_example', snapshot_id='snapshot_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_recover_site_configuration_snapshot_slot(client):
    """Test case for web_apps_recover_site_configuration_snapshot_slot

    Reverts the configuration of an app to a previous snapshot.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/web/snapshots/{snapshot_id}/recover'.format(resource_group_name='resource_group_name_example', name='name_example', snapshot_id='snapshot_id_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_recover_slot(client):
    """Test case for web_apps_recover_slot

    Recovers a web app to a previous snapshot.
    """
    recovery_entity = openapi_server.WebAppsRecoverRequest()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/recover'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=recovery_entity,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_reset_production_slot_config(client):
    """Test case for web_apps_reset_production_slot_config

    Resets the configuration settings of the current slot if they were previously modified by calling the API with POST.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/resetSlotConfig'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_reset_slot_configuration_slot(client):
    """Test case for web_apps_reset_slot_configuration_slot

    Resets the configuration settings of the current slot if they were previously modified by calling the API with POST.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/resetSlotConfig'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_restart(client):
    """Test case for web_apps_restart

    Restarts an app (or deployment slot, if specified).
    """
    params = [('softRestart', True),
                    ('synchronous', True),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/restart'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_restart_slot(client):
    """Test case for web_apps_restart_slot

    Restarts an app (or deployment slot, if specified).
    """
    params = [('softRestart', True),
                    ('synchronous', True),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/restart'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_restore(client):
    """Test case for web_apps_restore

    Restores a specific backup to another app (or deployment slot, if specified).
    """
    request = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/backups/{backup_id}/restore'.format(resource_group_name='resource_group_name_example', name='name_example', backup_id='backup_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_restore_slot(client):
    """Test case for web_apps_restore_slot

    Restores a specific backup to another app (or deployment slot, if specified).
    """
    request = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/backups/{backup_id}/restore'.format(resource_group_name='resource_group_name_example', name='name_example', backup_id='backup_id_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_run_triggered_web_job(client):
    """Test case for web_apps_run_triggered_web_job

    Run a triggered web job for an app, or a deployment slot.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/triggeredwebjobs/{web_job_name}/run'.format(resource_group_name='resource_group_name_example', name='name_example', web_job_name='web_job_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_run_triggered_web_job_slot(client):
    """Test case for web_apps_run_triggered_web_job_slot

    Run a triggered web job for an app, or a deployment slot.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/triggeredwebjobs/{web_job_name}/run'.format(resource_group_name='resource_group_name_example', name='name_example', web_job_name='web_job_name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_start(client):
    """Test case for web_apps_start

    Starts an app (or deployment slot, if specified).
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/start'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_start_continuous_web_job(client):
    """Test case for web_apps_start_continuous_web_job

    Start a continuous web job for an app, or a deployment slot.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/continuouswebjobs/{web_job_name}/start'.format(resource_group_name='resource_group_name_example', name='name_example', web_job_name='web_job_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_start_continuous_web_job_slot(client):
    """Test case for web_apps_start_continuous_web_job_slot

    Start a continuous web job for an app, or a deployment slot.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/continuouswebjobs/{web_job_name}/start'.format(resource_group_name='resource_group_name_example', name='name_example', web_job_name='web_job_name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_start_slot(client):
    """Test case for web_apps_start_slot

    Starts an app (or deployment slot, if specified).
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/start'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_start_web_site_network_trace(client):
    """Test case for web_apps_start_web_site_network_trace

    Start capturing network packets for the site.
    """
    params = [('durationInSeconds', 56),
                    ('maxFrameLength', 56),
                    ('sasUrl', 'sas_url_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/networkTrace/start'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_start_web_site_network_trace_slot(client):
    """Test case for web_apps_start_web_site_network_trace_slot

    Start capturing network packets for the site.
    """
    params = [('durationInSeconds', 56),
                    ('maxFrameLength', 56),
                    ('sasUrl', 'sas_url_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/networkTrace/start'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_stop(client):
    """Test case for web_apps_stop

    Stops an app (or deployment slot, if specified).
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/stop'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_stop_continuous_web_job(client):
    """Test case for web_apps_stop_continuous_web_job

    Stop a continuous web job for an app, or a deployment slot.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/continuouswebjobs/{web_job_name}/stop'.format(resource_group_name='resource_group_name_example', name='name_example', web_job_name='web_job_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_stop_continuous_web_job_slot(client):
    """Test case for web_apps_stop_continuous_web_job_slot

    Stop a continuous web job for an app, or a deployment slot.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/continuouswebjobs/{web_job_name}/stop'.format(resource_group_name='resource_group_name_example', name='name_example', web_job_name='web_job_name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_stop_slot(client):
    """Test case for web_apps_stop_slot

    Stops an app (or deployment slot, if specified).
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/stop'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_stop_web_site_network_trace(client):
    """Test case for web_apps_stop_web_site_network_trace

    Stop ongoing capturing network packets for the site.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/networkTrace/stop'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_stop_web_site_network_trace_slot(client):
    """Test case for web_apps_stop_web_site_network_trace_slot

    Stop ongoing capturing network packets for the site.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/networkTrace/stop'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_swap_slot_slot(client):
    """Test case for web_apps_swap_slot_slot

    Swaps two deployment slots of an app.
    """
    slot_swap_entity = {"preserveVnet":True,"targetSlot":"targetSlot"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/slotsswap'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=slot_swap_entity,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_swap_slot_with_production(client):
    """Test case for web_apps_swap_slot_with_production

    Swaps two deployment slots of an app.
    """
    slot_swap_entity = {"preserveVnet":True,"targetSlot":"targetSlot"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slotsswap'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=slot_swap_entity,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_sync_function_triggers(client):
    """Test case for web_apps_sync_function_triggers

    Syncs function trigger metadata to the scale controller
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/syncfunctiontriggers'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_sync_function_triggers_slot(client):
    """Test case for web_apps_sync_function_triggers_slot

    Syncs function trigger metadata to the scale controller
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/syncfunctiontriggers'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_sync_repository(client):
    """Test case for web_apps_sync_repository

    Sync web app repository.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/sync'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_sync_repository_slot(client):
    """Test case for web_apps_sync_repository_slot

    Sync web app repository.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/sync'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_update(client):
    """Test case for web_apps_update

    Creates a new web, mobile, or API app in an existing resource group, or updates an existing app.
    """
    site_envelope = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=site_envelope,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_update_application_settings(client):
    """Test case for web_apps_update_application_settings

    Replaces the application settings of an app.
    """
    app_settings = {"properties":{"key":"properties"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/config/appsettings'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=app_settings,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_update_application_settings_slot(client):
    """Test case for web_apps_update_application_settings_slot

    Replaces the application settings of an app.
    """
    app_settings = {"properties":{"key":"properties"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/appsettings'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=app_settings,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_update_auth_settings(client):
    """Test case for web_apps_update_auth_settings

    Updates the Authentication / Authorization settings associated with web app.
    """
    site_auth_settings = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/config/authsettings'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=site_auth_settings,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_update_auth_settings_slot(client):
    """Test case for web_apps_update_auth_settings_slot

    Updates the Authentication / Authorization settings associated with web app.
    """
    site_auth_settings = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/authsettings'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=site_auth_settings,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_update_backup_configuration(client):
    """Test case for web_apps_update_backup_configuration

    Updates the backup configuration of an app.
    """
    request = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/config/backup'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_update_backup_configuration_slot(client):
    """Test case for web_apps_update_backup_configuration_slot

    Updates the backup configuration of an app.
    """
    request = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/backup'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_update_configuration(client):
    """Test case for web_apps_update_configuration

    Updates the configuration of an app.
    """
    site_config = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/config/web'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=site_config,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_update_configuration_slot(client):
    """Test case for web_apps_update_configuration_slot

    Updates the configuration of an app.
    """
    site_config = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/web'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=site_config,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_update_connection_strings(client):
    """Test case for web_apps_update_connection_strings

    Replaces the connection strings of an app.
    """
    connection_strings = {"properties":{"key":{"type":"MySql","value":"value"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/config/connectionstrings'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=connection_strings,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_update_connection_strings_slot(client):
    """Test case for web_apps_update_connection_strings_slot

    Replaces the connection strings of an app.
    """
    connection_strings = {"properties":{"key":{"type":"MySql","value":"value"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/connectionstrings'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=connection_strings,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_update_diagnostic_logs_config(client):
    """Test case for web_apps_update_diagnostic_logs_config

    Updates the logging configuration of an app.
    """
    site_logs_config = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/config/logs'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=site_logs_config,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_update_diagnostic_logs_config_slot(client):
    """Test case for web_apps_update_diagnostic_logs_config_slot

    Updates the logging configuration of an app.
    """
    site_logs_config = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/logs'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=site_logs_config,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_update_domain_ownership_identifier(client):
    """Test case for web_apps_update_domain_ownership_identifier

    Creates a domain ownership identifier for web app, or updates an existing ownership identifier.
    """
    domain_ownership_identifier = openapi_server.WebAppsGetDomainOwnershipIdentifier200Response()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/domainOwnershipIdentifiers/{domain_ownership_identifier_name}'.format(resource_group_name='resource_group_name_example', name='name_example', domain_ownership_identifier_name='domain_ownership_identifier_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=domain_ownership_identifier,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_update_domain_ownership_identifier_slot(client):
    """Test case for web_apps_update_domain_ownership_identifier_slot

    Creates a domain ownership identifier for web app, or updates an existing ownership identifier.
    """
    domain_ownership_identifier = openapi_server.WebAppsGetDomainOwnershipIdentifier200Response()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/domainOwnershipIdentifiers/{domain_ownership_identifier_name}'.format(resource_group_name='resource_group_name_example', name='name_example', domain_ownership_identifier_name='domain_ownership_identifier_name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=domain_ownership_identifier,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_update_hybrid_connection(client):
    """Test case for web_apps_update_hybrid_connection

    Creates a new Hybrid Connection using a Service Bus relay.
    """
    connection_envelope = openapi_server.WebAppsGetHybridConnection200Response()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/hybridConnectionNamespaces/{namespace_name}/relays/{relay_name}'.format(resource_group_name='resource_group_name_example', name='name_example', namespace_name='namespace_name_example', relay_name='relay_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=connection_envelope,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_update_hybrid_connection_slot(client):
    """Test case for web_apps_update_hybrid_connection_slot

    Creates a new Hybrid Connection using a Service Bus relay.
    """
    connection_envelope = openapi_server.WebAppsGetHybridConnection200Response()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/hybridConnectionNamespaces/{namespace_name}/relays/{relay_name}'.format(resource_group_name='resource_group_name_example', name='name_example', namespace_name='namespace_name_example', relay_name='relay_name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=connection_envelope,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_update_metadata(client):
    """Test case for web_apps_update_metadata

    Replaces the metadata of an app.
    """
    metadata = {"properties":{"key":"properties"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/config/metadata'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=metadata,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_update_metadata_slot(client):
    """Test case for web_apps_update_metadata_slot

    Replaces the metadata of an app.
    """
    metadata = {"properties":{"key":"properties"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/metadata'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=metadata,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_update_relay_service_connection(client):
    """Test case for web_apps_update_relay_service_connection

    Creates a new hybrid connection configuration (PUT), or updates an existing one (PATCH).
    """
    connection_envelope = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/hybridconnection/{entity_name}'.format(resource_group_name='resource_group_name_example', name='name_example', entity_name='entity_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=connection_envelope,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_update_relay_service_connection_slot(client):
    """Test case for web_apps_update_relay_service_connection_slot

    Creates a new hybrid connection configuration (PUT), or updates an existing one (PATCH).
    """
    connection_envelope = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/hybridconnection/{entity_name}'.format(resource_group_name='resource_group_name_example', name='name_example', entity_name='entity_name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=connection_envelope,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_update_site_push_settings(client):
    """Test case for web_apps_update_site_push_settings

    Updates the Push settings associated with web app.
    """
    push_settings = openapi_server.WebAppsUpdateSitePushSettingsRequest()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/config/pushsettings'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=push_settings,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_update_site_push_settings_slot(client):
    """Test case for web_apps_update_site_push_settings_slot

    Updates the Push settings associated with web app.
    """
    push_settings = openapi_server.WebAppsUpdateSitePushSettingsRequest()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/pushsettings'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=push_settings,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_update_slot(client):
    """Test case for web_apps_update_slot

    Creates a new web, mobile, or API app in an existing resource group, or updates an existing app.
    """
    site_envelope = {"properties":"{}"}
    params = [('skipDnsRegistration', True),
                    ('skipCustomDomainVerification', True),
                    ('forceDnsRegistration', True),
                    ('ttlInSeconds', 'ttl_in_seconds_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=site_envelope,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_update_slot_configuration_names(client):
    """Test case for web_apps_update_slot_configuration_names

    Updates the names of application settings and connection string that remain with the slot during swap operation.
    """
    slot_config_names = {"properties":{"connectionStringNames":["connectionStringNames","connectionStringNames"],"appSettingNames":["appSettingNames","appSettingNames"]}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/config/slotConfigNames'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=slot_config_names,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_update_source_control(client):
    """Test case for web_apps_update_source_control

    Updates the source control configuration of an app.
    """
    site_source_control = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/sourcecontrols/web'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=site_source_control,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_update_source_control_slot(client):
    """Test case for web_apps_update_source_control_slot

    Updates the source control configuration of an app.
    """
    site_source_control = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/sourcecontrols/web'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=site_source_control,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_update_vnet_connection(client):
    """Test case for web_apps_update_vnet_connection

    Adds a Virtual Network connection to an app or slot (PUT) or updates the connection properties (PATCH).
    """
    connection_envelope = openapi_server.WebAppsGetVnetConnectionSlot200Response()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/virtualNetworkConnections/{vnet_name}'.format(resource_group_name='resource_group_name_example', name='name_example', vnet_name='vnet_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=connection_envelope,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_update_vnet_connection_gateway(client):
    """Test case for web_apps_update_vnet_connection_gateway

    Adds a gateway to a connected Virtual Network (PUT) or updates it (PATCH).
    """
    connection_envelope = openapi_server.WebAppsGetVnetConnectionGatewaySlot200Response()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/virtualNetworkConnections/{vnet_name}/gateways/{gateway_name}'.format(resource_group_name='resource_group_name_example', name='name_example', vnet_name='vnet_name_example', gateway_name='gateway_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=connection_envelope,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_update_vnet_connection_gateway_slot(client):
    """Test case for web_apps_update_vnet_connection_gateway_slot

    Adds a gateway to a connected Virtual Network (PUT) or updates it (PATCH).
    """
    connection_envelope = openapi_server.WebAppsGetVnetConnectionGatewaySlot200Response()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/virtualNetworkConnections/{vnet_name}/gateways/{gateway_name}'.format(resource_group_name='resource_group_name_example', name='name_example', vnet_name='vnet_name_example', gateway_name='gateway_name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=connection_envelope,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_apps_update_vnet_connection_slot(client):
    """Test case for web_apps_update_vnet_connection_slot

    Adds a Virtual Network connection to an app or slot (PUT) or updates the connection properties (PATCH).
    """
    connection_envelope = openapi_server.WebAppsGetVnetConnectionSlot200Response()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/virtualNetworkConnections/{vnet_name}'.format(resource_group_name='resource_group_name_example', name='name_example', vnet_name='vnet_name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=connection_envelope,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

