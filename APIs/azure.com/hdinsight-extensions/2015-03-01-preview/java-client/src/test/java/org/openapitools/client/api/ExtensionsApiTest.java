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
import org.openapitools.client.model.ClusterMonitoringRequest;
import org.openapitools.client.model.ClusterMonitoringResponse;
import org.openapitools.client.model.Extension;
import org.openapitools.client.model.ExtensionGetMonitoringStatusDefaultResponse;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for ExtensionsApi
 */
@Disabled
public class ExtensionsApiTest {

    private final ExtensionsApi api = new ExtensionsApi();

    /**
     * Creates an HDInsight cluster extension.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void extensionCreateTest() throws ApiException {
        String subscriptionId = null;
        String resourceGroupName = null;
        String clusterName = null;
        String extensionName = null;
        String apiVersion = null;
        Extension parameters = null;
        api.extensionCreate(subscriptionId, resourceGroupName, clusterName, extensionName, apiVersion, parameters);
        // TODO: test validations
    }

    /**
     * Deletes the specified extension for HDInsight cluster.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void extensionDeleteTest() throws ApiException {
        String subscriptionId = null;
        String resourceGroupName = null;
        String clusterName = null;
        String extensionName = null;
        String apiVersion = null;
        api.extensionDelete(subscriptionId, resourceGroupName, clusterName, extensionName, apiVersion);
        // TODO: test validations
    }

    /**
     * Disables the Operations Management Suite (OMS) on the HDInsight cluster.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void extensionDisableMonitoringTest() throws ApiException {
        String subscriptionId = null;
        String resourceGroupName = null;
        String clusterName = null;
        String apiVersion = null;
        api.extensionDisableMonitoring(subscriptionId, resourceGroupName, clusterName, apiVersion);
        // TODO: test validations
    }

    /**
     * Enables the Operations Management Suite (OMS) on the HDInsight cluster.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void extensionEnableMonitoringTest() throws ApiException {
        String subscriptionId = null;
        String resourceGroupName = null;
        String clusterName = null;
        String apiVersion = null;
        ClusterMonitoringRequest parameters = null;
        api.extensionEnableMonitoring(subscriptionId, resourceGroupName, clusterName, apiVersion, parameters);
        // TODO: test validations
    }

    /**
     * Gets the extension properties for the specified HDInsight cluster extension.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void extensionGetTest() throws ApiException {
        String subscriptionId = null;
        String resourceGroupName = null;
        String clusterName = null;
        String extensionName = null;
        String apiVersion = null;
        Extension response = api.extensionGet(subscriptionId, resourceGroupName, clusterName, extensionName, apiVersion);
        // TODO: test validations
    }

    /**
     * Gets the status of Operations Management Suite (OMS) on the HDInsight cluster.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void extensionGetMonitoringStatusTest() throws ApiException {
        String subscriptionId = null;
        String resourceGroupName = null;
        String clusterName = null;
        String apiVersion = null;
        ClusterMonitoringResponse response = api.extensionGetMonitoringStatus(subscriptionId, resourceGroupName, clusterName, apiVersion);
        // TODO: test validations
    }

}
