from typing import List, Dict
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
from openapi_server.models.child_entity_model_create_object import ChildEntityModelCreateObject
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
from openapi_server.models.entity_model_create_object import EntityModelCreateObject
from openapi_server.models.entity_model_update_object import EntityModelUpdateObject
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
from openapi_server.models.intent_classifier import IntentClassifier
from openapi_server.models.intents_suggestion_example import IntentsSuggestionExample
from openapi_server.models.label_example_response import LabelExampleResponse
from openapi_server.models.label_text_object import LabelTextObject
from openapi_server.models.labeled_utterance import LabeledUtterance
from openapi_server.models.luis_app import LuisApp
from openapi_server.models.model_add_composite_entity_child_request import ModelAddCompositeEntityChildRequest
from openapi_server.models.model_create_object import ModelCreateObject
from openapi_server.models.model_feature_information import ModelFeatureInformation
from openapi_server.models.model_info_response import ModelInfoResponse
from openapi_server.models.model_training_info import ModelTrainingInfo
from openapi_server.models.model_update_object import ModelUpdateObject
from openapi_server.models.n_depth_entity_extractor import NDepthEntityExtractor
from openapi_server.models.operation_status import OperationStatus
from openapi_server.models.pattern_any_entity_extractor import PatternAnyEntityExtractor
from openapi_server.models.pattern_any_model_create_object import PatternAnyModelCreateObject
from openapi_server.models.pattern_any_model_update_object import PatternAnyModelUpdateObject
from openapi_server.models.pattern_rule_create_object import PatternRuleCreateObject
from openapi_server.models.pattern_rule_info import PatternRuleInfo
from openapi_server.models.pattern_rule_update_object import PatternRuleUpdateObject
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
from openapi_server import util


async def apps_add(request: web.Request, application_create_object) -> web.Response:
    """apps_add

    Creates a new LUIS app.

    :param application_create_object: An application containing Name, Description (optional), Culture, Usage Scenario (optional), Domain (optional) and initial version ID (optional) of the application. Default value for the version ID is \&quot;0.1\&quot;. Note: the culture cannot be changed after the app is created.
    :type application_create_object: dict | bytes

    """
    application_create_object = ApplicationCreateObject.from_dict(application_create_object)
    return web.Response(status=200)


async def apps_add_custom_prebuilt_domain(request: web.Request, prebuilt_domain_create_object) -> web.Response:
    """apps_add_custom_prebuilt_domain

    Adds a prebuilt domain along with its intent and entity models as a new application.

    :param prebuilt_domain_create_object: A prebuilt domain create object containing the name and culture of the domain.
    :type prebuilt_domain_create_object: dict | bytes

    """
    prebuilt_domain_create_object = PrebuiltDomainCreateObject.from_dict(prebuilt_domain_create_object)
    return web.Response(status=200)


async def apps_delete(request: web.Request, app_id, force=None) -> web.Response:
    """apps_delete

    Deletes an application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param force: A flag to indicate whether to force an operation.
    :type force: bool

    """
    return web.Response(status=200)


async def apps_download_query_logs(request: web.Request, app_id) -> web.Response:
    """apps_download_query_logs

    Gets the logs of the past month&#39;s endpoint queries for the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str

    """
    return web.Response(status=200)


async def apps_get(request: web.Request, app_id) -> web.Response:
    """apps_get

    Gets the application info.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str

    """
    return web.Response(status=200)


async def apps_get_publish_settings(request: web.Request, app_id) -> web.Response:
    """apps_get_publish_settings

    Get the application publish settings including &#39;UseAllTrainingData&#39;.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str

    """
    return web.Response(status=200)


async def apps_get_settings(request: web.Request, app_id) -> web.Response:
    """apps_get_settings

    Get the application settings including &#39;UseAllTrainingData&#39;.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str

    """
    return web.Response(status=200)


async def apps_import(request: web.Request, luis_app, app_name=None) -> web.Response:
    """apps_import

    Imports an application to LUIS, the application&#39;s structure is included in the request body.

    :param luis_app: A LUIS application structure.
    :type luis_app: dict | bytes
    :param app_name: The application name to create. If not specified, the application name will be read from the imported object. If the application name already exists, an error is returned.
    :type app_name: str

    """
    luis_app = LuisApp.from_dict(luis_app)
    return web.Response(status=200)


async def apps_list(request: web.Request, skip=None, take=None) -> web.Response:
    """apps_list

    Lists all of the user&#39;s applications.

    :param skip: The number of entries to skip. Default value is 0.
    :type skip: int
    :param take: The number of entries to return. Maximum page size is 500. Default is 100.
    :type take: int

    """
    return web.Response(status=200)


async def apps_list_available_custom_prebuilt_domains(request: web.Request, ) -> web.Response:
    """apps_list_available_custom_prebuilt_domains

    Gets all the available custom prebuilt domains for all cultures.


    """
    return web.Response(status=200)


async def apps_list_available_custom_prebuilt_domains_for_culture(request: web.Request, culture) -> web.Response:
    """apps_list_available_custom_prebuilt_domains_for_culture

    Gets all the available prebuilt domains for a specific culture.

    :param culture: Culture.
    :type culture: str

    """
    return web.Response(status=200)


async def apps_list_cortana_endpoints(request: web.Request, ) -> web.Response:
    """apps_list_cortana_endpoints

    Gets the endpoint URLs for the prebuilt Cortana applications.


    """
    return web.Response(status=200)


async def apps_list_domains(request: web.Request, ) -> web.Response:
    """apps_list_domains

    Gets the available application domains.


    """
    return web.Response(status=200)


async def apps_list_endpoints(request: web.Request, app_id) -> web.Response:
    """apps_list_endpoints

    Returns the available endpoint deployment regions and URLs.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str

    """
    return web.Response(status=200)


async def apps_list_supported_cultures(request: web.Request, ) -> web.Response:
    """apps_list_supported_cultures

    Gets a list of supported cultures. Cultures are equivalent to the written language and locale. For example,\&quot;en-us\&quot; represents the U.S. variation of English.


    """
    return web.Response(status=200)


async def apps_list_usage_scenarios(request: web.Request, ) -> web.Response:
    """apps_list_usage_scenarios

    Gets the application available usage scenarios.


    """
    return web.Response(status=200)


async def apps_package_published_application_as_gzip(request: web.Request, app_id, slot_name) -> web.Response:
    """package - Gets published LUIS application package in binary stream GZip format

    Packages a published LUIS application as a GZip file to be used in the LUIS container.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param slot_name: The publishing slot name.
    :type slot_name: str

    """
    return web.Response(status=200)


async def apps_package_trained_application_as_gzip(request: web.Request, app_id, version_id) -> web.Response:
    """package - Gets trained LUIS application package in binary stream GZip format

    Packages trained LUIS application as GZip file to be used in the LUIS container.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str

    """
    return web.Response(status=200)


async def apps_publish(request: web.Request, app_id, application_publish_object) -> web.Response:
    """apps_publish

    Publishes a specific version of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param application_publish_object: The application publish object. The region is the target region that the application is published to.
    :type application_publish_object: dict | bytes

    """
    application_publish_object = ApplicationPublishObject.from_dict(application_publish_object)
    return web.Response(status=200)


async def apps_update(request: web.Request, app_id, application_update_object) -> web.Response:
    """apps_update

    Updates the name or description of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param application_update_object: A model containing Name and Description of the application.
    :type application_update_object: dict | bytes

    """
    application_update_object = ApplicationUpdateObject.from_dict(application_update_object)
    return web.Response(status=200)


async def apps_update_publish_settings(request: web.Request, app_id, publish_setting_update_object) -> web.Response:
    """apps_update_publish_settings

    Updates the application publish settings including &#39;UseAllTrainingData&#39;.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param publish_setting_update_object: An object containing the new publish application settings.
    :type publish_setting_update_object: dict | bytes

    """
    publish_setting_update_object = PublishSettingUpdateObject.from_dict(publish_setting_update_object)
    return web.Response(status=200)


async def apps_update_settings(request: web.Request, app_id, application_setting_update_object) -> web.Response:
    """apps_update_settings

    Updates the application settings including &#39;UseAllTrainingData&#39;.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param application_setting_update_object: An object containing the new application settings.
    :type application_setting_update_object: dict | bytes

    """
    application_setting_update_object = ApplicationSettingUpdateObject.from_dict(application_setting_update_object)
    return web.Response(status=200)


async def azure_accounts_assign_to_app(request: web.Request, app_id, authorization, azure_account_info_object=None) -> web.Response:
    """apps - Assign a LUIS Azure account to an application

    Assigns an Azure account to the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param authorization: The bearer authorization header to use; containing the user&#39;s ARM token used to validate Azure accounts information.
    :type authorization: str
    :param azure_account_info_object: The Azure account information object.
    :type azure_account_info_object: dict | bytes

    """
    azure_account_info_object = AzureAccountInfoObject.from_dict(azure_account_info_object)
    return web.Response(status=200)


