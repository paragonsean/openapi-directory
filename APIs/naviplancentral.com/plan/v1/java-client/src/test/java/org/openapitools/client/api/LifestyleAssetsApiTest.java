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
import org.openapitools.client.model.LifestyleAssetModel;
import org.openapitools.client.model.LifestyleAssetsModel;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for LifestyleAssetsApi
 */
@Disabled
public class LifestyleAssetsApiTest {

    private final LifestyleAssetsApi api = new LifestyleAssetsApi();

    /**
     * Retrieve lifestyle assets
     *
     * This operation retrieves a lifestyle asset from the plan.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void lifestyleAssetsGetByIdPlanidTest() throws ApiException {
        Integer id = null;
        String planId = null;
        LifestyleAssetModel response = api.lifestyleAssetsGetByIdPlanid(id, planId);
        // TODO: test validations
    }

    /**
     * Retrieve lifestyle assets
     *
     * This operation retrieves a list of all of the lifestyle assets in the plan.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void lifestyleAssetsGetByPlanidTest() throws ApiException {
        String planId = null;
        LifestyleAssetsModel response = api.lifestyleAssetsGetByPlanid(planId);
        // TODO: test validations
    }

}
