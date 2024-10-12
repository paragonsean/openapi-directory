from typing import List, Dict
from aiohttp import web

from openapi_server.models.alert import Alert
from openapi_server.models.alert_list_result import AlertListResult
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def alerts_get_alert_by_management_groups(request: web.Request, api_version, management_group_id, alert_id) -> web.Response:
    """alerts_get_alert_by_management_groups

    Gets an alert for Management Groups by alert ID.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    :type api_version: str
    :param management_group_id: Management Group ID
    :type management_group_id: str
    :param alert_id: Alert ID.
    :type alert_id: str

    """
    return web.Response(status=200)


async def alerts_get_by_account(request: web.Request, api_version, billing_account_id, enrollment_account_id, alert_id) -> web.Response:
    """alerts_get_by_account

    Gets the alert for an account by alert ID.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    :type api_version: str
    :param billing_account_id: BillingAccount ID
    :type billing_account_id: str
    :param enrollment_account_id: Enrollment Account Id
    :type enrollment_account_id: str
    :param alert_id: Alert ID.
    :type alert_id: str

    """
    return web.Response(status=200)


async def alerts_get_by_department(request: web.Request, api_version, billing_account_id, department_id, alert_id) -> web.Response:
    """alerts_get_by_department

    Gets the alert for a department by alert ID.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    :type api_version: str
    :param billing_account_id: BillingAccount ID
    :type billing_account_id: str
    :param department_id: Department ID
    :type department_id: str
    :param alert_id: Alert ID.
    :type alert_id: str

    """
    return web.Response(status=200)


async def alerts_get_by_enrollment(request: web.Request, api_version, billing_account_id, alert_id) -> web.Response:
    """alerts_get_by_enrollment

    Gets the alert for an enrollment by alert ID.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    :type api_version: str
    :param billing_account_id: BillingAccount ID
    :type billing_account_id: str
    :param alert_id: Alert ID.
    :type alert_id: str

    """
    return web.Response(status=200)


async def alerts_get_by_resource_group_name(request: web.Request, subscription_id, resource_group_name, api_version, alert_id) -> web.Response:
    """alerts_get_by_resource_group_name

    Gets the alert for a resource group under a subscription by alert ID.

    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param resource_group_name: Azure Resource Group Name.
    :type resource_group_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    :type api_version: str
    :param alert_id: Alert ID.
    :type alert_id: str

    """
    return web.Response(status=200)


async def alerts_get_by_subscription(request: web.Request, api_version, subscription_id, alert_id) -> web.Response:
    """alerts_get_by_subscription

    Gets the alert for a subscription by alert ID.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    :type api_version: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param alert_id: Alert ID.
    :type alert_id: str

    """
    return web.Response(status=200)


async def alerts_list(request: web.Request, api_version, subscription_id, filter=None, skiptoken=None, top=None) -> web.Response:
    """alerts_list

    List all alerts for a subscription.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    :type api_version: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param filter: May be used to filter alerts by properties/definition/type, properties/definition/category, properties/definition/criteria, properties/costEntityId, properties/creationTime, properties/closeTime, properties/status, properties/source. Supported operators are &#39;eq&#39;,&#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;.
    :type filter: str
    :param skiptoken: Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
    :type skiptoken: str
    :param top: May be used to limit the number of results to the most recent N alerts.
    :type top: int

    """
    return web.Response(status=200)


async def alerts_list_by_account(request: web.Request, api_version, billing_account_id, enrollment_account_id, filter=None, skiptoken=None, top=None) -> web.Response:
    """alerts_list_by_account

    List all alerts for an account.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    :type api_version: str
    :param billing_account_id: BillingAccount ID
    :type billing_account_id: str
    :param enrollment_account_id: Enrollment Account Id
    :type enrollment_account_id: str
    :param filter: May be used to filter alerts by properties/definition/type, properties/definition/category, properties/definition/criteria, properties/costEntityId, properties/creationTime, properties/closeTime, properties/status, properties/source. Supported operators are &#39;eq&#39;,&#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;.
    :type filter: str
    :param skiptoken: Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
    :type skiptoken: str
    :param top: May be used to limit the number of results to the most recent N alerts.
    :type top: int

    """
    return web.Response(status=200)


async def alerts_list_by_department(request: web.Request, api_version, billing_account_id, department_id, filter=None, skiptoken=None, top=None) -> web.Response:
    """alerts_list_by_department

    List all alerts for a department.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    :type api_version: str
    :param billing_account_id: BillingAccount ID
    :type billing_account_id: str
    :param department_id: Department ID
    :type department_id: str
    :param filter: May be used to filter alerts by properties/definition/type, properties/definition/category, properties/definition/criteria, properties/costEntityId, properties/creationTime, properties/closeTime, properties/status, properties/source. Supported operators are &#39;eq&#39;,&#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;.
    :type filter: str
    :param skiptoken: Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
    :type skiptoken: str
    :param top: May be used to limit the number of results to the most recent N alerts.
    :type top: int

    """
    return web.Response(status=200)


async def alerts_list_by_enrollment(request: web.Request, api_version, billing_account_id, filter=None, skiptoken=None, top=None) -> web.Response:
    """alerts_list_by_enrollment

    List all alerts for an enrollment.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    :type api_version: str
    :param billing_account_id: BillingAccount ID
    :type billing_account_id: str
    :param filter: May be used to filter alerts by properties/definition/type, properties/definition/category, properties/definition/criteria, properties/costEntityId, properties/creationTime, properties/closeTime, properties/status, properties/source. Supported operators are &#39;eq&#39;,&#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;.
    :type filter: str
    :param skiptoken: Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
    :type skiptoken: str
    :param top: May be used to limit the number of results to the most recent N alerts.
    :type top: int

    """
    return web.Response(status=200)


