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
import org.openapitools.client.model.BundleProductOptionManagementV1SavePostRequest;
import org.openapitools.client.model.ErrorResponse;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for BundleProductsOptionsAddApi
 */
@Disabled
public class BundleProductsOptionsAddApiTest {

    private final BundleProductsOptionsAddApi api = new BundleProductsOptionsAddApi();

    /**
     * bundle-products/options/add
     *
     * Add new option for bundle product
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void bundleProductOptionManagementV1SavePostTest() throws ApiException {
        BundleProductOptionManagementV1SavePostRequest bundleProductOptionManagementV1SavePostRequest = null;
        Integer response = api.bundleProductOptionManagementV1SavePost(bundleProductOptionManagementV1SavePostRequest);
        // TODO: test validations
    }

}
