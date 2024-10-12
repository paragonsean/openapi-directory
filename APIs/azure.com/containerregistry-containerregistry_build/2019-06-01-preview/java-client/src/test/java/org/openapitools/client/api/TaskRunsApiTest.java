/*
 * ContainerRegistryManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-06-01-preview
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.ErrorSchema;
import org.openapitools.client.model.TaskRun;
import org.openapitools.client.model.TaskRunListResult;
import org.openapitools.client.model.TaskRunUpdateParameters;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for TaskRunsApi
 */
@Disabled
public class TaskRunsApiTest {

    private final TaskRunsApi api = new TaskRunsApi();

    /**
     * Creates a task run for a container registry with the specified parameters.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void taskRunsCreateTest() throws ApiException {
        String subscriptionId = null;
        String resourceGroupName = null;
        String registryName = null;
        String apiVersion = null;
        String taskRunName = null;
        TaskRun taskRun = null;
        TaskRun response = api.taskRunsCreate(subscriptionId, resourceGroupName, registryName, apiVersion, taskRunName, taskRun);
        // TODO: test validations
    }

    /**
     * Deletes a specified task run resource.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void taskRunsDeleteTest() throws ApiException {
        String subscriptionId = null;
        String resourceGroupName = null;
        String registryName = null;
        String apiVersion = null;
        String taskRunName = null;
        api.taskRunsDelete(subscriptionId, resourceGroupName, registryName, apiVersion, taskRunName);
        // TODO: test validations
    }

    /**
     * Gets the detailed information for a given task run.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void taskRunsGetTest() throws ApiException {
        String subscriptionId = null;
        String resourceGroupName = null;
        String registryName = null;
        String apiVersion = null;
        String taskRunName = null;
        TaskRun response = api.taskRunsGet(subscriptionId, resourceGroupName, registryName, apiVersion, taskRunName);
        // TODO: test validations
    }

    /**
     * Lists all the task runs for a specified container registry.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void taskRunsListTest() throws ApiException {
        String subscriptionId = null;
        String resourceGroupName = null;
        String registryName = null;
        String apiVersion = null;
        TaskRunListResult response = api.taskRunsList(subscriptionId, resourceGroupName, registryName, apiVersion);
        // TODO: test validations
    }

    /**
     * Updates a task run with the specified parameters.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void taskRunsUpdateTest() throws ApiException {
        String subscriptionId = null;
        String resourceGroupName = null;
        String registryName = null;
        String apiVersion = null;
        String taskRunName = null;
        TaskRunUpdateParameters updateParameters = null;
        TaskRun response = api.taskRunsUpdate(subscriptionId, resourceGroupName, registryName, apiVersion, taskRunName, updateParameters);
        // TODO: test validations
    }

}
