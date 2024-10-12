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
import org.openapitools.client.model.CompanyCreditCreditLimitRepositoryV1SavePutRequest;
import org.openapitools.client.model.CompanyCreditDataCreditLimitInterface;
import org.openapitools.client.model.ErrorResponse;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for CompanyCreditsIdApi
 */
@Disabled
public class CompanyCreditsIdApiTest {

    private final CompanyCreditsIdApi api = new CompanyCreditsIdApi();

    /**
     * companyCredits/{id}
     *
     * Update the following company credit attributes: credit currency, credit limit and setting to exceed credit.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void companyCreditCreditLimitRepositoryV1SavePutTest() throws ApiException {
        String id = null;
        CompanyCreditCreditLimitRepositoryV1SavePutRequest companyCreditCreditLimitRepositoryV1SavePutRequest = null;
        CompanyCreditDataCreditLimitInterface response = api.companyCreditCreditLimitRepositoryV1SavePut(id, companyCreditCreditLimitRepositoryV1SavePutRequest);
        // TODO: test validations
    }

}
