/*
 * DaniWeb Connect API
 * User Recommendation Engine and Chat Network
 *
 * The version of the OpenAPI document: 4
 * Contact: dani@daniwebmail.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.EndpointGetAudiences;
import org.openapitools.client.model.EndpointGetAudiencesID;
import org.openapitools.client.model.EndpointPostAudiencesIDMemberships;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for AudiencesApi
 */
@Disabled
public class AudiencesApiTest {

    private final AudiencesApi api = new AudiencesApi();

    /**
     * Fetch all Daniapp audience segments that comprise the current access token&#39;s bubble.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void audiencesGetTest() throws ApiException {
        Integer offset = null;
        Integer limit = null;
        EndpointGetAudiences response = api.audiencesGet(offset, limit);
        // TODO: test validations
    }

    /**
     * Fetch an array of Daniapp audience segments that comprise the current access token&#39;s bubble.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void audiencesIDGetTest() throws ApiException {
        List<Integer> ID = null;
        EndpointGetAudiencesID response = api.audiencesIDGet(ID);
        // TODO: test validations
    }

    /**
     * Create a membership record for the OAuth&#39;ed end-user based on the current audience segment/bubble combination.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void audiencesIDMembershipsPostTest() throws ApiException {
        Integer ID = null;
        EndpointPostAudiencesIDMemberships response = api.audiencesIDMembershipsPost(ID);
        // TODO: test validations
    }

}
