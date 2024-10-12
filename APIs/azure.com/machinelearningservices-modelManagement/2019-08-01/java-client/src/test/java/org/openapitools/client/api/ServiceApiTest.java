/*
 * Azure Machine Learning Model Management Service
 * These APIs allow end users to manage Azure Machine Learning Models, Images, Profiles, and Services.
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
import org.openapitools.client.model.AuthKeys;
import org.openapitools.client.model.AuthToken;
import org.openapitools.client.model.CreateServiceRequest;
import org.openapitools.client.model.JsonPatchOperation;
import org.openapitools.client.model.ModelErrorResponse;
import org.openapitools.client.model.PaginatedServiceList;
import org.openapitools.client.model.RegenerateServiceKeysRequest;
import org.openapitools.client.model.ServiceResponseBase;
import java.util.UUID;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for ServiceApi
 */
@Disabled
public class ServiceApiTest {

    private final ServiceApi api = new ServiceApi();

    /**
     * Create a Service.
     *
     * Create a Service with the specified payload.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void servicesCreateTest() throws ApiException {
        UUID subscriptionId = null;
        String resourceGroup = null;
        String workspace = null;
        CreateServiceRequest request = null;
        api.servicesCreate(subscriptionId, resourceGroup, workspace, request);
        // TODO: test validations
    }

    /**
     * Delete a Service.
     *
     * Delete a specific Service.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void servicesDeleteTest() throws ApiException {
        UUID subscriptionId = null;
        String resourceGroup = null;
        String workspace = null;
        String id = null;
        api.servicesDelete(subscriptionId, resourceGroup, workspace, id);
        // TODO: test validations
    }

    /**
     * Generate Service Access Token.
     *
     * Gets access token that can be used for calling service.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void servicesGetServiceTokenTest() throws ApiException {
        UUID subscriptionId = null;
        String resourceGroup = null;
        String workspace = null;
        String id = null;
        AuthToken response = api.servicesGetServiceToken(subscriptionId, resourceGroup, workspace, id);
        // TODO: test validations
    }

    /**
     * Query the list of Services in a Workspace.
     *
     * If no filter is passed, the query lists all Services in the Workspace. The returned list is paginated and the count of item in each page is an optional parameter.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void servicesListQueryTest() throws ApiException {
        UUID subscriptionId = null;
        String resourceGroup = null;
        String workspace = null;
        String imageId = null;
        String imageName = null;
        String modelId = null;
        String modelName = null;
        String name = null;
        Integer count = null;
        String computeType = null;
        String $skipToken = null;
        String tags = null;
        String properties = null;
        Boolean expand = null;
        String orderby = null;
        PaginatedServiceList response = api.servicesListQuery(subscriptionId, resourceGroup, workspace, imageId, imageName, modelId, modelName, name, count, computeType, $skipToken, tags, properties, expand, orderby);
        // TODO: test validations
    }

    /**
     * Lists Service keys.
     *
     * Gets a list of Service keys.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void servicesListServiceKeysTest() throws ApiException {
        UUID subscriptionId = null;
        String resourceGroup = null;
        String workspace = null;
        String id = null;
        AuthKeys response = api.servicesListServiceKeys(subscriptionId, resourceGroup, workspace, id);
        // TODO: test validations
    }

    /**
     * Patch a Service.
     *
     * Patch a specific Service.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void servicesPatchTest() throws ApiException {
        UUID subscriptionId = null;
        String resourceGroup = null;
        String workspace = null;
        String id = null;
        List<JsonPatchOperation> patch = null;
        api.servicesPatch(subscriptionId, resourceGroup, workspace, id, patch);
        // TODO: test validations
    }

    /**
     * Get a Service.
     *
     * Get a Service by Id.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void servicesQueryByIdTest() throws ApiException {
        UUID subscriptionId = null;
        String resourceGroup = null;
        String workspace = null;
        String id = null;
        Boolean expand = null;
        ServiceResponseBase response = api.servicesQueryById(subscriptionId, resourceGroup, workspace, id, expand);
        // TODO: test validations
    }

    /**
     * Regenerate Service Keys.
     *
     * Regenerate and return the Service keys.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void servicesRegenerateServiceKeysTest() throws ApiException {
        UUID subscriptionId = null;
        String resourceGroup = null;
        String workspace = null;
        String id = null;
        RegenerateServiceKeysRequest request = null;
        AuthKeys response = api.servicesRegenerateServiceKeys(subscriptionId, resourceGroup, workspace, id, request);
        // TODO: test validations
    }

}
