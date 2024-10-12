from typing import List, Dict
from aiohttp import web

from openapi_server.models.async_request_status import AsyncRequestStatus
from openapi_server.models.available_version_info import AvailableVersionInfo
from openapi_server.models.boolean_response import BooleanResponse
from openapi_server.models.cluster_api_version import ClusterApiVersion
from openapi_server.models.cluster_certificate import ClusterCertificate
from openapi_server.models.cluster_info import ClusterInfo
from openapi_server.models.cluster_update import ClusterUpdate
from openapi_server.models.cluster_version import ClusterVersion
from openapi_server.models.community_user_credentials import CommunityUserCredentials
from openapi_server.models.cors_configuration import CorsConfiguration
from openapi_server.models.cors_configuration_patch import CorsConfigurationPatch
from openapi_server.models.encryption_status import EncryptionStatus
from openapi_server.models.event_notification import EventNotification
from openapi_server.models.fips_status import FipsStatus
from openapi_server.models.fips_status_patch import FipsStatusPatch
from openapi_server.models.kmip_client_configuration import KmipClientConfiguration
from openapi_server.models.kmip_client_detail import KmipClientDetail
from openapi_server.models.kmip_server_configuration import KmipServerConfiguration
from openapi_server.models.kmip_server_detail import KmipServerDetail
from openapi_server.models.manual_discovery_node_info import ManualDiscoveryNodeInfo
from openapi_server.models.manual_discovery_node_ipv4_info import ManualDiscoveryNodeIpv4Info
from openapi_server.models.node_hostname_info import NodeHostnameInfo
from openapi_server.models.node_hostname_info_list_response import NodeHostnameInfoListResponse
from openapi_server.models.node_id import NodeId
from openapi_server.models.password_requirements_patch_request import PasswordRequirementsPatchRequest
from openapi_server.models.password_requirements_summary import PasswordRequirementsSummary
from openapi_server.models.precheck_status_response import PrecheckStatusResponse
from openapi_server.models.rubrik_mib_file_download_link import RubrikMibFileDownloadLink
from openapi_server.models.stage_cdm_software_info import StageCdmSoftwareInfo
from openapi_server.models.syslog_export_rule_full import SyslogExportRuleFull
from openapi_server.models.syslog_export_rule_partial import SyslogExportRulePartial
from openapi_server.models.syslog_export_rule_summary import SyslogExportRuleSummary
from openapi_server.models.syslog_export_rule_summary_list_response import SyslogExportRuleSummaryListResponse
from openapi_server.models.syslog_msg_mib_file_download_link import SyslogMsgMibFileDownloadLink
from openapi_server.models.syslog_server_test_result import SyslogServerTestResult
from openapi_server.models.syslog_tc_mib_file_download_link import SyslogTcMibFileDownloadLink
from openapi_server.models.totp_global_setting import TotpGlobalSetting
from openapi_server.models.totp_global_setting_update import TotpGlobalSettingUpdate
from openapi_server.models.truststore_payload import TruststorePayload
from openapi_server.models.truststore_summary_list_response import TruststoreSummaryListResponse
from openapi_server.models.web_server_certificate_payload import WebServerCertificatePayload
from openapi_server.models.web_server_certificate_summary import WebServerCertificateSummary
from openapi_server import util


async def add_kmip_server(request: web.Request, id, body) -> web.Response:
    """Add a KMIP server

    Add the specified KMIP server to the set of active KMIP servers.

    :param id: ID assigned to a Rubrik cluster. Use *me* to refer to the Rubrik cluster that is hosting the current API session.
    :type id: str
    :param body: Object containing the configuration details for a KMIP server.
    :type body: dict | bytes

    """
    body = KmipServerConfiguration.from_dict(body)
    return web.Response(status=200)


async def add_syslog_export_rule(request: web.Request, body) -> web.Response:
    """Add a new syslog export rule

    Adds a new rule specifying where to export the specified syslog information. 

    :param body: Syslog export rule.
    :type body: dict | bytes

    """
    body = SyslogExportRuleFull.from_dict(body)
    return web.Response(status=200)


