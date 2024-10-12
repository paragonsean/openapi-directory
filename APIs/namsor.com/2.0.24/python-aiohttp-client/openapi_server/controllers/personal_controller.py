from typing import List, Dict
from aiohttp import web

from openapi_server.models.batch_corridor_in import BatchCorridorIn
from openapi_server.models.batch_corridor_out import BatchCorridorOut
from openapi_server.models.batch_first_last_name_diasporaed_out import BatchFirstLastNameDiasporaedOut
from openapi_server.models.batch_first_last_name_gendered_out import BatchFirstLastNameGenderedOut
from openapi_server.models.batch_first_last_name_geo_in import BatchFirstLastNameGeoIn
from openapi_server.models.batch_first_last_name_geo_subclassification_out import BatchFirstLastNameGeoSubclassificationOut
from openapi_server.models.batch_first_last_name_geo_zipped_in import BatchFirstLastNameGeoZippedIn
from openapi_server.models.batch_first_last_name_in import BatchFirstLastNameIn
from openapi_server.models.batch_first_last_name_origined_out import BatchFirstLastNameOriginedOut
from openapi_server.models.batch_first_last_name_us_race_ethnicity_out import BatchFirstLastNameUSRaceEthnicityOut
from openapi_server.models.batch_personal_name_gendered_out import BatchPersonalNameGenderedOut
from openapi_server.models.batch_personal_name_geo_in import BatchPersonalNameGeoIn
from openapi_server.models.batch_personal_name_geo_out import BatchPersonalNameGeoOut
from openapi_server.models.batch_personal_name_geo_subclassification_out import BatchPersonalNameGeoSubclassificationOut
from openapi_server.models.batch_personal_name_geo_subdivision_in import BatchPersonalNameGeoSubdivisionIn
from openapi_server.models.batch_personal_name_in import BatchPersonalNameIn
from openapi_server.models.batch_personal_name_parsed_out import BatchPersonalNameParsedOut
from openapi_server.models.batch_personal_name_religioned_out import BatchPersonalNameReligionedOut
from openapi_server.models.corridor_out import CorridorOut
from openapi_server.models.first_last_name_diasporaed_out import FirstLastNameDiasporaedOut
from openapi_server.models.first_last_name_gendered_out import FirstLastNameGenderedOut
from openapi_server.models.first_last_name_geo_subclassification_out import FirstLastNameGeoSubclassificationOut
from openapi_server.models.first_last_name_origined_out import FirstLastNameOriginedOut
from openapi_server.models.first_last_name_us_race_ethnicity_out import FirstLastNameUSRaceEthnicityOut
from openapi_server.models.personal_name_gendered_out import PersonalNameGenderedOut
from openapi_server.models.personal_name_geo_out import PersonalNameGeoOut
from openapi_server.models.personal_name_parsed_out import PersonalNameParsedOut
from openapi_server.models.personal_name_religioned_out import PersonalNameReligionedOut
from openapi_server import util


async def corridor(request: web.Request, country_iso2_from, first_name_from, last_name_from, country_iso2_to, first_name_to, last_name_to) -> web.Response:
    """[USES 20 UNITS PER NAME COUPLE] Infer several classifications for a cross border interaction between names (ex. remit, travel, intl com)

    

    :param country_iso2_from: 
    :type country_iso2_from: str
    :param first_name_from: 
    :type first_name_from: str
    :param last_name_from: 
    :type last_name_from: str
    :param country_iso2_to: 
    :type country_iso2_to: str
    :param first_name_to: 
    :type first_name_to: str
    :param last_name_to: 
    :type last_name_to: str

    """
    return web.Response(status=200)


async def corridor_batch(request: web.Request, body=None) -> web.Response:
    """[USES 20 UNITS PER NAME PAIR] Infer several classifications for up to 100 cross border interaction between names (ex. remit, travel, intl com)

    

    :param body: A list of name pairs, with country code (nameFrom -&gt; nameTo).
    :type body: dict | bytes

    """
    body = BatchCorridorIn.from_dict(body)
    return web.Response(status=200)


