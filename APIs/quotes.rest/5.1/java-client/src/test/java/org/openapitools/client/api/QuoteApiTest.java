/*
 * They Said So Quotes API
 *  They Said So Quotes API offers a complete feature rich REST API access to its quotes platform.  This is the documentation for the world famous [quotes API](https://theysaidso.com/api).  If you are a subscriber and you are trying this from a console you can use Bearer token with your api key as the token. You can test and play with the API right here on this web page. Please note recently we closed downs public access without api key to prevent abuse. The public routes are still available to use free of charge but requires a api token. You can get one for free at our website. For using the private end points and subscribing to the API please visit [https://theysaidso.com/api](https://theysaidso.com/api).
 *
 * The version of the OpenAPI document: 5.1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.QuoteResponse;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for QuoteApi
 */
@Disabled
public class QuoteApiTest {

    private final QuoteApi api = new QuoteApi();

    /**
     * Gets a list of popular author names in the system.  
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void quoteAuthorsPopularGetTest() throws ApiException {
        String language = null;
        Boolean detailed = null;
        Integer start = null;
        Integer limit = null;
        api.quoteAuthorsPopularGet(language, detailed, start, limit);
        // TODO: test validations
    }

    /**
     * Gets a list of author names in the system.  
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void quoteAuthorsSearchGetTest() throws ApiException {
        String query = null;
        String language = null;
        Boolean detailed = null;
        Integer start = null;
        Integer limit = null;
        api.quoteAuthorsSearchGet(query, language, detailed, start, limit);
        // TODO: test validations
    }

    /**
     * Toggle the user bookmark of the given Quote as a user of the API Key.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void quoteBookmarkToggleGetTest() throws ApiException {
        String quoteId = null;
        api.quoteBookmarkToggleGet(quoteId);
        // TODO: test validations
    }

    /**
     * Gets a list of popular &#x60;Quote&#x60; Categories. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void quoteCategoriesPopularGetTest() throws ApiException {
        Integer start = null;
        Integer limit = null;
        api.quoteCategoriesPopularGet(start, limit);
        // TODO: test validations
    }

    /**
     * Gets a list of &#x60;Quote&#x60; Categories matching the query string. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void quoteCategoriesSearchGetTest() throws ApiException {
        String query = null;
        Integer start = null;
        Integer limit = null;
        api.quoteCategoriesSearchGet(query, start, limit);
        // TODO: test validations
    }

    /**
     * Gets a &#x60;Quote&#x60; with a given &#x60;id&#x60;.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void quoteGetTest() throws ApiException {
        String id = null;
        QuoteResponse response = api.quoteGet(id);
        // TODO: test validations
    }

    /**
     * Toggle the user like of the given Quote as a user of the API Key.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void quoteLikeToggleGetTest() throws ApiException {
        String quoteId = null;
        api.quoteLikeToggleGet(quoteId);
        // TODO: test validations
    }

    /**
     * Gets a &#x60;Random Quote&#x60;. When you are in a hurry this is what you call to get a random famous quote.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void quoteRandomGetTest() throws ApiException {
        String language = null;
        Integer limit = null;
        QuoteResponse response = api.quoteRandomGet(language, limit);
        // TODO: test validations
    }

    /**
     * Search for a &#x60;Quote&#x60; in They Said So platform. Optional &#x60;category&#x60; , &#x60;author&#x60;, &#x60;minlength&#x60;, &#x60;maxlength&#x60; params determines the filters applied while searching for the quote. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void quoteSearchGetTest() throws ApiException {
        String category = null;
        String author = null;
        Integer minlength = null;
        Integer maxlength = null;
        String query = null;
        Boolean _private = null;
        String language = null;
        Integer limit = null;
        Boolean sfw = null;
        QuoteResponse response = api.quoteSearchGet(category, author, minlength, maxlength, query, _private, language, limit, sfw);
        // TODO: test validations
    }

}
