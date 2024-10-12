from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import ApiError
from openapi_server.models.arista_switch_data_source import AristaSwitchDataSource
from openapi_server.models.arista_switch_data_source_request import AristaSwitchDataSourceRequest
from openapi_server.models.brocade_switch_data_source import BrocadeSwitchDataSource
from openapi_server.models.brocade_switch_data_source_request import BrocadeSwitchDataSourceRequest
from openapi_server.models.checkpoint_firewall_data_source import CheckpointFirewallDataSource
from openapi_server.models.checkpoint_firewall_data_source_request import CheckpointFirewallDataSourceRequest
from openapi_server.models.cisco_switch_data_source import CiscoSwitchDataSource
from openapi_server.models.cisco_switch_data_source_request import CiscoSwitchDataSourceRequest
from openapi_server.models.data_source_list_response import DataSourceListResponse
from openapi_server.models.dell_switch_data_source import DellSwitchDataSource
from openapi_server.models.dell_switch_data_source_request import DellSwitchDataSourceRequest
from openapi_server.models.hp_one_view_manager_data_source import HPOneViewManagerDataSource
from openapi_server.models.hp_one_view_manager_data_source_request import HPOneViewManagerDataSourceRequest
from openapi_server.models.hpvc_manager_data_source import HPVCManagerDataSource
from openapi_server.models.hpvc_manager_data_source_request import HPVCManagerDataSourceRequest
from openapi_server.models.juniper_switch_data_source import JuniperSwitchDataSource
from openapi_server.models.juniper_switch_data_source_request import JuniperSwitchDataSourceRequest
from openapi_server.models.nsx_controller_data_collection import NSXControllerDataCollection
from openapi_server.models.nsxv_manager_data_source import NSXVManagerDataSource
from openapi_server.models.nsxv_manager_data_source_request import NSXVManagerDataSourceRequest
from openapi_server.models.pan_firewall_data_source import PanFirewallDataSource
from openapi_server.models.pan_firewall_data_source_request import PanFirewallDataSourceRequest
from openapi_server.models.snmp_config import SNMPConfig
from openapi_server.models.ucs_manager_data_source import UCSManagerDataSource
from openapi_server.models.ucs_manager_data_source_request import UCSManagerDataSourceRequest
from openapi_server.models.v_center_data_source import VCenterDataSource
from openapi_server.models.v_center_data_source_request import VCenterDataSourceRequest
from openapi_server import util


async def add_arista_switch(request: web.Request, body=None) -> web.Response:
    """Create an arista switch data source

    Add arista switch data source

    :param body: Add a cisco switch as datasource
    :type body: dict | bytes

    """
    body = AristaSwitchDataSourceRequest.from_dict(body)
    return web.Response(status=200)


async def add_brocade_switch(request: web.Request, body=None) -> web.Response:
    """Create a brocade switch data source

    Add brocade switch as a data source

    :param body: 
    :type body: dict | bytes

    """
    body = BrocadeSwitchDataSourceRequest.from_dict(body)
    return web.Response(status=200)


async def add_checkpoint_firewall(request: web.Request, body=None) -> web.Response:
    """Create a checkpoint firewall

    Add checkpoint firewall as data source

    :param body: Add a vSec Checkpoint firewall as data source
    :type body: dict | bytes

    """
    body = CheckpointFirewallDataSourceRequest.from_dict(body)
    return web.Response(status=200)


async def add_cisco_switch(request: web.Request, body=None) -> web.Response:
    """Create a cisco switch data source

    Add cisco switch as data source. User must provide one of ip or fqdn field in the request body. Appropriate proxy id is retrieved from infra/nodes URL to select the proxy node.

    :param body: Add a cisco switch as datasource.
    :type body: dict | bytes

    """
    body = CiscoSwitchDataSourceRequest.from_dict(body)
    return web.Response(status=200)


async def add_dell_switch(request: web.Request, body=None) -> web.Response:
    """Create a dell switch data source

    Add a dell switch as data source

    :param body: 
    :type body: dict | bytes

    """
    body = DellSwitchDataSourceRequest.from_dict(body)
    return web.Response(status=200)


async def add_hpov_manager(request: web.Request, body=None) -> web.Response:
    """Create a hp oneview manager data source

    Add a hp oneview manager data source

    :param body: 
    :type body: dict | bytes

    """
    body = HPOneViewManagerDataSourceRequest.from_dict(body)
    return web.Response(status=200)


