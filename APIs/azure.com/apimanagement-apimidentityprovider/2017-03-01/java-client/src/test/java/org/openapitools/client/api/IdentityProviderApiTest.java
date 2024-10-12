/*
 * ApiManagementClient
 * Use these REST APIs for performing operations on Identity Provider entity associated with your Azure API Management deployment. Setting up an external Identity Provider for authentication can help you manage the developer portal logins using the OAuth2 flow.
 *
 * The version of the OpenAPI document: 2017-03-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.IdentityProviderContract;
import org.openapitools.client.model.IdentityProviderList;
import org.openapitools.client.model.IdentityProviderListByServiceDefaultResponse;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for IdentityProviderApi
 */
@Disabled
public class IdentityProviderApiTest {

    private final IdentityProviderApi api = new IdentityProviderApi();

    /**
     * Creates or Updates the IdentityProvider configuration.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void identityProviderCreateOrUpdateTest() throws ApiException {
        String resourceGroupName = null;
        String serviceName = null;
        String identityProviderName = null;
        String apiVersion = null;
        String subscriptionId = null;
        IdentityProviderContract parameters = null;
        IdentityProviderContract response = api.identityProviderCreateOrUpdate(resourceGroupName, serviceName, identityProviderName, apiVersion, subscriptionId, parameters);
        // TODO: test validations
    }

    /**
     * Deletes the specified identity provider configuration.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void identityProviderDeleteTest() throws ApiException {
        String resourceGroupName = null;
        String serviceName = null;
        String identityProviderName = null;
        String ifMatch = null;
        String apiVersion = null;
        String subscriptionId = null;
        api.identityProviderDelete(resourceGroupName, serviceName, identityProviderName, ifMatch, apiVersion, subscriptionId);
        // TODO: test validations
    }

    /**
     * Gets the configuration details of the identity Provider configured in specified service instance.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void identityProviderGetTest() throws ApiException {
        String subscriptionId = null;
        String resourceGroupName = null;
        String serviceName = null;
        String identityProviderName = null;
        String apiVersion = null;
        IdentityProviderContract response = api.identityProviderGet(subscriptionId, resourceGroupName, serviceName, identityProviderName, apiVersion);
        // TODO: test validations
    }

    /**
     * Gets the entity state (Etag) version of the identityProvider specified by its identifier.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void identityProviderGetEntityTagTest() throws ApiException {
        String subscriptionId = null;
        String resourceGroupName = null;
        String serviceName = null;
        String identityProviderName = null;
        String apiVersion = null;
        api.identityProviderGetEntityTag(subscriptionId, resourceGroupName, serviceName, identityProviderName, apiVersion);
        // TODO: test validations
    }

    /**
     * Lists a collection of Identity Provider configured in the specified service instance.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void identityProviderListByServiceTest() throws ApiException {
        String subscriptionId = null;
        String resourceGroupName = null;
        String serviceName = null;
        String apiVersion = null;
        IdentityProviderList response = api.identityProviderListByService(subscriptionId, resourceGroupName, serviceName, apiVersion);
        // TODO: test validations
    }

}
