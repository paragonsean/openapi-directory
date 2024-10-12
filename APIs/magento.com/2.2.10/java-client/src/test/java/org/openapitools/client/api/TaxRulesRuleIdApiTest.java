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
import org.openapitools.client.model.TaxDataTaxRuleInterface;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for TaxRulesRuleIdApi
 */
@Disabled
public class TaxRulesRuleIdApiTest {

    private final TaxRulesRuleIdApi api = new TaxRulesRuleIdApi();

    /**
     * taxRules/{ruleId}
     *
     * Delete TaxRule
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void taxTaxRuleRepositoryV1DeleteByIdDeleteTest() throws ApiException {
        Integer ruleId = null;
        Boolean response = api.taxTaxRuleRepositoryV1DeleteByIdDelete(ruleId);
        // TODO: test validations
    }

    /**
     * taxRules/{ruleId}
     *
     * Get TaxRule
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void taxTaxRuleRepositoryV1GetGetTest() throws ApiException {
        Integer ruleId = null;
        TaxDataTaxRuleInterface response = api.taxTaxRuleRepositoryV1GetGet(ruleId);
        // TODO: test validations
    }

}
