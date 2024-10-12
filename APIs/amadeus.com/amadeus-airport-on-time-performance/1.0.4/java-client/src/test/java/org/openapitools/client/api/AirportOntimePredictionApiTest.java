/*
 * Airport On-Time Performance
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.
 *
 * The version of the OpenAPI document: 1.0.4
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.Error400;
import org.openapitools.client.model.Error500;
import java.time.LocalDate;
import org.openapitools.client.model.Prediction;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for AirportOntimePredictionApi
 */
@Disabled
public class AirportOntimePredictionApiTest {

    private final AirportOntimePredictionApi api = new AirportOntimePredictionApi();

    /**
     * Returns a percentage of on-time flight departures from a given airport.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getAirportOnTimePredictionTest() throws ApiException {
        String airportCode = null;
        LocalDate date = null;
        Prediction response = api.getAirportOnTimePrediction(airportCode, date);
        // TODO: test validations
    }

}