async def add_hpvc_manager(request: web.Request, body=None) -> web.Response:
    """Create a hpvc manager data source

    Add hpvc manager data source

    :param body: Add a switch as datasource
    :type body: dict | bytes

    """
    body = HPVCManagerDataSourceRequest.from_dict(body)
    return web.Response(status=200)


async def add_juniper_switch(request: web.Request, body=None) -> web.Response:
    """Add a juniper switch as data source

    Add switch Datasource

    :param body: Add a cisco switch as datasource
    :type body: dict | bytes

    """
    body = JuniperSwitchDataSourceRequest.from_dict(body)
    return web.Response(status=200)


async def add_nsxv_manager_datasource(request: web.Request, body=None) -> web.Response:
    """Create a nsx-v manager data source

    Add a nsx-v manager data source

    :param body: 
    :type body: dict | bytes

    """
    body = NSXVManagerDataSourceRequest.from_dict(body)
    return web.Response(status=200)


async def add_panorama_firewall(request: web.Request, body=None) -> web.Response:
    """Create panorama firewall data source

    Add panorama firewall as data source

    :param body: Add a panorama firewall as datasource
    :type body: dict | bytes

    """
    body = PanFirewallDataSourceRequest.from_dict(body)
    return web.Response(status=200)


async def add_ucs_manager(request: web.Request, body=None) -> web.Response:
    """Create an ucs manager data source

    Add an ucs manager as data source

    :param body: 
    :type body: dict | bytes

    """
    body = UCSManagerDataSourceRequest.from_dict(body)
    return web.Response(status=200)


async def add_vcenter_datasource(request: web.Request, body) -> web.Response:
    """Create a vCenter data source

    Add a vcenter data source. User must provide one of ip or fqdn field in the request body. Appropriate proxy id is retrieved from infra/nodes URL to select the proxy node.

    :param body: VCenter Credentials
    :type body: dict | bytes

    """
    body = VCenterDataSourceRequest.from_dict(body)
    return web.Response(status=200)


async def delete_arista_switch(request: web.Request, id) -> web.Response:
    """Delete an arista switch data source

    Delete an arista switch data source

    :param id: entity id
    :type id: str

    """
    return web.Response(status=200)


async def delete_brocade_switch(request: web.Request, id) -> web.Response:
    """Delete a brocade switch data source

    Delete a brocade switch data source

    :param id: entity id
    :type id: str

    """
    return web.Response(status=200)


async def delete_checkpoint_firewall(request: web.Request, id) -> web.Response:
    """Delete a checkpoint firewall data source

    Delete a checkpoint firewall data source

    :param id: entity id
    :type id: str

    """
    return web.Response(status=200)


async def delete_cisco_switch(request: web.Request, id) -> web.Response:
    """Delete a cisco switch data source

    Delete a cisco switch data source

    :param id: entity id
    :type id: str

    """
    return web.Response(status=200)


async def delete_dell_switch(request: web.Request, id) -> web.Response:
    """Delete a dell switch data source

    Delete a data source

    :param id: entity id
    :type id: str

    """
    return web.Response(status=200)


async def delete_hpov_manager(request: web.Request, id) -> web.Response:
    """Delete a hp oneview data source

    Delete a hp oneview data source

    :param id: entity id
    :type id: str

    """
    return web.Response(status=200)


async def delete_hpvc_manager(request: web.Request, id) -> web.Response:
    """Delete a hpvc manager data source

    Delete a hpvc manager data source

    :param id: entity id
    :type id: str

    """
    return web.Response(status=200)


async def delete_juniper_switch(request: web.Request, id) -> web.Response:
    """Delete a juniper switch data source

    Delete a juniper switch data source

    :param id: entity id
    :type id: str

    """
    return web.Response(status=200)


async def delete_nsxv_manager(request: web.Request, id) -> web.Response:
    """Delete a nsx-v manager data source

    Delete a nsx-v manager data source

    :param id: entity id
    :type id: str

    """
    return web.Response(status=200)


async def delete_panorama_firewall(request: web.Request, id) -> web.Response:
    """Delete a panorama firewall data source

    Delete a panorama firewall data source

    :param id: entity id
    :type id: str

    """
    return web.Response(status=200)