async def alerts_list_by_management_groups(request: web.Request, api_version, management_group_id, filter=None, skiptoken=None, top=None) -> web.Response:
    """alerts_list_by_management_groups

    List all alerts for Management Groups.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    :type api_version: str
    :param management_group_id: Management Group ID
    :type management_group_id: str
    :param filter: May be used to filter alerts by properties/definition/type, properties/definition/category, properties/definition/criteria, properties/costEntityId, properties/creationTime, properties/closeTime, properties/status, properties/source. Supported operators are &#39;eq&#39;,&#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;.
    :type filter: str
    :param skiptoken: Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
    :type skiptoken: str
    :param top: May be used to limit the number of results to the most recent N alerts.
    :type top: int

    """
    return web.Response(status=200)


async def alerts_list_by_resource_group_name(request: web.Request, subscription_id, resource_group_name, api_version, filter=None, skiptoken=None, top=None) -> web.Response:
    """alerts_list_by_resource_group_name

    List all alerts for a resource group under a subscription.

    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param resource_group_name: Azure Resource Group Name.
    :type resource_group_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    :type api_version: str
    :param filter: May be used to filter alerts by properties/definition/type, properties/definition/category, properties/definition/criteria, properties/costEntityId, properties/creationTime, properties/closeTime, properties/status, properties/source. Supported operators are &#39;eq&#39;,&#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;.
    :type filter: str
    :param skiptoken: Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
    :type skiptoken: str
    :param top: May be used to limit the number of results to the most recent N alerts.
    :type top: int

    """
    return web.Response(status=200)


async def alerts_update_billing_account_alert_status(request: web.Request, api_version, billing_account_id, alert_id, parameters) -> web.Response:
    """alerts_update_billing_account_alert_status

    Update alerts status for billing account.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    :type api_version: str
    :param billing_account_id: BillingAccount ID
    :type billing_account_id: str
    :param alert_id: Alert ID.
    :type alert_id: str
    :param parameters: Parameters supplied to the update alerts status operation.
    :type parameters: dict | bytes

    """
    parameters = Alert.from_dict(parameters)
    return web.Response(status=200)


async def alerts_update_departments_alert_status(request: web.Request, api_version, billing_account_id, department_id, alert_id, parameters) -> web.Response:
    """alerts_update_departments_alert_status

    Update alerts status for a department.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    :type api_version: str
    :param billing_account_id: BillingAccount ID
    :type billing_account_id: str
    :param department_id: Department ID
    :type department_id: str
    :param alert_id: Alert ID.
    :type alert_id: str
    :param parameters: Parameters supplied to the update alerts status operation.
    :type parameters: dict | bytes

    """
    parameters = Alert.from_dict(parameters)
    return web.Response(status=200)


async def alerts_update_enrollment_account_alert_status(request: web.Request, api_version, billing_account_id, enrollment_account_id, alert_id, parameters) -> web.Response:
    """alerts_update_enrollment_account_alert_status

    Update alerts status for an enrollment account.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    :type api_version: str
    :param billing_account_id: BillingAccount ID
    :type billing_account_id: str
    :param enrollment_account_id: Enrollment Account Id
    :type enrollment_account_id: str
    :param alert_id: Alert ID.
    :type alert_id: str
    :param parameters: Parameters supplied to the update alerts status operation.
    :type parameters: dict | bytes

    """
    parameters = Alert.from_dict(parameters)
    return web.Response(status=200)


async def alerts_update_management_group_alert_status(request: web.Request, api_version, management_group_id, alert_id, parameters) -> web.Response:
    """alerts_update_management_group_alert_status

    Update alerts status for management group.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    :type api_version: str
    :param management_group_id: Management Group ID
    :type management_group_id: str
    :param alert_id: Alert ID.
    :type alert_id: str
    :param parameters: Parameters supplied to the update alerts status operation.
    :type parameters: dict | bytes

    """
    parameters = Alert.from_dict(parameters)
    return web.Response(status=200)


async def alerts_update_resource_group_name_alert_status(request: web.Request, subscription_id, resource_group_name, alert_id, api_version, parameters) -> web.Response:
    """alerts_update_resource_group_name_alert_status

    Update alerts status for a resource group under a subscription.

    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param resource_group_name: Azure Resource Group Name.
    :type resource_group_name: str
    :param alert_id: Alert ID.
    :type alert_id: str
    :param api_version: Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    :type api_version: str
    :param parameters: Parameters supplied to the update alerts status operation.
    :type parameters: dict | bytes

    """
    parameters = Alert.from_dict(parameters)
    return web.Response(status=200)


async def alerts_update_subscription_alert_status(request: web.Request, api_version, subscription_id, alert_id, parameters) -> web.Response:
    """alerts_update_subscription_alert_status

    Update alerts status for a subscription.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    :type api_version: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param alert_id: Alert ID.
    :type alert_id: str
    :param parameters: Parameters supplied to the update alerts status operation.
    :type parameters: dict | bytes

    """
    parameters = Alert.from_dict(parameters)
    return web.Response(status=200)
