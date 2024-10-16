/*
 * NaviPlan API
 * An API for accessing NaviPlan plan data for a client.
 *
 * The version of the OpenAPI document: v1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.ProjectedAnnualSummariesModel;
import org.openapitools.client.model.ProjectedAnnualSummaryModel;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for ProjectedAnnualSummaryApi
 */
@Disabled
public class ProjectedAnnualSummaryApiTest {

    private final ProjectedAnnualSummaryApi api = new ProjectedAnnualSummaryApi();

    /**
     * Retrieve projected annual summary by id
     *
     * This operation retrieves an object containing annual summary information                 for a single specified year of the projected plan.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void projectedAnnualSummaryGetByIdPlanidTest() throws ApiException {
        Integer id = null;
        String planId = null;
        ProjectedAnnualSummaryModel response = api.projectedAnnualSummaryGetByIdPlanid(id, planId);
        // TODO: test validations
    }

    /**
     * Retrieve projected annual summaries
     *
     * This operation retrieves an object containing annual summary information                 for each year of the projected plan.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void projectedAnnualSummaryGetByPlanidTest() throws ApiException {
        String planId = null;
        ProjectedAnnualSummariesModel response = api.projectedAnnualSummaryGetByPlanid(planId);
        // TODO: test validations
    }

}
