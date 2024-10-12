/*
 * ResourceHealthMetadata API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-08-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.ResourceHealthMetadata;
import org.openapitools.client.model.ResourceHealthMetadataCollection;
import org.openapitools.client.model.ResourceHealthMetadataListDefaultResponse;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for ResourceHealthMetadataApi
 */
@Disabled
public class ResourceHealthMetadataApiTest {

    private final ResourceHealthMetadataApi api = new ResourceHealthMetadataApi();

    /**
     * Gets the category of ResourceHealthMetadata to use for the given site
     *
     * Description for Gets the category of ResourceHealthMetadata to use for the given site
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void resourceHealthMetadataGetBySiteTest() throws ApiException {
        String resourceGroupName = null;
        String name = null;
        String subscriptionId = null;
        String apiVersion = null;
        ResourceHealthMetadata response = api.resourceHealthMetadataGetBySite(resourceGroupName, name, subscriptionId, apiVersion);
        // TODO: test validations
    }

    /**
     * Gets the category of ResourceHealthMetadata to use for the given site
     *
     * Description for Gets the category of ResourceHealthMetadata to use for the given site
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void resourceHealthMetadataGetBySiteSlotTest() throws ApiException {
        String resourceGroupName = null;
        String name = null;
        String slot = null;
        String subscriptionId = null;
        String apiVersion = null;
        ResourceHealthMetadata response = api.resourceHealthMetadataGetBySiteSlot(resourceGroupName, name, slot, subscriptionId, apiVersion);
        // TODO: test validations
    }

    /**
     * List all ResourceHealthMetadata for all sites in the subscription.
     *
     * Description for List all ResourceHealthMetadata for all sites in the subscription.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void resourceHealthMetadataListTest() throws ApiException {
        String subscriptionId = null;
        String apiVersion = null;
        ResourceHealthMetadataCollection response = api.resourceHealthMetadataList(subscriptionId, apiVersion);
        // TODO: test validations
    }

    /**
     * List all ResourceHealthMetadata for all sites in the resource group in the subscription.
     *
     * Description for List all ResourceHealthMetadata for all sites in the resource group in the subscription.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void resourceHealthMetadataListByResourceGroupTest() throws ApiException {
        String resourceGroupName = null;
        String subscriptionId = null;
        String apiVersion = null;
        ResourceHealthMetadataCollection response = api.resourceHealthMetadataListByResourceGroup(resourceGroupName, subscriptionId, apiVersion);
        // TODO: test validations
    }

    /**
     * Gets the category of ResourceHealthMetadata to use for the given site as a collection
     *
     * Description for Gets the category of ResourceHealthMetadata to use for the given site as a collection
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void resourceHealthMetadataListBySiteTest() throws ApiException {
        String resourceGroupName = null;
        String name = null;
        String subscriptionId = null;
        String apiVersion = null;
        ResourceHealthMetadataCollection response = api.resourceHealthMetadataListBySite(resourceGroupName, name, subscriptionId, apiVersion);
        // TODO: test validations
    }

    /**
     * Gets the category of ResourceHealthMetadata to use for the given site as a collection
     *
     * Description for Gets the category of ResourceHealthMetadata to use for the given site as a collection
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void resourceHealthMetadataListBySiteSlotTest() throws ApiException {
        String resourceGroupName = null;
        String name = null;
        String slot = null;
        String subscriptionId = null;
        String apiVersion = null;
        ResourceHealthMetadataCollection response = api.resourceHealthMetadataListBySiteSlot(resourceGroupName, name, slot, subscriptionId, apiVersion);
        // TODO: test validations
    }

}
