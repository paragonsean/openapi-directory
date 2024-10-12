/*
 * FrontDoorManagementClient
 * Use these APIs to manage Azure Front Door resources through the Azure Resource Manager. You must make sure that requests made to these resources are secure.
 *
 * The version of the OpenAPI document: 2019-04-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.CustomHttpsConfiguration;
import org.openapitools.client.model.ErrorResponse;
import org.openapitools.client.model.FrontDoor;
import org.openapitools.client.model.FrontDoorListResult;
import org.openapitools.client.model.FrontendEndpoint;
import org.openapitools.client.model.FrontendEndpointsListResult;
import org.openapitools.client.model.PurgeParameters;
import org.openapitools.client.model.ValidateCustomDomainInput;
import org.openapitools.client.model.ValidateCustomDomainOutput;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for FrontDoorsApi
 */
@Disabled
public class FrontDoorsApiTest {

    private final FrontDoorsApi api = new FrontDoorsApi();

    /**
     * Removes a content from Front Door.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void endpointsPurgeContentTest() throws ApiException {
        String subscriptionId = null;
        String resourceGroupName = null;
        String frontDoorName = null;
        String apiVersion = null;
        PurgeParameters contentFilePaths = null;
        api.endpointsPurgeContent(subscriptionId, resourceGroupName, frontDoorName, apiVersion, contentFilePaths);
        // TODO: test validations
    }

    /**
     * Creates a new Front Door with a Front Door name under the specified subscription and resource group.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void frontDoorsCreateOrUpdateTest() throws ApiException {
        String subscriptionId = null;
        String resourceGroupName = null;
        String frontDoorName = null;
        String apiVersion = null;
        FrontDoor frontDoorParameters = null;
        FrontDoor response = api.frontDoorsCreateOrUpdate(subscriptionId, resourceGroupName, frontDoorName, apiVersion, frontDoorParameters);
        // TODO: test validations
    }

    /**
     * Deletes an existing Front Door with the specified parameters.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void frontDoorsDeleteTest() throws ApiException {
        String subscriptionId = null;
        String resourceGroupName = null;
        String frontDoorName = null;
        String apiVersion = null;
        api.frontDoorsDelete(subscriptionId, resourceGroupName, frontDoorName, apiVersion);
        // TODO: test validations
    }

    /**
     * Gets a Front Door with the specified Front Door name under the specified subscription and resource group.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void frontDoorsGetTest() throws ApiException {
        String subscriptionId = null;
        String resourceGroupName = null;
        String frontDoorName = null;
        String apiVersion = null;
        FrontDoor response = api.frontDoorsGet(subscriptionId, resourceGroupName, frontDoorName, apiVersion);
        // TODO: test validations
    }

    /**
     * Lists all of the Front Doors within an Azure subscription.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void frontDoorsListTest() throws ApiException {
        String subscriptionId = null;
        String apiVersion = null;
        FrontDoorListResult response = api.frontDoorsList(subscriptionId, apiVersion);
        // TODO: test validations
    }

    /**
     * Lists all of the Front Doors within a resource group under a subscription.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void frontDoorsListByResourceGroupTest() throws ApiException {
        String subscriptionId = null;
        String resourceGroupName = null;
        String apiVersion = null;
        FrontDoorListResult response = api.frontDoorsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion);
        // TODO: test validations
    }

    /**
     * Validates the custom domain mapping to ensure it maps to the correct Front Door endpoint in DNS.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void frontDoorsValidateCustomDomainTest() throws ApiException {
        String subscriptionId = null;
        String resourceGroupName = null;
        String frontDoorName = null;
        String apiVersion = null;
        ValidateCustomDomainInput customDomainProperties = null;
        ValidateCustomDomainOutput response = api.frontDoorsValidateCustomDomain(subscriptionId, resourceGroupName, frontDoorName, apiVersion, customDomainProperties);
        // TODO: test validations
    }

    /**
     * Disables a frontendEndpoint for HTTPS traffic
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void frontendEndpointsDisableHttpsTest() throws ApiException {
        String subscriptionId = null;
        String resourceGroupName = null;
        String frontDoorName = null;
        String frontendEndpointName = null;
        String apiVersion = null;
        api.frontendEndpointsDisableHttps(subscriptionId, resourceGroupName, frontDoorName, frontendEndpointName, apiVersion);
        // TODO: test validations
    }

    /**
     * Enables a frontendEndpoint for HTTPS traffic
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void frontendEndpointsEnableHttpsTest() throws ApiException {
        String subscriptionId = null;
        String resourceGroupName = null;
        String frontDoorName = null;
        String frontendEndpointName = null;
        String apiVersion = null;
        CustomHttpsConfiguration customHttpsConfiguration = null;
        api.frontendEndpointsEnableHttps(subscriptionId, resourceGroupName, frontDoorName, frontendEndpointName, apiVersion, customHttpsConfiguration);
        // TODO: test validations
    }

    /**
     * Gets a Frontend endpoint with the specified name within the specified Front Door.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void frontendEndpointsGetTest() throws ApiException {
        String subscriptionId = null;
        String resourceGroupName = null;
        String frontDoorName = null;
        String frontendEndpointName = null;
        String apiVersion = null;
        FrontendEndpoint response = api.frontendEndpointsGet(subscriptionId, resourceGroupName, frontDoorName, frontendEndpointName, apiVersion);
        // TODO: test validations
    }

    /**
     * Lists all of the frontend endpoints within a Front Door.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void frontendEndpointsListByFrontDoorTest() throws ApiException {
        String subscriptionId = null;
        String resourceGroupName = null;
        String frontDoorName = null;
        String apiVersion = null;
        FrontendEndpointsListResult response = api.frontendEndpointsListByFrontDoor(subscriptionId, resourceGroupName, frontDoorName, apiVersion);
        // TODO: test validations
    }

}
