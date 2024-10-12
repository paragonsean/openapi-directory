from typing import List, Dict
from aiohttp import web

from openapi_server.models.billing_line_item import BillingLineItem
from openapi_server.models.billing_profile import BillingProfile
from openapi_server.models.billing_profiles_list200_response import BillingProfilesList200Response
from openapi_server.models.cash_payment import CashPayment
from openapi_server.models.cash_payment_log import CashPaymentLog
from openapi_server.models.comm_logs_list200_response import CommLogsList200Response
from openapi_server.models.coverage import Coverage
from openapi_server.models.custom_insurance_plan_name import CustomInsurancePlanName
from openapi_server.models.custom_insurance_plan_names_list200_response import CustomInsurancePlanNamesList200Response
from openapi_server.models.eligibility_checks_list200_response import EligibilityChecksList200Response
from openapi_server.models.line_item_transaction import LineItemTransaction
from openapi_server.models.line_items_list200_response import LineItemsList200Response
from openapi_server.models.patient_payment_log_list200_response import PatientPaymentLogList200Response
from openapi_server.models.patient_payments_list200_response import PatientPaymentsList200Response
from openapi_server.models.phone_call_log import PhoneCallLog
from openapi_server.models.transactions_list200_response import TransactionsList200Response
from openapi_server import util


