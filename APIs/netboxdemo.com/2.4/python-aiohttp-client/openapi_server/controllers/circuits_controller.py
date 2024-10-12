from typing import List, Dict
from aiohttp import web

from openapi_server.models.circuit import Circuit
from openapi_server.models.circuit_termination import CircuitTermination
from openapi_server.models.circuit_type import CircuitType
from openapi_server.models.circuits_circuit_terminations_list200_response import CircuitsCircuitTerminationsList200Response
from openapi_server.models.circuits_circuit_types_list200_response import CircuitsCircuitTypesList200Response
from openapi_server.models.circuits_circuits_list200_response import CircuitsCircuitsList200Response
from openapi_server.models.circuits_providers_list200_response import CircuitsProvidersList200Response
from openapi_server.models.provider import Provider
from openapi_server.models.writable_circuit import WritableCircuit
from openapi_server.models.writable_circuit_termination import WritableCircuitTermination
from openapi_server import util


async def circuits_choices_list(request: web.Request, ) -> web.Response:
    """circuits_choices_list

    


    """
    return web.Response(status=200)


async def circuits_choices_read(request: web.Request, id) -> web.Response:
    """circuits_choices_read

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def circuits_circuit_terminations_create(request: web.Request, body) -> web.Response:
    """circuits_circuit_terminations_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableCircuitTermination.from_dict(body)
    return web.Response(status=200)


async def circuits_circuit_terminations_delete(request: web.Request, id) -> web.Response:
    """circuits_circuit_terminations_delete

    

    :param id: A unique integer value identifying this circuit termination.
    :type id: int

    """
    return web.Response(status=200)


async def circuits_circuit_terminations_list(request: web.Request, term_side=None, port_speed=None, upstream_speed=None, xconnect_id=None, q=None, circuit_id=None, site_id=None, site=None, limit=None, offset=None) -> web.Response:
    """circuits_circuit_terminations_list

    

    :param term_side: 
    :type term_side: str
    :param port_speed: 
    :type port_speed: 
    :param upstream_speed: 
    :type upstream_speed: 
    :param xconnect_id: 
    :type xconnect_id: str
    :param q: 
    :type q: str
    :param circuit_id: 
    :type circuit_id: str
    :param site_id: 
    :type site_id: str
    :param site: 
    :type site: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def circuits_circuit_terminations_partial_update(request: web.Request, id, body) -> web.Response:
    """circuits_circuit_terminations_partial_update

    

    :param id: A unique integer value identifying this circuit termination.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableCircuitTermination.from_dict(body)
    return web.Response(status=200)


async def circuits_circuit_terminations_read(request: web.Request, id) -> web.Response:
    """circuits_circuit_terminations_read

    

    :param id: A unique integer value identifying this circuit termination.
    :type id: int

    """
    return web.Response(status=200)


async def circuits_circuit_terminations_update(request: web.Request, id, body) -> web.Response:
    """circuits_circuit_terminations_update

    

    :param id: A unique integer value identifying this circuit termination.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableCircuitTermination.from_dict(body)
    return web.Response(status=200)


async def circuits_circuit_types_create(request: web.Request, body) -> web.Response:
    """circuits_circuit_types_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = CircuitType.from_dict(body)
    return web.Response(status=200)


async def circuits_circuit_types_delete(request: web.Request, id) -> web.Response:
    """circuits_circuit_types_delete

    

    :param id: A unique integer value identifying this circuit type.
    :type id: int

    """
    return web.Response(status=200)


async def circuits_circuit_types_list(request: web.Request, name=None, slug=None, limit=None, offset=None) -> web.Response:
    """circuits_circuit_types_list

    

    :param name: 
    :type name: str
    :param slug: 
    :type slug: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def circuits_circuit_types_partial_update(request: web.Request, id, body) -> web.Response:
    """circuits_circuit_types_partial_update

    

    :param id: A unique integer value identifying this circuit type.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = CircuitType.from_dict(body)
    return web.Response(status=200)


async def circuits_circuit_types_read(request: web.Request, id) -> web.Response:
    """circuits_circuit_types_read

    

    :param id: A unique integer value identifying this circuit type.
    :type id: int

    """
    return web.Response(status=200)


