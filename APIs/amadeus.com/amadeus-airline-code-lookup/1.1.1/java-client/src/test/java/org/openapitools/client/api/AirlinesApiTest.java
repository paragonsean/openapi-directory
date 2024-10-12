/*
 * Airline Code Lookup API
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, to see what is included in test please refer to our **[data collection](https://github.com/amadeus4dev/data-collection)**.
 *
 * The version of the OpenAPI document: 1.1.1
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
import org.openapitools.client.model.SuccessThings;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for AirlinesApi
 */
@Disabled
public class AirlinesApiTest {

    private final AirlinesApi api = new AirlinesApi();

    /**
     * Return airlines information.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getairlinesTest() throws ApiException {
        String airlineCodes = null;
        SuccessThings response = api.getairlines(airlineCodes);
        // TODO: test validations
    }

}