async def available_version(request: web.Request, id, filter_version=None, fetch_links=None, source_version=None, ignore_local=None, ignore_remote=None, ignore_downloading=None, download_job_instance_id=None, filter_upgradable=None, show_all=None) -> web.Response:
    """Retrieve CDM versions available for upgrade

    Retrieve a list of Rubrik CDM versions available to upgrade the Rubrik cluster.

    :param id: The ID of the Rubrik cluster. To query the local cluster, use *me*.
    :type id: str
    :param filter_version: A string that filters the results based on the prefix. For example, the string \&quot;5.1\&quot; filters all releases in the 5.1 family. If more than one result is desired then this parameter can be used in conjunction with the &#x60;show_all&#x60; parameter.
    :type filter_version: str
    :param fetch_links: Include a download URL for the single version passed in the &#39;filter_version&#39; parameter. A link response will not be provided if the chosen version is locally available, or if &#39;filter_version&#39; is not specified. 
    :type fetch_links: bool
    :param source_version: The source version of Rubrik CDM used for the upgradeability check if &#39;filter_upgradable&#39; if specified. If &#39;filter_upgradable&#39; is not specified, this parameter is ignored. 
    :type source_version: str
    :param ignore_local: If specified, ignore locally available versions.
    :type ignore_local: bool
    :param ignore_remote: If specified, ignore versions available in the Rubrik remote central repository. 
    :type ignore_remote: bool
    :param ignore_downloading: If specified, ignore versions currently being downloaded.
    :type ignore_downloading: bool
    :param download_job_instance_id: If specified, filter results for downloading versions to the provided job instance ID. 
    :type download_job_instance_id: str
    :param filter_upgradable: When this parameter is set, the query only returns versions of the Rubrik CDM that can be upgraded to from the version specified in the &#39;source_version&#39; parameter. If &#39;source_version&#39; is not specified, we use the cluster version as the source_version. 
    :type filter_upgradable: bool
    :param show_all: When this parameter is set, the query shows all patch releases including releases with a newer version released in the same family. When set to false, the query returns only the latest version from each release family. 
    :type show_all: bool

    """
    return web.Response(status=200)


async def change_cluster_node_hostnames(request: web.Request, id, body) -> web.Response:
    """Change hostname for nodes in a Rubrik cluster

    Change hostnames for multiple nodes at a time, for a specified Rubrik cluster. 

    :param id: ID of the Rubrik cluster or *me* for self.
    :type id: str
    :param body: Node ID to hostname mapping.
    :type body: list | bytes

    """
    body = [NodeHostnameInfo.from_dict(d) for d in body]
    return web.Response(status=200)


async def delete_kmip_server(request: web.Request, id, server_address) -> web.Response:
    """Remove the specified KMIP server

    Remove the server with the specified server address from the set of active KMIP servers.

    :param id: ID assigned to a Rubrik cluster. Use *me* to refer to the Rubrik cluster that is hosting the current API session.
    :type id: str
    :param server_address: IPv4 address or FQDN (fully qualified domain name) of the KMIP server.
    :type server_address: str

    """
    return web.Response(status=200)


async def delete_syslog_export_rule(request: web.Request, id) -> web.Response:
    """Delete the specified syslog export rule

    Delete the syslog export rule specified by the given id.

    :param id: The ID of the syslog export rule.
    :type id: str

    """
    return web.Response(status=200)


async def get_async_request_status_for_upgrade(request: web.Request, id, request_id) -> web.Response:
    """Get asynchronous request details

    Get asynchronous request details for an upgrade request.

    :param id: ID of the Rubrik cluster or *me* for self.
    :type id: str
    :param request_id: ID of the request.
    :type request_id: str

    """
    return web.Response(status=200)


async def get_cluster_api_version(request: web.Request, id) -> web.Response:
    """Get cluster REST API version

    Retrieves software version of the Rubrik cluster.

    :param id: ID of the Rubrik cluster or *me* for self.
    :type id: str

    """
    return web.Response(status=200)


async def get_cluster_certificate(request: web.Request, id) -> web.Response:
    """Get the cluster certificate

    Returns the cluster certificate.

    :param id: ID of the Rubrik cluster or *me* for self.
    :type id: str

    """
    return web.Response(status=200)


async def get_cluster_node_hostnames(request: web.Request, id) -> web.Response:
    """Get the node ID to hostname mapping for all the nodes in a Rubrik cluster 

    Retrieve the ID to hostname mapping for all the nodes that belong to a specified Rubrik cluster. 

    :param id: ID of the Rubrik cluster or *me* for self.
    :type id: str

    """
    return web.Response(status=200)


async def get_cluster_node_ids(request: web.Request, id) -> web.Response:
    """Get the name of the nodes in the cluster

    Retrieve the list of node IDs for the nodes in this Rubrik CDM cluster.

    :param id: ID of the Rubrik cluster or *me* for self.
    :type id: str

    """
    return web.Response(status=200)


