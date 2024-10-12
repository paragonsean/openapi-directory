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
import org.openapitools.client.model.ImageRegionProposal;
import java.util.UUID;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for ImageRegionProposalApiApi
 */
@Disabled
public class ImageRegionProposalApiApiTest {

    private final ImageRegionProposalApiApi api = new ImageRegionProposalApiApi();

    /**
     * Get region proposals for an image. Returns empty array if no proposals are found.
     *
     * This API will get region proposals for an image along with confidences for the region. It returns an empty array if no proposals are found.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getImageRegionProposalsTest() throws ApiException {
        UUID projectId = null;
        UUID imageId = null;
        String trainingKey = null;
        ImageRegionProposal response = api.getImageRegionProposals(projectId, imageId, trainingKey);
        // TODO: test validations
    }

}
