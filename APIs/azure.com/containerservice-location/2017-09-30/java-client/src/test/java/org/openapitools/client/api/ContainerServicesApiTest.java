/*
 * ContainerServiceClient
 * The Container Service Client.
 *
 * The version of the OpenAPI document: 2017-09-30
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.OrchestratorVersionProfileListResult;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for ContainerServicesApi
 */
@Disabled
public class ContainerServicesApiTest {

    private final ContainerServicesApi api = new ContainerServicesApi();

    /**
     * Gets a list of supported orchestrators in the specified subscription.
     *
     * Gets a list of supported orchestrators in the specified subscription. The operation returns properties of each orchestrator including version and available upgrades.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void containerServicesListOrchestratorsTest() throws ApiException {
        String apiVersion = null;
        String subscriptionId = null;
        String location = null;
        String resourceType = null;
        OrchestratorVersionProfileListResult response = api.containerServicesListOrchestrators(apiVersion, subscriptionId, location, resourceType);
        // TODO: test validations
    }

}
