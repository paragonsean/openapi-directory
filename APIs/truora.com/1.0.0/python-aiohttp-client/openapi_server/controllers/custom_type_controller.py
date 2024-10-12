from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.score_config_output import ScoreConfigOutput
from openapi_server.models.score_configs_output import ScoreConfigsOutput
from openapi_server import util


async def create_score_config(request: web.Request, country, type, dataset_affiliations_and_insurances=None, dataset_alert_in_media=None, dataset_business_background=None, dataset_criminal_record=None, dataset_driving_licenses=None, dataset_international_background=None, dataset_legal_background=None, dataset_personal_identity=None, dataset_professional_background=None, dataset_taxes_and_finances=None, dataset_traffic_fines=None, dataset_vehicle_information=None, dataset_vehicle_permits=None) -> web.Response:
    """Create Score Configurations

    Create a custom score configuration selecting the weight for each background check dataset and the country where it applies. Weights are numbers between 0 and 1 that represent how impactful the dataset is for the score. Keep in mind that the sum of all weights must equal 1.

    :param country: Country where this set of rules applies. Use \\\&quot;all\\\&quot; if the check type searches by name by relying on international databases
    :type country: str
    :param type: Score configuration name. It cannot be person, vehicle, or company
    :type type: str
    :param dataset_affiliations_and_insurances: Affiliation and insurance weight for score calculation. From 0 to 1
    :type dataset_affiliations_and_insurances: float
    :param dataset_alert_in_media: Alert in media weight for score calculation. From 0 to 1
    :type dataset_alert_in_media: float
    :param dataset_business_background: Business background weight for score calculation. From 0 to 1
    :type dataset_business_background: float
    :param dataset_criminal_record: Criminal record weight for score calculation. From 0 to 1
    :type dataset_criminal_record: float
    :param dataset_driving_licenses: Driving license weight for score calculation. From 0 to 1
    :type dataset_driving_licenses: float
    :param dataset_international_background: International background weight for score calculation. From 0 to 1
    :type dataset_international_background: float
    :param dataset_legal_background: Legal background weight for score calculation. From 0 to 1
    :type dataset_legal_background: float
    :param dataset_personal_identity: Personal identity weight for score calculation. From 0 to 1
    :type dataset_personal_identity: float
    :param dataset_professional_background: Professional background weight for score calculation. From 0 to 1
    :type dataset_professional_background: float
    :param dataset_taxes_and_finances: Taxes and financial background weight for score calculation. From 0 to 1
    :type dataset_taxes_and_finances: float
    :param dataset_traffic_fines: Traffic fines weight for score calculation. From 0 to 1
    :type dataset_traffic_fines: float
    :param dataset_vehicle_information: Vehicle information weight for score calculation. From 0 to 1
    :type dataset_vehicle_information: float
    :param dataset_vehicle_permits: Vehicle certificate background weight for score calculation. From 0 to 1
    :type dataset_vehicle_permits: float

    """
    return web.Response(status=200)


async def delete_custom_type(request: web.Request, type, country=None) -> web.Response:
    """Delete Custom Type

    Allows deleting a custom type. Person, vehicle, and company types cannot be deleted

    :param type: Name of the custom type to be deleted
    :type type: str
    :param country: Country where the custom type is valid
    :type country: str

    """
    return web.Response(status=200)


async def list_score_configs(request: web.Request, start_key=None) -> web.Response:
    """List Score Configurations

    Lists the custom score configurations of the associated account.

    :param start_key: The key to start the pagination
    :type start_key: str

    """
    return web.Response(status=200)


async def update_custom_type(request: web.Request, country, type, dataset_affiliations_and_insurances=None, dataset_alert_in_media=None, dataset_business_background=None, dataset_criminal_record=None, dataset_driving_licenses=None, dataset_international_background=None, dataset_legal_background=None, dataset_personal_identity=None, dataset_professional_background=None, dataset_taxes_and_finances=None, dataset_traffic_fines=None, dataset_vehicle_information=None, dataset_vehicle_permits=None) -> web.Response:
    """Update Custom Type

    Allows updating a custom type. Person, vehicle, and company types are not modifiable

    :param country: Country where this set of rules applies. Use \\\&quot;all\\\&quot; if the check type searches by name by relying on international databases
    :type country: str
    :param type: Score configuration name. It cannot be person, vehicle, or company
    :type type: str
    :param dataset_affiliations_and_insurances: Affiliation and insurance weight for score calculation. From 0 to 1
    :type dataset_affiliations_and_insurances: float
    :param dataset_alert_in_media: Alert in media weight for score calculation. From 0 to 1
    :type dataset_alert_in_media: float
    :param dataset_business_background: Business background weight for score calculation. From 0 to 1
    :type dataset_business_background: float
    :param dataset_criminal_record: Criminal record weight for score calculation. From 0 to 1
    :type dataset_criminal_record: float
    :param dataset_driving_licenses: Driving license weight for score calculation. From 0 to 1
    :type dataset_driving_licenses: float
    :param dataset_international_background: International background weight for score calculation. From 0 to 1
    :type dataset_international_background: float
    :param dataset_legal_background: Legal background weight for score calculation. From 0 to 1
    :type dataset_legal_background: float
    :param dataset_personal_identity: Personal identity weight for score calculation. From 0 to 1
    :type dataset_personal_identity: float
    :param dataset_professional_background: Professional background weight for score calculation. From 0 to 1
    :type dataset_professional_background: float
    :param dataset_taxes_and_finances: Taxes and financial background weight for score calculation. From 0 to 1
    :type dataset_taxes_and_finances: float
    :param dataset_traffic_fines: Traffic fines weight for score calculation. From 0 to 1
    :type dataset_traffic_fines: float
    :param dataset_vehicle_information: Vehicle information weight for score calculation. From 0 to 1
    :type dataset_vehicle_information: float
    :param dataset_vehicle_permits: Vehicle certificate background weight for score calculation. From 0 to 1
    :type dataset_vehicle_permits: float

    """
    return web.Response(status=200)