async def azure_accounts_get_assigned(request: web.Request, app_id, authorization) -> web.Response:
    """apps - Get LUIS Azure accounts assigned to the application

    Gets the LUIS Azure accounts assigned to the application for the user using his ARM token.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param authorization: The bearer authorization header to use; containing the user&#39;s ARM token used to validate Azure accounts information.
    :type authorization: str

    """
    return web.Response(status=200)


async def azure_accounts_list_user_luis_accounts(request: web.Request, authorization) -> web.Response:
    """user - Get LUIS Azure accounts

    Gets the LUIS Azure accounts for the user using his ARM token.

    :param authorization: The bearer authorization header to use; containing the user&#39;s ARM token used to validate Azure accounts information.
    :type authorization: str

    """
    return web.Response(status=200)


async def azure_accounts_remove_from_app(request: web.Request, app_id, authorization, azure_account_info_object=None) -> web.Response:
    """apps - Removes an assigned LUIS Azure account from an application

    Removes assigned Azure account from the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param authorization: The bearer authorization header to use; containing the user&#39;s ARM token used to validate Azure accounts information.
    :type authorization: str
    :param azure_account_info_object: The Azure account information object.
    :type azure_account_info_object: dict | bytes

    """
    azure_account_info_object = AzureAccountInfoObject.from_dict(azure_account_info_object)
    return web.Response(status=200)


async def examples_add(request: web.Request, app_id, version_id, example_label_object) -> web.Response:
    """examples_add

    Adds a labeled example utterance in a version of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param example_label_object: A labeled example utterance with the expected intent and entities.
    :type example_label_object: dict | bytes

    """
    example_label_object = ExampleLabelObject.from_dict(example_label_object)
    return web.Response(status=200)


async def examples_batch(request: web.Request, app_id, version_id, example_label_object_array) -> web.Response:
    """examples_batch

    Adds a batch of labeled example utterances to a version of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param example_label_object_array: Array of example utterances.
    :type example_label_object_array: list | bytes

    """
    example_label_object_array = [ExampleLabelObject.from_dict(d) for d in example_label_object_array]
    return web.Response(status=200)


async def examples_delete(request: web.Request, app_id, version_id, example_id) -> web.Response:
    """examples_delete

    Deletes the labeled example utterances with the specified ID from a version of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param example_id: The example ID.
    :type example_id: int

    """
    return web.Response(status=200)


async def examples_list(request: web.Request, app_id, version_id, skip=None, take=None) -> web.Response:
    """examples_list

    Returns example utterances to be reviewed from a version of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param skip: The number of entries to skip. Default value is 0.
    :type skip: int
    :param take: The number of entries to return. Maximum page size is 500. Default is 100.
    :type take: int

    """
    return web.Response(status=200)


async def features_add_entity_feature(request: web.Request, app_id, version_id, entity_id, feature_relation_create_object) -> web.Response:
    """features_add_entity_feature

    Adds a new feature relation to be used by the entity in a version of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param entity_id: The entity extractor ID.
    :type entity_id: str
    :type entity_id: str
    :param feature_relation_create_object: A Feature relation information object.
    :type feature_relation_create_object: dict | bytes

    """
    feature_relation_create_object = ModelFeatureInformation.from_dict(feature_relation_create_object)
    return web.Response(status=200)


async def features_add_intent_feature(request: web.Request, app_id, version_id, intent_id, feature_relation_create_object) -> web.Response:
    """features_add_intent_feature

    Adds a new feature relation to be used by the intent in a version of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param intent_id: The intent classifier ID.
    :type intent_id: str
    :type intent_id: str
    :param feature_relation_create_object: A Feature relation information object.
    :type feature_relation_create_object: dict | bytes

    """
    feature_relation_create_object = ModelFeatureInformation.from_dict(feature_relation_create_object)
    return web.Response(status=200)


async def features_add_phrase_list(request: web.Request, app_id, version_id, phraselist_create_object) -> web.Response:
    """features_add_phrase_list

    Creates a new phraselist feature in a version of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param phraselist_create_object: A Phraselist object containing Name, comma-separated Phrases and the isExchangeable boolean. Default value for isExchangeable is true.
    :type phraselist_create_object: dict | bytes

    """
    phraselist_create_object = PhraselistCreateObject.from_dict(phraselist_create_object)
    return web.Response(status=200)


async def features_delete_phrase_list(request: web.Request, app_id, version_id, phraselist_id) -> web.Response:
    """features_delete_phrase_list

    Deletes a phraselist feature from a version of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param phraselist_id: The ID of the feature to be deleted.
    :type phraselist_id: int

    """
    return web.Response(status=200)


async def features_get_phrase_list(request: web.Request, app_id, version_id, phraselist_id) -> web.Response:
    """features_get_phrase_list

    Gets phraselist feature info in a version of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param phraselist_id: The ID of the feature to be retrieved.
    :type phraselist_id: int

    """
    return web.Response(status=200)


async def features_list(request: web.Request, app_id, version_id, skip=None, take=None) -> web.Response:
    """features_list

    Gets all the extraction phraselist and pattern features in a version of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param skip: The number of entries to skip. Default value is 0.
    :type skip: int
    :param take: The number of entries to return. Maximum page size is 500. Default is 100.
    :type take: int

    """
    return web.Response(status=200)


async def features_list_phrase_lists(request: web.Request, app_id, version_id, skip=None, take=None) -> web.Response:
    """features_list_phrase_lists

    Gets all the phraselist features in a version of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param skip: The number of entries to skip. Default value is 0.
    :type skip: int
    :param take: The number of entries to return. Maximum page size is 500. Default is 100.
    :type take: int

    """
    return web.Response(status=200)


async def features_update_phrase_list(request: web.Request, app_id, version_id, phraselist_id, phraselist_update_object=None) -> web.Response:
    """features_update_phrase_list

    Updates the phrases, the state and the name of the phraselist feature in a version of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param phraselist_id: The ID of the feature to be updated.
    :type phraselist_id: int
    :param phraselist_update_object: The new values for: - Just a boolean called IsActive, in which case the status of the feature will be changed. - Name, Pattern, Mode, and a boolean called IsActive to update the feature.
    :type phraselist_update_object: dict | bytes

    """
    phraselist_update_object = PhraselistUpdateObject.from_dict(phraselist_update_object)
    return web.Response(status=200)


async def model_add_closed_list(request: web.Request, app_id, version_id, closed_list_model_create_object) -> web.Response:
    """model_add_closed_list

    Adds a list entity model to a version of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param closed_list_model_create_object: A model containing the name and words for the new list entity extractor.
    :type closed_list_model_create_object: dict | bytes

    """
    closed_list_model_create_object = ClosedListModelCreateObject.from_dict(closed_list_model_create_object)
    return web.Response(status=200)


async def model_add_composite_entity_child(request: web.Request, app_id, version_id, c_entity_id, composite_child_model_create_object) -> web.Response:
    """model_add_composite_entity_child

    Creates a single child in an existing composite entity model in a version of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param c_entity_id: The composite entity extractor ID.
    :type c_entity_id: str
    :type c_entity_id: str
    :param composite_child_model_create_object: A model object containing the name of the new composite child model.
    :type composite_child_model_create_object: dict | bytes

    """
    composite_child_model_create_object = ModelAddCompositeEntityChildRequest.from_dict(composite_child_model_create_object)
    return web.Response(status=200)


async def model_add_custom_prebuilt_domain(request: web.Request, app_id, version_id, prebuilt_domain_object) -> web.Response:
    """model_add_custom_prebuilt_domain

    Adds a customizable prebuilt domain along with all of its intent and entity models in a version of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param prebuilt_domain_object: A prebuilt domain create object containing the name of the domain.
    :type prebuilt_domain_object: dict | bytes

    """
    prebuilt_domain_object = PrebuiltDomainCreateBaseObject.from_dict(prebuilt_domain_object)
    return web.Response(status=200)


async def model_add_custom_prebuilt_entity(request: web.Request, app_id, version_id, prebuilt_domain_model_create_object) -> web.Response:
    """model_add_custom_prebuilt_entity

    Adds a prebuilt entity model to a version of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param prebuilt_domain_model_create_object: A model object containing the name of the prebuilt entity and the name of the domain to which this model belongs.
    :type prebuilt_domain_model_create_object: dict | bytes

    """
    prebuilt_domain_model_create_object = PrebuiltDomainModelCreateObject.from_dict(prebuilt_domain_model_create_object)
    return web.Response(status=200)


async def model_add_custom_prebuilt_intent(request: web.Request, app_id, version_id, prebuilt_domain_model_create_object) -> web.Response:
    """model_add_custom_prebuilt_intent

    Adds a customizable prebuilt intent model to a version of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param prebuilt_domain_model_create_object: A model object containing the name of the customizable prebuilt intent and the name of the domain to which this model belongs.
    :type prebuilt_domain_model_create_object: dict | bytes

    """
    prebuilt_domain_model_create_object = PrebuiltDomainModelCreateObject.from_dict(prebuilt_domain_model_create_object)
    return web.Response(status=200)


