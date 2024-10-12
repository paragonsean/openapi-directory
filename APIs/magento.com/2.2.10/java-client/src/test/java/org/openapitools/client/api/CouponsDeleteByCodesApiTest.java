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
import org.openapitools.client.model.SalesRuleCouponManagementV1DeleteByCodesPostRequest;
import org.openapitools.client.model.SalesRuleDataCouponMassDeleteResultInterface;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for CouponsDeleteByCodesApi
 */
@Disabled
public class CouponsDeleteByCodesApiTest {

    private final CouponsDeleteByCodesApi api = new CouponsDeleteByCodesApi();

    /**
     * coupons/deleteByCodes
     *
     * Delete coupon by coupon codes.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void salesRuleCouponManagementV1DeleteByCodesPostTest() throws ApiException {
        SalesRuleCouponManagementV1DeleteByCodesPostRequest salesRuleCouponManagementV1DeleteByCodesPostRequest = null;
        SalesRuleDataCouponMassDeleteResultInterface response = api.salesRuleCouponManagementV1DeleteByCodesPost(salesRuleCouponManagementV1DeleteByCodesPostRequest);
        // TODO: test validations
    }

}
