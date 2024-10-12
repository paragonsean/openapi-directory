/*
 * MySQLManagementClient
 * The Microsoft Azure management API provides create, read, update, and delete functionality for Azure MySQL resources including servers, databases, firewall rules, VNET rules, security alert policies, log files and configurations with new business model.
 *
 * The version of the OpenAPI document: 2018-06-01-privatepreview
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.CloudError;
import org.openapitools.client.model.PrivateEndpointConnection;
import org.openapitools.client.model.PrivateEndpointConnectionListResult;
import org.openapitools.client.model.TagsObject;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for PrivateEndpointConnectionsApi
 */
@Disabled
public class PrivateEndpointConnectionsApiTest {

    private final PrivateEndpointConnectionsApi api = new PrivateEndpointConnectionsApi();

    /**
     * Approve or reject a private endpoint connection with a given name.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void privateEndpointConnectionsCreateOrUpdateTest() throws ApiException {
        String resourceGroupName = null;
        String serverName = null;
        String privateEndpointConnectionName = null;
        String subscriptionId = null;
        String apiVersion = null;
        PrivateEndpointConnection parameters = null;
        PrivateEndpointConnection response = api.privateEndpointConnectionsCreateOrUpdate(resourceGroupName, serverName, privateEndpointConnectionName, subscriptionId, apiVersion, parameters);
        // TODO: test validations
    }

    /**
     * Deletes a private endpoint connection with a given name.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void privateEndpointConnectionsDeleteTest() throws ApiException {
        String resourceGroupName = null;
        String serverName = null;
        String privateEndpointConnectionName = null;
        String subscriptionId = null;
        String apiVersion = null;
        api.privateEndpointConnectionsDelete(resourceGroupName, serverName, privateEndpointConnectionName, subscriptionId, apiVersion);
        // TODO: test validations
    }

    /**
     * Gets a private endpoint connection.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void privateEndpointConnectionsGetTest() throws ApiException {
        String resourceGroupName = null;
        String serverName = null;
        String privateEndpointConnectionName = null;
        String subscriptionId = null;
        String apiVersion = null;
        PrivateEndpointConnection response = api.privateEndpointConnectionsGet(resourceGroupName, serverName, privateEndpointConnectionName, subscriptionId, apiVersion);
        // TODO: test validations
    }

    /**
     * Gets all private endpoint connections on a server.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void privateEndpointConnectionsListByServerTest() throws ApiException {
        String resourceGroupName = null;
        String serverName = null;
        String subscriptionId = null;
        String apiVersion = null;
        PrivateEndpointConnectionListResult response = api.privateEndpointConnectionsListByServer(resourceGroupName, serverName, subscriptionId, apiVersion);
        // TODO: test validations
    }

    /**
     * Updates tags on private endpoint connection.
     *
     * Updates private endpoint connection with the specified tags.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void privateEndpointConnectionsUpdateTagsTest() throws ApiException {
        String apiVersion = null;
        String subscriptionId = null;
        String resourceGroupName = null;
        String serverName = null;
        String privateEndpointConnectionName = null;
        TagsObject parameters = null;
        PrivateEndpointConnection response = api.privateEndpointConnectionsUpdateTags(apiVersion, subscriptionId, resourceGroupName, serverName, privateEndpointConnectionName, parameters);
        // TODO: test validations
    }

}
