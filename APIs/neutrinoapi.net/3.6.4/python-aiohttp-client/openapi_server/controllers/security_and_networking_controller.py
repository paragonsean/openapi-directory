from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import APIError
from openapi_server.models.domain_lookup_response import DomainLookupResponse
from openapi_server.models.email_verify_response import EmailVerifyResponse
from openapi_server.models.host_reputation_response import HostReputationResponse
from openapi_server.models.ip_blocklist_response import IPBlocklistResponse
from openapi_server.models.ip_probe_response import IPProbeResponse
from openapi_server import util


async def domain_lookup(request: web.Request, host, live=None) -> web.Response:
    """Domain Lookup

    Retrieve domain name details and detect potentially malicious or dangerous domains

    :param host: A domain name, hostname, FQDN, URL, HTML link or email address to lookup
    :type host: str
    :param live: For domains that we have never seen before then perform various live checks and realtime reconnaissance. &lt;br&gt;NOTE: this option may add additional non-deterministic delay to the request, if you require consistently fast API response times or just want to check our domain blocklists then you can disable this option
    :type live: bool

    """
    return web.Response(status=200)


async def email_verify(request: web.Request, email, fix_typos=None) -> web.Response:
    """Email Verify

    SMTP based email address verification

    :param email: An email address
    :type email: str
    :param fix_typos: Automatically attempt to fix typos in the address
    :type fix_typos: bool

    """
    return web.Response(status=200)


async def host_reputation(request: web.Request, host, list_rating=None, zones=None) -> web.Response:
    """Host Reputation

    Check the reputation of an IP address, domain name or URL against a comprehensive list of blacklists and blocklists

    :param host: An IP address, domain name, FQDN or URL. &lt;br&gt;If you supply a domain/URL it will be checked against the URI DNSBL lists
    :type host: str
    :param list_rating: Only check lists with this rating or better
    :type list_rating: int
    :param zones: Only check these DNSBL zones/hosts. Multiple zones can be supplied as comma-separated values
    :type zones: str

    """
    return web.Response(status=200)


async def i_p_blocklist(request: web.Request, ip, vpn_lookup=None) -> web.Response:
    """IP Blocklist

    The IP Blocklist API will detect potentially malicious or dangerous IP addresses

    :param ip: An IPv4 or IPv6 address. Accepts standard IP notation (with or without port number), CIDR notation and IPv6 compressed notation. If multiple IPs are passed using comma-separated values the first non-bogon address on the list will be checked
    :type ip: str
    :param vpn_lookup: Include public VPN provider IP addresses. &lt;br&gt;&lt;b&gt;NOTE&lt;/b&gt;: For more advanced VPN detection including the ability to identify private and stealth VPNs use the &lt;a href&#x3D;\&quot;https://www.neutrinoapi.com/api/ip-probe/\&quot;&gt;IP Probe API&lt;/a&gt;
    :type vpn_lookup: bool

    """
    return web.Response(status=200)


async def i_p_blocklist_download(request: web.Request, format=None, include_vpn=None, cidr=None, ip6=None) -> web.Response:
    """IP Blocklist Download

    This API is a direct feed to our IP blocklist data

    :param format: The data format. Can be either CSV or TXT
    :type format: str
    :param include_vpn: Include public VPN provider addresses, this option is only available for Tier 3 or higher accounts. Adds any IPs which are solely listed as VPN providers, IPs that are listed on multiple sensors will still be included without enabling this option. &lt;br&gt;&lt;b&gt;WARNING&lt;/b&gt;: This adds at least an additional 8 million IP addresses to the download if not using CIDR notation
    :type include_vpn: bool
    :param cidr: Output IPs using CIDR notation. This option should be preferred but is off by default for backwards compatibility
    :type cidr: bool
    :param ip6: Output the IPv6 version of the blocklist, the default is to output IPv4 only. Note that this option enables CIDR notation too as this is the only notation currently supported for IPv6
    :type ip6: bool

    """
    return web.Response(status=200)


async def i_p_probe(request: web.Request, ip) -> web.Response:
    """IP Probe

    Execute a realtime network probe against an IPv4 or IPv6 address

    :param ip: IPv4 or IPv6 address
    :type ip: str

    """
    return web.Response(status=200)