async def billing_profiles_list(request: web.Request, cursor=None, page_size=None, doctor=None) -> web.Response:
    """billing_profiles_list

    Retrieve or search billing profiles

    :param cursor: 
    :type cursor: str
    :param page_size: 
    :type page_size: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def billing_profiles_read(request: web.Request, id, doctor=None) -> web.Response:
    """billing_profiles_read

    Retrieve an existing billing profiles

    :param id: 
    :type id: str
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def comm_logs_create(request: web.Request, since=None, patient=None, doctor=None) -> web.Response:
    """comm_logs_create

    Create communication (phone call) logs

    :param since: 
    :type since: str
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def comm_logs_list(request: web.Request, cursor=None, page_size=None, since=None, patient=None, doctor=None) -> web.Response:
    """comm_logs_list

    Retrieve or search communicatioin (phone call) logs

    :param cursor: 
    :type cursor: str
    :param page_size: 
    :type page_size: int
    :param since: 
    :type since: str
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def comm_logs_partial_update(request: web.Request, id, since=None, patient=None, doctor=None) -> web.Response:
    """comm_logs_partial_update

    Update an existing communication (phone call) logs

    :param id: 
    :type id: str
    :param since: 
    :type since: str
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def comm_logs_read(request: web.Request, id, since=None, patient=None, doctor=None) -> web.Response:
    """comm_logs_read

    Retrieve an existing communication (phone call) logs

    :param id: 
    :type id: str
    :param since: 
    :type since: str
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def comm_logs_update(request: web.Request, id, since=None, patient=None, doctor=None) -> web.Response:
    """comm_logs_update

    Update an existing communication (phone call) logs

    :param id: 
    :type id: str
    :param since: 
    :type since: str
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def custom_insurance_plan_names_list(request: web.Request, cursor=None, page_size=None, since=None, user=None, name=None, doctor=None) -> web.Response:
    """custom_insurance_plan_names_list

    Retrieve or search custom insurance plan names

    :param cursor: 
    :type cursor: str
    :param page_size: 
    :type page_size: int
    :param since: 
    :type since: str
    :param user: 
    :type user: int
    :param name: 
    :type name: str
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def custom_insurance_plan_names_read(request: web.Request, id, since=None, user=None, name=None, doctor=None) -> web.Response:
    """custom_insurance_plan_names_read

    Retrieve an existing custom insurance plan name

    :param id: 
    :type id: str
    :param since: 
    :type since: str
    :param user: 
    :type user: int
    :param name: 
    :type name: str
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def eligibility_checks_list(request: web.Request, cursor=None, page_size=None, appointment=None, appointment_date=None, doctor=None, query_date_range=None, appointment_date_range=None, query_date=None, patient=None) -> web.Response:
    """eligibility_checks_list

    Retrieve or search past eligibility checks for patient

    :param cursor: 
    :type cursor: str
    :param page_size: 
    :type page_size: int
    :param appointment: 
    :type appointment: int
    :param appointment_date: 
    :type appointment_date: str
    :param doctor: 
    :type doctor: int
    :param query_date_range: 
    :type query_date_range: str
    :param appointment_date_range: 
    :type appointment_date_range: str
    :param query_date: 
    :type query_date: str
    :param patient: 
    :type patient: int

    """
    return web.Response(status=200)


async def eligibility_checks_read(request: web.Request, id, appointment=None, appointment_date=None, doctor=None, query_date_range=None, appointment_date_range=None, query_date=None, patient=None) -> web.Response:
    """eligibility_checks_read

    Retrieve an existing past eligibility check

    :param id: 
    :type id: str
    :param appointment: 
    :type appointment: int
    :param appointment_date: 
    :type appointment_date: str
    :param doctor: 
    :type doctor: int
    :param query_date_range: 
    :type query_date_range: str
    :param appointment_date_range: 
    :type appointment_date_range: str
    :param query_date: 
    :type query_date: str
    :param patient: 
    :type patient: int

    """
    return web.Response(status=200)


async def line_items_create(request: web.Request, posted_date=None, patient=None, office=None, doctor=None, since=None, appointment=None, service_date=None) -> web.Response:
    """line_items_create

    Create billing line item for appointments

    :param posted_date: 
    :type posted_date: str
    :param patient: 
    :type patient: int
    :param office: 
    :type office: int
    :param doctor: 
    :type doctor: int
    :param since: 
    :type since: str
    :param appointment: 
    :type appointment: int
    :param service_date: 
    :type service_date: str

    """
    return web.Response(status=200)


async def line_items_delete(request: web.Request, id, posted_date=None, patient=None, office=None, doctor=None, since=None, appointment=None, service_date=None) -> web.Response:
    """line_items_delete

    

    :param id: 
    :type id: str
    :param posted_date: 
    :type posted_date: str
    :param patient: 
    :type patient: int
    :param office: 
    :type office: int
    :param doctor: 
    :type doctor: int
    :param since: 
    :type since: str
    :param appointment: 
    :type appointment: int
    :param service_date: 
    :type service_date: str

    """
    return web.Response(status=200)


async def line_items_list(request: web.Request, cursor=None, page_size=None, posted_date=None, patient=None, office=None, doctor=None, since=None, appointment=None, service_date=None) -> web.Response:
    """line_items_list

    Retrieve or search billing line items

    :param cursor: 
    :type cursor: str
    :param page_size: 
    :type page_size: int
    :param posted_date: 
    :type posted_date: str
    :param patient: 
    :type patient: int
    :param office: 
    :type office: int
    :param doctor: 
    :type doctor: int
    :param since: 
    :type since: str
    :param appointment: 
    :type appointment: int
    :param service_date: 
    :type service_date: str

    """
    return web.Response(status=200)


async def line_items_partial_update(request: web.Request, id, posted_date=None, patient=None, office=None, doctor=None, since=None, appointment=None, service_date=None) -> web.Response:
    """line_items_partial_update

    

    :param id: 
    :type id: str
    :param posted_date: 
    :type posted_date: str
    :param patient: 
    :type patient: int
    :param office: 
    :type office: int
    :param doctor: 
    :type doctor: int
    :param since: 
    :type since: str
    :param appointment: 
    :type appointment: int
    :param service_date: 
    :type service_date: str

    """
    return web.Response(status=200)


async def line_items_read(request: web.Request, id, posted_date=None, patient=None, office=None, doctor=None, since=None, appointment=None, service_date=None) -> web.Response:
    """line_items_read

    Retrieve an existing billing line item

    :param id: 
    :type id: str
    :param posted_date: 
    :type posted_date: str
    :param patient: 
    :type patient: int
    :param office: 
    :type office: int
    :param doctor: 
    :type doctor: int
    :param since: 
    :type since: str
    :param appointment: 
    :type appointment: int
    :param service_date: 
    :type service_date: str

    """
    return web.Response(status=200)


async def line_items_update(request: web.Request, id, posted_date=None, patient=None, office=None, doctor=None, since=None, appointment=None, service_date=None) -> web.Response:
    """line_items_update

    

    :param id: 
    :type id: str
    :param posted_date: 
    :type posted_date: str
    :param patient: 
    :type patient: int
    :param office: 
    :type office: int
    :param doctor: 
    :type doctor: int
    :param since: 
    :type since: str
    :param appointment: 
    :type appointment: int
    :param service_date: 
    :type service_date: str

    """
    return web.Response(status=200)


async def patient_payment_log_list(request: web.Request, cursor=None, page_size=None, since=None, office=None, doctor=None) -> web.Response:
    """patient_payment_log_list

    Retrieve or search patient payment logs

    :param cursor: 
    :type cursor: str
    :param page_size: 
    :type page_size: int
    :param since: 
    :type since: str
    :param office: 
    :type office: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def patient_payment_log_read(request: web.Request, id, since=None, office=None, doctor=None) -> web.Response:
    """patient_payment_log_read

    Retrieve an existing patient payment log

    :param id: 
    :type id: str
    :param since: 
    :type since: str
    :param office: 
    :type office: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def patient_payments_create(request: web.Request, since=None, patient=None, doctor=None) -> web.Response:
    """patient_payments_create

    Create patient payment

    :param since: 
    :type since: str
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def patient_payments_list(request: web.Request, cursor=None, page_size=None, since=None, patient=None, doctor=None) -> web.Response:
    """patient_payments_list

    Retrieve or search patient payments

    :param cursor: 
    :type cursor: str
    :param page_size: 
    :type page_size: int
    :param since: 
    :type since: str
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def patient_payments_read(request: web.Request, id, since=None, patient=None, doctor=None) -> web.Response:
    """patient_payments_read

    Retrieve an existing patient payment

    :param id: 
    :type id: str
    :param since: 
    :type since: str
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def procedures_list(request: web.Request, cursor=None, page_size=None, mu_date=None, patient=None, doctor=None, mu_date_range=None, appointment=None, service_date=None) -> web.Response:
    """procedures_list

    

    :param cursor: 
    :type cursor: str
    :param page_size: 
    :type page_size: int
    :param mu_date: 
    :type mu_date: str
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int
    :param mu_date_range: 
    :type mu_date_range: str
    :param appointment: 
    :type appointment: int
    :param service_date: 
    :type service_date: str

    """
    return web.Response(status=200)


