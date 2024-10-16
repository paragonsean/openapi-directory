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
import org.openapitools.client.model.CreateNetworkFirmwareUpgradesStagedEventRequest;
import org.openapitools.client.model.GetNetworkEvents200Response;
import org.openapitools.client.model.GetNetworkEventsEventTypes200ResponseInner;
import org.openapitools.client.model.GetNetworkFirmwareUpgradesStagedEvents200Response;
import org.openapitools.client.model.RollbacksNetworkFirmwareUpgradesStagedEventsRequest;
import org.openapitools.client.model.UpdateNetworkFirmwareUpgradesStagedEventsRequest;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for EventsApi
 */
@Disabled
public class EventsApiTest {

    private final EventsApi api = new EventsApi();

    /**
     * Create a Staged Upgrade Event for a network
     *
     * Create a Staged Upgrade Event for a network
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createNetworkFirmwareUpgradesStagedEvent_3Test() throws ApiException {
        String networkId = null;
        CreateNetworkFirmwareUpgradesStagedEventRequest createNetworkFirmwareUpgradesStagedEventRequest = null;
        GetNetworkFirmwareUpgradesStagedEvents200Response response = api.createNetworkFirmwareUpgradesStagedEvent_3(networkId, createNetworkFirmwareUpgradesStagedEventRequest);
        // TODO: test validations
    }

    /**
     * Postpone by 1 week all pending staged upgrade stages for a network
     *
     * Postpone by 1 week all pending staged upgrade stages for a network
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deferNetworkFirmwareUpgradesStagedEvents_3Test() throws ApiException {
        String networkId = null;
        GetNetworkFirmwareUpgradesStagedEvents200Response response = api.deferNetworkFirmwareUpgradesStagedEvents_3(networkId);
        // TODO: test validations
    }

    /**
     * List the security events for a client
     *
     * List the security events for a client. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getNetworkApplianceClientSecurityEvents_3Test() throws ApiException {
        String networkId = null;
        String clientId = null;
        String t0 = null;
        String t1 = null;
        Float timespan = null;
        Integer perPage = null;
        String startingAfter = null;
        String endingBefore = null;
        String sortOrder = null;
        List<Object> response = api.getNetworkApplianceClientSecurityEvents_3(networkId, clientId, t0, t1, timespan, perPage, startingAfter, endingBefore, sortOrder);
        // TODO: test validations
    }

    /**
     * List the security events for a network
     *
     * List the security events for a network
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getNetworkApplianceSecurityEvents_2Test() throws ApiException {
        String networkId = null;
        String t0 = null;
        String t1 = null;
        Float timespan = null;
        Integer perPage = null;
        String startingAfter = null;
        String endingBefore = null;
        String sortOrder = null;
        List<Object> response = api.getNetworkApplianceSecurityEvents_2(networkId, t0, t1, timespan, perPage, startingAfter, endingBefore, sortOrder);
        // TODO: test validations
    }

    /**
     * List the event type to human-readable description
     *
     * List the event type to human-readable description
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getNetworkEventsEventTypes_1Test() throws ApiException {
        String networkId = null;
        List<GetNetworkEventsEventTypes200ResponseInner> response = api.getNetworkEventsEventTypes_1(networkId);
        // TODO: test validations
    }

    /**
     * List the events for the network
     *
     * List the events for the network
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getNetworkEvents_1Test() throws ApiException {
        String networkId = null;
        String productType = null;
        List<String> includedEventTypes = null;
        List<String> excludedEventTypes = null;
        String deviceMac = null;
        String deviceSerial = null;
        String deviceName = null;
        String clientIp = null;
        String clientMac = null;
        String clientName = null;
        String smDeviceMac = null;
        String smDeviceName = null;
        Integer perPage = null;
        String startingAfter = null;
        String endingBefore = null;
        GetNetworkEvents200Response response = api.getNetworkEvents_1(networkId, productType, includedEventTypes, excludedEventTypes, deviceMac, deviceSerial, deviceName, clientIp, clientMac, clientName, smDeviceMac, smDeviceName, perPage, startingAfter, endingBefore);
        // TODO: test validations
    }

    /**
     * Get the Staged Upgrade Event from a network
     *
     * Get the Staged Upgrade Event from a network
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getNetworkFirmwareUpgradesStagedEvents_3Test() throws ApiException {
        String networkId = null;
        GetNetworkFirmwareUpgradesStagedEvents200Response response = api.getNetworkFirmwareUpgradesStagedEvents_3(networkId);
        // TODO: test validations
    }

    /**
     * List the security events for an organization
     *
     * List the security events for an organization
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getOrganizationApplianceSecurityEvents_2Test() throws ApiException {
        String organizationId = null;
        String t0 = null;
        String t1 = null;
        Float timespan = null;
        Integer perPage = null;
        String startingAfter = null;
        String endingBefore = null;
        String sortOrder = null;
        List<Object> response = api.getOrganizationApplianceSecurityEvents_2(organizationId, t0, t1, timespan, perPage, startingAfter, endingBefore, sortOrder);
        // TODO: test validations
    }

    /**
     * Rollback a Staged Upgrade Event for a network
     *
     * Rollback a Staged Upgrade Event for a network
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void rollbacksNetworkFirmwareUpgradesStagedEvents_3Test() throws ApiException {
        String networkId = null;
        RollbacksNetworkFirmwareUpgradesStagedEventsRequest rollbacksNetworkFirmwareUpgradesStagedEventsRequest = null;
        GetNetworkFirmwareUpgradesStagedEvents200Response response = api.rollbacksNetworkFirmwareUpgradesStagedEvents_3(networkId, rollbacksNetworkFirmwareUpgradesStagedEventsRequest);
        // TODO: test validations
    }

    /**
     * Update the Staged Upgrade Event for a network
     *
     * Update the Staged Upgrade Event for a network
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateNetworkFirmwareUpgradesStagedEvents_3Test() throws ApiException {
        String networkId = null;
        UpdateNetworkFirmwareUpgradesStagedEventsRequest updateNetworkFirmwareUpgradesStagedEventsRequest = null;
        GetNetworkFirmwareUpgradesStagedEvents200Response response = api.updateNetworkFirmwareUpgradesStagedEvents_3(networkId, updateNetworkFirmwareUpgradesStagedEventsRequest);
        // TODO: test validations
    }

}
