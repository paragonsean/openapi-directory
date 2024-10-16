/*
 * Wayback API
 * API for Internet Archive's Wayback Machine
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.AvailabilityRequest;
import org.openapitools.client.model.AvailabilityResults;
import java.math.BigDecimal;
import org.openapitools.client.model.Error;
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
     * @throws ApiException if the Api call fails
     */
    @Test
    public void waybackV1AvailableGetTest() throws ApiException {
        String url = null;
        String timestamp = null;
        String paramCallback = null;
        BigDecimal timeout = null;
        String closest = null;
        Integer statusCode = null;
        String tag = null;
        api.waybackV1AvailableGet(url, timestamp, paramCallback, timeout, closest, statusCode, tag);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void waybackV1AvailablePostTest() throws ApiException {
        String url = null;
        String timestamp = null;
        String paramCallback = null;
        BigDecimal timeout = null;
        String closest = null;
        Integer statusCode = null;
        String tag = null;
        List<AvailabilityRequest> availabilityRequest = null;
        api.waybackV1AvailablePost(url, timestamp, paramCallback, timeout, closest, statusCode, tag, availabilityRequest);
        // TODO: test validations
    }

}
