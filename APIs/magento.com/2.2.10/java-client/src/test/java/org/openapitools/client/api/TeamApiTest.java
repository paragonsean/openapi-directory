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
import org.openapitools.client.model.CompanyDataTeamSearchResultsInterface;
import org.openapitools.client.model.ErrorResponse;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for TeamApi
 */
@Disabled
public class TeamApiTest {

    private final TeamApi api = new TeamApi();

    /**
     * team/
     *
     * Returns the list of teams for the specified search criteria (team name or description).
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void companyTeamRepositoryV1GetListGetTest() throws ApiException {
        String searchCriteriaFilterGroups0Filters0Field = null;
        String searchCriteriaFilterGroups0Filters0Value = null;
        String searchCriteriaFilterGroups0Filters0ConditionType = null;
        String searchCriteriaSortOrders0Field = null;
        String searchCriteriaSortOrders0Direction = null;
        Integer searchCriteriaPageSize = null;
        Integer searchCriteriaCurrentPage = null;
        CompanyDataTeamSearchResultsInterface response = api.companyTeamRepositoryV1GetListGet(searchCriteriaFilterGroups0Filters0Field, searchCriteriaFilterGroups0Filters0Value, searchCriteriaFilterGroups0Filters0ConditionType, searchCriteriaSortOrders0Field, searchCriteriaSortOrders0Direction, searchCriteriaPageSize, searchCriteriaCurrentPage);
        // TODO: test validations
    }

}
