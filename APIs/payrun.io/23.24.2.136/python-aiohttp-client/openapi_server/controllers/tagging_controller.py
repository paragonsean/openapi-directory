from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_model import ErrorModel
from openapi_server.models.link_collection import LinkCollection
from openapi_server.models.tag import Tag
from openapi_server import util


async def delete_cis_instruction_tag(request: web.Request, employer_id, sub_contractor_id, cis_instruction_id, tag_id, authorization, api_version) -> web.Response:
    """Delete CIS instruction tag

    Deletes a tag from the CIS instruction

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param sub_contractor_id: The sub contractors&#39; unique identifier. E.g SUB001
    :type sub_contractor_id: str
    :param cis_instruction_id: The CIS instruction unique identifier. E.g. CIS001
    :type cis_instruction_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def delete_cis_line_tag(request: web.Request, employer_id, sub_contractor_id, cis_line_id, tag_id, authorization, api_version) -> web.Response:
    """Delete CIS line tag

    Deletes a tag from the CIS line

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param sub_contractor_id: The sub contractors&#39; unique identifier. E.g SUB001
    :type sub_contractor_id: str
    :param cis_line_id: The CIS line unique identifier. E.g. CISLN001
    :type cis_line_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def delete_cis_line_type_tag(request: web.Request, employer_id, cis_line_type_id, tag_id, authorization, api_version) -> web.Response:
    """Delete CIS line type tag

    Deletes a tag from the CIS line type

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param cis_line_type_id: The CIS line type unique identifier. E.g. TYPEA
    :type cis_line_type_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def delete_employee_tag(request: web.Request, employer_id, employee_id, tag_id, authorization, api_version) -> web.Response:
    """Delete employee tag

    Deletes a tag from the employee

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param employee_id: The employees&#39; unique identifier. E.g EE001
    :type employee_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def delete_employer_tag(request: web.Request, employer_id, tag_id, authorization, api_version) -> web.Response:
    """Delete employer tag

    Deletes a tag from the employer

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def delete_holiday_scheme_tag(request: web.Request, employer_id, holiday_scheme_id, tag_id, authorization, api_version) -> web.Response:
    """Delete holiday scheme tag

    Deletes a tag from the holiday scheme

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param holiday_scheme_id: The holiday schemes&#39; unique identifier. E.g HOLSCH001
    :type holiday_scheme_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def delete_journal_line_tag(request: web.Request, employer_id, journal_line_id, tag_id, authorization, api_version) -> web.Response:
    """Delete journal line tag

    Deletes a tag from the journal line

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param journal_line_id: The journal line unique identifier. E.g JL001
    :type journal_line_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def delete_pay_code_tag(request: web.Request, employer_id, pay_code_id, tag_id, authorization, api_version) -> web.Response:
    """Delete pay code tag

    Deletes a tag from the pay code

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param pay_code_id: The pay code unique identifier. E.g. BASIC
    :type pay_code_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def delete_pay_instruction_tag(request: web.Request, employer_id, employee_id, pay_instruction_id, tag_id, authorization, api_version) -> web.Response:
    """Delete pay instruction tag

    Deletes a tag from the pay instruction

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param employee_id: The employees&#39; unique identifier. E.g EE001
    :type employee_id: str
    :param pay_instruction_id: The pay instruction unique identifier. E.g. SAL001
    :type pay_instruction_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def delete_pay_line_tag(request: web.Request, employer_id, employee_id, pay_line_id, tag_id, authorization, api_version) -> web.Response:
    """Delete pay line tag

    Deletes a tag from the pay line

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param employee_id: The employees&#39; unique identifier. E.g EE001
    :type employee_id: str
    :param pay_line_id: The pay line unique identifier. E.g. PL001
    :type pay_line_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def delete_pay_run_tag(request: web.Request, employer_id, pay_schedule_id, pay_run_id, tag_id, authorization, api_version) -> web.Response:
    """Delete pay run tag

    Deletes a tag from the pay run

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param pay_schedule_id: The pay schedules&#39; unique identifier. E.g SCH001
    :type pay_schedule_id: str
    :param pay_run_id: The pay runs&#39; unique identifier. E.g. PR001
    :type pay_run_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def delete_pay_schedule_tag(request: web.Request, employer_id, pay_schedule_id, tag_id, authorization, api_version) -> web.Response:
    """Delete pay schedule tag

    Deletes a tag from the pay schedule

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param pay_schedule_id: The pay schedules&#39; unique identifier. E.g SCH001
    :type pay_schedule_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def delete_permission_tag(request: web.Request, permission_id, tag_id, authorization, api_version) -> web.Response:
    """Delete Permission tag

    Deletes a tag from the Permission

    :param permission_id: The permission unique identifier. E.g PERM001
    :type permission_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def delete_rti_transaction_tag(request: web.Request, employer_id, rti_transaction_id, tag_id, authorization, api_version) -> web.Response:
    """Delete RTI transaction tag

    Deletes a tag from the RTI transaction

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param rti_transaction_id: The RTI transaction unique identifier. E.g. FPS001
    :type rti_transaction_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def delete_sub_contractor_tag(request: web.Request, employer_id, sub_contractor_id, tag_id, authorization, api_version) -> web.Response:
    """Delete sub contractor tag

    Deletes a tag from the sub contractor

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param sub_contractor_id: The sub contractors&#39; unique identifier. E.g SUB001
    :type sub_contractor_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def delete_third_party_transaction_tag(request: web.Request, employer_id, third_party_transaction_id, tag_id, authorization, api_version) -> web.Response:
    """Delete third party transaction tag

    Deletes a tag from the third party transaction

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param third_party_transaction_id: The third party transaction unique identifier. E.g TP001
    :type third_party_transaction_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def delete_user_tag(request: web.Request, user_id, tag_id, authorization, api_version) -> web.Response:
    """Delete user tag

    Deletes a tag from the user

    :param user_id: The user unique identifier. E.g USER001
    :type user_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_all_cis_instruction_tags(request: web.Request, employer_id, sub_contractor_id, authorization, api_version) -> web.Response:
    """Get all CIS instruction tags

    Gets all the CIS instruction tags

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param sub_contractor_id: The sub contractors&#39; unique identifier. E.g SUB001
    :type sub_contractor_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_all_cis_line_tags(request: web.Request, employer_id, sub_contractor_id, authorization, api_version) -> web.Response:
    """Get all CIS line tags

    Gets all the CIS line tags

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param sub_contractor_id: The sub contractors&#39; unique identifier. E.g SUB001
    :type sub_contractor_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_all_cis_line_type_tags(request: web.Request, employer_id, authorization, api_version) -> web.Response:
    """Get all CIS line type tags

    Gets all the CIS line type tags

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_all_employee_tags(request: web.Request, employer_id, authorization, api_version) -> web.Response:
    """Get all employee tags

    Gets all the employee tags

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_all_employer_tags(request: web.Request, authorization, api_version) -> web.Response:
    """Get all employer tags

    Gets all the employer tags

    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_all_holiday_scheme_tags(request: web.Request, employer_id, authorization, api_version) -> web.Response:
    """Get all holiday scheme tags

    Gets all the holiday scheme tags

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_all_journal_line_tags(request: web.Request, employer_id, authorization, api_version) -> web.Response:
    """Get all journal line tags

    Gets all the journal line tags

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_all_journal_lines_with_tag(request: web.Request, employer_id, tag_id, authorization, api_version) -> web.Response:
    """Get links to tagged journal lines

    Gets the journal lines with the specified tag

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_all_pay_code_tags(request: web.Request, employer_id, authorization, api_version) -> web.Response:
    """Get all pay code tags

    Gets all the pay code tags

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_all_pay_instruction_tags(request: web.Request, employer_id, employee_id, authorization, api_version) -> web.Response:
    """Get all pay instruction tags

    Gets all the pay instruction tags

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param employee_id: The employees&#39; unique identifier. E.g EE001
    :type employee_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_all_pay_line_tags(request: web.Request, employer_id, employee_id, authorization, api_version) -> web.Response:
    """Get all pay line tags

    Gets all the pay line tags

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param employee_id: The employees&#39; unique identifier. E.g EE001
    :type employee_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_all_pay_run_tags(request: web.Request, employer_id, pay_schedule_id, authorization, api_version) -> web.Response:
    """Get all pay run tags

    Gets all the pay run tags

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param pay_schedule_id: The pay schedules&#39; unique identifier. E.g SCH001
    :type pay_schedule_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_all_pay_schedule_tags(request: web.Request, employer_id, authorization, api_version) -> web.Response:
    """Get all pay schedule tags

    Gets all the pay schedule tags

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_all_permission_tags(request: web.Request, authorization, api_version) -> web.Response:
    """Get all Permission tags

    Get all tags from all Permissions

    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_all_permissions_with_tag(request: web.Request, tag_id, authorization, api_version) -> web.Response:
    """Get links to tagged Permissions

    Gets the Permissions with the specified tag

    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_all_rti_transaction_tags(request: web.Request, employer_id, authorization, api_version) -> web.Response:
    """Get all RTI transaction tags

    Gets all the RTI transaction tags

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_all_sub_contractor_tags(request: web.Request, employer_id, authorization, api_version) -> web.Response:
    """Get all sub contractor tags

    Gets all the sub contractor tags

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_all_third_party_transaction_tags(request: web.Request, employer_id, authorization, api_version) -> web.Response:
    """Get all third party transaction tags

    Gets all the third party transaction tags

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_all_third_party_transactions_with_tag(request: web.Request, employer_id, tag_id, authorization, api_version) -> web.Response:
    """Get links to tagged third party transactions

    Gets the third party transactions with the specified tag

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_all_user_tags(request: web.Request, authorization, api_version) -> web.Response:
    """Get all user tags

    Get all tags from all users

    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_all_users_with_tag(request: web.Request, tag_id, authorization, api_version) -> web.Response:
    """Get links to tagged users

    Gets the users with the specified tag

    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_cis_instructions_with_tag(request: web.Request, employer_id, sub_contractor_id, tag_id, authorization, api_version) -> web.Response:
    """Get CIS instructions with tag

    Gets the CIS instruction with the tag

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param sub_contractor_id: The sub contractors&#39; unique identifier. E.g SUB001
    :type sub_contractor_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_cis_line_types_with_tag(request: web.Request, employer_id, tag_id, authorization, api_version) -> web.Response:
    """Get CIS line types with tag

    Gets the CIS line type with the tag

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_cis_lines_with_tag(request: web.Request, employer_id, sub_contractor_id, tag_id, authorization, api_version) -> web.Response:
    """Get CIS lines with tag

    Gets the CIS line with the tag

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param sub_contractor_id: The sub contractors&#39; unique identifier. E.g SUB001
    :type sub_contractor_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_employees_with_tag(request: web.Request, employer_id, tag_id, authorization, api_version) -> web.Response:
    """Get employees with tag

    Gets the employees with the tag

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_employers_with_tag(request: web.Request, tag_id, authorization, api_version) -> web.Response:
    """Get employers with tag

    Gets the employers with the tag

    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_holiday_schemes_with_tag(request: web.Request, employer_id, tag_id, authorization, api_version) -> web.Response:
    """Get holiday schemes with tag

    Gets the holiday scheme with the tag

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_pay_codes_with_tag(request: web.Request, employer_id, tag_id, authorization, api_version) -> web.Response:
    """Get pay codes with tag

    Gets the pay codes with the tag

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_pay_instructions_with_tag(request: web.Request, employer_id, employee_id, tag_id, authorization, api_version) -> web.Response:
    """Get pay instructions with tag

    Gets the pay instructions with the tag

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param employee_id: The employees&#39; unique identifier. E.g EE001
    :type employee_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_pay_lines_with_tag(request: web.Request, employer_id, employee_id, tag_id, authorization, api_version) -> web.Response:
    """Get pay lines with tag

    Gets the pay line with the tag

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param employee_id: The employees&#39; unique identifier. E.g EE001
    :type employee_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_pay_runs_with_tag(request: web.Request, employer_id, pay_schedule_id, tag_id, authorization, api_version) -> web.Response:
    """Get pay runs with tag

    Gets the pay runs with the tag

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param pay_schedule_id: The pay schedules&#39; unique identifier. E.g SCH001
    :type pay_schedule_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_pay_schedules_with_tag(request: web.Request, employer_id, tag_id, authorization, api_version) -> web.Response:
    """Get pay schedule with tag

    Gets the pay schedules with the tag

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_rti_transactions_with_tag(request: web.Request, employer_id, tag_id, authorization, api_version) -> web.Response:
    """Get RTI transactions with tag

    Gets the RTI transactions with the tag

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_sub_contractors_with_tag(request: web.Request, employer_id, tag_id, authorization, api_version) -> web.Response:
    """Get sub contractors with tag

    Gets the sub contractor with the tag

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_tag_from_cis_instruction(request: web.Request, employer_id, sub_contractor_id, cis_instruction_id, tag_id, authorization, api_version) -> web.Response:
    """Get CIS instruction tag

    Gets the tag from the CIS instruction

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param sub_contractor_id: The sub contractors&#39; unique identifier. E.g SUB001
    :type sub_contractor_id: str
    :param cis_instruction_id: The CIS instruction unique identifier. E.g. CIS001
    :type cis_instruction_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_tag_from_cis_line(request: web.Request, employer_id, sub_contractor_id, cis_line_id, tag_id, authorization, api_version) -> web.Response:
    """Get CIS line tag

    Gets the tag from the CIS line

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param sub_contractor_id: The sub contractors&#39; unique identifier. E.g SUB001
    :type sub_contractor_id: str
    :param cis_line_id: The CIS line unique identifier. E.g. CISLN001
    :type cis_line_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_tag_from_cis_line_type(request: web.Request, employer_id, cis_line_type_id, tag_id, authorization, api_version) -> web.Response:
    """Get CIS line type tag

    Gets the tag from the CIS line type

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param cis_line_type_id: The CIS line type unique identifier. E.g. TYPEA
    :type cis_line_type_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_tag_from_employee(request: web.Request, employer_id, employee_id, tag_id, authorization, api_version) -> web.Response:
    """Get employee tag

    Gets the tag from the employee

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param employee_id: The employees&#39; unique identifier. E.g EE001
    :type employee_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_tag_from_employee_revision(request: web.Request, employer_id, employee_id, tag_id, effective_date, authorization, api_version) -> web.Response:
    """Get employee revision tag

    Gets the tag from the employee revision

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param employee_id: The employees&#39; unique identifier. E.g EE001
    :type employee_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param effective_date: The effective date to be applied. E.g 2016-04-06
    :type effective_date: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    effective_date = util.deserialize_date(effective_date)
    return web.Response(status=200)


