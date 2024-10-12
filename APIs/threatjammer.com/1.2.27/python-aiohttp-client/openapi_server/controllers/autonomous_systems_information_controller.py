from typing import List, Dict
from aiohttp import web

from openapi_server.models.autonomous_system_output import AutonomousSystemOutput
from openapi_server.models.autonomous_system_prefix_output import AutonomousSystemPrefixOutput
from openapi_server.models.autonomous_system_prefixes_output import AutonomousSystemPrefixesOutput
from openapi_server.models.autonomous_system_registry_output import AutonomousSystemRegistryOutput
from openapi_server.models.autonomous_system_status_output import AutonomousSystemStatusOutput
from openapi_server.models.body_query_asn_prefix_information_v1_asn_prefix_post import BodyQueryAsnPrefixInformationV1AsnPrefixPost
from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server import util


async def query_asn_prefix_information_v1_asn_prefix_post(request: web.Request, body) -> web.Response:
    """Get the IPv4 or IPv6 prefix of the CIDR given.

    ### What Obtain the IPv4 or IPv6 prefix and the Autonomous System information of the CIDR passed in the body as a POST method. This endpoint works around the problem of passing &#39;/&#39; addresses in the URI.  ### Parameters The endpoint accepts only the following parameter in the body as a JSON object: - &#x60;&#x60;prefix&#x60;&#x60;: (Mandatory) The CIDR v4 or v6 to be queried.  ### Result The result is a JSON object with the following structure: - &#x60;&#x60;self&#x60;&#x60;: the URI to individual IPv4 prefix. - &#x60;&#x60;asn&#x60;&#x60;: the URI to query the full details of the ASN. - &#x60;&#x60;object_type&#x60;&#x60;: the type of the prefix. The allowed values are: IPv4 or IPv6. - &#x60;&#x60;maintainer&#x60;&#x60;: the information about the maintainer of this prefix in the registry. - &#x60;&#x60;description&#x60;&#x60;: the description of the prefix as registered in the registry. - &#x60;&#x60;registry_date&#x60;&#x60;: the date of registration of the prefix in the registry. The format is YYYY-MM-DD. - &#x60;&#x60;registry_status&#x60;&#x60;: the URI of the status of the prefix as stored in the registry. - &#x60;&#x60;score&#x60;&#x60;: The risk score of the prefix. It ranges from 0 to 99. - &#x60;&#x60;risk&#x60;&#x60;: The risk of the prefix. The allowed values are: LOW, MEDIUM, HIGH. It&#39;s a human readable representation of the score.  ### Errors The endpoint will return the following errors: - a &#x60;404 Not Found&#x60; error if the prefix information was not found. - a &#x60;422 Unprocessable Entity&#x60; error if the CIDR is malformed.  It will also return the API Global errors described in the API description.

    :param body: 
    :type body: dict | bytes

    """
    body = BodyQueryAsnPrefixInformationV1AsnPrefixPost.from_dict(body)
    return web.Response(status=200)


