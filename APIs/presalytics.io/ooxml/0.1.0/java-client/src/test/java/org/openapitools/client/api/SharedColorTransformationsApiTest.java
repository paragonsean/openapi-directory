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
import org.openapitools.client.model.SharedColorTransformations;
import java.util.UUID;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for SharedColorTransformationsApi
 */
@Disabled
public class SharedColorTransformationsApiTest {

    private final SharedColorTransformationsApi api = new SharedColorTransformationsApi();

    /**
     * ColorTransformations: Get by Id
     *
     * Get by Id: Use this method to retrieve a ColorTransformations object by its primary key (id)
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void sharedColortransformationsGetIdTest() throws ApiException {
        UUID id = null;
        SharedColorTransformations response = api.sharedColortransformationsGetId(id);
        // TODO: test validations
    }

}
