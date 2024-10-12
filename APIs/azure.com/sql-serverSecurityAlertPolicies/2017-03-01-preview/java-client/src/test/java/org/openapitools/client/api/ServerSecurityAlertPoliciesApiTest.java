/*
 * SqlManagementClient
 * The Azure SQL Database management API provides a RESTful set of web APIs that interact with Azure SQL Database services to manage your databases. The API enables users to create, retrieve, update, and delete databases, servers, and other entities.
 *
 * The version of the OpenAPI document: 2017-03-01-preview
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.LogicalServerSecurityAlertPolicyListResult;
import org.openapitools.client.model.ServerSecurityAlertPolicy;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for ServerSecurityAlertPoliciesApi
 */
@Disabled
public class ServerSecurityAlertPoliciesApiTest {

    private final ServerSecurityAlertPoliciesApi api = new ServerSecurityAlertPoliciesApi();

    /**
     * Creates or updates a threat detection policy.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void serverSecurityAlertPoliciesCreateOrUpdateTest() throws ApiException {
        String resourceGroupName = null;
        String serverName = null;
        String securityAlertPolicyName = null;
        String subscriptionId = null;
        String apiVersion = null;
        ServerSecurityAlertPolicy parameters = null;
        ServerSecurityAlertPolicy response = api.serverSecurityAlertPoliciesCreateOrUpdate(resourceGroupName, serverName, securityAlertPolicyName, subscriptionId, apiVersion, parameters);
        // TODO: test validations
    }

    /**
     * Get a server&#39;s security alert policy.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void serverSecurityAlertPoliciesGetTest() throws ApiException {
        String resourceGroupName = null;
        String serverName = null;
        String securityAlertPolicyName = null;
        String subscriptionId = null;
        String apiVersion = null;
        ServerSecurityAlertPolicy response = api.serverSecurityAlertPoliciesGet(resourceGroupName, serverName, securityAlertPolicyName, subscriptionId, apiVersion);
        // TODO: test validations
    }

    /**
     * Get the server&#39;s threat detection policies.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void serverSecurityAlertPoliciesListByServerTest() throws ApiException {
        String resourceGroupName = null;
        String serverName = null;
        String subscriptionId = null;
        String apiVersion = null;
        LogicalServerSecurityAlertPolicyListResult response = api.serverSecurityAlertPoliciesListByServer(resourceGroupName, serverName, subscriptionId, apiVersion);
        // TODO: test validations
    }

}