async def model_add_entity(request: web.Request, app_id, version_id, entity_model_create_object) -> web.Response:
    """model_add_entity

    Adds an entity extractor to a version of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param entity_model_create_object: A model object containing the name of the new entity extractor and its children.
    :type entity_model_create_object: dict | bytes

    """
    entity_model_create_object = EntityModelCreateObject.from_dict(entity_model_create_object)
    return web.Response(status=200)


async def model_add_entity_child(request: web.Request, app_id, version_id, entity_id, child_entity_model_create_object) -> web.Response:
    """model_add_entity_child

    Creates a single child in an existing entity model hierarchy in a version of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param entity_id: The entity extractor ID.
    :type entity_id: str
    :type entity_id: str
    :param child_entity_model_create_object: A model object containing the name of the new child model and its children.
    :type child_entity_model_create_object: dict | bytes

    """
    child_entity_model_create_object = ChildEntityModelCreateObject.from_dict(child_entity_model_create_object)
    return web.Response(status=200)


async def model_add_explicit_list_item(request: web.Request, app_id, version_id, entity_id, item) -> web.Response:
    """Add a new exception to the explicit list for the Pattern.Any entity in a version of the application.

    

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param entity_id: The Pattern.Any entity extractor ID.
    :type entity_id: str
    :type entity_id: str
    :param item: The new explicit list item.
    :type item: dict | bytes

    """
    item = ExplicitListItemCreateObject.from_dict(item)
    return web.Response(status=200)


async def model_add_intent(request: web.Request, app_id, version_id, intent_create_object) -> web.Response:
    """model_add_intent

    Adds an intent to a version of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param intent_create_object: A model object containing the name of the new intent.
    :type intent_create_object: dict | bytes

    """
    intent_create_object = ModelCreateObject.from_dict(intent_create_object)
    return web.Response(status=200)


async def model_add_prebuilt(request: web.Request, app_id, version_id, prebuilt_extractor_names) -> web.Response:
    """model_add_prebuilt

    Adds a list of prebuilt entities to a version of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param prebuilt_extractor_names: An array of prebuilt entity extractor names.
    :type prebuilt_extractor_names: List[str]

    """
    return web.Response(status=200)


async def model_add_sub_list(request: web.Request, app_id, version_id, cl_entity_id, word_list_create_object) -> web.Response:
    """model_add_sub_list

    Adds a sublist to an existing list entity in a version of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param cl_entity_id: The list entity extractor ID.
    :type cl_entity_id: str
    :type cl_entity_id: str
    :param word_list_create_object: Words list.
    :type word_list_create_object: dict | bytes

    """
    word_list_create_object = WordListObject.from_dict(word_list_create_object)
    return web.Response(status=200)


async def model_create_closed_list_entity_role(request: web.Request, app_id, version_id, entity_id, entity_role_create_object) -> web.Response:
    """Create a role for a list entity in a version of the application.

    

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param entity_id: The entity model ID.
    :type entity_id: str
    :type entity_id: str
    :param entity_role_create_object: An entity role object containing the name of role.
    :type entity_role_create_object: dict | bytes

    """
    entity_role_create_object = EntityRoleCreateObject.from_dict(entity_role_create_object)
    return web.Response(status=200)


async def model_create_composite_entity_role(request: web.Request, app_id, version_id, c_entity_id, entity_role_create_object) -> web.Response:
    """Create a role for a composite entity in a version of the application.

    

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param c_entity_id: The composite entity extractor ID.
    :type c_entity_id: str
    :type c_entity_id: str
    :param entity_role_create_object: An entity role object containing the name of role.
    :type entity_role_create_object: dict | bytes

    """
    entity_role_create_object = EntityRoleCreateObject.from_dict(entity_role_create_object)
    return web.Response(status=200)


async def model_create_custom_prebuilt_entity_role(request: web.Request, app_id, version_id, entity_id, entity_role_create_object) -> web.Response:
    """Create a role for a prebuilt entity in a version of the application.

    

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param entity_id: The entity model ID.
    :type entity_id: str
    :type entity_id: str
    :param entity_role_create_object: An entity role object containing the name of role.
    :type entity_role_create_object: dict | bytes

    """
    entity_role_create_object = EntityRoleCreateObject.from_dict(entity_role_create_object)
    return web.Response(status=200)


async def model_create_entity_role(request: web.Request, app_id, version_id, entity_id, entity_role_create_object) -> web.Response:
    """Create an entity role in a version of the application.

    

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param entity_id: The entity model ID.
    :type entity_id: str
    :type entity_id: str
    :param entity_role_create_object: An entity role object containing the name of role.
    :type entity_role_create_object: dict | bytes

    """
    entity_role_create_object = EntityRoleCreateObject.from_dict(entity_role_create_object)
    return web.Response(status=200)


async def model_create_hierarchical_entity_role(request: web.Request, app_id, version_id, h_entity_id, entity_role_create_object) -> web.Response:
    """Create a role for an hierarchical entity in a version of the application.

    

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param h_entity_id: The hierarchical entity extractor ID.
    :type h_entity_id: str
    :type h_entity_id: str
    :param entity_role_create_object: An entity role object containing the name of role.
    :type entity_role_create_object: dict | bytes

    """
    entity_role_create_object = EntityRoleCreateObject.from_dict(entity_role_create_object)
    return web.Response(status=200)


async def model_create_pattern_any_entity_model(request: web.Request, app_id, version_id, extractor_create_object) -> web.Response:
    """Adds a pattern.any entity extractor to a version of the application.

    

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param extractor_create_object: A model object containing the name and explicit list for the new Pattern.Any entity extractor.
    :type extractor_create_object: dict | bytes

    """
    extractor_create_object = PatternAnyModelCreateObject.from_dict(extractor_create_object)
    return web.Response(status=200)


async def model_create_pattern_any_entity_role(request: web.Request, app_id, version_id, entity_id, entity_role_create_object) -> web.Response:
    """Create a role for an Pattern.any entity in a version of the application.

    

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param entity_id: The entity model ID.
    :type entity_id: str
    :type entity_id: str
    :param entity_role_create_object: An entity role object containing the name of role.
    :type entity_role_create_object: dict | bytes

    """
    entity_role_create_object = EntityRoleCreateObject.from_dict(entity_role_create_object)
    return web.Response(status=200)


async def model_create_prebuilt_entity_role(request: web.Request, app_id, version_id, entity_id, entity_role_create_object) -> web.Response:
    """Create a role for a prebuilt entity in a version of the application.

    

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param entity_id: The entity model ID.
    :type entity_id: str
    :type entity_id: str
    :param entity_role_create_object: An entity role object containing the name of role.
    :type entity_role_create_object: dict | bytes

    """
    entity_role_create_object = EntityRoleCreateObject.from_dict(entity_role_create_object)
    return web.Response(status=200)


async def model_create_regex_entity_model(request: web.Request, app_id, version_id, regex_entity_extractor_create_obj) -> web.Response:
    """Adds a regular expression entity model to a version of the application.

    

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param regex_entity_extractor_create_obj: A model object containing the name and regex pattern for the new regular expression entity extractor.
    :type regex_entity_extractor_create_obj: dict | bytes

    """
    regex_entity_extractor_create_obj = RegexModelCreateObject.from_dict(regex_entity_extractor_create_obj)
    return web.Response(status=200)


async def model_create_regex_entity_role(request: web.Request, app_id, version_id, entity_id, entity_role_create_object) -> web.Response:
    """Create a role for an regular expression entity in a version of the application.

    

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param entity_id: The entity model ID.
    :type entity_id: str
    :type entity_id: str
    :param entity_role_create_object: An entity role object containing the name of role.
    :type entity_role_create_object: dict | bytes

    """
    entity_role_create_object = EntityRoleCreateObject.from_dict(entity_role_create_object)
    return web.Response(status=200)


async def model_delete_closed_list(request: web.Request, app_id, version_id, cl_entity_id) -> web.Response:
    """model_delete_closed_list

    Deletes a list entity model from a version of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param cl_entity_id: The list entity model ID.
    :type cl_entity_id: str
    :type cl_entity_id: str

    """
    return web.Response(status=200)


async def model_delete_closed_list_entity_role(request: web.Request, app_id, version_id, entity_id, role_id) -> web.Response:
    """Delete a role for a given list entity in a version of the application.

    

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param entity_id: The entity ID.
    :type entity_id: str
    :type entity_id: str
    :param role_id: The entity role Id.
    :type role_id: str
    :type role_id: str

    """
    return web.Response(status=200)


async def model_delete_composite_entity(request: web.Request, app_id, version_id, c_entity_id) -> web.Response:
    """model_delete_composite_entity

    Deletes a composite entity from a version of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param c_entity_id: The composite entity extractor ID.
    :type c_entity_id: str
    :type c_entity_id: str

    """
    return web.Response(status=200)


