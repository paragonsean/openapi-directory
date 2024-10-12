/*
 * Otoroshi Admin API
 * Admin API of the Otoroshi reverse proxy
 *
 * The version of the OpenAPI document: 1.5.0-dev
 * Contact: oss@maif.fr
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.OtoroshiHealth;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for HealthApi
 */
@Disabled
public class HealthApiTest {

    private final HealthApi api = new HealthApi();

    /**
     * Return current Otoroshi health
     *
     * Import the full state of Otoroshi as a file
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void healthTest() throws ApiException {
        OtoroshiHealth response = api.health();
        // TODO: test validations
    }

}
