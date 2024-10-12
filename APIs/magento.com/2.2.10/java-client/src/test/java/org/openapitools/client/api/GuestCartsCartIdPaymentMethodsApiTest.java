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
import org.openapitools.client.model.QuoteDataPaymentMethodInterface;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for GuestCartsCartIdPaymentMethodsApi
 */
@Disabled
public class GuestCartsCartIdPaymentMethodsApiTest {

    private final GuestCartsCartIdPaymentMethodsApi api = new GuestCartsCartIdPaymentMethodsApi();

    /**
     * guest-carts/{cartId}/payment-methods
     *
     * List available payment methods for a specified shopping cart. This call returns an array of objects, but detailed information about each object’s attributes might not be included.  See https://devdocs.magento.com/codelinks/attributes.html#GuestPaymentMethodManagementInterface to determine which call to use to get detailed information about all attributes for an object.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void quoteGuestPaymentMethodManagementV1GetListGetTest() throws ApiException {
        String cartId = null;
        List<QuoteDataPaymentMethodInterface> response = api.quoteGuestPaymentMethodManagementV1GetListGet(cartId);
        // TODO: test validations
    }

}
