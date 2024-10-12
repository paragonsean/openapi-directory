/*
 * Azure Machine Learning Model Management Service
 * These APIs allow end users to manage Azure Machine Learning Models, Images, Profiles, and Services.
 *
 * The version of the OpenAPI document: 2019-09-30
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.AuthToken;
import org.openapitools.client.model.ModelErrorResponse;
import java.util.UUID;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for TokenApi
 */
@Disabled
public class TokenApiTest {

    private final TokenApi api = new TokenApi();

    /**
     * Generate Service Access Token.
     *
     * Gets access token that can be used for calling service.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void servicesGetServiceToken_0Test() throws ApiException {
        UUID subscriptionId = null;
        String resourceGroup = null;
        String workspace = null;
        String id = null;
        AuthToken response = api.servicesGetServiceToken_0(subscriptionId, resourceGroup, workspace, id);
        // TODO: test validations
    }

}
