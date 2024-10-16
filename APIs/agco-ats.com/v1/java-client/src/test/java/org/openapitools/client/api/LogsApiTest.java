/*
 * AGCO API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.APIModelsApiError;
import org.openapitools.client.model.APIModelsLog;
import org.openapitools.client.model.APIPagedResponseAPIModelsLog;
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
     * Get a log by ID
     *
     * No Documentation Found.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void logsGetLogTest() throws ApiException {
        String ID = null;
        APIModelsLog response = api.logsGetLog(ID);
        // TODO: test validations
    }

    /**
     * Get the API System logs, most recent first.
     *
     * No Documentation Found.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void logsGetLogsTest() throws ApiException {
        Integer limit = null;
        Integer offset = null;
        APIPagedResponseAPIModelsLog response = api.logsGetLogs(limit, offset);
        // TODO: test validations
    }

    /**
     * Add a Log entry
     *
     * No Documentation Found.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void logsPostLogTest() throws ApiException {
        String message = null;
        String response = api.logsPostLog(message);
        // TODO: test validations
    }

}