async def model_delete_composite_entity_child(request: web.Request, app_id, version_id, c_entity_id, c_child_id) -> web.Response:
    """model_delete_composite_entity_child

    Deletes a composite entity extractor child from a version of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param c_entity_id: The composite entity extractor ID.
    :type c_entity_id: str
    :type c_entity_id: str
    :param c_child_id: The hierarchical entity extractor child ID.
    :type c_child_id: str
    :type c_child_id: str

    """
    return web.Response(status=200)


async def model_delete_composite_entity_role(request: web.Request, app_id, version_id, c_entity_id, role_id) -> web.Response:
    """Delete a role for a given composite entity in a version of the application.

    

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param c_entity_id: The composite entity extractor ID.
    :type c_entity_id: str
    :type c_entity_id: str
    :param role_id: The entity role Id.
    :type role_id: str
    :type role_id: str

    """
    return web.Response(status=200)


async def model_delete_custom_entity_role(request: web.Request, app_id, version_id, entity_id, role_id) -> web.Response:
    """Delete a role for a given prebuilt entity in a version of the application.

    

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param entity_id: The entity ID.
    :type entity_id: str
    :type entity_id: str
    :param role_id: The entity role Id.
    :type role_id: str
    :type role_id: str

    """
    return web.Response(status=200)


async def model_delete_custom_prebuilt_domain(request: web.Request, app_id, version_id, domain_name) -> web.Response:
    """model_delete_custom_prebuilt_domain

    Deletes a prebuilt domain&#39;s models in a version of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param domain_name: Domain name.
    :type domain_name: str

    """
    return web.Response(status=200)


async def model_delete_entity(request: web.Request, app_id, version_id, entity_id) -> web.Response:
    """model_delete_entity

    Deletes an entity or a child from a version of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param entity_id: The entity extractor or the child entity extractor ID.
    :type entity_id: str
    :type entity_id: str

    """
    return web.Response(status=200)


async def model_delete_entity_feature(request: web.Request, app_id, version_id, entity_id, feature_relation_delete_object) -> web.Response:
    """model_delete_entity_feature

    Deletes a relation from the feature relations used by the entity in a version of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param entity_id: The entity extractor ID.
    :type entity_id: str
    :type entity_id: str
    :param feature_relation_delete_object: A feature information object containing the feature relation to delete.
    :type feature_relation_delete_object: dict | bytes

    """
    feature_relation_delete_object = ModelFeatureInformation.from_dict(feature_relation_delete_object)
    return web.Response(status=200)


async def model_delete_entity_role(request: web.Request, app_id, version_id, entity_id, role_id) -> web.Response:
    """Delete an entity role in a version of the application.

    

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param entity_id: The entity ID.
    :type entity_id: str
    :type entity_id: str
    :param role_id: The entity role Id.
    :type role_id: str
    :type role_id: str

    """
    return web.Response(status=200)


async def model_delete_explicit_list_item(request: web.Request, app_id, version_id, entity_id, item_id) -> web.Response:
    """Delete an item from the explicit (exception) list for a Pattern.any entity in a version of the application.

    

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param entity_id: The pattern.any entity id.
    :type entity_id: str
    :type entity_id: str
    :param item_id: The explicit list item which will be deleted.
    :type item_id: int

    """
    return web.Response(status=200)


async def model_delete_hierarchical_entity(request: web.Request, app_id, version_id, h_entity_id) -> web.Response:
    """model_delete_hierarchical_entity

    Deletes a hierarchical entity from a version of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param h_entity_id: The hierarchical entity extractor ID.
    :type h_entity_id: str
    :type h_entity_id: str

    """
    return web.Response(status=200)


async def model_delete_hierarchical_entity_child(request: web.Request, app_id, version_id, h_entity_id, h_child_id) -> web.Response:
    """model_delete_hierarchical_entity_child

    Deletes a hierarchical entity extractor child in a version of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param h_entity_id: The hierarchical entity extractor ID.
    :type h_entity_id: str
    :type h_entity_id: str
    :param h_child_id: The hierarchical entity extractor child ID.
    :type h_child_id: str
    :type h_child_id: str

    """
    return web.Response(status=200)


async def model_delete_hierarchical_entity_role(request: web.Request, app_id, version_id, h_entity_id, role_id) -> web.Response:
    """Delete a role for a given hierarchical role in a version of the application.

    

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param h_entity_id: The hierarchical entity extractor ID.
    :type h_entity_id: str
    :type h_entity_id: str
    :param role_id: The entity role Id.
    :type role_id: str
    :type role_id: str

    """
    return web.Response(status=200)


async def model_delete_intent(request: web.Request, app_id, version_id, intent_id, delete_utterances=None) -> web.Response:
    """model_delete_intent

    Deletes an intent from a version of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param intent_id: The intent classifier ID.
    :type intent_id: str
    :type intent_id: str
    :param delete_utterances: If true, deletes the intent&#39;s example utterances. If false, moves the example utterances to the None intent. The default value is false.
    :type delete_utterances: bool

    """
    return web.Response(status=200)


async def model_delete_intent_feature(request: web.Request, app_id, version_id, intent_id, feature_relation_delete_object) -> web.Response:
    """model_delete_intent_feature

    Deletes a relation from the feature relations used by the intent in a version of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param intent_id: The intent classifier ID.
    :type intent_id: str
    :type intent_id: str
    :param feature_relation_delete_object: A feature information object containing the feature relation to delete.
    :type feature_relation_delete_object: dict | bytes

    """
    feature_relation_delete_object = ModelFeatureInformation.from_dict(feature_relation_delete_object)
    return web.Response(status=200)


async def model_delete_pattern_any_entity_model(request: web.Request, app_id, version_id, entity_id) -> web.Response:
    """Deletes a Pattern.Any entity extractor from a version of the application.

    

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param entity_id: The Pattern.Any entity extractor ID.
    :type entity_id: str
    :type entity_id: str

    """
    return web.Response(status=200)


async def model_delete_pattern_any_entity_role(request: web.Request, app_id, version_id, entity_id, role_id) -> web.Response:
    """Delete a role for a given Pattern.any entity in a version of the application.

    

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param entity_id: The entity ID.
    :type entity_id: str
    :type entity_id: str
    :param role_id: The entity role Id.
    :type role_id: str
    :type role_id: str

    """
    return web.Response(status=200)


async def model_delete_prebuilt(request: web.Request, app_id, version_id, prebuilt_id) -> web.Response:
    """model_delete_prebuilt

    Deletes a prebuilt entity extractor from a version of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param prebuilt_id: The prebuilt entity extractor ID.
    :type prebuilt_id: str
    :type prebuilt_id: str

    """
    return web.Response(status=200)


async def model_delete_prebuilt_entity_role(request: web.Request, app_id, version_id, entity_id, role_id) -> web.Response:
    """Delete a role in a prebuilt entity in a version of the application.

    

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param entity_id: The entity ID.
    :type entity_id: str
    :type entity_id: str
    :param role_id: The entity role Id.
    :type role_id: str
    :type role_id: str

    """
    return web.Response(status=200)


async def model_delete_regex_entity_model(request: web.Request, app_id, version_id, regex_entity_id) -> web.Response:
    """Deletes a regular expression entity from a version of the application.

    

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param regex_entity_id: The regular expression entity extractor ID.
    :type regex_entity_id: str
    :type regex_entity_id: str

    """
    return web.Response(status=200)


async def model_delete_regex_entity_role(request: web.Request, app_id, version_id, entity_id, role_id) -> web.Response:
    """Delete a role for a given regular expression in a version of the application.

    

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param entity_id: The entity ID.
    :type entity_id: str
    :type entity_id: str
    :param role_id: The entity role Id.
    :type role_id: str
    :type role_id: str

    """
    return web.Response(status=200)


async def model_delete_sub_list(request: web.Request, app_id, version_id, cl_entity_id, sub_list_id) -> web.Response:
    """model_delete_sub_list

    Deletes a sublist of a specific list entity model from a version of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param cl_entity_id: The list entity extractor ID.
    :type cl_entity_id: str
    :type cl_entity_id: str
    :param sub_list_id: The sublist ID.
    :type sub_list_id: int

    """
    return web.Response(status=200)


async def model_examples(request: web.Request, app_id, version_id, model_id, skip=None, take=None) -> web.Response:
    """model_examples

    Gets the example utterances for the given intent or entity model in a version of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param model_id: The ID (GUID) of the model.
    :type model_id: str
    :param skip: The number of entries to skip. Default value is 0.
    :type skip: int
    :param take: The number of entries to return. Maximum page size is 500. Default is 100.
    :type take: int

    """
    return web.Response(status=200)


