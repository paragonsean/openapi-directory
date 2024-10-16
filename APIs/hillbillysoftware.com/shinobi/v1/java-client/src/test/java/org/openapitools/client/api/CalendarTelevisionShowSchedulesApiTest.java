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
import org.openapitools.client.model.Country;
import org.openapitools.client.model.Networks;
import org.openapitools.client.model.Schedule;
import org.openapitools.client.model.ShowSeasons;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for CalendarTelevisionShowSchedulesApi
 */
@Disabled
public class CalendarTelevisionShowSchedulesApiTest {

    private final CalendarTelevisionShowSchedulesApi api = new CalendarTelevisionShowSchedulesApi();

    /**
     * Will return show schedule for queried showname and year
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void calendarByShowNameGetTest() throws ApiException {
        String accessToken = null;
        String name = null;
        String year = null;
        List<Schedule> response = api.calendarByShowNameGet(accessToken, name, year);
        // TODO: test validations
    }

    /**
     * Returns list of available countries in calendar database
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void calendarCountriesGetTest() throws ApiException {
        String accessToken = null;
        List<Country> response = api.calendarCountriesGet(accessToken);
        // TODO: test validations
    }

    /**
     * Gets a list of available networks
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void calendarNetworksGetTest() throws ApiException {
        String accessToken = null;
        List<Networks> response = api.calendarNetworksGet(accessToken);
        // TODO: test validations
    }

    /**
     * Returns list of seasons available in the calendar for show
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void calendarShowSeasonsGetTest() throws ApiException {
        String accessToken = null;
        String name = null;
        List<ShowSeasons> response = api.calendarShowSeasonsGet(accessToken, name);
        // TODO: test validations
    }

    /**
     * Will return show schedule for today for all countries in database
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void calendarTodayGetTest() throws ApiException {
        String accessToken = null;
        List<Schedule> response = api.calendarTodayGet(accessToken);
        // TODO: test validations
    }

    /**
     * Get Calendar by showname and season
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void calendarbyShownameSeasonGetTest() throws ApiException {
        String accessToken = null;
        String name = null;
        String season = null;
        List<Schedule> response = api.calendarbyShownameSeasonGet(accessToken, name, season);
        // TODO: test validations
    }

    /**
     * Gets TV Schedule for selected data
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void scheduleByDateGetTest() throws ApiException {
        String accessToken = null;
        String date = null;
        String country = null;
        List<Schedule> response = api.scheduleByDateGet(accessToken, date, country);
        // TODO: test validations
    }

}