async def delete_ucs_manager(request: web.Request, id) -> web.Response:
    """Delete an ucs manager data source

    Delete an ucs manager data source

    :param id: entity id
    :type id: str

    """
    return web.Response(status=200)


async def delete_vcenter(request: web.Request, id) -> web.Response:
    """Delete a vCenter data source

    Delete a data source

    :param id: entity id
    :type id: str

    """
    return web.Response(status=200)


async def disable_arista_switch(request: web.Request, id) -> web.Response:
    """Disable an arista switch data source

    Disable an arista switch data source

    :param id: entity id
    :type id: str

    """
    return web.Response(status=200)


async def disable_brocade_switch(request: web.Request, id) -> web.Response:
    """Disable a brocade switch data source

    

    :param id: entity id
    :type id: str

    """
    return web.Response(status=200)


async def disable_checkpoint_firewall(request: web.Request, id) -> web.Response:
    """Disable a checkpoint firewall data source

    Disable a checkpoint firewall data source

    :param id: entity id
    :type id: str

    """
    return web.Response(status=200)


async def disable_cisco_switch(request: web.Request, id) -> web.Response:
    """Disable a cisco switch data source

    Disable a cisco switch data source

    :param id: entity id
    :type id: str

    """
    return web.Response(status=200)


async def disable_dell_switch(request: web.Request, id) -> web.Response:
    """Disable a dell switch data source

    Disable a dell switch data source

    :param id: entity id
    :type id: str

    """
    return web.Response(status=200)


async def disable_hpov_manager(request: web.Request, id) -> web.Response:
    """Disable a hp oneview data source

    Disable a hp oneview data source

    :param id: entity id
    :type id: str

    """
    return web.Response(status=200)


async def disable_hpvc_manager(request: web.Request, id) -> web.Response:
    """Disable a hpvc manager data source

    Disable a hpvc manager data source

    :param id: entity id
    :type id: str

    """
    return web.Response(status=200)


async def disable_juniper_switch(request: web.Request, id) -> web.Response:
    """Disable a juniper switch data source

    Disable a juniper switch data source

    :param id: entity id
    :type id: str

    """
    return web.Response(status=200)


async def disable_nsxv_manager(request: web.Request, id) -> web.Response:
    """Disable a nsx-v manager data source

    Disable a nsx-v manager data source

    :param id: entity id
    :type id: str

    """
    return web.Response(status=200)


async def disable_panorama_firewall(request: web.Request, id) -> web.Response:
    """Disable a panorama firewall data source

    Disable a panorama firewall data source

    :param id: entity id
    :type id: str

    """
    return web.Response(status=200)


async def disable_ucs_manager(request: web.Request, id) -> web.Response:
    """Disable an ucs manager data source

    Disable an ucs manager data source

    :param id: entity id
    :type id: str

    """
    return web.Response(status=200)


async def disable_vcenter(request: web.Request, id) -> web.Response:
    """Disable a vCenter data source

    Disable a vCenter data source

    :param id: entity id
    :type id: str

    """
    return web.Response(status=200)


async def enable_arista_switch(request: web.Request, id) -> web.Response:
    """Enable an arista switch data source

    Enable an arista switch data source

    :param id: entity id
    :type id: str

    """
    return web.Response(status=200)


async def enable_brocade_switch(request: web.Request, id) -> web.Response:
    """Enable a brocade switch data source

    

    :param id: entity id
    :type id: str

    """
    return web.Response(status=200)


async def enable_checkpoint_firewall(request: web.Request, id) -> web.Response:
    """Enable a checkpoint firewall data source

    Enable a checkpoint firewall data source

    :param id: entity id
    :type id: str

    """
    return web.Response(status=200)


async def enable_cisco_switch(request: web.Request, id) -> web.Response:
    """Enable a cisco switch data source

    Enable a cisco switch data source

    :param id: entity id
    :type id: str

    """
    return web.Response(status=200)


async def enable_dell_switch(request: web.Request, id) -> web.Response:
    """Enable a dell switch data source

    Enable a dell switch data source

    :param id: entity id
    :type id: str

    """
    return web.Response(status=200)


async def enable_hpov_manager(request: web.Request, id) -> web.Response:
    """Enable a hp oneview data source

    Enable a hp oneview data source

    :param id: entity id
    :type id: str

    """
    return web.Response(status=200)


