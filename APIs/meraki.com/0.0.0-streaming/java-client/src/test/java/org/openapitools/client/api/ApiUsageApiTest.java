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
 * API tests for ApiUsageApi
 */
@Disabled
public class ApiUsageApiTest {

    private final ApiUsageApi api = new ApiUsageApi();

    /**
     * List the API requests made by an organization
     *
     * List the API requests made by an organization
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getOrganizationApiRequestsTest() throws ApiException {
        String organizationId = null;
        String t0 = null;
        String t1 = null;
        Float timespan = null;
        Integer perPage = null;
        String startingAfter = null;
        String endingBefore = null;
        String adminId = null;
        String path = null;
        String method = null;
        Integer responseCode = null;
        String sourceIp = null;
        List<Object> response = api.getOrganizationApiRequests(organizationId, t0, t1, timespan, perPage, startingAfter, endingBefore, adminId, path, method, responseCode, sourceIp);
        // TODO: test validations
    }

    /**
     * Return an aggregated overview of API requests data
     *
     * Return an aggregated overview of API requests data
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getOrganizationApiRequestsOverviewTest() throws ApiException {
        String organizationId = null;
        String t0 = null;
        String t1 = null;
        Float timespan = null;
        Object response = api.getOrganizationApiRequestsOverview(organizationId, t0, t1, timespan);
        // TODO: test validations
    }

}
