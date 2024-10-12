/*
 * DataBoxEdgeManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-03-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.CloudError;
import org.openapitools.client.model.OperationsList;
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
     * List all the supported operations.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void operationsListTest() throws ApiException {
        String apiVersion = null;
        OperationsList response = api.operationsList(apiVersion);
        // TODO: test validations
    }

}
