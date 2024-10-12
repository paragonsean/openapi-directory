/*
 * LH Public API
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
 * API tests for OffersApi
 */
@Disabled
public class OffersApiTest {

    private final OffersApi api = new OffersApi();

    /**
     * Lounges
     *
     * Lounge information
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void offersLoungesByLocationGetTest() throws ApiException {
        String location = null;
        String accept = null;
        String cabinClass = null;
        String tierCode = null;
        String lang = null;
        Object response = api.offersLoungesByLocationGet(location, accept, cabinClass, tierCode, lang);
        // TODO: test validations
    }

    /**
     * Seat Maps
     *
     * Cabin layout and seat characteristics.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void offersSeatmapsDestinationDateCabinClassByFlightNumberAndOriginGetTest() throws ApiException {
        String flightNumber = null;
        String origin = null;
        String destination = null;
        String date = null;
        String cabinClass = null;
        String accept = null;
        Object response = api.offersSeatmapsDestinationDateCabinClassByFlightNumberAndOriginGet(flightNumber, origin, destination, date, cabinClass, accept);
        // TODO: test validations
    }

}
