/*
 * StorSimple8000SeriesManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2017-06-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.EncryptionSettings;
import org.openapitools.client.model.FeatureList;
import org.openapitools.client.model.Key;
import org.openapitools.client.model.Manager;
import org.openapitools.client.model.ManagerExtendedInfo;
import org.openapitools.client.model.ManagerList;
import org.openapitools.client.model.ManagerPatch;
import org.openapitools.client.model.MetricDefinitionList;
import org.openapitools.client.model.MetricList;
import org.openapitools.client.model.PublicKey;
import org.openapitools.client.model.SymmetricEncryptedSecret;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for ManagersApi
 */
@Disabled
public class ManagersApiTest {

    private final ManagersApi api = new ManagersApi();

    /**
     * Creates the extended info of the manager.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void managersCreateExtendedInfoTest() throws ApiException {
        String subscriptionId = null;
        String resourceGroupName = null;
        String managerName = null;
        String apiVersion = null;
        ManagerExtendedInfo parameters = null;
        ManagerExtendedInfo response = api.managersCreateExtendedInfo(subscriptionId, resourceGroupName, managerName, apiVersion, parameters);
        // TODO: test validations
    }

    /**
     * Creates or updates the manager.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void managersCreateOrUpdateTest() throws ApiException {
        String subscriptionId = null;
        String resourceGroupName = null;
        String managerName = null;
        String apiVersion = null;
        Manager parameters = null;
        Manager response = api.managersCreateOrUpdate(subscriptionId, resourceGroupName, managerName, apiVersion, parameters);
        // TODO: test validations
    }

    /**
     * Deletes the manager.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void managersDeleteTest() throws ApiException {
        String subscriptionId = null;
        String resourceGroupName = null;
        String managerName = null;
        String apiVersion = null;
        api.managersDelete(subscriptionId, resourceGroupName, managerName, apiVersion);
        // TODO: test validations
    }

    /**
     * Deletes the extended info of the manager.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void managersDeleteExtendedInfoTest() throws ApiException {
        String subscriptionId = null;
        String resourceGroupName = null;
        String managerName = null;
        String apiVersion = null;
        api.managersDeleteExtendedInfo(subscriptionId, resourceGroupName, managerName, apiVersion);
        // TODO: test validations
    }

    /**
     * Returns the properties of the specified manager name.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void managersGetTest() throws ApiException {
        String subscriptionId = null;
        String resourceGroupName = null;
        String managerName = null;
        String apiVersion = null;
        Manager response = api.managersGet(subscriptionId, resourceGroupName, managerName, apiVersion);
        // TODO: test validations
    }

    /**
     * Returns the activation key of the manager.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void managersGetActivationKeyTest() throws ApiException {
        String subscriptionId = null;
        String resourceGroupName = null;
        String managerName = null;
        String apiVersion = null;
        Key response = api.managersGetActivationKey(subscriptionId, resourceGroupName, managerName, apiVersion);
        // TODO: test validations
    }

    /**
     * Returns the public encryption key of the device.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void managersGetDevicePublicEncryptionKeyTest() throws ApiException {
        String deviceName = null;
        String subscriptionId = null;
        String resourceGroupName = null;
        String managerName = null;
        String apiVersion = null;
        PublicKey response = api.managersGetDevicePublicEncryptionKey(deviceName, subscriptionId, resourceGroupName, managerName, apiVersion);
        // TODO: test validations
    }

    /**
     * Returns the encryption settings of the manager.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void managersGetEncryptionSettingsTest() throws ApiException {
        String subscriptionId = null;
        String resourceGroupName = null;
        String managerName = null;
        String apiVersion = null;
        EncryptionSettings response = api.managersGetEncryptionSettings(subscriptionId, resourceGroupName, managerName, apiVersion);
        // TODO: test validations
    }

    /**
     * Returns the extended information of the specified manager name.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void managersGetExtendedInfoTest() throws ApiException {
        String subscriptionId = null;
        String resourceGroupName = null;
        String managerName = null;
        String apiVersion = null;
        ManagerExtendedInfo response = api.managersGetExtendedInfo(subscriptionId, resourceGroupName, managerName, apiVersion);
        // TODO: test validations
    }

    /**
     * Returns the symmetric encrypted public encryption key of the manager.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void managersGetPublicEncryptionKeyTest() throws ApiException {
        String subscriptionId = null;
        String resourceGroupName = null;
        String managerName = null;
        String apiVersion = null;
        SymmetricEncryptedSecret response = api.managersGetPublicEncryptionKey(subscriptionId, resourceGroupName, managerName, apiVersion);
        // TODO: test validations
    }

    /**
     * Retrieves all the managers in a subscription.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void managersListTest() throws ApiException {
        String subscriptionId = null;
        String apiVersion = null;
        ManagerList response = api.managersList(subscriptionId, apiVersion);
        // TODO: test validations
    }

    /**
     * Retrieves all the managers in a resource group.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void managersListByResourceGroupTest() throws ApiException {
        String subscriptionId = null;
        String resourceGroupName = null;
        String apiVersion = null;
        ManagerList response = api.managersListByResourceGroup(subscriptionId, resourceGroupName, apiVersion);
        // TODO: test validations
    }

    /**
     * Lists the features and their support status
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void managersListFeatureSupportStatusTest() throws ApiException {
        String subscriptionId = null;
        String resourceGroupName = null;
        String managerName = null;
        String apiVersion = null;
        String $filter = null;
        FeatureList response = api.managersListFeatureSupportStatus(subscriptionId, resourceGroupName, managerName, apiVersion, $filter);
        // TODO: test validations
    }

    /**
     * Gets the metric definitions for the specified manager.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void managersListMetricDefinitionTest() throws ApiException {
        String subscriptionId = null;
        String resourceGroupName = null;
        String managerName = null;
        String apiVersion = null;
        MetricDefinitionList response = api.managersListMetricDefinition(subscriptionId, resourceGroupName, managerName, apiVersion);
        // TODO: test validations
    }

    /**
     * Gets the metrics for the specified manager.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void managersListMetricsTest() throws ApiException {
        String subscriptionId = null;
        String resourceGroupName = null;
        String managerName = null;
        String apiVersion = null;
        String $filter = null;
        MetricList response = api.managersListMetrics(subscriptionId, resourceGroupName, managerName, apiVersion, $filter);
        // TODO: test validations
    }

    /**
     * Re-generates and returns the activation key of the manager.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void managersRegenerateActivationKeyTest() throws ApiException {
        String subscriptionId = null;
        String resourceGroupName = null;
        String managerName = null;
        String apiVersion = null;
        Key response = api.managersRegenerateActivationKey(subscriptionId, resourceGroupName, managerName, apiVersion);
        // TODO: test validations
    }

    /**
     * Updates the StorSimple Manager.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void managersUpdateTest() throws ApiException {
        String subscriptionId = null;
        String resourceGroupName = null;
        String managerName = null;
        String apiVersion = null;
        ManagerPatch parameters = null;
        Manager response = api.managersUpdate(subscriptionId, resourceGroupName, managerName, apiVersion, parameters);
        // TODO: test validations
    }

    /**
     * Updates the extended info of the manager.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void managersUpdateExtendedInfoTest() throws ApiException {
        String subscriptionId = null;
        String resourceGroupName = null;
        String managerName = null;
        String apiVersion = null;
        String ifMatch = null;
        ManagerExtendedInfo parameters = null;
        ManagerExtendedInfo response = api.managersUpdateExtendedInfo(subscriptionId, resourceGroupName, managerName, apiVersion, ifMatch, parameters);
        // TODO: test validations
    }

}
