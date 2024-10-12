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
import org.openapitools.client.model.CategoryResponseVersion;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for CategoriesApi
 */
@Disabled
public class CategoriesApiTest {

    private final CategoriesApi api = new CategoriesApi();

    /**
     * Add user categories
     *
     * This method adds user categories on Semantria side.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void addCategoriesTest() throws ApiException {
        String contentType = null;
        Object categories = null;
        String configId = null;
        List<CategoryResponseVersion> response = api.addCategories(contentType, categories, configId);
        // TODO: test validations
    }

    /**
     * Remove user categories
     *
     * This method removes certain user categories by their IDs on Semantria side.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteCategoriesTest() throws ApiException {
        String contentType = null;
        List<String> categoryIDs = null;
        String configId = null;
        api.deleteCategories(contentType, categoryIDs, configId);
        // TODO: test validations
    }

    /**
     * Retrieve user categories
     *
     * This method retrieves list of user categories available on Semantria side.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getCategoriesTest() throws ApiException {
        String contentType = null;
        String configId = null;
        List<CategoryResponseVersion> response = api.getCategories(contentType, configId);
        // TODO: test validations
    }

    /**
     * Updates user categories
     *
     * This method updates user categories by unique IDs on Semantria side.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateCategoriesTest() throws ApiException {
        String contentType = null;
        Object categories = null;
        String configId = null;
        List<CategoryResponseVersion> response = api.updateCategories(contentType, categories, configId);
        // TODO: test validations
    }

}
