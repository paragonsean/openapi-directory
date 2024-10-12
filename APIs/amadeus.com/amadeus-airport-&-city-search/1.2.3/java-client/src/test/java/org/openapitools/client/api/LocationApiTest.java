/*
 * Airport & City Search
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, in test this API only contains data from the United States, Spain, United Kingdom, Germany and India. 
 *
 * The version of the OpenAPI document: 1.2.3
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.Error400;
import org.openapitools.client.model.Error404;
import org.openapitools.client.model.Error500;
import org.openapitools.client.model.Success;
import org.openapitools.client.model.Success1;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for LocationApi
 */
@Disabled
public class LocationApiTest {

    private final LocationApi api = new LocationApi();

    /**
     * Returns a specific airports or cities based on its id.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getAirportCityTest() throws ApiException {
        String locationId = null;
        Success1 response = api.getAirportCity(locationId);
        // TODO: test validations
    }

    /**
     * Returns a list of airports and cities matching a given keyword.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getAirportCitySearchTest() throws ApiException {
        List<String> subType = null;
        String keyword = null;
        String countryCode = null;
        Integer pageLimit = null;
        Integer pageOffset = null;
        String sort = null;
        String view = null;
        Success response = api.getAirportCitySearch(subType, keyword, countryCode, pageLimit, pageOffset, sort, view);
        // TODO: test validations
    }

}
