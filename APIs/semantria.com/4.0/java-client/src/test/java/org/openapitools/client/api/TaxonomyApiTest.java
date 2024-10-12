/*
 * Semantria
 * Semantria applies Text and Sentiment Analysis to tweets, facebook posts, surveys, reviews or enterprise content.
 *
 * The version of the OpenAPI document: 4.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.TaxonomyNodeResponseVersion;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for TaxonomyApi
 */
@Disabled
public class TaxonomyApiTest {

    private final TaxonomyApi api = new TaxonomyApi();

    /**
     * Add taxonomy nodes
     *
     * This method adds taxonomy nodes on Semantria side.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void addTaxonomyTest() throws ApiException {
        String contentType = null;
        Object taxonomy = null;
        String configId = null;
        List<TaxonomyNodeResponseVersion> response = api.addTaxonomy(contentType, taxonomy, configId);
        // TODO: test validations
    }

    /**
     * Remove taxonomy nodes
     *
     * This method removes certain taxonomy nodes by their IDs on Semantria side.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteTaxonomyTest() throws ApiException {
        String contentType = null;
        List<String> taxonomyNodeIDs = null;
        String configId = null;
        api.deleteTaxonomy(contentType, taxonomyNodeIDs, configId);
        // TODO: test validations
    }

    /**
     * Retrieve taxonomy
     *
     * This method retrieves list of taxonomy available on Semantria side.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getTaxonomyTest() throws ApiException {
        String contentType = null;
        String configId = null;
        List<TaxonomyNodeResponseVersion> response = api.getTaxonomy(contentType, configId);
        // TODO: test validations
    }

    /**
     * Update taxonomy nodes
     *
     * This method updates taxonomy nodes on Semantria side.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateTaxonomyTest() throws ApiException {
        String contentType = null;
        Object taxonomy = null;
        String configId = null;
        List<TaxonomyNodeResponseVersion> response = api.updateTaxonomy(contentType, taxonomy, configId);
        // TODO: test validations
    }

}
