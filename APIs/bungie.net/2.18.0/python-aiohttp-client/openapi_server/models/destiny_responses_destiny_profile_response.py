# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.destiny_base_item_component_set_ofuint32 import DestinyBaseItemComponentSetOfuint32
from openapi_server.models.destiny_item_component_set_ofint64 import DestinyItemComponentSetOfint64
from openapi_server.models.dictionary_component_response_ofint64_and_destiny_character_activities_component import DictionaryComponentResponseOfint64AndDestinyCharacterActivitiesComponent
from openapi_server.models.dictionary_component_response_ofint64_and_destiny_character_component import DictionaryComponentResponseOfint64AndDestinyCharacterComponent
from openapi_server.models.dictionary_component_response_ofint64_and_destiny_character_progression_component import DictionaryComponentResponseOfint64AndDestinyCharacterProgressionComponent
from openapi_server.models.dictionary_component_response_ofint64_and_destiny_character_records_component import DictionaryComponentResponseOfint64AndDestinyCharacterRecordsComponent
from openapi_server.models.dictionary_component_response_ofint64_and_destiny_character_render_component import DictionaryComponentResponseOfint64AndDestinyCharacterRenderComponent
from openapi_server.models.dictionary_component_response_ofint64_and_destiny_collectibles_component import DictionaryComponentResponseOfint64AndDestinyCollectiblesComponent
from openapi_server.models.dictionary_component_response_ofint64_and_destiny_craftables_component import DictionaryComponentResponseOfint64AndDestinyCraftablesComponent
from openapi_server.models.dictionary_component_response_ofint64_and_destiny_currencies_component import DictionaryComponentResponseOfint64AndDestinyCurrenciesComponent
from openapi_server.models.dictionary_component_response_ofint64_and_destiny_inventory_component import DictionaryComponentResponseOfint64AndDestinyInventoryComponent
from openapi_server.models.dictionary_component_response_ofint64_and_destiny_kiosks_component import DictionaryComponentResponseOfint64AndDestinyKiosksComponent
from openapi_server.models.dictionary_component_response_ofint64_and_destiny_loadouts_component import DictionaryComponentResponseOfint64AndDestinyLoadoutsComponent
from openapi_server.models.dictionary_component_response_ofint64_and_destiny_plug_sets_component import DictionaryComponentResponseOfint64AndDestinyPlugSetsComponent
from openapi_server.models.dictionary_component_response_ofint64_and_destiny_presentation_nodes_component import DictionaryComponentResponseOfint64AndDestinyPresentationNodesComponent
from openapi_server.models.dictionary_component_response_ofint64_and_destiny_string_variables_component import DictionaryComponentResponseOfint64AndDestinyStringVariablesComponent
from openapi_server.models.single_component_response_of_destiny_inventory_component import SingleComponentResponseOfDestinyInventoryComponent
from openapi_server.models.single_component_response_of_destiny_kiosks_component import SingleComponentResponseOfDestinyKiosksComponent
from openapi_server.models.single_component_response_of_destiny_metrics_component import SingleComponentResponseOfDestinyMetricsComponent
from openapi_server.models.single_component_response_of_destiny_platform_silver_component import SingleComponentResponseOfDestinyPlatformSilverComponent
from openapi_server.models.single_component_response_of_destiny_plug_sets_component import SingleComponentResponseOfDestinyPlugSetsComponent
from openapi_server.models.single_component_response_of_destiny_presentation_nodes_component import SingleComponentResponseOfDestinyPresentationNodesComponent
from openapi_server.models.single_component_response_of_destiny_profile_collectibles_component import SingleComponentResponseOfDestinyProfileCollectiblesComponent
from openapi_server.models.single_component_response_of_destiny_profile_component import SingleComponentResponseOfDestinyProfileComponent
from openapi_server.models.single_component_response_of_destiny_profile_progression_component import SingleComponentResponseOfDestinyProfileProgressionComponent
from openapi_server.models.single_component_response_of_destiny_profile_records_component import SingleComponentResponseOfDestinyProfileRecordsComponent
from openapi_server.models.single_component_response_of_destiny_profile_transitory_component import SingleComponentResponseOfDestinyProfileTransitoryComponent
from openapi_server.models.single_component_response_of_destiny_social_commendations_component import SingleComponentResponseOfDestinySocialCommendationsComponent
from openapi_server.models.single_component_response_of_destiny_string_variables_component import SingleComponentResponseOfDestinyStringVariablesComponent
from openapi_server.models.single_component_response_of_destiny_vendor_receipts_component import SingleComponentResponseOfDestinyVendorReceiptsComponent
from openapi_server import util


class DestinyResponsesDestinyProfileResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, character_activities: DictionaryComponentResponseOfint64AndDestinyCharacterActivitiesComponent=None, character_collectibles: DictionaryComponentResponseOfint64AndDestinyCollectiblesComponent=None, character_craftables: DictionaryComponentResponseOfint64AndDestinyCraftablesComponent=None, character_currency_lookups: DictionaryComponentResponseOfint64AndDestinyCurrenciesComponent=None, character_equipment: DictionaryComponentResponseOfint64AndDestinyInventoryComponent=None, character_inventories: DictionaryComponentResponseOfint64AndDestinyInventoryComponent=None, character_kiosks: DictionaryComponentResponseOfint64AndDestinyKiosksComponent=None, character_loadouts: DictionaryComponentResponseOfint64AndDestinyLoadoutsComponent=None, character_plug_sets: DictionaryComponentResponseOfint64AndDestinyPlugSetsComponent=None, character_presentation_nodes: DictionaryComponentResponseOfint64AndDestinyPresentationNodesComponent=None, character_progressions: DictionaryComponentResponseOfint64AndDestinyCharacterProgressionComponent=None, character_records: DictionaryComponentResponseOfint64AndDestinyCharacterRecordsComponent=None, character_render_data: DictionaryComponentResponseOfint64AndDestinyCharacterRenderComponent=None, character_string_variables: DictionaryComponentResponseOfint64AndDestinyStringVariablesComponent=None, character_uninstanced_item_components: Dict[str, DestinyBaseItemComponentSetOfuint32]=None, characters: DictionaryComponentResponseOfint64AndDestinyCharacterComponent=None, item_components: DestinyItemComponentSetOfint64=None, metrics: SingleComponentResponseOfDestinyMetricsComponent=None, platform_silver: SingleComponentResponseOfDestinyPlatformSilverComponent=None, profile: SingleComponentResponseOfDestinyProfileComponent=None, profile_collectibles: SingleComponentResponseOfDestinyProfileCollectiblesComponent=None, profile_commendations: SingleComponentResponseOfDestinySocialCommendationsComponent=None, profile_currencies: SingleComponentResponseOfDestinyInventoryComponent=None, profile_inventory: SingleComponentResponseOfDestinyInventoryComponent=None, profile_kiosks: SingleComponentResponseOfDestinyKiosksComponent=None, profile_plug_sets: SingleComponentResponseOfDestinyPlugSetsComponent=None, profile_presentation_nodes: SingleComponentResponseOfDestinyPresentationNodesComponent=None, profile_progression: SingleComponentResponseOfDestinyProfileProgressionComponent=None, profile_records: SingleComponentResponseOfDestinyProfileRecordsComponent=None, profile_string_variables: SingleComponentResponseOfDestinyStringVariablesComponent=None, profile_transitory_data: SingleComponentResponseOfDestinyProfileTransitoryComponent=None, response_minted_timestamp: datetime=None, secondary_components_minted_timestamp: datetime=None, vendor_receipts: SingleComponentResponseOfDestinyVendorReceiptsComponent=None):
        """DestinyResponsesDestinyProfileResponse - a model defined in OpenAPI

        :param character_activities: The character_activities of this DestinyResponsesDestinyProfileResponse.
        :param character_collectibles: The character_collectibles of this DestinyResponsesDestinyProfileResponse.
        :param character_craftables: The character_craftables of this DestinyResponsesDestinyProfileResponse.
        :param character_currency_lookups: The character_currency_lookups of this DestinyResponsesDestinyProfileResponse.
        :param character_equipment: The character_equipment of this DestinyResponsesDestinyProfileResponse.
        :param character_inventories: The character_inventories of this DestinyResponsesDestinyProfileResponse.
        :param character_kiosks: The character_kiosks of this DestinyResponsesDestinyProfileResponse.
        :param character_loadouts: The character_loadouts of this DestinyResponsesDestinyProfileResponse.
        :param character_plug_sets: The character_plug_sets of this DestinyResponsesDestinyProfileResponse.
        :param character_presentation_nodes: The character_presentation_nodes of this DestinyResponsesDestinyProfileResponse.
        :param character_progressions: The character_progressions of this DestinyResponsesDestinyProfileResponse.
        :param character_records: The character_records of this DestinyResponsesDestinyProfileResponse.
        :param character_render_data: The character_render_data of this DestinyResponsesDestinyProfileResponse.
        :param character_string_variables: The character_string_variables of this DestinyResponsesDestinyProfileResponse.
        :param character_uninstanced_item_components: The character_uninstanced_item_components of this DestinyResponsesDestinyProfileResponse.
        :param characters: The characters of this DestinyResponsesDestinyProfileResponse.
        :param item_components: The item_components of this DestinyResponsesDestinyProfileResponse.
        :param metrics: The metrics of this DestinyResponsesDestinyProfileResponse.
        :param platform_silver: The platform_silver of this DestinyResponsesDestinyProfileResponse.
        :param profile: The profile of this DestinyResponsesDestinyProfileResponse.
        :param profile_collectibles: The profile_collectibles of this DestinyResponsesDestinyProfileResponse.
        :param profile_commendations: The profile_commendations of this DestinyResponsesDestinyProfileResponse.
        :param profile_currencies: The profile_currencies of this DestinyResponsesDestinyProfileResponse.
        :param profile_inventory: The profile_inventory of this DestinyResponsesDestinyProfileResponse.
        :param profile_kiosks: The profile_kiosks of this DestinyResponsesDestinyProfileResponse.
        :param profile_plug_sets: The profile_plug_sets of this DestinyResponsesDestinyProfileResponse.
        :param profile_presentation_nodes: The profile_presentation_nodes of this DestinyResponsesDestinyProfileResponse.
        :param profile_progression: The profile_progression of this DestinyResponsesDestinyProfileResponse.
        :param profile_records: The profile_records of this DestinyResponsesDestinyProfileResponse.
        :param profile_string_variables: The profile_string_variables of this DestinyResponsesDestinyProfileResponse.
        :param profile_transitory_data: The profile_transitory_data of this DestinyResponsesDestinyProfileResponse.
        :param response_minted_timestamp: The response_minted_timestamp of this DestinyResponsesDestinyProfileResponse.
        :param secondary_components_minted_timestamp: The secondary_components_minted_timestamp of this DestinyResponsesDestinyProfileResponse.
        :param vendor_receipts: The vendor_receipts of this DestinyResponsesDestinyProfileResponse.
        """
        self.openapi_types = {
            'character_activities': DictionaryComponentResponseOfint64AndDestinyCharacterActivitiesComponent,
            'character_collectibles': DictionaryComponentResponseOfint64AndDestinyCollectiblesComponent,
            'character_craftables': DictionaryComponentResponseOfint64AndDestinyCraftablesComponent,
            'character_currency_lookups': DictionaryComponentResponseOfint64AndDestinyCurrenciesComponent,
            'character_equipment': DictionaryComponentResponseOfint64AndDestinyInventoryComponent,
            'character_inventories': DictionaryComponentResponseOfint64AndDestinyInventoryComponent,
            'character_kiosks': DictionaryComponentResponseOfint64AndDestinyKiosksComponent,
            'character_loadouts': DictionaryComponentResponseOfint64AndDestinyLoadoutsComponent,
            'character_plug_sets': DictionaryComponentResponseOfint64AndDestinyPlugSetsComponent,
            'character_presentation_nodes': DictionaryComponentResponseOfint64AndDestinyPresentationNodesComponent,
            'character_progressions': DictionaryComponentResponseOfint64AndDestinyCharacterProgressionComponent,
            'character_records': DictionaryComponentResponseOfint64AndDestinyCharacterRecordsComponent,
            'character_render_data': DictionaryComponentResponseOfint64AndDestinyCharacterRenderComponent,
            'character_string_variables': DictionaryComponentResponseOfint64AndDestinyStringVariablesComponent,
            'character_uninstanced_item_components': Dict[str, DestinyBaseItemComponentSetOfuint32],
            'characters': DictionaryComponentResponseOfint64AndDestinyCharacterComponent,
            'item_components': DestinyItemComponentSetOfint64,
            'metrics': SingleComponentResponseOfDestinyMetricsComponent,
            'platform_silver': SingleComponentResponseOfDestinyPlatformSilverComponent,
            'profile': SingleComponentResponseOfDestinyProfileComponent,
            'profile_collectibles': SingleComponentResponseOfDestinyProfileCollectiblesComponent,
            'profile_commendations': SingleComponentResponseOfDestinySocialCommendationsComponent,
            'profile_currencies': SingleComponentResponseOfDestinyInventoryComponent,
            'profile_inventory': SingleComponentResponseOfDestinyInventoryComponent,
            'profile_kiosks': SingleComponentResponseOfDestinyKiosksComponent,
            'profile_plug_sets': SingleComponentResponseOfDestinyPlugSetsComponent,
            'profile_presentation_nodes': SingleComponentResponseOfDestinyPresentationNodesComponent,
            'profile_progression': SingleComponentResponseOfDestinyProfileProgressionComponent,
            'profile_records': SingleComponentResponseOfDestinyProfileRecordsComponent,
            'profile_string_variables': SingleComponentResponseOfDestinyStringVariablesComponent,
            'profile_transitory_data': SingleComponentResponseOfDestinyProfileTransitoryComponent,
            'response_minted_timestamp': datetime,
            'secondary_components_minted_timestamp': datetime,
            'vendor_receipts': SingleComponentResponseOfDestinyVendorReceiptsComponent
        }

        self.attribute_map = {
            'character_activities': 'characterActivities',
            'character_collectibles': 'characterCollectibles',
            'character_craftables': 'characterCraftables',
            'character_currency_lookups': 'characterCurrencyLookups',
            'character_equipment': 'characterEquipment',
            'character_inventories': 'characterInventories',
            'character_kiosks': 'characterKiosks',
            'character_loadouts': 'characterLoadouts',
            'character_plug_sets': 'characterPlugSets',
            'character_presentation_nodes': 'characterPresentationNodes',
            'character_progressions': 'characterProgressions',
            'character_records': 'characterRecords',
            'character_render_data': 'characterRenderData',
            'character_string_variables': 'characterStringVariables',
            'character_uninstanced_item_components': 'characterUninstancedItemComponents',
            'characters': 'characters',
            'item_components': 'itemComponents',
            'metrics': 'metrics',
            'platform_silver': 'platformSilver',
            'profile': 'profile',
            'profile_collectibles': 'profileCollectibles',
            'profile_commendations': 'profileCommendations',
            'profile_currencies': 'profileCurrencies',
            'profile_inventory': 'profileInventory',
            'profile_kiosks': 'profileKiosks',
            'profile_plug_sets': 'profilePlugSets',
            'profile_presentation_nodes': 'profilePresentationNodes',
            'profile_progression': 'profileProgression',
            'profile_records': 'profileRecords',
            'profile_string_variables': 'profileStringVariables',
            'profile_transitory_data': 'profileTransitoryData',
            'response_minted_timestamp': 'responseMintedTimestamp',
            'secondary_components_minted_timestamp': 'secondaryComponentsMintedTimestamp',
            'vendor_receipts': 'vendorReceipts'
        }

        self._character_activities = character_activities
        self._character_collectibles = character_collectibles
        self._character_craftables = character_craftables
        self._character_currency_lookups = character_currency_lookups
        self._character_equipment = character_equipment
        self._character_inventories = character_inventories
        self._character_kiosks = character_kiosks
        self._character_loadouts = character_loadouts
        self._character_plug_sets = character_plug_sets
        self._character_presentation_nodes = character_presentation_nodes
        self._character_progressions = character_progressions
        self._character_records = character_records
        self._character_render_data = character_render_data
        self._character_string_variables = character_string_variables
        self._character_uninstanced_item_components = character_uninstanced_item_components
        self._characters = characters
        self._item_components = item_components
        self._metrics = metrics
        self._platform_silver = platform_silver
        self._profile = profile
        self._profile_collectibles = profile_collectibles
        self._profile_commendations = profile_commendations
        self._profile_currencies = profile_currencies
        self._profile_inventory = profile_inventory
        self._profile_kiosks = profile_kiosks
        self._profile_plug_sets = profile_plug_sets
        self._profile_presentation_nodes = profile_presentation_nodes
        self._profile_progression = profile_progression
        self._profile_records = profile_records
        self._profile_string_variables = profile_string_variables
        self._profile_transitory_data = profile_transitory_data
        self._response_minted_timestamp = response_minted_timestamp
        self._secondary_components_minted_timestamp = secondary_components_minted_timestamp
        self._vendor_receipts = vendor_receipts

    @classmethod
    def from_dict(cls, dikt: dict) -> 'DestinyResponsesDestinyProfileResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Destiny.Responses.DestinyProfileResponse of this DestinyResponsesDestinyProfileResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def character_activities(self):
        """Gets the character_activities of this DestinyResponsesDestinyProfileResponse.

        Character activity data - the activities available to this character and its status, keyed by the Character's Id.  COMPONENT TYPE: CharacterActivities

        :return: The character_activities of this DestinyResponsesDestinyProfileResponse.
        :rtype: DictionaryComponentResponseOfint64AndDestinyCharacterActivitiesComponent
        """
        return self._character_activities

    @character_activities.setter
    def character_activities(self, character_activities):
        """Sets the character_activities of this DestinyResponsesDestinyProfileResponse.

        Character activity data - the activities available to this character and its status, keyed by the Character's Id.  COMPONENT TYPE: CharacterActivities

        :param character_activities: The character_activities of this DestinyResponsesDestinyProfileResponse.
        :type character_activities: DictionaryComponentResponseOfint64AndDestinyCharacterActivitiesComponent
        """

        self._character_activities = character_activities

    @property
    def character_collectibles(self):
        """Gets the character_collectibles of this DestinyResponsesDestinyProfileResponse.

        COMPONENT TYPE: Collectibles

        :return: The character_collectibles of this DestinyResponsesDestinyProfileResponse.
        :rtype: DictionaryComponentResponseOfint64AndDestinyCollectiblesComponent
        """
        return self._character_collectibles

    @character_collectibles.setter
    def character_collectibles(self, character_collectibles):
        """Sets the character_collectibles of this DestinyResponsesDestinyProfileResponse.

        COMPONENT TYPE: Collectibles

        :param character_collectibles: The character_collectibles of this DestinyResponsesDestinyProfileResponse.
        :type character_collectibles: DictionaryComponentResponseOfint64AndDestinyCollectiblesComponent
        """

        self._character_collectibles = character_collectibles

    @property
    def character_craftables(self):
        """Gets the character_craftables of this DestinyResponsesDestinyProfileResponse.

        COMPONENT TYPE: Craftables

        :return: The character_craftables of this DestinyResponsesDestinyProfileResponse.
        :rtype: DictionaryComponentResponseOfint64AndDestinyCraftablesComponent
        """
        return self._character_craftables

    @character_craftables.setter
    def character_craftables(self, character_craftables):
        """Sets the character_craftables of this DestinyResponsesDestinyProfileResponse.

        COMPONENT TYPE: Craftables

        :param character_craftables: The character_craftables of this DestinyResponsesDestinyProfileResponse.
        :type character_craftables: DictionaryComponentResponseOfint64AndDestinyCraftablesComponent
        """

        self._character_craftables = character_craftables

    @property
    def character_currency_lookups(self):
        """Gets the character_currency_lookups of this DestinyResponsesDestinyProfileResponse.

        A \"lookup\" convenience component that can be used to quickly check if the character has access to items that can be used for purchasing.  COMPONENT TYPE: CurrencyLookups

        :return: The character_currency_lookups of this DestinyResponsesDestinyProfileResponse.
        :rtype: DictionaryComponentResponseOfint64AndDestinyCurrenciesComponent
        """
        return self._character_currency_lookups

    @character_currency_lookups.setter
    def character_currency_lookups(self, character_currency_lookups):
        """Sets the character_currency_lookups of this DestinyResponsesDestinyProfileResponse.

        A \"lookup\" convenience component that can be used to quickly check if the character has access to items that can be used for purchasing.  COMPONENT TYPE: CurrencyLookups

        :param character_currency_lookups: The character_currency_lookups of this DestinyResponsesDestinyProfileResponse.
        :type character_currency_lookups: DictionaryComponentResponseOfint64AndDestinyCurrenciesComponent
        """

        self._character_currency_lookups = character_currency_lookups

    @property
    def character_equipment(self):
        """Gets the character_equipment of this DestinyResponsesDestinyProfileResponse.

        The character's equipped items, keyed by the Character's Id.  COMPONENT TYPE: CharacterEquipment

        :return: The character_equipment of this DestinyResponsesDestinyProfileResponse.
        :rtype: DictionaryComponentResponseOfint64AndDestinyInventoryComponent
        """
        return self._character_equipment

    @character_equipment.setter
    def character_equipment(self, character_equipment):
        """Sets the character_equipment of this DestinyResponsesDestinyProfileResponse.

        The character's equipped items, keyed by the Character's Id.  COMPONENT TYPE: CharacterEquipment

        :param character_equipment: The character_equipment of this DestinyResponsesDestinyProfileResponse.
        :type character_equipment: DictionaryComponentResponseOfint64AndDestinyInventoryComponent
        """

        self._character_equipment = character_equipment

    @property
    def character_inventories(self):
        """Gets the character_inventories of this DestinyResponsesDestinyProfileResponse.

        The character-level non-equipped inventory items, keyed by the Character's Id.  COMPONENT TYPE: CharacterInventories

        :return: The character_inventories of this DestinyResponsesDestinyProfileResponse.
        :rtype: DictionaryComponentResponseOfint64AndDestinyInventoryComponent
        """
        return self._character_inventories

    @character_inventories.setter
    def character_inventories(self, character_inventories):
        """Sets the character_inventories of this DestinyResponsesDestinyProfileResponse.

        The character-level non-equipped inventory items, keyed by the Character's Id.  COMPONENT TYPE: CharacterInventories

        :param character_inventories: The character_inventories of this DestinyResponsesDestinyProfileResponse.
        :type character_inventories: DictionaryComponentResponseOfint64AndDestinyInventoryComponent
        """

        self._character_inventories = character_inventories

    @property
    def character_kiosks(self):
        """Gets the character_kiosks of this DestinyResponsesDestinyProfileResponse.

        Items available from Kiosks that are available to a specific character as opposed to the account as a whole. It must be combined with data from the profileKiosks property to get a full picture of the character's available items to check out of a kiosk.  This component returns information about what Kiosk items are available to you on a *Character* level. Usually, kiosk items will be earned for the entire Profile (all characters) at once. To find those, look in the profileKiosks property.  COMPONENT TYPE: Kiosks

        :return: The character_kiosks of this DestinyResponsesDestinyProfileResponse.
        :rtype: DictionaryComponentResponseOfint64AndDestinyKiosksComponent
        """
        return self._character_kiosks

    @character_kiosks.setter
    def character_kiosks(self, character_kiosks):
        """Sets the character_kiosks of this DestinyResponsesDestinyProfileResponse.

        Items available from Kiosks that are available to a specific character as opposed to the account as a whole. It must be combined with data from the profileKiosks property to get a full picture of the character's available items to check out of a kiosk.  This component returns information about what Kiosk items are available to you on a *Character* level. Usually, kiosk items will be earned for the entire Profile (all characters) at once. To find those, look in the profileKiosks property.  COMPONENT TYPE: Kiosks

        :param character_kiosks: The character_kiosks of this DestinyResponsesDestinyProfileResponse.
        :type character_kiosks: DictionaryComponentResponseOfint64AndDestinyKiosksComponent
        """

        self._character_kiosks = character_kiosks

    @property
    def character_loadouts(self):
        """Gets the character_loadouts of this DestinyResponsesDestinyProfileResponse.

        The character loadouts, keyed by the Character's Id.  COMPONENT TYPE: CharacterLoadouts

        :return: The character_loadouts of this DestinyResponsesDestinyProfileResponse.
        :rtype: DictionaryComponentResponseOfint64AndDestinyLoadoutsComponent
        """
        return self._character_loadouts

    @character_loadouts.setter
    def character_loadouts(self, character_loadouts):
        """Sets the character_loadouts of this DestinyResponsesDestinyProfileResponse.

        The character loadouts, keyed by the Character's Id.  COMPONENT TYPE: CharacterLoadouts

        :param character_loadouts: The character_loadouts of this DestinyResponsesDestinyProfileResponse.
        :type character_loadouts: DictionaryComponentResponseOfint64AndDestinyLoadoutsComponent
        """

        self._character_loadouts = character_loadouts

    @property
    def character_plug_sets(self):
        """Gets the character_plug_sets of this DestinyResponsesDestinyProfileResponse.

        When sockets refer to reusable Plug Sets (see DestinyPlugSetDefinition for more info), this is the set of plugs and their states, per character, that are character-scoped.  This comes back with ItemSockets, as it is needed for a complete picture of the sockets on requested items.  COMPONENT TYPE: ItemSockets

        :return: The character_plug_sets of this DestinyResponsesDestinyProfileResponse.
        :rtype: DictionaryComponentResponseOfint64AndDestinyPlugSetsComponent
        """
        return self._character_plug_sets

    @character_plug_sets.setter
    def character_plug_sets(self, character_plug_sets):
        """Sets the character_plug_sets of this DestinyResponsesDestinyProfileResponse.

        When sockets refer to reusable Plug Sets (see DestinyPlugSetDefinition for more info), this is the set of plugs and their states, per character, that are character-scoped.  This comes back with ItemSockets, as it is needed for a complete picture of the sockets on requested items.  COMPONENT TYPE: ItemSockets

        :param character_plug_sets: The character_plug_sets of this DestinyResponsesDestinyProfileResponse.
        :type character_plug_sets: DictionaryComponentResponseOfint64AndDestinyPlugSetsComponent
        """

        self._character_plug_sets = character_plug_sets

    @property
    def character_presentation_nodes(self):
        """Gets the character_presentation_nodes of this DestinyResponsesDestinyProfileResponse.

        COMPONENT TYPE: PresentationNodes

        :return: The character_presentation_nodes of this DestinyResponsesDestinyProfileResponse.
        :rtype: DictionaryComponentResponseOfint64AndDestinyPresentationNodesComponent
        """
        return self._character_presentation_nodes

    @character_presentation_nodes.setter
    def character_presentation_nodes(self, character_presentation_nodes):
        """Sets the character_presentation_nodes of this DestinyResponsesDestinyProfileResponse.

        COMPONENT TYPE: PresentationNodes

        :param character_presentation_nodes: The character_presentation_nodes of this DestinyResponsesDestinyProfileResponse.
        :type character_presentation_nodes: DictionaryComponentResponseOfint64AndDestinyPresentationNodesComponent
        """

        self._character_presentation_nodes = character_presentation_nodes

    @property
    def character_progressions(self):
        """Gets the character_progressions of this DestinyResponsesDestinyProfileResponse.

        Character-level progression data, keyed by the Character's Id.  COMPONENT TYPE: CharacterProgressions

        :return: The character_progressions of this DestinyResponsesDestinyProfileResponse.
        :rtype: DictionaryComponentResponseOfint64AndDestinyCharacterProgressionComponent
        """
        return self._character_progressions

    @character_progressions.setter
    def character_progressions(self, character_progressions):
        """Sets the character_progressions of this DestinyResponsesDestinyProfileResponse.

        Character-level progression data, keyed by the Character's Id.  COMPONENT TYPE: CharacterProgressions

        :param character_progressions: The character_progressions of this DestinyResponsesDestinyProfileResponse.
        :type character_progressions: DictionaryComponentResponseOfint64AndDestinyCharacterProgressionComponent
        """

        self._character_progressions = character_progressions

    @property
    def character_records(self):
        """Gets the character_records of this DestinyResponsesDestinyProfileResponse.

        COMPONENT TYPE: Records

        :return: The character_records of this DestinyResponsesDestinyProfileResponse.
        :rtype: DictionaryComponentResponseOfint64AndDestinyCharacterRecordsComponent
        """
        return self._character_records

    @character_records.setter
    def character_records(self, character_records):
        """Sets the character_records of this DestinyResponsesDestinyProfileResponse.

        COMPONENT TYPE: Records

        :param character_records: The character_records of this DestinyResponsesDestinyProfileResponse.
        :type character_records: DictionaryComponentResponseOfint64AndDestinyCharacterRecordsComponent
        """

        self._character_records = character_records

    @property
    def character_render_data(self):
        """Gets the character_render_data of this DestinyResponsesDestinyProfileResponse.

        Character rendering data - a minimal set of info needed to render a character in 3D - keyed by the Character's Id.  COMPONENT TYPE: CharacterRenderData

        :return: The character_render_data of this DestinyResponsesDestinyProfileResponse.
        :rtype: DictionaryComponentResponseOfint64AndDestinyCharacterRenderComponent
        """
        return self._character_render_data

    @character_render_data.setter
    def character_render_data(self, character_render_data):
        """Sets the character_render_data of this DestinyResponsesDestinyProfileResponse.

        Character rendering data - a minimal set of info needed to render a character in 3D - keyed by the Character's Id.  COMPONENT TYPE: CharacterRenderData

        :param character_render_data: The character_render_data of this DestinyResponsesDestinyProfileResponse.
        :type character_render_data: DictionaryComponentResponseOfint64AndDestinyCharacterRenderComponent
        """

        self._character_render_data = character_render_data

    @property
    def character_string_variables(self):
        """Gets the character_string_variables of this DestinyResponsesDestinyProfileResponse.

        COMPONENT TYPE: StringVariables

        :return: The character_string_variables of this DestinyResponsesDestinyProfileResponse.
        :rtype: DictionaryComponentResponseOfint64AndDestinyStringVariablesComponent
        """
        return self._character_string_variables

    @character_string_variables.setter
    def character_string_variables(self, character_string_variables):
        """Sets the character_string_variables of this DestinyResponsesDestinyProfileResponse.

        COMPONENT TYPE: StringVariables

        :param character_string_variables: The character_string_variables of this DestinyResponsesDestinyProfileResponse.
        :type character_string_variables: DictionaryComponentResponseOfint64AndDestinyStringVariablesComponent
        """

        self._character_string_variables = character_string_variables

    @property
    def character_uninstanced_item_components(self):
        """Gets the character_uninstanced_item_components of this DestinyResponsesDestinyProfileResponse.

        Do you ever get the feeling that a system was designed *too* flexibly? That it can be used in so many different ways that you end up being unable to provide an easy to use abstraction for the mess that's happening under the surface?  Let's talk about character-specific data that might be related to items without instances. These two statements are totally unrelated, I promise.  At some point during D2, it was decided that items - such as Bounties - could be given to characters and *not* have instance data, but that *could* display and even use relevant state information on your account and character.  Up to now, any item that had meaningful dependencies on character or account state had to be instanced, and thus \"itemComponents\" was all that you needed: it was keyed by item's instance IDs and provided the stateful information you needed inside.  Unfortunately, we don't live in such a magical world anymore. This is information held on a per-character basis about non-instanced items that the characters have in their inventory - or that reference character-specific state information even if it's in Account-level inventory - and the values related to that item's state in relation to the given character.  To give a concrete example, look at a Moments of Triumph bounty. They exist in a character's inventory, and show/care about a character's progression toward completing the bounty. But the bounty itself is a non-instanced item, like a mod or a currency. This returns that data for the characters who have the bounty in their inventory.  I'm not crying, you're crying Okay we're both crying but it's going to be okay I promise Actually I shouldn't promise that, I don't know if it's going to be okay

        :return: The character_uninstanced_item_components of this DestinyResponsesDestinyProfileResponse.
        :rtype: Dict[str, DestinyBaseItemComponentSetOfuint32]
        """
        return self._character_uninstanced_item_components

    @character_uninstanced_item_components.setter
    def character_uninstanced_item_components(self, character_uninstanced_item_components):
        """Sets the character_uninstanced_item_components of this DestinyResponsesDestinyProfileResponse.

        Do you ever get the feeling that a system was designed *too* flexibly? That it can be used in so many different ways that you end up being unable to provide an easy to use abstraction for the mess that's happening under the surface?  Let's talk about character-specific data that might be related to items without instances. These two statements are totally unrelated, I promise.  At some point during D2, it was decided that items - such as Bounties - could be given to characters and *not* have instance data, but that *could* display and even use relevant state information on your account and character.  Up to now, any item that had meaningful dependencies on character or account state had to be instanced, and thus \"itemComponents\" was all that you needed: it was keyed by item's instance IDs and provided the stateful information you needed inside.  Unfortunately, we don't live in such a magical world anymore. This is information held on a per-character basis about non-instanced items that the characters have in their inventory - or that reference character-specific state information even if it's in Account-level inventory - and the values related to that item's state in relation to the given character.  To give a concrete example, look at a Moments of Triumph bounty. They exist in a character's inventory, and show/care about a character's progression toward completing the bounty. But the bounty itself is a non-instanced item, like a mod or a currency. This returns that data for the characters who have the bounty in their inventory.  I'm not crying, you're crying Okay we're both crying but it's going to be okay I promise Actually I shouldn't promise that, I don't know if it's going to be okay

        :param character_uninstanced_item_components: The character_uninstanced_item_components of this DestinyResponsesDestinyProfileResponse.
        :type character_uninstanced_item_components: Dict[str, DestinyBaseItemComponentSetOfuint32]
        """

        self._character_uninstanced_item_components = character_uninstanced_item_components

    @property
    def characters(self):
        """Gets the characters of this DestinyResponsesDestinyProfileResponse.

        Basic information about each character, keyed by the CharacterId.  COMPONENT TYPE: Characters

        :return: The characters of this DestinyResponsesDestinyProfileResponse.
        :rtype: DictionaryComponentResponseOfint64AndDestinyCharacterComponent
        """
        return self._characters

    @characters.setter
    def characters(self, characters):
        """Sets the characters of this DestinyResponsesDestinyProfileResponse.

        Basic information about each character, keyed by the CharacterId.  COMPONENT TYPE: Characters

        :param characters: The characters of this DestinyResponsesDestinyProfileResponse.
        :type characters: DictionaryComponentResponseOfint64AndDestinyCharacterComponent
        """

        self._characters = characters

    @property
    def item_components(self):
        """Gets the item_components of this DestinyResponsesDestinyProfileResponse.

        Information about instanced items across all returned characters, keyed by the item's instance ID.  COMPONENT TYPE: [See inside the DestinyItemComponentSet contract for component types.]

        :return: The item_components of this DestinyResponsesDestinyProfileResponse.
        :rtype: DestinyItemComponentSetOfint64
        """
        return self._item_components

    @item_components.setter
    def item_components(self, item_components):
        """Sets the item_components of this DestinyResponsesDestinyProfileResponse.

        Information about instanced items across all returned characters, keyed by the item's instance ID.  COMPONENT TYPE: [See inside the DestinyItemComponentSet contract for component types.]

        :param item_components: The item_components of this DestinyResponsesDestinyProfileResponse.
        :type item_components: DestinyItemComponentSetOfint64
        """

        self._item_components = item_components

    @property
    def metrics(self):
        """Gets the metrics of this DestinyResponsesDestinyProfileResponse.

        COMPONENT TYPE: Metrics

        :return: The metrics of this DestinyResponsesDestinyProfileResponse.
        :rtype: SingleComponentResponseOfDestinyMetricsComponent
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this DestinyResponsesDestinyProfileResponse.

        COMPONENT TYPE: Metrics

        :param metrics: The metrics of this DestinyResponsesDestinyProfileResponse.
        :type metrics: SingleComponentResponseOfDestinyMetricsComponent
        """

        self._metrics = metrics

    @property
    def platform_silver(self):
        """Gets the platform_silver of this DestinyResponsesDestinyProfileResponse.

        Silver quantities for any platform on which this Profile plays destiny.   COMPONENT TYPE: PlatformSilver

        :return: The platform_silver of this DestinyResponsesDestinyProfileResponse.
        :rtype: SingleComponentResponseOfDestinyPlatformSilverComponent
        """
        return self._platform_silver

    @platform_silver.setter
    def platform_silver(self, platform_silver):
        """Sets the platform_silver of this DestinyResponsesDestinyProfileResponse.

        Silver quantities for any platform on which this Profile plays destiny.   COMPONENT TYPE: PlatformSilver

        :param platform_silver: The platform_silver of this DestinyResponsesDestinyProfileResponse.
        :type platform_silver: SingleComponentResponseOfDestinyPlatformSilverComponent
        """

        self._platform_silver = platform_silver

    @property
    def profile(self):
        """Gets the profile of this DestinyResponsesDestinyProfileResponse.

        The basic information about the Destiny Profile (formerly \"Account\").  COMPONENT TYPE: Profiles

        :return: The profile of this DestinyResponsesDestinyProfileResponse.
        :rtype: SingleComponentResponseOfDestinyProfileComponent
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        """Sets the profile of this DestinyResponsesDestinyProfileResponse.

        The basic information about the Destiny Profile (formerly \"Account\").  COMPONENT TYPE: Profiles

        :param profile: The profile of this DestinyResponsesDestinyProfileResponse.
        :type profile: SingleComponentResponseOfDestinyProfileComponent
        """

        self._profile = profile

    @property
    def profile_collectibles(self):
        """Gets the profile_collectibles of this DestinyResponsesDestinyProfileResponse.

        COMPONENT TYPE: Collectibles

        :return: The profile_collectibles of this DestinyResponsesDestinyProfileResponse.
        :rtype: SingleComponentResponseOfDestinyProfileCollectiblesComponent
        """
        return self._profile_collectibles

    @profile_collectibles.setter
    def profile_collectibles(self, profile_collectibles):
        """Sets the profile_collectibles of this DestinyResponsesDestinyProfileResponse.

        COMPONENT TYPE: Collectibles

        :param profile_collectibles: The profile_collectibles of this DestinyResponsesDestinyProfileResponse.
        :type profile_collectibles: SingleComponentResponseOfDestinyProfileCollectiblesComponent
        """

        self._profile_collectibles = profile_collectibles

    @property
    def profile_commendations(self):
        """Gets the profile_commendations of this DestinyResponsesDestinyProfileResponse.

        COMPONENT TYPE: SocialCommendations

        :return: The profile_commendations of this DestinyResponsesDestinyProfileResponse.
        :rtype: SingleComponentResponseOfDestinySocialCommendationsComponent
        """
        return self._profile_commendations

    @profile_commendations.setter
    def profile_commendations(self, profile_commendations):
        """Sets the profile_commendations of this DestinyResponsesDestinyProfileResponse.

        COMPONENT TYPE: SocialCommendations

        :param profile_commendations: The profile_commendations of this DestinyResponsesDestinyProfileResponse.
        :type profile_commendations: SingleComponentResponseOfDestinySocialCommendationsComponent
        """

        self._profile_commendations = profile_commendations

    @property
    def profile_currencies(self):
        """Gets the profile_currencies of this DestinyResponsesDestinyProfileResponse.

        The profile-level currencies owned by the Destiny Profile.  COMPONENT TYPE: ProfileCurrencies

        :return: The profile_currencies of this DestinyResponsesDestinyProfileResponse.
        :rtype: SingleComponentResponseOfDestinyInventoryComponent
        """
        return self._profile_currencies

    @profile_currencies.setter
    def profile_currencies(self, profile_currencies):
        """Sets the profile_currencies of this DestinyResponsesDestinyProfileResponse.

        The profile-level currencies owned by the Destiny Profile.  COMPONENT TYPE: ProfileCurrencies

        :param profile_currencies: The profile_currencies of this DestinyResponsesDestinyProfileResponse.
        :type profile_currencies: SingleComponentResponseOfDestinyInventoryComponent
        """

        self._profile_currencies = profile_currencies

    @property
    def profile_inventory(self):
        """Gets the profile_inventory of this DestinyResponsesDestinyProfileResponse.

        The profile-level inventory of the Destiny Profile.  COMPONENT TYPE: ProfileInventories

        :return: The profile_inventory of this DestinyResponsesDestinyProfileResponse.
        :rtype: SingleComponentResponseOfDestinyInventoryComponent
        """
        return self._profile_inventory

    @profile_inventory.setter
    def profile_inventory(self, profile_inventory):
        """Sets the profile_inventory of this DestinyResponsesDestinyProfileResponse.

        The profile-level inventory of the Destiny Profile.  COMPONENT TYPE: ProfileInventories

        :param profile_inventory: The profile_inventory of this DestinyResponsesDestinyProfileResponse.
        :type profile_inventory: SingleComponentResponseOfDestinyInventoryComponent
        """

        self._profile_inventory = profile_inventory

    @property
    def profile_kiosks(self):
        """Gets the profile_kiosks of this DestinyResponsesDestinyProfileResponse.

        Items available from Kiosks that are available Profile-wide (i.e. across all characters)  This component returns information about what Kiosk items are available to you on a *Profile* level. It is theoretically possible for Kiosks to have items gated by specific Character as well. If you ever have those, you will find them on the characterKiosks property.  COMPONENT TYPE: Kiosks

        :return: The profile_kiosks of this DestinyResponsesDestinyProfileResponse.
        :rtype: SingleComponentResponseOfDestinyKiosksComponent
        """
        return self._profile_kiosks

    @profile_kiosks.setter
    def profile_kiosks(self, profile_kiosks):
        """Sets the profile_kiosks of this DestinyResponsesDestinyProfileResponse.

        Items available from Kiosks that are available Profile-wide (i.e. across all characters)  This component returns information about what Kiosk items are available to you on a *Profile* level. It is theoretically possible for Kiosks to have items gated by specific Character as well. If you ever have those, you will find them on the characterKiosks property.  COMPONENT TYPE: Kiosks

        :param profile_kiosks: The profile_kiosks of this DestinyResponsesDestinyProfileResponse.
        :type profile_kiosks: SingleComponentResponseOfDestinyKiosksComponent
        """

        self._profile_kiosks = profile_kiosks

    @property
    def profile_plug_sets(self):
        """Gets the profile_plug_sets of this DestinyResponsesDestinyProfileResponse.

        When sockets refer to reusable Plug Sets (see DestinyPlugSetDefinition for more info), this is the set of plugs and their states that are profile-scoped.  This comes back with ItemSockets, as it is needed for a complete picture of the sockets on requested items.  COMPONENT TYPE: ItemSockets

        :return: The profile_plug_sets of this DestinyResponsesDestinyProfileResponse.
        :rtype: SingleComponentResponseOfDestinyPlugSetsComponent
        """
        return self._profile_plug_sets

    @profile_plug_sets.setter
    def profile_plug_sets(self, profile_plug_sets):
        """Sets the profile_plug_sets of this DestinyResponsesDestinyProfileResponse.

        When sockets refer to reusable Plug Sets (see DestinyPlugSetDefinition for more info), this is the set of plugs and their states that are profile-scoped.  This comes back with ItemSockets, as it is needed for a complete picture of the sockets on requested items.  COMPONENT TYPE: ItemSockets

        :param profile_plug_sets: The profile_plug_sets of this DestinyResponsesDestinyProfileResponse.
        :type profile_plug_sets: SingleComponentResponseOfDestinyPlugSetsComponent
        """

        self._profile_plug_sets = profile_plug_sets

    @property
    def profile_presentation_nodes(self):
        """Gets the profile_presentation_nodes of this DestinyResponsesDestinyProfileResponse.

        COMPONENT TYPE: PresentationNodes

        :return: The profile_presentation_nodes of this DestinyResponsesDestinyProfileResponse.
        :rtype: SingleComponentResponseOfDestinyPresentationNodesComponent
        """
        return self._profile_presentation_nodes

    @profile_presentation_nodes.setter
    def profile_presentation_nodes(self, profile_presentation_nodes):
        """Sets the profile_presentation_nodes of this DestinyResponsesDestinyProfileResponse.

        COMPONENT TYPE: PresentationNodes

        :param profile_presentation_nodes: The profile_presentation_nodes of this DestinyResponsesDestinyProfileResponse.
        :type profile_presentation_nodes: SingleComponentResponseOfDestinyPresentationNodesComponent
        """

        self._profile_presentation_nodes = profile_presentation_nodes

    @property
    def profile_progression(self):
        """Gets the profile_progression of this DestinyResponsesDestinyProfileResponse.

        When we have progression information - such as Checklists - that may apply profile-wide, it will be returned here rather than in the per-character progression data.  COMPONENT TYPE: ProfileProgression

        :return: The profile_progression of this DestinyResponsesDestinyProfileResponse.
        :rtype: SingleComponentResponseOfDestinyProfileProgressionComponent
        """
        return self._profile_progression

    @profile_progression.setter
    def profile_progression(self, profile_progression):
        """Sets the profile_progression of this DestinyResponsesDestinyProfileResponse.

        When we have progression information - such as Checklists - that may apply profile-wide, it will be returned here rather than in the per-character progression data.  COMPONENT TYPE: ProfileProgression

        :param profile_progression: The profile_progression of this DestinyResponsesDestinyProfileResponse.
        :type profile_progression: SingleComponentResponseOfDestinyProfileProgressionComponent
        """

        self._profile_progression = profile_progression

    @property
    def profile_records(self):
        """Gets the profile_records of this DestinyResponsesDestinyProfileResponse.

        COMPONENT TYPE: Records

        :return: The profile_records of this DestinyResponsesDestinyProfileResponse.
        :rtype: SingleComponentResponseOfDestinyProfileRecordsComponent
        """
        return self._profile_records

    @profile_records.setter
    def profile_records(self, profile_records):
        """Sets the profile_records of this DestinyResponsesDestinyProfileResponse.

        COMPONENT TYPE: Records

        :param profile_records: The profile_records of this DestinyResponsesDestinyProfileResponse.
        :type profile_records: SingleComponentResponseOfDestinyProfileRecordsComponent
        """

        self._profile_records = profile_records

    @property
    def profile_string_variables(self):
        """Gets the profile_string_variables of this DestinyResponsesDestinyProfileResponse.

        COMPONENT TYPE: StringVariables

        :return: The profile_string_variables of this DestinyResponsesDestinyProfileResponse.
        :rtype: SingleComponentResponseOfDestinyStringVariablesComponent
        """
        return self._profile_string_variables

    @profile_string_variables.setter
    def profile_string_variables(self, profile_string_variables):
        """Sets the profile_string_variables of this DestinyResponsesDestinyProfileResponse.

        COMPONENT TYPE: StringVariables

        :param profile_string_variables: The profile_string_variables of this DestinyResponsesDestinyProfileResponse.
        :type profile_string_variables: SingleComponentResponseOfDestinyStringVariablesComponent
        """

        self._profile_string_variables = profile_string_variables

    @property
    def profile_transitory_data(self):
        """Gets the profile_transitory_data of this DestinyResponsesDestinyProfileResponse.

        COMPONENT TYPE: Transitory

        :return: The profile_transitory_data of this DestinyResponsesDestinyProfileResponse.
        :rtype: SingleComponentResponseOfDestinyProfileTransitoryComponent
        """
        return self._profile_transitory_data

    @profile_transitory_data.setter
    def profile_transitory_data(self, profile_transitory_data):
        """Sets the profile_transitory_data of this DestinyResponsesDestinyProfileResponse.

        COMPONENT TYPE: Transitory

        :param profile_transitory_data: The profile_transitory_data of this DestinyResponsesDestinyProfileResponse.
        :type profile_transitory_data: SingleComponentResponseOfDestinyProfileTransitoryComponent
        """

        self._profile_transitory_data = profile_transitory_data

    @property
    def response_minted_timestamp(self):
        """Gets the response_minted_timestamp of this DestinyResponsesDestinyProfileResponse.

        Records the timestamp of when most components were last generated from the world server source. Unless the component type is specified in the documentation for secondaryComponentsMintedTimestamp, this value is sufficient to do data freshness.

        :return: The response_minted_timestamp of this DestinyResponsesDestinyProfileResponse.
        :rtype: datetime
        """
        return self._response_minted_timestamp

    @response_minted_timestamp.setter
    def response_minted_timestamp(self, response_minted_timestamp):
        """Sets the response_minted_timestamp of this DestinyResponsesDestinyProfileResponse.

        Records the timestamp of when most components were last generated from the world server source. Unless the component type is specified in the documentation for secondaryComponentsMintedTimestamp, this value is sufficient to do data freshness.

        :param response_minted_timestamp: The response_minted_timestamp of this DestinyResponsesDestinyProfileResponse.
        :type response_minted_timestamp: datetime
        """

        self._response_minted_timestamp = response_minted_timestamp

    @property
    def secondary_components_minted_timestamp(self):
        """Gets the secondary_components_minted_timestamp of this DestinyResponsesDestinyProfileResponse.

        Some secondary components are not tracked in the primary response timestamp and have their timestamp tracked here. If your component is any of the following, this field is where you will find your timestamp value:   PresentationNodes, Records, Collectibles, Metrics, StringVariables, Craftables, Transitory   All other component types may use the primary timestamp property.

        :return: The secondary_components_minted_timestamp of this DestinyResponsesDestinyProfileResponse.
        :rtype: datetime
        """
        return self._secondary_components_minted_timestamp

    @secondary_components_minted_timestamp.setter
    def secondary_components_minted_timestamp(self, secondary_components_minted_timestamp):
        """Sets the secondary_components_minted_timestamp of this DestinyResponsesDestinyProfileResponse.

        Some secondary components are not tracked in the primary response timestamp and have their timestamp tracked here. If your component is any of the following, this field is where you will find your timestamp value:   PresentationNodes, Records, Collectibles, Metrics, StringVariables, Craftables, Transitory   All other component types may use the primary timestamp property.

        :param secondary_components_minted_timestamp: The secondary_components_minted_timestamp of this DestinyResponsesDestinyProfileResponse.
        :type secondary_components_minted_timestamp: datetime
        """

        self._secondary_components_minted_timestamp = secondary_components_minted_timestamp

    @property
    def vendor_receipts(self):
        """Gets the vendor_receipts of this DestinyResponsesDestinyProfileResponse.

        Recent, refundable purchases you have made from vendors. When will you use it? Couldn't say...  COMPONENT TYPE: VendorReceipts

        :return: The vendor_receipts of this DestinyResponsesDestinyProfileResponse.
        :rtype: SingleComponentResponseOfDestinyVendorReceiptsComponent
        """
        return self._vendor_receipts

    @vendor_receipts.setter
    def vendor_receipts(self, vendor_receipts):
        """Sets the vendor_receipts of this DestinyResponsesDestinyProfileResponse.

        Recent, refundable purchases you have made from vendors. When will you use it? Couldn't say...  COMPONENT TYPE: VendorReceipts

        :param vendor_receipts: The vendor_receipts of this DestinyResponsesDestinyProfileResponse.
        :type vendor_receipts: SingleComponentResponseOfDestinyVendorReceiptsComponent
        """

        self._vendor_receipts = vendor_receipts
