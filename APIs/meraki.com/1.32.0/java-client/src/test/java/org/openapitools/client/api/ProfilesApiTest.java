/*
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 05 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 1.32.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.CreateNetworkSensorAlertsProfileRequest;
import org.openapitools.client.model.CreateOrganizationAlertsProfileRequest;
import org.openapitools.client.model.GetNetworkSensorAlertsProfiles200ResponseInner;
import org.openapitools.client.model.GetNetworkSmProfiles200ResponseInner;
import org.openapitools.client.model.GetOrganizationConfigTemplateSwitchProfilePorts200ResponseInner;
import org.openapitools.client.model.GetOrganizationConfigTemplateSwitchProfiles200Response;
import org.openapitools.client.model.UpdateNetworkSensorAlertsProfileRequest;
import org.openapitools.client.model.UpdateOrganizationAlertsProfileRequest;
import org.openapitools.client.model.UpdateOrganizationConfigTemplateSwitchProfilePortRequest;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for ProfilesApi
 */
@Disabled
public class ProfilesApiTest {

    private final ProfilesApi api = new ProfilesApi();

    /**
     * Creates a sensor alert profile for a network.
     *
     * Creates a sensor alert profile for a network.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createNetworkSensorAlertsProfile_2Test() throws ApiException {
        String networkId = null;
        CreateNetworkSensorAlertsProfileRequest createNetworkSensorAlertsProfileRequest = null;
        GetNetworkSensorAlertsProfiles200ResponseInner response = api.createNetworkSensorAlertsProfile_2(networkId, createNetworkSensorAlertsProfileRequest);
        // TODO: test validations
    }

    /**
     * Create an organization-wide alert configuration
     *
     * Create an organization-wide alert configuration
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createOrganizationAlertsProfile_2Test() throws ApiException {
        String organizationId = null;
        CreateOrganizationAlertsProfileRequest createOrganizationAlertsProfileRequest = null;
        Object response = api.createOrganizationAlertsProfile_2(organizationId, createOrganizationAlertsProfileRequest);
        // TODO: test validations
    }

    /**
     * Deletes a sensor alert profile from a network.
     *
     * Deletes a sensor alert profile from a network.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteNetworkSensorAlertsProfile_2Test() throws ApiException {
        String networkId = null;
        String id = null;
        api.deleteNetworkSensorAlertsProfile_2(networkId, id);
        // TODO: test validations
    }

    /**
     * Removes an organization-wide alert config
     *
     * Removes an organization-wide alert config
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteOrganizationAlertsProfile_2Test() throws ApiException {
        String organizationId = null;
        String alertConfigId = null;
        api.deleteOrganizationAlertsProfile_2(organizationId, alertConfigId);
        // TODO: test validations
    }

    /**
     * Show details of a sensor alert profile for a network.
     *
     * Show details of a sensor alert profile for a network.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getNetworkSensorAlertsProfile_2Test() throws ApiException {
        String networkId = null;
        String id = null;
        GetNetworkSensorAlertsProfiles200ResponseInner response = api.getNetworkSensorAlertsProfile_2(networkId, id);
        // TODO: test validations
    }

    /**
     * Lists all sensor alert profiles for a network.
     *
     * Lists all sensor alert profiles for a network.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getNetworkSensorAlertsProfiles_2Test() throws ApiException {
        String networkId = null;
        List<GetNetworkSensorAlertsProfiles200ResponseInner> response = api.getNetworkSensorAlertsProfiles_2(networkId);
        // TODO: test validations
    }

    /**
     * List all profiles in a network
     *
     * List all profiles in a network
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getNetworkSmProfiles_1Test() throws ApiException {
        String networkId = null;
        List<GetNetworkSmProfiles200ResponseInner> response = api.getNetworkSmProfiles_1(networkId);
        // TODO: test validations
    }

    /**
     * List all organization-wide alert configurations
     *
     * List all organization-wide alert configurations
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getOrganizationAlertsProfiles_2Test() throws ApiException {
        String organizationId = null;
        List<Object> response = api.getOrganizationAlertsProfiles_2(organizationId);
        // TODO: test validations
    }

    /**
     * Return a switch profile port
     *
     * Return a switch profile port
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getOrganizationConfigTemplateSwitchProfilePort_2Test() throws ApiException {
        String organizationId = null;
        String configTemplateId = null;
        String profileId = null;
        String portId = null;
        GetOrganizationConfigTemplateSwitchProfilePorts200ResponseInner response = api.getOrganizationConfigTemplateSwitchProfilePort_2(organizationId, configTemplateId, profileId, portId);
        // TODO: test validations
    }

    /**
     * Return all the ports of a switch profile
     *
     * Return all the ports of a switch profile
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getOrganizationConfigTemplateSwitchProfilePorts_2Test() throws ApiException {
        String organizationId = null;
        String configTemplateId = null;
        String profileId = null;
        List<GetOrganizationConfigTemplateSwitchProfilePorts200ResponseInner> response = api.getOrganizationConfigTemplateSwitchProfilePorts_2(organizationId, configTemplateId, profileId);
        // TODO: test validations
    }

    /**
     * List the switch profiles for your switch template configuration
     *
     * List the switch profiles for your switch template configuration
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getOrganizationConfigTemplateSwitchProfiles_2Test() throws ApiException {
        String organizationId = null;
        String configTemplateId = null;
        GetOrganizationConfigTemplateSwitchProfiles200Response response = api.getOrganizationConfigTemplateSwitchProfiles_2(organizationId, configTemplateId);
        // TODO: test validations
    }

    /**
     * Updates a sensor alert profile for a network.
     *
     * Updates a sensor alert profile for a network.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateNetworkSensorAlertsProfile_2Test() throws ApiException {
        String networkId = null;
        String id = null;
        UpdateNetworkSensorAlertsProfileRequest updateNetworkSensorAlertsProfileRequest = null;
        GetNetworkSensorAlertsProfiles200ResponseInner response = api.updateNetworkSensorAlertsProfile_2(networkId, id, updateNetworkSensorAlertsProfileRequest);
        // TODO: test validations
    }

    /**
     * Update an organization-wide alert config
     *
     * Update an organization-wide alert config
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateOrganizationAlertsProfile_2Test() throws ApiException {
        String organizationId = null;
        String alertConfigId = null;
        UpdateOrganizationAlertsProfileRequest updateOrganizationAlertsProfileRequest = null;
        Object response = api.updateOrganizationAlertsProfile_2(organizationId, alertConfigId, updateOrganizationAlertsProfileRequest);
        // TODO: test validations
    }

    /**
     * Update a switch profile port
     *
     * Update a switch profile port
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateOrganizationConfigTemplateSwitchProfilePort_2Test() throws ApiException {
        String organizationId = null;
        String configTemplateId = null;
        String profileId = null;
        String portId = null;
        UpdateOrganizationConfigTemplateSwitchProfilePortRequest updateOrganizationConfigTemplateSwitchProfilePortRequest = null;
        GetOrganizationConfigTemplateSwitchProfilePorts200ResponseInner response = api.updateOrganizationConfigTemplateSwitchProfilePort_2(organizationId, configTemplateId, profileId, portId, updateOrganizationConfigTemplateSwitchProfilePortRequest);
        // TODO: test validations
    }

}
