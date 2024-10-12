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
import org.openapitools.client.model.GetNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice200ResponseInner;
import org.openapitools.client.model.GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInner;
import org.openapitools.client.model.GetOrganizationDevicesUplinksAddressesByDevice200ResponseInner;
import org.openapitools.client.model.GetOrganizationFirmwareUpgradesByDevice200ResponseInner;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for ByDeviceApi
 */
@Disabled
public class ByDeviceApiTest {

    private final ByDeviceApi api = new ByDeviceApi();

    /**
     * Return the devices that have a Dynamic ARP Inspection warning and their warnings
     *
     * Return the devices that have a Dynamic ARP Inspection warning and their warnings
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice_4Test() throws ApiException {
        String networkId = null;
        Integer perPage = null;
        String startingAfter = null;
        String endingBefore = null;
        List<GetNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice200ResponseInner> response = api.getNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice_4(networkId, perPage, startingAfter, endingBefore);
        // TODO: test validations
    }

    /**
     * List the power status information for devices in an organization
     *
     * List the power status information for devices in an organization. The data returned by this endpoint is updated every 5 minutes.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getOrganizationDevicesPowerModulesStatusesByDevice_4Test() throws ApiException {
        String organizationId = null;
        Integer perPage = null;
        String startingAfter = null;
        String endingBefore = null;
        List<String> networkIds = null;
        List<String> productTypes = null;
        List<String> serials = null;
        List<String> tags = null;
        String tagsFilterType = null;
        List<GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInner> response = api.getOrganizationDevicesPowerModulesStatusesByDevice_4(organizationId, perPage, startingAfter, endingBefore, networkIds, productTypes, serials, tags, tagsFilterType);
        // TODO: test validations
    }

    /**
     * List the current uplink addresses for devices in an organization.
     *
     * List the current uplink addresses for devices in an organization.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getOrganizationDevicesUplinksAddressesByDevice_4Test() throws ApiException {
        String organizationId = null;
        Integer perPage = null;
        String startingAfter = null;
        String endingBefore = null;
        List<String> networkIds = null;
        List<String> productTypes = null;
        List<String> serials = null;
        List<String> tags = null;
        String tagsFilterType = null;
        List<GetOrganizationDevicesUplinksAddressesByDevice200ResponseInner> response = api.getOrganizationDevicesUplinksAddressesByDevice_4(organizationId, perPage, startingAfter, endingBefore, networkIds, productTypes, serials, tags, tagsFilterType);
        // TODO: test validations
    }

    /**
     * Get firmware upgrade status for the filtered devices
     *
     * Get firmware upgrade status for the filtered devices
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getOrganizationFirmwareUpgradesByDevice_3Test() throws ApiException {
        String organizationId = null;
        Integer perPage = null;
        String startingAfter = null;
        String endingBefore = null;
        List<String> networkIds = null;
        List<String> serials = null;
        List<String> macs = null;
        List<String> firmwareUpgradeIds = null;
        List<String> firmwareUpgradeBatchIds = null;
        List<GetOrganizationFirmwareUpgradesByDevice200ResponseInner> response = api.getOrganizationFirmwareUpgradesByDevice_3(organizationId, perPage, startingAfter, endingBefore, networkIds, serials, macs, firmwareUpgradeIds, firmwareUpgradeBatchIds);
        // TODO: test validations
    }

}
