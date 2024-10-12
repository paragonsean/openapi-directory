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
import org.openapitools.client.model.EndpointGetMarkdownEmoticons;
import org.openapitools.client.model.EndpointPostMarkdown;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for MarkdownApi
 */
@Disabled
public class MarkdownApiTest {

    private final MarkdownApi api = new MarkdownApi();

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void markdownEmoticonsGetTest() throws ApiException {
        EndpointGetMarkdownEmoticons response = api.markdownEmoticonsGet();
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void markdownPostTest() throws ApiException {
        String textRaw = null;
        Boolean textEmoticons = null;
        EndpointPostMarkdown response = api.markdownPost(textRaw, textEmoticons);
        // TODO: test validations
    }

}
