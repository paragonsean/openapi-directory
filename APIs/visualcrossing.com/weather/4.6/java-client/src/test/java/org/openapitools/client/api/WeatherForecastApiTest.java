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
 * API tests for WeatherForecastApi
 */
@Disabled
public class WeatherForecastApiTest {

    private final WeatherForecastApi api = new WeatherForecastApi();

    /**
     * Weather Forecast API
     *
     * Provides access to weather forecast information. The forecast is available for up to 15 days at the hourly, 12 hour and daily summary level.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void visualCrossingWebServicesRestServicesWeatherdataForecastGetTest() throws ApiException {
        Boolean sendAsDatasource = null;
        Boolean allowAsynch = null;
        Boolean shortColumnNames = null;
        String locations = null;
        String aggregateHours = null;
        String contentType = null;
        String unitGroup = null;
        String key = null;
        api.visualCrossingWebServicesRestServicesWeatherdataForecastGet(sendAsDatasource, allowAsynch, shortColumnNames, locations, aggregateHours, contentType, unitGroup, key);
        // TODO: test validations
    }

}
