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
import org.openapitools.client.model.GetNetworkSmDevicePerformanceHistory200ResponseInner;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for PerformanceHistoryApi
 */
@Disabled
public class PerformanceHistoryApiTest {

    private final PerformanceHistoryApi api = new PerformanceHistoryApi();

    /**
     * Return historical records of various Systems Manager client metrics for desktop devices.
     *
     * Return historical records of various Systems Manager client metrics for desktop devices.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getNetworkSmDevicePerformanceHistory_2Test() throws ApiException {
        String networkId = null;
        String deviceId = null;
        Integer perPage = null;
        String startingAfter = null;
        String endingBefore = null;
        List<GetNetworkSmDevicePerformanceHistory200ResponseInner> response = api.getNetworkSmDevicePerformanceHistory_2(networkId, deviceId, perPage, startingAfter, endingBefore);
        // TODO: test validations
    }

}
