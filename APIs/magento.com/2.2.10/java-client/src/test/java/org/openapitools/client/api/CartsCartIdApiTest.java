/*
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.ErrorResponse;
import org.openapitools.client.model.QuoteCartManagementV1AssignCustomerPutRequest;
import org.openapitools.client.model.QuoteDataCartInterface;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for CartsCartIdApi
 */
@Disabled
public class CartsCartIdApiTest {

    private final CartsCartIdApi api = new CartsCartIdApi();

    /**
     * carts/{cartId}
     *
     * Assigns a specified customer to a specified shopping cart.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void quoteCartManagementV1AssignCustomerPutTest() throws ApiException {
        Integer cartId = null;
        QuoteCartManagementV1AssignCustomerPutRequest quoteCartManagementV1AssignCustomerPutRequest = null;
        Boolean response = api.quoteCartManagementV1AssignCustomerPut(cartId, quoteCartManagementV1AssignCustomerPutRequest);
        // TODO: test validations
    }

    /**
     * carts/{cartId}
     *
     * Enables an administrative user to return information for a specified cart.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void quoteCartRepositoryV1GetGetTest() throws ApiException {
        Integer cartId = null;
        QuoteDataCartInterface response = api.quoteCartRepositoryV1GetGet(cartId);
        // TODO: test validations
    }

}
