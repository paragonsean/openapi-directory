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
import org.openapitools.client.model.GetNetworkCellularGatewayDhcp200Response;
import org.openapitools.client.model.GetOrganizationCellularGatewayUplinkStatuses200ResponseInner;
import org.openapitools.client.model.UpdateDeviceCellularGatewayLanRequest;
import org.openapitools.client.model.UpdateDeviceCellularGatewayPortForwardingRulesRequest;
import org.openapitools.client.model.UpdateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest;
import org.openapitools.client.model.UpdateNetworkCellularGatewayDhcpRequest;
import org.openapitools.client.model.UpdateNetworkCellularGatewaySubnetPoolRequest;
import org.openapitools.client.model.UpdateNetworkCellularGatewayUplinkRequest;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for CellularGatewayApi
 */
@Disabled
public class CellularGatewayApiTest {

    private final CellularGatewayApi api = new CellularGatewayApi();

    /**
     * Show the LAN Settings of a MG
     *
     * Show the LAN Settings of a MG
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getDeviceCellularGatewayLanTest() throws ApiException {
        String serial = null;
        Object response = api.getDeviceCellularGatewayLan(serial);
        // TODO: test validations
    }

    /**
     * Returns the port forwarding rules for a single MG.
     *
     * Returns the port forwarding rules for a single MG.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getDeviceCellularGatewayPortForwardingRulesTest() throws ApiException {
        String serial = null;
        Object response = api.getDeviceCellularGatewayPortForwardingRules(serial);
        // TODO: test validations
    }

    /**
     * Return the connectivity testing destinations for an MG network
     *
     * Return the connectivity testing destinations for an MG network
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getNetworkCellularGatewayConnectivityMonitoringDestinationsTest() throws ApiException {
        String networkId = null;
        Object response = api.getNetworkCellularGatewayConnectivityMonitoringDestinations(networkId);
        // TODO: test validations
    }

    /**
     * List common DHCP settings of MGs
     *
     * List common DHCP settings of MGs
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getNetworkCellularGatewayDhcpTest() throws ApiException {
        String networkId = null;
        GetNetworkCellularGatewayDhcp200Response response = api.getNetworkCellularGatewayDhcp(networkId);
        // TODO: test validations
    }

    /**
     * Return the subnet pool and mask configured for MGs in the network.
     *
     * Return the subnet pool and mask configured for MGs in the network.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getNetworkCellularGatewaySubnetPoolTest() throws ApiException {
        String networkId = null;
        Object response = api.getNetworkCellularGatewaySubnetPool(networkId);
        // TODO: test validations
    }

    /**
     * Returns the uplink settings for your MG network.
     *
     * Returns the uplink settings for your MG network.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getNetworkCellularGatewayUplinkTest() throws ApiException {
        String networkId = null;
        Object response = api.getNetworkCellularGatewayUplink(networkId);
        // TODO: test validations
    }

    /**
     * List the uplink status of every Meraki MG cellular gateway in the organization
     *
     * List the uplink status of every Meraki MG cellular gateway in the organization
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getOrganizationCellularGatewayUplinkStatusesTest() throws ApiException {
        String organizationId = null;
        Integer perPage = null;
        String startingAfter = null;
        String endingBefore = null;
        List<String> networkIds = null;
        List<String> serials = null;
        List<String> iccids = null;
        List<GetOrganizationCellularGatewayUplinkStatuses200ResponseInner> response = api.getOrganizationCellularGatewayUplinkStatuses(organizationId, perPage, startingAfter, endingBefore, networkIds, serials, iccids);
        // TODO: test validations
    }

    /**
     * Update the LAN Settings for a single MG.
     *
     * Update the LAN Settings for a single MG.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateDeviceCellularGatewayLanTest() throws ApiException {
        String serial = null;
        UpdateDeviceCellularGatewayLanRequest updateDeviceCellularGatewayLanRequest = null;
        Object response = api.updateDeviceCellularGatewayLan(serial, updateDeviceCellularGatewayLanRequest);
        // TODO: test validations
    }

    /**
     * Updates the port forwarding rules for a single MG.
     *
     * Updates the port forwarding rules for a single MG.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateDeviceCellularGatewayPortForwardingRulesTest() throws ApiException {
        String serial = null;
        UpdateDeviceCellularGatewayPortForwardingRulesRequest updateDeviceCellularGatewayPortForwardingRulesRequest = null;
        Object response = api.updateDeviceCellularGatewayPortForwardingRules(serial, updateDeviceCellularGatewayPortForwardingRulesRequest);
        // TODO: test validations
    }

    /**
     * Update the connectivity testing destinations for an MG network
     *
     * Update the connectivity testing destinations for an MG network
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateNetworkCellularGatewayConnectivityMonitoringDestinationsTest() throws ApiException {
        String networkId = null;
        UpdateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest updateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest = null;
        Object response = api.updateNetworkCellularGatewayConnectivityMonitoringDestinations(networkId, updateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest);
        // TODO: test validations
    }

    /**
     * Update common DHCP settings of MGs
     *
     * Update common DHCP settings of MGs
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateNetworkCellularGatewayDhcpTest() throws ApiException {
        String networkId = null;
        UpdateNetworkCellularGatewayDhcpRequest updateNetworkCellularGatewayDhcpRequest = null;
        GetNetworkCellularGatewayDhcp200Response response = api.updateNetworkCellularGatewayDhcp(networkId, updateNetworkCellularGatewayDhcpRequest);
        // TODO: test validations
    }

    /**
     * Update the subnet pool and mask configuration for MGs in the network.
     *
     * Update the subnet pool and mask configuration for MGs in the network.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateNetworkCellularGatewaySubnetPoolTest() throws ApiException {
        String networkId = null;
        UpdateNetworkCellularGatewaySubnetPoolRequest updateNetworkCellularGatewaySubnetPoolRequest = null;
        Object response = api.updateNetworkCellularGatewaySubnetPool(networkId, updateNetworkCellularGatewaySubnetPoolRequest);
        // TODO: test validations
    }

    /**
     * Updates the uplink settings for your MG network.
     *
     * Updates the uplink settings for your MG network.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateNetworkCellularGatewayUplinkTest() throws ApiException {
        String networkId = null;
        UpdateNetworkCellularGatewayUplinkRequest updateNetworkCellularGatewayUplinkRequest = null;
        Object response = api.updateNetworkCellularGatewayUplink(networkId, updateNetworkCellularGatewayUplinkRequest);
        // TODO: test validations
    }

}
