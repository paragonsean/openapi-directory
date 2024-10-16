/*
 * shinobiapi
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
import org.openapitools.client.model.Awards;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for AwardsTelevisionMoviesApi
 */
@Disabled
public class AwardsTelevisionMoviesApiTest {

    private final AwardsTelevisionMoviesApi api = new AwardsTelevisionMoviesApi();

    /**
     * Gets all awards for requested year
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void awardsGetTest() throws ApiException {
        String year = null;
        List<Awards> response = api.awardsGet(year);
        // TODO: test validations
    }

    /**
     * Gets all awards by nominiee
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void awardsbyWinnerGetTest() throws ApiException {
        String accessToken = null;
        String nominee = null;
        List<Awards> response = api.awardsbyWinnerGet(accessToken, nominee);
        // TODO: test validations
    }

}
