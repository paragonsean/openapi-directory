/*
 * Advicent.FactFinderService
 * An API for accessing the NaviPlan Fact Finder.
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
import org.openapitools.client.model.AccountTypeModel;
import org.openapitools.client.model.AccountTypesModel;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for AccountTypesApi
 */
@Disabled
public class AccountTypesApiTest {

    private final AccountTypesApi api = new AccountTypesApi();

    /**
     * Description: This operation retrieves all Account Types for the specified country.&lt;br /&gt;                Purpose: Provides access to the Account Types including id and type description.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void accountTypesGetByCountryTest() throws ApiException {
        String country = null;
        AccountTypesModel response = api.accountTypesGetByCountry(country);
        // TODO: test validations
    }

    /**
     * Description: This operation retrieves all Account Types for the specified id.&lt;br /&gt;                Purpose: Provides access to the Account Types including id and type description.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void accountTypesGetByIdTest() throws ApiException {
        Integer id = null;
        AccountTypeModel response = api.accountTypesGetById(id);
        // TODO: test validations
    }

}
