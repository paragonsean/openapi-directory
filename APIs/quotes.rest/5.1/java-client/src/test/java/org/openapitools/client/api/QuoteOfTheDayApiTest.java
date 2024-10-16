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
import org.openapitools.client.model.QODResponse;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for QuoteOfTheDayApi
 */
@Disabled
public class QuoteOfTheDayApiTest {

    private final QuoteOfTheDayApi api = new QuoteOfTheDayApi();

    /**
     * Gets a list of &#x60;Quote of the Day&#x60; Categories. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void qodCategoriesGetTest() throws ApiException {
        String language = null;
        Boolean detailed = null;
        api.qodCategoriesGet(language, detailed);
        // TODO: test validations
    }

    /**
     * Gets &#x60;Quote of the Day&#x60; (QOD). Optional &#x60;category&#x60; param determines the category of returned quote of the day 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void qodGetTest() throws ApiException {
        String category = null;
        String language = null;
        String id = null;
        QODResponse response = api.qodGet(category, language, id);
        // TODO: test validations
    }

    /**
     * Gets a list of supported languages for &#x60;Quote of the Day&#x60;.  
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void qodLanguagesGetTest() throws ApiException {
        api.qodLanguagesGet();
        // TODO: test validations
    }

}
