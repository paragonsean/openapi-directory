/*
 * agentOS API V3, Maintenance Call Group
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v3-maintenance
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.MaintenanceIssueModel;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for MaintenanceControllerApi
 */
@Disabled
public class MaintenanceControllerApiTest {

    private final MaintenanceControllerApi api = new MaintenanceControllerApi();

    /**
     * Create a maintenance job for a specific branch
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void maintenanceControllerCreateMaintenanceJobTest() throws ApiException {
        String shortName = null;
        String branchID = null;
        MaintenanceIssueModel maintenanceIssueModel = null;
        Object response = api.maintenanceControllerCreateMaintenanceJob(shortName, branchID, maintenanceIssueModel);
        // TODO: test validations
    }

}
