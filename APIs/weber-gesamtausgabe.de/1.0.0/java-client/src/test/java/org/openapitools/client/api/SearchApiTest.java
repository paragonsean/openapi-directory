/*
 * WeGA API
 * ⚠️<b>DEPRECATION WARNING</b>⚠️<br/>This version of the WeGA API specification is outdated and superseded by [version 1.1.0](https://weber-gesamtausgabe.de/api/v1/openapi.json).  <br/> <br/> For feedback or requests about this API please contact stadler@weber-gesamtausgabe.de or start the discussion at https://github.com/Edirom/WeGA-WebApp
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.Document;
import org.openapitools.client.model.Error;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for SearchApi
 */
@Disabled
public class SearchApiTest {

    private final SearchApi api = new SearchApi();

    /**
     * Search for a WeGA entity
     *
     * This endpoint returns the search results for an entity&#39;s name or title. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void searchEntityGetTest() throws ApiException {
        List<String> docType = null;
        String q = null;
        Integer offset = null;
        Integer limit = null;
        List<Document> response = api.searchEntityGet(docType, q, offset, limit);
        // TODO: test validations
    }

}