async def model_get_closed_list(request: web.Request, app_id, version_id, cl_entity_id) -> web.Response:
    """model_get_closed_list

    Gets information about a list entity in a version of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param cl_entity_id: The list model ID.
    :type cl_entity_id: str
    :type cl_entity_id: str

    """
    return web.Response(status=200)


async def model_get_closed_list_entity_role(request: web.Request, app_id, version_id, entity_id, role_id) -> web.Response:
    """Get one role for a given list entity in a version of the application.

    

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param entity_id: entity ID.
    :type entity_id: str
    :type entity_id: str
    :param role_id: entity role ID.
    :type role_id: str
    :type role_id: str

    """
    return web.Response(status=200)


async def model_get_composite_entity(request: web.Request, app_id, version_id, c_entity_id) -> web.Response:
    """model_get_composite_entity

    Gets information about a composite entity in a version of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param c_entity_id: The composite entity extractor ID.
    :type c_entity_id: str
    :type c_entity_id: str

    """
    return web.Response(status=200)


async def model_get_composite_entity_role(request: web.Request, app_id, version_id, c_entity_id, role_id) -> web.Response:
    """Get one role for a given composite entity in a version of the application

    

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param c_entity_id: The composite entity extractor ID.
    :type c_entity_id: str
    :type c_entity_id: str
    :param role_id: entity role ID.
    :type role_id: str
    :type role_id: str

    """
    return web.Response(status=200)


async def model_get_custom_entity_role(request: web.Request, app_id, version_id, entity_id, role_id) -> web.Response:
    """Get one role for a given prebuilt entity in a version of the application.

    

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param entity_id: entity ID.
    :type entity_id: str
    :type entity_id: str
    :param role_id: entity role ID.
    :type role_id: str
    :type role_id: str

    """
    return web.Response(status=200)


async def model_get_entity(request: web.Request, app_id, version_id, entity_id) -> web.Response:
    """model_get_entity

    Gets information about an entity model in a version of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param entity_id: The entity extractor ID.
    :type entity_id: str
    :type entity_id: str

    """
    return web.Response(status=200)


async def model_get_entity_features(request: web.Request, app_id, version_id, entity_id) -> web.Response:
    """model_get_entity_features

    Gets the information of the features used by the entity in a version of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param entity_id: The entity extractor ID.
    :type entity_id: str
    :type entity_id: str

    """
    return web.Response(status=200)


async def model_get_entity_role(request: web.Request, app_id, version_id, entity_id, role_id) -> web.Response:
    """Get one role for a given entity in a version of the application

    

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param entity_id: entity ID.
    :type entity_id: str
    :type entity_id: str
    :param role_id: entity role ID.
    :type role_id: str
    :type role_id: str

    """
    return web.Response(status=200)


async def model_get_explicit_list(request: web.Request, app_id, version_id, entity_id) -> web.Response:
    """Get the explicit (exception) list of the pattern.any entity in a version of the application.

    

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param entity_id: The Pattern.Any entity id.
    :type entity_id: str
    :type entity_id: str

    """
    return web.Response(status=200)


async def model_get_explicit_list_item(request: web.Request, app_id, version_id, entity_id, item_id) -> web.Response:
    """Get the explicit (exception) list of the pattern.any entity in a version of the application.

    

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param entity_id: The Pattern.Any entity Id.
    :type entity_id: str
    :type entity_id: str
    :param item_id: The explicit list item Id.
    :type item_id: int

    """
    return web.Response(status=200)


async def model_get_hierarchical_entity(request: web.Request, app_id, version_id, h_entity_id) -> web.Response:
    """model_get_hierarchical_entity

    Gets information about a hierarchical entity in a version of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param h_entity_id: The hierarchical entity extractor ID.
    :type h_entity_id: str
    :type h_entity_id: str

    """
    return web.Response(status=200)


async def model_get_hierarchical_entity_child(request: web.Request, app_id, version_id, h_entity_id, h_child_id) -> web.Response:
    """model_get_hierarchical_entity_child

    Gets information about the child&#39;s model contained in an hierarchical entity child model in a version of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param h_entity_id: The hierarchical entity extractor ID.
    :type h_entity_id: str
    :type h_entity_id: str
    :param h_child_id: The hierarchical entity extractor child ID.
    :type h_child_id: str
    :type h_child_id: str

    """
    return web.Response(status=200)


async def model_get_hierarchical_entity_role(request: web.Request, app_id, version_id, h_entity_id, role_id) -> web.Response:
    """Get one role for a given hierarchical entity in a version of the application.

    

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param h_entity_id: The hierarchical entity extractor ID.
    :type h_entity_id: str
    :type h_entity_id: str
    :param role_id: entity role ID.
    :type role_id: str
    :type role_id: str

    """
    return web.Response(status=200)


async def model_get_intent(request: web.Request, app_id, version_id, intent_id) -> web.Response:
    """model_get_intent

    Gets information about the intent model in a version of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param intent_id: The intent classifier ID.
    :type intent_id: str
    :type intent_id: str

    """
    return web.Response(status=200)


async def model_get_intent_features(request: web.Request, app_id, version_id, intent_id) -> web.Response:
    """model_get_intent_features

    Gets the information of the features used by the intent in a version of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param intent_id: The intent classifier ID.
    :type intent_id: str
    :type intent_id: str

    """
    return web.Response(status=200)


async def model_get_pattern_any_entity_info(request: web.Request, app_id, version_id, entity_id) -> web.Response:
    """Gets information about the Pattern.Any model in a version of the application.

    

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param entity_id: The entity extractor ID.
    :type entity_id: str
    :type entity_id: str

    """
    return web.Response(status=200)


async def model_get_pattern_any_entity_role(request: web.Request, app_id, version_id, entity_id, role_id) -> web.Response:
    """Get one role for a given Pattern.any entity in a version of the application.

    

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param entity_id: entity ID.
    :type entity_id: str
    :type entity_id: str
    :param role_id: entity role ID.
    :type role_id: str
    :type role_id: str

    """
    return web.Response(status=200)


async def model_get_prebuilt(request: web.Request, app_id, version_id, prebuilt_id) -> web.Response:
    """model_get_prebuilt

    Gets information about a prebuilt entity model in a version of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param prebuilt_id: The prebuilt entity extractor ID.
    :type prebuilt_id: str
    :type prebuilt_id: str

    """
    return web.Response(status=200)


async def model_get_prebuilt_entity_role(request: web.Request, app_id, version_id, entity_id, role_id) -> web.Response:
    """Get one role for a given prebuilt entity in a version of the application

    

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param entity_id: entity ID.
    :type entity_id: str
    :type entity_id: str
    :param role_id: entity role ID.
    :type role_id: str
    :type role_id: str

    """
    return web.Response(status=200)


async def model_get_regex_entity_entity_info(request: web.Request, app_id, version_id, regex_entity_id) -> web.Response:
    """Gets information about a regular expression entity in a version of the application.

    

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param regex_entity_id: The regular expression entity model ID.
    :type regex_entity_id: str
    :type regex_entity_id: str

    """
    return web.Response(status=200)


async def model_get_regex_entity_role(request: web.Request, app_id, version_id, entity_id, role_id) -> web.Response:
    """Get one role for a given regular expression entity in a version of the application.

    

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param entity_id: entity ID.
    :type entity_id: str
    :type entity_id: str
    :param role_id: entity role ID.
    :type role_id: str
    :type role_id: str

    """
    return web.Response(status=200)


async def model_list_closed_list_entity_roles(request: web.Request, app_id, version_id, entity_id) -> web.Response:
    """Get all roles for a list entity in a version of the application.

    

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param entity_id: entity Id
    :type entity_id: str
    :type entity_id: str

    """
    return web.Response(status=200)


async def model_list_closed_lists(request: web.Request, app_id, version_id, skip=None, take=None) -> web.Response:
    """model_list_closed_lists

    Gets information about all the list entity models in a version of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param skip: The number of entries to skip. Default value is 0.
    :type skip: int
    :param take: The number of entries to return. Maximum page size is 500. Default is 100.
    :type take: int

    """
    return web.Response(status=200)


async def model_list_composite_entities(request: web.Request, app_id, version_id, skip=None, take=None) -> web.Response:
    """model_list_composite_entities

    Gets information about all the composite entity models in a version of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param skip: The number of entries to skip. Default value is 0.
    :type skip: int
    :param take: The number of entries to return. Maximum page size is 500. Default is 100.
    :type take: int

    """
    return web.Response(status=200)


async def model_list_composite_entity_roles(request: web.Request, app_id, version_id, c_entity_id) -> web.Response:
    """Get all roles for a composite entity in a version of the application

    

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param c_entity_id: The composite entity extractor ID.
    :type c_entity_id: str
    :type c_entity_id: str

    """
    return web.Response(status=200)


async def model_list_custom_prebuilt_entities(request: web.Request, app_id, version_id) -> web.Response:
    """model_list_custom_prebuilt_entities

    Gets all prebuilt entities used in a version of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str

    """
    return web.Response(status=200)


