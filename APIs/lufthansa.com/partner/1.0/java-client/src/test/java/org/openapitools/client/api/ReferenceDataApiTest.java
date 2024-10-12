/*
 * LH Partner API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for ReferenceDataApi
 */
@Disabled
public class ReferenceDataApiTest {

    private final ReferenceDataApi api = new ReferenceDataApi();

    /**
     * Seat Details
     *
     * A description of all available seat details by aircraft type. You can retrieve the full set or details for a particular aircraft type.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void seatDetailsTest() throws ApiException {
        String aircraftCode = null;
        String accept = null;
        String cabinCode = null;
        String lang = null;
        String response = api.seatDetails(aircraftCode, accept, cabinCode, lang);
        // TODO: test validations
    }

}
