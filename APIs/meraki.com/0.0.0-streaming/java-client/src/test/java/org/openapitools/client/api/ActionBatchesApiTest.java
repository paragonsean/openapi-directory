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
import org.openapitools.client.model.CreateOrganizationActionBatchRequest;
import org.openapitools.client.model.UpdateOrganizationActionBatchRequest;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for ActionBatchesApi
 */
@Disabled
public class ActionBatchesApiTest {

    private final ActionBatchesApi api = new ActionBatchesApi();

    /**
     * Create an action batch
     *
     * Create an action batch
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createOrganizationActionBatchTest() throws ApiException {
        String organizationId = null;
        CreateOrganizationActionBatchRequest createOrganizationActionBatchRequest = null;
        Object response = api.createOrganizationActionBatch(organizationId, createOrganizationActionBatchRequest);
        // TODO: test validations
    }

    /**
     * Delete an action batch
     *
     * Delete an action batch
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteOrganizationActionBatchTest() throws ApiException {
        String organizationId = null;
        String actionBatchId = null;
        api.deleteOrganizationActionBatch(organizationId, actionBatchId);
        // TODO: test validations
    }

    /**
     * Return the list of action batches in the organization
     *
     * Return the list of action batches in the organization
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getOrganizationActionBatchesTest() throws ApiException {
        String organizationId = null;
        String status = null;
        List<Object> response = api.getOrganizationActionBatches(organizationId, status);
        // TODO: test validations
    }

    /**
     * Update an action batch
     *
     * Update an action batch
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateOrganizationActionBatchTest() throws ApiException {
        String organizationId = null;
        String actionBatchId = null;
        UpdateOrganizationActionBatchRequest updateOrganizationActionBatchRequest = null;
        Object response = api.updateOrganizationActionBatch(organizationId, actionBatchId, updateOrganizationActionBatchRequest);
        // TODO: test validations
    }

}
