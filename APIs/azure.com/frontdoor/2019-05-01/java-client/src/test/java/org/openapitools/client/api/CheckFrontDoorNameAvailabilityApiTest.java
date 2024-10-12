/*
 * FrontDoorManagementClient
 * Use these APIs to manage Azure Front Door resources through the Azure Resource Manager. You must make sure that requests made to these resources are secure.
 *
 * The version of the OpenAPI document: 2019-05-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.CheckNameAvailabilityInput;
import org.openapitools.client.model.CheckNameAvailabilityOutput;
import org.openapitools.client.model.ErrorResponse;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for CheckFrontDoorNameAvailabilityApi
 */
@Disabled
public class CheckFrontDoorNameAvailabilityApiTest {

    private final CheckFrontDoorNameAvailabilityApi api = new CheckFrontDoorNameAvailabilityApi();

    /**
     * Check the availability of a Front Door resource name.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void checkFrontDoorNameAvailabilityTest() throws ApiException {
        String apiVersion = null;
        CheckNameAvailabilityInput checkFrontDoorNameAvailabilityInput = null;
        CheckNameAvailabilityOutput response = api.checkFrontDoorNameAvailability(apiVersion, checkFrontDoorNameAvailabilityInput);
        // TODO: test validations
    }

}
