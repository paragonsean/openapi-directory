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
import org.openapitools.client.model.UpdateNetworkAlertSettingsRequest;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for AlertSettingsApi
 */
@Disabled
public class AlertSettingsApiTest {

    private final AlertSettingsApi api = new AlertSettingsApi();

    /**
     * Return the alert configuration for this network
     *
     * Return the alert configuration for this network
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getNetworkAlertSettingsTest() throws ApiException {
        String networkId = null;
        Object response = api.getNetworkAlertSettings(networkId);
        // TODO: test validations
    }

    /**
     * Update the alert configuration for this network
     *
     * Update the alert configuration for this network
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateNetworkAlertSettingsTest() throws ApiException {
        String networkId = null;
        UpdateNetworkAlertSettingsRequest updateNetworkAlertSettingsRequest = null;
        Object response = api.updateNetworkAlertSettings(networkId, updateNetworkAlertSettingsRequest);
        // TODO: test validations
    }

}
