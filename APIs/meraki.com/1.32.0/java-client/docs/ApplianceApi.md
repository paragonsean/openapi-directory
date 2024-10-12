# ApplianceApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createDeviceApplianceVmxAuthenticationToken**](ApplianceApi.md#createDeviceApplianceVmxAuthenticationToken) | **POST** /devices/{serial}/appliance/vmx/authenticationToken | Generate a new vMX authentication token |
| [**createNetworkAppliancePrefixesDelegatedStatic**](ApplianceApi.md#createNetworkAppliancePrefixesDelegatedStatic) | **POST** /networks/{networkId}/appliance/prefixes/delegated/statics | Add a static delegated prefix from a network |
| [**createNetworkApplianceStaticRoute**](ApplianceApi.md#createNetworkApplianceStaticRoute) | **POST** /networks/{networkId}/appliance/staticRoutes | Add a static route for an MX or teleworker network |
| [**createNetworkApplianceTrafficShapingCustomPerformanceClass**](ApplianceApi.md#createNetworkApplianceTrafficShapingCustomPerformanceClass) | **POST** /networks/{networkId}/appliance/trafficShaping/customPerformanceClasses | Add a custom performance class for an MX network |
| [**createNetworkApplianceVlan**](ApplianceApi.md#createNetworkApplianceVlan) | **POST** /networks/{networkId}/appliance/vlans | Add a VLAN |
| [**deleteNetworkAppliancePrefixesDelegatedStatic**](ApplianceApi.md#deleteNetworkAppliancePrefixesDelegatedStatic) | **DELETE** /networks/{networkId}/appliance/prefixes/delegated/statics/{staticDelegatedPrefixId} | Delete a static delegated prefix from a network |
| [**deleteNetworkApplianceStaticRoute**](ApplianceApi.md#deleteNetworkApplianceStaticRoute) | **DELETE** /networks/{networkId}/appliance/staticRoutes/{staticRouteId} | Delete a static route from an MX or teleworker network |
| [**deleteNetworkApplianceTrafficShapingCustomPerformanceClass**](ApplianceApi.md#deleteNetworkApplianceTrafficShapingCustomPerformanceClass) | **DELETE** /networks/{networkId}/appliance/trafficShaping/customPerformanceClasses/{customPerformanceClassId} | Delete a custom performance class from an MX network |
| [**deleteNetworkApplianceVlan**](ApplianceApi.md#deleteNetworkApplianceVlan) | **DELETE** /networks/{networkId}/appliance/vlans/{vlanId} | Delete a VLAN from a network |
| [**getDeviceApplianceDhcpSubnets**](ApplianceApi.md#getDeviceApplianceDhcpSubnets) | **GET** /devices/{serial}/appliance/dhcp/subnets | Return the DHCP subnet information for an appliance |
| [**getDeviceAppliancePerformance**](ApplianceApi.md#getDeviceAppliancePerformance) | **GET** /devices/{serial}/appliance/performance | Return the performance score for a single MX |
| [**getDeviceAppliancePrefixesDelegated**](ApplianceApi.md#getDeviceAppliancePrefixesDelegated) | **GET** /devices/{serial}/appliance/prefixes/delegated | Return current delegated IPv6 prefixes on an appliance. |
| [**getDeviceAppliancePrefixesDelegatedVlanAssignments**](ApplianceApi.md#getDeviceAppliancePrefixesDelegatedVlanAssignments) | **GET** /devices/{serial}/appliance/prefixes/delegated/vlanAssignments | Return prefixes assigned to all IPv6 enabled VLANs on an appliance. |
| [**getDeviceApplianceUplinksSettings**](ApplianceApi.md#getDeviceApplianceUplinksSettings) | **GET** /devices/{serial}/appliance/uplinks/settings | Return the uplink settings for an MX appliance |
| [**getNetworkApplianceClientSecurityEvents**](ApplianceApi.md#getNetworkApplianceClientSecurityEvents) | **GET** /networks/{networkId}/appliance/clients/{clientId}/security/events | List the security events for a client |
| [**getNetworkApplianceConnectivityMonitoringDestinations**](ApplianceApi.md#getNetworkApplianceConnectivityMonitoringDestinations) | **GET** /networks/{networkId}/appliance/connectivityMonitoringDestinations | Return the connectivity testing destinations for an MX network |
| [**getNetworkApplianceContentFiltering**](ApplianceApi.md#getNetworkApplianceContentFiltering) | **GET** /networks/{networkId}/appliance/contentFiltering | Return the content filtering settings for an MX network |
| [**getNetworkApplianceContentFilteringCategories**](ApplianceApi.md#getNetworkApplianceContentFilteringCategories) | **GET** /networks/{networkId}/appliance/contentFiltering/categories | List all available content filtering categories for an MX network |
| [**getNetworkApplianceFirewallCellularFirewallRules**](ApplianceApi.md#getNetworkApplianceFirewallCellularFirewallRules) | **GET** /networks/{networkId}/appliance/firewall/cellularFirewallRules | Return the cellular firewall rules for an MX network |
| [**getNetworkApplianceFirewallFirewalledService**](ApplianceApi.md#getNetworkApplianceFirewallFirewalledService) | **GET** /networks/{networkId}/appliance/firewall/firewalledServices/{service} | Return the accessibility settings of the given service (&#39;ICMP&#39;, &#39;web&#39;, or &#39;SNMP&#39;) |
| [**getNetworkApplianceFirewallFirewalledServices**](ApplianceApi.md#getNetworkApplianceFirewallFirewalledServices) | **GET** /networks/{networkId}/appliance/firewall/firewalledServices | List the appliance services and their accessibility rules |
| [**getNetworkApplianceFirewallInboundCellularFirewallRules**](ApplianceApi.md#getNetworkApplianceFirewallInboundCellularFirewallRules) | **GET** /networks/{networkId}/appliance/firewall/inboundCellularFirewallRules | Return the inbound cellular firewall rules for an MX network |
| [**getNetworkApplianceFirewallInboundFirewallRules**](ApplianceApi.md#getNetworkApplianceFirewallInboundFirewallRules) | **GET** /networks/{networkId}/appliance/firewall/inboundFirewallRules | Return the inbound firewall rules for an MX network |
| [**getNetworkApplianceFirewallL3FirewallRules**](ApplianceApi.md#getNetworkApplianceFirewallL3FirewallRules) | **GET** /networks/{networkId}/appliance/firewall/l3FirewallRules | Return the L3 firewall rules for an MX network |
| [**getNetworkApplianceFirewallL7FirewallRules**](ApplianceApi.md#getNetworkApplianceFirewallL7FirewallRules) | **GET** /networks/{networkId}/appliance/firewall/l7FirewallRules | List the MX L7 firewall rules for an MX network |
| [**getNetworkApplianceFirewallL7FirewallRulesApplicationCategories**](ApplianceApi.md#getNetworkApplianceFirewallL7FirewallRulesApplicationCategories) | **GET** /networks/{networkId}/appliance/firewall/l7FirewallRules/applicationCategories | Return the L7 firewall application categories and their associated applications for an MX network |
| [**getNetworkApplianceFirewallOneToManyNatRules**](ApplianceApi.md#getNetworkApplianceFirewallOneToManyNatRules) | **GET** /networks/{networkId}/appliance/firewall/oneToManyNatRules | Return the 1:Many NAT mapping rules for an MX network |
| [**getNetworkApplianceFirewallOneToOneNatRules**](ApplianceApi.md#getNetworkApplianceFirewallOneToOneNatRules) | **GET** /networks/{networkId}/appliance/firewall/oneToOneNatRules | Return the 1:1 NAT mapping rules for an MX network |
| [**getNetworkApplianceFirewallPortForwardingRules**](ApplianceApi.md#getNetworkApplianceFirewallPortForwardingRules) | **GET** /networks/{networkId}/appliance/firewall/portForwardingRules | Return the port forwarding rules for an MX network |
| [**getNetworkApplianceFirewallSettings**](ApplianceApi.md#getNetworkApplianceFirewallSettings) | **GET** /networks/{networkId}/appliance/firewall/settings | Return the firewall settings for this network |
| [**getNetworkAppliancePort**](ApplianceApi.md#getNetworkAppliancePort) | **GET** /networks/{networkId}/appliance/ports/{portId} | Return per-port VLAN settings for a single MX port. |
| [**getNetworkAppliancePorts**](ApplianceApi.md#getNetworkAppliancePorts) | **GET** /networks/{networkId}/appliance/ports | List per-port VLAN settings for all ports of a MX. |
| [**getNetworkAppliancePrefixesDelegatedStatic**](ApplianceApi.md#getNetworkAppliancePrefixesDelegatedStatic) | **GET** /networks/{networkId}/appliance/prefixes/delegated/statics/{staticDelegatedPrefixId} | Return a static delegated prefix from a network |
| [**getNetworkAppliancePrefixesDelegatedStatics**](ApplianceApi.md#getNetworkAppliancePrefixesDelegatedStatics) | **GET** /networks/{networkId}/appliance/prefixes/delegated/statics | List static delegated prefixes for a network |
| [**getNetworkApplianceSecurityEvents**](ApplianceApi.md#getNetworkApplianceSecurityEvents) | **GET** /networks/{networkId}/appliance/security/events | List the security events for a network |
| [**getNetworkApplianceSecurityIntrusion**](ApplianceApi.md#getNetworkApplianceSecurityIntrusion) | **GET** /networks/{networkId}/appliance/security/intrusion | Returns all supported intrusion settings for an MX network |
| [**getNetworkApplianceSecurityMalware**](ApplianceApi.md#getNetworkApplianceSecurityMalware) | **GET** /networks/{networkId}/appliance/security/malware | Returns all supported malware settings for an MX network |
| [**getNetworkApplianceSettings**](ApplianceApi.md#getNetworkApplianceSettings) | **GET** /networks/{networkId}/appliance/settings | Return the appliance settings for a network |
| [**getNetworkApplianceSingleLan**](ApplianceApi.md#getNetworkApplianceSingleLan) | **GET** /networks/{networkId}/appliance/singleLan | Return single LAN configuration |
| [**getNetworkApplianceSsid**](ApplianceApi.md#getNetworkApplianceSsid) | **GET** /networks/{networkId}/appliance/ssids/{number} | Return a single MX SSID |
| [**getNetworkApplianceSsids**](ApplianceApi.md#getNetworkApplianceSsids) | **GET** /networks/{networkId}/appliance/ssids | List the MX SSIDs in a network |
| [**getNetworkApplianceStaticRoute**](ApplianceApi.md#getNetworkApplianceStaticRoute) | **GET** /networks/{networkId}/appliance/staticRoutes/{staticRouteId} | Return a static route for an MX or teleworker network |
| [**getNetworkApplianceStaticRoutes**](ApplianceApi.md#getNetworkApplianceStaticRoutes) | **GET** /networks/{networkId}/appliance/staticRoutes | List the static routes for an MX or teleworker network |
| [**getNetworkApplianceTrafficShaping**](ApplianceApi.md#getNetworkApplianceTrafficShaping) | **GET** /networks/{networkId}/appliance/trafficShaping | Display the traffic shaping settings for an MX network |
| [**getNetworkApplianceTrafficShapingCustomPerformanceClass**](ApplianceApi.md#getNetworkApplianceTrafficShapingCustomPerformanceClass) | **GET** /networks/{networkId}/appliance/trafficShaping/customPerformanceClasses/{customPerformanceClassId} | Return a custom performance class for an MX network |
| [**getNetworkApplianceTrafficShapingCustomPerformanceClasses**](ApplianceApi.md#getNetworkApplianceTrafficShapingCustomPerformanceClasses) | **GET** /networks/{networkId}/appliance/trafficShaping/customPerformanceClasses | List all custom performance classes for an MX network |
| [**getNetworkApplianceTrafficShapingRules**](ApplianceApi.md#getNetworkApplianceTrafficShapingRules) | **GET** /networks/{networkId}/appliance/trafficShaping/rules | Display the traffic shaping settings rules for an MX network |
| [**getNetworkApplianceTrafficShapingUplinkBandwidth**](ApplianceApi.md#getNetworkApplianceTrafficShapingUplinkBandwidth) | **GET** /networks/{networkId}/appliance/trafficShaping/uplinkBandwidth | Returns the uplink bandwidth limits for your MX network |
| [**getNetworkApplianceTrafficShapingUplinkSelection**](ApplianceApi.md#getNetworkApplianceTrafficShapingUplinkSelection) | **GET** /networks/{networkId}/appliance/trafficShaping/uplinkSelection | Show uplink selection settings for an MX network |
| [**getNetworkApplianceUplinksUsageHistory**](ApplianceApi.md#getNetworkApplianceUplinksUsageHistory) | **GET** /networks/{networkId}/appliance/uplinks/usageHistory | Get the sent and received bytes for each uplink of a network. |
| [**getNetworkApplianceVlan**](ApplianceApi.md#getNetworkApplianceVlan) | **GET** /networks/{networkId}/appliance/vlans/{vlanId} | Return a VLAN |
| [**getNetworkApplianceVlans**](ApplianceApi.md#getNetworkApplianceVlans) | **GET** /networks/{networkId}/appliance/vlans | List the VLANs for an MX network |
| [**getNetworkApplianceVlansSettings**](ApplianceApi.md#getNetworkApplianceVlansSettings) | **GET** /networks/{networkId}/appliance/vlans/settings | Returns the enabled status of VLANs for the network |
| [**getNetworkApplianceVpnBgp**](ApplianceApi.md#getNetworkApplianceVpnBgp) | **GET** /networks/{networkId}/appliance/vpn/bgp | Return a Hub BGP Configuration |
| [**getNetworkApplianceVpnSiteToSiteVpn**](ApplianceApi.md#getNetworkApplianceVpnSiteToSiteVpn) | **GET** /networks/{networkId}/appliance/vpn/siteToSiteVpn | Return the site-to-site VPN settings of a network |
| [**getNetworkApplianceWarmSpare**](ApplianceApi.md#getNetworkApplianceWarmSpare) | **GET** /networks/{networkId}/appliance/warmSpare | Return MX warm spare settings |
| [**getOrganizationApplianceSecurityEvents**](ApplianceApi.md#getOrganizationApplianceSecurityEvents) | **GET** /organizations/{organizationId}/appliance/security/events | List the security events for an organization |
| [**getOrganizationApplianceSecurityIntrusion**](ApplianceApi.md#getOrganizationApplianceSecurityIntrusion) | **GET** /organizations/{organizationId}/appliance/security/intrusion | Returns all supported intrusion settings for an organization |
| [**getOrganizationApplianceUplinkStatuses**](ApplianceApi.md#getOrganizationApplianceUplinkStatuses) | **GET** /organizations/{organizationId}/appliance/uplink/statuses | List the uplink status of every Meraki MX and Z series appliances in the organization |
| [**getOrganizationApplianceVpnStats**](ApplianceApi.md#getOrganizationApplianceVpnStats) | **GET** /organizations/{organizationId}/appliance/vpn/stats | Show VPN history stat for networks in an organization |
| [**getOrganizationApplianceVpnStatuses**](ApplianceApi.md#getOrganizationApplianceVpnStatuses) | **GET** /organizations/{organizationId}/appliance/vpn/statuses | Show VPN status for networks in an organization |
| [**getOrganizationApplianceVpnThirdPartyVPNPeers**](ApplianceApi.md#getOrganizationApplianceVpnThirdPartyVPNPeers) | **GET** /organizations/{organizationId}/appliance/vpn/thirdPartyVPNPeers | Return the third party VPN peers for an organization |
| [**getOrganizationApplianceVpnVpnFirewallRules**](ApplianceApi.md#getOrganizationApplianceVpnVpnFirewallRules) | **GET** /organizations/{organizationId}/appliance/vpn/vpnFirewallRules | Return the firewall rules for an organization&#39;s site-to-site VPN |
| [**swapNetworkApplianceWarmSpare**](ApplianceApi.md#swapNetworkApplianceWarmSpare) | **POST** /networks/{networkId}/appliance/warmSpare/swap | Swap MX primary and warm spare appliances |
| [**updateDeviceApplianceUplinksSettings**](ApplianceApi.md#updateDeviceApplianceUplinksSettings) | **PUT** /devices/{serial}/appliance/uplinks/settings | Update the uplink settings for an MX appliance |
| [**updateNetworkApplianceConnectivityMonitoringDestinations**](ApplianceApi.md#updateNetworkApplianceConnectivityMonitoringDestinations) | **PUT** /networks/{networkId}/appliance/connectivityMonitoringDestinations | Update the connectivity testing destinations for an MX network |
| [**updateNetworkApplianceContentFiltering**](ApplianceApi.md#updateNetworkApplianceContentFiltering) | **PUT** /networks/{networkId}/appliance/contentFiltering | Update the content filtering settings for an MX network |
| [**updateNetworkApplianceFirewallCellularFirewallRules**](ApplianceApi.md#updateNetworkApplianceFirewallCellularFirewallRules) | **PUT** /networks/{networkId}/appliance/firewall/cellularFirewallRules | Update the cellular firewall rules of an MX network |
| [**updateNetworkApplianceFirewallFirewalledService**](ApplianceApi.md#updateNetworkApplianceFirewallFirewalledService) | **PUT** /networks/{networkId}/appliance/firewall/firewalledServices/{service} | Updates the accessibility settings for the given service (&#39;ICMP&#39;, &#39;web&#39;, or &#39;SNMP&#39;) |
| [**updateNetworkApplianceFirewallInboundCellularFirewallRules**](ApplianceApi.md#updateNetworkApplianceFirewallInboundCellularFirewallRules) | **PUT** /networks/{networkId}/appliance/firewall/inboundCellularFirewallRules | Update the inbound cellular firewall rules of an MX network |
| [**updateNetworkApplianceFirewallInboundFirewallRules**](ApplianceApi.md#updateNetworkApplianceFirewallInboundFirewallRules) | **PUT** /networks/{networkId}/appliance/firewall/inboundFirewallRules | Update the inbound firewall rules of an MX network |
| [**updateNetworkApplianceFirewallL3FirewallRules**](ApplianceApi.md#updateNetworkApplianceFirewallL3FirewallRules) | **PUT** /networks/{networkId}/appliance/firewall/l3FirewallRules | Update the L3 firewall rules of an MX network |
| [**updateNetworkApplianceFirewallL7FirewallRules**](ApplianceApi.md#updateNetworkApplianceFirewallL7FirewallRules) | **PUT** /networks/{networkId}/appliance/firewall/l7FirewallRules | Update the MX L7 firewall rules for an MX network |
| [**updateNetworkApplianceFirewallOneToManyNatRules**](ApplianceApi.md#updateNetworkApplianceFirewallOneToManyNatRules) | **PUT** /networks/{networkId}/appliance/firewall/oneToManyNatRules | Set the 1:Many NAT mapping rules for an MX network |
| [**updateNetworkApplianceFirewallOneToOneNatRules**](ApplianceApi.md#updateNetworkApplianceFirewallOneToOneNatRules) | **PUT** /networks/{networkId}/appliance/firewall/oneToOneNatRules | Set the 1:1 NAT mapping rules for an MX network |
| [**updateNetworkApplianceFirewallPortForwardingRules**](ApplianceApi.md#updateNetworkApplianceFirewallPortForwardingRules) | **PUT** /networks/{networkId}/appliance/firewall/portForwardingRules | Update the port forwarding rules for an MX network |
| [**updateNetworkApplianceFirewallSettings**](ApplianceApi.md#updateNetworkApplianceFirewallSettings) | **PUT** /networks/{networkId}/appliance/firewall/settings | Update the firewall settings for this network |
| [**updateNetworkAppliancePort**](ApplianceApi.md#updateNetworkAppliancePort) | **PUT** /networks/{networkId}/appliance/ports/{portId} | Update the per-port VLAN settings for a single MX port. |
| [**updateNetworkAppliancePrefixesDelegatedStatic**](ApplianceApi.md#updateNetworkAppliancePrefixesDelegatedStatic) | **PUT** /networks/{networkId}/appliance/prefixes/delegated/statics/{staticDelegatedPrefixId} | Update a static delegated prefix from a network |
| [**updateNetworkApplianceSecurityIntrusion**](ApplianceApi.md#updateNetworkApplianceSecurityIntrusion) | **PUT** /networks/{networkId}/appliance/security/intrusion | Set the supported intrusion settings for an MX network |
| [**updateNetworkApplianceSecurityMalware**](ApplianceApi.md#updateNetworkApplianceSecurityMalware) | **PUT** /networks/{networkId}/appliance/security/malware | Set the supported malware settings for an MX network |
| [**updateNetworkApplianceSettings**](ApplianceApi.md#updateNetworkApplianceSettings) | **PUT** /networks/{networkId}/appliance/settings | Update the appliance settings for a network |
| [**updateNetworkApplianceSingleLan**](ApplianceApi.md#updateNetworkApplianceSingleLan) | **PUT** /networks/{networkId}/appliance/singleLan | Update single LAN configuration |
| [**updateNetworkApplianceSsid**](ApplianceApi.md#updateNetworkApplianceSsid) | **PUT** /networks/{networkId}/appliance/ssids/{number} | Update the attributes of an MX SSID |
| [**updateNetworkApplianceStaticRoute**](ApplianceApi.md#updateNetworkApplianceStaticRoute) | **PUT** /networks/{networkId}/appliance/staticRoutes/{staticRouteId} | Update a static route for an MX or teleworker network |
| [**updateNetworkApplianceTrafficShaping**](ApplianceApi.md#updateNetworkApplianceTrafficShaping) | **PUT** /networks/{networkId}/appliance/trafficShaping | Update the traffic shaping settings for an MX network |
| [**updateNetworkApplianceTrafficShapingCustomPerformanceClass**](ApplianceApi.md#updateNetworkApplianceTrafficShapingCustomPerformanceClass) | **PUT** /networks/{networkId}/appliance/trafficShaping/customPerformanceClasses/{customPerformanceClassId} | Update a custom performance class for an MX network |
| [**updateNetworkApplianceTrafficShapingRules**](ApplianceApi.md#updateNetworkApplianceTrafficShapingRules) | **PUT** /networks/{networkId}/appliance/trafficShaping/rules | Update the traffic shaping settings rules for an MX network |
| [**updateNetworkApplianceTrafficShapingUplinkBandwidth**](ApplianceApi.md#updateNetworkApplianceTrafficShapingUplinkBandwidth) | **PUT** /networks/{networkId}/appliance/trafficShaping/uplinkBandwidth | Updates the uplink bandwidth settings for your MX network. |
| [**updateNetworkApplianceTrafficShapingUplinkSelection**](ApplianceApi.md#updateNetworkApplianceTrafficShapingUplinkSelection) | **PUT** /networks/{networkId}/appliance/trafficShaping/uplinkSelection | Update uplink selection settings for an MX network |
| [**updateNetworkApplianceVlan**](ApplianceApi.md#updateNetworkApplianceVlan) | **PUT** /networks/{networkId}/appliance/vlans/{vlanId} | Update a VLAN |
| [**updateNetworkApplianceVlansSettings**](ApplianceApi.md#updateNetworkApplianceVlansSettings) | **PUT** /networks/{networkId}/appliance/vlans/settings | Enable/Disable VLANs for the given network |
| [**updateNetworkApplianceVpnBgp**](ApplianceApi.md#updateNetworkApplianceVpnBgp) | **PUT** /networks/{networkId}/appliance/vpn/bgp | Update a Hub BGP Configuration |
| [**updateNetworkApplianceVpnSiteToSiteVpn**](ApplianceApi.md#updateNetworkApplianceVpnSiteToSiteVpn) | **PUT** /networks/{networkId}/appliance/vpn/siteToSiteVpn | Update the site-to-site VPN settings of a network |
| [**updateNetworkApplianceWarmSpare**](ApplianceApi.md#updateNetworkApplianceWarmSpare) | **PUT** /networks/{networkId}/appliance/warmSpare | Update MX warm spare settings |
| [**updateOrganizationApplianceSecurityIntrusion**](ApplianceApi.md#updateOrganizationApplianceSecurityIntrusion) | **PUT** /organizations/{organizationId}/appliance/security/intrusion | Sets supported intrusion settings for an organization |
| [**updateOrganizationApplianceVpnThirdPartyVPNPeers**](ApplianceApi.md#updateOrganizationApplianceVpnThirdPartyVPNPeers) | **PUT** /organizations/{organizationId}/appliance/vpn/thirdPartyVPNPeers | Update the third party VPN peers for an organization |
| [**updateOrganizationApplianceVpnVpnFirewallRules**](ApplianceApi.md#updateOrganizationApplianceVpnVpnFirewallRules) | **PUT** /organizations/{organizationId}/appliance/vpn/vpnFirewallRules | Update the firewall rules of an organization&#39;s site-to-site VPN |


<a id="createDeviceApplianceVmxAuthenticationToken"></a>
# **createDeviceApplianceVmxAuthenticationToken**
> CreateDeviceApplianceVmxAuthenticationToken201Response createDeviceApplianceVmxAuthenticationToken(serial)

Generate a new vMX authentication token

Generate a new vMX authentication token

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String serial = "serial_example"; // String | 
    try {
      CreateDeviceApplianceVmxAuthenticationToken201Response result = apiInstance.createDeviceApplianceVmxAuthenticationToken(serial);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#createDeviceApplianceVmxAuthenticationToken");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **serial** | **String**|  | |

### Return type

[**CreateDeviceApplianceVmxAuthenticationToken201Response**](CreateDeviceApplianceVmxAuthenticationToken201Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful operation |  -  |

<a id="createNetworkAppliancePrefixesDelegatedStatic"></a>
# **createNetworkAppliancePrefixesDelegatedStatic**
> Object createNetworkAppliancePrefixesDelegatedStatic(networkId, createNetworkAppliancePrefixesDelegatedStaticRequest)

Add a static delegated prefix from a network

Add a static delegated prefix from a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    CreateNetworkAppliancePrefixesDelegatedStaticRequest createNetworkAppliancePrefixesDelegatedStaticRequest = new CreateNetworkAppliancePrefixesDelegatedStaticRequest(); // CreateNetworkAppliancePrefixesDelegatedStaticRequest | 
    try {
      Object result = apiInstance.createNetworkAppliancePrefixesDelegatedStatic(networkId, createNetworkAppliancePrefixesDelegatedStaticRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#createNetworkAppliancePrefixesDelegatedStatic");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |
| **createNetworkAppliancePrefixesDelegatedStaticRequest** | [**CreateNetworkAppliancePrefixesDelegatedStaticRequest**](CreateNetworkAppliancePrefixesDelegatedStaticRequest.md)|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful operation |  -  |

<a id="createNetworkApplianceStaticRoute"></a>
# **createNetworkApplianceStaticRoute**
> Object createNetworkApplianceStaticRoute(networkId, createNetworkApplianceStaticRouteRequest)

Add a static route for an MX or teleworker network

Add a static route for an MX or teleworker network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    CreateNetworkApplianceStaticRouteRequest createNetworkApplianceStaticRouteRequest = new CreateNetworkApplianceStaticRouteRequest(); // CreateNetworkApplianceStaticRouteRequest | 
    try {
      Object result = apiInstance.createNetworkApplianceStaticRoute(networkId, createNetworkApplianceStaticRouteRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#createNetworkApplianceStaticRoute");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |
| **createNetworkApplianceStaticRouteRequest** | [**CreateNetworkApplianceStaticRouteRequest**](CreateNetworkApplianceStaticRouteRequest.md)|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful operation |  -  |

<a id="createNetworkApplianceTrafficShapingCustomPerformanceClass"></a>
# **createNetworkApplianceTrafficShapingCustomPerformanceClass**
> Object createNetworkApplianceTrafficShapingCustomPerformanceClass(networkId, createNetworkApplianceTrafficShapingCustomPerformanceClassRequest)

Add a custom performance class for an MX network

Add a custom performance class for an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    CreateNetworkApplianceTrafficShapingCustomPerformanceClassRequest createNetworkApplianceTrafficShapingCustomPerformanceClassRequest = new CreateNetworkApplianceTrafficShapingCustomPerformanceClassRequest(); // CreateNetworkApplianceTrafficShapingCustomPerformanceClassRequest | 
    try {
      Object result = apiInstance.createNetworkApplianceTrafficShapingCustomPerformanceClass(networkId, createNetworkApplianceTrafficShapingCustomPerformanceClassRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#createNetworkApplianceTrafficShapingCustomPerformanceClass");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |
| **createNetworkApplianceTrafficShapingCustomPerformanceClassRequest** | [**CreateNetworkApplianceTrafficShapingCustomPerformanceClassRequest**](CreateNetworkApplianceTrafficShapingCustomPerformanceClassRequest.md)|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful operation |  -  |

<a id="createNetworkApplianceVlan"></a>
# **createNetworkApplianceVlan**
> CreateNetworkApplianceVlan201Response createNetworkApplianceVlan(networkId, createNetworkApplianceVlanRequest)

Add a VLAN

Add a VLAN

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    CreateNetworkApplianceVlanRequest createNetworkApplianceVlanRequest = new CreateNetworkApplianceVlanRequest(); // CreateNetworkApplianceVlanRequest | 
    try {
      CreateNetworkApplianceVlan201Response result = apiInstance.createNetworkApplianceVlan(networkId, createNetworkApplianceVlanRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#createNetworkApplianceVlan");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |
| **createNetworkApplianceVlanRequest** | [**CreateNetworkApplianceVlanRequest**](CreateNetworkApplianceVlanRequest.md)|  | |

### Return type

[**CreateNetworkApplianceVlan201Response**](CreateNetworkApplianceVlan201Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful operation |  -  |

<a id="deleteNetworkAppliancePrefixesDelegatedStatic"></a>
# **deleteNetworkAppliancePrefixesDelegatedStatic**
> deleteNetworkAppliancePrefixesDelegatedStatic(networkId, staticDelegatedPrefixId)

Delete a static delegated prefix from a network

Delete a static delegated prefix from a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String staticDelegatedPrefixId = "staticDelegatedPrefixId_example"; // String | 
    try {
      apiInstance.deleteNetworkAppliancePrefixesDelegatedStatic(networkId, staticDelegatedPrefixId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#deleteNetworkAppliancePrefixesDelegatedStatic");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |
| **staticDelegatedPrefixId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successful operation |  -  |

<a id="deleteNetworkApplianceStaticRoute"></a>
# **deleteNetworkApplianceStaticRoute**
> deleteNetworkApplianceStaticRoute(networkId, staticRouteId)

Delete a static route from an MX or teleworker network

Delete a static route from an MX or teleworker network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String staticRouteId = "staticRouteId_example"; // String | 
    try {
      apiInstance.deleteNetworkApplianceStaticRoute(networkId, staticRouteId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#deleteNetworkApplianceStaticRoute");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |
| **staticRouteId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successful operation |  -  |

<a id="deleteNetworkApplianceTrafficShapingCustomPerformanceClass"></a>
# **deleteNetworkApplianceTrafficShapingCustomPerformanceClass**
> deleteNetworkApplianceTrafficShapingCustomPerformanceClass(networkId, customPerformanceClassId)

Delete a custom performance class from an MX network

Delete a custom performance class from an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String customPerformanceClassId = "customPerformanceClassId_example"; // String | 
    try {
      apiInstance.deleteNetworkApplianceTrafficShapingCustomPerformanceClass(networkId, customPerformanceClassId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#deleteNetworkApplianceTrafficShapingCustomPerformanceClass");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |
| **customPerformanceClassId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successful operation |  -  |

<a id="deleteNetworkApplianceVlan"></a>
# **deleteNetworkApplianceVlan**
> deleteNetworkApplianceVlan(networkId, vlanId)

Delete a VLAN from a network

Delete a VLAN from a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String vlanId = "vlanId_example"; // String | 
    try {
      apiInstance.deleteNetworkApplianceVlan(networkId, vlanId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#deleteNetworkApplianceVlan");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |
| **vlanId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successful operation |  -  |

<a id="getDeviceApplianceDhcpSubnets"></a>
# **getDeviceApplianceDhcpSubnets**
> List&lt;Object&gt; getDeviceApplianceDhcpSubnets(serial)

Return the DHCP subnet information for an appliance

Return the DHCP subnet information for an appliance

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String serial = "serial_example"; // String | 
    try {
      List<Object> result = apiInstance.getDeviceApplianceDhcpSubnets(serial);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#getDeviceApplianceDhcpSubnets");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **serial** | **String**|  | |

### Return type

**List&lt;Object&gt;**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getDeviceAppliancePerformance"></a>
# **getDeviceAppliancePerformance**
> Object getDeviceAppliancePerformance(serial)

Return the performance score for a single MX

Return the performance score for a single MX. Only primary MX devices supported. If no data is available, a 204 error code is returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String serial = "serial_example"; // String | 
    try {
      Object result = apiInstance.getDeviceAppliancePerformance(serial);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#getDeviceAppliancePerformance");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **serial** | **String**|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getDeviceAppliancePrefixesDelegated"></a>
# **getDeviceAppliancePrefixesDelegated**
> List&lt;Object&gt; getDeviceAppliancePrefixesDelegated(serial)

Return current delegated IPv6 prefixes on an appliance.

Return current delegated IPv6 prefixes on an appliance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String serial = "serial_example"; // String | 
    try {
      List<Object> result = apiInstance.getDeviceAppliancePrefixesDelegated(serial);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#getDeviceAppliancePrefixesDelegated");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **serial** | **String**|  | |

### Return type

**List&lt;Object&gt;**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getDeviceAppliancePrefixesDelegatedVlanAssignments"></a>
# **getDeviceAppliancePrefixesDelegatedVlanAssignments**
> List&lt;Object&gt; getDeviceAppliancePrefixesDelegatedVlanAssignments(serial)

Return prefixes assigned to all IPv6 enabled VLANs on an appliance.

Return prefixes assigned to all IPv6 enabled VLANs on an appliance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String serial = "serial_example"; // String | 
    try {
      List<Object> result = apiInstance.getDeviceAppliancePrefixesDelegatedVlanAssignments(serial);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#getDeviceAppliancePrefixesDelegatedVlanAssignments");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **serial** | **String**|  | |

### Return type

**List&lt;Object&gt;**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getDeviceApplianceUplinksSettings"></a>
# **getDeviceApplianceUplinksSettings**
> GetDeviceApplianceUplinksSettings200Response getDeviceApplianceUplinksSettings(serial)

Return the uplink settings for an MX appliance

Return the uplink settings for an MX appliance

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String serial = "serial_example"; // String | 
    try {
      GetDeviceApplianceUplinksSettings200Response result = apiInstance.getDeviceApplianceUplinksSettings(serial);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#getDeviceApplianceUplinksSettings");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **serial** | **String**|  | |

### Return type

[**GetDeviceApplianceUplinksSettings200Response**](GetDeviceApplianceUplinksSettings200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkApplianceClientSecurityEvents"></a>
# **getNetworkApplianceClientSecurityEvents**
> List&lt;Object&gt; getNetworkApplianceClientSecurityEvents(networkId, clientId, t0, t1, timespan, perPage, startingAfter, endingBefore, sortOrder)

List the security events for a client

List the security events for a client. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String clientId = "clientId_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. Data is gathered after the specified t0 value. The maximum lookback period is 791 days from today.
    String t1 = "t1_example"; // String | The end of the timespan for the data. t1 can be a maximum of 791 days after t0.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 791 days. The default is 31 days.
    Integer perPage = 56; // Integer | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
    String startingAfter = "startingAfter_example"; // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String endingBefore = "endingBefore_example"; // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String sortOrder = "ascending"; // String | Sorted order of security events based on event detection time. Order options are 'ascending' or 'descending'. Default is ascending order.
    try {
      List<Object> result = apiInstance.getNetworkApplianceClientSecurityEvents(networkId, clientId, t0, t1, timespan, perPage, startingAfter, endingBefore, sortOrder);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#getNetworkApplianceClientSecurityEvents");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |
| **clientId** | **String**|  | |
| **t0** | **String**| The beginning of the timespan for the data. Data is gathered after the specified t0 value. The maximum lookback period is 791 days from today. | [optional] |
| **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 791 days after t0. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 791 days. The default is 31 days. | [optional] |
| **perPage** | **Integer**| The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100. | [optional] |
| **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **sortOrder** | **String**| Sorted order of security events based on event detection time. Order options are &#39;ascending&#39; or &#39;descending&#39;. Default is ascending order. | [optional] [enum: ascending, descending] |

### Return type

**List&lt;Object&gt;**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  * Link - A comma-separated list of first, last, prev, and next relative links used for subsequent paginated requests. <br>  |

<a id="getNetworkApplianceConnectivityMonitoringDestinations"></a>
# **getNetworkApplianceConnectivityMonitoringDestinations**
> Object getNetworkApplianceConnectivityMonitoringDestinations(networkId)

Return the connectivity testing destinations for an MX network

Return the connectivity testing destinations for an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkApplianceConnectivityMonitoringDestinations(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#getNetworkApplianceConnectivityMonitoringDestinations");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkApplianceContentFiltering"></a>
# **getNetworkApplianceContentFiltering**
> Object getNetworkApplianceContentFiltering(networkId)

Return the content filtering settings for an MX network

Return the content filtering settings for an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkApplianceContentFiltering(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#getNetworkApplianceContentFiltering");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkApplianceContentFilteringCategories"></a>
# **getNetworkApplianceContentFilteringCategories**
> Object getNetworkApplianceContentFilteringCategories(networkId)

List all available content filtering categories for an MX network

List all available content filtering categories for an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkApplianceContentFilteringCategories(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#getNetworkApplianceContentFilteringCategories");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkApplianceFirewallCellularFirewallRules"></a>
# **getNetworkApplianceFirewallCellularFirewallRules**
> Object getNetworkApplianceFirewallCellularFirewallRules(networkId)

Return the cellular firewall rules for an MX network

Return the cellular firewall rules for an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkApplianceFirewallCellularFirewallRules(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#getNetworkApplianceFirewallCellularFirewallRules");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkApplianceFirewallFirewalledService"></a>
# **getNetworkApplianceFirewallFirewalledService**
> Object getNetworkApplianceFirewallFirewalledService(networkId, service)

Return the accessibility settings of the given service (&#39;ICMP&#39;, &#39;web&#39;, or &#39;SNMP&#39;)

Return the accessibility settings of the given service (&#39;ICMP&#39;, &#39;web&#39;, or &#39;SNMP&#39;)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String service = "service_example"; // String | 
    try {
      Object result = apiInstance.getNetworkApplianceFirewallFirewalledService(networkId, service);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#getNetworkApplianceFirewallFirewalledService");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |
| **service** | **String**|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkApplianceFirewallFirewalledServices"></a>
# **getNetworkApplianceFirewallFirewalledServices**
> List&lt;Object&gt; getNetworkApplianceFirewallFirewalledServices(networkId)

List the appliance services and their accessibility rules

List the appliance services and their accessibility rules

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<Object> result = apiInstance.getNetworkApplianceFirewallFirewalledServices(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#getNetworkApplianceFirewallFirewalledServices");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |

### Return type

**List&lt;Object&gt;**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkApplianceFirewallInboundCellularFirewallRules"></a>
# **getNetworkApplianceFirewallInboundCellularFirewallRules**
> List&lt;Object&gt; getNetworkApplianceFirewallInboundCellularFirewallRules(networkId)

Return the inbound cellular firewall rules for an MX network

Return the inbound cellular firewall rules for an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<Object> result = apiInstance.getNetworkApplianceFirewallInboundCellularFirewallRules(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#getNetworkApplianceFirewallInboundCellularFirewallRules");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |

### Return type

**List&lt;Object&gt;**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkApplianceFirewallInboundFirewallRules"></a>
# **getNetworkApplianceFirewallInboundFirewallRules**
> Object getNetworkApplianceFirewallInboundFirewallRules(networkId)

Return the inbound firewall rules for an MX network

Return the inbound firewall rules for an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkApplianceFirewallInboundFirewallRules(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#getNetworkApplianceFirewallInboundFirewallRules");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkApplianceFirewallL3FirewallRules"></a>
# **getNetworkApplianceFirewallL3FirewallRules**
> Object getNetworkApplianceFirewallL3FirewallRules(networkId)

Return the L3 firewall rules for an MX network

Return the L3 firewall rules for an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkApplianceFirewallL3FirewallRules(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#getNetworkApplianceFirewallL3FirewallRules");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkApplianceFirewallL7FirewallRules"></a>
# **getNetworkApplianceFirewallL7FirewallRules**
> Object getNetworkApplianceFirewallL7FirewallRules(networkId)

List the MX L7 firewall rules for an MX network

List the MX L7 firewall rules for an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkApplianceFirewallL7FirewallRules(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#getNetworkApplianceFirewallL7FirewallRules");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkApplianceFirewallL7FirewallRulesApplicationCategories"></a>
# **getNetworkApplianceFirewallL7FirewallRulesApplicationCategories**
> Object getNetworkApplianceFirewallL7FirewallRulesApplicationCategories(networkId)

Return the L7 firewall application categories and their associated applications for an MX network

Return the L7 firewall application categories and their associated applications for an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkApplianceFirewallL7FirewallRulesApplicationCategories(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#getNetworkApplianceFirewallL7FirewallRulesApplicationCategories");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkApplianceFirewallOneToManyNatRules"></a>
# **getNetworkApplianceFirewallOneToManyNatRules**
> Object getNetworkApplianceFirewallOneToManyNatRules(networkId)

Return the 1:Many NAT mapping rules for an MX network

Return the 1:Many NAT mapping rules for an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkApplianceFirewallOneToManyNatRules(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#getNetworkApplianceFirewallOneToManyNatRules");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkApplianceFirewallOneToOneNatRules"></a>
# **getNetworkApplianceFirewallOneToOneNatRules**
> Object getNetworkApplianceFirewallOneToOneNatRules(networkId)

Return the 1:1 NAT mapping rules for an MX network

Return the 1:1 NAT mapping rules for an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkApplianceFirewallOneToOneNatRules(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#getNetworkApplianceFirewallOneToOneNatRules");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkApplianceFirewallPortForwardingRules"></a>
# **getNetworkApplianceFirewallPortForwardingRules**
> Object getNetworkApplianceFirewallPortForwardingRules(networkId)

Return the port forwarding rules for an MX network

Return the port forwarding rules for an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkApplianceFirewallPortForwardingRules(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#getNetworkApplianceFirewallPortForwardingRules");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkApplianceFirewallSettings"></a>
# **getNetworkApplianceFirewallSettings**
> Object getNetworkApplianceFirewallSettings(networkId)

Return the firewall settings for this network

Return the firewall settings for this network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkApplianceFirewallSettings(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#getNetworkApplianceFirewallSettings");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkAppliancePort"></a>
# **getNetworkAppliancePort**
> GetNetworkAppliancePorts200ResponseInner getNetworkAppliancePort(networkId, portId)

Return per-port VLAN settings for a single MX port.

Return per-port VLAN settings for a single MX port.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String portId = "portId_example"; // String | 
    try {
      GetNetworkAppliancePorts200ResponseInner result = apiInstance.getNetworkAppliancePort(networkId, portId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#getNetworkAppliancePort");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |
| **portId** | **String**|  | |

### Return type

[**GetNetworkAppliancePorts200ResponseInner**](GetNetworkAppliancePorts200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkAppliancePorts"></a>
# **getNetworkAppliancePorts**
> List&lt;GetNetworkAppliancePorts200ResponseInner&gt; getNetworkAppliancePorts(networkId)

List per-port VLAN settings for all ports of a MX.

List per-port VLAN settings for all ports of a MX.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<GetNetworkAppliancePorts200ResponseInner> result = apiInstance.getNetworkAppliancePorts(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#getNetworkAppliancePorts");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |

### Return type

[**List&lt;GetNetworkAppliancePorts200ResponseInner&gt;**](GetNetworkAppliancePorts200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkAppliancePrefixesDelegatedStatic"></a>
# **getNetworkAppliancePrefixesDelegatedStatic**
> GetNetworkAppliancePrefixesDelegatedStatics200ResponseInner getNetworkAppliancePrefixesDelegatedStatic(networkId, staticDelegatedPrefixId)

Return a static delegated prefix from a network

Return a static delegated prefix from a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String staticDelegatedPrefixId = "staticDelegatedPrefixId_example"; // String | 
    try {
      GetNetworkAppliancePrefixesDelegatedStatics200ResponseInner result = apiInstance.getNetworkAppliancePrefixesDelegatedStatic(networkId, staticDelegatedPrefixId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#getNetworkAppliancePrefixesDelegatedStatic");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |
| **staticDelegatedPrefixId** | **String**|  | |

### Return type

[**GetNetworkAppliancePrefixesDelegatedStatics200ResponseInner**](GetNetworkAppliancePrefixesDelegatedStatics200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkAppliancePrefixesDelegatedStatics"></a>
# **getNetworkAppliancePrefixesDelegatedStatics**
> List&lt;GetNetworkAppliancePrefixesDelegatedStatics200ResponseInner&gt; getNetworkAppliancePrefixesDelegatedStatics(networkId)

List static delegated prefixes for a network

List static delegated prefixes for a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<GetNetworkAppliancePrefixesDelegatedStatics200ResponseInner> result = apiInstance.getNetworkAppliancePrefixesDelegatedStatics(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#getNetworkAppliancePrefixesDelegatedStatics");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |

### Return type

[**List&lt;GetNetworkAppliancePrefixesDelegatedStatics200ResponseInner&gt;**](GetNetworkAppliancePrefixesDelegatedStatics200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkApplianceSecurityEvents"></a>
# **getNetworkApplianceSecurityEvents**
> List&lt;Object&gt; getNetworkApplianceSecurityEvents(networkId, t0, t1, timespan, perPage, startingAfter, endingBefore, sortOrder)

List the security events for a network

List the security events for a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. Data is gathered after the specified t0 value. The maximum lookback period is 365 days from today.
    String t1 = "t1_example"; // String | The end of the timespan for the data. t1 can be a maximum of 365 days after t0.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 365 days. The default is 31 days.
    Integer perPage = 56; // Integer | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
    String startingAfter = "startingAfter_example"; // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String endingBefore = "endingBefore_example"; // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String sortOrder = "ascending"; // String | Sorted order of security events based on event detection time. Order options are 'ascending' or 'descending'. Default is ascending order.
    try {
      List<Object> result = apiInstance.getNetworkApplianceSecurityEvents(networkId, t0, t1, timespan, perPage, startingAfter, endingBefore, sortOrder);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#getNetworkApplianceSecurityEvents");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |
| **t0** | **String**| The beginning of the timespan for the data. Data is gathered after the specified t0 value. The maximum lookback period is 365 days from today. | [optional] |
| **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 365 days after t0. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 365 days. The default is 31 days. | [optional] |
| **perPage** | **Integer**| The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100. | [optional] |
| **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **sortOrder** | **String**| Sorted order of security events based on event detection time. Order options are &#39;ascending&#39; or &#39;descending&#39;. Default is ascending order. | [optional] [enum: ascending, descending] |

### Return type

**List&lt;Object&gt;**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  * Link - A comma-separated list of first, last, prev, and next relative links used for subsequent paginated requests. <br>  |

<a id="getNetworkApplianceSecurityIntrusion"></a>
# **getNetworkApplianceSecurityIntrusion**
> Object getNetworkApplianceSecurityIntrusion(networkId)

Returns all supported intrusion settings for an MX network

Returns all supported intrusion settings for an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkApplianceSecurityIntrusion(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#getNetworkApplianceSecurityIntrusion");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkApplianceSecurityMalware"></a>
# **getNetworkApplianceSecurityMalware**
> Object getNetworkApplianceSecurityMalware(networkId)

Returns all supported malware settings for an MX network

Returns all supported malware settings for an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkApplianceSecurityMalware(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#getNetworkApplianceSecurityMalware");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkApplianceSettings"></a>
# **getNetworkApplianceSettings**
> GetNetworkApplianceSettings200Response getNetworkApplianceSettings(networkId)

Return the appliance settings for a network

Return the appliance settings for a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      GetNetworkApplianceSettings200Response result = apiInstance.getNetworkApplianceSettings(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#getNetworkApplianceSettings");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |

### Return type

[**GetNetworkApplianceSettings200Response**](GetNetworkApplianceSettings200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkApplianceSingleLan"></a>
# **getNetworkApplianceSingleLan**
> GetNetworkApplianceSingleLan200Response getNetworkApplianceSingleLan(networkId)

Return single LAN configuration

Return single LAN configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      GetNetworkApplianceSingleLan200Response result = apiInstance.getNetworkApplianceSingleLan(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#getNetworkApplianceSingleLan");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |

### Return type

[**GetNetworkApplianceSingleLan200Response**](GetNetworkApplianceSingleLan200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkApplianceSsid"></a>
# **getNetworkApplianceSsid**
> GetNetworkApplianceSsids200ResponseInner getNetworkApplianceSsid(networkId, number)

Return a single MX SSID

Return a single MX SSID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    try {
      GetNetworkApplianceSsids200ResponseInner result = apiInstance.getNetworkApplianceSsid(networkId, number);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#getNetworkApplianceSsid");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |
| **number** | **String**|  | |

### Return type

[**GetNetworkApplianceSsids200ResponseInner**](GetNetworkApplianceSsids200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkApplianceSsids"></a>
# **getNetworkApplianceSsids**
> List&lt;GetNetworkApplianceSsids200ResponseInner&gt; getNetworkApplianceSsids(networkId)

List the MX SSIDs in a network

List the MX SSIDs in a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<GetNetworkApplianceSsids200ResponseInner> result = apiInstance.getNetworkApplianceSsids(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#getNetworkApplianceSsids");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |

### Return type

[**List&lt;GetNetworkApplianceSsids200ResponseInner&gt;**](GetNetworkApplianceSsids200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkApplianceStaticRoute"></a>
# **getNetworkApplianceStaticRoute**
> Object getNetworkApplianceStaticRoute(networkId, staticRouteId)

Return a static route for an MX or teleworker network

Return a static route for an MX or teleworker network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String staticRouteId = "staticRouteId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkApplianceStaticRoute(networkId, staticRouteId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#getNetworkApplianceStaticRoute");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |
| **staticRouteId** | **String**|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkApplianceStaticRoutes"></a>
# **getNetworkApplianceStaticRoutes**
> List&lt;Object&gt; getNetworkApplianceStaticRoutes(networkId)

List the static routes for an MX or teleworker network

List the static routes for an MX or teleworker network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<Object> result = apiInstance.getNetworkApplianceStaticRoutes(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#getNetworkApplianceStaticRoutes");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |

### Return type

**List&lt;Object&gt;**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkApplianceTrafficShaping"></a>
# **getNetworkApplianceTrafficShaping**
> Object getNetworkApplianceTrafficShaping(networkId)

Display the traffic shaping settings for an MX network

Display the traffic shaping settings for an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkApplianceTrafficShaping(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#getNetworkApplianceTrafficShaping");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkApplianceTrafficShapingCustomPerformanceClass"></a>
# **getNetworkApplianceTrafficShapingCustomPerformanceClass**
> Object getNetworkApplianceTrafficShapingCustomPerformanceClass(networkId, customPerformanceClassId)

Return a custom performance class for an MX network

Return a custom performance class for an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String customPerformanceClassId = "customPerformanceClassId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkApplianceTrafficShapingCustomPerformanceClass(networkId, customPerformanceClassId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#getNetworkApplianceTrafficShapingCustomPerformanceClass");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |
| **customPerformanceClassId** | **String**|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkApplianceTrafficShapingCustomPerformanceClasses"></a>
# **getNetworkApplianceTrafficShapingCustomPerformanceClasses**
> List&lt;Object&gt; getNetworkApplianceTrafficShapingCustomPerformanceClasses(networkId)

List all custom performance classes for an MX network

List all custom performance classes for an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<Object> result = apiInstance.getNetworkApplianceTrafficShapingCustomPerformanceClasses(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#getNetworkApplianceTrafficShapingCustomPerformanceClasses");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |

### Return type

**List&lt;Object&gt;**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkApplianceTrafficShapingRules"></a>
# **getNetworkApplianceTrafficShapingRules**
> Object getNetworkApplianceTrafficShapingRules(networkId)

Display the traffic shaping settings rules for an MX network

Display the traffic shaping settings rules for an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkApplianceTrafficShapingRules(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#getNetworkApplianceTrafficShapingRules");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkApplianceTrafficShapingUplinkBandwidth"></a>
# **getNetworkApplianceTrafficShapingUplinkBandwidth**
> GetNetworkApplianceTrafficShapingUplinkBandwidth200Response getNetworkApplianceTrafficShapingUplinkBandwidth(networkId)

Returns the uplink bandwidth limits for your MX network

Returns the uplink bandwidth limits for your MX network. This may not reflect the affected device&#39;s hardware capabilities.  For more information on your device&#39;s hardware capabilities, please consult our MX Family Datasheet - [https://meraki.cisco.com/product-collateral/mx-family-datasheet/?file]

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      GetNetworkApplianceTrafficShapingUplinkBandwidth200Response result = apiInstance.getNetworkApplianceTrafficShapingUplinkBandwidth(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#getNetworkApplianceTrafficShapingUplinkBandwidth");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |

### Return type

[**GetNetworkApplianceTrafficShapingUplinkBandwidth200Response**](GetNetworkApplianceTrafficShapingUplinkBandwidth200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkApplianceTrafficShapingUplinkSelection"></a>
# **getNetworkApplianceTrafficShapingUplinkSelection**
> GetNetworkApplianceTrafficShapingUplinkSelection200Response getNetworkApplianceTrafficShapingUplinkSelection(networkId)

Show uplink selection settings for an MX network

Show uplink selection settings for an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      GetNetworkApplianceTrafficShapingUplinkSelection200Response result = apiInstance.getNetworkApplianceTrafficShapingUplinkSelection(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#getNetworkApplianceTrafficShapingUplinkSelection");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |

### Return type

[**GetNetworkApplianceTrafficShapingUplinkSelection200Response**](GetNetworkApplianceTrafficShapingUplinkSelection200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkApplianceUplinksUsageHistory"></a>
# **getNetworkApplianceUplinksUsageHistory**
> List&lt;Object&gt; getNetworkApplianceUplinksUsageHistory(networkId, t0, t1, timespan, resolution)

Get the sent and received bytes for each uplink of a network.

Get the sent and received bytes for each uplink of a network.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 365 days from today.
    String t1 = "t1_example"; // String | The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 10 minutes.
    Integer resolution = 56; // Integer | The time resolution in seconds for returned data. The valid resolutions are: 60, 300, 600, 1800, 3600, 86400. The default is 60.
    try {
      List<Object> result = apiInstance.getNetworkApplianceUplinksUsageHistory(networkId, t0, t1, timespan, resolution);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#getNetworkApplianceUplinksUsageHistory");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |
| **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 365 days from today. | [optional] |
| **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 31 days after t0. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 10 minutes. | [optional] |
| **resolution** | **Integer**| The time resolution in seconds for returned data. The valid resolutions are: 60, 300, 600, 1800, 3600, 86400. The default is 60. | [optional] |

### Return type

**List&lt;Object&gt;**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkApplianceVlan"></a>
# **getNetworkApplianceVlan**
> GetNetworkApplianceVlans200ResponseInner getNetworkApplianceVlan(networkId, vlanId)

Return a VLAN

Return a VLAN

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String vlanId = "vlanId_example"; // String | 
    try {
      GetNetworkApplianceVlans200ResponseInner result = apiInstance.getNetworkApplianceVlan(networkId, vlanId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#getNetworkApplianceVlan");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |
| **vlanId** | **String**|  | |

### Return type

[**GetNetworkApplianceVlans200ResponseInner**](GetNetworkApplianceVlans200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkApplianceVlans"></a>
# **getNetworkApplianceVlans**
> List&lt;GetNetworkApplianceVlans200ResponseInner&gt; getNetworkApplianceVlans(networkId)

List the VLANs for an MX network

List the VLANs for an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<GetNetworkApplianceVlans200ResponseInner> result = apiInstance.getNetworkApplianceVlans(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#getNetworkApplianceVlans");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |

### Return type

[**List&lt;GetNetworkApplianceVlans200ResponseInner&gt;**](GetNetworkApplianceVlans200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkApplianceVlansSettings"></a>
# **getNetworkApplianceVlansSettings**
> Object getNetworkApplianceVlansSettings(networkId)

Returns the enabled status of VLANs for the network

Returns the enabled status of VLANs for the network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkApplianceVlansSettings(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#getNetworkApplianceVlansSettings");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkApplianceVpnBgp"></a>
# **getNetworkApplianceVpnBgp**
> Object getNetworkApplianceVpnBgp(networkId)

Return a Hub BGP Configuration

Return a Hub BGP Configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkApplianceVpnBgp(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#getNetworkApplianceVpnBgp");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkApplianceVpnSiteToSiteVpn"></a>
# **getNetworkApplianceVpnSiteToSiteVpn**
> GetNetworkApplianceVpnSiteToSiteVpn200Response getNetworkApplianceVpnSiteToSiteVpn(networkId)

Return the site-to-site VPN settings of a network

Return the site-to-site VPN settings of a network. Only valid for MX networks.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      GetNetworkApplianceVpnSiteToSiteVpn200Response result = apiInstance.getNetworkApplianceVpnSiteToSiteVpn(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#getNetworkApplianceVpnSiteToSiteVpn");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |

### Return type

[**GetNetworkApplianceVpnSiteToSiteVpn200Response**](GetNetworkApplianceVpnSiteToSiteVpn200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkApplianceWarmSpare"></a>
# **getNetworkApplianceWarmSpare**
> Object getNetworkApplianceWarmSpare(networkId)

Return MX warm spare settings

Return MX warm spare settings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkApplianceWarmSpare(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#getNetworkApplianceWarmSpare");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getOrganizationApplianceSecurityEvents"></a>
# **getOrganizationApplianceSecurityEvents**
> List&lt;Object&gt; getOrganizationApplianceSecurityEvents(organizationId, t0, t1, timespan, perPage, startingAfter, endingBefore, sortOrder)

List the security events for an organization

List the security events for an organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. Data is gathered after the specified t0 value. The maximum lookback period is 365 days from today.
    String t1 = "t1_example"; // String | The end of the timespan for the data. t1 can be a maximum of 365 days after t0.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 365 days. The default is 31 days.
    Integer perPage = 56; // Integer | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
    String startingAfter = "startingAfter_example"; // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String endingBefore = "endingBefore_example"; // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String sortOrder = "ascending"; // String | Sorted order of security events based on event detection time. Order options are 'ascending' or 'descending'. Default is ascending order.
    try {
      List<Object> result = apiInstance.getOrganizationApplianceSecurityEvents(organizationId, t0, t1, timespan, perPage, startingAfter, endingBefore, sortOrder);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#getOrganizationApplianceSecurityEvents");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **organizationId** | **String**|  | |
| **t0** | **String**| The beginning of the timespan for the data. Data is gathered after the specified t0 value. The maximum lookback period is 365 days from today. | [optional] |
| **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 365 days after t0. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 365 days. The default is 31 days. | [optional] |
| **perPage** | **Integer**| The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100. | [optional] |
| **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **sortOrder** | **String**| Sorted order of security events based on event detection time. Order options are &#39;ascending&#39; or &#39;descending&#39;. Default is ascending order. | [optional] [enum: ascending, descending] |

### Return type

**List&lt;Object&gt;**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  * Link - A comma-separated list of first, last, prev, and next relative links used for subsequent paginated requests. <br>  |

<a id="getOrganizationApplianceSecurityIntrusion"></a>
# **getOrganizationApplianceSecurityIntrusion**
> Object getOrganizationApplianceSecurityIntrusion(organizationId)

Returns all supported intrusion settings for an organization

Returns all supported intrusion settings for an organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    try {
      Object result = apiInstance.getOrganizationApplianceSecurityIntrusion(organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#getOrganizationApplianceSecurityIntrusion");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **organizationId** | **String**|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getOrganizationApplianceUplinkStatuses"></a>
# **getOrganizationApplianceUplinkStatuses**
> List&lt;Object&gt; getOrganizationApplianceUplinkStatuses(organizationId, perPage, startingAfter, endingBefore, networkIds, serials, iccids)

List the uplink status of every Meraki MX and Z series appliances in the organization

List the uplink status of every Meraki MX and Z series appliances in the organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    Integer perPage = 56; // Integer | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    String startingAfter = "startingAfter_example"; // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String endingBefore = "endingBefore_example"; // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    List<String> networkIds = Arrays.asList(); // List<String> | A list of network IDs. The returned devices will be filtered to only include these networks.
    List<String> serials = Arrays.asList(); // List<String> | A list of serial numbers. The returned devices will be filtered to only include these serials.
    List<String> iccids = Arrays.asList(); // List<String> | A list of ICCIDs. The returned devices will be filtered to only include these ICCIDs.
    try {
      List<Object> result = apiInstance.getOrganizationApplianceUplinkStatuses(organizationId, perPage, startingAfter, endingBefore, networkIds, serials, iccids);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#getOrganizationApplianceUplinkStatuses");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **organizationId** | **String**|  | |
| **perPage** | **Integer**| The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. | [optional] |
| **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **networkIds** | [**List&lt;String&gt;**](String.md)| A list of network IDs. The returned devices will be filtered to only include these networks. | [optional] |
| **serials** | [**List&lt;String&gt;**](String.md)| A list of serial numbers. The returned devices will be filtered to only include these serials. | [optional] |
| **iccids** | [**List&lt;String&gt;**](String.md)| A list of ICCIDs. The returned devices will be filtered to only include these ICCIDs. | [optional] |

### Return type

**List&lt;Object&gt;**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  * Link - A comma-separated list of first, last, prev, and next relative links used for subsequent paginated requests. <br>  |

<a id="getOrganizationApplianceVpnStats"></a>
# **getOrganizationApplianceVpnStats**
> List&lt;Object&gt; getOrganizationApplianceVpnStats(organizationId, perPage, startingAfter, endingBefore, networkIds, t0, t1, timespan)

Show VPN history stat for networks in an organization

Show VPN history stat for networks in an organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    Integer perPage = 56; // Integer | The number of entries per page returned. Acceptable range is 3 - 300. Default is 300.
    String startingAfter = "startingAfter_example"; // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String endingBefore = "endingBefore_example"; // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    List<String> networkIds = Arrays.asList(); // List<String> | A list of Meraki network IDs to filter results to contain only specified networks. E.g.: networkIds[]=N_12345678&networkIds[]=L_3456
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    String t1 = "t1_example"; // String | The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    try {
      List<Object> result = apiInstance.getOrganizationApplianceVpnStats(organizationId, perPage, startingAfter, endingBefore, networkIds, t0, t1, timespan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#getOrganizationApplianceVpnStats");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **organizationId** | **String**|  | |
| **perPage** | **Integer**| The number of entries per page returned. Acceptable range is 3 - 300. Default is 300. | [optional] |
| **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **networkIds** | [**List&lt;String&gt;**](String.md)| A list of Meraki network IDs to filter results to contain only specified networks. E.g.: networkIds[]&#x3D;N_12345678&amp;networkIds[]&#x3D;L_3456 | [optional] |
| **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 31 days from today. | [optional] |
| **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 31 days after t0. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day. | [optional] |

### Return type

**List&lt;Object&gt;**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  * Link - A comma-separated list of first, last, prev, and next relative links used for subsequent paginated requests. <br>  |

<a id="getOrganizationApplianceVpnStatuses"></a>
# **getOrganizationApplianceVpnStatuses**
> List&lt;Object&gt; getOrganizationApplianceVpnStatuses(organizationId, perPage, startingAfter, endingBefore, networkIds)

Show VPN status for networks in an organization

Show VPN status for networks in an organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    Integer perPage = 56; // Integer | The number of entries per page returned. Acceptable range is 3 - 300. Default is 300.
    String startingAfter = "startingAfter_example"; // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String endingBefore = "endingBefore_example"; // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    List<String> networkIds = Arrays.asList(); // List<String> | A list of Meraki network IDs to filter results to contain only specified networks. E.g.: networkIds[]=N_12345678&networkIds[]=L_3456
    try {
      List<Object> result = apiInstance.getOrganizationApplianceVpnStatuses(organizationId, perPage, startingAfter, endingBefore, networkIds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#getOrganizationApplianceVpnStatuses");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **organizationId** | **String**|  | |
| **perPage** | **Integer**| The number of entries per page returned. Acceptable range is 3 - 300. Default is 300. | [optional] |
| **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **networkIds** | [**List&lt;String&gt;**](String.md)| A list of Meraki network IDs to filter results to contain only specified networks. E.g.: networkIds[]&#x3D;N_12345678&amp;networkIds[]&#x3D;L_3456 | [optional] |

### Return type

**List&lt;Object&gt;**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  * Link - A comma-separated list of first, last, prev, and next relative links used for subsequent paginated requests. <br>  |

<a id="getOrganizationApplianceVpnThirdPartyVPNPeers"></a>
# **getOrganizationApplianceVpnThirdPartyVPNPeers**
> GetOrganizationApplianceVpnThirdPartyVPNPeers200Response getOrganizationApplianceVpnThirdPartyVPNPeers(organizationId)

Return the third party VPN peers for an organization

Return the third party VPN peers for an organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    try {
      GetOrganizationApplianceVpnThirdPartyVPNPeers200Response result = apiInstance.getOrganizationApplianceVpnThirdPartyVPNPeers(organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#getOrganizationApplianceVpnThirdPartyVPNPeers");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **organizationId** | **String**|  | |

### Return type

[**GetOrganizationApplianceVpnThirdPartyVPNPeers200Response**](GetOrganizationApplianceVpnThirdPartyVPNPeers200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getOrganizationApplianceVpnVpnFirewallRules"></a>
# **getOrganizationApplianceVpnVpnFirewallRules**
> Object getOrganizationApplianceVpnVpnFirewallRules(organizationId)

Return the firewall rules for an organization&#39;s site-to-site VPN

Return the firewall rules for an organization&#39;s site-to-site VPN

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    try {
      Object result = apiInstance.getOrganizationApplianceVpnVpnFirewallRules(organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#getOrganizationApplianceVpnVpnFirewallRules");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **organizationId** | **String**|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="swapNetworkApplianceWarmSpare"></a>
# **swapNetworkApplianceWarmSpare**
> Object swapNetworkApplianceWarmSpare(networkId)

Swap MX primary and warm spare appliances

Swap MX primary and warm spare appliances

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.swapNetworkApplianceWarmSpare(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#swapNetworkApplianceWarmSpare");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateDeviceApplianceUplinksSettings"></a>
# **updateDeviceApplianceUplinksSettings**
> GetDeviceApplianceUplinksSettings200Response updateDeviceApplianceUplinksSettings(serial, updateDeviceApplianceUplinksSettingsRequest)

Update the uplink settings for an MX appliance

Update the uplink settings for an MX appliance

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String serial = "serial_example"; // String | 
    UpdateDeviceApplianceUplinksSettingsRequest updateDeviceApplianceUplinksSettingsRequest = new UpdateDeviceApplianceUplinksSettingsRequest(); // UpdateDeviceApplianceUplinksSettingsRequest | 
    try {
      GetDeviceApplianceUplinksSettings200Response result = apiInstance.updateDeviceApplianceUplinksSettings(serial, updateDeviceApplianceUplinksSettingsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#updateDeviceApplianceUplinksSettings");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **serial** | **String**|  | |
| **updateDeviceApplianceUplinksSettingsRequest** | [**UpdateDeviceApplianceUplinksSettingsRequest**](UpdateDeviceApplianceUplinksSettingsRequest.md)|  | |

### Return type

[**GetDeviceApplianceUplinksSettings200Response**](GetDeviceApplianceUplinksSettings200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkApplianceConnectivityMonitoringDestinations"></a>
# **updateNetworkApplianceConnectivityMonitoringDestinations**
> Object updateNetworkApplianceConnectivityMonitoringDestinations(networkId, updateNetworkApplianceConnectivityMonitoringDestinationsRequest)

Update the connectivity testing destinations for an MX network

Update the connectivity testing destinations for an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkApplianceConnectivityMonitoringDestinationsRequest updateNetworkApplianceConnectivityMonitoringDestinationsRequest = new UpdateNetworkApplianceConnectivityMonitoringDestinationsRequest(); // UpdateNetworkApplianceConnectivityMonitoringDestinationsRequest | 
    try {
      Object result = apiInstance.updateNetworkApplianceConnectivityMonitoringDestinations(networkId, updateNetworkApplianceConnectivityMonitoringDestinationsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#updateNetworkApplianceConnectivityMonitoringDestinations");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |
| **updateNetworkApplianceConnectivityMonitoringDestinationsRequest** | [**UpdateNetworkApplianceConnectivityMonitoringDestinationsRequest**](UpdateNetworkApplianceConnectivityMonitoringDestinationsRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkApplianceContentFiltering"></a>
# **updateNetworkApplianceContentFiltering**
> Object updateNetworkApplianceContentFiltering(networkId, updateNetworkApplianceContentFilteringRequest)

Update the content filtering settings for an MX network

Update the content filtering settings for an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkApplianceContentFilteringRequest updateNetworkApplianceContentFilteringRequest = new UpdateNetworkApplianceContentFilteringRequest(); // UpdateNetworkApplianceContentFilteringRequest | 
    try {
      Object result = apiInstance.updateNetworkApplianceContentFiltering(networkId, updateNetworkApplianceContentFilteringRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#updateNetworkApplianceContentFiltering");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |
| **updateNetworkApplianceContentFilteringRequest** | [**UpdateNetworkApplianceContentFilteringRequest**](UpdateNetworkApplianceContentFilteringRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkApplianceFirewallCellularFirewallRules"></a>
# **updateNetworkApplianceFirewallCellularFirewallRules**
> Object updateNetworkApplianceFirewallCellularFirewallRules(networkId, updateNetworkApplianceFirewallCellularFirewallRulesRequest)

Update the cellular firewall rules of an MX network

Update the cellular firewall rules of an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkApplianceFirewallCellularFirewallRulesRequest updateNetworkApplianceFirewallCellularFirewallRulesRequest = new UpdateNetworkApplianceFirewallCellularFirewallRulesRequest(); // UpdateNetworkApplianceFirewallCellularFirewallRulesRequest | 
    try {
      Object result = apiInstance.updateNetworkApplianceFirewallCellularFirewallRules(networkId, updateNetworkApplianceFirewallCellularFirewallRulesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#updateNetworkApplianceFirewallCellularFirewallRules");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |
| **updateNetworkApplianceFirewallCellularFirewallRulesRequest** | [**UpdateNetworkApplianceFirewallCellularFirewallRulesRequest**](UpdateNetworkApplianceFirewallCellularFirewallRulesRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkApplianceFirewallFirewalledService"></a>
# **updateNetworkApplianceFirewallFirewalledService**
> Object updateNetworkApplianceFirewallFirewalledService(networkId, service, updateNetworkApplianceFirewallFirewalledServiceRequest)

Updates the accessibility settings for the given service (&#39;ICMP&#39;, &#39;web&#39;, or &#39;SNMP&#39;)

Updates the accessibility settings for the given service (&#39;ICMP&#39;, &#39;web&#39;, or &#39;SNMP&#39;)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String service = "service_example"; // String | 
    UpdateNetworkApplianceFirewallFirewalledServiceRequest updateNetworkApplianceFirewallFirewalledServiceRequest = new UpdateNetworkApplianceFirewallFirewalledServiceRequest(); // UpdateNetworkApplianceFirewallFirewalledServiceRequest | 
    try {
      Object result = apiInstance.updateNetworkApplianceFirewallFirewalledService(networkId, service, updateNetworkApplianceFirewallFirewalledServiceRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#updateNetworkApplianceFirewallFirewalledService");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |
| **service** | **String**|  | |
| **updateNetworkApplianceFirewallFirewalledServiceRequest** | [**UpdateNetworkApplianceFirewallFirewalledServiceRequest**](UpdateNetworkApplianceFirewallFirewalledServiceRequest.md)|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkApplianceFirewallInboundCellularFirewallRules"></a>
# **updateNetworkApplianceFirewallInboundCellularFirewallRules**
> List&lt;Object&gt; updateNetworkApplianceFirewallInboundCellularFirewallRules(networkId, updateNetworkApplianceFirewallCellularFirewallRulesRequest)

Update the inbound cellular firewall rules of an MX network

Update the inbound cellular firewall rules of an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkApplianceFirewallCellularFirewallRulesRequest updateNetworkApplianceFirewallCellularFirewallRulesRequest = new UpdateNetworkApplianceFirewallCellularFirewallRulesRequest(); // UpdateNetworkApplianceFirewallCellularFirewallRulesRequest | 
    try {
      List<Object> result = apiInstance.updateNetworkApplianceFirewallInboundCellularFirewallRules(networkId, updateNetworkApplianceFirewallCellularFirewallRulesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#updateNetworkApplianceFirewallInboundCellularFirewallRules");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |
| **updateNetworkApplianceFirewallCellularFirewallRulesRequest** | [**UpdateNetworkApplianceFirewallCellularFirewallRulesRequest**](UpdateNetworkApplianceFirewallCellularFirewallRulesRequest.md)|  | [optional] |

### Return type

**List&lt;Object&gt;**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkApplianceFirewallInboundFirewallRules"></a>
# **updateNetworkApplianceFirewallInboundFirewallRules**
> Object updateNetworkApplianceFirewallInboundFirewallRules(networkId, updateNetworkApplianceFirewallInboundFirewallRulesRequest)

Update the inbound firewall rules of an MX network

Update the inbound firewall rules of an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkApplianceFirewallInboundFirewallRulesRequest updateNetworkApplianceFirewallInboundFirewallRulesRequest = new UpdateNetworkApplianceFirewallInboundFirewallRulesRequest(); // UpdateNetworkApplianceFirewallInboundFirewallRulesRequest | 
    try {
      Object result = apiInstance.updateNetworkApplianceFirewallInboundFirewallRules(networkId, updateNetworkApplianceFirewallInboundFirewallRulesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#updateNetworkApplianceFirewallInboundFirewallRules");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |
| **updateNetworkApplianceFirewallInboundFirewallRulesRequest** | [**UpdateNetworkApplianceFirewallInboundFirewallRulesRequest**](UpdateNetworkApplianceFirewallInboundFirewallRulesRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkApplianceFirewallL3FirewallRules"></a>
# **updateNetworkApplianceFirewallL3FirewallRules**
> Object updateNetworkApplianceFirewallL3FirewallRules(networkId, updateNetworkApplianceFirewallInboundFirewallRulesRequest)

Update the L3 firewall rules of an MX network

Update the L3 firewall rules of an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkApplianceFirewallInboundFirewallRulesRequest updateNetworkApplianceFirewallInboundFirewallRulesRequest = new UpdateNetworkApplianceFirewallInboundFirewallRulesRequest(); // UpdateNetworkApplianceFirewallInboundFirewallRulesRequest | 
    try {
      Object result = apiInstance.updateNetworkApplianceFirewallL3FirewallRules(networkId, updateNetworkApplianceFirewallInboundFirewallRulesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#updateNetworkApplianceFirewallL3FirewallRules");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |
| **updateNetworkApplianceFirewallInboundFirewallRulesRequest** | [**UpdateNetworkApplianceFirewallInboundFirewallRulesRequest**](UpdateNetworkApplianceFirewallInboundFirewallRulesRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkApplianceFirewallL7FirewallRules"></a>
# **updateNetworkApplianceFirewallL7FirewallRules**
> Object updateNetworkApplianceFirewallL7FirewallRules(networkId, updateNetworkApplianceFirewallL7FirewallRulesRequest)

Update the MX L7 firewall rules for an MX network

Update the MX L7 firewall rules for an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkApplianceFirewallL7FirewallRulesRequest updateNetworkApplianceFirewallL7FirewallRulesRequest = new UpdateNetworkApplianceFirewallL7FirewallRulesRequest(); // UpdateNetworkApplianceFirewallL7FirewallRulesRequest | 
    try {
      Object result = apiInstance.updateNetworkApplianceFirewallL7FirewallRules(networkId, updateNetworkApplianceFirewallL7FirewallRulesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#updateNetworkApplianceFirewallL7FirewallRules");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |
| **updateNetworkApplianceFirewallL7FirewallRulesRequest** | [**UpdateNetworkApplianceFirewallL7FirewallRulesRequest**](UpdateNetworkApplianceFirewallL7FirewallRulesRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkApplianceFirewallOneToManyNatRules"></a>
# **updateNetworkApplianceFirewallOneToManyNatRules**
> Object updateNetworkApplianceFirewallOneToManyNatRules(networkId, updateNetworkApplianceFirewallOneToManyNatRulesRequest)

Set the 1:Many NAT mapping rules for an MX network

Set the 1:Many NAT mapping rules for an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkApplianceFirewallOneToManyNatRulesRequest updateNetworkApplianceFirewallOneToManyNatRulesRequest = new UpdateNetworkApplianceFirewallOneToManyNatRulesRequest(); // UpdateNetworkApplianceFirewallOneToManyNatRulesRequest | 
    try {
      Object result = apiInstance.updateNetworkApplianceFirewallOneToManyNatRules(networkId, updateNetworkApplianceFirewallOneToManyNatRulesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#updateNetworkApplianceFirewallOneToManyNatRules");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |
| **updateNetworkApplianceFirewallOneToManyNatRulesRequest** | [**UpdateNetworkApplianceFirewallOneToManyNatRulesRequest**](UpdateNetworkApplianceFirewallOneToManyNatRulesRequest.md)|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkApplianceFirewallOneToOneNatRules"></a>
# **updateNetworkApplianceFirewallOneToOneNatRules**
> Object updateNetworkApplianceFirewallOneToOneNatRules(networkId, updateNetworkApplianceFirewallOneToOneNatRulesRequest)

Set the 1:1 NAT mapping rules for an MX network

Set the 1:1 NAT mapping rules for an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkApplianceFirewallOneToOneNatRulesRequest updateNetworkApplianceFirewallOneToOneNatRulesRequest = new UpdateNetworkApplianceFirewallOneToOneNatRulesRequest(); // UpdateNetworkApplianceFirewallOneToOneNatRulesRequest | 
    try {
      Object result = apiInstance.updateNetworkApplianceFirewallOneToOneNatRules(networkId, updateNetworkApplianceFirewallOneToOneNatRulesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#updateNetworkApplianceFirewallOneToOneNatRules");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |
| **updateNetworkApplianceFirewallOneToOneNatRulesRequest** | [**UpdateNetworkApplianceFirewallOneToOneNatRulesRequest**](UpdateNetworkApplianceFirewallOneToOneNatRulesRequest.md)|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkApplianceFirewallPortForwardingRules"></a>
# **updateNetworkApplianceFirewallPortForwardingRules**
> Object updateNetworkApplianceFirewallPortForwardingRules(networkId, updateNetworkApplianceFirewallPortForwardingRulesRequest)

Update the port forwarding rules for an MX network

Update the port forwarding rules for an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkApplianceFirewallPortForwardingRulesRequest updateNetworkApplianceFirewallPortForwardingRulesRequest = new UpdateNetworkApplianceFirewallPortForwardingRulesRequest(); // UpdateNetworkApplianceFirewallPortForwardingRulesRequest | 
    try {
      Object result = apiInstance.updateNetworkApplianceFirewallPortForwardingRules(networkId, updateNetworkApplianceFirewallPortForwardingRulesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#updateNetworkApplianceFirewallPortForwardingRules");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |
| **updateNetworkApplianceFirewallPortForwardingRulesRequest** | [**UpdateNetworkApplianceFirewallPortForwardingRulesRequest**](UpdateNetworkApplianceFirewallPortForwardingRulesRequest.md)|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkApplianceFirewallSettings"></a>
# **updateNetworkApplianceFirewallSettings**
> Object updateNetworkApplianceFirewallSettings(networkId, updateNetworkApplianceFirewallSettingsRequest)

Update the firewall settings for this network

Update the firewall settings for this network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkApplianceFirewallSettingsRequest updateNetworkApplianceFirewallSettingsRequest = new UpdateNetworkApplianceFirewallSettingsRequest(); // UpdateNetworkApplianceFirewallSettingsRequest | 
    try {
      Object result = apiInstance.updateNetworkApplianceFirewallSettings(networkId, updateNetworkApplianceFirewallSettingsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#updateNetworkApplianceFirewallSettings");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |
| **updateNetworkApplianceFirewallSettingsRequest** | [**UpdateNetworkApplianceFirewallSettingsRequest**](UpdateNetworkApplianceFirewallSettingsRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkAppliancePort"></a>
# **updateNetworkAppliancePort**
> GetNetworkAppliancePorts200ResponseInner updateNetworkAppliancePort(networkId, portId, updateNetworkAppliancePortRequest)

Update the per-port VLAN settings for a single MX port.

Update the per-port VLAN settings for a single MX port.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String portId = "portId_example"; // String | 
    UpdateNetworkAppliancePortRequest updateNetworkAppliancePortRequest = new UpdateNetworkAppliancePortRequest(); // UpdateNetworkAppliancePortRequest | 
    try {
      GetNetworkAppliancePorts200ResponseInner result = apiInstance.updateNetworkAppliancePort(networkId, portId, updateNetworkAppliancePortRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#updateNetworkAppliancePort");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |
| **portId** | **String**|  | |
| **updateNetworkAppliancePortRequest** | [**UpdateNetworkAppliancePortRequest**](UpdateNetworkAppliancePortRequest.md)|  | [optional] |

### Return type

[**GetNetworkAppliancePorts200ResponseInner**](GetNetworkAppliancePorts200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkAppliancePrefixesDelegatedStatic"></a>
# **updateNetworkAppliancePrefixesDelegatedStatic**
> Object updateNetworkAppliancePrefixesDelegatedStatic(networkId, staticDelegatedPrefixId, updateNetworkAppliancePrefixesDelegatedStaticRequest)

Update a static delegated prefix from a network

Update a static delegated prefix from a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String staticDelegatedPrefixId = "staticDelegatedPrefixId_example"; // String | 
    UpdateNetworkAppliancePrefixesDelegatedStaticRequest updateNetworkAppliancePrefixesDelegatedStaticRequest = new UpdateNetworkAppliancePrefixesDelegatedStaticRequest(); // UpdateNetworkAppliancePrefixesDelegatedStaticRequest | 
    try {
      Object result = apiInstance.updateNetworkAppliancePrefixesDelegatedStatic(networkId, staticDelegatedPrefixId, updateNetworkAppliancePrefixesDelegatedStaticRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#updateNetworkAppliancePrefixesDelegatedStatic");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |
| **staticDelegatedPrefixId** | **String**|  | |
| **updateNetworkAppliancePrefixesDelegatedStaticRequest** | [**UpdateNetworkAppliancePrefixesDelegatedStaticRequest**](UpdateNetworkAppliancePrefixesDelegatedStaticRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkApplianceSecurityIntrusion"></a>
# **updateNetworkApplianceSecurityIntrusion**
> Object updateNetworkApplianceSecurityIntrusion(networkId, updateNetworkApplianceSecurityIntrusionRequest)

Set the supported intrusion settings for an MX network

Set the supported intrusion settings for an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkApplianceSecurityIntrusionRequest updateNetworkApplianceSecurityIntrusionRequest = new UpdateNetworkApplianceSecurityIntrusionRequest(); // UpdateNetworkApplianceSecurityIntrusionRequest | 
    try {
      Object result = apiInstance.updateNetworkApplianceSecurityIntrusion(networkId, updateNetworkApplianceSecurityIntrusionRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#updateNetworkApplianceSecurityIntrusion");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |
| **updateNetworkApplianceSecurityIntrusionRequest** | [**UpdateNetworkApplianceSecurityIntrusionRequest**](UpdateNetworkApplianceSecurityIntrusionRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkApplianceSecurityMalware"></a>
# **updateNetworkApplianceSecurityMalware**
> Object updateNetworkApplianceSecurityMalware(networkId, updateNetworkApplianceSecurityMalwareRequest)

Set the supported malware settings for an MX network

Set the supported malware settings for an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkApplianceSecurityMalwareRequest updateNetworkApplianceSecurityMalwareRequest = new UpdateNetworkApplianceSecurityMalwareRequest(); // UpdateNetworkApplianceSecurityMalwareRequest | 
    try {
      Object result = apiInstance.updateNetworkApplianceSecurityMalware(networkId, updateNetworkApplianceSecurityMalwareRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#updateNetworkApplianceSecurityMalware");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |
| **updateNetworkApplianceSecurityMalwareRequest** | [**UpdateNetworkApplianceSecurityMalwareRequest**](UpdateNetworkApplianceSecurityMalwareRequest.md)|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkApplianceSettings"></a>
# **updateNetworkApplianceSettings**
> GetNetworkApplianceSettings200Response updateNetworkApplianceSettings(networkId, updateNetworkApplianceSettingsRequest)

Update the appliance settings for a network

Update the appliance settings for a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkApplianceSettingsRequest updateNetworkApplianceSettingsRequest = new UpdateNetworkApplianceSettingsRequest(); // UpdateNetworkApplianceSettingsRequest | 
    try {
      GetNetworkApplianceSettings200Response result = apiInstance.updateNetworkApplianceSettings(networkId, updateNetworkApplianceSettingsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#updateNetworkApplianceSettings");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |
| **updateNetworkApplianceSettingsRequest** | [**UpdateNetworkApplianceSettingsRequest**](UpdateNetworkApplianceSettingsRequest.md)|  | [optional] |

### Return type

[**GetNetworkApplianceSettings200Response**](GetNetworkApplianceSettings200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkApplianceSingleLan"></a>
# **updateNetworkApplianceSingleLan**
> GetNetworkApplianceSingleLan200Response updateNetworkApplianceSingleLan(networkId, updateNetworkApplianceSingleLanRequest)

Update single LAN configuration

Update single LAN configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkApplianceSingleLanRequest updateNetworkApplianceSingleLanRequest = new UpdateNetworkApplianceSingleLanRequest(); // UpdateNetworkApplianceSingleLanRequest | 
    try {
      GetNetworkApplianceSingleLan200Response result = apiInstance.updateNetworkApplianceSingleLan(networkId, updateNetworkApplianceSingleLanRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#updateNetworkApplianceSingleLan");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |
| **updateNetworkApplianceSingleLanRequest** | [**UpdateNetworkApplianceSingleLanRequest**](UpdateNetworkApplianceSingleLanRequest.md)|  | [optional] |

### Return type

[**GetNetworkApplianceSingleLan200Response**](GetNetworkApplianceSingleLan200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkApplianceSsid"></a>
# **updateNetworkApplianceSsid**
> GetNetworkApplianceSsids200ResponseInner updateNetworkApplianceSsid(networkId, number, updateNetworkApplianceSsidRequest)

Update the attributes of an MX SSID

Update the attributes of an MX SSID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    UpdateNetworkApplianceSsidRequest updateNetworkApplianceSsidRequest = new UpdateNetworkApplianceSsidRequest(); // UpdateNetworkApplianceSsidRequest | 
    try {
      GetNetworkApplianceSsids200ResponseInner result = apiInstance.updateNetworkApplianceSsid(networkId, number, updateNetworkApplianceSsidRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#updateNetworkApplianceSsid");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |
| **number** | **String**|  | |
| **updateNetworkApplianceSsidRequest** | [**UpdateNetworkApplianceSsidRequest**](UpdateNetworkApplianceSsidRequest.md)|  | [optional] |

### Return type

[**GetNetworkApplianceSsids200ResponseInner**](GetNetworkApplianceSsids200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkApplianceStaticRoute"></a>
# **updateNetworkApplianceStaticRoute**
> Object updateNetworkApplianceStaticRoute(networkId, staticRouteId, updateNetworkApplianceStaticRouteRequest)

Update a static route for an MX or teleworker network

Update a static route for an MX or teleworker network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String staticRouteId = "staticRouteId_example"; // String | 
    UpdateNetworkApplianceStaticRouteRequest updateNetworkApplianceStaticRouteRequest = new UpdateNetworkApplianceStaticRouteRequest(); // UpdateNetworkApplianceStaticRouteRequest | 
    try {
      Object result = apiInstance.updateNetworkApplianceStaticRoute(networkId, staticRouteId, updateNetworkApplianceStaticRouteRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#updateNetworkApplianceStaticRoute");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |
| **staticRouteId** | **String**|  | |
| **updateNetworkApplianceStaticRouteRequest** | [**UpdateNetworkApplianceStaticRouteRequest**](UpdateNetworkApplianceStaticRouteRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkApplianceTrafficShaping"></a>
# **updateNetworkApplianceTrafficShaping**
> Object updateNetworkApplianceTrafficShaping(networkId, updateNetworkApplianceTrafficShapingRequest)

Update the traffic shaping settings for an MX network

Update the traffic shaping settings for an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkApplianceTrafficShapingRequest updateNetworkApplianceTrafficShapingRequest = new UpdateNetworkApplianceTrafficShapingRequest(); // UpdateNetworkApplianceTrafficShapingRequest | 
    try {
      Object result = apiInstance.updateNetworkApplianceTrafficShaping(networkId, updateNetworkApplianceTrafficShapingRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#updateNetworkApplianceTrafficShaping");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |
| **updateNetworkApplianceTrafficShapingRequest** | [**UpdateNetworkApplianceTrafficShapingRequest**](UpdateNetworkApplianceTrafficShapingRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkApplianceTrafficShapingCustomPerformanceClass"></a>
# **updateNetworkApplianceTrafficShapingCustomPerformanceClass**
> Object updateNetworkApplianceTrafficShapingCustomPerformanceClass(networkId, customPerformanceClassId, updateNetworkApplianceTrafficShapingCustomPerformanceClassRequest)

Update a custom performance class for an MX network

Update a custom performance class for an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String customPerformanceClassId = "customPerformanceClassId_example"; // String | 
    UpdateNetworkApplianceTrafficShapingCustomPerformanceClassRequest updateNetworkApplianceTrafficShapingCustomPerformanceClassRequest = new UpdateNetworkApplianceTrafficShapingCustomPerformanceClassRequest(); // UpdateNetworkApplianceTrafficShapingCustomPerformanceClassRequest | 
    try {
      Object result = apiInstance.updateNetworkApplianceTrafficShapingCustomPerformanceClass(networkId, customPerformanceClassId, updateNetworkApplianceTrafficShapingCustomPerformanceClassRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#updateNetworkApplianceTrafficShapingCustomPerformanceClass");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |
| **customPerformanceClassId** | **String**|  | |
| **updateNetworkApplianceTrafficShapingCustomPerformanceClassRequest** | [**UpdateNetworkApplianceTrafficShapingCustomPerformanceClassRequest**](UpdateNetworkApplianceTrafficShapingCustomPerformanceClassRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkApplianceTrafficShapingRules"></a>
# **updateNetworkApplianceTrafficShapingRules**
> Object updateNetworkApplianceTrafficShapingRules(networkId, updateNetworkApplianceTrafficShapingRulesRequest)

Update the traffic shaping settings rules for an MX network

Update the traffic shaping settings rules for an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkApplianceTrafficShapingRulesRequest updateNetworkApplianceTrafficShapingRulesRequest = new UpdateNetworkApplianceTrafficShapingRulesRequest(); // UpdateNetworkApplianceTrafficShapingRulesRequest | 
    try {
      Object result = apiInstance.updateNetworkApplianceTrafficShapingRules(networkId, updateNetworkApplianceTrafficShapingRulesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#updateNetworkApplianceTrafficShapingRules");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |
| **updateNetworkApplianceTrafficShapingRulesRequest** | [**UpdateNetworkApplianceTrafficShapingRulesRequest**](UpdateNetworkApplianceTrafficShapingRulesRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkApplianceTrafficShapingUplinkBandwidth"></a>
# **updateNetworkApplianceTrafficShapingUplinkBandwidth**
> Object updateNetworkApplianceTrafficShapingUplinkBandwidth(networkId, updateNetworkApplianceTrafficShapingUplinkBandwidthRequest)

Updates the uplink bandwidth settings for your MX network.

Updates the uplink bandwidth settings for your MX network.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkApplianceTrafficShapingUplinkBandwidthRequest updateNetworkApplianceTrafficShapingUplinkBandwidthRequest = new UpdateNetworkApplianceTrafficShapingUplinkBandwidthRequest(); // UpdateNetworkApplianceTrafficShapingUplinkBandwidthRequest | 
    try {
      Object result = apiInstance.updateNetworkApplianceTrafficShapingUplinkBandwidth(networkId, updateNetworkApplianceTrafficShapingUplinkBandwidthRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#updateNetworkApplianceTrafficShapingUplinkBandwidth");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |
| **updateNetworkApplianceTrafficShapingUplinkBandwidthRequest** | [**UpdateNetworkApplianceTrafficShapingUplinkBandwidthRequest**](UpdateNetworkApplianceTrafficShapingUplinkBandwidthRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkApplianceTrafficShapingUplinkSelection"></a>
# **updateNetworkApplianceTrafficShapingUplinkSelection**
> GetNetworkApplianceTrafficShapingUplinkSelection200Response updateNetworkApplianceTrafficShapingUplinkSelection(networkId, updateNetworkApplianceTrafficShapingUplinkSelectionRequest)

Update uplink selection settings for an MX network

Update uplink selection settings for an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkApplianceTrafficShapingUplinkSelectionRequest updateNetworkApplianceTrafficShapingUplinkSelectionRequest = new UpdateNetworkApplianceTrafficShapingUplinkSelectionRequest(); // UpdateNetworkApplianceTrafficShapingUplinkSelectionRequest | 
    try {
      GetNetworkApplianceTrafficShapingUplinkSelection200Response result = apiInstance.updateNetworkApplianceTrafficShapingUplinkSelection(networkId, updateNetworkApplianceTrafficShapingUplinkSelectionRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#updateNetworkApplianceTrafficShapingUplinkSelection");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |
| **updateNetworkApplianceTrafficShapingUplinkSelectionRequest** | [**UpdateNetworkApplianceTrafficShapingUplinkSelectionRequest**](UpdateNetworkApplianceTrafficShapingUplinkSelectionRequest.md)|  | [optional] |

### Return type

[**GetNetworkApplianceTrafficShapingUplinkSelection200Response**](GetNetworkApplianceTrafficShapingUplinkSelection200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkApplianceVlan"></a>
# **updateNetworkApplianceVlan**
> GetNetworkApplianceVlans200ResponseInner updateNetworkApplianceVlan(networkId, vlanId, updateNetworkApplianceVlanRequest)

Update a VLAN

Update a VLAN

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String vlanId = "vlanId_example"; // String | 
    UpdateNetworkApplianceVlanRequest updateNetworkApplianceVlanRequest = new UpdateNetworkApplianceVlanRequest(); // UpdateNetworkApplianceVlanRequest | 
    try {
      GetNetworkApplianceVlans200ResponseInner result = apiInstance.updateNetworkApplianceVlan(networkId, vlanId, updateNetworkApplianceVlanRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#updateNetworkApplianceVlan");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |
| **vlanId** | **String**|  | |
| **updateNetworkApplianceVlanRequest** | [**UpdateNetworkApplianceVlanRequest**](UpdateNetworkApplianceVlanRequest.md)|  | [optional] |

### Return type

[**GetNetworkApplianceVlans200ResponseInner**](GetNetworkApplianceVlans200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkApplianceVlansSettings"></a>
# **updateNetworkApplianceVlansSettings**
> Object updateNetworkApplianceVlansSettings(networkId, updateNetworkApplianceVlansSettingsRequest)

Enable/Disable VLANs for the given network

Enable/Disable VLANs for the given network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkApplianceVlansSettingsRequest updateNetworkApplianceVlansSettingsRequest = new UpdateNetworkApplianceVlansSettingsRequest(); // UpdateNetworkApplianceVlansSettingsRequest | 
    try {
      Object result = apiInstance.updateNetworkApplianceVlansSettings(networkId, updateNetworkApplianceVlansSettingsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#updateNetworkApplianceVlansSettings");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |
| **updateNetworkApplianceVlansSettingsRequest** | [**UpdateNetworkApplianceVlansSettingsRequest**](UpdateNetworkApplianceVlansSettingsRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkApplianceVpnBgp"></a>
# **updateNetworkApplianceVpnBgp**
> Object updateNetworkApplianceVpnBgp(networkId, updateNetworkApplianceVpnBgpRequest)

Update a Hub BGP Configuration

Update a Hub BGP Configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkApplianceVpnBgpRequest updateNetworkApplianceVpnBgpRequest = new UpdateNetworkApplianceVpnBgpRequest(); // UpdateNetworkApplianceVpnBgpRequest | 
    try {
      Object result = apiInstance.updateNetworkApplianceVpnBgp(networkId, updateNetworkApplianceVpnBgpRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#updateNetworkApplianceVpnBgp");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |
| **updateNetworkApplianceVpnBgpRequest** | [**UpdateNetworkApplianceVpnBgpRequest**](UpdateNetworkApplianceVpnBgpRequest.md)|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkApplianceVpnSiteToSiteVpn"></a>
# **updateNetworkApplianceVpnSiteToSiteVpn**
> GetNetworkApplianceVpnSiteToSiteVpn200Response updateNetworkApplianceVpnSiteToSiteVpn(networkId, updateNetworkApplianceVpnSiteToSiteVpnRequest)

Update the site-to-site VPN settings of a network

Update the site-to-site VPN settings of a network. Only valid for MX networks in NAT mode.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkApplianceVpnSiteToSiteVpnRequest updateNetworkApplianceVpnSiteToSiteVpnRequest = new UpdateNetworkApplianceVpnSiteToSiteVpnRequest(); // UpdateNetworkApplianceVpnSiteToSiteVpnRequest | 
    try {
      GetNetworkApplianceVpnSiteToSiteVpn200Response result = apiInstance.updateNetworkApplianceVpnSiteToSiteVpn(networkId, updateNetworkApplianceVpnSiteToSiteVpnRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#updateNetworkApplianceVpnSiteToSiteVpn");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |
| **updateNetworkApplianceVpnSiteToSiteVpnRequest** | [**UpdateNetworkApplianceVpnSiteToSiteVpnRequest**](UpdateNetworkApplianceVpnSiteToSiteVpnRequest.md)|  | |

### Return type

[**GetNetworkApplianceVpnSiteToSiteVpn200Response**](GetNetworkApplianceVpnSiteToSiteVpn200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkApplianceWarmSpare"></a>
# **updateNetworkApplianceWarmSpare**
> Object updateNetworkApplianceWarmSpare(networkId, updateNetworkApplianceWarmSpareRequest)

Update MX warm spare settings

Update MX warm spare settings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkApplianceWarmSpareRequest updateNetworkApplianceWarmSpareRequest = new UpdateNetworkApplianceWarmSpareRequest(); // UpdateNetworkApplianceWarmSpareRequest | 
    try {
      Object result = apiInstance.updateNetworkApplianceWarmSpare(networkId, updateNetworkApplianceWarmSpareRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#updateNetworkApplianceWarmSpare");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **networkId** | **String**|  | |
| **updateNetworkApplianceWarmSpareRequest** | [**UpdateNetworkApplianceWarmSpareRequest**](UpdateNetworkApplianceWarmSpareRequest.md)|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateOrganizationApplianceSecurityIntrusion"></a>
# **updateOrganizationApplianceSecurityIntrusion**
> Object updateOrganizationApplianceSecurityIntrusion(organizationId, updateOrganizationApplianceSecurityIntrusionRequest)

Sets supported intrusion settings for an organization

Sets supported intrusion settings for an organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    UpdateOrganizationApplianceSecurityIntrusionRequest updateOrganizationApplianceSecurityIntrusionRequest = new UpdateOrganizationApplianceSecurityIntrusionRequest(); // UpdateOrganizationApplianceSecurityIntrusionRequest | 
    try {
      Object result = apiInstance.updateOrganizationApplianceSecurityIntrusion(organizationId, updateOrganizationApplianceSecurityIntrusionRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#updateOrganizationApplianceSecurityIntrusion");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **organizationId** | **String**|  | |
| **updateOrganizationApplianceSecurityIntrusionRequest** | [**UpdateOrganizationApplianceSecurityIntrusionRequest**](UpdateOrganizationApplianceSecurityIntrusionRequest.md)|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateOrganizationApplianceVpnThirdPartyVPNPeers"></a>
# **updateOrganizationApplianceVpnThirdPartyVPNPeers**
> GetOrganizationApplianceVpnThirdPartyVPNPeers200Response updateOrganizationApplianceVpnThirdPartyVPNPeers(organizationId, updateOrganizationApplianceVpnThirdPartyVPNPeersRequest)

Update the third party VPN peers for an organization

Update the third party VPN peers for an organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    UpdateOrganizationApplianceVpnThirdPartyVPNPeersRequest updateOrganizationApplianceVpnThirdPartyVPNPeersRequest = new UpdateOrganizationApplianceVpnThirdPartyVPNPeersRequest(); // UpdateOrganizationApplianceVpnThirdPartyVPNPeersRequest | 
    try {
      GetOrganizationApplianceVpnThirdPartyVPNPeers200Response result = apiInstance.updateOrganizationApplianceVpnThirdPartyVPNPeers(organizationId, updateOrganizationApplianceVpnThirdPartyVPNPeersRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#updateOrganizationApplianceVpnThirdPartyVPNPeers");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **organizationId** | **String**|  | |
| **updateOrganizationApplianceVpnThirdPartyVPNPeersRequest** | [**UpdateOrganizationApplianceVpnThirdPartyVPNPeersRequest**](UpdateOrganizationApplianceVpnThirdPartyVPNPeersRequest.md)|  | |

### Return type

[**GetOrganizationApplianceVpnThirdPartyVPNPeers200Response**](GetOrganizationApplianceVpnThirdPartyVPNPeers200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateOrganizationApplianceVpnVpnFirewallRules"></a>
# **updateOrganizationApplianceVpnVpnFirewallRules**
> Object updateOrganizationApplianceVpnVpnFirewallRules(organizationId, updateOrganizationApplianceVpnVpnFirewallRulesRequest)

Update the firewall rules of an organization&#39;s site-to-site VPN

Update the firewall rules of an organization&#39;s site-to-site VPN

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApplianceApi apiInstance = new ApplianceApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    UpdateOrganizationApplianceVpnVpnFirewallRulesRequest updateOrganizationApplianceVpnVpnFirewallRulesRequest = new UpdateOrganizationApplianceVpnVpnFirewallRulesRequest(); // UpdateOrganizationApplianceVpnVpnFirewallRulesRequest | 
    try {
      Object result = apiInstance.updateOrganizationApplianceVpnVpnFirewallRules(organizationId, updateOrganizationApplianceVpnVpnFirewallRulesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceApi#updateOrganizationApplianceVpnVpnFirewallRules");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **organizationId** | **String**|  | |
| **updateOrganizationApplianceVpnVpnFirewallRulesRequest** | [**UpdateOrganizationApplianceVpnVpnFirewallRulesRequest**](UpdateOrganizationApplianceVpnVpnFirewallRulesRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