async def enable_hpvc_manager(request: web.Request, id) -> web.Response:
    """Enable a hpvc manager data source

    Enable a hpvc manager data source

    :param id: entity id
    :type id: str

    """
    return web.Response(status=200)


async def enable_juniper_switch(request: web.Request, id) -> web.Response:
    """Enable a juniper switch data source

    Enable a juniper switch data source

    :param id: entity id
    :type id: str

    """
    return web.Response(status=200)


async def enable_nsxv_manager(request: web.Request, id) -> web.Response:
    """Enable a nsx-v manager data source

    Enable a nsx-v manager data source

    :param id: entity id
    :type id: str

    """
    return web.Response(status=200)


async def enable_panorama_firewall(request: web.Request, id) -> web.Response:
    """Enable a panorama firewall data source

    Enable a panorama firewall data source

    :param id: entity id
    :type id: str

    """
    return web.Response(status=200)


async def enable_ucs_manager(request: web.Request, id) -> web.Response:
    """Enable an ucs manager data source

    Enable an ucs manager data source

    :param id: entity id
    :type id: str

    """
    return web.Response(status=200)


async def enable_vcenter(request: web.Request, id) -> web.Response:
    """Enable a vCenter data source

    Enable a vCenter data source

    :param id: entity id
    :type id: str

    """
    return web.Response(status=200)


async def get_arista_switch(request: web.Request, id) -> web.Response:
    """Show arista switch data source details

    Show arista switch data source details

    :param id: entity id
    :type id: str

    """
    return web.Response(status=200)


async def get_arista_switch_snmp_config(request: web.Request, id) -> web.Response:
    """Show snmp config for arista switch data source

    Show snmp config for arista switch data source

    :param id: entity id
    :type id: str

    """
    return web.Response(status=200)


async def get_brocade_switch(request: web.Request, id) -> web.Response:
    """Show brocade switch data source details

    Show brocade switch data source details

    :param id: entity id
    :type id: str

    """
    return web.Response(status=200)


async def get_brocade_switch_snmp_config(request: web.Request, id) -> web.Response:
    """Show snmp config for brocade switch data source

    Show snmp config for brocade switch data source

    :param id: entity id
    :type id: str

    """
    return web.Response(status=200)


async def get_checkpoint_firewall(request: web.Request, id) -> web.Response:
    """Show checkpoint firewall data source details

    Show checkpoint firewall data source details

    :param id: entity id
    :type id: str

    """
    return web.Response(status=200)


async def get_cisco_switch(request: web.Request, id) -> web.Response:
    """Show cisco switch data source details

    Show cisco switch data source details

    :param id: entity id
    :type id: str

    """
    return web.Response(status=200)


async def get_cisco_switch_snmp_config(request: web.Request, id) -> web.Response:
    """Show snmp config for cisco switch data source

    Show snmp config for cisco switch data source

    :param id: entity id
    :type id: str

    """
    return web.Response(status=200)


async def get_dell_switch(request: web.Request, id) -> web.Response:
    """Show dell switch data source details

    Get a dell switch data source details

    :param id: entity id
    :type id: str

    """
    return web.Response(status=200)


async def get_dell_switch_snmp_config(request: web.Request, id) -> web.Response:
    """Show snmp config for dell switch data source

    Show snmp config for dell switch data source

    :param id: entity id
    :type id: str

    """
    return web.Response(status=200)


async def get_hpov_manager(request: web.Request, id) -> web.Response:
    """Show hp oneview data source details

    Show hp oneview data source details

    :param id: entity id
    :type id: str

    """
    return web.Response(status=200)


async def get_hpvc_manager(request: web.Request, id) -> web.Response:
    """Show hpvc data source details

    Show hpvc data source details

    :param id: entity id
    :type id: str

    """
    return web.Response(status=200)


async def get_juniper_switch(request: web.Request, id) -> web.Response:
    """Show juniper switch data source details

    Show juniper switch data source details

    :param id: entity id
    :type id: str

    """
    return web.Response(status=200)


async def get_juniper_switch_snmp_config(request: web.Request, id) -> web.Response:
    """Show snmp config for juniper switch data source

    Show snmp config for juniper switch data source

    :param id: entity id
    :type id: str

    """
    return web.Response(status=200)