async def get_cluster_version(request: web.Request, id) -> web.Response:
    """Get cluster software version

    Retrieves software version of the Rubrik cluster.

    :param id: ID of the Rubrik cluster or *me* for self.
    :type id: str

    """
    return web.Response(status=200)


async def get_cors_configuration(request: web.Request, id) -> web.Response:
    """Get CORS configuration

    Get the current CORS support configuration for a web server.

    :param id: ID of the Rubrik cluster or *me* for self.
    :type id: str

    """
    return web.Response(status=200)


async def get_encryption_status(request: web.Request, id) -> web.Response:
    """Get encryption at rest status

    Get the current encryption at rest status of the cluster.

    :param id: ID of the Rubrik cluster or *me* for self.
    :type id: str

    """
    return web.Response(status=200)


async def get_fips(request: web.Request, id) -> web.Response:
    """Get FIPS enablement status

    Returns the current status of FIPS on the specified cluster. When the status is true, FIPS is enabled.

    :param id: ID of the Rubrik cluster or *me* for self.
    :type id: str

    """
    return web.Response(status=200)


async def get_kmip_client(request: web.Request, id) -> web.Response:
    """Get the KMIP client configuration

    Return the currently configured KMIP client information. The response object contains empty fields when KMIP is not configured.

    :param id: ID assigned to a Rubrik cluster. Use *me* to refer to the Rubrik cluster that is hosting the current API session.
    :type id: str

    """
    return web.Response(status=200)


async def get_kmip_server(request: web.Request, id, server_address=None) -> web.Response:
    """Get KMIP server information

    Returns the KMIP server information for the specified server address. When no server address is specified, this call returns information on all active KMIP servers. The response array is empty when KMIP is not configured or when the server address cannot be found.

    :param id: ID assigned to a Rubrik cluster. Use *me* to refer to the Rubrik cluster that is hosting the current API session.
    :type id: str
    :param server_address: The address of the KMIP server.
    :type server_address: str

    """
    return web.Response(status=200)


async def get_periodic_upgrade_prechecks_status(request: web.Request, id, fetch_next_run_info=None) -> web.Response:
    """Get the result of the latest run of the upgrade prechecks

    Get the result of the latest run of the upgrade prechecks. 

    :param id: ID of the Rubrik cluster or *me* for self.
    :type id: str
    :param fetch_next_run_info: If specified, fetch information corresponding to next upgrade prechecks job instance. If an upgrade prechecks job instance is currently running, results corresponding to it are returned. 
    :type fetch_next_run_info: bool

    """
    return web.Response(status=200)


async def get_public_cluster_info(request: web.Request, id) -> web.Response:
    """Get cluster details

    Retrieve public information about the Rubrik cluster.

    :param id: ID of the Rubrik cluster or *me* for self.
    :type id: str

    """
    return web.Response(status=200)


async def get_rubrik_snmp_mib_download_link(request: web.Request, id) -> web.Response:
    """Get the link for Rubrik SNMP MIB file

    Retrieve the download link for the Rubrik SNMP MIB file. The retrieval is a synchronous operation.

    :param id: ID of the Rubrik cluster or *me* for self.
    :type id: str

    """
    return web.Response(status=200)


async def get_syslog_export_rule(request: web.Request, id) -> web.Response:
    """Get the specified syslog export rule

    Get the summary of the syslog export rule specified by the given id. 

    :param id: The ID of syslog export rule.
    :type id: str

    """
    return web.Response(status=200)


async def get_syslog_export_rules(request: web.Request, ) -> web.Response:
    """Get the configured syslog export rules

    Return the list of all configured syslog export rules.


    """
    return web.Response(status=200)


async def get_syslog_msg_snmp_mib_download_link(request: web.Request, id) -> web.Response:
    """Get the link for SYSLOG-MSG-MIB file

    Retrieve the download link for the SYSLOG-MSG-MIB file. The retrieval is a synchronous operation.

    :param id: ID of the Rubrik cluster or *me* for self.
    :type id: str

    """
    return web.Response(status=200)


async def get_syslog_tc_snmp_mib_download_link(request: web.Request, id) -> web.Response:
    """Get the link for SYSLOG-TC-MIB file

    Retrieve the download link for the SYSLOG-TC-MIB file. The retrieval is a synchronous operation.

    :param id: ID of the Rubrik cluster or *me* for self.
    :type id: str

    """
    return web.Response(status=200)


