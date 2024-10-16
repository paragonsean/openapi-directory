/*
 * Story
 * This API is the main entry point for creating, editing and publishing analytics throught the Presalytics API
 *
 * The version of the OpenAPI document: 0.3.1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.ProblemDetail;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for SchemasApi
 */
@Disabled
public class SchemasApiTest {

    private final SchemasApi api = new SchemasApi();

    /**
     * Story Outline Schema
     *
     * Json Schema for validating Story Outline objects
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void storyOutlineSchemaTest() throws ApiException {
        String schemaVersion = null;
        api.storyOutlineSchema(schemaVersion);
        // TODO: test validations
    }

}