async def query_asn_prefixes_list_v1_asn_number_prefixes_get(request: web.Request, number) -> web.Response:
    """Get the list of IPv4 and IPv6 prefixes of the AS number given.

    ### What Obtain the full list of IPv4 and IPv6 prefixes of the Autonomous System Number (ASN) passed as a parameter.  ### Parameters The endpoint accepts only the following parameter in the path: - &#x60;&#x60;number&#x60;&#x60;: (Mandatory) The ASN number to be queried.  ### Result The result is a JSON object with the following structure: - &#x60;&#x60;self&#x60;&#x60;: the URI of the API call - &#x60;&#x60;asn&#x60;&#x60;: the URI to query the full details of the ASN. - &#x60;&#x60;prefixes_v4&#x60;&#x60;: the list of IPv4 prefixes that belong to the ASN. Each element of the list is a JSON object with the following structure:     - &#x60;&#x60;self&#x60;&#x60;: the URI to individual IPv4 prefix.     - &#x60;&#x60;asn&#x60;&#x60;: the URI to query the full details of the ASN.     - &#x60;&#x60;object_type&#x60;&#x60;: the type of the prefix. The allowed values are: IPv4.     - &#x60;&#x60;maintainer&#x60;&#x60;: the information about the maintainer of this prefix in the registry.     - &#x60;&#x60;description&#x60;&#x60;: the description of the prefix as registered in the registry.     - &#x60;&#x60;registry_date&#x60;&#x60;: the date of registration of the prefix in the registry. The format is YYYY-MM-DD.     - &#x60;&#x60;registry_status&#x60;&#x60;: the URI of the status of the prefix as stored in the registry.     - &#x60;&#x60;score&#x60;&#x60;: The risk score of the prefix. It ranges from 0 to 99.     - &#x60;&#x60;risk&#x60;&#x60;: The risk of the prefix. The allowed values are: LOW, MEDIUM, HIGH. It&#39;s a human readable representation of the score. - &#x60;&#x60;prefixes_v6&#x60;&#x60;: the list of IPv6 prefixes that belong to the ASN. Each element of the list is a JSON object with the following structure:     - &#x60;&#x60;self&#x60;&#x60;: the URI to individual IPv6 prefix.     - &#x60;&#x60;asn&#x60;&#x60;: the URI to query the full details of the ASN.     - &#x60;&#x60;object_type&#x60;&#x60;: the type of the prefix. The allowed values are: IPv6.     - &#x60;&#x60;maintainer&#x60;&#x60;: the information about the maintainer of this prefix in the registry.     - &#x60;&#x60;description&#x60;&#x60;: the description of the prefix as registered in the registry.     - &#x60;&#x60;registry_date&#x60;&#x60;: the date of registration of the prefix in the registry. The format is YYYY-MM-DD.     - &#x60;&#x60;registry_status&#x60;&#x60;: the URI of the status of the prefix as stored in the registry.     - &#x60;&#x60;score&#x60;&#x60;: The risk score of the prefix. It ranges from 0 to 99.     - &#x60;&#x60;risk&#x60;&#x60;: The risk of the prefix. The allowed values are: LOW, MEDIUM, HIGH. It&#39;s a human readable representation of the score.  ### Errors The endpoint will return the following errors: - a &#x60;404 Not Found&#x60; error if the AS was not found. - a &#x60;422 Unprocessable Entity&#x60; error if the AS number is malformed.  It will also return the API Global errors described in the API description.

    :param number: 
    :type number: int

    """
    return web.Response(status=200)


async def query_asn_v1_asn_number_get(request: web.Request, number) -> web.Response:
    """Get the Autonomous System details of the AS number given.

    ### What Obtain the full details of the Autonomous System Number (ASN) passed as a parameter.  ### Parameters The endpoint accepts only the following parameter in the path: - &#x60;&#x60;number&#x60;&#x60;: (Mandatory) The ASN number to be queried.  ### Result The result is a JSON object with the following structure: - &#x60;&#x60;self&#x60;&#x60;: the URI of the API call - &#x60;&#x60;name&#x60;&#x60;: the name of the Autonomous System as registered in the registries databases. - &#x60;&#x60;description&#x60;&#x60;: the description of the Autonomous System as registered in the registries databases. - &#x60;&#x60;country_code&#x60;&#x60;: the ISO 3166-1 alpha-2 country code of the Autonomous System. - &#x60;&#x60;registry_date&#x60;&#x60;: the date of registration of the Autonomous System in the registry. The format is YYYY-MM-DD. - &#x60;&#x60;registry&#x60;&#x60;: the URI of the registry where the Autonomous System is registered. - &#x60;&#x60;status&#x60;&#x60;: the status of the Autonomous System as stored in the registry. - &#x60;&#x60;prefixes&#x60;&#x60;: the URI to the list of prefixes that belong to the Autonomous System. - &#x60;&#x60;score&#x60;&#x60;: The risk score of the Autonomous System. It ranges from 0 to 99. - &#x60;&#x60;risk&#x60;&#x60;: The risk of the Autonomous System. The allowed values are: LOW, MEDIUM, HIGH. It&#39;s a human readable representation of the score.   ### Errors The endpoint will return the following errors: - a &#x60;404 Not Found&#x60; error if the AS was not found. - a &#x60;422 Unprocessable Entity&#x60; error if the AS number is malformed.  It will also return the API Global errors described in the API description.

    :param number: 
    :type number: int

    """
    return web.Response(status=200)


