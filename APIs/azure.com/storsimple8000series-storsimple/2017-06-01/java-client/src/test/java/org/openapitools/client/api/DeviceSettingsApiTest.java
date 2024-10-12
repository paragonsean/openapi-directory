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
import org.openapitools.client.model.AlertSettings;
import org.openapitools.client.model.NetworkSettings;
import org.openapitools.client.model.NetworkSettingsPatch;
import org.openapitools.client.model.SecuritySettings;
import org.openapitools.client.model.SecuritySettingsPatch;
import org.openapitools.client.model.TimeSettings;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for DeviceSettingsApi
 */
@Disabled
public class DeviceSettingsApiTest {

    private final DeviceSettingsApi api = new DeviceSettingsApi();

    /**
     * Creates or updates the alert settings of the specified device.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deviceSettingsCreateOrUpdateAlertSettingsTest() throws ApiException {
        String deviceName = null;
        String subscriptionId = null;
        String resourceGroupName = null;
        String managerName = null;
        String apiVersion = null;
        AlertSettings parameters = null;
        AlertSettings response = api.deviceSettingsCreateOrUpdateAlertSettings(deviceName, subscriptionId, resourceGroupName, managerName, apiVersion, parameters);
        // TODO: test validations
    }

    /**
     * Creates or updates the time settings of the specified device.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deviceSettingsCreateOrUpdateTimeSettingsTest() throws ApiException {
        String deviceName = null;
        String subscriptionId = null;
        String resourceGroupName = null;
        String managerName = null;
        String apiVersion = null;
        TimeSettings parameters = null;
        TimeSettings response = api.deviceSettingsCreateOrUpdateTimeSettings(deviceName, subscriptionId, resourceGroupName, managerName, apiVersion, parameters);
        // TODO: test validations
    }

    /**
     * Gets the alert settings of the specified device.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deviceSettingsGetAlertSettingsTest() throws ApiException {
        String deviceName = null;
        String subscriptionId = null;
        String resourceGroupName = null;
        String managerName = null;
        String apiVersion = null;
        AlertSettings response = api.deviceSettingsGetAlertSettings(deviceName, subscriptionId, resourceGroupName, managerName, apiVersion);
        // TODO: test validations
    }

    /**
     * Gets the network settings of the specified device.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deviceSettingsGetNetworkSettingsTest() throws ApiException {
        String deviceName = null;
        String subscriptionId = null;
        String resourceGroupName = null;
        String managerName = null;
        String apiVersion = null;
        NetworkSettings response = api.deviceSettingsGetNetworkSettings(deviceName, subscriptionId, resourceGroupName, managerName, apiVersion);
        // TODO: test validations
    }

    /**
     * Returns the Security properties of the specified device name.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deviceSettingsGetSecuritySettingsTest() throws ApiException {
        String deviceName = null;
        String subscriptionId = null;
        String resourceGroupName = null;
        String managerName = null;
        String apiVersion = null;
        SecuritySettings response = api.deviceSettingsGetSecuritySettings(deviceName, subscriptionId, resourceGroupName, managerName, apiVersion);
        // TODO: test validations
    }

    /**
     * Gets the time settings of the specified device.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deviceSettingsGetTimeSettingsTest() throws ApiException {
        String deviceName = null;
        String subscriptionId = null;
        String resourceGroupName = null;
        String managerName = null;
        String apiVersion = null;
        TimeSettings response = api.deviceSettingsGetTimeSettings(deviceName, subscriptionId, resourceGroupName, managerName, apiVersion);
        // TODO: test validations
    }

    /**
     * sync Remote management Certificate between appliance and Service
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deviceSettingsSyncRemotemanagementCertificateTest() throws ApiException {
        String deviceName = null;
        String subscriptionId = null;
        String resourceGroupName = null;
        String managerName = null;
        String apiVersion = null;
        api.deviceSettingsSyncRemotemanagementCertificate(deviceName, subscriptionId, resourceGroupName, managerName, apiVersion);
        // TODO: test validations
    }

    /**
     * Updates the network settings on the specified device.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deviceSettingsUpdateNetworkSettingsTest() throws ApiException {
        String deviceName = null;
        String subscriptionId = null;
        String resourceGroupName = null;
        String managerName = null;
        String apiVersion = null;
        NetworkSettingsPatch parameters = null;
        NetworkSettings response = api.deviceSettingsUpdateNetworkSettings(deviceName, subscriptionId, resourceGroupName, managerName, apiVersion, parameters);
        // TODO: test validations
    }

    /**
     * Patch Security properties of the specified device name.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deviceSettingsUpdateSecuritySettingsTest() throws ApiException {
        String deviceName = null;
        String subscriptionId = null;
        String resourceGroupName = null;
        String managerName = null;
        String apiVersion = null;
        SecuritySettingsPatch parameters = null;
        SecuritySettings response = api.deviceSettingsUpdateSecuritySettings(deviceName, subscriptionId, resourceGroupName, managerName, apiVersion, parameters);
        // TODO: test validations
    }

}