async def procedures_read(request: web.Request, id, mu_date=None, patient=None, doctor=None, mu_date_range=None, appointment=None, service_date=None) -> web.Response:
    """procedures_read

    

    :param id: 
    :type id: str
    :param mu_date: 
    :type mu_date: str
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int
    :param mu_date_range: 
    :type mu_date_range: str
    :param appointment: 
    :type appointment: int
    :param service_date: 
    :type service_date: str

    """
    return web.Response(status=200)


async def transactions_list(request: web.Request, cursor=None, page_size=None, line_item=None, posted_date=None, appointment=None, since=None, doctor=None) -> web.Response:
    """transactions_list

    Retrieve or search insurance transactions associated with billing line items

    :param cursor: 
    :type cursor: str
    :param page_size: 
    :type page_size: int
    :param line_item: 
    :type line_item: int
    :param posted_date: 
    :type posted_date: str
    :param appointment: 
    :type appointment: int
    :param since: 
    :type since: str
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def transactions_read(request: web.Request, id, line_item=None, posted_date=None, appointment=None, since=None, doctor=None) -> web.Response:
    """transactions_read

    Retrieve an existing insurance transaction

    :param id: 
    :type id: str
    :param line_item: 
    :type line_item: int
    :param posted_date: 
    :type posted_date: str
    :param appointment: 
    :type appointment: int
    :param since: 
    :type since: str
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)