async def get_nsxv_controller_cluster(request: web.Request, id) -> web.Response:
    """Show nsx controller-cluster details

    Show nsx controller-cluster details

    :param id: entity id
    :type id: str

    """
    return web.Response(status=200)


async def get_nsxv_manager(request: web.Request, id) -> web.Response:
    """Show nsx-v manager data source details

    Show nsx-v manager data source details

    :param id: entity id
    :type id: str

    """
    return web.Response(status=200)


async def get_panorama_firewall(request: web.Request, id) -> web.Response:
    """Show panorama firewall data source details

    Show panorama firewall data source details

    :param id: entity id
    :type id: str

    """
    return web.Response(status=200)


async def get_ucs_manager(request: web.Request, id) -> web.Response:
    """Show ucs manager data source details

    Show ucs manager data source details

    :param id: entity id
    :type id: str

    """
    return web.Response(status=200)


async def get_ucs_snmp_config(request: web.Request, id) -> web.Response:
    """Show snmp config for ucs fabric interconnects

    Show snmp config for ucs fabric interconnects

    :param id: entity id
    :type id: str

    """
    return web.Response(status=200)


async def get_vcenter(request: web.Request, id) -> web.Response:
    """Show vCenter data source details

    Show vCenter data source details

    :param id: entity id
    :type id: str

    """
    return web.Response(status=200)


async def list_arista_switches(request: web.Request, ) -> web.Response:
    """List arista switch data sources

    List arista switch data sources


    """
    return web.Response(status=200)


async def list_brocade_switches(request: web.Request, ) -> web.Response:
    """List brocade switch data sources

    List brocade switch data sources


    """
    return web.Response(status=200)


async def list_checkpoint_firewalls(request: web.Request, ) -> web.Response:
    """List checkpoint firewall data sources

    List checkpoint firewall data sources


    """
    return web.Response(status=200)


async def list_cisco_switches(request: web.Request, ) -> web.Response:
    """List cisco switch data sources

    List cisco switch data sources


    """
    return web.Response(status=200)


async def list_dell_switches(request: web.Request, ) -> web.Response:
    """List dell switch data sources

    List dell switch data sources


    """
    return web.Response(status=200)


async def list_hpov_managers(request: web.Request, ) -> web.Response:
    """List hp oneview manager data sources

    List hp oneview manager data sources


    """
    return web.Response(status=200)


async def list_hpvc_managers(request: web.Request, ) -> web.Response:
    """List hpvc manager data sources

    List hpvc manager data sources


    """
    return web.Response(status=200)


async def list_juniper_switches(request: web.Request, ) -> web.Response:
    """List juniper switch data sources

    List juniper switch data sources


    """
    return web.Response(status=200)


async def list_nsxv_managers(request: web.Request, ) -> web.Response:
    """List nsx-v manager data sources

    List nsx-v manager data sources


    """
    return web.Response(status=200)


async def list_panorama_firewalls(request: web.Request, ) -> web.Response:
    """List panorama firewall data sources

    List panorama firewall data sources


    """
    return web.Response(status=200)


async def list_ucs_managers(request: web.Request, ) -> web.Response:
    """List ucs manager data sources

    List ucs manager data sources


    """
    return web.Response(status=200)


async def list_vcenters(request: web.Request, ) -> web.Response:
    """List vCenter data sources

    List vCenter data sources


    """
    return web.Response(status=200)


async def update_arista_switch(request: web.Request, id, body=None) -> web.Response:
    """Update an arista switch data source

    Update an switch data source

    :param id: entity id
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = AristaSwitchDataSource.from_dict(body)
    return web.Response(status=200)


async def update_arista_switch_snmp_config(request: web.Request, id, body=None) -> web.Response:
    """Update snmp config for arista switch data source

    Update snmp config for arista switch data source

    :param id: entity id
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = SNMPConfig.from_dict(body)
    return web.Response(status=200)


async def update_brocade_switch(request: web.Request, id, body=None) -> web.Response:
    """Update a brocade switch data source

    Update a brocade switch data source. Only credentials, nickname and notes can be updated.

    :param id: entity id
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = BrocadeSwitchDataSource.from_dict(body)
    return web.Response(status=200)


async def update_brocade_switch_snmp_config(request: web.Request, id, body=None) -> web.Response:
    """Update snmp config for brocade switch data source

    Update snmp config for brocade switch data source

    :param id: entity id
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = SNMPConfig.from_dict(body)
    return web.Response(status=200)


