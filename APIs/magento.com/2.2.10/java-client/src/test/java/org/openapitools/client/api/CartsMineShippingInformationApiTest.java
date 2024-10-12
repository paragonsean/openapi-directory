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
import org.openapitools.client.model.CheckoutDataPaymentDetailsInterface;
import org.openapitools.client.model.CheckoutShippingInformationManagementV1SaveAddressInformationPostRequest;
import org.openapitools.client.model.ErrorResponse;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for CartsMineShippingInformationApi
 */
@Disabled
public class CartsMineShippingInformationApiTest {

    private final CartsMineShippingInformationApi api = new CartsMineShippingInformationApi();

    /**
     * carts/mine/shipping-information
     *
     * 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void checkoutShippingInformationManagementV1SaveAddressInformationPostTest() throws ApiException {
        CheckoutShippingInformationManagementV1SaveAddressInformationPostRequest checkoutShippingInformationManagementV1SaveAddressInformationPostRequest = null;
        CheckoutDataPaymentDetailsInterface response = api.checkoutShippingInformationManagementV1SaveAddressInformationPost(checkoutShippingInformationManagementV1SaveAddressInformationPostRequest);
        // TODO: test validations
    }

}
