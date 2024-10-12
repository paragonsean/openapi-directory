# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.app_version_setting_object import AppVersionSettingObject
from openapi_server.models.application_create_object import ApplicationCreateObject
from openapi_server.models.application_info_response import ApplicationInfoResponse
from openapi_server.models.application_publish_object import ApplicationPublishObject
from openapi_server.models.application_setting_update_object import ApplicationSettingUpdateObject
from openapi_server.models.application_settings import ApplicationSettings
from openapi_server.models.application_update_object import ApplicationUpdateObject
from openapi_server.models.available_culture import AvailableCulture
from openapi_server.models.available_prebuilt_entity_model import AvailablePrebuiltEntityModel
from openapi_server.models.azure_account_info_object import AzureAccountInfoObject
from openapi_server.models.batch_label_example import BatchLabelExample
from openapi_server.models.closed_list_entity_extractor import ClosedListEntityExtractor
from openapi_server.models.closed_list_model_create_object import ClosedListModelCreateObject
from openapi_server.models.closed_list_model_patch_object import ClosedListModelPatchObject
from openapi_server.models.closed_list_model_update_object import ClosedListModelUpdateObject
from openapi_server.models.collaborators_array import CollaboratorsArray
from openapi_server.models.composite_entity_extractor import CompositeEntityExtractor
from openapi_server.models.composite_entity_model import CompositeEntityModel
from openapi_server.models.custom_prebuilt_model import CustomPrebuiltModel
from openapi_server.models.enqueue_training_response import EnqueueTrainingResponse
from openapi_server.models.entities_suggestion_example import EntitiesSuggestionExample
from openapi_server.models.entity_extractor import EntityExtractor
from openapi_server.models.entity_role import EntityRole
from openapi_server.models.entity_role_create_object import EntityRoleCreateObject
from openapi_server.models.entity_role_update_object import EntityRoleUpdateObject
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.example_label_object import ExampleLabelObject
from openapi_server.models.explicit_list_item import ExplicitListItem
from openapi_server.models.explicit_list_item_create_object import ExplicitListItemCreateObject
from openapi_server.models.explicit_list_item_update_object import ExplicitListItemUpdateObject
from openapi_server.models.features_response_object import FeaturesResponseObject
from openapi_server.models.hierarchical_child_entity import HierarchicalChildEntity
from openapi_server.models.hierarchical_entity_extractor import HierarchicalEntityExtractor
from openapi_server.models.hierarchical_entity_model import HierarchicalEntityModel
from openapi_server.models.intent_classifier import IntentClassifier
from openapi_server.models.intents_suggestion_example import IntentsSuggestionExample
from openapi_server.models.label_example_response import LabelExampleResponse
from openapi_server.models.label_text_object import LabelTextObject
from openapi_server.models.labeled_utterance import LabeledUtterance
from openapi_server.models.luis_app import LuisApp
from openapi_server.models.model_add_composite_entity_child_request import ModelAddCompositeEntityChildRequest
from openapi_server.models.model_create_object import ModelCreateObject
from openapi_server.models.model_info_response import ModelInfoResponse
from openapi_server.models.model_training_info import ModelTrainingInfo
from openapi_server.models.model_update_object import ModelUpdateObject
from openapi_server.models.operation_status import OperationStatus
from openapi_server.models.pattern_any_entity_extractor import PatternAnyEntityExtractor
from openapi_server.models.pattern_any_model_create_object import PatternAnyModelCreateObject
from openapi_server.models.pattern_any_model_update_object import PatternAnyModelUpdateObject
from openapi_server.models.pattern_create_object import PatternCreateObject
from openapi_server.models.pattern_feature_info import PatternFeatureInfo
from openapi_server.models.pattern_rule_create_object import PatternRuleCreateObject
from openapi_server.models.pattern_rule_info import PatternRuleInfo
from openapi_server.models.pattern_rule_update_object import PatternRuleUpdateObject
from openapi_server.models.pattern_update_object import PatternUpdateObject
from openapi_server.models.personal_assistants_response import PersonalAssistantsResponse
from openapi_server.models.phrase_list_feature_info import PhraseListFeatureInfo
from openapi_server.models.phraselist_create_object import PhraselistCreateObject
from openapi_server.models.phraselist_update_object import PhraselistUpdateObject
from openapi_server.models.prebuilt_domain import PrebuiltDomain
from openapi_server.models.prebuilt_domain_create_base_object import PrebuiltDomainCreateBaseObject
from openapi_server.models.prebuilt_domain_create_object import PrebuiltDomainCreateObject
from openapi_server.models.prebuilt_domain_model_create_object import PrebuiltDomainModelCreateObject
from openapi_server.models.prebuilt_entity_extractor import PrebuiltEntityExtractor
from openapi_server.models.production_or_staging_endpoint_info import ProductionOrStagingEndpointInfo
from openapi_server.models.publish_setting_update_object import PublishSettingUpdateObject
from openapi_server.models.publish_settings import PublishSettings
from openapi_server.models.regex_entity_extractor import RegexEntityExtractor
from openapi_server.models.regex_model_create_object import RegexModelCreateObject
from openapi_server.models.regex_model_update_object import RegexModelUpdateObject
from openapi_server.models.task_update_object import TaskUpdateObject
from openapi_server.models.user_access_list import UserAccessList
from openapi_server.models.user_collaborator import UserCollaborator
from openapi_server.models.version_info import VersionInfo
from openapi_server.models.word_list_base_update_object import WordListBaseUpdateObject
from openapi_server.models.word_list_object import WordListObject


pytestmark = pytest.mark.asyncio

