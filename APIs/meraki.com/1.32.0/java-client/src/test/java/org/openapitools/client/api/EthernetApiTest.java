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
import org.openapitools.client.model.GetOrganizationWirelessDevicesEthernetStatuses200ResponseInner;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for EthernetApi
 */
@Disabled
public class EthernetApiTest {

    private final EthernetApi api = new EthernetApi();

    /**
     * Endpoint to see power status for wireless devices
     *
     * Endpoint to see power status for wireless devices
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getOrganizationWirelessDevicesEthernetStatuses_2Test() throws ApiException {
        String organizationId = null;
        Integer perPage = null;
        String startingAfter = null;
        String endingBefore = null;
        List<String> networkIds = null;
        List<GetOrganizationWirelessDevicesEthernetStatuses200ResponseInner> response = api.getOrganizationWirelessDevicesEthernetStatuses_2(organizationId, perPage, startingAfter, endingBefore, networkIds);
        // TODO: test validations
    }

}
