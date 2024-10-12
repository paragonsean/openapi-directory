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
import org.openapitools.client.model.QuoteCartManagementV1PlaceOrderPutRequest;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for CartsCartIdOrderApi
 */
@Disabled
public class CartsCartIdOrderApiTest {

    private final CartsCartIdOrderApi api = new CartsCartIdOrderApi();

    /**
     * carts/{cartId}/order
     *
     * Places an order for a specified cart.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void v1CartsCartIdOrderPutTest() throws ApiException {
        Integer cartId = null;
        QuoteCartManagementV1PlaceOrderPutRequest quoteCartManagementV1PlaceOrderPutRequest = null;
        Integer response = api.v1CartsCartIdOrderPut(cartId, quoteCartManagementV1PlaceOrderPutRequest);
        // TODO: test validations
    }

}
