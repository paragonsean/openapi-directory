/*
 * SqlManagementClient
 * The Azure SQL Database management API provides a RESTful set of web APIs that interact with Azure SQL Database services to manage your databases. The API enables users to create, retrieve, update, and delete databases, servers, and other entities.
 *
 * The version of the OpenAPI document: 2015-05-01-preview
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.SubscriptionUsage;
import org.openapitools.client.model.SubscriptionUsageListResult;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for SubscriptionUsagesApi
 */
@Disabled
public class SubscriptionUsagesApiTest {

    private final SubscriptionUsagesApi api = new SubscriptionUsagesApi();

    /**
     * Gets a subscription usage metric.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void subscriptionUsagesGetTest() throws ApiException {
        String locationName = null;
        String usageName = null;
        String subscriptionId = null;
        String apiVersion = null;
        SubscriptionUsage response = api.subscriptionUsagesGet(locationName, usageName, subscriptionId, apiVersion);
        // TODO: test validations
    }

    /**
     * Gets all subscription usage metrics in a given location.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void subscriptionUsagesListByLocationTest() throws ApiException {
        String locationName = null;
        String subscriptionId = null;
        String apiVersion = null;
        SubscriptionUsageListResult response = api.subscriptionUsagesListByLocation(locationName, subscriptionId, apiVersion);
        // TODO: test validations
    }

}
