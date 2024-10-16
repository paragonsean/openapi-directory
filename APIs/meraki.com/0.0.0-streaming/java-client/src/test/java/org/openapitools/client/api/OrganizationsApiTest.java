/*
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 23 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 0.0.0-streaming
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.ClaimIntoOrganizationRequest;
import org.openapitools.client.model.CloneOrganizationRequest;
import org.openapitools.client.model.UpdateOrganizationThirdPartyVPNPeersRequest;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for OrganizationsApi
 */
@Disabled
public class OrganizationsApiTest {

    private final OrganizationsApi api = new OrganizationsApi();

    /**
     * Claim a list of devices, licenses, and/or orders into an organization
     *
     * Claim a list of devices, licenses, and/or orders into an organization. When claiming by order, all devices and licenses in the order will be claimed; licenses will be added to the organization and devices will be placed in the organization&#39;s inventory.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void claimIntoOrganizationTest() throws ApiException {
        String organizationId = null;
        ClaimIntoOrganizationRequest claimIntoOrganizationRequest = null;
        Object response = api.claimIntoOrganization(organizationId, claimIntoOrganizationRequest);
        // TODO: test validations
    }

    /**
     * Create a new organization by cloning the addressed organization
     *
     * Create a new organization by cloning the addressed organization
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void cloneOrganizationTest() throws ApiException {
        String organizationId = null;
        CloneOrganizationRequest cloneOrganizationRequest = null;
        Object response = api.cloneOrganization(organizationId, cloneOrganizationRequest);
        // TODO: test validations
    }

    /**
     * Return an organization
     *
     * Return an organization
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getOrganizationTest() throws ApiException {
        String organizationId = null;
        Object response = api.getOrganization(organizationId);
        // TODO: test validations
    }

    /**
     * List the status of every Meraki device in the organization
     *
     * List the status of every Meraki device in the organization
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getOrganizationDeviceStatusesTest() throws ApiException {
        String organizationId = null;
        List<Object> response = api.getOrganizationDeviceStatuses(organizationId);
        // TODO: test validations
    }

    /**
     * Return the inventory for an organization
     *
     * Return the inventory for an organization
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getOrganizationInventoryTest() throws ApiException {
        String organizationId = null;
        Boolean includeLicenseInfo = null;
        List<Object> response = api.getOrganizationInventory(organizationId, includeLicenseInfo);
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
    public void getOrganizationThirdPartyVPNPeersTest() throws ApiException {
        String organizationId = null;
        List<Object> response = api.getOrganizationThirdPartyVPNPeers(organizationId);
        // TODO: test validations
    }

    /**
     * Return the uplink loss and latency for every MX in the organization from at latest 2 minutes ago
     *
     * Return the uplink loss and latency for every MX in the organization from at latest 2 minutes ago
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getOrganizationUplinksLossAndLatencyTest() throws ApiException {
        String organizationId = null;
        String t0 = null;
        String t1 = null;
        Float timespan = null;
        String uplink = null;
        String ip = null;
        List<Object> response = api.getOrganizationUplinksLossAndLatency(organizationId, t0, t1, timespan, uplink, ip);
        // TODO: test validations
    }

    /**
     * List the organizations that the user has privileges on
     *
     * List the organizations that the user has privileges on
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getOrganizationsTest() throws ApiException {
        List<Object> response = api.getOrganizations();
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
    public void updateOrganizationThirdPartyVPNPeersTest() throws ApiException {
        String organizationId = null;
        UpdateOrganizationThirdPartyVPNPeersRequest updateOrganizationThirdPartyVPNPeersRequest = null;
        List<Object> response = api.updateOrganizationThirdPartyVPNPeers(organizationId, updateOrganizationThirdPartyVPNPeersRequest);
        // TODO: test validations
    }

}