async def update_checkpoint_firewall(request: web.Request, id, body=None) -> web.Response:
    """Update a checkpoint firewall data source

    Update a checkpoint firewall data source

    :param id: entity id
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CheckpointFirewallDataSource.from_dict(body)
    return web.Response(status=200)


async def update_cisco_switch(request: web.Request, id, body=None) -> web.Response:
    """Update a cisco switch data source

    Update a cisco switch data source. Only credentials, nickname and notes can be updated.

    :param id: entity id
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CiscoSwitchDataSource.from_dict(body)
    return web.Response(status=200)


async def update_cisco_switch_snmp_config(request: web.Request, id, body=None) -> web.Response:
    """Update snmp config for cisco switch data source

    Update snmp config for cisco switch data source

    :param id: entity id
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = SNMPConfig.from_dict(body)
    return web.Response(status=200)


async def update_dell_switch(request: web.Request, id, body=None) -> web.Response:
    """Update a dell switch data source

    Update a dell switch data source. Only credentials, nickname and notes can be updated

    :param id: entity id
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = DellSwitchDataSource.from_dict(body)
    return web.Response(status=200)


async def update_dell_switch_snmp_config(request: web.Request, id, body=None) -> web.Response:
    """Update snmp config for dell switch data source

    Update snmp config for dell switch data source

    :param id: entity id
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = SNMPConfig.from_dict(body)
    return web.Response(status=200)


async def update_hpov_manager(request: web.Request, id, body=None) -> web.Response:
    """Update a hp oneview data source

    Update a hp oneview data source

    :param id: entity id
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = HPOneViewManagerDataSource.from_dict(body)
    return web.Response(status=200)


async def update_hpvc_manager(request: web.Request, id, body=None) -> web.Response:
    """Update a hpvc manager data source

    Update a hpvc manager data source

    :param id: entity id
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = HPVCManagerDataSource.from_dict(body)
    return web.Response(status=200)


async def update_juniper_switch(request: web.Request, id, body=None) -> web.Response:
    """Update a juniper switch data source

    Update a juniper switch data source

    :param id: entity id
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = JuniperSwitchDataSource.from_dict(body)
    return web.Response(status=200)


async def update_juniper_switch_snmp_config(request: web.Request, id, body=None) -> web.Response:
    """Update snmp config for a juniper switch data source

    Update snmp config for a juniper switch data source

    :param id: entity id
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = SNMPConfig.from_dict(body)
    return web.Response(status=200)


async def update_nsxv_controller_cluster(request: web.Request, id, body=None) -> web.Response:
    """Update nsx controller-cluster details

    Update nsx controller-cluster details

    :param id: entity id
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = NSXControllerDataCollection.from_dict(body)
    return web.Response(status=200)


async def update_nsxv_manager(request: web.Request, id, body=None) -> web.Response:
    """Update a nsx-v manager data source

    Update a nsx-v manager data source

    :param id: entity id
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = NSXVManagerDataSource.from_dict(body)
    return web.Response(status=200)


async def update_panorama_firewall(request: web.Request, id, body=None) -> web.Response:
    """Update a panorama firewall data source

    Update a panorama firewall data source

    :param id: entity id
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PanFirewallDataSource.from_dict(body)
    return web.Response(status=200)


async def update_ucs_manager(request: web.Request, id, body=None) -> web.Response:
    """Update an ucs manager data source

    Update an ucs manager data source

    :param id: entity id
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UCSManagerDataSource.from_dict(body)
    return web.Response(status=200)


async def update_ucs_snmp_config(request: web.Request, id, body=None) -> web.Response:
    """Update snmp config for ucs fabric interconnects

    Update snmp config for ucs fabric interconnects

    :param id: entity id
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = SNMPConfig.from_dict(body)
    return web.Response(status=200)


async def update_vcenter(request: web.Request, id, body=None) -> web.Response:
    """Update a vCenter data source.

    Update a vcenter data source. Only nickname, notes and credentials can be updated.

    :param id: entity id
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = VCenterDataSource.from_dict(body)
    return web.Response(status=200)
