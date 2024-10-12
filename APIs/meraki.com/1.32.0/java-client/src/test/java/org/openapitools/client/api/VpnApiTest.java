/*
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 05 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 1.32.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.GetNetworkApplianceVpnSiteToSiteVpn200Response;
import org.openapitools.client.model.GetOrganizationApplianceVpnThirdPartyVPNPeers200Response;
import org.openapitools.client.model.UpdateNetworkApplianceVpnBgpRequest;
import org.openapitools.client.model.UpdateNetworkApplianceVpnSiteToSiteVpnRequest;
import org.openapitools.client.model.UpdateNetworkWirelessSsidVpnRequest;
import org.openapitools.client.model.UpdateOrganizationApplianceVpnThirdPartyVPNPeersRequest;
import org.openapitools.client.model.UpdateOrganizationApplianceVpnVpnFirewallRulesRequest;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for VpnApi
 */
@Disabled
public class VpnApiTest {

    private final VpnApi api = new VpnApi();

    /**
     * Return a Hub BGP Configuration
     *
     * Return a Hub BGP Configuration
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getNetworkApplianceVpnBgp_1Test() throws ApiException {
        String networkId = null;
        Object response = api.getNetworkApplianceVpnBgp_1(networkId);
        // TODO: test validations
    }

    /**
     * Return the site-to-site VPN settings of a network
     *
     * Return the site-to-site VPN settings of a network. Only valid for MX networks.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getNetworkApplianceVpnSiteToSiteVpn_1Test() throws ApiException {
        String networkId = null;
        GetNetworkApplianceVpnSiteToSiteVpn200Response response = api.getNetworkApplianceVpnSiteToSiteVpn_1(networkId);
        // TODO: test validations
    }

    /**
     * List the VPN settings for the SSID.
     *
     * List the VPN settings for the SSID.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getNetworkWirelessSsidVpn_2Test() throws ApiException {
        String networkId = null;
        String number = null;
        Object response = api.getNetworkWirelessSsidVpn_2(networkId, number);
        // TODO: test validations
    }

    /**
     * Show VPN history stat for networks in an organization
     *
     * Show VPN history stat for networks in an organization
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getOrganizationApplianceVpnStats_1Test() throws ApiException {
        String organizationId = null;
        Integer perPage = null;
        String startingAfter = null;
        String endingBefore = null;
        List<String> networkIds = null;
        String t0 = null;
        String t1 = null;
        Float timespan = null;
        List<Object> response = api.getOrganizationApplianceVpnStats_1(organizationId, perPage, startingAfter, endingBefore, networkIds, t0, t1, timespan);
        // TODO: test validations
    }

    /**
     * Show VPN status for networks in an organization
     *
     * Show VPN status for networks in an organization
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getOrganizationApplianceVpnStatuses_1Test() throws ApiException {
        String organizationId = null;
        Integer perPage = null;
        String startingAfter = null;
        String endingBefore = null;
        List<String> networkIds = null;
        List<Object> response = api.getOrganizationApplianceVpnStatuses_1(organizationId, perPage, startingAfter, endingBefore, networkIds);
        // TODO: test validations
    }

    /**
     * Return the third party VPN peers for an organization
     *
     * Return the third party VPN peers for an organization
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getOrganizationApplianceVpnThirdPartyVPNPeers_1Test() throws ApiException {
        String organizationId = null;
        GetOrganizationApplianceVpnThirdPartyVPNPeers200Response response = api.getOrganizationApplianceVpnThirdPartyVPNPeers_1(organizationId);
        // TODO: test validations
    }

    /**
     * Return the firewall rules for an organization&#39;s site-to-site VPN
     *
     * Return the firewall rules for an organization&#39;s site-to-site VPN
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getOrganizationApplianceVpnVpnFirewallRules_1Test() throws ApiException {
        String organizationId = null;
        Object response = api.getOrganizationApplianceVpnVpnFirewallRules_1(organizationId);
        // TODO: test validations
    }

    /**
     * Update a Hub BGP Configuration
     *
     * Update a Hub BGP Configuration
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateNetworkApplianceVpnBgp_1Test() throws ApiException {
        String networkId = null;
        UpdateNetworkApplianceVpnBgpRequest updateNetworkApplianceVpnBgpRequest = null;
        Object response = api.updateNetworkApplianceVpnBgp_1(networkId, updateNetworkApplianceVpnBgpRequest);
        // TODO: test validations
    }

    /**
     * Update the site-to-site VPN settings of a network
     *
     * Update the site-to-site VPN settings of a network. Only valid for MX networks in NAT mode.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateNetworkApplianceVpnSiteToSiteVpn_1Test() throws ApiException {
        String networkId = null;
        UpdateNetworkApplianceVpnSiteToSiteVpnRequest updateNetworkApplianceVpnSiteToSiteVpnRequest = null;
        GetNetworkApplianceVpnSiteToSiteVpn200Response response = api.updateNetworkApplianceVpnSiteToSiteVpn_1(networkId, updateNetworkApplianceVpnSiteToSiteVpnRequest);
        // TODO: test validations
    }

    /**
     * Update the VPN settings for the SSID
     *
     * Update the VPN settings for the SSID
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateNetworkWirelessSsidVpn_2Test() throws ApiException {
        String networkId = null;
        String number = null;
        UpdateNetworkWirelessSsidVpnRequest updateNetworkWirelessSsidVpnRequest = null;
        Object response = api.updateNetworkWirelessSsidVpn_2(networkId, number, updateNetworkWirelessSsidVpnRequest);
        // TODO: test validations
    }

    /**
     * Update the third party VPN peers for an organization
     *
     * Update the third party VPN peers for an organization
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateOrganizationApplianceVpnThirdPartyVPNPeers_1Test() throws ApiException {
        String organizationId = null;
        UpdateOrganizationApplianceVpnThirdPartyVPNPeersRequest updateOrganizationApplianceVpnThirdPartyVPNPeersRequest = null;
        GetOrganizationApplianceVpnThirdPartyVPNPeers200Response response = api.updateOrganizationApplianceVpnThirdPartyVPNPeers_1(organizationId, updateOrganizationApplianceVpnThirdPartyVPNPeersRequest);
        // TODO: test validations
    }

    /**
     * Update the firewall rules of an organization&#39;s site-to-site VPN
     *
     * Update the firewall rules of an organization&#39;s site-to-site VPN
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateOrganizationApplianceVpnVpnFirewallRules_1Test() throws ApiException {
        String organizationId = null;
        UpdateOrganizationApplianceVpnVpnFirewallRulesRequest updateOrganizationApplianceVpnVpnFirewallRulesRequest = null;
        Object response = api.updateOrganizationApplianceVpnVpnFirewallRules_1(organizationId, updateOrganizationApplianceVpnVpnFirewallRulesRequest);
        // TODO: test validations
    }

}
