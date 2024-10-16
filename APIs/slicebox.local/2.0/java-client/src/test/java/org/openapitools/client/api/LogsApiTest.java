/*
 * Slicebox API
 * Slicebox - safe sharing of medical images
 *
 * The version of the OpenAPI document: 2.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.LogEntry;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for LogsApi
 */
@Disabled
public class LogsApiTest {

    private final LogsApi api = new LogsApi();

    /**
     * delete all log messages
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void logDeleteTest() throws ApiException {
        api.logDelete();
        // TODO: test validations
    }

    /**
     * get a list of slicebox log messages
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void logGetTest() throws ApiException {
        Long startindex = null;
        Long count = null;
        String subject = null;
        String type = null;
        List<LogEntry> response = api.logGet(startindex, count, subject, type);
        // TODO: test validations
    }

    /**
     * Delete the log entry with the supplied ID
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void logIdDeleteTest() throws ApiException {
        Long id = null;
        api.logIdDelete(id);
        // TODO: test validations
    }

}
