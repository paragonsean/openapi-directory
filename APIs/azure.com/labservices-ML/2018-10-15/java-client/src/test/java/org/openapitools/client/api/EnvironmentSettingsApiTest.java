/*
 * ManagedLabsClient
 * The Managed Labs Client.
 *
 * The version of the OpenAPI document: 2018-10-15
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.CloudError;
import org.openapitools.client.model.EnvironmentSetting;
import org.openapitools.client.model.EnvironmentSettingFragment;
import org.openapitools.client.model.PublishPayload;
import org.openapitools.client.model.ResponseWithContinuationEnvironmentSetting;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for EnvironmentSettingsApi
 */
@Disabled
public class EnvironmentSettingsApiTest {

    private final EnvironmentSettingsApi api = new EnvironmentSettingsApi();

    /**
     * Claims a random environment for a user in an environment settings
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void environmentSettingsClaimAnyTest() throws ApiException {
        String subscriptionId = null;
        String resourceGroupName = null;
        String labAccountName = null;
        String labName = null;
        String environmentSettingName = null;
        String apiVersion = null;
        api.environmentSettingsClaimAny(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, apiVersion);
        // TODO: test validations
    }

    /**
     * Create or replace an existing Environment Setting. This operation can take a while to complete
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void environmentSettingsCreateOrUpdateTest() throws ApiException {
        String subscriptionId = null;
        String resourceGroupName = null;
        String labAccountName = null;
        String labName = null;
        String environmentSettingName = null;
        String apiVersion = null;
        EnvironmentSetting environmentSetting = null;
        EnvironmentSetting response = api.environmentSettingsCreateOrUpdate(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, apiVersion, environmentSetting);
        // TODO: test validations
    }

    /**
     * Delete environment setting. This operation can take a while to complete
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void environmentSettingsDeleteTest() throws ApiException {
        String subscriptionId = null;
        String resourceGroupName = null;
        String labAccountName = null;
        String labName = null;
        String environmentSettingName = null;
        String apiVersion = null;
        api.environmentSettingsDelete(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, apiVersion);
        // TODO: test validations
    }

    /**
     * Get environment setting
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void environmentSettingsGetTest() throws ApiException {
        String subscriptionId = null;
        String resourceGroupName = null;
        String labAccountName = null;
        String labName = null;
        String environmentSettingName = null;
        String apiVersion = null;
        String $expand = null;
        EnvironmentSetting response = api.environmentSettingsGet(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, apiVersion, $expand);
        // TODO: test validations
    }

    /**
     * List environment setting in a given lab.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void environmentSettingsListTest() throws ApiException {
        String subscriptionId = null;
        String resourceGroupName = null;
        String labAccountName = null;
        String labName = null;
        String apiVersion = null;
        String $expand = null;
        String $filter = null;
        Integer $top = null;
        String $orderby = null;
        ResponseWithContinuationEnvironmentSetting response = api.environmentSettingsList(subscriptionId, resourceGroupName, labAccountName, labName, apiVersion, $expand, $filter, $top, $orderby);
        // TODO: test validations
    }

    /**
     * Provisions/deprovisions required resources for an environment setting based on current state of the lab/environment setting.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void environmentSettingsPublishTest() throws ApiException {
        String subscriptionId = null;
        String resourceGroupName = null;
        String labAccountName = null;
        String labName = null;
        String environmentSettingName = null;
        String apiVersion = null;
        PublishPayload publishPayload = null;
        api.environmentSettingsPublish(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, apiVersion, publishPayload);
        // TODO: test validations
    }

    /**
     * Starts a template by starting all resources inside the template. This operation can take a while to complete
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void environmentSettingsStartTest() throws ApiException {
        String subscriptionId = null;
        String resourceGroupName = null;
        String labAccountName = null;
        String labName = null;
        String environmentSettingName = null;
        String apiVersion = null;
        api.environmentSettingsStart(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, apiVersion);
        // TODO: test validations
    }

    /**
     * Starts a template by starting all resources inside the template. This operation can take a while to complete
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void environmentSettingsStopTest() throws ApiException {
        String subscriptionId = null;
        String resourceGroupName = null;
        String labAccountName = null;
        String labName = null;
        String environmentSettingName = null;
        String apiVersion = null;
        api.environmentSettingsStop(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, apiVersion);
        // TODO: test validations
    }

    /**
     * Modify properties of environment setting.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void environmentSettingsUpdateTest() throws ApiException {
        String subscriptionId = null;
        String resourceGroupName = null;
        String labAccountName = null;
        String labName = null;
        String environmentSettingName = null;
        String apiVersion = null;
        EnvironmentSettingFragment environmentSetting = null;
        EnvironmentSetting response = api.environmentSettingsUpdate(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, apiVersion, environmentSetting);
        // TODO: test validations
    }

}