async def country(request: web.Request, personal_name_full) -> web.Response:
    """[USES 10 UNITS PER NAME] Infer the likely country of residence of a personal full name, or one surname. Assumes names as they are in the country of residence OR the country of origin.

    

    :param personal_name_full: 
    :type personal_name_full: str

    """
    return web.Response(status=200)


async def country_batch(request: web.Request, body=None) -> web.Response:
    """[USES 10 UNITS PER NAME] Infer the likely country of residence of up to 100 personal full names, or surnames. Assumes names as they are in the country of residence OR the country of origin.

    

    :param body: A list of personal names
    :type body: dict | bytes

    """
    body = BatchPersonalNameIn.from_dict(body)
    return web.Response(status=200)


async def diaspora(request: web.Request, country_iso2, first_name, last_name) -> web.Response:
    """[USES 20 UNITS PER NAME] Infer the likely ethnicity/diaspora of a personal name, given a country of residence ISO2 code (ex. US, CA, AU, NZ etc.)

    

    :param country_iso2: 
    :type country_iso2: str
    :param first_name: 
    :type first_name: str
    :param last_name: 
    :type last_name: str

    """
    return web.Response(status=200)


async def diaspora_batch(request: web.Request, body=None) -> web.Response:
    """[USES 20 UNITS PER NAME] Infer the likely ethnicity/diaspora of up to 100 personal names, given a country of residence ISO2 code (ex. US, CA, AU, NZ etc.)

    

    :param body: A list of personal names
    :type body: dict | bytes

    """
    body = BatchFirstLastNameGeoIn.from_dict(body)
    return web.Response(status=200)


async def gender(request: web.Request, first_name, last_name) -> web.Response:
    """Infer the likely gender of a name.

    

    :param first_name: 
    :type first_name: str
    :param last_name: 
    :type last_name: str

    """
    return web.Response(status=200)


async def gender1(request: web.Request, first_name) -> web.Response:
    """Infer the likely gender of a just a fiven name, assuming default &#39;US&#39; local context. Please use preferably full names and local geographic context for better accuracy.

    

    :param first_name: 
    :type first_name: str

    """
    return web.Response(status=200)


async def gender_batch(request: web.Request, body=None) -> web.Response:
    """Infer the likely gender of up to 100 names, detecting automatically the cultural context.

    

    :param body: A list of personal names
    :type body: dict | bytes

    """
    body = BatchFirstLastNameIn.from_dict(body)
    return web.Response(status=200)


async def gender_full(request: web.Request, full_name) -> web.Response:
    """Infer the likely gender of a full name, ex. John H. Smith

    

    :param full_name: 
    :type full_name: str

    """
    return web.Response(status=200)


async def gender_full_batch(request: web.Request, body=None) -> web.Response:
    """Infer the likely gender of up to 100 full names, detecting automatically the cultural context.

    

    :param body: A list of personal names
    :type body: dict | bytes

    """
    body = BatchPersonalNameIn.from_dict(body)
    return web.Response(status=200)


async def gender_full_geo(request: web.Request, full_name, country_iso2) -> web.Response:
    """Infer the likely gender of a full name, given a local context (ISO2 country code).

    

    :param full_name: 
    :type full_name: str
    :param country_iso2: 
    :type country_iso2: str

    """
    return web.Response(status=200)


async def gender_full_geo_batch(request: web.Request, body=None) -> web.Response:
    """Infer the likely gender of up to 100 full names, with a given cultural context (country ISO2 code).

    

    :param body: A list of personal names, with a country ISO2 code
    :type body: dict | bytes

    """
    body = BatchPersonalNameGeoIn.from_dict(body)
    return web.Response(status=200)


async def gender_geo(request: web.Request, first_name, last_name, country_iso2) -> web.Response:
    """Infer the likely gender of a name, given a local context (ISO2 country code).

    

    :param first_name: 
    :type first_name: str
    :param last_name: 
    :type last_name: str
    :param country_iso2: 
    :type country_iso2: str

    """
    return web.Response(status=200)


