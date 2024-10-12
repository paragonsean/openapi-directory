/*
 * Storage Cache Mgmt Client
 * A Storage Cache provides scalable caching service for NAS clients, serving data from either NFSv3 or Blob at-rest storage (referred to as \"Storage Targets\"). These operations allow you to manage caches.
 *
 * The version of the OpenAPI document: 2019-08-01-preview
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.ApiOperationListResult;
import org.openapitools.client.model.CloudError;
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
     * Lists all of the available RP operations.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void operationsListTest() throws ApiException {
        String apiVersion = null;
        ApiOperationListResult response = api.operationsList(apiVersion);
        // TODO: test validations
    }

}