async def get_totp_global_setting(request: web.Request, id) -> web.Response:
    """Get global TOTP setting

    Returns TOTP global setting, including whether TOTP is enforced or not.

    :param id: ID assigned to a Rubrik cluster. Use *me* to refer to the Rubrik cluster that is hosting the current API session.
    :type id: str

    """
    return web.Response(status=200)


async def get_truststores(request: web.Request, id) -> web.Response:
    """Get summary of all truststores

    Get summary of all truststores.

    :param id: ID of the Rubrik cluster or *me* for self.
    :type id: str

    """
    return web.Response(status=200)


async def get_web_signed_certificate(request: web.Request, id) -> web.Response:
    """Get the signed certificate for Web server

    If the web server uses a signed certificate, fetch it.

    :param id: ID of the Rubrik cluster or *me* for self.
    :type id: str

    """
    return web.Response(status=200)


async def has_rubrik_support_portal_credentials(request: web.Request, id) -> web.Response:
    """Check credentials to the Rubrik support portal

    Check whether the specified Rubrik cluster has an existing set of credentials for the Rubrik support portal. 

    :param id: The ID of a Rubrik cluster, or use *me* for the Rubrik cluster that is hosting the current session. 
    :type id: str

    """
    return web.Response(status=200)


async def manual_discover(request: web.Request, id, body) -> web.Response:
    """Manually discover nodes

    Manually specifies mDNS discovery data. Output for this endpoint is identical to the output of the &#39;discover&#39; endpoint.

    :param id: ID of the Rubrik cluster or *me* for self.
    :type id: str
    :param body: Manual discovery input data.
    :type body: dict | bytes

    """
    body = ManualDiscoveryNodeInfo.from_dict(body)
    return web.Response(status=200)


async def manual_discover_ipv4(request: web.Request, id, body) -> web.Response:
    """Manually discover nodes over IPv4 address

    Manually specifies discovery data. This endpoint output is identical to the output of the &#39;discover&#39; endpoint.

    :param id: ID of the Rubrik cluster, or *me* for the current cluster.
    :type id: str
    :param body: Manual discovery input data.
    :type body: dict | bytes

    """
    body = ManualDiscoveryNodeIpv4Info.from_dict(body)
    return web.Response(status=200)


async def monitor_events(request: web.Request, event_notification_query) -> web.Response:
    """Get event notifications

    Gets notifications about events from a specified set of possible events. 

    :param event_notification_query: Specifies a list of events to monitor for notifications.
    :type event_notification_query: List[str]

    """
    return web.Response(status=200)


async def patch_password_requirements(request: web.Request, id, body) -> web.Response:
    """Set password requirements

    Update user password requirements for a cluster.

    :param id: ID of the Rubrik cluster or *me* for self.
    :type id: str
    :param body: Password requirements.
    :type body: dict | bytes

    """
    body = PasswordRequirementsPatchRequest.from_dict(body)
    return web.Response(status=200)


async def query_password_requirements(request: web.Request, id) -> web.Response:
    """Get password requirements

    Query user password requirements for a cluster.

    :param id: ID of the Rubrik cluster or *me* for self.
    :type id: str

    """
    return web.Response(status=200)


async def reset_web_signed_certificate(request: web.Request, id) -> web.Response:
    """Reset the signed certificate for Web server

    Resetting the customer-given certificate for each node&#39;s web server.

    :param id: ID of the Rubrik cluster or *me* for self.
    :type id: str

    """
    return web.Response(status=200)


async def run_periodic_upgrade_prechecks(request: web.Request, id) -> web.Response:
    """Start an on demand run of the prechecks

    Start an on demand run of the prechecks. 

    :param id: ID of the Rubrik cluster or *me* for self.
    :type id: str

    """
    return web.Response(status=200)


async def set_kmip_client(request: web.Request, id, body) -> web.Response:
    """Specify KMIP client credentials for nodes

    Specify KMIP client credentials for each of the Rubrik cluster nodes.

    :param id: ID assigned to a Rubrik cluster. Use *me* to refer to the Rubrik cluster that is hosting the current API session.
    :type id: str
    :param body: KMIP client configuration.
    :type body: dict | bytes

    """
    body = KmipClientConfiguration.from_dict(body)
    return web.Response(status=200)


