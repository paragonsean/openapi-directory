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
import org.openapitools.client.model.TaxDataTaxRateSearchResultsInterface;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for TaxRatesSearchApi
 */
@Disabled
public class TaxRatesSearchApiTest {

    private final TaxRatesSearchApi api = new TaxRatesSearchApi();

    /**
     * taxRates/search
     *
     * Search TaxRates This call returns an array of objects, but detailed information about each object’s attributes might not be included. See https://devdocs.magento.com/codelinks/attributes.html#TaxRateRepositoryInterface to determine which call to use to get detailed information about all attributes for an object.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void taxTaxRateRepositoryV1GetListGetTest() throws ApiException {
        String searchCriteriaFilterGroups0Filters0Field = null;
        String searchCriteriaFilterGroups0Filters0Value = null;
        String searchCriteriaFilterGroups0Filters0ConditionType = null;
        String searchCriteriaSortOrders0Field = null;
        String searchCriteriaSortOrders0Direction = null;
        Integer searchCriteriaPageSize = null;
        Integer searchCriteriaCurrentPage = null;
        TaxDataTaxRateSearchResultsInterface response = api.taxTaxRateRepositoryV1GetListGet(searchCriteriaFilterGroups0Filters0Field, searchCriteriaFilterGroups0Filters0Value, searchCriteriaFilterGroups0Filters0ConditionType, searchCriteriaSortOrders0Field, searchCriteriaSortOrders0Direction, searchCriteriaPageSize, searchCriteriaCurrentPage);
        // TODO: test validations
    }

}
