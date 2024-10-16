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
import org.openapitools.client.model.DefinedBenefitPensionModel;
import org.openapitools.client.model.DefinedBenefitPensionsModel;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for DefinedBenefitPensionsApi
 */
@Disabled
public class DefinedBenefitPensionsApiTest {

    private final DefinedBenefitPensionsApi api = new DefinedBenefitPensionsApi();

    /**
     * Retrieve a definedBenefitPension
     *
     * This operation retrieves a defined benefit pension from the plan.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void definedBenefitPensionsGetByIdPlanidTest() throws ApiException {
        Integer id = null;
        String planId = null;
        DefinedBenefitPensionModel response = api.definedBenefitPensionsGetByIdPlanid(id, planId);
        // TODO: test validations
    }

    /**
     * Retrieve defined benefit pensions
     *
     * This operation retrieves a list of all of the defined benefit pensions in the plan.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void definedBenefitPensionsGetByPlanidTest() throws ApiException {
        String planId = null;
        DefinedBenefitPensionsModel response = api.definedBenefitPensionsGetByPlanid(planId);
        // TODO: test validations
    }

}