async def query_ip_address_network_information_v1_asn_ip_ip_address_get(request: web.Request, ip_address) -> web.Response:
    """Get the IPv4 or IPv6 prefix of the IP address given.

    ### What Obtain the IPv4 or IPv6 prefix and the Autonomous System information of the IP address passed as a parameter.  ### Parameters The endpoint accepts only the following parameter in the path: - &#x60;&#x60;ip_address&#x60;&#x60;: (Mandatory) The IPv4 or IPv6 address to be queried.  ### Result The result is a JSON object with the following structure: - &#x60;&#x60;self&#x60;&#x60;: the URI to individual IPv4 prefix. - &#x60;&#x60;asn&#x60;&#x60;: the URI to query the full details of the ASN. - &#x60;&#x60;object_type&#x60;&#x60;: the type of the prefix. The allowed values are: IPv4 or IPv6. - &#x60;&#x60;maintainer&#x60;&#x60;: the information about the maintainer of this prefix in the registry. - &#x60;&#x60;description&#x60;&#x60;: the description of the prefix as registered in the registry. - &#x60;&#x60;registry_date&#x60;&#x60;: the date of registration of the prefix in the registry. The format is YYYY-MM-DD. - &#x60;&#x60;registry_status&#x60;&#x60;: the URI of the status of the prefix as stored in the registry. - &#x60;&#x60;score&#x60;&#x60;: The risk score of the prefix. It ranges from 0 to 99. - &#x60;&#x60;risk&#x60;&#x60;: The risk of the prefix. The allowed values are: LOW, MEDIUM, HIGH. It&#39;s a human readable representation of the score.  ### Errors The endpoint will return the following errors: - a &#x60;404 Not Found&#x60; error if the prefix information was not found. - a &#x60;422 Unprocessable Entity&#x60; error if the IP address is malformed.  It will also return the API Global errors described in the API description.

    :param ip_address: 
    :type ip_address: str

    """
    return web.Response(status=200)


async def query_registry_by_the_name_v1_asn_registry_code_get(request: web.Request, code) -> web.Response:
    """Get the information of a Regional Internet Registries (RIRs) given.

    ### What Obtain the information about the Regional Internet Registries (RIRs) given as a parameter.  ### Parameters The endpoint accepts only the following parameter in the path: - &#x60;&#x60;code&#x60;&#x60;: (Mandatory) The code that identifies uniquely the RIR. Possible values are: iana, arin, ripencc, afrinic, apnic, lacnic.  ### Result The result is a JSON object with the following structure: - &#x60;&#x60;self&#x60;&#x60;: the URI to individual RIR. - &#x60;&#x60;name&#x60;&#x60;: the RIR name. - &#x60;&#x60;code&#x60;&#x60;: the internal code of the RIR in the system.  ### Errors - a &#x60;422 Unprocessable Entity&#x60; error if the code is not one of the available.  It will also return the API Global errors described in the API description.

    :param code: 
    :type code: str

    """
    return web.Response(status=200)


async def query_registry_names_v1_asn_registry_all_get(request: web.Request, ) -> web.Response:
    """Get the list of the Regional Internet Registries (RIRs) entities worldwide.

    ### What Obtain the list of Regional Internet Registries (RIRs) entities worldwide.  ### Parameters No parameters are required.  ### Result The result is a JSON object with a list of the following JSON objects: - &#x60;&#x60;self&#x60;&#x60;: the URI to individual RIR. - &#x60;&#x60;name&#x60;&#x60;: the RIR name. - &#x60;&#x60;code&#x60;&#x60;: the internal code of the RIR in the system. Possible values are: iana, arin, ripencc, afrinic, apnic, lacnic.  ### Errors It will return the API Global errors described in the API description.


    """
    return web.Response(status=200)


async def query_status_by_the_name_v1_asn_status_code_get(request: web.Request, code) -> web.Response:
    """Get the information of a status given.

    ### What Obtain the information about the status of an object in the registry as a parameter.  ### Parameters The endpoint accepts only the following parameter in the path: - &#x60;&#x60;code&#x60;&#x60;: (Mandatory) The code that identifies uniquely the status in the registry. Possible values are: assigned, reserved, allocated, available.   ### Result The result is a JSON object with the following structure: - &#x60;&#x60;self&#x60;&#x60;: the URI to individual status. - &#x60;&#x60;name&#x60;&#x60;: the human readable name of the status. - &#x60;&#x60;code&#x60;&#x60;: the internal code of the status in the system.  ### Errors - a &#x60;422 Unprocessable Entity&#x60; error if the code is not one of the available.  It will also return the API Global errors described in the API description.

    :param code: 
    :type code: str

    """
    return web.Response(status=200)


async def query_status_names_v1_asn_status_all_get(request: web.Request, ) -> web.Response:
    """Get the list of status of an object in a registry.

    ### What Obtain the list of status of an object can be in a registry.  ### Parameters No parameters are required.  ### Result The result is a JSON object with a list of the following JSON objects: - &#x60;&#x60;self&#x60;&#x60;: the URI to individual status. - &#x60;&#x60;name&#x60;&#x60;: the code name. - &#x60;&#x60;code&#x60;&#x60;: the internal code of the status in the system. Possible values are: assigned, reserved, allocated, available.  ### Errors It will return the API Global errors described in the API description.


    """
    return web.Response(status=200)
