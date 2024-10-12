/*
 * Reisezentren-API
 * This REST-API enables you to query information about travel centers in Germany.
 *
 * The version of the OpenAPI document: v1
 * Contact: Joachim.Schirrmacher@deutschebahn.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.Error;
import org.openapitools.client.model.TravelCenter;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for DefaultApi
 */
@Disabled
public class DefaultApiTest {

    private final DefaultApi api = new DefaultApi();

    /**
     * Get all station infos
     *
     * Get all station infos
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void reisezentrenGetTest() throws ApiException {
        String name = null;
        List<TravelCenter> response = api.reisezentrenGet(name);
        // TODO: test validations
    }

    /**
     * Get information about a specific station
     *
     * Get information about a specific station
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void reisezentrenIdGetTest() throws ApiException {
        String id = null;
        TravelCenter response = api.reisezentrenIdGet(id);
        // TODO: test validations
    }

    /**
     * Get stations in a given radius
     *
     * Get stations in a given radius
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void reisezentrenLocLatLonDistGetTest() throws ApiException {
        Float lat = null;
        Float lon = null;
        Float dist = null;
        TravelCenter response = api.reisezentrenLocLatLonDistGet(lat, lon, dist);
        // TODO: test validations
    }

    /**
     * Get information about a station near a location
     *
     * Get information about a station near a location
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void reisezentrenLocLatLonGetTest() throws ApiException {
        Float lat = null;
        Float lon = null;
        TravelCenter response = api.reisezentrenLocLatLonGet(lat, lon);
        // TODO: test validations
    }

}
