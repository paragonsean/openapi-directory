/*
 * NBA v3 RotoBaller Articles
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.Article;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for DefaultApi
 */
@Disabled
public class DefaultApiTest {

    private final DefaultApi api = new DefaultApi();

    /**
     * RotoBaller Articles
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void rotoballerArticlesTest() throws ApiException {
        String format = null;
        List<Article> response = api.rotoballerArticles(format);
        // TODO: test validations
    }

    /**
     * RotoBaller Articles by Date
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void rotoballerArticlesByDateTest() throws ApiException {
        String format = null;
        String date = null;
        List<Article> response = api.rotoballerArticlesByDate(format, date);
        // TODO: test validations
    }

    /**
     * RotoBaller Articles by Player
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void rotoballerArticlesByPlayerTest() throws ApiException {
        String format = null;
        String playerid = null;
        List<Article> response = api.rotoballerArticlesByPlayer(format, playerid);
        // TODO: test validations
    }

}
