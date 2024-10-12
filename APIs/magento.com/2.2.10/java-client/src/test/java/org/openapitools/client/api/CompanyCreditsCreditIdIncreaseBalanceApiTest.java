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
import org.openapitools.client.model.CompanyCreditCreditBalanceManagementV1DecreasePostRequest;
import org.openapitools.client.model.ErrorResponse;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for CompanyCreditsCreditIdIncreaseBalanceApi
 */
@Disabled
public class CompanyCreditsCreditIdIncreaseBalanceApiTest {

    private final CompanyCreditsCreditIdIncreaseBalanceApi api = new CompanyCreditsCreditIdIncreaseBalanceApi();

    /**
     * companyCredits/{creditId}/increaseBalance
     *
     * Increases the company credit with an Allocate, Update, Refund, Revert, or Reimburse transaction. This transaction decreases company&#39;s outstanding balance and increases company&#39;s available credit.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void companyCreditCreditBalanceManagementV1IncreasePostTest() throws ApiException {
        Integer creditId = null;
        CompanyCreditCreditBalanceManagementV1DecreasePostRequest companyCreditCreditBalanceManagementV1DecreasePostRequest = null;
        Boolean response = api.companyCreditCreditBalanceManagementV1IncreasePost(creditId, companyCreditCreditBalanceManagementV1DecreasePostRequest);
        // TODO: test validations
    }

}