async def get_tag_from_employer(request: web.Request, employer_id, tag_id, authorization, api_version) -> web.Response:
    """Get employer tag

    Gets the tag from the employer

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_tag_from_employer_revision(request: web.Request, employer_id, tag_id, effective_date, authorization, api_version) -> web.Response:
    """Get employer revision tag

    Gets the tag from the employer revision

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param effective_date: The effective date to be applied. E.g 2016-04-06
    :type effective_date: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    effective_date = util.deserialize_date(effective_date)
    return web.Response(status=200)


async def get_tag_from_holiday_scheme(request: web.Request, employer_id, holiday_scheme_id, tag_id, authorization, api_version) -> web.Response:
    """Get holiday scheme tag

    Gets the tag from the holiday scheme

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param holiday_scheme_id: The holiday schemes&#39; unique identifier. E.g HOLSCH001
    :type holiday_scheme_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_tag_from_holiday_scheme_revision(request: web.Request, employer_id, holiday_scheme_id, tag_id, effective_date, authorization, api_version) -> web.Response:
    """Get holiday scheme revision tag

    Gets the tag from the holiday scheme revision

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param holiday_scheme_id: The holiday schemes&#39; unique identifier. E.g HOLSCH001
    :type holiday_scheme_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param effective_date: The effective date to be applied. E.g 2016-04-06
    :type effective_date: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    effective_date = util.deserialize_date(effective_date)
    return web.Response(status=200)


