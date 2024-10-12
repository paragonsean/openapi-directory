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
import org.openapitools.client.model.Job;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for OperationsStatusApi
 */
@Disabled
public class OperationsStatusApiTest {

    private final OperationsStatusApi api = new OperationsStatusApi();

    /**
     * Gets the details of a specified job on a data box edge/gateway device.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void operationsStatusGetTest() throws ApiException {
        String deviceName = null;
        String name = null;
        String subscriptionId = null;
        String resourceGroupName = null;
        String apiVersion = null;
        Job response = api.operationsStatusGet(deviceName, name, subscriptionId, resourceGroupName, apiVersion);
        // TODO: test validations
    }

}
