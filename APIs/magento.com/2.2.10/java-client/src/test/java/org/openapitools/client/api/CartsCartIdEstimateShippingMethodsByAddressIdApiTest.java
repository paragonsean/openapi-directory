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
import org.openapitools.client.model.QuoteDataShippingMethodInterface;
import org.openapitools.client.model.QuoteShippingMethodManagementV1EstimateByAddressIdPostRequest;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for CartsCartIdEstimateShippingMethodsByAddressIdApi
 */
@Disabled
public class CartsCartIdEstimateShippingMethodsByAddressIdApiTest {

    private final CartsCartIdEstimateShippingMethodsByAddressIdApi api = new CartsCartIdEstimateShippingMethodsByAddressIdApi();

    /**
     * carts/{cartId}/estimate-shipping-methods-by-address-id
     *
     * Estimate shipping
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void v1CartsCartIdEstimateShippingMethodsByAddressIdPostTest() throws ApiException {
        Integer cartId = null;
        QuoteShippingMethodManagementV1EstimateByAddressIdPostRequest quoteShippingMethodManagementV1EstimateByAddressIdPostRequest = null;
        List<QuoteDataShippingMethodInterface> response = api.v1CartsCartIdEstimateShippingMethodsByAddressIdPost(cartId, quoteShippingMethodManagementV1EstimateByAddressIdPostRequest);
        // TODO: test validations
    }

}