async def get_tag_from_journal_line(request: web.Request, employer_id, journal_line_id, tag_id, authorization, api_version) -> web.Response:
    """Get journal line tag

    Gets a tag from the journal line

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param journal_line_id: The journal line unique identifier. E.g JL001
    :type journal_line_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_tag_from_pay_code(request: web.Request, employer_id, pay_code_id, tag_id, authorization, api_version) -> web.Response:
    """Get pay code tag

    Gets the tag from the pay code

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param pay_code_id: The pay code unique identifier. E.g. BASIC
    :type pay_code_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_tag_from_pay_instruction(request: web.Request, employer_id, employee_id, pay_instruction_id, tag_id, authorization, api_version) -> web.Response:
    """Get pay instruction tag

    Gets the tag from the pay instruction

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param employee_id: The employees&#39; unique identifier. E.g EE001
    :type employee_id: str
    :param pay_instruction_id: The pay instruction unique identifier. E.g. SAL001
    :type pay_instruction_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_tag_from_pay_line(request: web.Request, employer_id, employee_id, pay_line_id, tag_id, authorization, api_version) -> web.Response:
    """Get pay line tag

    Gets the tag from the pay line

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param employee_id: The employees&#39; unique identifier. E.g EE001
    :type employee_id: str
    :param pay_line_id: The pay line unique identifier. E.g. PL001
    :type pay_line_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_tag_from_pay_run(request: web.Request, employer_id, pay_schedule_id, pay_run_id, tag_id, authorization, api_version) -> web.Response:
    """Get pay run tag

    Gets the tag from the pay run

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param pay_schedule_id: The pay schedules&#39; unique identifier. E.g SCH001
    :type pay_schedule_id: str
    :param pay_run_id: The pay runs&#39; unique identifier. E.g. PR001
    :type pay_run_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_tag_from_pay_schedule(request: web.Request, employer_id, pay_schedule_id, tag_id, authorization, api_version) -> web.Response:
    """Get pay schedule tag

    Gets the tag from the pay schedule

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param pay_schedule_id: The pay schedules&#39; unique identifier. E.g SCH001
    :type pay_schedule_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_tag_from_permission(request: web.Request, permission_id, tag_id, authorization, api_version) -> web.Response:
    """Get Permission tag

    Gets a tag from the Permission

    :param permission_id: The permission unique identifier. E.g PERM001
    :type permission_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_tag_from_rti_transaction(request: web.Request, employer_id, rti_transaction_id, tag_id, authorization, api_version) -> web.Response:
    """Get RTI transaction tag

    Gets the tag from the RTI transaction

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param rti_transaction_id: The RTI transaction unique identifier. E.g. FPS001
    :type rti_transaction_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_tag_from_sub_contractor(request: web.Request, employer_id, sub_contractor_id, tag_id, authorization, api_version) -> web.Response:
    """Get sub contractor tag

    Gets the tag from the sub contractor

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param sub_contractor_id: The sub contractors&#39; unique identifier. E.g SUB001
    :type sub_contractor_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_tag_from_sub_contractor_revision(request: web.Request, employer_id, sub_contractor_id, tag_id, effective_date, authorization, api_version) -> web.Response:
    """Get sub contractor revision tag

    Gets the tag from the sub contractor revision

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param sub_contractor_id: The sub contractors&#39; unique identifier. E.g SUB001
    :type sub_contractor_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param effective_date: The effective date to be applied. E.g 2016-04-06
    :type effective_date: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    effective_date = util.deserialize_date(effective_date)
    return web.Response(status=200)


