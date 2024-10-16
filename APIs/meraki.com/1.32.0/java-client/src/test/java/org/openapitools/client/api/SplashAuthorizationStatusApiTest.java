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
import org.openapitools.client.model.UpdateNetworkClientSplashAuthorizationStatusRequest;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for SplashAuthorizationStatusApi
 */
@Disabled
public class SplashAuthorizationStatusApiTest {

    private final SplashAuthorizationStatusApi api = new SplashAuthorizationStatusApi();

    /**
     * Return the splash authorization for a client, for each SSID they&#39;ve associated with through splash
     *
     * Return the splash authorization for a client, for each SSID they&#39;ve associated with through splash. Only enabled SSIDs with Click-through splash enabled will be included. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getNetworkClientSplashAuthorizationStatus_2Test() throws ApiException {
        String networkId = null;
        String clientId = null;
        Object response = api.getNetworkClientSplashAuthorizationStatus_2(networkId, clientId);
        // TODO: test validations
    }

    /**
     * Update a client&#39;s splash authorization
     *
     * Update a client&#39;s splash authorization. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateNetworkClientSplashAuthorizationStatus_2Test() throws ApiException {
        String networkId = null;
        String clientId = null;
        UpdateNetworkClientSplashAuthorizationStatusRequest updateNetworkClientSplashAuthorizationStatusRequest = null;
        Object response = api.updateNetworkClientSplashAuthorizationStatus_2(networkId, clientId, updateNetworkClientSplashAuthorizationStatusRequest);
        // TODO: test validations
    }

}
