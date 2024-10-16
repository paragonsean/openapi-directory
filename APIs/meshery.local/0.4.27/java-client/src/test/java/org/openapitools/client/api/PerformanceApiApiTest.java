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
import org.openapitools.client.model.PerformanceProfile;
import org.openapitools.client.model.PerformanceProfileParameters;
import org.openapitools.client.model.PerformanceProfilesAPIResponse;
import org.openapitools.client.model.PerformanceResultsAPIResponse;
import java.util.UUID;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for PerformanceApiApi
 */
@Disabled
public class PerformanceApiApiTest {

    private final PerformanceApiApi api = new PerformanceApiApi();

    /**
     * Handle Delete requests for performance profiles
     *
     * Deletes a performance profile with the given id
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void idDeletePerformanceProfileTest() throws ApiException {
        UUID id = null;
        api.idDeletePerformanceProfile(id);
        // TODO: test validations
    }

    /**
     * Handle GET request for results of a profile
     *
     * Fetchs pages of results from Remote Provider for the given id
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void idGETProfileResultsTest() throws ApiException {
        UUID id = null;
        PerformanceResultsAPIResponse response = api.idGETProfileResults(id);
        // TODO: test validations
    }

    /**
     * Handles GET requests for performance results
     *
     * Returns pages of all the performance results from Remote Provider
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void idGetAllPerformanceResultsTest() throws ApiException {
        PerformanceResultsAPIResponse response = api.idGetAllPerformanceResults();
        // TODO: test validations
    }

    /**
     * Handle GET requests for performance profiles
     *
     * Returns the list of all the performance profiles saved by the current user
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void idGetPerformanceProfilesTest() throws ApiException {
        PerformanceProfilesAPIResponse response = api.idGetPerformanceProfiles();
        // TODO: test validations
    }

    /**
     * Handle GET requests for performance results of a profile
     *
     * Returns single performance profile with the given id
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void idGetSinglePerformanceProfileTest() throws ApiException {
        UUID id = null;
        PerformanceProfile response = api.idGetSinglePerformanceProfile(id);
        // TODO: test validations
    }

    /**
     * Handle GET request to run a performance test
     *
     * Runs the load test with the given parameters
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void idRunPerformanceTestTest() throws ApiException {
        String id = null;
        api.idRunPerformanceTest(id);
        // TODO: test validations
    }

    /**
     * Handle POST requests for saving performance profile
     *
     * Save performance profile using the current provider&#39;s persistence mechanism
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void idSavePerformanceProfileTest() throws ApiException {
        PerformanceProfileParameters performanceProfileParameters = null;
        PerformanceProfile response = api.idSavePerformanceProfile(performanceProfileParameters);
        // TODO: test validations
    }

}
