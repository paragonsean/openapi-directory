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
import org.openapitools.client.model.ErrorResponse;
import org.openapitools.client.model.GetDaemonToken200Response;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for DaemonApi
 */
@Disabled
public class DaemonApiTest {

    private final DaemonApi api = new DaemonApi();

    /**
     * Get a token for opening a daemon connection
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getDaemonTokenTest() throws ApiException {
        String daemon = null;
        GetDaemonToken200Response response = api.getDaemonToken(daemon);
        // TODO: test validations
    }

}
