from typing import List, Dict
from aiohttp import web

from openapi_server.models.check_details_output import CheckDetailsOutput
from openapi_server.models.check_output import CheckOutput
from openapi_server.models.checks_output import ChecksOutput
from openapi_server.models.database import Database
from openapi_server.models.error import Error
from openapi_server import util


async def create_check(request: web.Request, country, type, truora_priority=None, birth_certificate=None, company_name=None, date_of_birth=None, diplomatic_id=None, driver_license=None, escrow=None, first_name=None, force_creation=None, foreign_id=None, issue_date=None, last_name=None, license_plate=None, national_id=None, native_country=None, owner_document_id=None, owner_document_type=None, passport=None, payment_date=None, pep=None, phone_number=None, professional_card=None, ptp=None, region=None, report_id=None, state_id=None, tax_id=None, user_authorized=None, vehicle_id=None, verification_code=None, watch=None) -> web.Response:
    """Create a background check

    Creates a background check and queues it to start collecting information. The full details of background checks can be retrieved with their respective Check IDs using getCheck endpoint. Keep in mind that, depending on the check type, input document, and country of a search, certain inputs are required. You should always provide as many inputs as possible in order to get the highest accuracy.  If your check type is not referenced in the following table, please reach out to find out the fields that apply for you.  | Country | Person-National | PersonForeigner | Company | Vehicle-National | Vehicle-Foreigner | |:-------:|:---------------:|:---------------:|:-------:|:----------------:|:-----------------:| | Chile&lt;br&gt;CL | national_id*&lt;br&gt;date_of_birth&lt;br&gt;phone_number | foreign_id*&lt;br&gt;date_of_birth*&lt;br&gt;phone_number&lt;br&gt;first_name*&lt;br&gt;last_name*&lt;br&gt;native_country* | N/A | national_id*&lt;br&gt;license_plate*&lt;br&gt;payment_date (Santiago only)&lt;br&gt;driver_license (Santiago only) | foreign_id*&lt;br&gt;first_name*&lt;br&gt;last_name*&lt;br&gt;date_of_birth*&lt;br&gt;native_country*&lt;br&gt;license_plate*&lt;br&gt;payment_date (Santiago only)&lt;br&gt;driver_license (Santiago only) | | Colombia&lt;br&gt;CO | national_id*&lt;br&gt;date_of_birth&lt;br&gt;issue_date&lt;br&gt;phone_number | foreign_id* or PEP*&lt;br&gt;date_of_birth&lt;br&gt;phone_number&lt;br&gt;issue_date* | tax_id*&lt;br&gt;national_id | national_id*&lt;br&gt;date_of_birth&lt;br&gt;phone_number&lt;br&gt;license_plate*&lt;br&gt;owner_document_type&lt;br&gt;owner_document_id | foreign_id*&lt;br&gt;date_of_birth&lt;br&gt;phone_number&lt;br&gt;license_plate*&lt;br&gt;issue_date* | | Mexico&lt;br&gt;MX | national_id*&lt;br&gt;phone_number | foreign_id* | tax_id* | license_plate*&lt;br&gt;national_id&lt;br&gt;vehicle_id&lt;br&gt;driver_license(Estado de Mexico only) | N/A | | Brazil&lt;br&gt;BR | national_id*&lt;br&gt;date_of_birth*&lt;br&gt;region*&lt;br&gt;phone_number | N/A | tax_id* | license_plate* | N/A | | Costa Rica&lt;br&gt;CR | national_id*&lt;br&gt;phone_number | foreign_id* | N/A | license_plate* | N/A | | Ecuador&lt;br&gt;EC | national_id*&lt;br&gt;phone_number | foreign_id* | tax_id* | license_plate* | N/A | | Peru&lt;br&gt;PE | national_id*&lt;br&gt;date_of_birth&lt;br&gt;phone_number | foreign_id*&lt;br&gt;ptp&lt;br&gt;date_of_birth*&lt;br&gt;phone_number | N/A | national_id*&lt;br&gt;date_of_birth&lt;br&gt;license_plate* | foreign_id*&lt;br&gt;ptp&lt;br&gt;date_of_birth*&lt;br&gt;license_plate* | | Argentina&lt;br&gt;AR | national_id* | N/A | N/A | national_id* | N/A | | International&lt;br&gt;ALL | name* | name* | company_name* | N/A | N/A |  (*) Required field

    :param country: Document country
    :type country: str
    :param type: Background check type
    :type type: str
    :param truora_priority: Describes the background check priority. The amount of high priority checks is limited by country. Medium priority is used by default
    :type truora_priority: str
    :param birth_certificate: Person birth certificate
    :type birth_certificate: str
    :param company_name: Company name \\\&quot;Don&#39;t forget this required field to complete background checks in Brazil\\\&quot;
    :type company_name: str
    :param date_of_birth: Person birthdate. This date is used to get some additional information about a person and to filter homonyms in some cases. YYYY-MM-DD format, Required for complete background checks in Brazil
    :type date_of_birth: str
    :param diplomatic_id: Diplomatic ID
    :type diplomatic_id: str
    :param driver_license: Driver&#39;s license number
    :type driver_license: str
    :param escrow: Colombian escrow
    :type escrow: str
    :param first_name: Person or entity first name. If the document type and number are not provided, the report might include homonyms. Required when searching by first name, Required in order to get complete background checks in Brazil
    :type first_name: str
    :param force_creation: Forces a new background check creation when true. Reuses recently created background checks otherwise
    :type force_creation: bool
    :param foreign_id: Person foreign ID
    :type foreign_id: str
    :param issue_date: Person document issue date in \\\&quot;YYYY-mm-dd\\\&quot; format (e.g. 2008-12-31) . This date is used to get some additional information about a person in some cases
    :type issue_date: str
    :param last_name: Person or entity last name. If the document type and number are not provided, the report might include homonyms. Required when searching by last name. Required in order to get complete background checks in Brazil
    :type last_name: str
    :param license_plate: Vehicle license plate
    :type license_plate: str
    :param national_id: National ID
    :type national_id: str
    :param native_country: Country of birth
    :type native_country: str
    :param owner_document_id: National ID of the vehicle owner
    :type owner_document_id: str
    :param owner_document_type: National ID, foreign ID, or tax ID
    :type owner_document_type: str
    :param passport: Person passport
    :type passport: str
    :param payment_date: Payment day of a vehicle circulation permit (Chile only)
    :type payment_date: str
    :param pep: ID for Venezuelans working in Colombia
    :type pep: str
    :param phone_number: Person phone number. Required by law to notify the person their background is being checked
    :type phone_number: str
    :param professional_card: Professional ID card
    :type professional_card: str
    :param ptp: ID for Venezuelans working in Peru
    :type ptp: str
    :param region: Region where the background is to be checked in addition to the region where the person is from. By default, background checks in Brazil are performed in the region where the person is from. Required for Brazil only. Allowed values are: DF: Distrito Federal, AC: Acre, AL: Alagoas, AP: Amapá, AM: Amazonas, BA: Bahía, CE: Ceará, ES: Espírito Santo, GO: Goiás, MA: Maranhão, MT: Mato Grosso, MS: Mato Grosso do Sul, MG: Minas Gerais, PA: Pará, PB: Paraíba, PR: Paraná, PE: Pernambuco, PI: Piauí, RJ: Río de Janeiro, RN: Río Grande do Norte, RS: Río Grande do Sul, RO: Rondônia, RR: Roraima, SC: Santa Catarina, SP: São Paulo, SE: Sergipe, TO : Tocantins.
    :type region: str
    :param report_id: Report ID the background check will be inserted into
    :type report_id: str
    :param state_id:  Used for the RG (Registro Geral) identification in Brazil. This identification has different formats according to the state that issues the document. It can have numbers and letters but other characters (- * , . ) are omitted, Required in order to get complete background checks in Brazil
    :type state_id: str
    :param tax_id: Company ID used for tax payments
    :type tax_id: str
    :param user_authorized: Indicates whether the person subject to the validation authorized the validation. Must be true in order to proceed [Required for API key V1 or later]
    :type user_authorized: bool
    :param vehicle_id: Vehicle license plate
    :type vehicle_id: str
    :param verification_code: Verification code registered for criminal records in Peru only
    :type verification_code: str
    :param watch: Indicates whether the check score is to be periodically revised and its frequency. It can be daily, weekly, monthly, yearly or have a custom frequency written as a number accompanied by d: day, w: week, m: month, y: year for instance: 3d: every three days, 2w: every two weeks. Ignore this field if the check is only to be performed once
    :type watch: str

    """
    date_of_birth = util.deserialize_date(date_of_birth)
    issue_date = util.deserialize_date(issue_date)
    payment_date = util.deserialize_date(payment_date)
    return web.Response(status=200)