async def model_list_custom_prebuilt_entity_roles(request: web.Request, app_id, version_id, entity_id) -> web.Response:
    """Get all roles for a prebuilt entity in a version of the application

    

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param entity_id: entity Id
    :type entity_id: str
    :type entity_id: str

    """
    return web.Response(status=200)


async def model_list_custom_prebuilt_intents(request: web.Request, app_id, version_id) -> web.Response:
    """model_list_custom_prebuilt_intents

    Gets information about customizable prebuilt intents added to a version of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str

    """
    return web.Response(status=200)


async def model_list_custom_prebuilt_models(request: web.Request, app_id, version_id) -> web.Response:
    """model_list_custom_prebuilt_models

    Gets all prebuilt intent and entity model information used in a version of this application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str

    """
    return web.Response(status=200)


async def model_list_entities(request: web.Request, app_id, version_id, skip=None, take=None) -> web.Response:
    """model_list_entities

    Gets information about all the simple entity models in a version of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param skip: The number of entries to skip. Default value is 0.
    :type skip: int
    :param take: The number of entries to return. Maximum page size is 500. Default is 100.
    :type take: int

    """
    return web.Response(status=200)


async def model_list_entity_roles(request: web.Request, app_id, version_id, entity_id) -> web.Response:
    """Get all roles for an entity in a version of the application

    

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param entity_id: entity Id
    :type entity_id: str
    :type entity_id: str

    """
    return web.Response(status=200)


async def model_list_entity_suggestions(request: web.Request, app_id, version_id, entity_id, take=None) -> web.Response:
    """model_list_entity_suggestions

    Get suggested example utterances that would improve the accuracy of the entity model in a version of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param entity_id: The target entity extractor model to enhance.
    :type entity_id: str
    :type entity_id: str
    :param take: The number of entries to return. Maximum page size is 500. Default is 100.
    :type take: int

    """
    return web.Response(status=200)


async def model_list_hierarchical_entities(request: web.Request, app_id, version_id, skip=None, take=None) -> web.Response:
    """model_list_hierarchical_entities

    Gets information about all the hierarchical entity models in a version of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param skip: The number of entries to skip. Default value is 0.
    :type skip: int
    :param take: The number of entries to return. Maximum page size is 500. Default is 100.
    :type take: int

    """
    return web.Response(status=200)


async def model_list_hierarchical_entity_roles(request: web.Request, app_id, version_id, h_entity_id) -> web.Response:
    """Get all roles for a hierarchical entity in a version of the application

    

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param h_entity_id: The hierarchical entity extractor ID.
    :type h_entity_id: str
    :type h_entity_id: str

    """
    return web.Response(status=200)


async def model_list_intent_suggestions(request: web.Request, app_id, version_id, intent_id, take=None) -> web.Response:
    """model_list_intent_suggestions

    Suggests example utterances that would improve the accuracy of the intent model in a version of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param intent_id: The intent classifier ID.
    :type intent_id: str
    :type intent_id: str
    :param take: The number of entries to return. Maximum page size is 500. Default is 100.
    :type take: int

    """
    return web.Response(status=200)


async def model_list_intents(request: web.Request, app_id, version_id, skip=None, take=None) -> web.Response:
    """model_list_intents

    Gets information about the intent models in a version of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param skip: The number of entries to skip. Default value is 0.
    :type skip: int
    :param take: The number of entries to return. Maximum page size is 500. Default is 100.
    :type take: int

    """
    return web.Response(status=200)


async def model_list_models(request: web.Request, app_id, version_id, skip=None, take=None) -> web.Response:
    """model_list_models

    Gets information about all the intent and entity models in a version of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param skip: The number of entries to skip. Default value is 0.
    :type skip: int
    :param take: The number of entries to return. Maximum page size is 500. Default is 100.
    :type take: int

    """
    return web.Response(status=200)


async def model_list_pattern_any_entity_infos(request: web.Request, app_id, version_id, skip=None, take=None) -> web.Response:
    """Get information about the Pattern.Any entity models in a version of the application.

    

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param skip: The number of entries to skip. Default value is 0.
    :type skip: int
    :param take: The number of entries to return. Maximum page size is 500. Default is 100.
    :type take: int

    """
    return web.Response(status=200)


async def model_list_pattern_any_entity_roles(request: web.Request, app_id, version_id, entity_id) -> web.Response:
    """Get all roles for a Pattern.any entity in a version of the application

    

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param entity_id: entity Id
    :type entity_id: str
    :type entity_id: str

    """
    return web.Response(status=200)


async def model_list_prebuilt_entities(request: web.Request, app_id, version_id) -> web.Response:
    """model_list_prebuilt_entities

    Gets all the available prebuilt entities in a version of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str

    """
    return web.Response(status=200)


async def model_list_prebuilt_entity_roles(request: web.Request, app_id, version_id, entity_id) -> web.Response:
    """Get a prebuilt entity&#39;s roles in a version of the application.

    

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param entity_id: entity Id
    :type entity_id: str
    :type entity_id: str

    """
    return web.Response(status=200)


async def model_list_prebuilts(request: web.Request, app_id, version_id, skip=None, take=None) -> web.Response:
    """model_list_prebuilts

    Gets information about all the prebuilt entities in a version of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param skip: The number of entries to skip. Default value is 0.
    :type skip: int
    :param take: The number of entries to return. Maximum page size is 500. Default is 100.
    :type take: int

    """
    return web.Response(status=200)


async def model_list_regex_entity_infos(request: web.Request, app_id, version_id, skip=None, take=None) -> web.Response:
    """Gets information about the regular expression entity models in a version of the application.

    

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param skip: The number of entries to skip. Default value is 0.
    :type skip: int
    :param take: The number of entries to return. Maximum page size is 500. Default is 100.
    :type take: int

    """
    return web.Response(status=200)


async def model_list_regex_entity_roles(request: web.Request, app_id, version_id, entity_id) -> web.Response:
    """Get all roles for a regular expression entity in a version of the application.

    

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param entity_id: entity Id
    :type entity_id: str
    :type entity_id: str

    """
    return web.Response(status=200)


async def model_patch_closed_list(request: web.Request, app_id, version_id, cl_entity_id, closed_list_model_patch_object) -> web.Response:
    """model_patch_closed_list

    Adds a batch of sublists to an existing list entity in a version of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param cl_entity_id: The list entity model ID.
    :type cl_entity_id: str
    :type cl_entity_id: str
    :param closed_list_model_patch_object: A words list batch.
    :type closed_list_model_patch_object: dict | bytes

    """
    closed_list_model_patch_object = ClosedListModelPatchObject.from_dict(closed_list_model_patch_object)
    return web.Response(status=200)


async def model_replace_entity_features(request: web.Request, app_id, version_id, entity_id, feature_relations_update_object) -> web.Response:
    """model_replace_entity_features

    Updates the information of the features used by the entity in a version of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param entity_id: The entity extractor ID.
    :type entity_id: str
    :type entity_id: str
    :param feature_relations_update_object: A list of feature information objects containing the new feature relations.
    :type feature_relations_update_object: list | bytes

    """
    feature_relations_update_object = [ModelFeatureInformation.from_dict(d) for d in feature_relations_update_object]
    return web.Response(status=200)


async def model_replace_intent_features(request: web.Request, app_id, version_id, intent_id, feature_relations_update_object) -> web.Response:
    """model_replace_intent_features

    Updates the information of the features used by the intent in a version of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param intent_id: The intent classifier ID.
    :type intent_id: str
    :type intent_id: str
    :param feature_relations_update_object: A list of feature information objects containing the new feature relations.
    :type feature_relations_update_object: list | bytes

    """
    feature_relations_update_object = [ModelFeatureInformation.from_dict(d) for d in feature_relations_update_object]
    return web.Response(status=200)


async def model_update_closed_list(request: web.Request, app_id, version_id, cl_entity_id, closed_list_model_update_object) -> web.Response:
    """model_update_closed_list

    Updates the list entity in a version of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param cl_entity_id: The list model ID.
    :type cl_entity_id: str
    :type cl_entity_id: str
    :param closed_list_model_update_object: The new list entity name and words list.
    :type closed_list_model_update_object: dict | bytes

    """
    closed_list_model_update_object = ClosedListModelUpdateObject.from_dict(closed_list_model_update_object)
    return web.Response(status=200)


async def model_update_closed_list_entity_role(request: web.Request, app_id, version_id, entity_id, role_id, entity_role_update_object) -> web.Response:
    """Update a role for a given list entity in a version of the application.

    

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param entity_id: The entity ID.
    :type entity_id: str
    :type entity_id: str
    :param role_id: The entity role ID.
    :type role_id: str
    :type role_id: str
    :param entity_role_update_object: The new entity role.
    :type entity_role_update_object: dict | bytes

    """
    entity_role_update_object = EntityRoleUpdateObject.from_dict(entity_role_update_object)
    return web.Response(status=200)


