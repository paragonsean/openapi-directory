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
import org.openapitools.client.model.BundleDataLinkInterface;
import org.openapitools.client.model.ErrorResponse;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for BundleProductsProductSkuChildrenApi
 */
@Disabled
public class BundleProductsProductSkuChildrenApiTest {

    private final BundleProductsProductSkuChildrenApi api = new BundleProductsProductSkuChildrenApi();

    /**
     * bundle-products/{productSku}/children
     *
     * Get all children for Bundle product
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void bundleProductLinkManagementV1GetChildrenGetTest() throws ApiException {
        String productSku = null;
        Integer optionId = null;
        List<BundleDataLinkInterface> response = api.bundleProductLinkManagementV1GetChildrenGet(productSku, optionId);
        // TODO: test validations
    }

}