async def get_check(request: web.Request, check_id) -> web.Response:
    """Get Background Check

    Returns the results of the check that matches the ID provided, complete with a set of scores explained below.  ### Scores:   - **Global Score**: Average risk associated with a person, company or vehicle, according to  the background check results. The global score considers results that are validated with the  ID number provided. The score ranges from 0 to 1, where 0 represents high risk and 1 low risk.   - **ID Score**: Average risk associated with a person according to the background check  results. The ID score considers the results that are validated with a person identity  document. The score ranges from 0 to 1, where 0 represents high risk and 1 low risk.    - **Homonym Score**: Average risk associated with a person according to the background check  results. The homonym score considers results that are validated against the name of a person and could not be validated with their ID number. These results might have homonyms associated with them. The score ranges from 0 to 1, where 0 represents high risk and 1 low risk.   In order to calculate these scores, a weighted average is considered with different weights allocated to each dataset. Scores can be customized using the config endpoints by assigning a weight to each dataset according to its relevance.  Keep in mind that results from the API vary depending on the country, check type and the inputs entered on check creation.

    :param check_id: Check ID
    :type check_id: str

    """
    return web.Response(status=200)


async def get_health_dashboard(request: web.Request, country=None, unix_timestamp_seconds=None, unixtimezone_offset_seconds=None) -> web.Response:
    """Get Health Dashboard

    Get the status of a database

    :param country: Country in ISO 3166, uppercase
    :type country: str
    :param unix_timestamp_seconds: Unix timestamp in seconds. Send a day timestamp to view the database hourly status for that day or send the current time to know the current database status
    :type unix_timestamp_seconds: str
    :param unixtimezone_offset_seconds: Offset between the local time and the UTC time in seconds. (e.g., Colombia is at UTC -18000 seconds)  
    :type unixtimezone_offset_seconds: str

    """
    return web.Response(status=200)


async def list_check_details(request: web.Request, check_id, start_key=None, lang=None) -> web.Response:
    """List Check Details

    Lists all details associated with a Check. It can be paginated.

    :param check_id: ID of the Check
    :type check_id: str
    :param start_key: Start key value for the pagination
    :type start_key: str
    :param lang: This parameter is used to specify the language wanted for details, if not specified details will come in their original language.
    :type lang: str

    """
    return web.Response(status=200)


async def list_checks(request: web.Request, start_key=None, report_id=None) -> web.Response:
    """List Checks

    Lists the existing checks in the account or in a specified report.

    :param start_key: Start key value for the pagination
    :type start_key: str
    :param report_id: Report id checks to be returned
    :type report_id: str

    """
    return web.Response(status=200)