async def model_update_composite_entity(request: web.Request, app_id, version_id, c_entity_id, composite_model_update_object) -> web.Response:
    """model_update_composite_entity

    Updates a composite entity in a version of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param c_entity_id: The composite entity extractor ID.
    :type c_entity_id: str
    :type c_entity_id: str
    :param composite_model_update_object: A model object containing the new entity extractor name and children.
    :type composite_model_update_object: dict | bytes

    """
    composite_model_update_object = CompositeEntityModel.from_dict(composite_model_update_object)
    return web.Response(status=200)


async def model_update_composite_entity_role(request: web.Request, app_id, version_id, c_entity_id, role_id, entity_role_update_object) -> web.Response:
    """Update a role for a given composite entity in a version of the application

    

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param c_entity_id: The composite entity extractor ID.
    :type c_entity_id: str
    :type c_entity_id: str
    :param role_id: The entity role ID.
    :type role_id: str
    :type role_id: str
    :param entity_role_update_object: The new entity role.
    :type entity_role_update_object: dict | bytes

    """
    entity_role_update_object = EntityRoleUpdateObject.from_dict(entity_role_update_object)
    return web.Response(status=200)


async def model_update_custom_prebuilt_entity_role(request: web.Request, app_id, version_id, entity_id, role_id, entity_role_update_object) -> web.Response:
    """Update a role for a given prebuilt entity in a version of the application.

    

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param entity_id: The entity ID.
    :type entity_id: str
    :type entity_id: str
    :param role_id: The entity role ID.
    :type role_id: str
    :type role_id: str
    :param entity_role_update_object: The new entity role.
    :type entity_role_update_object: dict | bytes

    """
    entity_role_update_object = EntityRoleUpdateObject.from_dict(entity_role_update_object)
    return web.Response(status=200)


async def model_update_entity_child(request: web.Request, app_id, version_id, entity_id, entity_model_update_object) -> web.Response:
    """model_update_entity_child

    Updates the name of an entity extractor or the name and instanceOf model of a child entity extractor.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param entity_id: The entity extractor or the child entity extractor ID.
    :type entity_id: str
    :type entity_id: str
    :param entity_model_update_object: A model object containing the name new entity extractor or the name and instance of model of a child entity extractor 
    :type entity_model_update_object: dict | bytes

    """
    entity_model_update_object = EntityModelUpdateObject.from_dict(entity_model_update_object)
    return web.Response(status=200)


async def model_update_entity_role(request: web.Request, app_id, version_id, entity_id, role_id, entity_role_update_object) -> web.Response:
    """Update a role for a given entity in a version of the application.

    

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param entity_id: The entity ID.
    :type entity_id: str
    :type entity_id: str
    :param role_id: The entity role ID.
    :type role_id: str
    :type role_id: str
    :param entity_role_update_object: The new entity role.
    :type entity_role_update_object: dict | bytes

    """
    entity_role_update_object = EntityRoleUpdateObject.from_dict(entity_role_update_object)
    return web.Response(status=200)


async def model_update_explicit_list_item(request: web.Request, app_id, version_id, entity_id, item_id, item) -> web.Response:
    """Updates an explicit (exception) list item for a Pattern.Any entity in a version of the application.

    

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param entity_id: The Pattern.Any entity extractor ID.
    :type entity_id: str
    :type entity_id: str
    :param item_id: The explicit list item ID.
    :type item_id: int
    :param item: The new explicit list item.
    :type item: dict | bytes

    """
    item = ExplicitListItemUpdateObject.from_dict(item)
    return web.Response(status=200)


async def model_update_hierarchical_entity(request: web.Request, app_id, version_id, h_entity_id, model_update_object) -> web.Response:
    """model_update_hierarchical_entity

    Updates the name of a hierarchical entity model in a version of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param h_entity_id: The hierarchical entity extractor ID.
    :type h_entity_id: str
    :type h_entity_id: str
    :param model_update_object: Model containing names of the hierarchical entity.
    :type model_update_object: dict | bytes

    """
    model_update_object = ModelUpdateObject.from_dict(model_update_object)
    return web.Response(status=200)


async def model_update_hierarchical_entity_child(request: web.Request, app_id, version_id, h_entity_id, h_child_id, hierarchical_child_model_update_object) -> web.Response:
    """model_update_hierarchical_entity_child

    Renames a single child in an existing hierarchical entity model in a version of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param h_entity_id: The hierarchical entity extractor ID.
    :type h_entity_id: str
    :type h_entity_id: str
    :param h_child_id: The hierarchical entity extractor child ID.
    :type h_child_id: str
    :type h_child_id: str
    :param hierarchical_child_model_update_object: Model object containing new name of the hierarchical entity child.
    :type hierarchical_child_model_update_object: dict | bytes

    """
    hierarchical_child_model_update_object = ModelAddCompositeEntityChildRequest.from_dict(hierarchical_child_model_update_object)
    return web.Response(status=200)


async def model_update_hierarchical_entity_role(request: web.Request, app_id, version_id, h_entity_id, role_id, entity_role_update_object) -> web.Response:
    """Update a role for a given hierarchical entity in a version of the application.

    

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param h_entity_id: The hierarchical entity extractor ID.
    :type h_entity_id: str
    :type h_entity_id: str
    :param role_id: The entity role ID.
    :type role_id: str
    :type role_id: str
    :param entity_role_update_object: The new entity role.
    :type entity_role_update_object: dict | bytes

    """
    entity_role_update_object = EntityRoleUpdateObject.from_dict(entity_role_update_object)
    return web.Response(status=200)


async def model_update_intent(request: web.Request, app_id, version_id, intent_id, model_update_object) -> web.Response:
    """model_update_intent

    Updates the name of an intent in a version of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param intent_id: The intent classifier ID.
    :type intent_id: str
    :type intent_id: str
    :param model_update_object: A model object containing the new intent name.
    :type model_update_object: dict | bytes

    """
    model_update_object = ModelUpdateObject.from_dict(model_update_object)
    return web.Response(status=200)


async def model_update_pattern_any_entity_model(request: web.Request, app_id, version_id, entity_id, pattern_any_update_object) -> web.Response:
    """Updates the name and explicit (exception) list of a Pattern.Any entity model in a version of the application.

    

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param entity_id: The Pattern.Any entity extractor ID.
    :type entity_id: str
    :type entity_id: str
    :param pattern_any_update_object: An object containing the explicit list of the Pattern.Any entity.
    :type pattern_any_update_object: dict | bytes

    """
    pattern_any_update_object = PatternAnyModelUpdateObject.from_dict(pattern_any_update_object)
    return web.Response(status=200)


async def model_update_pattern_any_entity_role(request: web.Request, app_id, version_id, entity_id, role_id, entity_role_update_object) -> web.Response:
    """Update a role for a given Pattern.any entity in a version of the application.

    

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param entity_id: The entity ID.
    :type entity_id: str
    :type entity_id: str
    :param role_id: The entity role ID.
    :type role_id: str
    :type role_id: str
    :param entity_role_update_object: The new entity role.
    :type entity_role_update_object: dict | bytes

    """
    entity_role_update_object = EntityRoleUpdateObject.from_dict(entity_role_update_object)
    return web.Response(status=200)


async def model_update_prebuilt_entity_role(request: web.Request, app_id, version_id, entity_id, role_id, entity_role_update_object) -> web.Response:
    """Update a role for a given prebuilt entity in a version of the application

    

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param entity_id: The entity ID.
    :type entity_id: str
    :type entity_id: str
    :param role_id: The entity role ID.
    :type role_id: str
    :type role_id: str
    :param entity_role_update_object: The new entity role.
    :type entity_role_update_object: dict | bytes

    """
    entity_role_update_object = EntityRoleUpdateObject.from_dict(entity_role_update_object)
    return web.Response(status=200)


async def model_update_regex_entity_model(request: web.Request, app_id, version_id, regex_entity_id, regex_entity_update_object) -> web.Response:
    """Updates the regular expression entity in a version of the application.

    

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param regex_entity_id: The regular expression entity extractor ID.
    :type regex_entity_id: str
    :type regex_entity_id: str
    :param regex_entity_update_object: An object containing the new entity name and regex pattern.
    :type regex_entity_update_object: dict | bytes

    """
    regex_entity_update_object = RegexModelUpdateObject.from_dict(regex_entity_update_object)
    return web.Response(status=200)


async def model_update_regex_entity_role(request: web.Request, app_id, version_id, entity_id, role_id, entity_role_update_object) -> web.Response:
    """Update a role for a given regular expression entity in a version of the application

    

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param entity_id: The entity ID.
    :type entity_id: str
    :type entity_id: str
    :param role_id: The entity role ID.
    :type role_id: str
    :type role_id: str
    :param entity_role_update_object: The new entity role.
    :type entity_role_update_object: dict | bytes

    """
    entity_role_update_object = EntityRoleUpdateObject.from_dict(entity_role_update_object)
    return web.Response(status=200)


