/*
 * eNanoMapper database
 * AMBIT REST web services [eNanoMapper profile] with free text & faceted search
 *
 * The version of the OpenAPI document: 4.0.0
 * Contact: support@ideaconsult.net
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.SolrResponse;
import org.openapitools.client.model.SolrqueryPostRequest;
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
     * Apache Solr powered search
     *
     * GET is simpler to use, but imposes restrictions on the complexity and the lenght of the parameters.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void solrqueryGetTest() throws ApiException {
        String q = null;
        String fq = null;
        String fl = null;
        Integer start = null;
        Integer rows = null;
        String wt = null;
        SolrResponse response = api.solrqueryGet(q, fq, fl, start, rows, wt);
        // TODO: test validations
    }

    /**
     * Apache Solr powered search
     *
     * POST is more complex to use, but also allows for much for complex and lengthy queries.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void solrqueryPostTest() throws ApiException {
        String wt = null;
        SolrqueryPostRequest solrqueryPostRequest = null;
        SolrResponse response = api.solrqueryPost(wt, solrqueryPostRequest);
        // TODO: test validations
    }

}
