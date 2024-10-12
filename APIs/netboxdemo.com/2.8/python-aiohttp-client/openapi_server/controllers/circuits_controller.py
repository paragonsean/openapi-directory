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


async def circuits_circuit_terminations_list(request: web.Request, term_side=None, port_speed=None, upstream_speed=None, xconnect_id=None, q=None, circuit_id=None, site_id=None, site=None, term_side__n=None, port_speed__n=None, port_speed__lte=None, port_speed__lt=None, port_speed__gte=None, port_speed__gt=None, upstream_speed__n=None, upstream_speed__lte=None, upstream_speed__lt=None, upstream_speed__gte=None, upstream_speed__gt=None, xconnect_id__n=None, xconnect_id__ic=None, xconnect_id__nic=None, xconnect_id__iew=None, xconnect_id__niew=None, xconnect_id__isw=None, xconnect_id__nisw=None, xconnect_id__ie=None, xconnect_id__nie=None, circuit_id__n=None, site_id__n=None, site__n=None, limit=None, offset=None) -> web.Response:
    """circuits_circuit_terminations_list

    Call to super to allow for caching

    :param term_side: 
    :type term_side: str
    :param port_speed: 
    :type port_speed: str
    :param upstream_speed: 
    :type upstream_speed: str
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
    :param term_side__n: 
    :type term_side__n: str
    :param port_speed__n: 
    :type port_speed__n: str
    :param port_speed__lte: 
    :type port_speed__lte: str
    :param port_speed__lt: 
    :type port_speed__lt: str
    :param port_speed__gte: 
    :type port_speed__gte: str
    :param port_speed__gt: 
    :type port_speed__gt: str
    :param upstream_speed__n: 
    :type upstream_speed__n: str
    :param upstream_speed__lte: 
    :type upstream_speed__lte: str
    :param upstream_speed__lt: 
    :type upstream_speed__lt: str
    :param upstream_speed__gte: 
    :type upstream_speed__gte: str
    :param upstream_speed__gt: 
    :type upstream_speed__gt: str
    :param xconnect_id__n: 
    :type xconnect_id__n: str
    :param xconnect_id__ic: 
    :type xconnect_id__ic: str
    :param xconnect_id__nic: 
    :type xconnect_id__nic: str
    :param xconnect_id__iew: 
    :type xconnect_id__iew: str
    :param xconnect_id__niew: 
    :type xconnect_id__niew: str
    :param xconnect_id__isw: 
    :type xconnect_id__isw: str
    :param xconnect_id__nisw: 
    :type xconnect_id__nisw: str
    :param xconnect_id__ie: 
    :type xconnect_id__ie: str
    :param xconnect_id__nie: 
    :type xconnect_id__nie: str
    :param circuit_id__n: 
    :type circuit_id__n: str
    :param site_id__n: 
    :type site_id__n: str
    :param site__n: 
    :type site__n: str
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

    Call to super to allow for caching

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


async def circuits_circuit_types_list(request: web.Request, id=None, name=None, slug=None, q=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, slug__n=None, slug__ic=None, slug__nic=None, slug__iew=None, slug__niew=None, slug__isw=None, slug__nisw=None, slug__ie=None, slug__nie=None, limit=None, offset=None) -> web.Response:
    """circuits_circuit_types_list

    Call to super to allow for caching

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param slug: 
    :type slug: str
    :param q: 
    :type q: str
    :param id__n: 
    :type id__n: str
    :param id__lte: 
    :type id__lte: str
    :param id__lt: 
    :type id__lt: str
    :param id__gte: 
    :type id__gte: str
    :param id__gt: 
    :type id__gt: str
    :param name__n: 
    :type name__n: str
    :param name__ic: 
    :type name__ic: str
    :param name__nic: 
    :type name__nic: str
    :param name__iew: 
    :type name__iew: str
    :param name__niew: 
    :type name__niew: str
    :param name__isw: 
    :type name__isw: str
    :param name__nisw: 
    :type name__nisw: str
    :param name__ie: 
    :type name__ie: str
    :param name__nie: 
    :type name__nie: str
    :param slug__n: 
    :type slug__n: str
    :param slug__ic: 
    :type slug__ic: str
    :param slug__nic: 
    :type slug__nic: str
    :param slug__iew: 
    :type slug__iew: str
    :param slug__niew: 
    :type slug__niew: str
    :param slug__isw: 
    :type slug__isw: str
    :param slug__nisw: 
    :type slug__nisw: str
    :param slug__ie: 
    :type slug__ie: str
    :param slug__nie: 
    :type slug__nie: str
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

    Call to super to allow for caching

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