async def model_update_sub_list(request: web.Request, app_id, version_id, cl_entity_id, sub_list_id, word_list_base_update_object) -> web.Response:
    """model_update_sub_list

    Updates one of the list entity&#39;s sublists in a version of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param cl_entity_id: The list entity extractor ID.
    :type cl_entity_id: str
    :type cl_entity_id: str
    :param sub_list_id: The sublist ID.
    :type sub_list_id: int
    :param word_list_base_update_object: A sublist update object containing the new canonical form and the list of words.
    :type word_list_base_update_object: dict | bytes

    """
    word_list_base_update_object = WordListBaseUpdateObject.from_dict(word_list_base_update_object)
    return web.Response(status=200)


async def pattern_add_pattern(request: web.Request, app_id, version_id, pattern) -> web.Response:
    """Adds a pattern to a version of the application.

    

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param pattern: The input pattern.
    :type pattern: dict | bytes

    """
    pattern = PatternRuleCreateObject.from_dict(pattern)
    return web.Response(status=200)


async def pattern_batch_add_patterns(request: web.Request, app_id, version_id, patterns) -> web.Response:
    """Adds a batch of patterns in a version of the application.

    

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param patterns: A JSON array containing patterns.
    :type patterns: list | bytes

    """
    patterns = [PatternRuleCreateObject.from_dict(d) for d in patterns]
    return web.Response(status=200)


async def pattern_delete_pattern(request: web.Request, app_id, version_id, pattern_id) -> web.Response:
    """Deletes the pattern with the specified ID from a version of the application..

    

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param pattern_id: The pattern ID.
    :type pattern_id: str
    :type pattern_id: str

    """
    return web.Response(status=200)


async def pattern_delete_patterns(request: web.Request, app_id, version_id, pattern_ids) -> web.Response:
    """Deletes a list of patterns in a version of the application.

    

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param pattern_ids: The patterns IDs.
    :type pattern_ids: List[str]

    """
    return web.Response(status=200)


async def pattern_list_intent_patterns(request: web.Request, app_id, version_id, intent_id, skip=None, take=None) -> web.Response:
    """Returns patterns for the specific intent in a version of the application.

    

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param intent_id: The intent classifier ID.
    :type intent_id: str
    :type intent_id: str
    :param skip: The number of entries to skip. Default value is 0.
    :type skip: int
    :param take: The number of entries to return. Maximum page size is 500. Default is 100.
    :type take: int

    """
    return web.Response(status=200)


async def pattern_list_patterns(request: web.Request, app_id, version_id, skip=None, take=None) -> web.Response:
    """Gets patterns in a version of the application.

    

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param skip: The number of entries to skip. Default value is 0.
    :type skip: int
    :param take: The number of entries to return. Maximum page size is 500. Default is 100.
    :type take: int

    """
    return web.Response(status=200)


async def pattern_update_pattern(request: web.Request, app_id, version_id, pattern_id, pattern) -> web.Response:
    """Updates a pattern in a version of the application.

    

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param pattern_id: The pattern ID.
    :type pattern_id: str
    :type pattern_id: str
    :param pattern: An object representing a pattern.
    :type pattern: dict | bytes

    """
    pattern = PatternRuleUpdateObject.from_dict(pattern)
    return web.Response(status=200)


async def pattern_update_patterns(request: web.Request, app_id, version_id, patterns) -> web.Response:
    """Updates patterns in a version of the application.

    

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param patterns: An array represents the patterns.
    :type patterns: list | bytes

    """
    patterns = [PatternRuleUpdateObject.from_dict(d) for d in patterns]
    return web.Response(status=200)


async def permissions_add(request: web.Request, app_id, user_to_add) -> web.Response:
    """permissions_add

    Adds a user to the allowed list of users to access this LUIS application. Users are added using their email address.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param user_to_add: A model containing the user&#39;s email address.
    :type user_to_add: dict | bytes

    """
    user_to_add = UserCollaborator.from_dict(user_to_add)
    return web.Response(status=200)


async def permissions_delete(request: web.Request, app_id, user_to_delete) -> web.Response:
    """permissions_delete

    Removes a user from the allowed list of users to access this LUIS application. Users are removed using their email address.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param user_to_delete: A model containing the user&#39;s email address.
    :type user_to_delete: dict | bytes

    """
    user_to_delete = UserCollaborator.from_dict(user_to_delete)
    return web.Response(status=200)


async def permissions_list(request: web.Request, app_id) -> web.Response:
    """permissions_list

    Gets the list of user emails that have permissions to access your application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str

    """
    return web.Response(status=200)


async def permissions_update(request: web.Request, app_id, collaborators) -> web.Response:
    """permissions_update

    Replaces the current user access list with the new list sent in the body. If an empty list is sent, all access to other users will be removed.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param collaborators: A model containing a list of user email addresses.
    :type collaborators: dict | bytes

    """
    collaborators = CollaboratorsArray.from_dict(collaborators)
    return web.Response(status=200)


async def settings_list(request: web.Request, app_id, version_id) -> web.Response:
    """settings_list

    Gets the settings in a version of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str

    """
    return web.Response(status=200)


async def settings_update(request: web.Request, app_id, version_id, list_of_app_version_setting_object) -> web.Response:
    """settings_update

    Updates the settings in a version of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param list_of_app_version_setting_object: A list of the updated application version settings.
    :type list_of_app_version_setting_object: list | bytes

    """
    list_of_app_version_setting_object = [AppVersionSettingObject.from_dict(d) for d in list_of_app_version_setting_object]
    return web.Response(status=200)


async def train_get_status(request: web.Request, app_id, version_id) -> web.Response:
    """train_get_status

    Gets the training status of all models (intents and entities) for the specified LUIS app. You must call the train API to train the LUIS app before you call this API to get training status. \&quot;appID\&quot; specifies the LUIS app ID. \&quot;versionId\&quot; specifies the version number of the LUIS app. For example, \&quot;0.1\&quot;.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str

    """
    return web.Response(status=200)


async def train_train_version(request: web.Request, app_id, version_id) -> web.Response:
    """train_train_version

    Sends a training request for a version of a specified LUIS app. This POST request initiates a request asynchronously. To determine whether the training request is successful, submit a GET request to get training status. Note: The application version is not fully trained unless all the models (intents and entities) are trained successfully or are up to date. To verify training success, get the training status at least once after training is complete.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str

    """
    return web.Response(status=200)


async def versions_clone(request: web.Request, app_id, version_id, version_clone_object) -> web.Response:
    """versions_clone

    Creates a new version from the selected version.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param version_clone_object: A model containing the new version ID.
    :type version_clone_object: dict | bytes

    """
    version_clone_object = TaskUpdateObject.from_dict(version_clone_object)
    return web.Response(status=200)


async def versions_delete(request: web.Request, app_id, version_id) -> web.Response:
    """versions_delete

    Deletes an application version.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str

    """
    return web.Response(status=200)


async def versions_delete_unlabelled_utterance(request: web.Request, app_id, version_id, utterance) -> web.Response:
    """versions_delete_unlabelled_utterance

    Deleted an unlabelled utterance in a version of the application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param utterance: The utterance text to delete.
    :type utterance: str

    """
    return web.Response(status=200)


async def versions_export(request: web.Request, app_id, version_id) -> web.Response:
    """versions_export

    Exports a LUIS application to JSON format.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str

    """
    return web.Response(status=200)


async def versions_get(request: web.Request, app_id, version_id) -> web.Response:
    """versions_get

    Gets the version information such as date created, last modified date, endpoint URL, count of intents and entities, training and publishing status.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str

    """
    return web.Response(status=200)


async def versions_import(request: web.Request, app_id, luis_app, version_id=None) -> web.Response:
    """versions_import

    Imports a new version into a LUIS application.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param luis_app: A LUIS application structure.
    :type luis_app: dict | bytes
    :param version_id: The new versionId to import. If not specified, the versionId will be read from the imported object.
    :type version_id: str

    """
    luis_app = LuisApp.from_dict(luis_app)
    return web.Response(status=200)


async def versions_list(request: web.Request, app_id, skip=None, take=None) -> web.Response:
    """versions_list

    Gets a list of versions for this application ID.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param skip: The number of entries to skip. Default value is 0.
    :type skip: int
    :param take: The number of entries to return. Maximum page size is 500. Default is 100.
    :type take: int

    """
    return web.Response(status=200)


async def versions_update(request: web.Request, app_id, version_id, version_update_object) -> web.Response:
    """versions_update

    Updates the name or description of the application version.

    :param app_id: The application ID.
    :type app_id: str
    :type app_id: str
    :param version_id: The version ID.
    :type version_id: str
    :param version_update_object: A model containing Name and Description of the application.
    :type version_update_object: dict | bytes

    """
    version_update_object = TaskUpdateObject.from_dict(version_update_object)
    return web.Response(status=200)
