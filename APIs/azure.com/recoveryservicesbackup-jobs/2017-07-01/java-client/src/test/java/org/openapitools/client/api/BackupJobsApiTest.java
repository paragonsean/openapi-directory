/*
 * RecoveryServicesBackupClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2017-07-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.JobResourceList;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for BackupJobsApi
 */
@Disabled
public class BackupJobsApiTest {

    private final BackupJobsApi api = new BackupJobsApi();

    /**
     * Provides a pageable list of jobs.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void backupJobsListTest() throws ApiException {
        String apiVersion = null;
        String vaultName = null;
        String resourceGroupName = null;
        String subscriptionId = null;
        String $filter = null;
        String $skipToken = null;
        JobResourceList response = api.backupJobsList(apiVersion, vaultName, resourceGroupName, subscriptionId, $filter, $skipToken);
        // TODO: test validations
    }

}
