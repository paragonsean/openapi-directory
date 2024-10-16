/*
 * Cenit IO - REST API Specification
 * Cenit IO is an Open Platform for Data and Business Integration (iPaaS) 
 *
 * The version of the OpenAPI document: v1
 * Contact: support@cenit.io
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.Scheduler;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for SchedulerApi
 */
@Disabled
public class SchedulerApiTest {

    private final SchedulerApi api = new SchedulerApi();

    /**
     * Returns a list of schedulers
     *
     * Returns a list of schedulers you&#39;ve previously created. The schedulers are returned in sorted order, with the most recent scheduler appearing first.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void setupSchedulerGetTest() throws ApiException {
        List<Scheduler> response = api.setupSchedulerGet();
        // TODO: test validations
    }

    /**
     * Delete an schedule
     *
     * Deletes the specified scheduler.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void setupSchedulerIdDeleteTest() throws ApiException {
        String id = null;
        api.setupSchedulerIdDelete(id);
        // TODO: test validations
    }

    /**
     * Retrieve an existing schedule
     *
     * Retrieves the details of an existing scheduler. You need only supply the unique scheduler identifier that was returned upon scheduler creation.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void setupSchedulerIdGetTest() throws ApiException {
        String id = null;
        Scheduler response = api.setupSchedulerIdGet(id);
        // TODO: test validations
    }

    /**
     * Create or update an scheduler
     *
     * Creates or updates the specified scheduler. Any parameters not provided will be left unchanged.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void setupSchedulerPostTest() throws ApiException {
        Scheduler response = api.setupSchedulerPost();
        // TODO: test validations
    }

}