async def set_truststore_certificate(request: web.Request, id, body) -> web.Response:
    """Set certificates for one or more truststores

    Setting the given certificate for each node&#39;s truststores.

    :param id: ID of the Rubrik cluster or *me* for self.
    :type id: str
    :param body: Request to update certificate for truststore.
    :type body: list | bytes

    """
    body = [TruststorePayload.from_dict(d) for d in body]
    return web.Response(status=200)


async def set_web_signed_certificate(request: web.Request, id, body) -> web.Response:
    """Set a signed certificate for Web server

    Setting the given certificate for each node&#39;s web server to use.

    :param id: ID of the Rubrik cluster or *me* for self.
    :type id: str
    :param body: Request to update certificate for web server.
    :type body: dict | bytes

    """
    body = WebServerCertificatePayload.from_dict(body)
    return web.Response(status=200)


async def stage_cdm_software(request: web.Request, id, body) -> web.Response:
    """Stage software on CDM for upgrade

    Stage software corresponding to a given CDM version on the cluster, in preparation for an upgrade.

    :param id: ID of the Rubrik cluster or *me* for self.
    :type id: str
    :param body: Information about the provided CDM software package.
    :type body: dict | bytes

    """
    body = StageCdmSoftwareInfo.from_dict(body)
    return web.Response(status=200)


async def test_syslog_export_rule(request: web.Request, body) -> web.Response:
    """Test the specified syslog export rule

    Send a test message using the syslog export rule specified by the given id. 

    :param body: Syslog export rule.
    :type body: dict | bytes

    """
    body = SyslogExportRuleFull.from_dict(body)
    return web.Response(status=200)


async def unset_truststore_certificate(request: web.Request, id, truststores) -> web.Response:
    """Remove certificate associated with specified truststore

    Remove certificate associated with specified truststore.

    :param id: ID of the Rubrik cluster or *me* for self.
    :type id: str
    :param truststores: Comma separated list of truststore types.
    :type truststores: List[str]

    """
    return web.Response(status=200)


async def update_cluster(request: web.Request, id, body) -> web.Response:
    """Change Rubrik cluster properties

    Change the properties of a specified Rubrik cluster. Changes to cluster name could take upto 10 minutes to be propagated to all nodes.

    :param id: ID of a Rubrik cluster object, or use *me* for the Rubrik cluster that is hosting the current API session.
    :type id: str
    :param body: Array that contains the changed information for the Rubrik cluster object.
    :type body: dict | bytes

    """
    body = ClusterUpdate.from_dict(body)
    return web.Response(status=200)


async def update_cors_configuration(request: web.Request, id, body) -> web.Response:
    """Update CORS configuration

    Update the CORS support configuration for a web server.

    :param id: ID of the Rubrik cluster or *me* for self.
    :type id: str
    :param body: CORS configuration.
    :type body: dict | bytes

    """
    body = CorsConfigurationPatch.from_dict(body)
    return web.Response(status=200)


async def update_fips(request: web.Request, id, body) -> web.Response:
    """Update FIPS enablement status

    Update the current FIPS enablement status for a cluster.

    :param id: ID of the Rubrik cluster or *me* for self.
    :type id: str
    :param body: Update FIPS enablement status.
    :type body: dict | bytes

    """
    body = FipsStatusPatch.from_dict(body)
    return web.Response(status=200)


async def update_rubrik_support_portal_credentials(request: web.Request, id, body) -> web.Response:
    """Update credentials to the Rubrik support portal

    Update credentials for the specified Rubrik cluster to connect to the Rubrik support portal. 

    :param id: The ID of a Rubrik cluster, or use *me* for the Rubrik cluster that is hosting the current session. 
    :type id: str
    :param body: The credentials used to connect to the Rubrik support portal. 
    :type body: dict | bytes

    """
    body = CommunityUserCredentials.from_dict(body)
    return web.Response(status=200)


async def update_syslog_export_rule(request: web.Request, id, body) -> web.Response:
    """Update the specified syslog export rule

    Update the syslog export rule specified by the given id.

    :param id: The ID of syslog export rule.
    :type id: str
    :param body: Syslog export rule.
    :type body: dict | bytes

    """
    body = SyslogExportRulePartial.from_dict(body)
    return web.Response(status=200)


async def update_totp_global_setting(request: web.Request, id, body) -> web.Response:
    """Update TOTP global setting

    Update TOTP global setting, including whether TOTP is enforced or not.

    :param id: ID assigned to a Rubrik cluster. Use *me* to refer to the Rubrik cluster that is hosting the current API session.
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = TotpGlobalSettingUpdate.from_dict(body)
    return web.Response(status=200)
