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
import org.openapitools.client.model.AirportResponse;
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
     * Aircraft
     *
     * List all aircraft types or one specific aircraft type.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void referencesAircraftByAircraftCodeGetTest() throws ApiException {
        String accept = null;
        String aircraftCode = null;
        String limit = null;
        String offset = null;
        Object response = api.referencesAircraftByAircraftCodeGet(accept, aircraftCode, limit, offset);
        // TODO: test validations
    }

    /**
     * Airlines
     *
     * List all airlines or one specific airline.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void referencesAirlinesByAirlineCodeGetTest() throws ApiException {
        String accept = null;
        String airlineCode = null;
        String limit = null;
        String offset = null;
        Object response = api.referencesAirlinesByAirlineCodeGet(accept, airlineCode, limit, offset);
        // TODO: test validations
    }

    /**
     * Airports
     *
     * List all airports or one specific airport. All airports response is very large. It is possible to request the response in a specific language.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void referencesAirportsByAirportCodeGetTest() throws ApiException {
        String accept = null;
        String airportCode = null;
        String lang = null;
        String limit = null;
        String offset = null;
        Boolean lhoperated = null;
        AirportResponse response = api.referencesAirportsByAirportCodeGet(accept, airportCode, lang, limit, offset, lhoperated);
        // TODO: test validations
    }

    /**
     * Nearest Airports
     *
     * List the 5 closest airports to the given latitude and longitude, irrespective of the radius of the reference point.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void referencesAirportsNearestByLatitudeAndLongitudeGetTest() throws ApiException {
        Integer latitude = null;
        Integer longitude = null;
        String accept = null;
        String lang = null;
        Object response = api.referencesAirportsNearestByLatitudeAndLongitudeGet(latitude, longitude, accept, lang);
        // TODO: test validations
    }

    /**
     * Cities
     *
     * List all cities or one specific city. It is possible to request the response in a specific language.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void referencesCitiesByCityCodeGetTest() throws ApiException {
        String accept = null;
        String cityCode = null;
        String lang = null;
        String limit = null;
        String offset = null;
        Object response = api.referencesCitiesByCityCodeGet(accept, cityCode, lang, limit, offset);
        // TODO: test validations
    }

    /**
     * Countries
     *
     * List all countries or one specific country. It is possible to request the response in a specific language.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void referencesCountriesByCountryCodeGetTest() throws ApiException {
        String accept = null;
        String countryCode = null;
        String lang = null;
        String limit = null;
        String offset = null;
        Object response = api.referencesCountriesByCountryCodeGet(accept, countryCode, lang, limit, offset);
        // TODO: test validations
    }

}
