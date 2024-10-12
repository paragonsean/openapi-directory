/*
 * IoTSpacesClient
 * Use this API to manage the IoTSpaces service instances in your Azure subscription.
 *
 * The version of the OpenAPI document: 2017-10-01-preview
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.ErrorDetails;
import org.openapitools.client.model.IoTSpacesDescription;
import org.openapitools.client.model.IoTSpacesPatchDescription;
import java.util.UUID;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for ResourceApi
 */
@Disabled
public class ResourceApiTest {

    private final ResourceApi api = new ResourceApi();

    /**
     * Create or update the metadata of an IoTSpaces instance. The usual pattern to modify a property is to retrieve the IoTSpaces instance metadata and security metadata, and then combine them with the modified values in a new body to update the IoTSpaces instance.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void ioTSpacesCreateOrUpdateTest() throws ApiException {
        String apiVersion = null;
        UUID subscriptionId = null;
        String resourceGroupName = null;
        String resourceName = null;
        IoTSpacesDescription iotSpaceDescription = null;
        IoTSpacesDescription response = api.ioTSpacesCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, resourceName, iotSpaceDescription);
        // TODO: test validations
    }

    /**
     * Delete an IoTSpaces instance.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void ioTSpacesDeleteTest() throws ApiException {
        String apiVersion = null;
        UUID subscriptionId = null;
        String resourceGroupName = null;
        String resourceName = null;
        IoTSpacesDescription response = api.ioTSpacesDelete(apiVersion, subscriptionId, resourceGroupName, resourceName);
        // TODO: test validations
    }

    /**
     * Get the metadata of a IoTSpaces instance.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void ioTSpacesGetTest() throws ApiException {
        String apiVersion = null;
        UUID subscriptionId = null;
        String resourceGroupName = null;
        String resourceName = null;
        IoTSpacesDescription response = api.ioTSpacesGet(apiVersion, subscriptionId, resourceGroupName, resourceName);
        // TODO: test validations
    }

    /**
     * Update the metadata of a IoTSpaces instance.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void ioTSpacesUpdateTest() throws ApiException {
        String apiVersion = null;
        UUID subscriptionId = null;
        String resourceGroupName = null;
        String resourceName = null;
        IoTSpacesPatchDescription iotSpacePatchDescription = null;
        IoTSpacesDescription response = api.ioTSpacesUpdate(apiVersion, subscriptionId, resourceGroupName, resourceName, iotSpacePatchDescription);
        // TODO: test validations
    }

}
