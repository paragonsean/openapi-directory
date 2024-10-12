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
import org.openapitools.client.model.CmsDataBlockSearchResultsInterface;
import org.openapitools.client.model.ErrorResponse;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for CmsBlockSearchApi
 */
@Disabled
public class CmsBlockSearchApiTest {

    private final CmsBlockSearchApi api = new CmsBlockSearchApi();

    /**
     * cmsBlock/search
     *
     * Retrieve blocks matching the specified criteria.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void cmsBlockRepositoryV1GetListGetTest() throws ApiException {
        String searchCriteriaFilterGroups0Filters0Field = null;
        String searchCriteriaFilterGroups0Filters0Value = null;
        String searchCriteriaFilterGroups0Filters0ConditionType = null;
        String searchCriteriaSortOrders0Field = null;
        String searchCriteriaSortOrders0Direction = null;
        Integer searchCriteriaPageSize = null;
        Integer searchCriteriaCurrentPage = null;
        CmsDataBlockSearchResultsInterface response = api.cmsBlockRepositoryV1GetListGet(searchCriteriaFilterGroups0Filters0Field, searchCriteriaFilterGroups0Filters0Value, searchCriteriaFilterGroups0Filters0ConditionType, searchCriteriaSortOrders0Field, searchCriteriaSortOrders0Direction, searchCriteriaPageSize, searchCriteriaCurrentPage);
        // TODO: test validations
    }

}
