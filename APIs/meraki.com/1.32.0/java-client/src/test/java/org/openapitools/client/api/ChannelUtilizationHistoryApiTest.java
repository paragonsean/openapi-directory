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
import org.openapitools.client.model.GetNetworkWirelessChannelUtilizationHistory200ResponseInner;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for ChannelUtilizationHistoryApi
 */
@Disabled
public class ChannelUtilizationHistoryApiTest {

    private final ChannelUtilizationHistoryApi api = new ChannelUtilizationHistoryApi();

    /**
     * Return AP channel utilization over time for a device or network client
     *
     * Return AP channel utilization over time for a device or network client
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getNetworkWirelessChannelUtilizationHistory_1Test() throws ApiException {
        String networkId = null;
        String t0 = null;
        String t1 = null;
        Float timespan = null;
        Integer resolution = null;
        Boolean autoResolution = null;
        String clientId = null;
        String deviceSerial = null;
        String apTag = null;
        String band = null;
        List<GetNetworkWirelessChannelUtilizationHistory200ResponseInner> response = api.getNetworkWirelessChannelUtilizationHistory_1(networkId, t0, t1, timespan, resolution, autoResolution, clientId, deviceSerial, apTag, band);
        // TODO: test validations
    }

}
