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
import org.openapitools.client.model.UpdateNetworkApplianceContentFilteringRequest;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for ContentFilteringApi
 */
@Disabled
public class ContentFilteringApiTest {

    private final ContentFilteringApi api = new ContentFilteringApi();

    /**
     * List all available content filtering categories for an MX network
     *
     * List all available content filtering categories for an MX network
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getNetworkApplianceContentFilteringCategories_1Test() throws ApiException {
        String networkId = null;
        Object response = api.getNetworkApplianceContentFilteringCategories_1(networkId);
        // TODO: test validations
    }

    /**
     * Return the content filtering settings for an MX network
     *
     * Return the content filtering settings for an MX network
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getNetworkApplianceContentFiltering_1Test() throws ApiException {
        String networkId = null;
        Object response = api.getNetworkApplianceContentFiltering_1(networkId);
        // TODO: test validations
    }

    /**
     * Update the content filtering settings for an MX network
     *
     * Update the content filtering settings for an MX network
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateNetworkApplianceContentFiltering_1Test() throws ApiException {
        String networkId = null;
        UpdateNetworkApplianceContentFilteringRequest updateNetworkApplianceContentFilteringRequest = null;
        Object response = api.updateNetworkApplianceContentFiltering_1(networkId, updateNetworkApplianceContentFilteringRequest);
        // TODO: test validations
    }

}
