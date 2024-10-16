/*
 * Advicent.FactFinderService
 * An API for accessing the NaviPlan Fact Finder.
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
import org.openapitools.client.model.LifeInsurancePoliciesModel;
import org.openapitools.client.model.LifeInsurancePolicyModel;
import org.openapitools.client.model.LifeInsurancePolicySubaccountModel;
import org.openapitools.client.model.LifeInsurancePolicySubaccountWithIdModel;
import org.openapitools.client.model.LifeInsurancePolicySubaccountsModel;
import org.openapitools.client.model.LifeInsurancePolicyWithIdModel;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for LifeInsurancePoliciesApi
 */
@Disabled
public class LifeInsurancePoliciesApiTest {

    private final LifeInsurancePoliciesApi api = new LifeInsurancePoliciesApi();

    /**
     * Description: The operation removes a Life Insurance Policy tied to a Fact Finder.&lt;br /&gt;                Purpose: Allows for removal of a Life Insurance Policy and associated subaccounts from a Fact Finder.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void lifeInsurancePoliciesDeleteByIdTest() throws ApiException {
        Integer id = null;
        api.lifeInsurancePoliciesDeleteById(id);
        // TODO: test validations
    }

    /**
     * Description: Deletes an existing Life Insurance Policy Subaccount for an existing Life Insurance Policy.&lt;br /&gt;                Purpose: Allows for removal of a subaccount from a Life Insurance Policy.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void lifeInsurancePoliciesDeleteSubaccountByLifeinsurancepolicyidIdTest() throws ApiException {
        Integer lifeInsurancePolicyId = null;
        Integer id = null;
        api.lifeInsurancePoliciesDeleteSubaccountByLifeinsurancepolicyidId(lifeInsurancePolicyId, id);
        // TODO: test validations
    }

    /**
     * Description: This operation retrieves a single Life Insurance Policy for the specified Life Insurance Policy ID.&lt;br /&gt;                Purpose: Provides access to the Life Insurance Policy including description and policy type.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void lifeInsurancePoliciesGetByIdTest() throws ApiException {
        Integer id = null;
        LifeInsurancePolicyWithIdModel response = api.lifeInsurancePoliciesGetById(id);
        // TODO: test validations
    }

    /**
     * Description: This operation retrieves all Life Insurance Policies for the specified Fact Finder ID.&lt;br /&gt;                Purpose: Provides access to the Life Insurance Policies including description and policy type.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void lifeInsurancePoliciesGetLifeInsurancePoliciesByFactFinderIdByFactfinderidTest() throws ApiException {
        Integer factFinderId = null;
        LifeInsurancePoliciesModel response = api.lifeInsurancePoliciesGetLifeInsurancePoliciesByFactFinderIdByFactfinderid(factFinderId);
        // TODO: test validations
    }

    /**
     * Description: Get a specific subaccount for an existing Life Insurance Policy.&lt;br /&gt;                Purpose: Provides access to the Life Insurance Policy subaccount.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void lifeInsurancePoliciesGetSubaccountByLifeinsurancepolicyidIdTest() throws ApiException {
        Integer lifeInsurancePolicyId = null;
        Integer id = null;
        LifeInsurancePolicySubaccountWithIdModel response = api.lifeInsurancePoliciesGetSubaccountByLifeinsurancepolicyidId(lifeInsurancePolicyId, id);
        // TODO: test validations
    }

    /**
     * Description: Get all the subaccounts for an existing Life Insurance Policy.&lt;br /&gt;                Purpose: Provides access to all the Life Insurance Policy subaccounts.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void lifeInsurancePoliciesGetSubaccountsByLifeinsurancepolicyidTest() throws ApiException {
        Integer lifeInsurancePolicyId = null;
        LifeInsurancePolicySubaccountsModel response = api.lifeInsurancePoliciesGetSubaccountsByLifeinsurancepolicyid(lifeInsurancePolicyId);
        // TODO: test validations
    }

    /**
     * Description: The operation creates a Life Insurance Policy.&lt;br /&gt;                Purpose: Allows for creation of Life Insurance Policies on a Fact Finder.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void lifeInsurancePoliciesPostByModelTest() throws ApiException {
        LifeInsurancePolicyModel model = null;
        LifeInsurancePolicyWithIdModel response = api.lifeInsurancePoliciesPostByModel(model);
        // TODO: test validations
    }

    /**
     * Description: Creates a subaccount and adds it to an existing Life Insurance Policy.&lt;br /&gt;                Purpose: Allows for creation of subaccount on a Life Insurance Policy.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void lifeInsurancePoliciesPostSubaccountByLifeinsurancepolicyidModelTest() throws ApiException {
        Integer lifeInsurancePolicyId = null;
        LifeInsurancePolicySubaccountModel model = null;
        LifeInsurancePolicySubaccountWithIdModel response = api.lifeInsurancePoliciesPostSubaccountByLifeinsurancepolicyidModel(lifeInsurancePolicyId, model);
        // TODO: test validations
    }

    /**
     * Description: The operation updates a Life Insurance Policy, deletes associated sub-accounts if the policy type changes.&lt;br /&gt;                Purpose: Allows for complete replacement of a Life Insurance Policy on a Fact Finder.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void lifeInsurancePoliciesPutByIdModelTest() throws ApiException {
        Integer id = null;
        LifeInsurancePolicyModel model = null;
        LifeInsurancePolicyWithIdModel response = api.lifeInsurancePoliciesPutByIdModel(id, model);
        // TODO: test validations
    }

    /**
     * Description: Updates an existing Life Insurance Policy Subaccount for an existing Life Insurance Policy.&lt;br /&gt;                Purpose: Allows for complete replacement of a subaccount on a Life Insurance Policy.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void lifeInsurancePoliciesPutSubaccountByLifeinsurancepolicyidIdModelTest() throws ApiException {
        Integer lifeInsurancePolicyId = null;
        Integer id = null;
        LifeInsurancePolicySubaccountModel model = null;
        LifeInsurancePolicySubaccountModel response = api.lifeInsurancePoliciesPutSubaccountByLifeinsurancepolicyidIdModel(lifeInsurancePolicyId, id, model);
        // TODO: test validations
    }

}