async def circuits_circuits_list(request: web.Request, id=None, cid=None, install_date=None, commit_rate=None, tenant_group_id=None, tenant_group=None, tenant_id=None, tenant=None, created=None, created__gte=None, created__lte=None, last_updated=None, last_updated__gte=None, last_updated__lte=None, q=None, provider_id=None, provider=None, type_id=None, type=None, status=None, site_id=None, site=None, region_id=None, region=None, tag=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, cid__n=None, cid__ic=None, cid__nic=None, cid__iew=None, cid__niew=None, cid__isw=None, cid__nisw=None, cid__ie=None, cid__nie=None, install_date__n=None, install_date__lte=None, install_date__lt=None, install_date__gte=None, install_date__gt=None, commit_rate__n=None, commit_rate__lte=None, commit_rate__lt=None, commit_rate__gte=None, commit_rate__gt=None, tenant_group_id__n=None, tenant_group__n=None, tenant_id__n=None, tenant__n=None, provider_id__n=None, provider__n=None, type_id__n=None, type__n=None, status__n=None, site_id__n=None, site__n=None, region_id__n=None, region__n=None, tag__n=None, limit=None, offset=None) -> web.Response:
    """circuits_circuits_list

    Call to super to allow for caching

    :param id: 
    :type id: str
    :param cid: 
    :type cid: str
    :param install_date: 
    :type install_date: str
    :param commit_rate: 
    :type commit_rate: str
    :param tenant_group_id: 
    :type tenant_group_id: str
    :param tenant_group: 
    :type tenant_group: str
    :param tenant_id: 
    :type tenant_id: str
    :param tenant: 
    :type tenant: str
    :param created: 
    :type created: str
    :param created__gte: 
    :type created__gte: str
    :param created__lte: 
    :type created__lte: str
    :param last_updated: 
    :type last_updated: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__lte: 
    :type last_updated__lte: str
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
    :param site_id: 
    :type site_id: str
    :param site: 
    :type site: str
    :param region_id: 
    :type region_id: str
    :param region: 
    :type region: str
    :param tag: 
    :type tag: str
    :param id__n: 
    :type id__n: str
    :param id__lte: 
    :type id__lte: str
    :param id__lt: 
    :type id__lt: str
    :param id__gte: 
    :type id__gte: str
    :param id__gt: 
    :type id__gt: str
    :param cid__n: 
    :type cid__n: str
    :param cid__ic: 
    :type cid__ic: str
    :param cid__nic: 
    :type cid__nic: str
    :param cid__iew: 
    :type cid__iew: str
    :param cid__niew: 
    :type cid__niew: str
    :param cid__isw: 
    :type cid__isw: str
    :param cid__nisw: 
    :type cid__nisw: str
    :param cid__ie: 
    :type cid__ie: str
    :param cid__nie: 
    :type cid__nie: str
    :param install_date__n: 
    :type install_date__n: str
    :param install_date__lte: 
    :type install_date__lte: str
    :param install_date__lt: 
    :type install_date__lt: str
    :param install_date__gte: 
    :type install_date__gte: str
    :param install_date__gt: 
    :type install_date__gt: str
    :param commit_rate__n: 
    :type commit_rate__n: str
    :param commit_rate__lte: 
    :type commit_rate__lte: str
    :param commit_rate__lt: 
    :type commit_rate__lt: str
    :param commit_rate__gte: 
    :type commit_rate__gte: str
    :param commit_rate__gt: 
    :type commit_rate__gt: str
    :param tenant_group_id__n: 
    :type tenant_group_id__n: str
    :param tenant_group__n: 
    :type tenant_group__n: str
    :param tenant_id__n: 
    :type tenant_id__n: str
    :param tenant__n: 
    :type tenant__n: str
    :param provider_id__n: 
    :type provider_id__n: str
    :param provider__n: 
    :type provider__n: str
    :param type_id__n: 
    :type type_id__n: str
    :param type__n: 
    :type type__n: str
    :param status__n: 
    :type status__n: str
    :param site_id__n: 
    :type site_id__n: str
    :param site__n: 
    :type site__n: str
    :param region_id__n: 
    :type region_id__n: str
    :param region__n: 
    :type region__n: str
    :param tag__n: 
    :type tag__n: str
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

    Call to super to allow for caching

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


async def circuits_providers_list(request: web.Request, id=None, name=None, slug=None, asn=None, account=None, created=None, created__gte=None, created__lte=None, last_updated=None, last_updated__gte=None, last_updated__lte=None, q=None, region_id=None, region=None, site_id=None, site=None, tag=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, slug__n=None, slug__ic=None, slug__nic=None, slug__iew=None, slug__niew=None, slug__isw=None, slug__nisw=None, slug__ie=None, slug__nie=None, asn__n=None, asn__lte=None, asn__lt=None, asn__gte=None, asn__gt=None, account__n=None, account__ic=None, account__nic=None, account__iew=None, account__niew=None, account__isw=None, account__nisw=None, account__ie=None, account__nie=None, region_id__n=None, region__n=None, site_id__n=None, site__n=None, tag__n=None, limit=None, offset=None) -> web.Response:
    """circuits_providers_list

    Call to super to allow for caching

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param slug: 
    :type slug: str
    :param asn: 
    :type asn: str
    :param account: 
    :type account: str
    :param created: 
    :type created: str
    :param created__gte: 
    :type created__gte: str
    :param created__lte: 
    :type created__lte: str
    :param last_updated: 
    :type last_updated: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param q: 
    :type q: str
    :param region_id: 
    :type region_id: str
    :param region: 
    :type region: str
    :param site_id: 
    :type site_id: str
    :param site: 
    :type site: str
    :param tag: 
    :type tag: str
    :param id__n: 
    :type id__n: str
    :param id__lte: 
    :type id__lte: str
    :param id__lt: 
    :type id__lt: str
    :param id__gte: 
    :type id__gte: str
    :param id__gt: 
    :type id__gt: str
    :param name__n: 
    :type name__n: str
    :param name__ic: 
    :type name__ic: str
    :param name__nic: 
    :type name__nic: str
    :param name__iew: 
    :type name__iew: str
    :param name__niew: 
    :type name__niew: str
    :param name__isw: 
    :type name__isw: str
    :param name__nisw: 
    :type name__nisw: str
    :param name__ie: 
    :type name__ie: str
    :param name__nie: 
    :type name__nie: str
    :param slug__n: 
    :type slug__n: str
    :param slug__ic: 
    :type slug__ic: str
    :param slug__nic: 
    :type slug__nic: str
    :param slug__iew: 
    :type slug__iew: str
    :param slug__niew: 
    :type slug__niew: str
    :param slug__isw: 
    :type slug__isw: str
    :param slug__nisw: 
    :type slug__nisw: str
    :param slug__ie: 
    :type slug__ie: str
    :param slug__nie: 
    :type slug__nie: str
    :param asn__n: 
    :type asn__n: str
    :param asn__lte: 
    :type asn__lte: str
    :param asn__lt: 
    :type asn__lt: str
    :param asn__gte: 
    :type asn__gte: str
    :param asn__gt: 
    :type asn__gt: str
    :param account__n: 
    :type account__n: str
    :param account__ic: 
    :type account__ic: str
    :param account__nic: 
    :type account__nic: str
    :param account__iew: 
    :type account__iew: str
    :param account__niew: 
    :type account__niew: str
    :param account__isw: 
    :type account__isw: str
    :param account__nisw: 
    :type account__nisw: str
    :param account__ie: 
    :type account__ie: str
    :param account__nie: 
    :type account__nie: str
    :param region_id__n: 
    :type region_id__n: str
    :param region__n: 
    :type region__n: str
    :param site_id__n: 
    :type site_id__n: str
    :param site__n: 
    :type site__n: str
    :param tag__n: 
    :type tag__n: str
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

    Call to super to allow for caching

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
