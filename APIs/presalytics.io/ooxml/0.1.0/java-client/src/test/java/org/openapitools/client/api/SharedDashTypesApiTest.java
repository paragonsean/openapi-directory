/*
 * OOXML Automation
 * This API helps users convert Excel and Powerpoint documents into rich, live dashboards and stories.
 *
 * The version of the OpenAPI document: 0.1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.ProblemDetails;
import org.openapitools.client.model.SharedDashTypes;
import java.util.UUID;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for SharedDashTypesApi
 */
@Disabled
public class SharedDashTypesApiTest {

    private final SharedDashTypesApi api = new SharedDashTypesApi();

    /**
     * DashTypes: List All Possible Types
     *
     * List Types: Use this method to retreive a list of possible options for the DashTypes type. Use the Id from oneof the returned elements on to make changes to elements in the Shared object space.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void sharedDashtypesGetTest() throws ApiException {
        List<SharedDashTypes> response = api.sharedDashtypesGet();
        // TODO: test validations
    }

    /**
     * DashTypes: Get by Id
     *
     * Get by Id: Use this method to retrieve a DashTypes object by its primary key (id)
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void sharedDashtypesGetIdTest() throws ApiException {
        UUID id = null;
        SharedDashTypes response = api.sharedDashtypesGetId(id);
        // TODO: test validations
    }

    /**
     * DashTypes: Get By Type Id
     *
     * This endpoint returns Type metadata from an integer type_id that can found on objects throughout the api.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void sharedDashtypesTypeidGetTypeIdTest() throws ApiException {
        Integer typeId = null;
        SharedDashTypes response = api.sharedDashtypesTypeidGetTypeId(typeId);
        // TODO: test validations
    }

}