async def get_tag_from_third_party_transaction(request: web.Request, employer_id, third_party_transaction_id, tag_id, authorization, api_version) -> web.Response:
    """Get third party transaction tag

    Gets a tag from the third party transaction

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param third_party_transaction_id: The third party transaction unique identifier. E.g TP001
    :type third_party_transaction_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_tag_from_user(request: web.Request, user_id, tag_id, authorization, api_version) -> web.Response:
    """Get user tag

    Gets a tag from the user

    :param user_id: The user unique identifier. E.g USER001
    :type user_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_tags_from_cis_instruction(request: web.Request, employer_id, sub_contractor_id, cis_instruction_id, authorization, api_version) -> web.Response:
    """Get all tags from the CIS instruction

    Gets all the tags from the CIS instruction

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param sub_contractor_id: The sub contractors&#39; unique identifier. E.g SUB001
    :type sub_contractor_id: str
    :param cis_instruction_id: The CIS instruction unique identifier. E.g. CIS001
    :type cis_instruction_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_tags_from_cis_line(request: web.Request, employer_id, sub_contractor_id, cis_line_id, authorization, api_version) -> web.Response:
    """Get all tags from the CIS line

    Gets all the tags from the CIS line

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param sub_contractor_id: The sub contractors&#39; unique identifier. E.g SUB001
    :type sub_contractor_id: str
    :param cis_line_id: The CIS line unique identifier. E.g. CISLN001
    :type cis_line_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_tags_from_cis_line_type(request: web.Request, employer_id, cis_line_type_id, authorization, api_version) -> web.Response:
    """Get all tags from the CIS line type

    Gets all the tags from the CIS line type

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param cis_line_type_id: The CIS line type unique identifier. E.g. TYPEA
    :type cis_line_type_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_tags_from_employee(request: web.Request, employer_id, employee_id, authorization, api_version) -> web.Response:
    """Get all employee tags

    Gets all the tags from the employee

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param employee_id: The employees&#39; unique identifier. E.g EE001
    :type employee_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_tags_from_employee_revision(request: web.Request, employer_id, employee_id, effective_date, authorization, api_version) -> web.Response:
    """Get all employee revision tags

    Gets all the tags from the employee revision

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param employee_id: The employees&#39; unique identifier. E.g EE001
    :type employee_id: str
    :param effective_date: The effective date to be applied. E.g 2016-04-06
    :type effective_date: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    effective_date = util.deserialize_date(effective_date)
    return web.Response(status=200)


async def get_tags_from_employer(request: web.Request, employer_id, authorization, api_version) -> web.Response:
    """Get all employer tags

    Gets all the tags from the employer

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_tags_from_employer_revision(request: web.Request, employer_id, effective_date, authorization, api_version) -> web.Response:
    """Get all employer revision tags

    Gets all the tags from the employer revision

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param effective_date: The effective date to be applied. E.g 2016-04-06
    :type effective_date: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    effective_date = util.deserialize_date(effective_date)
    return web.Response(status=200)


async def get_tags_from_holiday_scheme(request: web.Request, employer_id, holiday_scheme_id, authorization, api_version) -> web.Response:
    """Get all tags from the holiday scheme

    Gets all the tags from the holiday scheme

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param holiday_scheme_id: The holiday schemes&#39; unique identifier. E.g HOLSCH001
    :type holiday_scheme_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_tags_from_holiday_scheme_revision(request: web.Request, employer_id, holiday_scheme_id, effective_date, authorization, api_version) -> web.Response:
    """Get all holiday scheme revision tags

    Gets all the tags from the holiday scheme revision

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param holiday_scheme_id: The holiday schemes&#39; unique identifier. E.g HOLSCH001
    :type holiday_scheme_id: str
    :param effective_date: The effective date to be applied. E.g 2016-04-06
    :type effective_date: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    effective_date = util.deserialize_date(effective_date)
    return web.Response(status=200)


async def get_tags_from_journal_line(request: web.Request, employer_id, journal_line_id, authorization, api_version) -> web.Response:
    """Get tags from journal line

    Gets all tags from the journal line

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param journal_line_id: The journal line unique identifier. E.g JL001
    :type journal_line_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_tags_from_pay_code(request: web.Request, employer_id, pay_code_id, authorization, api_version) -> web.Response:
    """Get all pay code tags

    Gets all the tags from the pay code

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param pay_code_id: The pay code unique identifier. E.g. BASIC
    :type pay_code_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_tags_from_pay_instruction(request: web.Request, employer_id, employee_id, pay_instruction_id, authorization, api_version) -> web.Response:
    """Get all tags from the pay instruction

    Gets all the tags from the pay instruction

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param employee_id: The employees&#39; unique identifier. E.g EE001
    :type employee_id: str
    :param pay_instruction_id: The pay instruction unique identifier. E.g. SAL001
    :type pay_instruction_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_tags_from_pay_line(request: web.Request, employer_id, employee_id, pay_line_id, authorization, api_version) -> web.Response:
    """Get all tags from the pay line

    Gets all the tags from the pay line

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param employee_id: The employees&#39; unique identifier. E.g EE001
    :type employee_id: str
    :param pay_line_id: The pay line unique identifier. E.g. PL001
    :type pay_line_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_tags_from_pay_run(request: web.Request, employer_id, pay_schedule_id, pay_run_id, authorization, api_version) -> web.Response:
    """Get all pay run tags

    Gets all the tags from the pay run

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param pay_schedule_id: The pay schedules&#39; unique identifier. E.g SCH001
    :type pay_schedule_id: str
    :param pay_run_id: The pay runs&#39; unique identifier. E.g. PR001
    :type pay_run_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_tags_from_pay_schedule(request: web.Request, employer_id, pay_schedule_id, authorization, api_version) -> web.Response:
    """Get all pay schedule tags

    Gets all the tags from the pay schedule

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param pay_schedule_id: The pay schedules&#39; unique identifier. E.g SCH001
    :type pay_schedule_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_tags_from_permission(request: web.Request, permission_id, authorization, api_version) -> web.Response:
    """Get tags from Permission

    Gets all tags from the Permission

    :param permission_id: The permission unique identifier. E.g PERM001
    :type permission_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_tags_from_rti_transaction(request: web.Request, employer_id, rti_transaction_id, authorization, api_version) -> web.Response:
    """Get all tags from RTI transaction

    Gets all the tags from the RTI transaction

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param rti_transaction_id: The RTI transaction unique identifier. E.g. FPS001
    :type rti_transaction_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_tags_from_sub_contractor(request: web.Request, employer_id, sub_contractor_id, authorization, api_version) -> web.Response:
    """Get all tags from the sub contractor

    Gets all the tags from the sub contractor

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param sub_contractor_id: The sub contractors&#39; unique identifier. E.g SUB001
    :type sub_contractor_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_tags_from_sub_contractor_revision(request: web.Request, employer_id, sub_contractor_id, effective_date, authorization, api_version) -> web.Response:
    """Get all sub contractor revision tags

    Gets all the tags from the sub contractor revision

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param sub_contractor_id: The sub contractors&#39; unique identifier. E.g SUB001
    :type sub_contractor_id: str
    :param effective_date: The effective date to be applied. E.g 2016-04-06
    :type effective_date: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    effective_date = util.deserialize_date(effective_date)
    return web.Response(status=200)


async def get_tags_from_third_party_transaction(request: web.Request, employer_id, third_party_transaction_id, authorization, api_version) -> web.Response:
    """Get tags from third party transaction

    Gets all tags from the third party transaction

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param third_party_transaction_id: The third party transaction unique identifier. E.g TP001
    :type third_party_transaction_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_tags_from_user(request: web.Request, user_id, authorization, api_version) -> web.Response:
    """Get tags from user

    Gets all tags from the user

    :param user_id: The user unique identifier. E.g USER001
    :type user_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def put_cis_instruction_tag(request: web.Request, employer_id, sub_contractor_id, cis_instruction_id, tag_id, authorization, api_version) -> web.Response:
    """Insert CIS instruction tag

    Inserts a new tag on the CIS instruction

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param sub_contractor_id: The sub contractors&#39; unique identifier. E.g SUB001
    :type sub_contractor_id: str
    :param cis_instruction_id: The CIS instruction unique identifier. E.g. CIS001
    :type cis_instruction_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def put_cis_line_tag(request: web.Request, employer_id, sub_contractor_id, cis_line_id, tag_id, authorization, api_version) -> web.Response:
    """Insert CIS line tag

    Inserts a new tag on the CIS line

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param sub_contractor_id: The sub contractors&#39; unique identifier. E.g SUB001
    :type sub_contractor_id: str
    :param cis_line_id: The CIS line unique identifier. E.g. CISLN001
    :type cis_line_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def put_cis_line_type_tag(request: web.Request, employer_id, cis_line_type_id, tag_id, authorization, api_version) -> web.Response:
    """Insert CIS line type tag

    Inserts a new tag on the CIS line type

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param cis_line_type_id: The CIS line type unique identifier. E.g. TYPEA
    :type cis_line_type_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def put_employee_tag(request: web.Request, employer_id, employee_id, tag_id, authorization, api_version) -> web.Response:
    """Insert employee tag

    Inserts a new tag on the employee

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param employee_id: The employees&#39; unique identifier. E.g EE001
    :type employee_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def put_employer_tag(request: web.Request, employer_id, tag_id, authorization, api_version) -> web.Response:
    """Insert employer tag

    Inserts a new tag on the employer

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def put_holiday_scheme_tag(request: web.Request, employer_id, holiday_scheme_id, tag_id, authorization, api_version) -> web.Response:
    """Insert holiday scheme tag

    Inserts a new tag on the holiday scheme

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param holiday_scheme_id: The holiday schemes&#39; unique identifier. E.g HOLSCH001
    :type holiday_scheme_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def put_journal_line_tag(request: web.Request, employer_id, journal_line_id, tag_id, authorization, api_version) -> web.Response:
    """Insert journal line tag

    Inserts a tag on the journal line

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param journal_line_id: The journal line unique identifier. E.g JL001
    :type journal_line_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def put_pay_code_tag(request: web.Request, employer_id, pay_code_id, tag_id, authorization, api_version) -> web.Response:
    """Insert pay code tag

    Inserts a new tag on the pay code

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param pay_code_id: The pay code unique identifier. E.g. BASIC
    :type pay_code_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def put_pay_instruction_tag(request: web.Request, employer_id, employee_id, pay_instruction_id, tag_id, authorization, api_version) -> web.Response:
    """Insert pay instruction tag

    Inserts a new tag on the pay instruction

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param employee_id: The employees&#39; unique identifier. E.g EE001
    :type employee_id: str
    :param pay_instruction_id: The pay instruction unique identifier. E.g. SAL001
    :type pay_instruction_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def put_pay_line_tag(request: web.Request, employer_id, employee_id, pay_line_id, tag_id, authorization, api_version) -> web.Response:
    """Insert pay line tag

    Inserts a new tag on the pay line

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param employee_id: The employees&#39; unique identifier. E.g EE001
    :type employee_id: str
    :param pay_line_id: The pay line unique identifier. E.g. PL001
    :type pay_line_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def put_pay_run_tag(request: web.Request, employer_id, pay_schedule_id, pay_run_id, tag_id, authorization, api_version) -> web.Response:
    """Insert pay run tag

    Inserts a new tag on the pay run

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param pay_schedule_id: The pay schedules&#39; unique identifier. E.g SCH001
    :type pay_schedule_id: str
    :param pay_run_id: The pay runs&#39; unique identifier. E.g. PR001
    :type pay_run_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def put_pay_schedule_tag(request: web.Request, employer_id, pay_schedule_id, tag_id, authorization, api_version) -> web.Response:
    """Insert pay schedule tag

    Inserts a new tag on the pay schedule

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param pay_schedule_id: The pay schedules&#39; unique identifier. E.g SCH001
    :type pay_schedule_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def put_permission_tag(request: web.Request, permission_id, tag_id, authorization, api_version) -> web.Response:
    """Insert Permission tag

    Inserts a tag on the Permission

    :param permission_id: The permission unique identifier. E.g PERM001
    :type permission_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def put_rti_transaction_tag(request: web.Request, employer_id, rti_transaction_id, tag_id, authorization, api_version) -> web.Response:
    """Insert RTI transaction tag

    Inserts a new tag on the RTI transaction

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param rti_transaction_id: The RTI transaction unique identifier. E.g. FPS001
    :type rti_transaction_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def put_sub_contractor_tag(request: web.Request, employer_id, sub_contractor_id, tag_id, authorization, api_version) -> web.Response:
    """Insert sub contractor tag

    Inserts a new tag on the sub contractor

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param sub_contractor_id: The sub contractors&#39; unique identifier. E.g SUB001
    :type sub_contractor_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def put_third_party_transaction_tag(request: web.Request, employer_id, third_party_transaction_id, tag_id, authorization, api_version) -> web.Response:
    """insert third party transaction tag

    Inserts a tag on the third party transaction

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param third_party_transaction_id: The third party transaction unique identifier. E.g TP001
    :type third_party_transaction_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def put_user_tag(request: web.Request, user_id, tag_id, authorization, api_version) -> web.Response:
    """Insert user tag

    Inserts a tag on the user

    :param user_id: The user unique identifier. E.g USER001
    :type user_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)