async def gender_geo_batch(request: web.Request, body=None) -> web.Response:
    """Infer the likely gender of up to 100 names, each given a local context (ISO2 country code).

    

    :param body: A list of names, with country code.
    :type body: dict | bytes

    """
    body = BatchFirstLastNameGeoIn.from_dict(body)
    return web.Response(status=200)


async def origin(request: web.Request, first_name, last_name) -> web.Response:
    """[USES 10 UNITS PER NAME] Infer the likely country of origin of a personal name. Assumes names as they are in the country of origin. For US, CA, AU, NZ and other melting-pots : use &#39;diaspora&#39; instead.

    

    :param first_name: 
    :type first_name: str
    :param last_name: 
    :type last_name: str

    """
    return web.Response(status=200)


async def origin_batch(request: web.Request, body=None) -> web.Response:
    """[USES 10 UNITS PER NAME] Infer the likely country of origin of up to 100 names, detecting automatically the cultural context.

    

    :param body: A list of personal names
    :type body: dict | bytes

    """
    body = BatchFirstLastNameIn.from_dict(body)
    return web.Response(status=200)


async def parse_name(request: web.Request, name_full) -> web.Response:
    """Infer the likely first/last name structure of a name, ex. John Smith or SMITH, John or SMITH; John. 

    

    :param name_full: 
    :type name_full: str

    """
    return web.Response(status=200)


async def parse_name_batch(request: web.Request, body=None) -> web.Response:
    """Infer the likely first/last name structure of a name, ex. John Smith or SMITH, John or SMITH; John.

    

    :param body: A list of personal names
    :type body: dict | bytes

    """
    body = BatchPersonalNameIn.from_dict(body)
    return web.Response(status=200)


async def parse_name_geo(request: web.Request, name_full, country_iso2) -> web.Response:
    """Infer the likely first/last name structure of a name, ex. John Smith or SMITH, John or SMITH; John. For better accuracy, provide a geographic context.

    

    :param name_full: 
    :type name_full: str
    :param country_iso2: 
    :type country_iso2: str

    """
    return web.Response(status=200)


async def parse_name_geo_batch(request: web.Request, body=None) -> web.Response:
    """Infer the likely first/last name structure of a name, ex. John Smith or SMITH, John or SMITH; John. Giving a local context improves precision. 

    

    :param body: A list of personal names
    :type body: dict | bytes

    """
    body = BatchPersonalNameGeoIn.from_dict(body)
    return web.Response(status=200)


async def religion_full(request: web.Request, country_iso2, sub_division_iso31662, personal_name_full) -> web.Response:
    """[USES 10 UNITS PER NAME] Infer the likely religion of a personal full name. NB: only for INDIA (as of current version).

    

    :param country_iso2: 
    :type country_iso2: str
    :param sub_division_iso31662: 
    :type sub_division_iso31662: str
    :param personal_name_full: 
    :type personal_name_full: str

    """
    return web.Response(status=200)


async def religion_full_batch(request: web.Request, body=None) -> web.Response:
    """[USES 10 UNITS PER NAME] Infer the likely religion of up to 100 personal full names. NB: only for India as of currently.

    

    :param body: A list of personal names
    :type body: dict | bytes

    """
    body = BatchPersonalNameGeoSubdivisionIn.from_dict(body)
    return web.Response(status=200)


async def subclassification(request: web.Request, country_iso2, first_name, last_name) -> web.Response:
    """[USES 10 UNITS PER NAME] Infer the likely origin of a name at a country subclassification level (state or regeion). Initially, this is only supported for India (ISO2 code &#39;IN&#39;).

    

    :param country_iso2: 
    :type country_iso2: str
    :param first_name: 
    :type first_name: str
    :param last_name: 
    :type last_name: str

    """
    return web.Response(status=200)


async def subclassification_batch(request: web.Request, body=None) -> web.Response:
    """[USES 10 UNITS PER NAME] Infer the likely origin of a list of up to 100 names at a country subclassification level (state or regeion). Initially, this is only supported for India (ISO2 code &#39;IN&#39;).

    

    :param body: A list of personal names
    :type body: dict | bytes

    """
    body = BatchFirstLastNameGeoIn.from_dict(body)
    return web.Response(status=200)


