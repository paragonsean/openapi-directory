/*
 * TrainingApi
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import java.io.File;
import org.openapitools.client.model.ImagePrediction;
import org.openapitools.client.model.ImageUrl;
import org.openapitools.client.model.PredictionQueryResult;
import org.openapitools.client.model.PredictionQueryToken;
import java.util.UUID;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for PredictionsApiApi
 */
@Disabled
public class PredictionsApiApiTest {

    private final PredictionsApiApi api = new PredictionsApiApi();

    /**
     * Delete a set of predicted images and their associated prediction results
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deletePredictionTest() throws ApiException {
        UUID projectId = null;
        List<String> ids = null;
        String trainingKey = null;
        api.deletePrediction(projectId, ids, trainingKey);
        // TODO: test validations
    }

    /**
     * Get images that were sent to your prediction endpoint
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void queryPredictionsTest() throws ApiException {
        UUID projectId = null;
        String trainingKey = null;
        PredictionQueryToken predictionQueryToken = null;
        PredictionQueryResult response = api.queryPredictions(projectId, trainingKey, predictionQueryToken);
        // TODO: test validations
    }

    /**
     * Quick test an image
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void quickTestImageTest() throws ApiException {
        UUID projectId = null;
        String trainingKey = null;
        File imageData = null;
        UUID iterationId = null;
        ImagePrediction response = api.quickTestImage(projectId, trainingKey, imageData, iterationId);
        // TODO: test validations
    }

    /**
     * Quick test an image url
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void quickTestImageUrlTest() throws ApiException {
        UUID projectId = null;
        String trainingKey = null;
        ImageUrl imageUrl = null;
        UUID iterationId = null;
        ImagePrediction response = api.quickTestImageUrl(projectId, trainingKey, imageUrl, iterationId);
        // TODO: test validations
    }

}
