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
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for CartsGuestCartsCartIdGiftCardsGiftCardCodeApi
 */
@Disabled
public class CartsGuestCartsCartIdGiftCardsGiftCardCodeApiTest {

    private final CartsGuestCartsCartIdGiftCardsGiftCardCodeApi api = new CartsGuestCartsCartIdGiftCardsGiftCardCodeApi();

    /**
     * carts/guest-carts/{cartId}/giftCards/{giftCardCode}
     *
     * Remove GiftCard Account entity
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void giftCardAccountGuestGiftCardAccountManagementV1DeleteByQuoteIdDeleteTest() throws ApiException {
        String cartId = null;
        String giftCardCode = null;
        Boolean response = api.giftCardAccountGuestGiftCardAccountManagementV1DeleteByQuoteIdDelete(cartId, giftCardCode);
        // TODO: test validations
    }

}
