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
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for MerakiAuthUsersApi
 */
@Disabled
public class MerakiAuthUsersApiTest {

    private final MerakiAuthUsersApi api = new MerakiAuthUsersApi();

    /**
     * Return the Meraki Auth splash or RADIUS user
     *
     * Return the Meraki Auth splash or RADIUS user
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getNetworkMerakiAuthUserTest() throws ApiException {
        String networkId = null;
        String merakiAuthUserId = null;
        Object response = api.getNetworkMerakiAuthUser(networkId, merakiAuthUserId);
        // TODO: test validations
    }

    /**
     * List the splash or RADIUS users configured under Meraki Authentication for a network
     *
     * List the splash or RADIUS users configured under Meraki Authentication for a network
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getNetworkMerakiAuthUsersTest() throws ApiException {
        String networkId = null;
        List<Object> response = api.getNetworkMerakiAuthUsers(networkId);
        // TODO: test validations
    }

}
