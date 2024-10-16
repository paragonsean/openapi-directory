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
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for LossAndLatencyHistoryApi
 */
@Disabled
public class LossAndLatencyHistoryApiTest {

    private final LossAndLatencyHistoryApi api = new LossAndLatencyHistoryApi();

    /**
     * Get the uplink loss percentage and latency in milliseconds, and goodput in kilobits per second for a wired network device.
     *
     * Get the uplink loss percentage and latency in milliseconds, and goodput in kilobits per second for a wired network device.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getDeviceLossAndLatencyHistory_2Test() throws ApiException {
        String serial = null;
        String ip = null;
        String t0 = null;
        String t1 = null;
        Float timespan = null;
        Integer resolution = null;
        String uplink = null;
        List<Object> response = api.getDeviceLossAndLatencyHistory_2(serial, ip, t0, t1, timespan, resolution, uplink);
        // TODO: test validations
    }

}
