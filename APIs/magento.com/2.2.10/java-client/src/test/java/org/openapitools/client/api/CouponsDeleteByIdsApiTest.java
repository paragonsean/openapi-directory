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
import org.openapitools.client.model.SalesRuleCouponManagementV1DeleteByIdsPostRequest;
import org.openapitools.client.model.SalesRuleDataCouponMassDeleteResultInterface;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for CouponsDeleteByIdsApi
 */
@Disabled
public class CouponsDeleteByIdsApiTest {

    private final CouponsDeleteByIdsApi api = new CouponsDeleteByIdsApi();

    /**
     * coupons/deleteByIds
     *
     * Delete coupon by coupon ids.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void salesRuleCouponManagementV1DeleteByIdsPostTest() throws ApiException {
        SalesRuleCouponManagementV1DeleteByIdsPostRequest salesRuleCouponManagementV1DeleteByIdsPostRequest = null;
        SalesRuleDataCouponMassDeleteResultInterface response = api.salesRuleCouponManagementV1DeleteByIdsPost(salesRuleCouponManagementV1DeleteByIdsPostRequest);
        // TODO: test validations
    }

}
