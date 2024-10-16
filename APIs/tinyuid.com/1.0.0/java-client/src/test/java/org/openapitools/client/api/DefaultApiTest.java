/*
 * TinyUID.com
 * Paste a Long URL link to shorten it
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: contact@tinyuid.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.V1ShortenPost200Response;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for DefaultApi
 */
@Disabled
public class DefaultApiTest {

    private final DefaultApi api = new DefaultApi();

    /**
     * Create short link
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void v1ShortenPostTest() throws ApiException {
        String url = null;
        V1ShortenPost200Response response = api.v1ShortenPost(url);
        // TODO: test validations
    }

}
