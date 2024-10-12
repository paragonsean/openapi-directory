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
import org.openapitools.client.model.PhraseResponseVersion;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for PhrasesApi
 */
@Disabled
public class PhrasesApiTest {

    private final PhrasesApi api = new PhrasesApi();

    /**
     * Add sentiment-bearing phrases
     *
     * This method adds sentiment-bearing phrases on Semantria side.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void addPhrasesTest() throws ApiException {
        String contentType = null;
        Object sentimentPhrases = null;
        String configId = null;
        List<PhraseResponseVersion> response = api.addPhrases(contentType, sentimentPhrases, configId);
        // TODO: test validations
    }

    /**
     * Remove sentiment-bearing phrases
     *
     * This method removes certain sentiment-bearing phrases by their names on Semantria side.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deletePhrasesTest() throws ApiException {
        String contentType = null;
        List<String> sentimentPhraseIDs = null;
        String configId = null;
        api.deletePhrases(contentType, sentimentPhraseIDs, configId);
        // TODO: test validations
    }

    /**
     * Retrieve sentiment-bearing phrases
     *
     * This method retrieves list of sentiment-bearing phrases available on Semantria side.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getPhrasesTest() throws ApiException {
        String contentType = null;
        String configId = null;
        List<PhraseResponseVersion> response = api.getPhrases(contentType, configId);
        // TODO: test validations
    }

    /**
     * Updates sentiment-bearing phrases
     *
     * This method updates sentiment-bearing phrases by unique IDs on Semantria side.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updatePhrasesTest() throws ApiException {
        String contentType = null;
        Object sentimentPhrases = null;
        String configId = null;
        List<PhraseResponseVersion> response = api.updatePhrases(contentType, sentimentPhrases, configId);
        // TODO: test validations
    }

}
