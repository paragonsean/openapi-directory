/*
 * HDInsightManagementClient
 * The HDInsight Management Client.
 *
 * The version of the OpenAPI document: 2015-03-01-preview
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.Application;
import org.openapitools.client.model.ApplicationListResult;
import org.openapitools.client.model.ApplicationsListDefaultResponse;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for ApplicationsApi
 */
@Disabled
public class ApplicationsApiTest {

    private final ApplicationsApi api = new ApplicationsApi();

    /**
     * Creates applications for the HDInsight cluster.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void applicationsCreateTest() throws ApiException {
        String subscriptionId = null;
        String resourceGroupName = null;
        String clusterName = null;
        String applicationName = null;
        String apiVersion = null;
        Application parameters = null;
        Application response = api.applicationsCreate(subscriptionId, resourceGroupName, clusterName, applicationName, apiVersion, parameters);
        // TODO: test validations
    }

    /**
     * Deletes the specified application on the HDInsight cluster.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void applicationsDeleteTest() throws ApiException {
        String subscriptionId = null;
        String resourceGroupName = null;
        String clusterName = null;
        String applicationName = null;
        String apiVersion = null;
        api.applicationsDelete(subscriptionId, resourceGroupName, clusterName, applicationName, apiVersion);
        // TODO: test validations
    }

    /**
     * Lists properties of the specified application.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void applicationsGetTest() throws ApiException {
        String subscriptionId = null;
        String resourceGroupName = null;
        String clusterName = null;
        String applicationName = null;
        String apiVersion = null;
        Application response = api.applicationsGet(subscriptionId, resourceGroupName, clusterName, applicationName, apiVersion);
        // TODO: test validations
    }

    /**
     * Lists all of the applications for the HDInsight cluster.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void applicationsListTest() throws ApiException {
        String subscriptionId = null;
        String resourceGroupName = null;
        String clusterName = null;
        String apiVersion = null;
        ApplicationListResult response = api.applicationsList(subscriptionId, resourceGroupName, clusterName, apiVersion);
        // TODO: test validations
    }

}
