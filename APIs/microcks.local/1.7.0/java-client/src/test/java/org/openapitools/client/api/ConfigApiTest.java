/*
 * Microcks API v1.7
 * API offered by Microcks, the Kubernetes native tools for API and microservices mocking and testing (microcks.io)
 *
 * The version of the OpenAPI document: 1.7.0
 * Contact: laurent@microcks.io
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.Counter;
import org.openapitools.client.model.KeycloakConfig;
import org.openapitools.client.model.Secret;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for ConfigApi
 */
@Disabled
public class ConfigApiTest {

    private final ConfigApi api = new ConfigApi();

    /**
     * Create a new Secret
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createSecretTest() throws ApiException {
        Secret secret = null;
        Secret response = api.createSecret(secret);
        // TODO: test validations
    }

    /**
     * Delete Secret
     *
     * Delete a Secret
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteSecretTest() throws ApiException {
        String id = null;
        api.deleteSecret(id);
        // TODO: test validations
    }

    /**
     * Get features configuration
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getFeaturesConfigurationTest() throws ApiException {
        api.getFeaturesConfiguration();
        // TODO: test validations
    }

    /**
     * Get authentification configuration
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getKeycloakConfigTest() throws ApiException {
        KeycloakConfig response = api.getKeycloakConfig();
        // TODO: test validations
    }

    /**
     * Get Secret
     *
     * Retrieve a Secret
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getSecretTest() throws ApiException {
        String id = null;
        Secret response = api.getSecret(id);
        // TODO: test validations
    }

    /**
     * Get Secrets
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getSecretsTest() throws ApiException {
        Integer page = null;
        Integer size = null;
        List<Secret> response = api.getSecrets(page, size);
        // TODO: test validations
    }

    /**
     * Get the Secrets counter
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getSecretsCounterTest() throws ApiException {
        Counter response = api.getSecretsCounter();
        // TODO: test validations
    }

    /**
     * Update Secret
     *
     * Update a Secret
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateSecretTest() throws ApiException {
        String id = null;
        api.updateSecret(id);
        // TODO: test validations
    }

}
