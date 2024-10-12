/*
 * OOXML Automation
 * This API helps users convert Excel and Powerpoint documents into rich, live dashboards and stories.
 *
 * The version of the OpenAPI document: 0.1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.SharedSolidFills;
import java.util.UUID;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for SharedSolidFillsApi
 */
@Disabled
public class SharedSolidFillsApiTest {

    private final SharedSolidFillsApi api = new SharedSolidFillsApi();

    /**
     * SolidFills: Get by Id
     *
     * Get by Id: Use this method to retrieve a SolidFills object by its primary key (id)
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void sharedSolidfillsGetIdTest() throws ApiException {
        UUID id = null;
        SharedSolidFills response = api.sharedSolidfillsGetId(id);
        // TODO: test validations
    }

}