async def test_apps_add(client):
    """Test case for apps_add

    
    """
    application_create_object = {"usageScenario":"usageScenario","culture":"culture","domain":"domain","name":"name","description":"description","initialVersionId":"initialVersionId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/apps/',
        headers=headers,
        json=application_create_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_add_custom_prebuilt_domain(client):
    """Test case for apps_add_custom_prebuilt_domain

    
    """
    prebuilt_domain_create_object = {"culture":"culture","domainName":"domainName"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/apps/customprebuiltdomains',
        headers=headers,
        json=prebuilt_domain_create_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_delete(client):
    """Test case for apps_delete

    
    """
    params = [('force', False)]
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/apps/{app_id}'.format(app_id='app_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_download_query_logs(client):
    """Test case for apps_download_query_logs

    
    """
    headers = { 
        'Accept': 'application/octet-stream',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/{app_id}/querylogs'.format(app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_get(client):
    """Test case for apps_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/{app_id}'.format(app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_get_publish_settings(client):
    """Test case for apps_get_publish_settings

    
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/{app_id}/publishsettings'.format(app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_get_settings(client):
    """Test case for apps_get_settings

    
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/{app_id}/settings'.format(app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_import(client):
    """Test case for apps_import

    
    """
    luis_app = {"utterances":[{"entities":[{"role":"role","entity":"entity","startPos":6,"endPos":0},{"role":"role","entity":"entity","startPos":6,"endPos":0}],"text":"text","intent":"intent"},{"entities":[{"role":"role","entity":"entity","startPos":6,"endPos":0},{"role":"role","entity":"entity","startPos":6,"endPos":0}],"text":"text","intent":"intent"}],"intents":[{"children":["children","children"],"roles":["roles","roles"],"name":"name","inherits":{"domain_name":"domain_name","model_name":"model_name"}},{"children":["children","children"],"roles":["roles","roles"],"name":"name","inherits":{"domain_name":"domain_name","model_name":"model_name"}}],"prebuiltEntities":[{"roles":["roles","roles"],"name":"name"},{"roles":["roles","roles"],"name":"name"}],"patterns":[{"pattern":"pattern","intent":"intent"},{"pattern":"pattern","intent":"intent"}],"composites":[{"children":["children","children"],"roles":["roles","roles"],"name":"name","inherits":{"domain_name":"domain_name","model_name":"model_name"}},{"children":["children","children"],"roles":["roles","roles"],"name":"name","inherits":{"domain_name":"domain_name","model_name":"model_name"}}],"versionId":"versionId","closedLists":[{"roles":["roles","roles"],"name":"name","subLists":[{"canonicalForm":"canonicalForm","list":["list","list"]},{"canonicalForm":"canonicalForm","list":["list","list"]}]},{"roles":["roles","roles"],"name":"name","subLists":[{"canonicalForm":"canonicalForm","list":["list","list"]},{"canonicalForm":"canonicalForm","list":["list","list"]}]}],"entities":[{"children":["children","children"],"roles":["roles","roles"],"name":"name","inherits":{"domain_name":"domain_name","model_name":"model_name"}},{"children":["children","children"],"roles":["roles","roles"],"name":"name","inherits":{"domain_name":"domain_name","model_name":"model_name"}}],"culture":"culture","regex_entities":[{"roles":["roles","roles"],"name":"name","regexPattern":"regexPattern"},{"roles":["roles","roles"],"name":"name","regexPattern":"regexPattern"}],"patternAnyEntities":[{"explicitList":["explicitList","explicitList"],"roles":["roles","roles"],"name":"name"},{"explicitList":["explicitList","explicitList"],"roles":["roles","roles"],"name":"name"}],"model_features":[{"mode":True,"name":"name","words":"words","activated":True},{"mode":True,"name":"name","words":"words","activated":True}],"name":"name","regex_features":[{"name":"name","pattern":"pattern","activated":True},{"name":"name","pattern":"pattern","activated":True}],"desc":"desc"}
    params = [('appName', 'app_name_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/apps/import',
        headers=headers,
        json=luis_app,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_list(client):
    """Test case for apps_list

    
    """
    params = [('skip', 0),
                    ('take', 100)]
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_list_available_custom_prebuilt_domains(client):
    """Test case for apps_list_available_custom_prebuilt_domains

    
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/customprebuiltdomains',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_list_available_custom_prebuilt_domains_for_culture(client):
    """Test case for apps_list_available_custom_prebuilt_domains_for_culture

    
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/customprebuiltdomains/{culture}'.format(culture='culture_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_list_cortana_endpoints(client):
    """Test case for apps_list_cortana_endpoints

    
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/assistants',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_list_domains(client):
    """Test case for apps_list_domains

    
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/domains',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_list_endpoints(client):
    """Test case for apps_list_endpoints

    
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/{app_id}/endpoints'.format(app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_list_supported_cultures(client):
    """Test case for apps_list_supported_cultures

    
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/cultures',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_list_usage_scenarios(client):
    """Test case for apps_list_usage_scenarios

    
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/usagescenarios',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_package_published_application_as_gzip(client):
    """Test case for apps_package_published_application_as_gzip

    package - Gets published LUIS application package in binary stream GZip format
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/package/{app_id}/slot/{slot_name}/gzip'.format(app_id='app_id_example', slot_name='slot_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_package_trained_application_as_gzip(client):
    """Test case for apps_package_trained_application_as_gzip

    package - Gets trained LUIS application package in binary stream GZip format
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/package/{app_id}/versions/{version_id}/gzip'.format(app_id='app_id_example', version_id='version_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_publish(client):
    """Test case for apps_publish

    
    """
    application_publish_object = {"versionId":"versionId","isStaging":False}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/apps/{app_id}/publish'.format(app_id='app_id_example'),
        headers=headers,
        json=application_publish_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_update(client):
    """Test case for apps_update

    
    """
    application_update_object = {"name":"name","description":"description"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/apps/{app_id}'.format(app_id='app_id_example'),
        headers=headers,
        json=application_update_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_update_publish_settings(client):
    """Test case for apps_update_publish_settings

    
    """
    publish_setting_update_object = {"sentimentAnalysis":True,"speech":True,"spellChecker":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/apps/{app_id}/publishsettings'.format(app_id='app_id_example'),
        headers=headers,
        json=publish_setting_update_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_update_settings(client):
    """Test case for apps_update_settings

    
    """
    application_setting_update_object = {"public":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/apps/{app_id}/settings'.format(app_id='app_id_example'),
        headers=headers,
        json=application_setting_update_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_azure_accounts_assign_to_app(client):
    """Test case for azure_accounts_assign_to_app

    apps - Assign a LUIS Azure account to an application
    """
    azure_account_info_object = {"resourceGroup":"resourceGroup","accountName":"accountName","azureSubscriptionId":"azureSubscriptionId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/apps/{app_id}/azureaccounts'.format(app_id='app_id_example'),
        headers=headers,
        json=azure_account_info_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_azure_accounts_get_assigned(client):
    """Test case for azure_accounts_get_assigned

    apps - Get LUIS Azure accounts assigned to the application
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/{app_id}/azureaccounts'.format(app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_azure_accounts_list_user_luis_accounts(client):
    """Test case for azure_accounts_list_user_luis_accounts

    user - Get LUIS Azure accounts
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/azureaccounts',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_azure_accounts_remove_from_app(client):
    """Test case for azure_accounts_remove_from_app

    apps - Removes an assigned LUIS Azure account from an application
    """
    azure_account_info_object = {"resourceGroup":"resourceGroup","accountName":"accountName","azureSubscriptionId":"azureSubscriptionId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/apps/{app_id}/azureaccounts'.format(app_id='app_id_example'),
        headers=headers,
        json=azure_account_info_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_examples_add(client):
    """Test case for examples_add

    
    """
    example_label_object = {"entityLabels":[{"role":"role","startCharIndex":6,"entityName":"entityName","endCharIndex":0},{"role":"role","startCharIndex":6,"entityName":"entityName","endCharIndex":0}],"intentName":"intentName","text":"text"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/apps/{app_id}/versions/{version_id}/example'.format(app_id='app_id_example', version_id='version_id_example'),
        headers=headers,
        json=example_label_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_examples_batch(client):
    """Test case for examples_batch

    
    """
    example_label_object_array = {"entityLabels":[{"role":"role","startCharIndex":6,"entityName":"entityName","endCharIndex":0},{"role":"role","startCharIndex":6,"entityName":"entityName","endCharIndex":0}],"intentName":"intentName","text":"text"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/apps/{app_id}/versions/{version_id}/examples'.format(app_id='app_id_example', version_id='version_id_example'),
        headers=headers,
        json=example_label_object_array,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_examples_delete(client):
    """Test case for examples_delete

    
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/apps/{app_id}/versions/{version_id}/examples/{example_id}'.format(app_id='app_id_example', version_id='version_id_example', example_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_examples_list(client):
    """Test case for examples_list

    
    """
    params = [('skip', 0),
                    ('take', 100)]
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/{app_id}/versions/{version_id}/examples'.format(app_id='app_id_example', version_id='version_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_features_add_phrase_list(client):
    """Test case for features_add_phrase_list

    
    """
    phraselist_create_object = {"name":"name","isExchangeable":True,"phrases":"phrases"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/apps/{app_id}/versions/{version_id}/phraselists'.format(app_id='app_id_example', version_id='version_id_example'),
        headers=headers,
        json=phraselist_create_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_features_create_pattern_feature(client):
    """Test case for features_create_pattern_feature

    
    """
    pattern_create_object = {"name":"name","pattern":"pattern"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/apps/{app_id}/versions/{version_id}/patterns'.format(app_id='app_id_example', version_id='version_id_example'),
        headers=headers,
        json=pattern_create_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_features_delete_pattern_feature(client):
    """Test case for features_delete_pattern_feature

    
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/apps/{app_id}/versions/{version_id}/patterns/{pattern_id}'.format(app_id='app_id_example', version_id='version_id_example', pattern_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_features_delete_phrase_list(client):
    """Test case for features_delete_phrase_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/apps/{app_id}/versions/{version_id}/phraselists/{phraselist_id}'.format(app_id='app_id_example', version_id='version_id_example', phraselist_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_features_get_pattern_feature_info(client):
    """Test case for features_get_pattern_feature_info

    
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/{app_id}/versions/{version_id}/patterns/{pattern_id}'.format(app_id='app_id_example', version_id='version_id_example', pattern_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_features_get_phrase_list(client):
    """Test case for features_get_phrase_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/{app_id}/versions/{version_id}/phraselists/{phraselist_id}'.format(app_id='app_id_example', version_id='version_id_example', phraselist_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_features_list(client):
    """Test case for features_list

    
    """
    params = [('skip', 0),
                    ('take', 100)]
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/{app_id}/versions/{version_id}/features'.format(app_id='app_id_example', version_id='version_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_features_list_application_version_pattern_features(client):
    """Test case for features_list_application_version_pattern_features

    
    """
    params = [('skip', 0),
                    ('take', 100)]
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/{app_id}/versions/{version_id}/patterns'.format(app_id='app_id_example', version_id='version_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_features_list_phrase_lists(client):
    """Test case for features_list_phrase_lists

    
    """
    params = [('skip', 0),
                    ('take', 100)]
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/{app_id}/versions/{version_id}/phraselists'.format(app_id='app_id_example', version_id='version_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_features_update_pattern_feature(client):
    """Test case for features_update_pattern_feature

    
    """
    pattern_update_object = {"name":"name","pattern":"pattern","isActive":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/apps/{app_id}/versions/{version_id}/patterns/{pattern_id}'.format(app_id='app_id_example', version_id='version_id_example', pattern_id=56),
        headers=headers,
        json=pattern_update_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_features_update_phrase_list(client):
    """Test case for features_update_phrase_list

    
    """
    phraselist_update_object = {"name":"name","isExchangeable":True,"isActive":True,"phrases":"phrases"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/apps/{app_id}/versions/{version_id}/phraselists/{phraselist_id}'.format(app_id='app_id_example', version_id='version_id_example', phraselist_id=56),
        headers=headers,
        json=phraselist_update_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_add_closed_list(client):
    """Test case for model_add_closed_list

    
    """
    closed_list_model_create_object = {"name":"name","subLists":[{"canonicalForm":"canonicalForm","list":["list","list"]},{"canonicalForm":"canonicalForm","list":["list","list"]}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/apps/{app_id}/versions/{version_id}/closedlists'.format(app_id='app_id_example', version_id='version_id_example'),
        headers=headers,
        json=closed_list_model_create_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_add_composite_entity(client):
    """Test case for model_add_composite_entity

    
    """
    composite_model_create_object = {"children":["children","children"],"name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/apps/{app_id}/versions/{version_id}/compositeentities'.format(app_id='app_id_example', version_id='version_id_example'),
        headers=headers,
        json=composite_model_create_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_add_composite_entity_child(client):
    """Test case for model_add_composite_entity_child

    
    """
    composite_child_model_create_object = openapi_server.ModelAddCompositeEntityChildRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/apps/{app_id}/versions/{version_id}/compositeentities/{c_entity_id}/children'.format(app_id='app_id_example', version_id='version_id_example', c_entity_id='c_entity_id_example'),
        headers=headers,
        json=composite_child_model_create_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_add_custom_prebuilt_domain(client):
    """Test case for model_add_custom_prebuilt_domain

    
    """
    prebuilt_domain_object = {"domainName":"domainName"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/apps/{app_id}/versions/{version_id}/customprebuiltdomains'.format(app_id='app_id_example', version_id='version_id_example'),
        headers=headers,
        json=prebuilt_domain_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_add_custom_prebuilt_entity(client):
    """Test case for model_add_custom_prebuilt_entity

    
    """
    prebuilt_domain_model_create_object = {"modelName":"modelName","domainName":"domainName"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/apps/{app_id}/versions/{version_id}/customprebuiltentities'.format(app_id='app_id_example', version_id='version_id_example'),
        headers=headers,
        json=prebuilt_domain_model_create_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_add_custom_prebuilt_intent(client):
    """Test case for model_add_custom_prebuilt_intent

    
    """
    prebuilt_domain_model_create_object = {"modelName":"modelName","domainName":"domainName"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/apps/{app_id}/versions/{version_id}/customprebuiltintents'.format(app_id='app_id_example', version_id='version_id_example'),
        headers=headers,
        json=prebuilt_domain_model_create_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_add_entity(client):
    """Test case for model_add_entity

    
    """
    model_create_object = {"name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/apps/{app_id}/versions/{version_id}/entities'.format(app_id='app_id_example', version_id='version_id_example'),
        headers=headers,
        json=model_create_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_add_explicit_list_item(client):
    """Test case for model_add_explicit_list_item

    Add a new exception to the explicit list for the Pattern.Any entity in a version of the application.
    """
    item = {"explicitListItem":"explicitListItem"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/apps/{app_id}/versions/{version_id}/patternanyentities/{entity_id}/explicitlist'.format(app_id='app_id_example', version_id='version_id_example', entity_id='entity_id_example'),
        headers=headers,
        json=item,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_add_hierarchical_entity(client):
    """Test case for model_add_hierarchical_entity

    
    """
    hierarchical_model_create_object = {"children":["children","children"],"name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/apps/{app_id}/versions/{version_id}/hierarchicalentities'.format(app_id='app_id_example', version_id='version_id_example'),
        headers=headers,
        json=hierarchical_model_create_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_add_hierarchical_entity_child(client):
    """Test case for model_add_hierarchical_entity_child

    
    """
    hierarchical_child_model_create_object = openapi_server.ModelAddCompositeEntityChildRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/apps/{app_id}/versions/{version_id}/hierarchicalentities/{h_entity_id}/children'.format(app_id='app_id_example', version_id='version_id_example', h_entity_id='h_entity_id_example'),
        headers=headers,
        json=hierarchical_child_model_create_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_add_intent(client):
    """Test case for model_add_intent

    
    """
    intent_create_object = {"name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/apps/{app_id}/versions/{version_id}/intents'.format(app_id='app_id_example', version_id='version_id_example'),
        headers=headers,
        json=intent_create_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_add_prebuilt(client):
    """Test case for model_add_prebuilt

    
    """
    prebuilt_extractor_names = ['prebuilt_extractor_names_example']
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/apps/{app_id}/versions/{version_id}/prebuilts'.format(app_id='app_id_example', version_id='version_id_example'),
        headers=headers,
        json=prebuilt_extractor_names,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_add_sub_list(client):
    """Test case for model_add_sub_list

    
    """
    word_list_create_object = {"canonicalForm":"canonicalForm","list":["list","list"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/apps/{app_id}/versions/{version_id}/closedlists/{cl_entity_id}/sublists'.format(app_id='app_id_example', version_id='version_id_example', cl_entity_id='cl_entity_id_example'),
        headers=headers,
        json=word_list_create_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_create_closed_list_entity_role(client):
    """Test case for model_create_closed_list_entity_role

    Create a role for a list entity in a version of the application.
    """
    entity_role_create_object = {"name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/apps/{app_id}/versions/{version_id}/closedlists/{entity_id}/roles'.format(app_id='app_id_example', version_id='version_id_example', entity_id='entity_id_example'),
        headers=headers,
        json=entity_role_create_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_create_composite_entity_role(client):
    """Test case for model_create_composite_entity_role

    Create a role for a composite entity in a version of the application.
    """
    entity_role_create_object = {"name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/apps/{app_id}/versions/{version_id}/compositeentities/{c_entity_id}/roles'.format(app_id='app_id_example', version_id='version_id_example', c_entity_id='c_entity_id_example'),
        headers=headers,
        json=entity_role_create_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_create_custom_prebuilt_entity_role(client):
    """Test case for model_create_custom_prebuilt_entity_role

    Create a role for a prebuilt entity in a version of the application.
    """
    entity_role_create_object = {"name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/apps/{app_id}/versions/{version_id}/customprebuiltentities/{entity_id}/roles'.format(app_id='app_id_example', version_id='version_id_example', entity_id='entity_id_example'),
        headers=headers,
        json=entity_role_create_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_create_entity_role(client):
    """Test case for model_create_entity_role

    Create an entity role in a version of the application.
    """
    entity_role_create_object = {"name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/apps/{app_id}/versions/{version_id}/entities/{entity_id}/roles'.format(app_id='app_id_example', version_id='version_id_example', entity_id='entity_id_example'),
        headers=headers,
        json=entity_role_create_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_create_hierarchical_entity_role(client):
    """Test case for model_create_hierarchical_entity_role

    Create a role for an hierarchical entity in a version of the application.
    """
    entity_role_create_object = {"name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/apps/{app_id}/versions/{version_id}/hierarchicalentities/{h_entity_id}/roles'.format(app_id='app_id_example', version_id='version_id_example', h_entity_id='h_entity_id_example'),
        headers=headers,
        json=entity_role_create_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_create_pattern_any_entity_model(client):
    """Test case for model_create_pattern_any_entity_model

    Adds a pattern.any entity extractor to a version of the application.
    """
    extractor_create_object = {"explicitList":["explicitList","explicitList"],"name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/apps/{app_id}/versions/{version_id}/patternanyentities'.format(app_id='app_id_example', version_id='version_id_example'),
        headers=headers,
        json=extractor_create_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_create_pattern_any_entity_role(client):
    """Test case for model_create_pattern_any_entity_role

    Create a role for an Pattern.any entity in a version of the application.
    """
    entity_role_create_object = {"name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/apps/{app_id}/versions/{version_id}/patternanyentities/{entity_id}/roles'.format(app_id='app_id_example', version_id='version_id_example', entity_id='entity_id_example'),
        headers=headers,
        json=entity_role_create_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_create_prebuilt_entity_role(client):
    """Test case for model_create_prebuilt_entity_role

    Create a role for a prebuilt entity in a version of the application.
    """
    entity_role_create_object = {"name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/apps/{app_id}/versions/{version_id}/prebuilts/{entity_id}/roles'.format(app_id='app_id_example', version_id='version_id_example', entity_id='entity_id_example'),
        headers=headers,
        json=entity_role_create_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_create_regex_entity_model(client):
    """Test case for model_create_regex_entity_model

    Adds a regular expression entity model to a version of the application.
    """
    regex_entity_extractor_create_obj = {"name":"name","regexPattern":"regexPattern"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/apps/{app_id}/versions/{version_id}/regexentities'.format(app_id='app_id_example', version_id='version_id_example'),
        headers=headers,
        json=regex_entity_extractor_create_obj,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_create_regex_entity_role(client):
    """Test case for model_create_regex_entity_role

    Create a role for an regular expression entity in a version of the application.
    """
    entity_role_create_object = {"name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/apps/{app_id}/versions/{version_id}/regexentities/{entity_id}/roles'.format(app_id='app_id_example', version_id='version_id_example', entity_id='entity_id_example'),
        headers=headers,
        json=entity_role_create_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_delete_closed_list(client):
    """Test case for model_delete_closed_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/apps/{app_id}/versions/{version_id}/closedlists/{cl_entity_id}'.format(app_id='app_id_example', version_id='version_id_example', cl_entity_id='cl_entity_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_delete_closed_list_entity_role(client):
    """Test case for model_delete_closed_list_entity_role

    Delete a role for a given list entity in a version of the application.
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/apps/{app_id}/versions/{version_id}/closedlists/{entity_id}/roles/{role_id}'.format(app_id='app_id_example', version_id='version_id_example', entity_id='entity_id_example', role_id='role_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_delete_composite_entity(client):
    """Test case for model_delete_composite_entity

    
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/apps/{app_id}/versions/{version_id}/compositeentities/{c_entity_id}'.format(app_id='app_id_example', version_id='version_id_example', c_entity_id='c_entity_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_delete_composite_entity_child(client):
    """Test case for model_delete_composite_entity_child

    
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/apps/{app_id}/versions/{version_id}/compositeentities/{c_entity_id}/children/{c_child_id}'.format(app_id='app_id_example', version_id='version_id_example', c_entity_id='c_entity_id_example', c_child_id='c_child_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_delete_composite_entity_role(client):
    """Test case for model_delete_composite_entity_role

    Delete a role for a given composite entity in a version of the application.
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/apps/{app_id}/versions/{version_id}/compositeentities/{c_entity_id}/roles/{role_id}'.format(app_id='app_id_example', version_id='version_id_example', c_entity_id='c_entity_id_example', role_id='role_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_delete_custom_entity_role(client):
    """Test case for model_delete_custom_entity_role

    Delete a role for a given prebuilt entity in a version of the application.
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/apps/{app_id}/versions/{version_id}/customprebuiltentities/{entity_id}/roles/{role_id}'.format(app_id='app_id_example', version_id='version_id_example', entity_id='entity_id_example', role_id='role_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_delete_custom_prebuilt_domain(client):
    """Test case for model_delete_custom_prebuilt_domain

    
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/apps/{app_id}/versions/{version_id}/customprebuiltdomains/{domain_name}'.format(app_id='app_id_example', version_id='version_id_example', domain_name='domain_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_delete_entity(client):
    """Test case for model_delete_entity

    
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/apps/{app_id}/versions/{version_id}/entities/{entity_id}'.format(app_id='app_id_example', version_id='version_id_example', entity_id='entity_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_delete_entity_role(client):
    """Test case for model_delete_entity_role

    Delete an entity role in a version of the application.
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/apps/{app_id}/versions/{version_id}/entities/{entity_id}/roles/{role_id}'.format(app_id='app_id_example', version_id='version_id_example', entity_id='entity_id_example', role_id='role_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_delete_explicit_list_item(client):
    """Test case for model_delete_explicit_list_item

    Delete an item from the explicit (exception) list for a Pattern.any entity in a version of the application.
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/apps/{app_id}/versions/{version_id}/patternanyentities/{entity_id}/explicitlist/{item_id}'.format(app_id='app_id_example', version_id='version_id_example', entity_id='entity_id_example', item_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_delete_hierarchical_entity(client):
    """Test case for model_delete_hierarchical_entity

    
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/apps/{app_id}/versions/{version_id}/hierarchicalentities/{h_entity_id}'.format(app_id='app_id_example', version_id='version_id_example', h_entity_id='h_entity_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_delete_hierarchical_entity_child(client):
    """Test case for model_delete_hierarchical_entity_child

    
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/apps/{app_id}/versions/{version_id}/hierarchicalentities/{h_entity_id}/children/{h_child_id}'.format(app_id='app_id_example', version_id='version_id_example', h_entity_id='h_entity_id_example', h_child_id='h_child_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_delete_hierarchical_entity_role(client):
    """Test case for model_delete_hierarchical_entity_role

    Delete a role for a given hierarchical role in a version of the application.
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/apps/{app_id}/versions/{version_id}/hierarchicalentities/{h_entity_id}/roles/{role_id}'.format(app_id='app_id_example', version_id='version_id_example', h_entity_id='h_entity_id_example', role_id='role_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_delete_intent(client):
    """Test case for model_delete_intent

    
    """
    params = [('deleteUtterances', False)]
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/apps/{app_id}/versions/{version_id}/intents/{intent_id}'.format(app_id='app_id_example', version_id='version_id_example', intent_id='intent_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_delete_pattern_any_entity_model(client):
    """Test case for model_delete_pattern_any_entity_model

    Deletes a Pattern.Any entity extractor from a version of the application.
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/apps/{app_id}/versions/{version_id}/patternanyentities/{entity_id}'.format(app_id='app_id_example', version_id='version_id_example', entity_id='entity_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_delete_pattern_any_entity_role(client):
    """Test case for model_delete_pattern_any_entity_role

    Delete a role for a given Pattern.any entity in a version of the application.
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/apps/{app_id}/versions/{version_id}/patternanyentities/{entity_id}/roles/{role_id}'.format(app_id='app_id_example', version_id='version_id_example', entity_id='entity_id_example', role_id='role_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_delete_prebuilt(client):
    """Test case for model_delete_prebuilt

    
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/apps/{app_id}/versions/{version_id}/prebuilts/{prebuilt_id}'.format(app_id='app_id_example', version_id='version_id_example', prebuilt_id='prebuilt_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_delete_prebuilt_entity_role(client):
    """Test case for model_delete_prebuilt_entity_role

    Delete a role in a prebuilt entity in a version of the application.
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/apps/{app_id}/versions/{version_id}/prebuilts/{entity_id}/roles/{role_id}'.format(app_id='app_id_example', version_id='version_id_example', entity_id='entity_id_example', role_id='role_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_delete_regex_entity_model(client):
    """Test case for model_delete_regex_entity_model

    Deletes a regular expression entity from a version of the application.
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/apps/{app_id}/versions/{version_id}/regexentities/{regex_entity_id}'.format(app_id='app_id_example', version_id='version_id_example', regex_entity_id='regex_entity_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_delete_regex_entity_role(client):
    """Test case for model_delete_regex_entity_role

    Delete a role for a given regular expression in a version of the application.
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/apps/{app_id}/versions/{version_id}/regexentities/{entity_id}/roles/{role_id}'.format(app_id='app_id_example', version_id='version_id_example', entity_id='entity_id_example', role_id='role_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_delete_sub_list(client):
    """Test case for model_delete_sub_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/apps/{app_id}/versions/{version_id}/closedlists/{cl_entity_id}/sublists/{sub_list_id}'.format(app_id='app_id_example', version_id='version_id_example', cl_entity_id='cl_entity_id_example', sub_list_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_examples(client):
    """Test case for model_examples

    
    """
    params = [('skip', 0),
                    ('take', 100)]
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/{app_id}/versions/{version_id}/models/{model_id}/examples'.format(app_id='app_id_example', version_id='version_id_example', model_id='model_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_get_closed_list(client):
    """Test case for model_get_closed_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/{app_id}/versions/{version_id}/closedlists/{cl_entity_id}'.format(app_id='app_id_example', version_id='version_id_example', cl_entity_id='cl_entity_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_get_closed_list_entity_role(client):
    """Test case for model_get_closed_list_entity_role

    Get one role for a given list entity in a version of the application.
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/{app_id}/versions/{version_id}/closedlists/{entity_id}/roles/{role_id}'.format(app_id='app_id_example', version_id='version_id_example', entity_id='entity_id_example', role_id='role_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_get_composite_entity(client):
    """Test case for model_get_composite_entity

    
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/{app_id}/versions/{version_id}/compositeentities/{c_entity_id}'.format(app_id='app_id_example', version_id='version_id_example', c_entity_id='c_entity_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_get_composite_entity_role(client):
    """Test case for model_get_composite_entity_role

    Get one role for a given composite entity in a version of the application
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/{app_id}/versions/{version_id}/compositeentities/{c_entity_id}/roles/{role_id}'.format(app_id='app_id_example', version_id='version_id_example', c_entity_id='c_entity_id_example', role_id='role_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_get_custom_entity_role(client):
    """Test case for model_get_custom_entity_role

    Get one role for a given prebuilt entity in a version of the application.
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/{app_id}/versions/{version_id}/customprebuiltentities/{entity_id}/roles/{role_id}'.format(app_id='app_id_example', version_id='version_id_example', entity_id='entity_id_example', role_id='role_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_get_entity(client):
    """Test case for model_get_entity

    
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/{app_id}/versions/{version_id}/entities/{entity_id}'.format(app_id='app_id_example', version_id='version_id_example', entity_id='entity_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_get_entity_role(client):
    """Test case for model_get_entity_role

    Get one role for a given entity in a version of the application
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/{app_id}/versions/{version_id}/entities/{entity_id}/roles/{role_id}'.format(app_id='app_id_example', version_id='version_id_example', entity_id='entity_id_example', role_id='role_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_get_explicit_list(client):
    """Test case for model_get_explicit_list

    Get the explicit (exception) list of the pattern.any entity in a version of the application.
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/{app_id}/versions/{version_id}/patternanyentities/{entity_id}/explicitlist'.format(app_id='app_id_example', version_id='version_id_example', entity_id='entity_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_get_explicit_list_item(client):
    """Test case for model_get_explicit_list_item

    Get the explicit (exception) list of the pattern.any entity in a version of the application.
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/{app_id}/versions/{version_id}/patternanyentities/{entity_id}/explicitlist/{item_id}'.format(app_id='app_id_example', version_id='version_id_example', entity_id='entity_id_example', item_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_get_hierarchical_entity(client):
    """Test case for model_get_hierarchical_entity

    
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/{app_id}/versions/{version_id}/hierarchicalentities/{h_entity_id}'.format(app_id='app_id_example', version_id='version_id_example', h_entity_id='h_entity_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_get_hierarchical_entity_child(client):
    """Test case for model_get_hierarchical_entity_child

    
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/{app_id}/versions/{version_id}/hierarchicalentities/{h_entity_id}/children/{h_child_id}'.format(app_id='app_id_example', version_id='version_id_example', h_entity_id='h_entity_id_example', h_child_id='h_child_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_get_hierarchical_entity_role(client):
    """Test case for model_get_hierarchical_entity_role

    Get one role for a given hierarchical entity in a version of the application.
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/{app_id}/versions/{version_id}/hierarchicalentities/{h_entity_id}/roles/{role_id}'.format(app_id='app_id_example', version_id='version_id_example', h_entity_id='h_entity_id_example', role_id='role_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_get_intent(client):
    """Test case for model_get_intent

    
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/{app_id}/versions/{version_id}/intents/{intent_id}'.format(app_id='app_id_example', version_id='version_id_example', intent_id='intent_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_get_pattern_any_entity_info(client):
    """Test case for model_get_pattern_any_entity_info

    Gets information about the Pattern.Any model in a version of the application.
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/{app_id}/versions/{version_id}/patternanyentities/{entity_id}'.format(app_id='app_id_example', version_id='version_id_example', entity_id='entity_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_get_pattern_any_entity_role(client):
    """Test case for model_get_pattern_any_entity_role

    Get one role for a given Pattern.any entity in a version of the application.
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/{app_id}/versions/{version_id}/patternanyentities/{entity_id}/roles/{role_id}'.format(app_id='app_id_example', version_id='version_id_example', entity_id='entity_id_example', role_id='role_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_get_prebuilt(client):
    """Test case for model_get_prebuilt

    
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/{app_id}/versions/{version_id}/prebuilts/{prebuilt_id}'.format(app_id='app_id_example', version_id='version_id_example', prebuilt_id='prebuilt_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_get_prebuilt_entity_role(client):
    """Test case for model_get_prebuilt_entity_role

    Get one role for a given prebuilt entity in a version of the application
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/{app_id}/versions/{version_id}/prebuilts/{entity_id}/roles/{role_id}'.format(app_id='app_id_example', version_id='version_id_example', entity_id='entity_id_example', role_id='role_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_get_regex_entity_entity_info(client):
    """Test case for model_get_regex_entity_entity_info

    Gets information about a regular expression entity in a version of the application.
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/{app_id}/versions/{version_id}/regexentities/{regex_entity_id}'.format(app_id='app_id_example', version_id='version_id_example', regex_entity_id='regex_entity_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_get_regex_entity_role(client):
    """Test case for model_get_regex_entity_role

    Get one role for a given regular expression entity in a version of the application.
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/{app_id}/versions/{version_id}/regexentities/{entity_id}/roles/{role_id}'.format(app_id='app_id_example', version_id='version_id_example', entity_id='entity_id_example', role_id='role_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_list_closed_list_entity_roles(client):
    """Test case for model_list_closed_list_entity_roles

    Get all roles for a list entity in a version of the application.
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/{app_id}/versions/{version_id}/closedlists/{entity_id}/roles'.format(app_id='app_id_example', version_id='version_id_example', entity_id='entity_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_list_closed_lists(client):
    """Test case for model_list_closed_lists

    
    """
    params = [('skip', 0),
                    ('take', 100)]
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/{app_id}/versions/{version_id}/closedlists'.format(app_id='app_id_example', version_id='version_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_list_composite_entities(client):
    """Test case for model_list_composite_entities

    
    """
    params = [('skip', 0),
                    ('take', 100)]
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/{app_id}/versions/{version_id}/compositeentities'.format(app_id='app_id_example', version_id='version_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_list_composite_entity_roles(client):
    """Test case for model_list_composite_entity_roles

    Get all roles for a composite entity in a version of the application
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/{app_id}/versions/{version_id}/compositeentities/{c_entity_id}/roles'.format(app_id='app_id_example', version_id='version_id_example', c_entity_id='c_entity_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_list_custom_prebuilt_entities(client):
    """Test case for model_list_custom_prebuilt_entities

    
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/{app_id}/versions/{version_id}/customprebuiltentities'.format(app_id='app_id_example', version_id='version_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_list_custom_prebuilt_entity_roles(client):
    """Test case for model_list_custom_prebuilt_entity_roles

    Get all roles for a prebuilt entity in a version of the application
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/{app_id}/versions/{version_id}/customprebuiltentities/{entity_id}/roles'.format(app_id='app_id_example', version_id='version_id_example', entity_id='entity_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_list_custom_prebuilt_intents(client):
    """Test case for model_list_custom_prebuilt_intents

    
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/{app_id}/versions/{version_id}/customprebuiltintents'.format(app_id='app_id_example', version_id='version_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_list_custom_prebuilt_models(client):
    """Test case for model_list_custom_prebuilt_models

    
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/{app_id}/versions/{version_id}/customprebuiltmodels'.format(app_id='app_id_example', version_id='version_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_list_entities(client):
    """Test case for model_list_entities

    
    """
    params = [('skip', 0),
                    ('take', 100)]
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/{app_id}/versions/{version_id}/entities'.format(app_id='app_id_example', version_id='version_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_list_entity_roles(client):
    """Test case for model_list_entity_roles

    Get all roles for an entity in a version of the application
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/{app_id}/versions/{version_id}/entities/{entity_id}/roles'.format(app_id='app_id_example', version_id='version_id_example', entity_id='entity_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_list_entity_suggestions(client):
    """Test case for model_list_entity_suggestions

    
    """
    params = [('take', 100)]
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/{app_id}/versions/{version_id}/entities/{entity_id}/suggest'.format(app_id='app_id_example', version_id='version_id_example', entity_id='entity_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_list_hierarchical_entities(client):
    """Test case for model_list_hierarchical_entities

    
    """
    params = [('skip', 0),
                    ('take', 100)]
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/{app_id}/versions/{version_id}/hierarchicalentities'.format(app_id='app_id_example', version_id='version_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_list_hierarchical_entity_roles(client):
    """Test case for model_list_hierarchical_entity_roles

    Get all roles for a hierarchical entity in a version of the application
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/{app_id}/versions/{version_id}/hierarchicalentities/{h_entity_id}/roles'.format(app_id='app_id_example', version_id='version_id_example', h_entity_id='h_entity_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_list_intent_suggestions(client):
    """Test case for model_list_intent_suggestions

    
    """
    params = [('take', 100)]
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/{app_id}/versions/{version_id}/intents/{intent_id}/suggest'.format(app_id='app_id_example', version_id='version_id_example', intent_id='intent_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_list_intents(client):
    """Test case for model_list_intents

    
    """
    params = [('skip', 0),
                    ('take', 100)]
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/{app_id}/versions/{version_id}/intents'.format(app_id='app_id_example', version_id='version_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_list_models(client):
    """Test case for model_list_models

    
    """
    params = [('skip', 0),
                    ('take', 100)]
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/{app_id}/versions/{version_id}/models'.format(app_id='app_id_example', version_id='version_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_list_pattern_any_entity_infos(client):
    """Test case for model_list_pattern_any_entity_infos

    Get information about the Pattern.Any entity models in a version of the application.
    """
    params = [('skip', 0),
                    ('take', 100)]
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/{app_id}/versions/{version_id}/patternanyentities'.format(app_id='app_id_example', version_id='version_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_list_pattern_any_entity_roles(client):
    """Test case for model_list_pattern_any_entity_roles

    Get all roles for a Pattern.any entity in a version of the application
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/{app_id}/versions/{version_id}/patternanyentities/{entity_id}/roles'.format(app_id='app_id_example', version_id='version_id_example', entity_id='entity_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_list_prebuilt_entities(client):
    """Test case for model_list_prebuilt_entities

    
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/{app_id}/versions/{version_id}/listprebuilts'.format(app_id='app_id_example', version_id='version_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_list_prebuilt_entity_roles(client):
    """Test case for model_list_prebuilt_entity_roles

    Get a prebuilt entity's roles in a version of the application.
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/{app_id}/versions/{version_id}/prebuilts/{entity_id}/roles'.format(app_id='app_id_example', version_id='version_id_example', entity_id='entity_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_list_prebuilts(client):
    """Test case for model_list_prebuilts

    
    """
    params = [('skip', 0),
                    ('take', 100)]
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/{app_id}/versions/{version_id}/prebuilts'.format(app_id='app_id_example', version_id='version_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_list_regex_entity_infos(client):
    """Test case for model_list_regex_entity_infos

    Gets information about the regular expression entity models in a version of the application.
    """
    params = [('skip', 0),
                    ('take', 100)]
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/{app_id}/versions/{version_id}/regexentities'.format(app_id='app_id_example', version_id='version_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_list_regex_entity_roles(client):
    """Test case for model_list_regex_entity_roles

    Get all roles for a regular expression entity in a version of the application.
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/{app_id}/versions/{version_id}/regexentities/{entity_id}/roles'.format(app_id='app_id_example', version_id='version_id_example', entity_id='entity_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_patch_closed_list(client):
    """Test case for model_patch_closed_list

    
    """
    closed_list_model_patch_object = {"subLists":[{"canonicalForm":"canonicalForm","list":["list","list"]},{"canonicalForm":"canonicalForm","list":["list","list"]}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/apps/{app_id}/versions/{version_id}/closedlists/{cl_entity_id}'.format(app_id='app_id_example', version_id='version_id_example', cl_entity_id='cl_entity_id_example'),
        headers=headers,
        json=closed_list_model_patch_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_update_closed_list(client):
    """Test case for model_update_closed_list

    
    """
    closed_list_model_update_object = {"name":"name","subLists":[{"canonicalForm":"canonicalForm","list":["list","list"]},{"canonicalForm":"canonicalForm","list":["list","list"]}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/apps/{app_id}/versions/{version_id}/closedlists/{cl_entity_id}'.format(app_id='app_id_example', version_id='version_id_example', cl_entity_id='cl_entity_id_example'),
        headers=headers,
        json=closed_list_model_update_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_update_closed_list_entity_role(client):
    """Test case for model_update_closed_list_entity_role

    Update a role for a given list entity in a version of the application.
    """
    entity_role_update_object = {"name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/apps/{app_id}/versions/{version_id}/closedlists/{entity_id}/roles/{role_id}'.format(app_id='app_id_example', version_id='version_id_example', entity_id='entity_id_example', role_id='role_id_example'),
        headers=headers,
        json=entity_role_update_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_update_composite_entity(client):
    """Test case for model_update_composite_entity

    
    """
    composite_model_update_object = {"children":["children","children"],"name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/apps/{app_id}/versions/{version_id}/compositeentities/{c_entity_id}'.format(app_id='app_id_example', version_id='version_id_example', c_entity_id='c_entity_id_example'),
        headers=headers,
        json=composite_model_update_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_update_composite_entity_role(client):
    """Test case for model_update_composite_entity_role

    Update a role for a given composite entity in a version of the application
    """
    entity_role_update_object = {"name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/apps/{app_id}/versions/{version_id}/compositeentities/{c_entity_id}/roles/{role_id}'.format(app_id='app_id_example', version_id='version_id_example', c_entity_id='c_entity_id_example', role_id='role_id_example'),
        headers=headers,
        json=entity_role_update_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_update_custom_prebuilt_entity_role(client):
    """Test case for model_update_custom_prebuilt_entity_role

    Update a role for a given prebuilt entity in a version of the application.
    """
    entity_role_update_object = {"name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/apps/{app_id}/versions/{version_id}/customprebuiltentities/{entity_id}/roles/{role_id}'.format(app_id='app_id_example', version_id='version_id_example', entity_id='entity_id_example', role_id='role_id_example'),
        headers=headers,
        json=entity_role_update_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_update_entity(client):
    """Test case for model_update_entity

    
    """
    model_update_object = {"name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/apps/{app_id}/versions/{version_id}/entities/{entity_id}'.format(app_id='app_id_example', version_id='version_id_example', entity_id='entity_id_example'),
        headers=headers,
        json=model_update_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_update_entity_role(client):
    """Test case for model_update_entity_role

    Update a role for a given entity in a version of the application.
    """
    entity_role_update_object = {"name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/apps/{app_id}/versions/{version_id}/entities/{entity_id}/roles/{role_id}'.format(app_id='app_id_example', version_id='version_id_example', entity_id='entity_id_example', role_id='role_id_example'),
        headers=headers,
        json=entity_role_update_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_update_explicit_list_item(client):
    """Test case for model_update_explicit_list_item

    Updates an explicit (exception) list item for a Pattern.Any entity in a version of the application.
    """
    item = {"explicitListItem":"explicitListItem"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/apps/{app_id}/versions/{version_id}/patternanyentities/{entity_id}/explicitlist/{item_id}'.format(app_id='app_id_example', version_id='version_id_example', entity_id='entity_id_example', item_id=56),
        headers=headers,
        json=item,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_update_hierarchical_entity(client):
    """Test case for model_update_hierarchical_entity

    
    """
    hierarchical_model_update_object = {"children":["children","children"],"name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/apps/{app_id}/versions/{version_id}/hierarchicalentities/{h_entity_id}'.format(app_id='app_id_example', version_id='version_id_example', h_entity_id='h_entity_id_example'),
        headers=headers,
        json=hierarchical_model_update_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_update_hierarchical_entity_child(client):
    """Test case for model_update_hierarchical_entity_child

    
    """
    hierarchical_child_model_update_object = openapi_server.ModelAddCompositeEntityChildRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/apps/{app_id}/versions/{version_id}/hierarchicalentities/{h_entity_id}/children/{h_child_id}'.format(app_id='app_id_example', version_id='version_id_example', h_entity_id='h_entity_id_example', h_child_id='h_child_id_example'),
        headers=headers,
        json=hierarchical_child_model_update_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_update_hierarchical_entity_role(client):
    """Test case for model_update_hierarchical_entity_role

    Update a role for a given hierarchical entity in a version of the application.
    """
    entity_role_update_object = {"name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/apps/{app_id}/versions/{version_id}/hierarchicalentities/{h_entity_id}/roles/{role_id}'.format(app_id='app_id_example', version_id='version_id_example', h_entity_id='h_entity_id_example', role_id='role_id_example'),
        headers=headers,
        json=entity_role_update_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_update_intent(client):
    """Test case for model_update_intent

    
    """
    model_update_object = {"name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/apps/{app_id}/versions/{version_id}/intents/{intent_id}'.format(app_id='app_id_example', version_id='version_id_example', intent_id='intent_id_example'),
        headers=headers,
        json=model_update_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_update_pattern_any_entity_model(client):
    """Test case for model_update_pattern_any_entity_model

    Updates the name and explicit (exception) list of a Pattern.Any entity model in a version of the application.
    """
    pattern_any_update_object = {"explicitList":["explicitList","explicitList"],"name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/apps/{app_id}/versions/{version_id}/patternanyentities/{entity_id}'.format(app_id='app_id_example', version_id='version_id_example', entity_id='entity_id_example'),
        headers=headers,
        json=pattern_any_update_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_update_pattern_any_entity_role(client):
    """Test case for model_update_pattern_any_entity_role

    Update a role for a given Pattern.any entity in a version of the application.
    """
    entity_role_update_object = {"name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/apps/{app_id}/versions/{version_id}/patternanyentities/{entity_id}/roles/{role_id}'.format(app_id='app_id_example', version_id='version_id_example', entity_id='entity_id_example', role_id='role_id_example'),
        headers=headers,
        json=entity_role_update_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_update_prebuilt_entity_role(client):
    """Test case for model_update_prebuilt_entity_role

    Update a role for a given prebuilt entity in a version of the application
    """
    entity_role_update_object = {"name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/apps/{app_id}/versions/{version_id}/prebuilts/{entity_id}/roles/{role_id}'.format(app_id='app_id_example', version_id='version_id_example', entity_id='entity_id_example', role_id='role_id_example'),
        headers=headers,
        json=entity_role_update_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_update_regex_entity_model(client):
    """Test case for model_update_regex_entity_model

    Updates the regular expression entity in a version of the application.
    """
    regex_entity_update_object = {"name":"name","regexPattern":"regexPattern"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/apps/{app_id}/versions/{version_id}/regexentities/{regex_entity_id}'.format(app_id='app_id_example', version_id='version_id_example', regex_entity_id='regex_entity_id_example'),
        headers=headers,
        json=regex_entity_update_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_update_regex_entity_role(client):
    """Test case for model_update_regex_entity_role

    Update a role for a given regular expression entity in a version of the application
    """
    entity_role_update_object = {"name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/apps/{app_id}/versions/{version_id}/regexentities/{entity_id}/roles/{role_id}'.format(app_id='app_id_example', version_id='version_id_example', entity_id='entity_id_example', role_id='role_id_example'),
        headers=headers,
        json=entity_role_update_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_update_sub_list(client):
    """Test case for model_update_sub_list

    
    """
    word_list_base_update_object = {"canonicalForm":"canonicalForm","list":["list","list"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/apps/{app_id}/versions/{version_id}/closedlists/{cl_entity_id}/sublists/{sub_list_id}'.format(app_id='app_id_example', version_id='version_id_example', cl_entity_id='cl_entity_id_example', sub_list_id=56),
        headers=headers,
        json=word_list_base_update_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pattern_add_pattern(client):
    """Test case for pattern_add_pattern

    Adds a pattern to a version of the application.
    """
    pattern = {"pattern":"pattern","intent":"intent"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/apps/{app_id}/versions/{version_id}/patternrule'.format(app_id='app_id_example', version_id='version_id_example'),
        headers=headers,
        json=pattern,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pattern_batch_add_patterns(client):
    """Test case for pattern_batch_add_patterns

    Adds a batch of patterns in a version of the application.
    """
    patterns = {"pattern":"pattern","intent":"intent"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/apps/{app_id}/versions/{version_id}/patternrules'.format(app_id='app_id_example', version_id='version_id_example'),
        headers=headers,
        json=patterns,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pattern_delete_pattern(client):
    """Test case for pattern_delete_pattern

    Deletes the pattern with the specified ID from a version of the application..
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/apps/{app_id}/versions/{version_id}/patternrules/{pattern_id}'.format(app_id='app_id_example', version_id='version_id_example', pattern_id='pattern_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pattern_delete_patterns(client):
    """Test case for pattern_delete_patterns

    Deletes a list of patterns in a version of the application.
    """
    pattern_ids = ['pattern_ids_example']
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/apps/{app_id}/versions/{version_id}/patternrules'.format(app_id='app_id_example', version_id='version_id_example'),
        headers=headers,
        json=pattern_ids,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pattern_list_intent_patterns(client):
    """Test case for pattern_list_intent_patterns

    Returns patterns for the specific intent in a version of the application.
    """
    params = [('skip', 0),
                    ('take', 100)]
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/{app_id}/versions/{version_id}/intents/{intent_id}/patternrules'.format(app_id='app_id_example', version_id='version_id_example', intent_id='intent_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pattern_list_patterns(client):
    """Test case for pattern_list_patterns

    Gets patterns in a version of the application.
    """
    params = [('skip', 0),
                    ('take', 100)]
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/{app_id}/versions/{version_id}/patternrules'.format(app_id='app_id_example', version_id='version_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pattern_update_pattern(client):
    """Test case for pattern_update_pattern

    Updates a pattern in a version of the application.
    """
    pattern = {"pattern":"pattern","id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","intent":"intent"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/apps/{app_id}/versions/{version_id}/patternrules/{pattern_id}'.format(app_id='app_id_example', version_id='version_id_example', pattern_id='pattern_id_example'),
        headers=headers,
        json=pattern,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pattern_update_patterns(client):
    """Test case for pattern_update_patterns

    Updates patterns in a version of the application.
    """
    patterns = {"pattern":"pattern","id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","intent":"intent"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/apps/{app_id}/versions/{version_id}/patternrules'.format(app_id='app_id_example', version_id='version_id_example'),
        headers=headers,
        json=patterns,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_permissions_add(client):
    """Test case for permissions_add

    
    """
    user_to_add = {"email":"email"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/apps/{app_id}/permissions'.format(app_id='app_id_example'),
        headers=headers,
        json=user_to_add,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_permissions_delete(client):
    """Test case for permissions_delete

    
    """
    user_to_delete = {"email":"email"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/apps/{app_id}/permissions'.format(app_id='app_id_example'),
        headers=headers,
        json=user_to_delete,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_permissions_list(client):
    """Test case for permissions_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/{app_id}/permissions'.format(app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_permissions_update(client):
    """Test case for permissions_update

    
    """
    collaborators = {"emails":["emails","emails"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/apps/{app_id}/permissions'.format(app_id='app_id_example'),
        headers=headers,
        json=collaborators,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_settings_list(client):
    """Test case for settings_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/{app_id}/versions/{version_id}/settings'.format(app_id='app_id_example', version_id='version_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_settings_update(client):
    """Test case for settings_update

    
    """
    list_of_app_version_setting_object = {"name":"name","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/apps/{app_id}/versions/{version_id}/settings'.format(app_id='app_id_example', version_id='version_id_example'),
        headers=headers,
        json=list_of_app_version_setting_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_train_get_status(client):
    """Test case for train_get_status

    
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/{app_id}/versions/{version_id}/train'.format(app_id='app_id_example', version_id='version_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_train_train_version(client):
    """Test case for train_train_version

    
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/apps/{app_id}/versions/{version_id}/train'.format(app_id='app_id_example', version_id='version_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_versions_clone(client):
    """Test case for versions_clone

    
    """
    version_clone_object = {"version":"version"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/apps/{app_id}/versions/{version_id}/clone'.format(app_id='app_id_example', version_id='version_id_example'),
        headers=headers,
        json=version_clone_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_versions_delete(client):
    """Test case for versions_delete

    
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/apps/{app_id}/versions/{version_id}'.format(app_id='app_id_example', version_id='version_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_versions_delete_unlabelled_utterance(client):
    """Test case for versions_delete_unlabelled_utterance

    
    """
    utterance = 'utterance_example'
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/apps/{app_id}/versions/{version_id}/suggest'.format(app_id='app_id_example', version_id='version_id_example'),
        headers=headers,
        json=utterance,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_versions_export(client):
    """Test case for versions_export

    
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/{app_id}/versions/{version_id}/export'.format(app_id='app_id_example', version_id='version_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_versions_get(client):
    """Test case for versions_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/{app_id}/versions/{version_id}'.format(app_id='app_id_example', version_id='version_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_versions_import(client):
    """Test case for versions_import

    
    """
    luis_app = {"utterances":[{"entities":[{"role":"role","entity":"entity","startPos":6,"endPos":0},{"role":"role","entity":"entity","startPos":6,"endPos":0}],"text":"text","intent":"intent"},{"entities":[{"role":"role","entity":"entity","startPos":6,"endPos":0},{"role":"role","entity":"entity","startPos":6,"endPos":0}],"text":"text","intent":"intent"}],"intents":[{"children":["children","children"],"roles":["roles","roles"],"name":"name","inherits":{"domain_name":"domain_name","model_name":"model_name"}},{"children":["children","children"],"roles":["roles","roles"],"name":"name","inherits":{"domain_name":"domain_name","model_name":"model_name"}}],"prebuiltEntities":[{"roles":["roles","roles"],"name":"name"},{"roles":["roles","roles"],"name":"name"}],"patterns":[{"pattern":"pattern","intent":"intent"},{"pattern":"pattern","intent":"intent"}],"composites":[{"children":["children","children"],"roles":["roles","roles"],"name":"name","inherits":{"domain_name":"domain_name","model_name":"model_name"}},{"children":["children","children"],"roles":["roles","roles"],"name":"name","inherits":{"domain_name":"domain_name","model_name":"model_name"}}],"versionId":"versionId","closedLists":[{"roles":["roles","roles"],"name":"name","subLists":[{"canonicalForm":"canonicalForm","list":["list","list"]},{"canonicalForm":"canonicalForm","list":["list","list"]}]},{"roles":["roles","roles"],"name":"name","subLists":[{"canonicalForm":"canonicalForm","list":["list","list"]},{"canonicalForm":"canonicalForm","list":["list","list"]}]}],"entities":[{"children":["children","children"],"roles":["roles","roles"],"name":"name","inherits":{"domain_name":"domain_name","model_name":"model_name"}},{"children":["children","children"],"roles":["roles","roles"],"name":"name","inherits":{"domain_name":"domain_name","model_name":"model_name"}}],"culture":"culture","regex_entities":[{"roles":["roles","roles"],"name":"name","regexPattern":"regexPattern"},{"roles":["roles","roles"],"name":"name","regexPattern":"regexPattern"}],"patternAnyEntities":[{"explicitList":["explicitList","explicitList"],"roles":["roles","roles"],"name":"name"},{"explicitList":["explicitList","explicitList"],"roles":["roles","roles"],"name":"name"}],"model_features":[{"mode":True,"name":"name","words":"words","activated":True},{"mode":True,"name":"name","words":"words","activated":True}],"name":"name","regex_features":[{"name":"name","pattern":"pattern","activated":True},{"name":"name","pattern":"pattern","activated":True}],"desc":"desc"}
    params = [('versionId', 'version_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/apps/{app_id}/versions/import'.format(app_id='app_id_example'),
        headers=headers,
        json=luis_app,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_versions_list(client):
    """Test case for versions_list

    
    """
    params = [('skip', 0),
                    ('take', 100)]
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/{app_id}/versions'.format(app_id='app_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_versions_update(client):
    """Test case for versions_update

    
    """
    version_update_object = {"version":"version"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/apps/{app_id}/versions/{version_id}'.format(app_id='app_id_example', version_id='version_id_example'),
        headers=headers,
        json=version_update_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

