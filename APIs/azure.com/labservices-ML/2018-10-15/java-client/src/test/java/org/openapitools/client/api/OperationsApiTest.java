/*
 * ManagedLabsClient
 * The Managed Labs Client.
 *
 * The version of the OpenAPI document: 2018-10-15
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.CloudError;
import org.openapitools.client.model.OperationResult;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for OperationsApi
 */
@Disabled
public class OperationsApiTest {

    private final OperationsApi api = new OperationsApi();

    /**
     * Get operation
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void operationsGetTest() throws ApiException {
        String subscriptionId = null;
        String locationName = null;
        String operationName = null;
        String apiVersion = null;
        OperationResult response = api.operationsGet(subscriptionId, locationName, operationName, apiVersion);
        // TODO: test validations
    }

}
