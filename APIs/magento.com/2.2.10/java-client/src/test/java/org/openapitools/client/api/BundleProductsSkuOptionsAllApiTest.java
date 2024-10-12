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
import org.openapitools.client.model.BundleDataOptionInterface;
import org.openapitools.client.model.ErrorResponse;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for BundleProductsSkuOptionsAllApi
 */
@Disabled
public class BundleProductsSkuOptionsAllApiTest {

    private final BundleProductsSkuOptionsAllApi api = new BundleProductsSkuOptionsAllApi();

    /**
     * bundle-products/{sku}/options/all
     *
     * Get all options for bundle product
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void bundleProductOptionRepositoryV1GetListGetTest() throws ApiException {
        String sku = null;
        List<BundleDataOptionInterface> response = api.bundleProductOptionRepositoryV1GetListGet(sku);
        // TODO: test validations
    }

}
