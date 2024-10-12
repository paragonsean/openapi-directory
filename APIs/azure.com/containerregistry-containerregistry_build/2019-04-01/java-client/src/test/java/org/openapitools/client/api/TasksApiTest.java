/*
 * ContainerRegistryManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-04-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.Task;
import org.openapitools.client.model.TaskListResult;
import org.openapitools.client.model.TaskUpdateParameters;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for TasksApi
 */
@Disabled
public class TasksApiTest {

    private final TasksApi api = new TasksApi();

    /**
     * Creates a task for a container registry with the specified parameters.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void tasksCreateTest() throws ApiException {
        String subscriptionId = null;
        String resourceGroupName = null;
        String registryName = null;
        String apiVersion = null;
        String taskName = null;
        Task taskCreateParameters = null;
        Task response = api.tasksCreate(subscriptionId, resourceGroupName, registryName, apiVersion, taskName, taskCreateParameters);
        // TODO: test validations
    }

    /**
     * Deletes a specified task.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void tasksDeleteTest() throws ApiException {
        String subscriptionId = null;
        String resourceGroupName = null;
        String registryName = null;
        String apiVersion = null;
        String taskName = null;
        api.tasksDelete(subscriptionId, resourceGroupName, registryName, apiVersion, taskName);
        // TODO: test validations
    }

    /**
     * Get the properties of a specified task.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void tasksGetTest() throws ApiException {
        String subscriptionId = null;
        String resourceGroupName = null;
        String registryName = null;
        String apiVersion = null;
        String taskName = null;
        Task response = api.tasksGet(subscriptionId, resourceGroupName, registryName, apiVersion, taskName);
        // TODO: test validations
    }

    /**
     * Returns a task with extended information that includes all secrets.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void tasksGetDetailsTest() throws ApiException {
        String subscriptionId = null;
        String resourceGroupName = null;
        String registryName = null;
        String apiVersion = null;
        String taskName = null;
        Task response = api.tasksGetDetails(subscriptionId, resourceGroupName, registryName, apiVersion, taskName);
        // TODO: test validations
    }

    /**
     * Lists all the tasks for a specified container registry.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void tasksListTest() throws ApiException {
        String subscriptionId = null;
        String resourceGroupName = null;
        String registryName = null;
        String apiVersion = null;
        TaskListResult response = api.tasksList(subscriptionId, resourceGroupName, registryName, apiVersion);
        // TODO: test validations
    }

    /**
     * Updates a task with the specified parameters.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void tasksUpdateTest() throws ApiException {
        String subscriptionId = null;
        String resourceGroupName = null;
        String registryName = null;
        String apiVersion = null;
        String taskName = null;
        TaskUpdateParameters taskUpdateParameters = null;
        Task response = api.tasksUpdate(subscriptionId, resourceGroupName, registryName, apiVersion, taskName, taskUpdateParameters);
        // TODO: test validations
    }

}