async def subclassification_full(request: web.Request, country_iso2, full_name) -> web.Response:
    """[USES 10 UNITS PER NAME] Infer the likely origin of a name at a country subclassification level (state or regeion). Initially, this is only supported for India (ISO2 code &#39;IN&#39;).

    

    :param country_iso2: 
    :type country_iso2: str
    :param full_name: 
    :type full_name: str

    """
    return web.Response(status=200)


async def subclassification_full_batch(request: web.Request, body=None) -> web.Response:
    """[USES 10 UNITS PER NAME] Infer the likely origin of a list of up to 100 names at a country subclassification level (state or regeion). Initially, this is only supported for India (ISO2 code &#39;IN&#39;).

    

    :param body: A list of personal names
    :type body: dict | bytes

    """
    body = BatchPersonalNameGeoIn.from_dict(body)
    return web.Response(status=200)


async def us_race_ethnicity(request: web.Request, first_name, last_name) -> web.Response:
    """[USES 10 UNITS PER NAME] Infer a US resident&#39;s likely race/ethnicity according to US Census taxonomy W_NL (white, non latino), HL (hispano latino),  A (asian, non latino), B_NL (black, non latino). Optionally add header X-OPTION-USRACEETHNICITY-TAXONOMY: USRACEETHNICITY-6CLASSES for two additional classes, AI_AN (American Indian or Alaskan Native) and PI (Pacific Islander).

    

    :param first_name: 
    :type first_name: str
    :param last_name: 
    :type last_name: str

    """
    return web.Response(status=200)


async def us_race_ethnicity_batch(request: web.Request, body=None) -> web.Response:
    """[USES 10 UNITS PER NAME] Infer up-to 100 US resident&#39;s likely race/ethnicity according to US Census taxonomy. Output is W_NL (white, non latino), HL (hispano latino),  A (asian, non latino), B_NL (black, non latino). Optionally add header X-OPTION-USRACEETHNICITY-TAXONOMY: USRACEETHNICITY-6CLASSES for two additional classes, AI_AN (American Indian or Alaskan Native) and PI (Pacific Islander).

    

    :param body: A list of personal names
    :type body: dict | bytes

    """
    body = BatchFirstLastNameGeoIn.from_dict(body)
    return web.Response(status=200)


async def us_race_ethnicity_zip5(request: web.Request, first_name, last_name, zip5_code) -> web.Response:
    """[USES 10 UNITS PER NAME] Infer a US resident&#39;s likely race/ethnicity according to US Census taxonomy, using (optional) ZIP5 code info. Output is W_NL (white, non latino), HL (hispano latino),  A (asian, non latino), B_NL (black, non latino). Optionally add header X-OPTION-USRACEETHNICITY-TAXONOMY: USRACEETHNICITY-6CLASSES for two additional classes, AI_AN (American Indian or Alaskan Native) and PI (Pacific Islander).

    

    :param first_name: 
    :type first_name: str
    :param last_name: 
    :type last_name: str
    :param zip5_code: 
    :type zip5_code: str

    """
    return web.Response(status=200)


async def us_zip_race_ethnicity_batch(request: web.Request, body=None) -> web.Response:
    """[USES 10 UNITS PER NAME] Infer up-to 100 US resident&#39;s likely race/ethnicity according to US Census taxonomy, with (optional) ZIP code. Output is W_NL (white, non latino), HL (hispano latino),  A (asian, non latino), B_NL (black, non latino). Optionally add header X-OPTION-USRACEETHNICITY-TAXONOMY: USRACEETHNICITY-6CLASSES for two additional classes, AI_AN (American Indian or Alaskan Native) and PI (Pacific Islander).

    

    :param body: A list of personal names
    :type body: dict | bytes

    """
    body = BatchFirstLastNameGeoZippedIn.from_dict(body)
    return web.Response(status=200)
