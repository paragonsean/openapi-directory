/*
 * Wowza Streaming Cloud REST API Reference Documentation
 *  # About the REST API  The Wowza Streaming Cloud<sup>TM</sup> REST API (application programming interface) offers complete programmatic control over live streams, transcoders, stream sources, and stream targets. Anything you can do in the Wowza Streaming Cloud UI can also be achieved by making HTTP-based requests to cloud-based servers through the REST API.  The Wowza Streaming Cloud REST API features *cross-origin resource sharing*, or CORS. CORS is a [W3C specification](https://www.w3.org/TR/cors/) that provides headers in HTTP requests to enable a web server to safely make a network request to another domain.  In order to protect shared resources, the Wowza Streaming Cloud REST API is subject to limits. For details, see [Wowza Streaming Cloud REST API limits](https://www.wowza.com/docs/wowza-streaming-cloud-rest-api-limits). # About this documentation This reference documentation is based on the open-source [Swagger framework](http://swagger.io/specification/). It allows you to view the operations, parameters, and request and reponse schemas for every resource. Request samples are presented in cURL (Shell) and JavaScript; some samples also include just the JSON object. Response samples are all JSON.  For more information and examples on using the Wowza Streaming Cloud REST API, see our [library of Wowza Streaming Cloud REST API technical articles](https://www.wowza.com/docs/wowza-streaming-cloud-rest-api).  # Query requirements The Wowza Streaming Cloud REST API uses HTTP requests to retrieve data from cloud-based servers. Requests must contain proper JSON, two authentication keys, and the correct version number in the base path.  ## JSON The Wowza Streaming Cloud REST API uses the [JSON API specification](http://jsonapi.org/format/) to request and return data. This means requests must include the header `Content-Type: application/json` and must include a single resource object in JSON format as primary data.  Responses include HTTP status codes that indicate whether the query was successful. If there was an error, a description explains the problem so that you can fix it and try again.  ## Authentication Requests to the Wowza Streaming Cloud REST API must be authenticated with two keys: an API key and an access key. Each key is a 64-character alphanumeric string that you can find on the **API Access** page in Wowza Streaming Cloud.  Use the `wsc-api-key` and `wsc-access-key` headers to authenticate requests, like this (in cURL):  ```bash curl -H 'wsc-api-key: [64-character-api-key-goes-here]' -H 'wsc-access-key: [64-character-access-key-goes-here]' ```  <!-- ReDoc-Inject: <security-definitions> -->  ## Version The Wowza Streaming Cloud API is currently at version 1.0.0. Use `v1` in your base path in every request, like this path to the live_streams endpoint: ``` https://api.cloud.wowza.com/api/v1/live_streams ``` ## Example query Here is a complete example POST request, in cURL, with proper JSON syntax, headers, authentication, and version information: ```bash curl -H 'wsc-api-key: [64-character-api-key-goes-here]' -H 'wsc-access-key: [64-character-access-key-goes-here]'   -H 'Content-Type: application/json' -X POST -d '{     \"live_stream\": {       \"name\": \"My live Stream\",       \"...\": \"...\"     }   }' https://api.cloud.wowza.com/api/v1/live_streams ``` 
 *
 * The version of the OpenAPI document: 1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.CreateSchedule200Response;
import org.openapitools.client.model.DisableSchedule200Response;
import org.openapitools.client.model.EnableSchedule200Response;
import org.openapitools.client.model.Error401;
import org.openapitools.client.model.Error403;
import org.openapitools.client.model.Error404;
import org.openapitools.client.model.Error410;
import org.openapitools.client.model.Error422;
import org.openapitools.client.model.ScheduleCreateInput;
import org.openapitools.client.model.ScheduleUpdateInput;
import org.openapitools.client.model.Schedules;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for SchedulesApi
 */
@Disabled
public class SchedulesApiTest {

    private final SchedulesApi api = new SchedulesApi();

    /**
     * Create a schedule
     *
     * This operation creates a schedule.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createScheduleTest() throws ApiException {
        ScheduleCreateInput schedule = null;
        CreateSchedule200Response response = api.createSchedule(schedule);
        // TODO: test validations
    }

    /**
     * Delete a schedule
     *
     * This operation deletes a schedule.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteScheduleTest() throws ApiException {
        String id = null;
        api.deleteSchedule(id);
        // TODO: test validations
    }

    /**
     * Disable a schedule
     *
     * This operation disables a schedule.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void disableScheduleTest() throws ApiException {
        String id = null;
        DisableSchedule200Response response = api.disableSchedule(id);
        // TODO: test validations
    }

    /**
     * Enable a schedule
     *
     * This operation enables a schedule.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void enableScheduleTest() throws ApiException {
        String id = null;
        EnableSchedule200Response response = api.enableSchedule(id);
        // TODO: test validations
    }

    /**
     * Fetch all schedules
     *
     * This operation shows the details of all of your schedules.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listSchedulesTest() throws ApiException {
        Integer page = null;
        Integer perPage = null;
        Schedules response = api.listSchedules(page, perPage);
        // TODO: test validations
    }

    /**
     * Fetch a schedule
     *
     * This operation shows the details of a specific schedule.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void showScheduleTest() throws ApiException {
        String id = null;
        CreateSchedule200Response response = api.showSchedule(id);
        // TODO: test validations
    }

    /**
     * Fetch the state of a schedule
     *
     * This operation shows the current state of a schedule.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void showScheduleStateTest() throws ApiException {
        String id = null;
        EnableSchedule200Response response = api.showScheduleState(id);
        // TODO: test validations
    }

    /**
     * Update a schedule
     *
     * This operation updates a schedule.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateScheduleTest() throws ApiException {
        String id = null;
        ScheduleUpdateInput schedule = null;
        CreateSchedule200Response response = api.updateSchedule(id, schedule);
        // TODO: test validations
    }

}
