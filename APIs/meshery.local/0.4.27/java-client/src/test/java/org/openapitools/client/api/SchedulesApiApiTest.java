/*
 * Meshery API.
 * the purpose of this application is to provide an application that is using plain go code to define an API  This should demonstrate all the possible comment annotations that are available to turn go code into a fully compliant swagger 2.0 spec
 *
 * The version of the OpenAPI document: 0.4.27
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.Schedule;
import org.openapitools.client.model.SchedulesAPIResponse;
import java.util.UUID;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for SchedulesApiApi
 */
@Disabled
public class SchedulesApiApiTest {

    private final SchedulesApiApi api = new SchedulesApiApi();

    /**
     * Handle DELETE reqeuest for Schedules
     *
     * Deletes a schedule with the given id
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void idDeleteSchedulesTest() throws ApiException {
        UUID id = null;
        SchedulesAPIResponse response = api.idDeleteSchedules(id);
        // TODO: test validations
    }

    /**
     * Handle GET reqeuest for Schedules
     *
     * Returns the list of all the schedules saved by the current user
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void idGetSchedulesTest() throws ApiException {
        SchedulesAPIResponse response = api.idGetSchedules();
        // TODO: test validations
    }

    /**
     * Handle GET reqeuest for Schedules
     *
     * Fetches and returns the schedule with the given id
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void idGetSingleScheduleTest() throws ApiException {
        UUID id = null;
        Schedule response = api.idGetSingleSchedule(id);
        // TODO: test validations
    }

    /**
     * Handle POST reqeuest for Schedules
     *
     * Save schedule using the current provider&#39;s persistence mechanism
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void idPostSchedulesTest() throws ApiException {
        Schedule response = api.idPostSchedules();
        // TODO: test validations
    }

}
