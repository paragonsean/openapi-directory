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
import org.openapitools.client.model.GiftRegistryShippingMethodManagementV1EstimateByRegistryIdPostRequest;
import org.openapitools.client.model.QuoteDataShippingMethodInterface;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for GiftregistryMineEstimateShippingMethodsApi
 */
@Disabled
public class GiftregistryMineEstimateShippingMethodsApiTest {

    private final GiftregistryMineEstimateShippingMethodsApi api = new GiftregistryMineEstimateShippingMethodsApi();

    /**
     * giftregistry/mine/estimate-shipping-methods
     *
     * Estimate shipping
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void giftRegistryShippingMethodManagementV1EstimateByRegistryIdPostTest() throws ApiException {
        GiftRegistryShippingMethodManagementV1EstimateByRegistryIdPostRequest giftRegistryShippingMethodManagementV1EstimateByRegistryIdPostRequest = null;
        List<QuoteDataShippingMethodInterface> response = api.giftRegistryShippingMethodManagementV1EstimateByRegistryIdPost(giftRegistryShippingMethodManagementV1EstimateByRegistryIdPostRequest);
        // TODO: test validations
    }

}
