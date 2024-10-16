/*
 * Visual Crossing Weather API
 * Weather Forecast and Historical Weather Data via RESTful API.
 *
 * The version of the OpenAPI document: 4.6
 * Contact: info@visualcrossing.com
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
 * API tests for TimelineWeatherApi15DayForecastRequestApi
 */
@Disabled
public class TimelineWeatherApi15DayForecastRequestApiTest {

    private final TimelineWeatherApi15DayForecastRequestApi api = new TimelineWeatherApi15DayForecastRequestApi();

    /**
     * Historical and Forecast Weather API
     *
     * Seamless access to daily and hourly historical and forecast weather data plus weather alerts, events and current conditions.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void visualCrossingWebServicesRestServicesTimelineLocationGetTest() throws ApiException {
        String location = null;
        String key = null;
        String contentType = null;
        String unitGroup = null;
        String include = null;
        String lang = null;
        api.visualCrossingWebServicesRestServicesTimelineLocationGet(location, key, contentType, unitGroup, include, lang);
        // TODO: test validations
    }

}
