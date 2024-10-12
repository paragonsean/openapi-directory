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
import org.openapitools.client.model.SalesRuleCouponManagementV1GeneratePostRequest;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for CouponsGenerateApi
 */
@Disabled
public class CouponsGenerateApiTest {

    private final CouponsGenerateApi api = new CouponsGenerateApi();

    /**
     * coupons/generate
     *
     * Generate coupon for a rule
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void salesRuleCouponManagementV1GeneratePostTest() throws ApiException {
        SalesRuleCouponManagementV1GeneratePostRequest salesRuleCouponManagementV1GeneratePostRequest = null;
        List<String> response = api.salesRuleCouponManagementV1GeneratePost(salesRuleCouponManagementV1GeneratePostRequest);
        // TODO: test validations
    }

}
