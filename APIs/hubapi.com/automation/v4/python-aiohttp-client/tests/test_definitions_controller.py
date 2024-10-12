# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.collection_response_public_action_definition_forward_paging import CollectionResponsePublicActionDefinitionForwardPaging
from openapi_server.models.error import Error
from openapi_server.models.public_action_definition import PublicActionDefinition
from openapi_server.models.public_action_definition_egg import PublicActionDefinitionEgg
from openapi_server.models.public_action_definition_patch import PublicActionDefinitionPatch


pytestmark = pytest.mark.asyncio

async def test_delete_automation_v4_actions_app_id_definition_id_archive(client):
    """Test case for delete_automation_v4_actions_app_id_definition_id_archive

    Archive an extension definition
    """
    headers = { 
        'Accept': '*/*',
        'developer_hapikey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/automation/v4/actions/{app_id}/{definition_id}'.format(definition_id='definition_id_example', app_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_automation_v4_actions_app_id_definition_id_get_by_id(client):
    """Test case for get_automation_v4_actions_app_id_definition_id_get_by_id

    Get extension definition by Id
    """
    params = [('archived', False)]
    headers = { 
        'Accept': 'application/json',
        'developer_hapikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/automation/v4/actions/{app_id}/{definition_id}'.format(definition_id='definition_id_example', app_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_automation_v4_actions_app_id_get_page(client):
    """Test case for get_automation_v4_actions_app_id_get_page

    Get paged extension definitions
    """
    params = [('limit', 56),
                    ('after', 'after_example'),
                    ('archived', False)]
    headers = { 
        'Accept': 'application/json',
        'developer_hapikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/automation/v4/actions/{app_id}'.format(app_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_automation_v4_actions_app_id_definition_id_update(client):
    """Test case for patch_automation_v4_actions_app_id_definition_id_update

    Patch an existing extension definition
    """
    body = {"inputFields":[{"isRequired":True,"automationFieldType":"automationFieldType","typeDefinition":{"helpText":"helpText","referencedObjectType":"CONTACT","name":"name","options":[{"hidden":True,"displayOrder":6,"doubleData":1.4658129805029452,"description":"description","readOnly":True,"label":"label","value":"value"},{"hidden":True,"displayOrder":6,"doubleData":1.4658129805029452,"description":"description","readOnly":True,"label":"label","value":"value"}],"description":"description","externalOptionsReferenceType":"externalOptionsReferenceType","label":"label","type":"string","externalOptions":True,"fieldType":"booleancheckbox","optionsUrl":"optionsUrl"},"supportedValueTypes":["STATIC_VALUE","STATIC_VALUE"]},{"isRequired":True,"automationFieldType":"automationFieldType","typeDefinition":{"helpText":"helpText","referencedObjectType":"CONTACT","name":"name","options":[{"hidden":True,"displayOrder":6,"doubleData":1.4658129805029452,"description":"description","readOnly":True,"label":"label","value":"value"},{"hidden":True,"displayOrder":6,"doubleData":1.4658129805029452,"description":"description","readOnly":True,"label":"label","value":"value"}],"description":"description","externalOptionsReferenceType":"externalOptionsReferenceType","label":"label","type":"string","externalOptions":True,"fieldType":"booleancheckbox","optionsUrl":"optionsUrl"},"supportedValueTypes":["STATIC_VALUE","STATIC_VALUE"]}],"outputFields":[{"typeDefinition":{"helpText":"helpText","referencedObjectType":"CONTACT","name":"name","options":[{"hidden":True,"displayOrder":6,"doubleData":1.4658129805029452,"description":"description","readOnly":True,"label":"label","value":"value"},{"hidden":True,"displayOrder":6,"doubleData":1.4658129805029452,"description":"description","readOnly":True,"label":"label","value":"value"}],"description":"description","externalOptionsReferenceType":"externalOptionsReferenceType","label":"label","type":"string","externalOptions":True,"fieldType":"booleancheckbox","optionsUrl":"optionsUrl"}},{"typeDefinition":{"helpText":"helpText","referencedObjectType":"CONTACT","name":"name","options":[{"hidden":True,"displayOrder":6,"doubleData":1.4658129805029452,"description":"description","readOnly":True,"label":"label","value":"value"},{"hidden":True,"displayOrder":6,"doubleData":1.4658129805029452,"description":"description","readOnly":True,"label":"label","value":"value"}],"description":"description","externalOptionsReferenceType":"externalOptionsReferenceType","label":"label","type":"string","externalOptions":True,"fieldType":"booleancheckbox","optionsUrl":"optionsUrl"}}],"actionUrl":"actionUrl","inputFieldDependencies":[{"dependencyType":"SINGLE_FIELD","controllingFieldName":"controllingFieldName","dependentFieldNames":["dependentFieldNames","dependentFieldNames"]},{"dependencyType":"SINGLE_FIELD","controllingFieldName":"controllingFieldName","dependentFieldNames":["dependentFieldNames","dependentFieldNames"]}],"executionRules":[{"conditions":{"key":"{}"},"labelName":"labelName"},{"conditions":{"key":"{}"},"labelName":"labelName"}],"published":True,"objectTypes":["objectTypes","objectTypes"],"labels":{"key":{"inputFieldDescriptions":{"key":"inputFieldDescriptions"},"appDisplayName":"appDisplayName","outputFieldLabels":{"key":"outputFieldLabels"},"actionDescription":"actionDescription","executionRules":{"key":"executionRules"},"inputFieldOptionLabels":{"key":{"key":"inputFieldOptionLabels"}},"actionCardContent":"actionCardContent","actionName":"actionName","inputFieldLabels":{"key":"inputFieldLabels"}}},"objectRequestOptions":{"properties":["properties","properties"]}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'developer_hapikey': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/automation/v4/actions/{app_id}/{definition_id}'.format(definition_id='definition_id_example', app_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_automation_v4_actions_app_id_create(client):
    """Test case for post_automation_v4_actions_app_id_create

    Create a new extension definition
    """
    body = {"inputFields":[{"isRequired":True,"automationFieldType":"automationFieldType","typeDefinition":{"helpText":"helpText","referencedObjectType":"CONTACT","name":"name","options":[{"hidden":True,"displayOrder":6,"doubleData":1.4658129805029452,"description":"description","readOnly":True,"label":"label","value":"value"},{"hidden":True,"displayOrder":6,"doubleData":1.4658129805029452,"description":"description","readOnly":True,"label":"label","value":"value"}],"description":"description","externalOptionsReferenceType":"externalOptionsReferenceType","label":"label","type":"string","externalOptions":True,"fieldType":"booleancheckbox","optionsUrl":"optionsUrl"},"supportedValueTypes":["STATIC_VALUE","STATIC_VALUE"]},{"isRequired":True,"automationFieldType":"automationFieldType","typeDefinition":{"helpText":"helpText","referencedObjectType":"CONTACT","name":"name","options":[{"hidden":True,"displayOrder":6,"doubleData":1.4658129805029452,"description":"description","readOnly":True,"label":"label","value":"value"},{"hidden":True,"displayOrder":6,"doubleData":1.4658129805029452,"description":"description","readOnly":True,"label":"label","value":"value"}],"description":"description","externalOptionsReferenceType":"externalOptionsReferenceType","label":"label","type":"string","externalOptions":True,"fieldType":"booleancheckbox","optionsUrl":"optionsUrl"},"supportedValueTypes":["STATIC_VALUE","STATIC_VALUE"]}],"outputFields":[{"typeDefinition":{"helpText":"helpText","referencedObjectType":"CONTACT","name":"name","options":[{"hidden":True,"displayOrder":6,"doubleData":1.4658129805029452,"description":"description","readOnly":True,"label":"label","value":"value"},{"hidden":True,"displayOrder":6,"doubleData":1.4658129805029452,"description":"description","readOnly":True,"label":"label","value":"value"}],"description":"description","externalOptionsReferenceType":"externalOptionsReferenceType","label":"label","type":"string","externalOptions":True,"fieldType":"booleancheckbox","optionsUrl":"optionsUrl"}},{"typeDefinition":{"helpText":"helpText","referencedObjectType":"CONTACT","name":"name","options":[{"hidden":True,"displayOrder":6,"doubleData":1.4658129805029452,"description":"description","readOnly":True,"label":"label","value":"value"},{"hidden":True,"displayOrder":6,"doubleData":1.4658129805029452,"description":"description","readOnly":True,"label":"label","value":"value"}],"description":"description","externalOptionsReferenceType":"externalOptionsReferenceType","label":"label","type":"string","externalOptions":True,"fieldType":"booleancheckbox","optionsUrl":"optionsUrl"}}],"archivedAt":0,"functions":[{"functionSource":"functionSource","functionType":"PRE_ACTION_EXECUTION","id":"id"},{"functionSource":"functionSource","functionType":"PRE_ACTION_EXECUTION","id":"id"}],"actionUrl":"actionUrl","inputFieldDependencies":[{"dependencyType":"SINGLE_FIELD","controllingFieldName":"controllingFieldName","dependentFieldNames":["dependentFieldNames","dependentFieldNames"]},{"dependencyType":"SINGLE_FIELD","controllingFieldName":"controllingFieldName","dependentFieldNames":["dependentFieldNames","dependentFieldNames"]}],"executionRules":[{"conditions":{"key":"{}"},"labelName":"labelName"},{"conditions":{"key":"{}"},"labelName":"labelName"}],"published":True,"objectTypes":["objectTypes","objectTypes"],"labels":{"key":{"inputFieldDescriptions":{"key":"inputFieldDescriptions"},"appDisplayName":"appDisplayName","outputFieldLabels":{"key":"outputFieldLabels"},"actionDescription":"actionDescription","executionRules":{"key":"executionRules"},"inputFieldOptionLabels":{"key":{"key":"inputFieldOptionLabels"}},"actionCardContent":"actionCardContent","actionName":"actionName","inputFieldLabels":{"key":"inputFieldLabels"}}},"objectRequestOptions":{"properties":["properties","properties"]}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'developer_hapikey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/automation/v4/actions/{app_id}'.format(app_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