async def circuits_circuit_types_update(request: web.Request, id, body) -> web.Response:
    """circuits_circuit_types_update

    

    :param id: A unique integer value identifying this circuit type.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = CircuitType.from_dict(body)
    return web.Response(status=200)


async def circuits_circuits_create(request: web.Request, body) -> web.Response:
    """circuits_circuits_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableCircuit.from_dict(body)
    return web.Response(status=200)


async def circuits_circuits_delete(request: web.Request, id) -> web.Response:
    """circuits_circuits_delete

    

    :param id: A unique integer value identifying this circuit.
    :type id: int

    """
    return web.Response(status=200)


async def circuits_circuits_list(request: web.Request, cid=None, install_date=None, commit_rate=None, id__in=None, q=None, provider_id=None, provider=None, type_id=None, type=None, status=None, tenant_id=None, tenant=None, site_id=None, site=None, tag=None, limit=None, offset=None) -> web.Response:
    """circuits_circuits_list

    

    :param cid: 
    :type cid: str
    :param install_date: 
    :type install_date: str
    :param commit_rate: 
    :type commit_rate: 
    :param id__in: Multiple values may be separated by commas.
    :type id__in: str
    :param q: 
    :type q: str
    :param provider_id: 
    :type provider_id: str
    :param provider: 
    :type provider: str
    :param type_id: 
    :type type_id: str
    :param type: 
    :type type: str
    :param status: 
    :type status: str
    :param tenant_id: 
    :type tenant_id: str
    :param tenant: 
    :type tenant: str
    :param site_id: 
    :type site_id: str
    :param site: 
    :type site: str
    :param tag: 
    :type tag: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def circuits_circuits_partial_update(request: web.Request, id, body) -> web.Response:
    """circuits_circuits_partial_update

    

    :param id: A unique integer value identifying this circuit.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableCircuit.from_dict(body)
    return web.Response(status=200)


async def circuits_circuits_read(request: web.Request, id) -> web.Response:
    """circuits_circuits_read

    

    :param id: A unique integer value identifying this circuit.
    :type id: int

    """
    return web.Response(status=200)


async def circuits_circuits_update(request: web.Request, id, body) -> web.Response:
    """circuits_circuits_update

    

    :param id: A unique integer value identifying this circuit.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableCircuit.from_dict(body)
    return web.Response(status=200)


async def circuits_providers_create(request: web.Request, body) -> web.Response:
    """circuits_providers_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = Provider.from_dict(body)
    return web.Response(status=200)


async def circuits_providers_delete(request: web.Request, id) -> web.Response:
    """circuits_providers_delete

    

    :param id: A unique integer value identifying this provider.
    :type id: int

    """
    return web.Response(status=200)


async def circuits_providers_graphs(request: web.Request, id) -> web.Response:
    """circuits_providers_graphs

    A convenience method for rendering graphs for a particular provider.

    :param id: A unique integer value identifying this provider.
    :type id: int

    """
    return web.Response(status=200)


async def circuits_providers_list(request: web.Request, name=None, slug=None, asn=None, account=None, id__in=None, q=None, site_id=None, site=None, tag=None, limit=None, offset=None) -> web.Response:
    """circuits_providers_list

    

    :param name: 
    :type name: str
    :param slug: 
    :type slug: str
    :param asn: 
    :type asn: 
    :param account: 
    :type account: str
    :param id__in: Multiple values may be separated by commas.
    :type id__in: str
    :param q: 
    :type q: str
    :param site_id: 
    :type site_id: str
    :param site: 
    :type site: str
    :param tag: 
    :type tag: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def circuits_providers_partial_update(request: web.Request, id, body) -> web.Response:
    """circuits_providers_partial_update

    

    :param id: A unique integer value identifying this provider.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = Provider.from_dict(body)
    return web.Response(status=200)


async def circuits_providers_read(request: web.Request, id) -> web.Response:
    """circuits_providers_read

    

    :param id: A unique integer value identifying this provider.
    :type id: int

    """
    return web.Response(status=200)


async def circuits_providers_update(request: web.Request, id, body) -> web.Response:
    """circuits_providers_update

    

    :param id: A unique integer value identifying this provider.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = Provider.from_dict(body)
    return web.Response(status=200)
