/*
 * Mailscript
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.4.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.AddWorkspaceRequest;
import org.openapitools.client.model.ErrorResponse;
import org.openapitools.client.model.GetAllWorkspacesResponse;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for WorkspacesApi
 */
@Disabled
public class WorkspacesApiTest {

    private final WorkspacesApi api = new WorkspacesApi();

    /**
     * Claim a Mailscript workspace
     *
     * An attendant address will be created as well
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void addWorkspaceTest() throws ApiException {
        AddWorkspaceRequest addWorkspaceRequest = null;
        api.addWorkspace(addWorkspaceRequest);
        // TODO: test validations
    }

    /**
     * Get all workspaces you have access to
     *
     * 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getAllWorkspacesTest() throws ApiException {
        GetAllWorkspacesResponse response = api.getAllWorkspaces();
        // TODO: test validations
    }

}
